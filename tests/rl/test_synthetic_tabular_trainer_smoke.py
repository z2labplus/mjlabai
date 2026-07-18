from __future__ import annotations

from dataclasses import FrozenInstanceError, asdict, replace
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.synthetic_tabular_trainer_smoke as trainer_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    MAX_SYNTHETIC_TABULAR_TRAINING_PASSES,
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION,
    SyntheticPolicyTableEntry,
    SyntheticPolicyTableUpdateSmokeError,
    SyntheticPolicyUpdateInput,
    SyntheticTabularTrainerSmokeError,
    SyntheticTabularTrainingResult,
    train_synthetic_policy_table_smoke,
)


def _record(**overrides: object) -> SyntheticPolicyUpdateInput:
    values: dict[str, object] = {
        "record_id": "trainer-pass1:0001",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "state_id": "synthetic-state:a",
        "action_id": "discard-1m",
        "current_action_value": 2.0,
        "reward": 1.0,
        "next_max_action_value": 4.0,
        "terminal": False,
        "project_authored": True,
        "synthetic": True,
        "local_only": True,
        "uses_real_data": False,
        "uses_external_log": False,
        "uses_platform_data": False,
        "uses_model_output": False,
        "uses_self_play": False,
    }
    values.update(overrides)
    return SyntheticPolicyUpdateInput(**values)  # type: ignore[arg-type]


def _first_trace() -> tuple[
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
]:
    return (
        _record(),
        _record(
            record_id="trainer-pass1:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=10.0,
            reward=2.0,
            next_max_action_value=6.0,
        ),
        _record(
            record_id="trainer-pass1:0003",
            current_action_value=3.0,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id="trainer-pass1:0004",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=8.25,
            reward=4.25,
            next_max_action_value=None,
            terminal=True,
        ),
    )


def _second_trace() -> tuple[
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
]:
    return (
        _record(
            record_id="trainer-pass2:0001",
            current_action_value=4.0,
            reward=0.0,
            next_max_action_value=8.0,
        ),
        _record(
            record_id="trainer-pass2:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=6.25,
            reward=1.0,
            next_max_action_value=3.0,
        ),
        _record(
            record_id="trainer-pass2:0003",
            current_action_value=5.0,
            reward=7.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id="trainer-pass2:0004",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=4.75,
            reward=2.75,
            next_max_action_value=None,
            terminal=True,
        ),
    )


def _noop_trace(pass_index: int) -> tuple[
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
]:
    prefix = f"trainer-noop-{pass_index}"
    return (
        _record(
            record_id=f"{prefix}:0001",
            reward=2.0,
            next_max_action_value=0.0,
        ),
        _record(
            record_id=f"{prefix}:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=10.0,
            reward=10.0,
            next_max_action_value=0.0,
        ),
        _record(
            record_id=f"{prefix}:0003",
            current_action_value=2.0,
            reward=2.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id=f"{prefix}:0004",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=10.0,
            reward=10.0,
            next_max_action_value=None,
            terminal=True,
        ),
    )


def _entries() -> tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]:
    return (
        SyntheticPolicyTableEntry("synthetic-state:a", "discard-1m", 2.0),
        SyntheticPolicyTableEntry("synthetic-state:b", "discard-2p", 10.0),
    )


