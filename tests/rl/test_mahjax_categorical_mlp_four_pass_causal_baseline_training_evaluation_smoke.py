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

import mjlabai.rl.mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_EVALUATION_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS,
    MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult,
    MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError,
    run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke,
)


class MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_EVALUATION_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError",
                "MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult",
                "run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_EVALUATION_SMOKE_VERSION,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.selected_pass_index = 4  # type: ignore[misc]

    def test_exact_four_pass_disjoint_protocol(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS,
            tuple(range(32)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS,
            tuple(range(52, 84)),
        )
        self.assertEqual(self.result.pass_count, 4)
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.update_attempt_count, 128)
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertEqual(self.result.replication_evaluation_seeds, tuple(range(84, 116)))
        self.assertTrue(self.result.all_seed_sets_pairwise_disjoint)
        self.assertEqual(self.result.evaluation_call_count, 4)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_checkpoint_id)

    def test_pass_summaries_match_predeclared_probe(self) -> None:
        self.assertEqual(
            self.result.per_pass_nonzero_update_counts,
            (31, 32, 32, 32),
        )
        self.assertEqual(
            self.result.per_pass_nonzero_raw_outcome_counts,
            (10, 10, 10, 11),
        )
        self.assertEqual(len(self.result.pass_ending_baselines), 4)
        expected = (
            (-0.0121875, -0.015625, -0.05, 0.0528125),
            (0.000625, -0.02734375, -0.05859375, 0.0571875),
            (0.0054166667, -0.0296875, -0.0630208333, 0.0591666667),
            (0.00625, -0.040390625, -0.054140625, 0.0609375),
        )
        for actual_row, expected_row in zip(
            self.result.pass_ending_baselines,
            expected,
        ):
            for actual, expected_value in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual, expected_value, places=6)

    def test_policy_and_baseline_are_continuous_across_pass_edges(self) -> None:
        for edge in (32, 64, 96):
            self.assertEqual(
                self.result.baseline_before_per_attempt[edge],
                self.result.baseline_after_per_attempt[edge - 1],
            )
        self.assertEqual(
            self.result.final_running_baseline,
            self.result.pass_ending_baselines[-1],
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

    def test_complete_128_training_records_are_retained_and_legal(self) -> None:
        self.assertEqual(tuple(map(len, self.result.per_pass_action_traces)), (32,) * 4)
        self.assertEqual(
            tuple(map(len, self.result.per_pass_action_trace_sha256)),
            (32,) * 4,
        )
        self.assertEqual(len(set(self.result.per_pass_action_trace_sha256[0])), 32)
        for pass_actions, pass_legal in zip(
            self.result.per_pass_action_traces,
            self.result.per_pass_legal_action_traces,
        ):
            for actions, legal_rows in zip(pass_actions, pass_legal):
                self.assertEqual(len(actions), len(legal_rows))
                self.assertTrue(
                    all(action in legal for action, legal in zip(actions, legal_rows))
                )

    def test_final_parameter_deltas_match_probe(self) -> None:
        self.assertTrue(self.result.parameters_changed)
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            (0.0119271539, 0.0016169089, 0.0243039839, 0.0027456258),
        ):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_disjoint_evaluation_pins_bounded_improvement(self) -> None:
        self.assertEqual(self.result.initial_project_raw_sum, -312.0)
        self.assertEqual(self.result.final_project_raw_sum, -297.0)
        self.assertEqual(self.result.project_raw_sum_delta, 15.0)
        self.assertEqual(
            (self.result.initial_positive_round_count, self.result.final_positive_round_count),
            (2, 2),
        )
        self.assertEqual(
            (self.result.initial_negative_round_count, self.result.final_negative_round_count),
            (20, 19),
        )
        self.assertEqual(
            self.result.changed_evaluation_seeds,
            (52, 58, 65, 70, 72),
        )
        self.assertEqual(
            self.result.initial_evaluation_project_raw_rewards[6],
            -15.0,
        )
        self.assertEqual(self.result.final_evaluation_project_raw_rewards[6], 0.0)
        self.assertTrue(self.result.bounded_diagnostic_improved)

    def test_predeclared_replication_evaluation_is_pinned_without_selection(self) -> None:
        self.assertEqual(
            self.result.initial_replication_project_raw_rewards,
            (
                -13.0, -10.0, 0.0, -77.0, -40.0, -10.0, 0.0, 0.0,
                -180.0, -116.0, 0.0, -10.0, -160.0, 0.0, 0.0, 0.0,
                0.0, -77.0, -20.0, -15.0, -10.0, 0.0, -10.0, -77.0,
                0.0, -80.0, 0.0, -20.0, -15.0, -116.0, 0.0, 0.0,
            ),
        )
        self.assertEqual(
            self.result.final_replication_project_raw_rewards,
            (
                -13.0, -10.0, 0.0, -77.0, -40.0, -10.0, 0.0, 0.0,
                -180.0, -116.0, 0.0, -10.0, -160.0, 0.0, 0.0, 0.0,
                0.0, -77.0, -20.0, -10.0, -10.0, 0.0, -10.0, -77.0,
                0.0, -80.0, 0.0, -20.0, -15.0, 0.0, 0.0, 0.0,
            ),
        )
        self.assertEqual(
            self.result.initial_replication_transition_counts,
            (37, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
             84, 35, 60, 87, 82, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76),
        )
        self.assertEqual(
            self.result.final_replication_transition_counts,
            (38, 88, 48, 65, 85, 81, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
             84, 35, 59, 50, 81, 66, 36, 48, 36, 59, 74, 86, 82, 79, 75, 76),
        )
        self.assertEqual(self.result.initial_replication_project_raw_sum, -1056.0)
        self.assertEqual(self.result.final_replication_project_raw_sum, -935.0)
        self.assertEqual(self.result.replication_project_raw_sum_delta, 121.0)
        self.assertEqual(
            (
                self.result.initial_replication_positive_round_count,
                self.result.final_replication_positive_round_count,
            ),
            (0, 0),
        )
        self.assertEqual(
            (
                self.result.initial_replication_negative_round_count,
                self.result.final_replication_negative_round_count,
            ),
            (19, 18),
        )
        self.assertEqual(
            self.result.changed_replication_evaluation_seeds,
            (84, 89, 92, 94, 102, 103, 104, 106, 110, 113, 114),
        )
        for counts, traces, scores in (
            (
                self.result.initial_replication_transition_counts,
                self.result.initial_replication_project_action_traces,
                self.result.initial_replication_final_scores,
            ),
            (
                self.result.final_replication_transition_counts,
                self.result.final_replication_project_action_traces,
                self.result.final_replication_final_scores,
            ),
        ):
            self.assertEqual((len(counts), len(traces), len(scores)), (32, 32, 32))
            self.assertTrue(
                all(
                    0 < len(project_trace) <= transition_count
                    for project_trace, transition_count in zip(traces, counts)
                )
            )
            self.assertTrue(all(len(score) == 4 for score in scores))

    def test_safety_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.all_training_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact four-pass causal-baseline two-fixed-window deterministic diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "exactly 128 attempts",
            "evaluation occurs only before training and after all four passes",
            "replication outcome is retained regardless of sign and never selected",
            "replication sum changes from -1056 to -935",
            "two fixed deterministic windows are not robust or generalization evidence",
            "no fifth pass, alternate count, early stop",
            "not policy-quality, model-strength, stable-dan",
            "not tenhou or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_wraps_runtime_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("runtime unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError,
                "pinned four-pass causal-baseline runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke()

    def test_source_forbids_intermediate_selection_or_open_ended_training(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("_PASS_COUNT = 4", source)
        self.assertEqual(source.count("_evaluate("), 5)
        self.assertIn("for _pass_index in range(_PASS_COUNT):", source)
        self.assertIn("selected_pass_index=None", source)
        self.assertNotIn("while ", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "early_stop",
            "replay_buffer",
            "best_checkpoint",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
