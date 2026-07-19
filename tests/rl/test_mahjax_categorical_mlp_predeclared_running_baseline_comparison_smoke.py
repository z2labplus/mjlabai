from __future__ import annotations

from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_COMPARISON_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS,
    MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult,
    MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError,
    run_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke,
)


class MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_COMPARISON_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError",
                "MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult",
                "run_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_COMPARISON_SMOKE_VERSION,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.selected_estimator_id = "baseline"  # type: ignore[misc]

    def test_exact_shared_predeclared_protocol(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS,
            tuple(range(32)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS,
            tuple(range(52, 84)),
        )
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertIsNone(self.result.selected_estimator_id)
        self.assertIsNone(self.result.selected_checkpoint_id)

    def test_causal_baseline_uses_prior_records_only(self) -> None:
        self.assertEqual(self.result.baseline_before_per_attempt[0], (0.0,) * 4)
        self.assertEqual(self.result.baseline_after_per_attempt[0], (0.0,) * 4)
        self.assertEqual(self.result.baseline_before_per_attempt[1], (0.0,) * 4)
        for actual, expected in zip(
            self.result.baseline_after_per_attempt[1],
            (-0.1, 0.35, -0.1, -0.15),
        ):
            self.assertAlmostEqual(actual, expected, places=7)
        self.assertEqual(
            self.result.baseline_before_per_attempt[2],
            self.result.baseline_after_per_attempt[1],
        )
        for actual, expected in zip(
            self.result.advantage_seat_returns_per_attempt[2],
            (0.1, -0.35, 0.1, 0.15),
        ):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_running_baseline_densifies_nonzero_updates(self) -> None:
        self.assertEqual(self.result.baseline_update_attempt_count, 32)
        self.assertEqual(self.result.raw_nonzero_update_count, 10)
        self.assertEqual(self.result.baseline_nonzero_update_count, 31)
        self.assertEqual(self.result.baseline_noop_seeds, (0,))
        self.assertEqual(
            self.result.baseline_nonzero_update_seeds,
            tuple(range(1, 32)),
        )
        self.assertEqual(
            self.result.per_attempt_parameter_delta_l2[0],
            (0.0, 0.0, 0.0, 0.0),
        )
        self.assertTrue(
            all(
                any(value > 0.0 for value in row)
                for row in self.result.per_attempt_parameter_delta_l2[1:]
            )
        )

    def test_complete_training_trajectories_are_retained_and_legal(self) -> None:
        self.assertEqual(len(self.result.training_transition_counts), 32)
        self.assertEqual(len(self.result.training_action_trace_sha256), 32)
        self.assertTrue(all(self.result.training_transition_counts))
        self.assertEqual(
            self.result.training_transition_counts,
            self.result.raw_reference.training_transition_counts,
        )
        self.assertEqual(
            self.result.training_action_trace_sha256,
            self.result.raw_reference.training_action_trace_sha256,
        )
        for actions, legal_rows in zip(
            self.result.training_action_traces,
            self.result.training_legal_action_traces,
        ):
            self.assertEqual(len(actions), len(legal_rows))
            self.assertTrue(
                all(action in legal for action, legal in zip(actions, legal_rows))
            )

    def test_final_baseline_and_parameter_deltas_match_probe(self) -> None:
        for actual, expected in zip(
            self.result.final_running_baseline,
            (-0.0121875, -0.015625, -0.05, 0.0528125),
        ):
            self.assertAlmostEqual(actual, expected, places=7)
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            (0.0035393923, 0.0006425792, 0.0084222732, 0.0009679428),
        ):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_evaluation_reward_diagnostic_is_unchanged(self) -> None:
        self.assertEqual(self.result.evaluation_project_raw_sum, -312.0)
        self.assertEqual(self.result.evaluation_positive_round_count, 2)
        self.assertEqual(self.result.evaluation_negative_round_count, 20)
        self.assertEqual(
            self.result.changed_from_initial_evaluation_seeds,
            (52, 65, 72),
        )
        self.assertEqual(
            self.result.changed_from_raw_evaluation_seeds,
            (65,),
        )
        self.assertTrue(self.result.baseline_reward_vector_matches_raw)
        self.assertTrue(self.result.baseline_reward_counts_match_raw)
        self.assertTrue(
            self.result.signal_densified_without_reward_improvement
        )
        self.assertEqual(
            self.result.evaluation_project_raw_rewards,
            self.result.raw_reference.final_evaluation_project_raw_rewards,
        )

    def test_safety_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.all_training_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local causal-running-baseline signal-densification comparison evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "prior records only",
            "31 of 32",
            "does not improve",
            "no third estimator, critic, replay",
            "not improvement, policy-quality, model-strength",
            "not tenhou, stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_wraps_raw_reference_failure(self) -> None:
        with patch.object(
            smoke_module,
            "run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke",
            side_effect=RuntimeError("raw unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError,
                "reviewed raw full-range reference failed",
            ):
                run_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke()

    def test_source_forbids_persistence_selection_or_extra_estimators(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("tuple(range(1, 32))", source)
        self.assertIn("selected_estimator_id=None", source)
        self.assertLess(
            source.index("_apply_causal_running_baseline_update("),
            source.index("running_baseline = update.baseline_after"),
        )
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "best_checkpoint",
            "standardized",
            "learned_critic",
            "gae_lambda",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
