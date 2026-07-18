from __future__ import annotations

from dataclasses import FrozenInstanceError, asdict
import inspect
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.synthetic_policy_update_sequence_smoke as sequence_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateSequenceResult,
    SyntheticPolicyUpdateSequenceSmokeError,
    SyntheticPolicyUpdateSmokeError,
    apply_synthetic_policy_update_sequence_smoke,
)


def _record(**overrides: object) -> SyntheticPolicyUpdateInput:
    values: dict[str, object] = {
        "record_id": "p8-sequence-record:0001",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "state_id": "synthetic-state:sequence-0001",
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


def _sequence() -> tuple[SyntheticPolicyUpdateInput, SyntheticPolicyUpdateInput]:
    return (
        _record(),
        _record(
            record_id="p8-sequence-record:0002",
            current_action_value=3.0,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
        ),
    )


class SyntheticPolicyUpdateSequenceSmokeTests(unittest.TestCase):
    def test_exact_two_step_formulas_and_final_value(self) -> None:
        result = apply_synthetic_policy_update_sequence_smoke(
            _sequence(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertIsInstance(result, SyntheticPolicyUpdateSequenceResult)
        first, second = result.step_results
        self.assertEqual((first.target_value, first.td_error), (4.0, 2.0))
        self.assertEqual(first.updated_action_value, 3.0)
        self.assertEqual((second.target_value, second.td_error), (5.0, 2.0))
        self.assertEqual(second.updated_action_value, 4.0)
        self.assertEqual(result.initial_action_value, 2.0)
        self.assertEqual(result.intermediate_action_value, 3.0)
        self.assertEqual(result.final_action_value, 4.0)

    def test_requires_exact_two_record_tuple(self) -> None:
        first, second = _sequence()
        invalid_inputs = (
            [first, second],
            {"first": first, "second": second},
            (record for record in (first, second)),
            "two-records",
            b"two-records",
            bytearray(b"two-records"),
            (first,),
            (first, second, second),
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(SyntheticPolicyUpdateSequenceSmokeError):
                    apply_synthetic_policy_update_sequence_smoke(  # type: ignore[arg-type]
                        value, learning_rate=0.5, discount_factor=0.75
                    )

        with self.assertRaisesRegex(
            SyntheticPolicyUpdateSequenceSmokeError,
            "SyntheticPolicyUpdateInput",
        ):
            apply_synthetic_policy_update_sequence_smoke(  # type: ignore[arg-type]
                (first, object()), learning_rate=0.5, discount_factor=0.75
            )

    def test_terminal_ordering_is_exact(self) -> None:
        first, second = _sequence()
        cases = (
            (
                _record(next_max_action_value=None, terminal=True),
                second,
                "step 1",
            ),
            (
                first,
                _record(
                    record_id="p8-sequence-record:0002",
                    current_action_value=3.0,
                    terminal=False,
                ),
                "step 2",
            ),
        )
        for bad_first, bad_second, message in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateSequenceSmokeError, message
                ):
                    apply_synthetic_policy_update_sequence_smoke(
                        (bad_first, bad_second),
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_identity_and_distinct_record_ids_are_required(self) -> None:
        first, second = _sequence()
        cases = (
            ("record_ids", _record(record_id=first.record_id, current_action_value=3.0, next_max_action_value=None, terminal=True)),
            ("source_kind", _record(record_id=second.record_id, source_kind="other", current_action_value=3.0, next_max_action_value=None, terminal=True)),
            ("state_id", _record(record_id=second.record_id, state_id="synthetic-state:other", current_action_value=3.0, next_max_action_value=None, terminal=True)),
            ("action_id", _record(record_id=second.record_id, action_id="discard-2m", current_action_value=3.0, next_max_action_value=None, terminal=True)),
        )
        for message, bad_second in cases:
            with self.subTest(message=message):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateSequenceSmokeError, message
                ):
                    apply_synthetic_policy_update_sequence_smoke(
                        (first, bad_second),
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

    def test_exact_intermediate_value_continuity_is_required(self) -> None:
        first, second = _sequence()
        bad_second = _record(
            record_id=second.record_id,
            current_action_value=3.0000000000000004,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
        )

        with self.assertRaisesRegex(
            SyntheticPolicyUpdateSequenceSmokeError, "exactly equal"
        ):
            apply_synthetic_policy_update_sequence_smoke(
                (first, bad_second),
                learning_rate=0.5,
                discount_factor=0.75,
            )

    def test_base_validation_error_is_wrapped_with_step_and_cause(self) -> None:
        first, second = _sequence()
        bad_second = _record(
            record_id=second.record_id,
            current_action_value=3.0,
            reward=5.0,
            next_max_action_value=None,
            terminal=True,
            uses_real_data=True,
        )
        cases = (
            (1, (_record(uses_real_data=True), second)),
            (2, (first, bad_second)),
        )

        for step_index, records in cases:
            with self.subTest(step_index=step_index):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateSequenceSmokeError,
                    f"step {step_index} failed",
                ) as context:
                    apply_synthetic_policy_update_sequence_smoke(
                        records,
                        learning_rate=0.5,
                        discount_factor=0.75,
                    )

                self.assertIsInstance(
                    context.exception.__cause__,
                    SyntheticPolicyUpdateSmokeError,
                )

    def test_repeated_output_is_equal_and_inputs_are_immutable(self) -> None:
        records = _sequence()
        before = tuple(asdict(record) for record in records)

        first = apply_synthetic_policy_update_sequence_smoke(
            records, learning_rate=0.5, discount_factor=0.75
        )
        second = apply_synthetic_policy_update_sequence_smoke(
            records, learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(first, second)
        self.assertEqual(tuple(asdict(record) for record in records), before)
        with self.assertRaises(FrozenInstanceError):
            records[0].reward = 9.0  # type: ignore[misc]

    def test_result_is_frozen_and_has_exact_safe_fields(self) -> None:
        result = apply_synthetic_policy_update_sequence_smoke(
            _sequence(), learning_rate=0.5, discount_factor=0.75
        )

        self.assertEqual(
            set(asdict(result)),
            {
                "sequence_version",
                "step_count",
                "record_ids",
                "source_kind",
                "state_id",
                "action_id",
                "learning_rate",
                "discount_factor",
                "initial_action_value",
                "intermediate_action_value",
                "final_action_value",
                "step_results",
                "sequence_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.sequence_version,
            SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION,
        )
        self.assertEqual(result.step_count, 2)
        self.assertEqual(
            result.evidence_grade,
            "P8 synthetic/local two-step numerical policy-update sequence "
            "smoke evidence only",
        )
        self.assertTrue(result.sequence_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local two-step numerical smoke only",
            "not an environment or episode",
            "not self-play",
            "not production training",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)
        with self.assertRaises(FrozenInstanceError):
            result.step_count = 3  # type: ignore[misc]

    def test_public_imports_are_available_from_rl_package(self) -> None:
        self.assertIs(
            apply_synthetic_policy_update_sequence_smoke,
            sequence_module.apply_synthetic_policy_update_sequence_smoke,
        )
        self.assertIs(
            SyntheticPolicyUpdateSequenceResult,
            sequence_module.SyntheticPolicyUpdateSequenceResult,
        )

    def test_public_api_has_no_path_or_broad_runtime_surface(self) -> None:
        self.assertEqual(
            set(sequence_module.__all__),
            {
                "SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION",
                "SyntheticPolicyUpdateSequenceResult",
                "SyntheticPolicyUpdateSequenceSmokeError",
                "apply_synthetic_policy_update_sequence_smoke",
            },
        )
        self.assertEqual(
            tuple(
                inspect.signature(
                    apply_synthetic_policy_update_sequence_smoke
                ).parameters
            ),
            ("input_records", "learning_rate", "discount_factor"),
        )
        public_text = " ".join(sequence_module.__all__).lower()
        for forbidden in (
            "path",
            "fixture",
            "environment",
            "episode",
            "self_play",
            "model",
            "optimizer",
            "training",
        ):
            self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
