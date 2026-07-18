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

import mjlabai.rl.synthetic_policy_update_trace_smoke as trace_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateSmokeError,
    SyntheticPolicyUpdateTraceResult,
    SyntheticPolicyUpdateTraceSmokeError,
    apply_synthetic_policy_update_trace_smoke,
)


def _record(**overrides: object) -> SyntheticPolicyUpdateInput:
    values: dict[str, object] = {
        "record_id": "p8-trace-record:0001",
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


def _trace() -> tuple[
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
]:
    return (
        _record(),
        _record(
            record_id="p8-trace-record:0002",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=10.0,
            reward=2.0,
            next_max_action_value=6.0,
        ),
        _record(
            record_id="p8-trace-record:0003",
            current_action_value=3.0,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
        ),
        _record(
            record_id="p8-trace-record:0004",
            state_id="synthetic-state:b",
            action_id="discard-2p",
            current_action_value=8.25,
            reward=4.25,
            next_max_action_value=None,
            terminal=True,
        ),
    )


class SyntheticPolicyUpdateTraceSmokeTests(unittest.TestCase):
    def test_exact_interleaved_formulas_and_final_values(self) -> None:
        result = apply_synthetic_policy_update_trace_smoke(
            _trace(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertIsInstance(result, SyntheticPolicyUpdateTraceResult)
        step_1, step_2, step_3, step_4 = result.step_results
        self.assertEqual(
            (step_1.target_value, step_1.td_error, step_1.updated_action_value),
            (4.0, 2.0, 3.0),
        )
        self.assertEqual(
            (step_2.target_value, step_2.td_error, step_2.updated_action_value),
            (6.5, -3.5, 8.25),
        )
        self.assertEqual(
            (step_3.target_value, step_3.td_error, step_3.updated_action_value),
            (5.0, 2.0, 4.0),
        )
        self.assertEqual(
            (step_4.target_value, step_4.td_error, step_4.updated_action_value),
            (4.25, -4.0, 6.25),
        )
        self.assertEqual(result.initial_action_values, (2.0, 10.0))
        self.assertEqual(result.intermediate_action_values, (3.0, 8.25))
        self.assertEqual(result.final_action_values, (4.0, 6.25))

    def test_requires_exact_four_record_tuple(self) -> None:
        records = _trace()

        class TupleSubclass(tuple):
            pass

        invalid_inputs = (
            list(records),
            {"records": records},
            (record for record in records),
            "four-records",
            b"four-records",
            bytearray(b"four-records"),
            TupleSubclass(records),
            records[:3],
            records + (records[-1],),
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(SyntheticPolicyUpdateTraceSmokeError):
                    apply_synthetic_policy_update_trace_smoke(  # type: ignore[arg-type]
                        value,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

        with self.assertRaisesRegex(
            SyntheticPolicyUpdateTraceSmokeError,
            "SyntheticPolicyUpdateInput",
        ):
            apply_synthetic_policy_update_trace_smoke(  # type: ignore[arg-type]
                records[:3] + (object(),),
                learning_rate=0.5,
                discount_factor=0.75,
            )

    def test_requires_two_distinct_keys_in_exact_abab_order(self) -> None:
        first_a, first_b, second_a, second_b = _trace()
        cases = (
            (
                "two distinct",
                (first_a, replace(first_b, state_id=first_a.state_id, action_id=first_a.action_id), second_a, second_b),
            ),
            (
                "step 3",
                (first_a, first_b, replace(second_a, state_id=first_b.state_id, action_id=first_b.action_id), second_b),
            ),
            (
                "step 4",
                (first_a, first_b, second_a, replace(second_b, state_id=first_a.state_id, action_id=first_a.action_id)),
            ),
            (
                "step 3",
                (first_a, first_b, replace(second_a, state_id="synthetic-state:c"), second_b),
            ),
        )
        for message, records in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateTraceSmokeError, message
                ):
                    apply_synthetic_policy_update_trace_smoke(
                        records,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_requires_distinct_record_ids_and_shared_source(self) -> None:
        records = _trace()
        duplicate_id = records[:3] + (
            replace(records[3], record_id=records[0].record_id),
        )
        different_source = (
            records[0],
            replace(records[1], source_kind="other"),
            records[2],
            records[3],
        )
        cases = (
            ("record_ids", duplicate_id),
            ("source_kind", different_source),
        )
        for message, bad_records in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateTraceSmokeError, message
                ):
                    apply_synthetic_policy_update_trace_smoke(
                        bad_records,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_terminal_ordering_is_exact_for_all_steps(self) -> None:
        records = _trace()
        cases = (
            (1, replace(records[0], terminal=True, next_max_action_value=None)),
            (2, replace(records[1], terminal=True, next_max_action_value=None)),
            (3, replace(records[2], terminal=False, next_max_action_value=1.0)),
            (4, replace(records[3], terminal=False, next_max_action_value=1.0)),
        )
        for step_index, replacement in cases:
            bad_records = list(records)
            bad_records[step_index - 1] = replacement
            with self.subTest(step_index=step_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateTraceSmokeError,
                    f"step {step_index}",
                ):
                    apply_synthetic_policy_update_trace_smoke(
                        tuple(bad_records),  # type: ignore[arg-type]
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_requires_exact_independent_continuity_for_both_keys(self) -> None:
        records = _trace()
        cases = (
            (3, replace(records[2], current_action_value=3.0000000000000004)),
            (4, replace(records[3], current_action_value=8.250000000000002)),
        )
        for step_index, replacement in cases:
            bad_records = list(records)
            bad_records[step_index - 1] = replacement
            with self.subTest(step_index=step_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateTraceSmokeError,
                    f"step {step_index} current_action_value",
                ):
                    apply_synthetic_policy_update_trace_smoke(
                        tuple(bad_records),  # type: ignore[arg-type]
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_base_errors_are_wrapped_for_each_step_with_cause(self) -> None:
        records = _trace()
        for step_index in range(1, 5):
            bad_records = list(records)
            bad_records[step_index - 1] = replace(
                bad_records[step_index - 1],
                uses_real_data=True,
            )
            with self.subTest(step_index=step_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateTraceSmokeError,
                    f"step {step_index} failed",
                ) as context:
                    apply_synthetic_policy_update_trace_smoke(
                        tuple(bad_records),  # type: ignore[arg-type]
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )
                self.assertIsInstance(
                    context.exception.__cause__,
                    SyntheticPolicyUpdateSmokeError,
                )

    def test_repeated_output_is_equal_and_inputs_are_immutable(self) -> None:
        records = _trace()
        before = tuple(asdict(record) for record in records)

        first = apply_synthetic_policy_update_trace_smoke(
            records, learning_rate=0.5, discount_factor=0.75
        )
        second = apply_synthetic_policy_update_trace_smoke(
            records, learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(first, second)
        self.assertEqual(tuple(asdict(record) for record in records), before)
        with self.assertRaises(FrozenInstanceError):
            records[0].reward = 9.0  # type: ignore[misc]

    def test_result_is_frozen_and_has_exact_safe_fields(self) -> None:
        result = apply_synthetic_policy_update_trace_smoke(
            _trace(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(
            set(asdict(result)),
            {
                "trace_version",
                "step_count",
                "record_ids",
                "source_kind",
                "learning_rate",
                "discount_factor",
                "state_action_keys",
                "initial_action_values",
                "intermediate_action_values",
                "final_action_values",
                "step_results",
                "trace_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.trace_version,
            SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION,
        )
        self.assertEqual(result.step_count, 4)
        self.assertEqual(
            result.record_ids,
            tuple(record.record_id for record in _trace()),
        )
        self.assertEqual(
            result.state_action_keys,
            (
                ("synthetic-state:a", "discard-1m"),
                ("synthetic-state:b", "discard-2p"),
            ),
        )
        self.assertEqual(len(result.step_results), 4)
        self.assertEqual(
            result.evidence_grade,
            "P8 synthetic/local four-record interleaved two-key numerical "
            "policy-update trace smoke evidence only",
        )
        self.assertTrue(result.trace_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local four-record interleaved numerical smoke only",
            "not an environment, episode or replay buffer",
            "not self-play",
            "not a variable or production training loop",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)
        with self.assertRaises(FrozenInstanceError):
            result.step_count = 5  # type: ignore[misc]

    def test_public_imports_are_available_from_rl_package(self) -> None:
        self.assertIs(
            apply_synthetic_policy_update_trace_smoke,
            trace_module.apply_synthetic_policy_update_trace_smoke,
        )
        self.assertIs(
            SyntheticPolicyUpdateTraceResult,
            trace_module.SyntheticPolicyUpdateTraceResult,
        )

    def test_public_surface_is_narrow_and_base_helper_is_reused(self) -> None:
        self.assertEqual(
            set(trace_module.__all__),
            {
                "SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION",
                "SyntheticPolicyUpdateTraceResult",
                "SyntheticPolicyUpdateTraceSmokeError",
                "apply_synthetic_policy_update_trace_smoke",
            },
        )
        self.assertEqual(
            tuple(
                inspect.signature(
                    apply_synthetic_policy_update_trace_smoke
                ).parameters
            ),
            ("input_records", "learning_rate", "discount_factor"),
        )
        public_text = " ".join(trace_module.__all__).lower()
        for forbidden in (
            "path",
            "fixture",
            "environment",
            "episode",
            "replay",
            "self_play",
            "model",
            "optimizer",
            "training",
        ):
            self.assertNotIn(forbidden, public_text)

        with patch.object(
            trace_module,
            "apply_synthetic_policy_update_smoke",
            wraps=trace_module.apply_synthetic_policy_update_smoke,
        ) as base_helper:
            apply_synthetic_policy_update_trace_smoke(
                _trace(), learning_rate=0.5, discount_factor=0.75
            )
        self.assertEqual(base_helper.call_count, 4)
        source = inspect.getsource(trace_module)
        for duplicated_formula in (
            "target_value =",
            "td_error =",
            "updated_action_value =",
        ):
            self.assertNotIn(duplicated_formula, source)


if __name__ == "__main__":
    unittest.main()
