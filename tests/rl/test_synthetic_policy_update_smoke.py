from __future__ import annotations

from dataclasses import FrozenInstanceError, asdict
import math
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_POLICY_UPDATE_SMOKE_VERSION,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateResult,
    SyntheticPolicyUpdateSmokeError,
    apply_synthetic_policy_update_smoke,
)


def _record(**overrides: object) -> SyntheticPolicyUpdateInput:
    values: dict[str, object] = {
        "record_id": "p8-smoke-record:0001",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "state_id": "synthetic-state:0001",
        "action_id": "discard-1m",
        "current_action_value": 2.0,
        "reward": 1.0,
        "next_max_action_value": None,
        "terminal": True,
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


class SyntheticPolicyUpdateSmokeTests(unittest.TestCase):
    def test_terminal_update_formula(self) -> None:
        result = apply_synthetic_policy_update_smoke(
            _record(), learning_rate=0.25, discount_factor=0.9
        )

        self.assertIsInstance(result, SyntheticPolicyUpdateResult)
        self.assertEqual(result.target_value, 1.0)
        self.assertEqual(result.td_error, -1.0)
        self.assertEqual(result.updated_action_value, 1.75)
        self.assertTrue(result.update_applied)

    def test_non_terminal_update_formula(self) -> None:
        result = apply_synthetic_policy_update_smoke(
            _record(
                terminal=False,
                current_action_value=2.0,
                reward=1.0,
                next_max_action_value=4.0,
            ),
            learning_rate=0.5,
            discount_factor=0.75,
        )

        self.assertEqual(result.target_value, 4.0)
        self.assertEqual(result.td_error, 2.0)
        self.assertEqual(result.updated_action_value, 3.0)

    def test_repeated_calls_are_equal_and_input_is_immutable(self) -> None:
        input_record = _record()
        before = asdict(input_record)

        first = apply_synthetic_policy_update_smoke(
            input_record, learning_rate=0.5, discount_factor=1.0
        )
        second = apply_synthetic_policy_update_smoke(
            input_record, learning_rate=0.5, discount_factor=1.0
        )

        self.assertEqual(first, second)
        self.assertEqual(asdict(input_record), before)
        with self.assertRaises(FrozenInstanceError):
            input_record.reward = 9.0  # type: ignore[misc]

    def test_invalid_learning_rate_and_discount_factor_are_rejected(self) -> None:
        cases = (
            (0.0, 0.5, "learning_rate"),
            (-0.1, 0.5, "learning_rate"),
            (1.1, 0.5, "learning_rate"),
            (0.5, -0.1, "discount_factor"),
            (0.5, 1.1, "discount_factor"),
        )
        for learning_rate, discount_factor, message in cases:
            with self.subTest(
                learning_rate=learning_rate,
                discount_factor=discount_factor,
            ):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateSmokeError, message
                ):
                    apply_synthetic_policy_update_smoke(
                        _record(),
                        learning_rate=learning_rate,
                        discount_factor=discount_factor,
                    )

    def test_non_finite_and_bool_numeric_values_are_rejected(self) -> None:
        record_cases = (
            ("current_action_value", math.nan),
            ("current_action_value", math.inf),
            ("reward", -math.inf),
            ("reward", True),
            ("next_max_action_value", math.nan),
            ("next_max_action_value", False),
        )
        for field, value in record_cases:
            with self.subTest(field=field, value=value):
                overrides: dict[str, object] = {field: value}
                if field == "next_max_action_value":
                    overrides["terminal"] = False
                with self.assertRaises(SyntheticPolicyUpdateSmokeError):
                    apply_synthetic_policy_update_smoke(
                        _record(**overrides),
                        learning_rate=0.5,
                        discount_factor=0.9,
                    )

        for parameter in (math.nan, math.inf, True):
            with self.subTest(parameter=parameter):
                with self.assertRaises(SyntheticPolicyUpdateSmokeError):
                    apply_synthetic_policy_update_smoke(
                        _record(),
                        learning_rate=parameter,  # type: ignore[arg-type]
                        discount_factor=0.9,
                    )

    def test_non_finite_derived_value_is_rejected(self) -> None:
        with self.assertRaisesRegex(
            SyntheticPolicyUpdateSmokeError, "derived target_value"
        ):
            apply_synthetic_policy_update_smoke(
                _record(
                    terminal=False,
                    reward=1.0e308,
                    next_max_action_value=1.0e308,
                ),
                learning_rate=1.0,
                discount_factor=1.0,
            )

    def test_non_float_representable_real_uses_validation_error(self) -> None:
        with self.assertRaisesRegex(
            SyntheticPolicyUpdateSmokeError,
            "current_action_value must be representable as a finite float",
        ):
            apply_synthetic_policy_update_smoke(
                _record(current_action_value=10**10000),
                learning_rate=0.5,
                discount_factor=0.9,
            )

    def test_terminal_next_value_consistency_is_enforced(self) -> None:
        cases = (
            _record(next_max_action_value=1.0),
            _record(terminal=False, next_max_action_value=None),
        )
        for record in cases:
            with self.subTest(terminal=record.terminal):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateSmokeError, "next_max_action_value"
                ):
                    apply_synthetic_policy_update_smoke(
                        record, learning_rate=0.5, discount_factor=0.9
                    )

    def test_false_or_mistyped_provenance_guardrails_are_rejected(self) -> None:
        cases = {
            "project_authored": False,
            "synthetic": False,
            "local_only": False,
            "uses_real_data": True,
            "uses_external_log": True,
            "uses_platform_data": True,
            "uses_model_output": True,
            "uses_self_play": True,
            "project_authored_non_bool": 1,
        }
        for name, value in cases.items():
            field = name.removesuffix("_non_bool")
            with self.subTest(field=field, value=value):
                with self.assertRaisesRegex(
                    SyntheticPolicyUpdateSmokeError, field
                ):
                    apply_synthetic_policy_update_smoke(
                        _record(**{field: value}),
                        learning_rate=0.5,
                        discount_factor=0.9,
                    )

        with self.assertRaisesRegex(
            SyntheticPolicyUpdateSmokeError, "source_kind"
        ):
            apply_synthetic_policy_update_smoke(
                _record(source_kind="external"),
                learning_rate=0.5,
                discount_factor=0.9,
            )

    def test_identifier_tokens_reject_path_like_and_non_ascii_values(self) -> None:
        invalid_values = (
            "",
            ".",
            "..",
            "state/path",
            r"state\path",
            "state id",
            "状态",
        )
        for field in ("record_id", "state_id", "action_id"):
            for value in invalid_values:
                with self.subTest(field=field, value=value):
                    with self.assertRaisesRegex(
                        SyntheticPolicyUpdateSmokeError, field
                    ):
                        apply_synthetic_policy_update_smoke(
                            _record(**{field: value}),
                            learning_rate=0.5,
                            discount_factor=0.9,
                        )

    def test_result_stays_within_safe_diagnostic_boundary(self) -> None:
        result = apply_synthetic_policy_update_smoke(
            _record(), learning_rate=0.5, discount_factor=0.9
        )

        self.assertEqual(
            set(asdict(result)),
            {
                "smoke_version",
                "record_id",
                "source_kind",
                "state_id",
                "action_id",
                "terminal",
                "learning_rate",
                "discount_factor",
                "current_action_value",
                "reward",
                "next_max_action_value",
                "target_value",
                "td_error",
                "updated_action_value",
                "update_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.smoke_version, SYNTHETIC_POLICY_UPDATE_SMOKE_VERSION
        )
        self.assertEqual(
            result.evidence_grade,
            "P8 synthetic/local numerical policy-update smoke evidence only",
        )
        self.assertTrue(result.safety_guardrails_all_satisfied)
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local only",
            "not real tenhou or haifu data",
            "not self-play",
            "not production training",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_wrong_input_type_and_terminal_type_are_rejected(self) -> None:
        with self.assertRaisesRegex(
            SyntheticPolicyUpdateSmokeError, "SyntheticPolicyUpdateInput"
        ):
            apply_synthetic_policy_update_smoke(  # type: ignore[arg-type]
                {}, learning_rate=0.5, discount_factor=0.9
            )

        with self.assertRaisesRegex(SyntheticPolicyUpdateSmokeError, "terminal"):
            apply_synthetic_policy_update_smoke(
                _record(terminal=1),  # type: ignore[arg-type]
                learning_rate=0.5,
                discount_factor=0.9,
            )


if __name__ == "__main__":
    unittest.main()
