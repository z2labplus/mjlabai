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

import mjlabai.rl.mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke as smoke_module  # noqa: E402
import mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke as mean_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATED_TRAINING_PROTOCOL_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER,
    MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult,
    MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError,
    run_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke,
)


class MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATED_TRAINING_PROTOCOL_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER",
                "MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError",
                "MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult",
                "run_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATED_TRAINING_PROTOCOL_SMOKE_VERSION,
        )
        for value in (self.result, self.result.reference, self.result.alternate):
            self.assertNotIn("parameters", {field.name for field in fields(value)})
        with self.assertRaises(FrozenInstanceError):
            self.result.batch_gradient_multiplier = 1.0  # type: ignore[misc]

    def test_exact_fixed_multiplier_and_bounded_protocol(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER,
            32.0,
        )
        self.assertEqual(self.result.base_learning_rate, 0.01)
        self.assertEqual(self.result.batch_gradient_multiplier, 32.0)
        self.assertEqual(self.result.effective_mean_gradient_learning_rate, 0.32)
        self.assertEqual(self.result.pass_count, 4)
        self.assertEqual(self.result.trajectories_per_pass, 32)
        self.assertEqual(self.result.total_training_trajectory_count, 256)
        self.assertEqual(self.result.total_training_update_count, 8)
        self.assertEqual(self.result.evaluation_call_count, 4)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertTrue(self.result.all_seed_sets_pairwise_disjoint)
        self.assertEqual(self.result.reference.training_seeds_per_pass, tuple(range(32)))
        self.assertEqual(
            self.result.alternate.training_seeds_per_pass,
            tuple(range(116, 148)),
        )

    def test_leave_one_out_baselines_remain_exact_and_centered(self) -> None:
        for branch in (self.result.reference, self.result.alternate):
            for rewards, baselines, advantages in zip(
                branch.per_pass_cumulative_raw_rewards,
                branch.per_pass_leave_one_out_seat_baselines,
                branch.per_pass_advantage_seat_returns,
            ):
                normalized = tuple(
                    tuple(value / 100.0 for value in row) for row in rewards
                )
                for row_index, (row, baseline, advantage) in enumerate(
                    zip(normalized, baselines, advantages)
                ):
                    for seat in range(4):
                        expected = sum(
                            other[seat]
                            for other_index, other in enumerate(normalized)
                            if other_index != row_index
                        ) / 31
                        self.assertAlmostEqual(baseline[seat], expected, places=12)
                        self.assertAlmostEqual(
                            advantage[seat], row[seat] - expected, places=12
                        )
                for seat in range(4):
                    self.assertAlmostEqual(
                        sum(row[seat] for row in advantages), 0.0, places=12
                    )

    def test_reference_expected_objectives_deltas_and_training_sums(self) -> None:
        branch = self.result.reference
        for actual, expected in zip(
            branch.per_pass_batch_initial_objectives,
            (-0.0085045587, -0.0165455118, -0.0182897860, -0.0174096585),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            branch.per_pass_batch_post_update_objectives,
            (-0.0087652362, -0.0167149225, -0.0184521101, -0.0175859964),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            branch.final_parameter_delta_l2,
            (0.0123636629, 0.0017657150, 0.0261666030, 0.0029413241),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertEqual(
            tuple(
                tuple(sum(row[seat] for row in rows) for seat in range(4))
                for rows in branch.per_pass_cumulative_raw_rewards
            ),
            (
                (-55.0, -34.0, -150.0, 179.0),
                (-19.0, -120.0, -220.0, 279.0),
                (43.0, -125.0, -215.0, 197.0),
                (38.0, -90.0, -240.0, 192.0),
            ),
        )

    def test_alternate_expected_objectives_deltas_and_training_sums(self) -> None:
        branch = self.result.alternate
        for actual, expected in zip(
            branch.per_pass_batch_initial_objectives,
            (-0.0105261516, -0.0112280485, -0.0164435498, -0.0173537340),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            branch.per_pass_batch_post_update_objectives,
            (-0.0107582265, -0.0114182580, -0.0167419830, -0.0176754166),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            branch.final_parameter_delta_l2,
            (0.0121162534, 0.0025018181, 0.0312487930, 0.0036535931),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertEqual(
            tuple(
                tuple(sum(row[seat] for row in rows) for seat in range(4))
                for rows in branch.per_pass_cumulative_raw_rewards
            ),
            (
                (130.0, 90.0, 6.0, -286.0),
                (120.0, 110.0, -4.0, -296.0),
                (176.0, -45.0, -19.0, -212.0),
                (205.0, 104.0, -28.0, -381.0),
            ),
        )

    def test_fixed_compensation_creates_protocol_dependent_outcomes(self) -> None:
        reference = self.result.reference
        alternate = self.result.alternate
        self.assertEqual(reference.primary_delta_from_initial, 54.0)
        self.assertEqual(reference.replication_delta_from_initial, 121.0)
        self.assertEqual(reference.primary_changed_from_initial_reward_seeds, (58, 61))
        self.assertEqual(
            reference.replication_changed_from_initial_reward_seeds,
            (103, 113),
        )
        self.assertEqual(alternate.primary_delta_from_initial, -60.0)
        self.assertEqual(alternate.replication_delta_from_initial, 0.0)
        self.assertEqual(alternate.primary_changed_from_initial_reward_seeds, (73,))
        self.assertEqual(alternate.replication_changed_from_initial_reward_seeds, ())
        self.assertEqual(
            (
                self.result.reviewed_mean_reference_primary_delta,
                self.result.reviewed_mean_reference_replication_delta,
                self.result.reviewed_mean_alternate_primary_delta,
                self.result.reviewed_mean_alternate_replication_delta,
            ),
            (0.0, 0.0, 0.0, 0.0),
        )

    def test_complete_records_are_legal_and_exact(self) -> None:
        expected_reference_primary_counts = (
            78, 58, 63, 67, 58, 76, 86, 36, 86, 75, 27, 70, 67, 87, 51, 81,
            14, 45, 19, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
        )
        expected_alternate_primary_counts = (
            78, 58, 64, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 88, 51, 81,
            14, 45, 18, 80, 29, 90, 28, 61, 70, 75, 71, 22, 89, 85, 77, 58,
        )
        self.assertEqual(
            self.result.reference.final_primary_transition_counts,
            expected_reference_primary_counts,
        )
        self.assertEqual(
            self.result.alternate.final_primary_transition_counts,
            expected_alternate_primary_counts,
        )
        for branch in (self.result.reference, self.result.alternate):
            self.assertTrue(branch.all_training_actions_legal)
            self.assertTrue(branch.all_rounds_terminated)
            self.assertTrue(branch.parameters_changed)
            for counts, actions, legal_rows in zip(
                branch.per_pass_transition_counts,
                branch.per_pass_action_traces,
                branch.per_pass_legal_action_traces,
            ):
                self.assertEqual(tuple(map(len, actions)), counts)
                self.assertTrue(
                    all(
                        action in legal
                        for action_trace, legal_trace in zip(actions, legal_rows)
                        for action, legal in zip(action_trace, legal_trace)
                    )
                )

    def test_no_selection_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact fixed-32x two-protocol batch-size compensation diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "fixed batch-size compensation multiplier 32.0 only",
            "mean-gradient and online branches are not rerun",
            "retained regardless of sign and no protocol is selected",
            "no multiplier search, third protocol, fifth pass",
            "not robustness, generalization, policy-quality",
            "not stable-dan, candidate-promotion, tenhou or luckyj 10.68",
        ):
            self.assertIn(phrase, warning_text)

    def test_wraps_runtime_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("runtime unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError,
                "pinned batch-size-compensated runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke()

    def test_source_preserves_mean_path_and_forbids_search_and_open_ended_work(self) -> None:
        source = inspect.getsource(smoke_module)
        mean_source = inspect.getsource(mean_module)
        self.assertIn("BATCH_SIZE_COMPENSATION_MULTIPLIER = 32.0", source)
        self.assertEqual(source.count("_run_protocol("), 2)
        self.assertNotIn("while ", source)
        self.assertGreaterEqual(mean_source.count("        1.0,"), 2)
        self.assertIn("gradient_multiplier * gradient", mean_source)
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
            "multiplier_candidates",
            "learning_rate_candidates",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
