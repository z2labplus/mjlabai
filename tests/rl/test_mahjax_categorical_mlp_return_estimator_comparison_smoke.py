from __future__ import annotations

from dataclasses import FrozenInstanceError, fields
import inspect
import math
from pathlib import Path
import statistics
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_return_estimator_comparison_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_return_estimator_comparison_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS,
    MahJaxCategoricalMlpReturnEstimatorComparisonResult,
    MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError,
    run_mahjax_categorical_mlp_return_estimator_comparison_smoke,
)


class MahJaxCategoricalMlpReturnEstimatorComparisonSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_return_estimator_comparison_smoke()

    def test_exact_public_surface_constants_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE",
                "MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError",
                "MahJaxCategoricalMlpReturnEstimatorComparisonResult",
                "run_mahjax_categorical_mlp_return_estimator_comparison_smoke",
            },
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpReturnEstimatorComparisonResult,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        for branch in (
            self.result.raw_branch,
            self.result.centered_branch,
            self.result.standardized_branch,
        ):
            self.assertNotIn("parameters", {field.name for field in fields(branch)})
        with self.assertRaises(FrozenInstanceError):
            self.result.evaluation_update_count = 1  # type: ignore[misc]

    def test_exact_seed_learning_rate_and_independent_branch_contract(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS,
            (1, 3, 5, 7, 11),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS,
            tuple(range(20, 36)),
        )
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE, 0.01)
        self.assertEqual(
            self.result.estimator_ids,
            (
                "raw_actor_return",
                "seat_centered_actor_return",
                "seat_standardized_actor_return",
            ),
        )
        self.assertTrue(self.result.branch_initial_parameters_identical)
        self.assertTrue(self.result.branch_final_parameters_distinct)
        self.assertTrue(self.result.centered_parameters_differ_from_raw)
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertEqual(self.result.evaluation_update_count, 0)

    def test_all_branches_reuse_exact_legal_terminal_training_trajectories(self) -> None:
        branches = (
            self.result.raw_branch,
            self.result.centered_branch,
            self.result.standardized_branch,
        )
        for branch in branches:
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
            for actors, actions, legal_trace in zip(
                branch.training_actor_traces,
                branch.training_action_traces,
                branch.training_legal_action_traces,
            ):
                self.assertEqual(len(actors), len(actions))
                self.assertEqual(len(actions), len(legal_trace))
                for action, legal_actions in zip(actions, legal_trace):
                    self.assertIn(action, legal_actions)
        self.assertEqual(
            self.result.raw_branch.training_action_traces,
            self.result.centered_branch.training_action_traces,
        )
        self.assertEqual(
            self.result.raw_branch.training_action_traces,
            self.result.standardized_branch.training_action_traces,
        )
        self.assertTrue(self.result.all_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)

    def test_exact_raw_centered_and_standardized_return_formulas(self) -> None:
        for raw_rewards, raw_returns, centered_returns, standardized_returns in zip(
            self.result.raw_branch.training_cumulative_raw_rewards,
            self.result.raw_branch.estimated_seat_returns,
            self.result.centered_branch.estimated_seat_returns,
            self.result.standardized_branch.estimated_seat_returns,
        ):
            expected_raw = tuple(value / 100.0 for value in raw_rewards)
            mean_raw = statistics.fmean(expected_raw)
            expected_centered = tuple(value - mean_raw for value in expected_raw)
            standard_deviation = statistics.pstdev(expected_centered)
            expected_standardized = tuple(
                value / standard_deviation for value in expected_centered
            )
            for actual, expected in zip(raw_returns, expected_raw):
                self.assertAlmostEqual(actual, expected, places=6)
            for actual, expected in zip(centered_returns, expected_centered):
                self.assertAlmostEqual(actual, expected, places=6)
            for actual, expected in zip(
                standardized_returns,
                expected_standardized,
            ):
                self.assertAlmostEqual(actual, expected, places=6)
            self.assertAlmostEqual(math.fsum(centered_returns), 0.0, places=6)
            self.assertAlmostEqual(statistics.pstdev(standardized_returns), 1.0, places=6)

    def test_objectives_and_parameter_deltas_are_finite_and_exact(self) -> None:
        expected_final_deltas = (
            (0.0021020556, 0.0004550584, 0.0053585209, 0.0005585462),
            (0.0020699743, 0.0004389429, 0.0052021975, 0.0005401245),
            (0.0056803911, 0.0015099167, 0.0181233995, 0.0020000334),
        )
        for branch, expected_final in zip(
            (
                self.result.raw_branch,
                self.result.centered_branch,
                self.result.standardized_branch,
            ),
            expected_final_deltas,
        ):
            self.assertEqual(len(branch.initial_objectives), 5)
            self.assertEqual(len(branch.post_update_objectives), 5)
            for initial, post in zip(
                branch.initial_objectives,
                branch.post_update_objectives,
            ):
                self.assertTrue(math.isfinite(initial))
                self.assertTrue(math.isfinite(post))
                self.assertLess(post, initial)
            for actual, expected in zip(
                branch.final_parameter_delta_l2,
                expected_final,
            ):
                self.assertGreater(actual, 0.0)
                self.assertAlmostEqual(actual, expected, places=5)

    def test_fixed_evaluation_records_exact_failure_comparison(self) -> None:
        self.assertEqual(self.result.initial_project_raw_sum, -320.0)
        self.assertEqual(self.result.raw_branch.project_raw_sum, -454.0)
        self.assertEqual(self.result.centered_branch.project_raw_sum, -454.0)
        self.assertEqual(self.result.standardized_branch.project_raw_sum, -490.0)
        self.assertEqual(
            self.result.raw_branch.changed_from_initial_evaluation_seeds,
            (32,),
        )
        self.assertEqual(
            self.result.centered_branch.changed_from_initial_evaluation_seeds,
            (32,),
        )
        self.assertEqual(
            self.result.standardized_branch.changed_from_initial_evaluation_seeds,
            (20, 27, 31, 32, 35),
        )
        self.assertEqual(self.result.standardized_branch.positive_round_count, 0)
        self.assertEqual(self.result.standardized_branch.negative_round_count, 11)
        self.assertTrue(self.result.raw_matches_reviewed_failure_diagnostic)
        self.assertTrue(self.result.standardized_fixed_diagnostic_is_worse)

    def test_centered_parameters_differ_but_evaluation_matches_raw(self) -> None:
        self.assertTrue(self.result.centered_parameters_differ_from_raw)
        self.assertTrue(self.result.centered_evaluation_matches_raw)
        self.assertEqual(
            self.result.raw_branch.evaluation_transition_counts,
            self.result.centered_branch.evaluation_transition_counts,
        )
        self.assertEqual(
            self.result.raw_branch.evaluation_project_action_traces,
            self.result.centered_branch.evaluation_project_action_traces,
        )
        self.assertEqual(
            self.result.raw_branch.evaluation_project_raw_rewards,
            self.result.centered_branch.evaluation_project_raw_rewards,
        )

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_categorical_mlp_return_estimator_comparison_smoke(),
        )

    def test_wraps_imitation_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_return_estimator_comparison_smoke()

    def test_warnings_and_source_prevent_scope_drift(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local raw/centered/standardized return-estimator failure-comparison smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "initial/raw/centered/standardized project sums are -320/-454/-454/-490",
            "centering changes parameters but not fixed greedy evaluation behavior",
            "no estimator is selected, promoted or approved for scale-up",
            "not improvement, policy-quality, estimator-superiority or strength evidence",
        ):
            self.assertIn(phrase, warning_text)
        source = inspect.getsource(smoke_module)
        self.assertIn("for estimator_id in _ESTIMATOR_IDS", source)
        self.assertIn(
            "for seed in MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS",
            source,
        )
        self.assertIn("_apply_actor_indexed_raw_outcome_update(", source)
        self.assertIn("_collect_mixed_policy_evaluation_round(", source)
        self.assertIn("rule_based_player", source)
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
