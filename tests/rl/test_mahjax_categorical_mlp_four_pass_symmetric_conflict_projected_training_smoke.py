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

import mjlabai.rl.mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke as smoke_module  # noqa: E402,E501
from mjlabai.rl.mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke import (  # noqa: E402,E501
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SYMMETRIC_CONFLICT_PROJECTED_TRAINING_SMOKE_VERSION,
    MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult,
    MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError,
    MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult,
    run_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke,
)


class MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SYMMETRIC_CONFLICT_PROJECTED_TRAINING_SMOKE_VERSION",
                "MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError",
                "MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult",
                "MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult",
                "run_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SYMMETRIC_CONFLICT_PROJECTED_TRAINING_SMOKE_VERSION,
        )
        self.assertTrue(
            all(
                isinstance(item, MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult)
                for item in self.result.passes
            )
        )
        for value in (
            self.result,
            *self.result.passes,
            *(item.reference for item in self.result.passes),
            *(item.alternate for item in self.result.passes),
            *(item.geometry for item in self.result.passes),
        ):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("gradients", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.pass_count = 5  # type: ignore[misc]

    def test_exact_pass_batch_update_and_evaluation_counts(self) -> None:
        self.assertEqual(self.result.pass_count, 4)
        self.assertEqual(self.result.trajectories_per_protocol_per_pass, 32)
        self.assertEqual(self.result.total_training_trajectory_count, 256)
        self.assertEqual(self.result.training_update_count, 4)
        self.assertEqual(self.result.intermediate_evaluation_call_count, 0)
        self.assertEqual(self.result.evaluation_call_count, 2)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertEqual(self.result.primary_evaluation_seeds, tuple(range(52, 84)))
        self.assertEqual(
            self.result.replication_evaluation_seeds,
            tuple(range(84, 116)),
        )
        self.assertTrue(self.result.all_seed_sets_pairwise_disjoint)
        for pass_index, item in enumerate(self.result.passes):
            self.assertEqual(item.pass_index, pass_index)
            self.assertEqual(item.reference.training_seeds, tuple(range(32)))
            self.assertEqual(item.alternate.training_seeds, tuple(range(116, 148)))
            self.assertEqual(item.reference.trajectory_count, 32)
            self.assertEqual(item.alternate.trajectory_count, 32)

    def test_all_four_pass_gradient_signs_and_geometry_are_pinned(self) -> None:
        expected_original_cosines = (
            -0.18687750082306825,
            -0.14942482899110554,
            -0.4011737460616803,
            -0.3252072255045935,
        )
        expected_projected_cosines = (
            0.18687816233561955,
            0.14942474248546794,
            0.40117368232699746,
            0.3252071743795551,
        )
        expected_combined_norms = (
            0.020943923926851044,
            0.020351296588768303,
            0.021302940176116714,
            0.025686131890207718,
        )
        for item, original, projected, combined in zip(
            self.result.passes,
            expected_original_cosines,
            expected_projected_cosines,
            expected_combined_norms,
        ):
            geometry = item.geometry
            self.assertAlmostEqual(
                geometry.original_global_cosine_similarity,
                original,
                places=6,
            )
            self.assertAlmostEqual(
                geometry.projected_global_cosine_similarity,
                projected,
                places=6,
            )
            self.assertAlmostEqual(geometry.combined_global_l2, combined, places=6)
            self.assertLess(geometry.original_global_dot_product, 0.0)
            self.assertLess(geometry.original_global_cosine_similarity, 0.0)
            self.assertGreater(geometry.projected_global_dot_product, 0.0)
            self.assertGreater(geometry.projected_global_cosine_similarity, 0.0)
            self.assertEqual(geometry.update_rate, 0.32)
            self.assertTrue(geometry.all_values_finite)
            self.assertTrue(geometry.all_required_norms_nonzero)

    def test_shared_parameter_continuity_and_final_delta_are_exact(self) -> None:
        self.assertEqual(
            self.result.passes[0].start_parameter_delta_from_initial_l2,
            (0.0, 0.0, 0.0, 0.0),
        )
        for previous, current in zip(self.result.passes, self.result.passes[1:]):
            self.assertEqual(
                current.start_parameter_delta_from_initial_l2,
                previous.end_parameter_delta_from_initial_l2,
            )
        expected_final_delta = (
            0.010112007148563862,
            0.002028877381235361,
            0.024002619087696075,
            0.0027637341991066933,
        )
        self.assertEqual(
            self.result.passes[-1].end_parameter_delta_from_initial_l2,
            self.result.final_parameter_delta_l2,
        )
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            expected_final_delta,
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertTrue(all(value > 0.0 for value in self.result.final_parameter_delta_l2))

    def test_final_fixed_windows_retain_primary_and_degrade_replication(self) -> None:
        self.assertEqual(self.result.initial_primary_raw_sum, -312.0)
        self.assertEqual(self.result.final_primary_raw_sum, -312.0)
        self.assertEqual(self.result.primary_delta_from_initial, 0.0)
        self.assertEqual(self.result.primary_changed_from_initial_reward_seeds, ())
        self.assertEqual(self.result.initial_replication_raw_sum, -1056.0)
        self.assertEqual(self.result.final_replication_raw_sum, -1133.0)
        self.assertEqual(self.result.replication_delta_from_initial, -77.0)
        self.assertEqual(
            self.result.replication_changed_from_initial_reward_seeds,
            (92,),
        )
        self.assertEqual(len(self.result.primary_raw_rewards), 32)
        self.assertEqual(len(self.result.replication_raw_rewards), 32)
        self.assertEqual(len(self.result.primary_transition_counts), 32)
        self.assertEqual(len(self.result.replication_transition_counts), 32)

    def test_training_and_evaluation_provenance_is_complete(self) -> None:
        for item in self.result.passes:
            for branch in (item.reference, item.alternate):
                self.assertTrue(branch.all_training_actions_legal)
                self.assertTrue(branch.all_rounds_terminated)
                self.assertTrue(branch.all_advantage_sums_centered)
                self.assertEqual(len(branch.action_trace_sha256), 32)
        for counts, traces, scores in (
            (
                self.result.primary_transition_counts,
                self.result.primary_project_action_traces,
                self.result.primary_final_scores,
            ),
            (
                self.result.replication_transition_counts,
                self.result.replication_project_action_traces,
                self.result.replication_final_scores,
            ),
        ):
            self.assertTrue(
                all(0 < len(trace) <= count for trace, count in zip(traces, counts))
            )
            self.assertEqual(len(scores), 32)

    def test_no_selection_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_multiplier)
        self.assertIsNone(self.result.selected_projection_id)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact four-pass shared-policy symmetric conflict-projected training diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one shared branch and exactly four",
            "same simultaneous symmetric projection and one update",
            "all update rates are fixed at 0.32",
            "no intermediate evaluation, pass selection or checkpoint selection",
            "no fifth pass, third protocol, seed search",
            "no formula, order, coefficient, rate, optimizer or exploration search",
            "not robustness, generalization, policy-quality or model-strength",
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
                MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError,
                "pinned four-pass conflict-projected runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke()

    def test_source_forbids_search_intermediate_evaluation_and_open_work(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertEqual(source.count("_summarize_protocol("), 2)
        self.assertEqual(source.count("_apply_symmetric_conflict_projected_update("), 1)
        self.assertEqual(source.count("_evaluate("), 2)
        self.assertIn("for pass_index in range(_PASS_COUNT):", source)
        self.assertNotIn("while ", source)
        self.assertNotIn("random.shuffle", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "projection_candidates",
            "coefficient_candidates",
            "learning_rate_candidates",
            "multiplier_candidates",
            "temperature_candidates",
            "entropy_candidates",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
