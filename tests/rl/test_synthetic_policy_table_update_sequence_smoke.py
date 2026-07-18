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

import mjlabai.rl.synthetic_policy_table_update_sequence_smoke as sequence_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION,
    SyntheticPolicyTableEntry,
    SyntheticPolicyTableUpdateSequenceResult,
    SyntheticPolicyTableUpdateSequenceSmokeError,
    SyntheticPolicyTableUpdateSmokeError,
    SyntheticPolicyUpdateInput,
    apply_synthetic_policy_table_update_sequence_smoke,
)


def _record(**overrides: object) -> SyntheticPolicyUpdateInput:
    values: dict[str, object] = {
        "record_id": "p8-sequence-pass1:0001",
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
            record_id="p8-sequence-pass1:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=10.0,
            reward=2.0,
            next_max_action_value=6.0,
        ),
        _record(
            record_id="p8-sequence-pass1:0003",
            current_action_value=3.0,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id="p8-sequence-pass1:0004",
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
            record_id="p8-sequence-pass2:0001",
            current_action_value=4.0,
            reward=0.0,
            next_max_action_value=8.0,
        ),
        _record(
            record_id="p8-sequence-pass2:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=6.25,
            reward=1.0,
            next_max_action_value=3.0,
        ),
        _record(
            record_id="p8-sequence-pass2:0003",
            current_action_value=5.0,
            reward=7.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id="p8-sequence-pass2:0004",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=4.75,
            reward=2.75,
            next_max_action_value=None,
            terminal=True,
        ),
    )


def _entries() -> tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]:
    return (
        SyntheticPolicyTableEntry("synthetic-state:a", "discard-1m", 2.0),
        SyntheticPolicyTableEntry("synthetic-state:b", "discard-2p", 10.0),
    )


def _traces() -> tuple[
    tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
    tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
]:
    return (_first_trace(), _second_trace())


