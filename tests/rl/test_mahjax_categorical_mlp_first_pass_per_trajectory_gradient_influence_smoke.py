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

import mjlabai.rl.mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke as smoke_module  # noqa: E402,E501
import mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke as batch_module  # noqa: E402,E501
from mjlabai.rl.mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke import (  # noqa: E402,E501
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_PER_TRAJECTORY_GRADIENT_INFLUENCE_SMOKE_VERSION,
    MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult,
    MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError,
    MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult,
    MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult,
    MahJaxCategoricalMlpTrajectoryGradientInfluenceResult,
    MahJaxCategoricalMlpUnitNormAggregateAlignmentResult,
    run_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke,
)


class MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_PER_TRAJECTORY_GRADIENT_INFLUENCE_SMOKE_VERSION",
                "MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError",
                "MahJaxCategoricalMlpTrajectoryGradientInfluenceResult",
                "MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult",
                "MahJaxCategoricalMlpUnitNormAggregateAlignmentResult",
                "MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult",
                "MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult",
                "run_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult,
        )
        self.assertIsInstance(
            self.result.unit_norm_aggregate_alignment,
            MahJaxCategoricalMlpUnitNormAggregateAlignmentResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_PER_TRAJECTORY_GRADIENT_INFLUENCE_SMOKE_VERSION,
        )
        for protocol in (self.result.reference, self.result.alternate):
            self.assertIsInstance(
                protocol,
                MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult,
            )
            self.assertTrue(
                all(
                    isinstance(
                        item,
                        MahJaxCategoricalMlpTrajectoryGradientInfluenceResult,
                    )
                    for item in protocol.trajectories
                )
            )
            self.assertIsInstance(
                protocol.opposite_alignment_magnitude_concentration,
                MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult,
            )
        for value in (
            self.result,
            self.result.reference,
            self.result.alternate,
            self.result.unit_norm_aggregate_alignment,
            *self.result.reference.trajectories,
            *self.result.alternate.trajectories,
        ):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("gradients", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.training_update_count = 1  # type: ignore[misc]

    def test_exact_batch_and_zero_update_evaluation_counts(self) -> None:
        self.assertEqual(self.result.trajectories_per_protocol, 32)
        self.assertEqual(self.result.total_training_trajectory_count, 64)
        self.assertEqual(self.result.training_update_count, 0)
        self.assertEqual(self.result.evaluation_call_count, 0)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertEqual(self.result.reference.training_seeds, tuple(range(32)))
        self.assertEqual(
            self.result.alternate.training_seeds,
            tuple(range(116, 148)),
        )
        self.assertFalse(
            set(self.result.reference.training_seeds)
            & set(self.result.alternate.training_seeds)
        )

    def test_exact_aggregate_geometry_is_preserved(self) -> None:
        self.assertAlmostEqual(
            self.result.aggregate_global_gradient_dot_product,
            -0.0001429308561853304,
            places=9,
        )
        self.assertAlmostEqual(
            self.result.aggregate_global_gradient_cosine_similarity,
            -0.18687683284469966,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.reference.aggregate_global_gradient_l2,
            0.028464037702741144,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.alternate.aggregate_global_gradient_l2,
            0.026870393353875678,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.reference.batch_initial_objective,
            -0.008504558742060908,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.alternate.batch_initial_objective,
            -0.010526151631779612,
            places=6,
        )

    def test_opposite_alignment_is_mixed_across_both_protocols(self) -> None:
        self.assertEqual(
            self.result.reference.own_alignment_sign_counts,
            (13, 0, 19),
        )
        self.assertEqual(
            self.result.reference.opposite_alignment_sign_counts,
            (14, 0, 18),
        )
        self.assertEqual(
            self.result.alternate.own_alignment_sign_counts,
            (7, 0, 25),
        )
        self.assertEqual(
            self.result.alternate.opposite_alignment_sign_counts,
            (18, 0, 14),
        )
        for protocol in (self.result.reference, self.result.alternate):
            self.assertEqual(sum(protocol.own_alignment_sign_counts), 32)
            self.assertEqual(sum(protocol.opposite_alignment_sign_counts), 32)
            self.assertGreater(protocol.opposite_alignment_sign_counts[0], 0)
            self.assertGreater(protocol.opposite_alignment_sign_counts[2], 0)

    def test_opposite_alignment_magnitude_concentration_is_pinned(self) -> None:
        reference = self.result.reference.opposite_alignment_magnitude_concentration
        alternate = self.result.alternate.opposite_alignment_magnitude_concentration
        self.assertEqual(reference.contribution_count, 32)
        self.assertEqual(alternate.contribution_count, 32)
        self.assertAlmostEqual(
            reference.signed_mean,
            self.result.aggregate_global_gradient_dot_product,
            places=8,
        )
        self.assertAlmostEqual(
            alternate.signed_mean,
            self.result.aggregate_global_gradient_dot_product,
            places=8,
        )
        self.assertAlmostEqual(reference.effective_contribution_count, 12.063341748289508)
        self.assertAlmostEqual(alternate.effective_contribution_count, 5.153621597928097)
        self.assertAlmostEqual(reference.largest_absolute_share, 0.16033531920600053)
        self.assertAlmostEqual(alternate.largest_absolute_share, 0.4158428046888921)
        self.assertAlmostEqual(reference.top_four_absolute_share, 0.4870449948159291)
        self.assertAlmostEqual(alternate.top_four_absolute_share, 0.5942865543230846)
        self.assertAlmostEqual(reference.top_eight_absolute_share, 0.7174696416854126)
        self.assertAlmostEqual(alternate.top_eight_absolute_share, 0.7457630373122845)
        for summary in (reference, alternate):
            self.assertAlmostEqual(
                summary.absolute_sum,
                summary.positive_sum + summary.absolute_negative_sum,
            )
            self.assertGreater(summary.net_cancellation_ratio, 0.0)
            self.assertLess(summary.net_cancellation_ratio, 1.0)
            self.assertGreater(summary.absolute_contribution_hhi, 0.0)
            self.assertLessEqual(summary.top_four_absolute_share, 1.0)
            self.assertLessEqual(summary.top_eight_absolute_share, 1.0)

    def test_unit_norm_aggregate_alignment_is_complete_and_finite(self) -> None:
        alignment = self.result.unit_norm_aggregate_alignment
        self.assertEqual(alignment.contribution_count_per_protocol, 32)
        self.assertEqual(
            len(alignment.reference_parameter_group_gradient_l2),
            len(self.result.reference.parameter_group_shapes),
        )
        self.assertEqual(
            len(alignment.alternate_parameter_group_gradient_l2),
            len(self.result.alternate.parameter_group_shapes),
        )
        self.assertTrue(alignment.all_source_gradients_finite_and_nonzero)
        self.assertTrue(alignment.all_values_finite)
        self.assertGreater(alignment.reference_global_gradient_l2, 0.0)
        self.assertGreater(alignment.alternate_global_gradient_l2, 0.0)
        self.assertIsNotNone(alignment.cross_protocol_cosine_similarity)
        self.assertGreaterEqual(alignment.cross_protocol_cosine_similarity, -1.0)
        self.assertLessEqual(alignment.cross_protocol_cosine_similarity, 1.0)
        self.assertAlmostEqual(
            alignment.reference_global_gradient_l2,
            0.16546103181537164,
        )
        self.assertAlmostEqual(
            alignment.alternate_global_gradient_l2,
            0.23798262889766802,
        )
        self.assertAlmostEqual(
            alignment.cross_protocol_dot_product,
            0.00927360774949193,
        )
        self.assertAlmostEqual(
            alignment.cross_protocol_cosine_similarity,
            0.2355091236577188,
        )
        self.assertLess(
            self.result.aggregate_global_gradient_cosine_similarity,
            0.0,
        )
        self.assertGreater(alignment.cross_protocol_cosine_similarity, 0.0)

    def test_all_64_trajectory_influences_and_provenance_are_retained(self) -> None:
        for protocol in (self.result.reference, self.result.alternate):
            self.assertEqual(protocol.trajectory_count, 32)
            self.assertEqual(
                tuple(item.seed for item in protocol.trajectories),
                protocol.training_seeds,
            )
            self.assertEqual(len(protocol.action_trace_sha256), 32)
            self.assertEqual(len(protocol.transition_counts), 32)
            self.assertEqual(len(protocol.cumulative_raw_rewards), 32)
            self.assertEqual(len(protocol.final_scores), 32)
            self.assertEqual(len(protocol.leave_one_out_seat_baselines), 32)
            self.assertEqual(len(protocol.advantage_seat_returns), 32)
            self.assertEqual(len(protocol.initial_trajectory_objectives), 32)
            self.assertTrue(protocol.all_training_actions_legal)
            self.assertTrue(protocol.all_rounds_terminated)
            self.assertTrue(protocol.all_advantage_sums_centered)
            for item, digest, transition_count in zip(
                protocol.trajectories,
                protocol.action_trace_sha256,
                protocol.transition_counts,
            ):
                self.assertEqual(item.action_trace_sha256, digest)
                self.assertEqual(item.transition_count, transition_count)
                self.assertGreater(item.global_gradient_l2, 0.0)
                self.assertTrue(item.all_values_finite)
                self.assertIsNotNone(item.own_aggregate_cosine_similarity)
                self.assertIsNotNone(item.opposite_aggregate_cosine_similarity)

    def test_representative_seed_values_are_deterministic_without_selection(self) -> None:
        reference_first = self.result.reference.trajectories[0]
        alternate_last = self.result.alternate.trajectories[-1]
        self.assertEqual(reference_first.seed, 0)
        self.assertAlmostEqual(reference_first.global_gradient_l2, 0.027014031274606408)
        self.assertAlmostEqual(
            reference_first.opposite_aggregate_cosine_similarity,
            0.18982501243553482,
        )
        self.assertEqual(alternate_last.seed, 147)
        self.assertAlmostEqual(alternate_last.global_gradient_l2, 0.035312303674272655)
        self.assertAlmostEqual(
            alternate_last.opposite_aggregate_cosine_similarity,
            0.20684754905628489,
        )

    def test_no_selection_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_trajectory_seed)
        self.assertIsNone(self.result.selected_gradient_direction)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact first-pass per-trajectory cross-protocol gradient influence diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "all 64 already-computed",
            "own and opposite aggregate mean gradients",
            "unit-norm aggregation weights every one of the same 64 gradients equally",
            "unit-norm geometry is objective-scale diagnosis, not an approved update rule",
            "no threshold is searched",
            "no trajectory is ranked, removed, clipped, selected or promoted",
            "zero parameter updates and zero policy evaluations",
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
                MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError,
                "pinned per-trajectory gradient-influence runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke()

    def test_source_reuses_individual_gradients_and_forbids_open_work(self) -> None:
        source = inspect.getsource(smoke_module)
        batch_source = inspect.getsource(batch_module)
        magnitude_source = inspect.getsource(
            smoke_module._build_magnitude_concentration
        )
        unit_norm_source = inspect.getsource(
            smoke_module._unit_norm_mean_gradients
        )
        self.assertEqual(source.count("_collect_protocol_gradients("), 3)
        self.assertEqual(source.count("_calculate_leave_one_out_batch_gradients("), 1)
        self.assertNotIn("_evaluate(", source)
        self.assertIn("trajectory_gradients.append(gradients)", batch_source)
        self.assertIn("trajectory_gradients=tuple(trajectory_gradients)", batch_source)
        self.assertEqual(source.count("sorted("), 1)
        self.assertIn(
            "sorted(absolute_values, reverse=True)",
            magnitude_source,
        )
        self.assertIn("value / global_norm", unit_norm_source)
        self.assertIn("/ _TRAJECTORIES_PER_PROTOCOL", unit_norm_source)
        self.assertNotIn("epsilon", unit_norm_source.lower())
        self.assertNotIn("clip", unit_norm_source.lower())
        self.assertNotIn("while ", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "selected_trajectory =",
            "ranking",
            "learning_rate_candidates",
            "projection_candidates",
            "temperature_candidates",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
