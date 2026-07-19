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

import mjlabai.rl.mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_SEED_SENSITIVITY_SMOKE_VERSION,
    MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult,
    MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError,
    run_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke,
)


class MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_SEED_SENSITIVITY_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError",
                "MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult",
                "run_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_SEED_SENSITIVITY_SMOKE_VERSION,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.selected_training_protocol_id = "reference"  # type: ignore[misc]

    def test_exact_alternate_training_and_fixed_evaluation_protocol(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS,
            tuple(range(116, 148)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS,
            tuple(range(52, 84)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS,
            tuple(range(84, 116)),
        )
        self.assertEqual(self.result.reference_training_seeds_per_pass, tuple(range(32)))
        self.assertEqual(self.result.pass_count, 4)
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.update_attempt_count, 128)
        self.assertTrue(self.result.all_seed_sets_pairwise_disjoint)
        self.assertEqual(self.result.evaluation_call_count, 2)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertEqual(self.result.reference_training_branch_rerun_count, 0)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_checkpoint_id)

    def test_alternate_pass_summaries_match_predeclared_probe(self) -> None:
        self.assertEqual(self.result.per_pass_nonzero_update_counts, (24, 32, 32, 32))
        self.assertEqual(
            self.result.per_pass_nonzero_raw_outcome_counts,
            (8, 8, 12, 10),
        )
        expected_baselines = (
            (0.0375, 0.034375, -0.00125, -0.0925),
            (0.0321875, 0.02265625, -0.00046875, -0.079375),
            (0.0470833333, 0.0144791667, -0.0115625, -0.0802083333),
            (0.036953125, 0.01625, -0.0159375, -0.070078125),
        )
        for actual_row, expected_row in zip(
            self.result.pass_ending_baselines,
            expected_baselines,
        ):
            for actual, expected in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual, expected, places=6)
        self.assertEqual(
            self.result.final_running_baseline,
            self.result.pass_ending_baselines[-1],
        )

    def test_policy_and_baseline_are_continuous_and_parameters_change(self) -> None:
        for edge in (32, 64, 96):
            self.assertEqual(
                self.result.baseline_before_per_attempt[edge],
                self.result.baseline_after_per_attempt[edge - 1],
            )
        self.assertTrue(self.result.parameters_changed)
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            (0.0107313367, 0.0021179726, 0.0285595842, 0.0033060384),
        ):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_complete_alternate_training_records_are_retained_and_legal(self) -> None:
        self.assertEqual(tuple(map(len, self.result.per_pass_action_traces)), (32,) * 4)
        self.assertEqual(
            tuple(map(len, self.result.per_pass_action_trace_sha256)),
            (32,) * 4,
        )
        for transition_counts, actions, legal_rows in zip(
            self.result.per_pass_transition_counts,
            self.result.per_pass_action_traces,
            self.result.per_pass_legal_action_traces,
        ):
            self.assertEqual(tuple(map(len, actions)), transition_counts)
            for action_trace, legal_trace in zip(actions, legal_rows):
                self.assertEqual(len(action_trace), len(legal_trace))
                self.assertTrue(
                    all(
                        action in legal
                        for action, legal in zip(action_trace, legal_trace)
                    )
                )

    def test_alternate_primary_retains_initial_rewards_not_reference_improvement(self) -> None:
        self.assertEqual(
            self.result.alternate_final_primary_raw_rewards,
            self.result.initial_primary_raw_rewards,
        )
        self.assertEqual(self.result.alternate_final_primary_raw_sum, -312.0)
        self.assertEqual(self.result.alternate_primary_delta_from_initial, 0.0)
        self.assertEqual(self.result.alternate_primary_delta_from_reference, -15.0)
        self.assertEqual(
            (
                self.result.alternate_primary_positive_round_count,
                self.result.alternate_primary_negative_round_count,
            ),
            (2, 20),
        )
        self.assertEqual(
            self.result.alternate_primary_changed_from_initial_reward_seeds,
            (),
        )
        self.assertEqual(
            self.result.alternate_primary_changed_from_reference_reward_seeds,
            (58,),
        )

    def test_alternate_replication_retains_initial_rewards_not_reference_improvement(self) -> None:
        self.assertEqual(
            self.result.alternate_final_replication_raw_rewards,
            self.result.initial_replication_raw_rewards,
        )
        self.assertEqual(self.result.alternate_final_replication_raw_sum, -1056.0)
        self.assertEqual(self.result.alternate_replication_delta_from_initial, 0.0)
        self.assertEqual(
            self.result.alternate_replication_delta_from_reference,
            -121.0,
        )
        self.assertEqual(
            (
                self.result.alternate_replication_positive_round_count,
                self.result.alternate_replication_negative_round_count,
            ),
            (0, 19),
        )
        self.assertEqual(
            self.result.alternate_replication_changed_from_initial_reward_seeds,
            (),
        )
        self.assertEqual(
            self.result.alternate_replication_changed_from_reference_reward_seeds,
            (103, 113),
        )

    def test_final_evaluation_records_are_complete(self) -> None:
        expected_primary_counts = (
            78, 58, 64, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 88, 51, 81,
            14, 45, 18, 80, 29, 52, 28, 61, 70, 74, 71, 22, 89, 85, 77, 58,
        )
        expected_replication_counts = (
            38, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 66, 88, 55,
            84, 35, 60, 87, 81, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
        )
        for counts, traces, scores, expected_counts in (
            (
                self.result.alternate_final_primary_transition_counts,
                self.result.alternate_final_primary_project_action_traces,
                self.result.alternate_final_primary_final_scores,
                expected_primary_counts,
            ),
            (
                self.result.alternate_final_replication_transition_counts,
                self.result.alternate_final_replication_project_action_traces,
                self.result.alternate_final_replication_final_scores,
                expected_replication_counts,
            ),
        ):
            self.assertEqual(counts, expected_counts)
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
            "P8 local exact two-training-protocol deterministic sensitivity diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "the reviewed reference training branch is not rerun",
            "evaluation occurs only after all 128 alternate attempts",
            "retained regardless of sign and never selected",
            "reference fixed-window improvements do not reproduce",
            "two training protocols are not robust or generalization evidence",
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
                MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError,
                "pinned alternate-training sensitivity runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke()

    def test_source_forbids_reference_rerun_selection_and_open_ended_training(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("_PASS_COUNT = 4", source)
        self.assertEqual(source.count("_evaluate("), 2)
        self.assertIn("for _pass_index in range(_PASS_COUNT):", source)
        self.assertIn("reference_training_branch_rerun_count=0", source)
        self.assertIn("selected_training_protocol_id=None", source)
        self.assertNotIn(
            "run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke",
            source,
        )
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