class SyntheticTabularTrainerSmokeTests(unittest.TestCase):
    def test_exact_one_pass_training_output(self) -> None:
        result = train_synthetic_policy_table_smoke(
            _entries(), (_first_trace(),), learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(result.pass_count, 1)
        self.assertEqual(len(result.pass_results), 1)
        self.assertEqual(
            tuple(entry.action_value for entry in result.final_entries),
            (4.0, 6.25),
        )
        self.assertEqual(len(result.record_ids), 4)

    def test_exact_two_pass_training_output(self) -> None:
        result = train_synthetic_policy_table_smoke(
            _entries(),
            (_first_trace(), _second_trace()),
            learning_rate=0.5,
            discount_factor=0.75,
        )

        self.assertEqual(
            tuple(entry.action_value for entry in result.initial_entries),
            (2.0, 10.0),
        )
        self.assertEqual(
            tuple(
                entry.action_value
                for entry in result.pass_results[0].final_entries
            ),
            (4.0, 6.25),
        )
        self.assertEqual(
            tuple(entry.action_value for entry in result.final_entries),
            (6.0, 3.75),
        )

    def test_enforces_lower_and_upper_pass_limits(self) -> None:
        with self.assertRaises(SyntheticTabularTrainerSmokeError):
            train_synthetic_policy_table_smoke(
                _entries(), (), learning_rate=0.5, discount_factor=0.75
            )
        with self.assertRaises(SyntheticTabularTrainerSmokeError):
            train_synthetic_policy_table_smoke(
                _entries(),
                tuple(_noop_trace(index) for index in range(1, 10)),
                learning_rate=0.5,
                discount_factor=0.75,
            )

        result = train_synthetic_policy_table_smoke(
            _entries(),
            tuple(_noop_trace(index) for index in range(1, 9)),
            learning_rate=0.5,
            discount_factor=0.75,
        )
        self.assertEqual(result.pass_count, 8)
        self.assertEqual(result.max_passes, 8)
        self.assertEqual(len(result.record_ids), 32)

    def test_requires_exact_outer_tuple(self) -> None:
        traces = (_first_trace(),)

        class TupleSubclass(tuple):
            pass

        invalid_inputs = (
            list(traces),
            {"traces": traces},
            (trace for trace in traces),
            "traces",
            b"traces",
            bytearray(b"traces"),
            TupleSubclass(traces),
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(SyntheticTabularTrainerSmokeError):
                    train_synthetic_policy_table_smoke(  # type: ignore[arg-type]
                        _entries(),
                        value,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_inner_errors_are_wrapped_with_pass_index_and_cause(self) -> None:
        first, second = _first_trace(), _second_trace()
        cases = (
            (1, (list(first), second)),
            (2, (first, (replace(second[0], uses_external_log=True),) + second[1:])),
        )
        for pass_index, traces in cases:
            with self.subTest(pass_index=pass_index):
                with self.assertRaisesRegex(
                    SyntheticTabularTrainerSmokeError,
                    f"pass {pass_index} failed",
                ) as context:
                    train_synthetic_policy_table_smoke(  # type: ignore[arg-type]
                        _entries(),
                        traces,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )
                self.assertIsInstance(
                    context.exception.__cause__,
                    SyntheticPolicyTableUpdateSmokeError,
                )

    def test_requires_table_state_continuity_for_both_keys(self) -> None:
        first, second = _first_trace(), _second_trace()
        replacements = (
            replace(second[0], current_action_value=4.000000000000001),
            replace(second[1], current_action_value=6.250000000000001),
        )
        for key_index, replacement in enumerate(replacements, start=1):
            bad_second = list(second)
            bad_second[key_index - 1] = replacement
            with self.subTest(key_index=key_index):
                with self.assertRaisesRegex(
                    SyntheticTabularTrainerSmokeError,
                    "pass 2 failed",
                ):
                    train_synthetic_policy_table_smoke(
                        _entries(),
                        (first, tuple(bad_second)),  # type: ignore[arg-type]
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_rejects_duplicate_record_ids_across_passes(self) -> None:
        first, second = _first_trace(), _second_trace()
        bad_second = (
            replace(second[0], record_id=first[2].record_id),
        ) + second[1:]

        with self.assertRaisesRegex(
            SyntheticTabularTrainerSmokeError,
            "record_ids across all passes",
        ):
            train_synthetic_policy_table_smoke(
                _entries(),
                (first, bad_second),
                learning_rate=0.5,
                discount_factor=0.75,
            )

    def test_helper_call_count_matches_ordered_pass_count_without_formula_copy(self) -> None:
        traces = tuple(_noop_trace(index) for index in range(1, 5))
        with patch.object(
            trainer_module,
            "apply_synthetic_policy_table_update_smoke",
            wraps=trainer_module.apply_synthetic_policy_table_update_smoke,
        ) as table_helper:
            result = train_synthetic_policy_table_smoke(
                _entries(), traces, learning_rate=0.5, discount_factor=0.75
            )
        self.assertEqual(table_helper.call_count, 4)
        self.assertEqual(
            tuple(call.args[1] for call in table_helper.call_args_list),
            traces,
        )
        self.assertEqual(result.pass_count, 4)
        source = inspect.getsource(trainer_module)
        for duplicated_formula in (
            "target_value =",
            "td_error =",
            "updated_action_value =",
        ):
            self.assertNotIn(duplicated_formula, source)

    def test_repeated_output_is_equal_and_inputs_are_immutable(self) -> None:
        entries = _entries()
        traces = (_first_trace(), _second_trace())
        before_entries = tuple(asdict(entry) for entry in entries)
        before_traces = tuple(
            tuple(asdict(record) for record in trace) for trace in traces
        )

        first = train_synthetic_policy_table_smoke(
            entries, traces, learning_rate=0.5, discount_factor=0.75
        )
        second = train_synthetic_policy_table_smoke(
            entries, traces, learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(first, second)
        self.assertEqual(tuple(asdict(entry) for entry in entries), before_entries)
        self.assertEqual(
            tuple(tuple(asdict(record) for record in trace) for trace in traces),
            before_traces,
        )
        with self.assertRaises(FrozenInstanceError):
            first.pass_count = 3  # type: ignore[misc]

    def test_result_has_exact_fields_counts_grade_and_warnings(self) -> None:
        result = train_synthetic_policy_table_smoke(
            _entries(),
            (_first_trace(), _second_trace()),
            learning_rate=0.5,
            discount_factor=0.75,
        )

        self.assertIsInstance(result, SyntheticTabularTrainingResult)
        self.assertEqual(
            set(asdict(result)),
            {
                "trainer_version",
                "pass_count",
                "max_passes",
                "initial_entries",
                "final_entries",
                "pass_results",
                "record_ids",
                "training_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(result.trainer_version, SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION)
        self.assertEqual(result.max_passes, MAX_SYNTHETIC_TABULAR_TRAINING_PASSES)
        self.assertEqual(result.pass_count, len(result.pass_results))
        self.assertEqual(len(result.record_ids), 4 * result.pass_count)
        self.assertEqual(len(set(result.record_ids)), len(result.record_ids))
        self.assertEqual(
            result.evidence_grade,
            "P8 bounded synthetic/local tabular training-loop smoke evidence only",
        )
        self.assertTrue(result.training_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "bounded synthetic/local tabular training smoke only",
            "maximum eight ordered in-memory passes",
            "no shuffle, minibatch, optimizer, checkpoint or resume",
            "not a model or network training system",
            "not an environment, episode, replay buffer or self-play",
            "not production training or evaluation",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_exports_and_public_surface_are_narrow(self) -> None:
        self.assertIs(
            train_synthetic_policy_table_smoke,
            trainer_module.train_synthetic_policy_table_smoke,
        )
        self.assertEqual(
            set(trainer_module.__all__),
            {
                "MAX_SYNTHETIC_TABULAR_TRAINING_PASSES",
                "SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION",
                "SyntheticTabularTrainerSmokeError",
                "SyntheticTabularTrainingResult",
                "train_synthetic_policy_table_smoke",
            },
        )
        public_text = " ".join(trainer_module.__all__).lower()
        for forbidden in (
            "path",
            "file",
            "persistence",
            "environment",
            "replay",
            "self_play",
            "network",
            "optimizer",
            "checkpoint",
            "evaluation",
        ):
            self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
