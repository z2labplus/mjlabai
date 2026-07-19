from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate as gate_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_PROTOCOL_ROBUSTNESS_GATE_VERSION,
    MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult,
    build_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate,
)


class MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateTests(
    unittest.TestCase
):
    def setUp(self) -> None:
        self.result = (
            build_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate()
        )

    def test_exact_public_surface_and_zero_argument_builder(self) -> None:
        self.assertEqual(
            set(gate_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_PROTOCOL_ROBUSTNESS_GATE_VERSION",
                "MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult",
                "build_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate",
            },
        )
        self.assertEqual(
            tuple(
                inspect.signature(
                    build_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate
                ).parameters
            ),
            (),
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult,
        )
        self.assertEqual(
            self.result.gate_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_PROTOCOL_ROBUSTNESS_GATE_VERSION,
        )

    def test_exact_reviewed_protocols_windows_and_deltas(self) -> None:
        self.assertEqual(
            self.result.protocol_ids,
            (
                "reference_ordered_0_31_four_pass",
                "alternate_ordered_116_147_four_pass",
            ),
        )
        self.assertEqual(
            self.result.evaluation_window_ids,
            ("fixed_primary_seeds_52_83", "fixed_replication_seeds_84_115"),
        )
        self.assertEqual(
            self.result.reference_window_raw_reward_deltas,
            (15.0, 121.0),
        )
        self.assertEqual(
            self.result.alternate_window_raw_reward_deltas,
            (0.0, 0.0),
        )

    def test_zero_is_not_improvement_and_neither_window_reproduces(self) -> None:
        self.assertEqual(
            self.result.reference_window_positive_improvements,
            (True, True),
        )
        self.assertEqual(
            self.result.alternate_window_positive_improvements,
            (False, False),
        )
        self.assertEqual(
            self.result.per_window_improvement_reproduced,
            (False, False),
        )
        self.assertFalse(self.result.protocols_agree_on_all_windows)
        self.assertFalse(self.result.improvement_reproduced_across_protocols)
        self.assertFalse(self.result.robustness_established)

    def test_selection_is_forbidden_and_no_runtime_calls_occur(self) -> None:
        self.assertFalse(self.result.selection_permitted)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertEqual(self.result.training_call_count, 0)
        self.assertEqual(self.result.evaluation_call_count, 0)

    def test_result_is_frozen_array_free_and_has_no_ranking_fields(self) -> None:
        field_names = {field.name for field in fields(self.result)}
        for forbidden_field in (
            "parameters",
            "threshold",
            "winner",
            "ranking",
            "score",
        ):
            self.assertNotIn(forbidden_field, field_names)
        with self.assertRaises(FrozenInstanceError):
            self.result.selection_permitted = True  # type: ignore[misc]
        self.assertTrue(
            all(
                isinstance(value, (str, int, float, bool, tuple, type(None)))
                for value in vars(self.result).values()
            )
        )

    def test_evidence_and_non_strength_warnings_are_explicit(self) -> None:
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local reviewed-summary two-training-protocol robustness gating evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "reviewed immutable summary values only",
            "no mahjax, jax, environment, training or evaluation execution",
            "zero raw-reward delta is not a positive improvement",
            "do not reproduce under the alternate protocol",
            "two protocols do not establish robustness or generalization",
            "no protocol, model, pass or checkpoint is selected",
            "not policy-quality, model-strength, stable-dan",
            "not tenhou or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_only_standard_library_imports_and_no_io_runtime(self) -> None:
        source = inspect.getsource(gate_module)
        tree = ast.parse(source)
        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])
        self.assertEqual(imported_roots, {"__future__", "dataclasses", "typing"})
        for forbidden in (
            "Path(",
            "open(",
            "subprocess",
            "requests",
            "pickle",
            ".save(",
            "mahjax.make",
            "jax.jit",
            "_evaluate(",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
