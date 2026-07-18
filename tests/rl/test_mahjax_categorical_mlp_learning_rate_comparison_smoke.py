from __future__ import annotations

from dataclasses import FrozenInstanceError, fields
import inspect
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_learning_rate_comparison_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_learning_rate_comparison_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES,
    MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS,
    MahJaxCategoricalMlpLearningRateComparisonResult,
    MahJaxCategoricalMlpLearningRateComparisonSmokeError,
    run_mahjax_categorical_mlp_learning_rate_comparison_smoke,
)


class MahJaxCategoricalMlpLearningRateComparisonSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_learning_rate_comparison_smoke()

    def test_exact_public_surface_constants_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES",
                "MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpLearningRateComparisonSmokeError",
                "MahJaxCategoricalMlpLearningRateComparisonResult",
                "run_mahjax_categorical_mlp_learning_rate_comparison_smoke",
            },
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpLearningRateComparisonResult,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        self.assertNotIn("selected_rate", {field.name for field in fields(self.result)})
        for branch in self.result.branches:
            self.assertNotIn("parameters", {field.name for field in fields(branch)})
        with self.assertRaises(FrozenInstanceError):
            self.result.evaluation_update_count = 1  # type: ignore[misc]

    def test_exact_predeclared_rate_and_seed_contract(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES,
            (0.01, 0.005, 0.001, 0.0001),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS,
            (1, 3, 5, 7, 11),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS,
            tuple(range(20, 52)),
        )
        self.assertEqual(
            tuple(branch.learning_rate for branch in self.result.branches),
            (0.01, 0.005, 0.001, 0.0001),
        )
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertEqual(self.result.evaluation_update_count, 0)

    def test_all_rate_branches_use_same_legal_terminal_trajectories(self) -> None:
        reference = self.result.branches[0]
        for branch in self.result.branches:
            self.assertEqual(branch.update_count, 5)
            self.assertEqual(branch.training_transition_counts, (77, 84, 83, 81, 84))
            self.assertEqual(
                branch.training_seat_decision_counts,
                (
                    (21, 22, 17, 17),
                    (23, 22, 19, 20),
                    (18, 23, 21, 21),
                    (18, 21, 23, 19),
                    (22, 23, 19, 20),
                ),
            )
            self.assertEqual(branch.training_actor_traces, reference.training_actor_traces)
            self.assertEqual(branch.training_action_traces, reference.training_action_traces)
            self.assertEqual(
                branch.training_legal_action_traces,
                reference.training_legal_action_traces,
            )
            for actions, legal_trace in zip(
                branch.training_action_traces,
                branch.training_legal_action_traces,
            ):
                for action, legal_actions in zip(actions, legal_trace):
                    self.assertIn(action, legal_actions)
        self.assertTrue(self.result.all_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)

    def test_all_branches_change_parameters_with_exact_scaled_deltas(self) -> None:
        expected_final_deltas = (
            (0.0021020556, 0.0004550584, 0.0053585209, 0.0005585462),
            (0.0010509313, 0.0002272493, 0.0026764988, 0.0002789878),
            (0.0002101750, 0.0000453977, 0.0005348558, 0.0000557546),
            (0.0000210247, 0.0000045383, 0.0000534743, 0.0000055721),
        )
        self.assertTrue(self.result.branch_initial_parameters_identical)
        self.assertTrue(self.result.branch_final_parameters_distinct)
        self.assertTrue(self.result.all_branches_changed_parameters)
        for branch, expected_deltas in zip(
            self.result.branches,
            expected_final_deltas,
        ):
            for initial, post in zip(
                branch.initial_objectives,
                branch.post_update_objectives,
            ):
                self.assertTrue(math.isfinite(initial))
                self.assertTrue(math.isfinite(post))
                self.assertLess(post, initial)
            for actual, expected in zip(
                branch.final_parameter_delta_l2,
                expected_deltas,
            ):
                self.assertGreater(actual, 0.0)
                self.assertAlmostEqual(actual, expected, places=5)

    def test_fixed_evaluation_records_exact_step_size_sensitivity(self) -> None:
        self.assertEqual(self.result.initial_project_raw_sum, -501.0)
        self.assertEqual(
            tuple(branch.project_raw_sum for branch in self.result.branches),
            (-650.0, -635.0, -501.0, -501.0),
        )
        self.assertEqual(
            tuple(
                branch.changed_from_initial_evaluation_seeds
                for branch in self.result.branches
            ),
            ((32, 39, 43, 44, 50), (32, 39, 44, 50), (), ()),
        )
        self.assertEqual(
            tuple(branch.positive_round_count for branch in self.result.branches),
            (0, 0, 1, 1),
        )
        self.assertEqual(
            tuple(branch.negative_round_count for branch in self.result.branches),
            (18, 17, 16, 16),
        )
        self.assertFalse(self.result.larger_rate_evaluation_identity)
        self.assertTrue(self.result.smaller_rate_initial_behavior_identity)

    def test_small_rates_preserve_behavior_but_not_parameters(self) -> None:
        for branch in self.result.branches[2:]:
            self.assertEqual(
                branch.evaluation_transition_counts,
                self.result.initial_evaluation_transition_counts,
            )
            self.assertEqual(
                branch.evaluation_project_action_traces,
                self.result.initial_evaluation_project_action_traces,
            )
            self.assertEqual(
                branch.evaluation_project_raw_rewards,
                self.result.initial_evaluation_project_raw_rewards,
            )
            self.assertTrue(all(value > 0.0 for value in branch.final_parameter_delta_l2))

    def test_exact_pins_make_repeatability_a_runtime_contract(self) -> None:
        self.assertEqual(len(self.result.branches), 4)
        self.assertTrue(self.result.branch_initial_parameters_identical)
        self.assertTrue(self.result.branch_final_parameters_distinct)
        for branch in self.result.branches:
            self.assertEqual(len(branch.initial_objectives), 5)
            self.assertEqual(len(branch.evaluation_project_action_traces), 32)

    def test_wraps_imitation_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpLearningRateComparisonSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_learning_rate_comparison_smoke()

    def test_warnings_and_source_prevent_selection_or_scope_drift(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local fixed raw-return learning-rate sensitivity smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "32-seed project sums are -650, -635, -501 and -501 against initial -501",
            "rates 0.01 and 0.005 no longer have identical fixed evaluation behavior",
            "smaller rates change parameters but leave fixed greedy behavior unchanged",
            "no rate is ranked, selected, promoted or approved for scale-up",
            "unchanged behavior is not improvement or policy-quality evidence",
        ):
            self.assertIn(phrase, warning_text)
        source = inspect.getsource(smoke_module)
        self.assertIn(
            "for learning_rate in MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES",
            source,
        )
        self.assertIn(
            "for seed in MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS",
            source,
        )
        self.assertIn("_apply_actor_indexed_raw_outcome_update(", source)
        self.assertIn("_evaluate_parameters(", source)
        self.assertNotIn("selected_rate", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            ".load(",
            "pickle",
            "requests",
            "subprocess",
            "platform_data",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