class SyntheticPolicyTableUpdateSequenceSmokeTests(unittest.TestCase):
    def test_exact_two_pass_intermediate_and_final_values(self) -> None:
        result = apply_synthetic_policy_table_update_sequence_smoke(
            _entries(), _traces(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertIsInstance(result, SyntheticPolicyTableUpdateSequenceResult)
        self.assertEqual(
            tuple(entry.action_value for entry in result.initial_entries),
            (2.0, 10.0),
        )
        self.assertEqual(
            tuple(entry.action_value for entry in result.intermediate_entries),
            (4.0, 6.25),
        )
        self.assertEqual(
            tuple(entry.action_value for entry in result.final_entries),
            (6.0, 3.75),
        )

    def test_requires_exact_two_trace_outer_tuple(self) -> None:
        traces = _traces()

        class TupleSubclass(tuple):
            pass

        invalid_inputs = (
            list(traces),
            {"traces": traces},
            (trace for trace in traces),
            "two-traces",
            b"two-traces",
            bytearray(b"two-traces"),
            TupleSubclass(traces),
            traces[:1],
            traces + (traces[-1],),
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(SyntheticPolicyTableUpdateSequenceSmokeError):
                    apply_synthetic_policy_table_update_sequence_smoke(  # type: ignore[arg-type]
                        _entries(),
                        value,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_inner_trace_errors_are_pass_indexed(self) -> None:
        first, second = _traces()
        cases = (
            (1, (list(first), second)),
            (2, (first, list(second))),
        )
        for pass_index, traces in cases:
            with self.subTest(pass_index=pass_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyTableUpdateSequenceSmokeError,
                    f"pass {pass_index} failed",
                ) as context:
                    apply_synthetic_policy_table_update_sequence_smoke(  # type: ignore[arg-type]
                        _entries(),
                        traces,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )
                self.assertIsInstance(
                    context.exception.__cause__,
                    SyntheticPolicyTableUpdateSmokeError,
                )

    def test_requires_exact_pass_continuity_for_both_keys(self) -> None:
        first, second = _traces()
        cases = (
            replace(second[0], current_action_value=4.000000000000001),
            replace(second[1], current_action_value=6.250000000000001),
        )
        for key_index, replacement in enumerate(cases, start=1):
            bad_second = list(second)
            bad_second[key_index - 1] = replacement
            with self.subTest(key_index=key_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyTableUpdateSequenceSmokeError,
                    "pass 2 failed",
                ):
                    apply_synthetic_policy_table_update_sequence_smoke(
                        _entries(),
                        (first, tuple(bad_second)),  # type: ignore[arg-type]
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_requires_pairwise_distinct_ids_across_both_passes(self) -> None:
        first, second = _traces()
        bad_second = (
            replace(second[0], record_id=first[3].record_id),
        ) + second[1:]

        with self.assertRaisesRegex(
            SyntheticPolicyTableUpdateSequenceSmokeError,
            "record_ids across both passes",
        ):
            apply_synthetic_policy_table_update_sequence_smoke(
                _entries(),
                (first, bad_second),
                learning_rate=0.5,
                discount_factor=0.75,
            )

    def test_table_helper_is_reused_exactly_twice_without_duplicate_formula(self) -> None:
        with patch.object(
            sequence_module,
            "apply_synthetic_policy_table_update_smoke",
            wraps=sequence_module.apply_synthetic_policy_table_update_smoke,
        ) as table_helper:
            apply_synthetic_policy_table_update_sequence_smoke(
                _entries(), _traces(), learning_rate=0.5, discount_factor=0.75
            )
        self.assertEqual(table_helper.call_count, 2)
        source = inspect.getsource(sequence_module)
        for duplicated_formula in (
            "target_value =",
            "td_error =",
            "updated_action_value =",
        ):
            self.assertNotIn(duplicated_formula, source)

    def test_table_errors_are_wrapped_for_both_passes_with_cause(self) -> None:
        first, second = _traces()
        cases = (
            (1, (replace(first[0], uses_real_data=True),) + first[1:], second),
            (2, first, (replace(second[0], uses_external_log=True),) + second[1:]),
        )
        for case in cases:
            pass_index = case[0]
            traces = (case[1], case[2])
            with self.subTest(pass_index=pass_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyTableUpdateSequenceSmokeError,
                    f"pass {pass_index} failed",
                ) as context:
                    apply_synthetic_policy_table_update_sequence_smoke(
                        _entries(),
                        traces,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )
                self.assertIsInstance(
                    context.exception.__cause__,
                    SyntheticPolicyTableUpdateSmokeError,
                )

    def test_repeated_output_is_equal_and_inputs_are_immutable(self) -> None:
        entries = _entries()
        traces = _traces()
        before_entries = tuple(asdict(entry) for entry in entries)
        before_traces = tuple(
            tuple(asdict(record) for record in trace) for trace in traces
        )

        first = apply_synthetic_policy_table_update_sequence_smoke(
            entries, traces, learning_rate=0.5, discount_factor=0.75
        )
        second = apply_synthetic_policy_table_update_sequence_smoke(
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

    def test_result_is_frozen_and_has_exact_safe_fields(self) -> None:
        result = apply_synthetic_policy_table_update_sequence_smoke(
            _entries(), _traces(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(
            set(asdict(result)),
            {
                "sequence_version",
                "pass_count",
                "initial_entries",
                "intermediate_entries",
                "final_entries",
                "pass_results",
                "sequence_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.sequence_version,
            SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION,
        )
        self.assertEqual(result.pass_count, 2)
        self.assertEqual(len(result.pass_results), 2)
        self.assertEqual(
            result.evidence_grade,
            "P8 synthetic/local fixed two-pass policy-table update sequence "
            "smoke evidence only",
        )
        self.assertTrue(result.sequence_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local fixed two-pass policy-table update sequence smoke only",
            "not a variable epoch, trainer or production training loop",
            "not a persistent policy, model or checkpoint",
            "not an environment, episode or replay buffer",
            "not self-play",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_public_imports_are_available_from_rl_package(self) -> None:
        self.assertIs(
            apply_synthetic_policy_table_update_sequence_smoke,
            sequence_module.apply_synthetic_policy_table_update_sequence_smoke,
        )
        self.assertIs(
            SyntheticPolicyTableUpdateSequenceResult,
            sequence_module.SyntheticPolicyTableUpdateSequenceResult,
        )

    def test_public_surface_is_narrow(self) -> None:
        self.assertEqual(
            set(sequence_module.__all__),
            {
                "SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION",
                "SyntheticPolicyTableUpdateSequenceResult",
                "SyntheticPolicyTableUpdateSequenceSmokeError",
                "apply_synthetic_policy_table_update_sequence_smoke",
            },
        )
        public_text = " ".join(sequence_module.__all__).lower()
        for forbidden in (
            "third_pass",
            "epoch",
            "trainer",
            "mapping",
            "persistence",
            "path",
            "fixture",
            "environment",
            "replay",
            "self_play",
            "model",
            "optimizer",
            "training",
        ):
            self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
