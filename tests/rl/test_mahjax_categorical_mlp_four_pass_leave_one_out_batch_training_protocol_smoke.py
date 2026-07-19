from __future__ import annotations

from dataclasses import FrozenInstanceError, fields, is_dataclass
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_TRAINING_PROTOCOL_SMOKE_VERSION,
    MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult,
    MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult,
    MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError,
    run_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke,
)


class MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_TRAINING_PROTOCOL_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError",
                "MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult",
                "MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult",
                "run_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_TRAINING_PROTOCOL_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result.reference,
            MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult,
        )
        self.assertIsInstance(
            self.result.alternate,
            MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult,
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.selected_training_protocol_id = "reference"  # type: ignore[misc]
        for value in (self.result, self.result.reference, self.result.alternate):
            self.assertNotIn("parameters", {field.name for field in fields(value)})
            self.assertTrue(is_dataclass(value))

    def test_exact_two_protocol_four_pass_batch_contract(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
            tuple(range(32)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
            tuple(range(116, 148)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
            tuple(range(52, 84)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
            tuple(range(84, 116)),
        )
        self.assertEqual(self.result.pass_count, 4)
        self.assertEqual(self.result.trajectories_per_pass, 32)
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.total_training_trajectory_count, 256)
        self.assertEqual(self.result.total_training_update_count, 8)
        self.assertEqual(self.result.evaluation_call_count, 4)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertTrue(self.result.all_seed_sets_pairwise_disjoint)
        for branch in (self.result.reference, self.result.alternate):
            self.assertEqual(branch.pass_count, 4)
            self.assertEqual(branch.trajectory_count, 128)
            self.assertEqual(branch.update_count, 4)
            self.assertEqual(tuple(map(len, branch.per_pass_transition_counts)), (32,) * 4)

    def test_leave_one_out_baselines_exclude_current_trajectory(self) -> None:
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
                        expected_baseline = sum(
                            other[seat]
                            for other_index, other in enumerate(normalized)
                            if other_index != row_index
                        ) / 31
                        self.assertAlmostEqual(
                            baseline[seat], expected_baseline, places=12
                        )
                        self.assertAlmostEqual(
                            advantage[seat], row[seat] - expected_baseline, places=12
                        )
                for seat in range(4):
                    self.assertAlmostEqual(
                        sum(row[seat] for row in advantages), 0.0, places=12
                    )

    def test_reference_expected_objectives_deltas_and_training_sums(self) -> None:
        branch = self.result.reference
        expected_initial = (
            -0.0085045587,
            -0.0085126634,
            -0.0084424117,
            -0.0182129891,
        )
        expected_post = (
            -0.0085126634,
            -0.0085207718,
            -0.0084506209,
            -0.0182186403,
        )
        for actual, expected in zip(branch.per_pass_batch_initial_objectives, expected_initial):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(branch.per_pass_batch_post_update_objectives, expected_post):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            branch.final_parameter_delta_l2,
            (0.0004183974, 0.0000731221, 0.0009828927, 0.0001114113),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertEqual(
            tuple(
                tuple(sum(row[seat] for row in rows) for seat in range(4))
                for rows in branch.per_pass_cumulative_raw_rewards
            ),
            (
                (-55.0, -34.0, -150.0, 179.0),
                (-55.0, -34.0, -150.0, 179.0),
                (-55.0, -34.0, -150.0, 179.0),
                (-35.0, -104.0, -210.0, 289.0),
            ),
        )

    def test_alternate_expected_objectives_deltas_and_training_sums(self) -> None:
        branch = self.result.alternate
        expected_initial = (
            -0.0105261516,
            -0.0105333736,
            -0.0105405992,
            -0.0105478288,
        )
        expected_post = (
            -0.0105333736,
            -0.0105405992,
            -0.0105478288,
            -0.0105550605,
        )
        for actual, expected in zip(branch.per_pass_batch_initial_objectives, expected_initial):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(branch.per_pass_batch_post_update_objectives, expected_post):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            branch.final_parameter_delta_l2,
            (0.0003831175, 0.0000831156, 0.0009945069, 0.0001161640),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertEqual(
            tuple(
                tuple(sum(row[seat] for row in rows) for seat in range(4))
                for rows in branch.per_pass_cumulative_raw_rewards
            ),
            ((130.0, 90.0, 6.0, -286.0),) * 4,
        )

    def test_both_protocols_change_parameters_but_retain_initial_evaluation_rewards(self) -> None:
        for branch in (self.result.reference, self.result.alternate):
            self.assertTrue(branch.parameters_changed)
            self.assertEqual(branch.final_primary_raw_sum, -312.0)
            self.assertEqual(branch.primary_delta_from_initial, 0.0)
            self.assertEqual(
                (branch.primary_positive_round_count, branch.primary_negative_round_count),
                (2, 20),
            )
            self.assertEqual(branch.primary_changed_from_initial_reward_seeds, ())
            self.assertEqual(branch.final_replication_raw_sum, -1056.0)
            self.assertEqual(branch.replication_delta_from_initial, 0.0)
            self.assertEqual(
                (
                    branch.replication_positive_round_count,
                    branch.replication_negative_round_count,
                ),
                (0, 19),
            )
            self.assertEqual(branch.replication_changed_from_initial_reward_seeds, ())
        self.assertEqual(
            self.result.reference.final_primary_raw_rewards,
            self.result.alternate.final_primary_raw_rewards,
        )
        self.assertEqual(
            self.result.reference.final_replication_raw_rewards,
            self.result.alternate.final_replication_raw_rewards,
        )

    def test_complete_training_and_evaluation_records_are_legal(self) -> None:
        expected_primary_counts = (
            78, 58, 63, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 90, 51, 81,
            14, 45, 18, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
        )
        expected_replication_counts = (
            37, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
            84, 35, 60, 87, 82, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
        )
        for branch in (self.result.reference, self.result.alternate):
            self.assertTrue(branch.all_training_actions_legal)
            self.assertTrue(branch.all_rounds_terminated)
            self.assertEqual(branch.final_primary_transition_counts, expected_primary_counts)
            self.assertEqual(
                branch.final_replication_transition_counts,
                expected_replication_counts,
            )
            for counts, actions, legal_rows in zip(
                branch.per_pass_transition_counts,
                branch.per_pass_action_traces,
                branch.per_pass_legal_action_traces,
            ):
                self.assertEqual(tuple(map(len, actions)), counts)
                for action_trace, legal_trace in zip(actions, legal_rows):
                    self.assertEqual(len(action_trace), len(legal_trace))
                    self.assertTrue(
                        all(
                            action in legal
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
            "P8 local exact two-protocol leave-one-out batch-baseline variance diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "collects all 32 trajectories before one aggregate update",
            "other 31 same-seat returns only",
            "all outcomes are retained regardless of sign",
            "no third protocol, seed search, fifth pass",
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
                MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError,
                "pinned leave-one-out batch diagnostic runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke()

    def test_source_forbids_online_updates_selection_and_open_ended_work(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("_PASS_COUNT = 4", source)
        self.assertIn("_TRAJECTORIES_PER_PASS = 32", source)
        self.assertIn("for _pass_index in range(_PASS_COUNT):", source)
        self.assertIn("pass_parameters = parameters", source)
        self.assertEqual(source.count("_evaluate("), 2)
        self.assertIn("selected_training_protocol_id=None", source)
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
