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

import mjlabai.rl.mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke as smoke_module  # noqa: E402,E501
from mjlabai.rl.mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke import (  # noqa: E402,E501
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE,
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_SMOKE_VERSION,
    MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult,
    MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError,
    MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry,
    run_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke,
)


class MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE",
                "MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError",
                "MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry",
                "MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult",
                "run_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult,
        )
        self.assertIsInstance(
            self.result.geometry,
            MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_SMOKE_VERSION,
        )
        for value in (self.result, self.result.geometry):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("gradients", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.training_update_count = 2  # type: ignore[misc]

    def test_exact_batches_update_and_evaluation_counts(self) -> None:
        self.assertEqual(self.result.reference.training_seeds, tuple(range(32)))
        self.assertEqual(self.result.alternate.training_seeds, tuple(range(116, 148)))
        self.assertEqual(self.result.total_training_trajectory_count, 64)
        self.assertEqual(self.result.training_update_count, 1)
        self.assertEqual(self.result.evaluation_call_count, 2)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertEqual(self.result.primary_evaluation_seeds, tuple(range(52, 84)))
        self.assertEqual(
            self.result.replication_evaluation_seeds,
            tuple(range(84, 116)),
        )

    def test_norm_match_geometry_is_complete(self) -> None:
        geometry = self.result.geometry
        self.assertEqual(
            geometry.update_rate,
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE,
        )
        self.assertTrue(geometry.all_values_finite)
        self.assertTrue(geometry.all_required_norms_nonzero)
        self.assertAlmostEqual(
            geometry.raw_combined_global_l2,
            geometry.scaled_unit_combined_global_l2,
            places=8,
        )
        self.assertGreater(geometry.norm_match_scale, 0.0)
        self.assertTrue(all(value > 0.0 for value in geometry.parameter_delta_l2))
        self.assertGreater(
            self.result.unit_norm_aggregate_alignment.cross_protocol_cosine_similarity,
            0.0,
        )
        self.assertAlmostEqual(geometry.raw_combined_global_l2, 0.017651899867127615)
        self.assertAlmostEqual(
            geometry.unit_combined_global_l2_before_scale,
            0.16012519702957836,
        )
        self.assertAlmostEqual(geometry.norm_match_scale, 0.11023811489123071)
        self.assertAlmostEqual(
            geometry.scaled_unit_combined_global_l2,
            0.017651901635441395,
        )
        self.assertAlmostEqual(
            self.result.unit_norm_aggregate_alignment.cross_protocol_cosine_similarity,
            0.2355091236577188,
        )

    def test_fixed_windows_retain_complete_outputs(self) -> None:
        for seeds, counts, traces, rewards, scores in (
            (
                self.result.primary_evaluation_seeds,
                self.result.primary_transition_counts,
                self.result.primary_project_action_traces,
                self.result.primary_raw_rewards,
                self.result.primary_final_scores,
            ),
            (
                self.result.replication_evaluation_seeds,
                self.result.replication_transition_counts,
                self.result.replication_project_action_traces,
                self.result.replication_raw_rewards,
                self.result.replication_final_scores,
            ),
        ):
            self.assertEqual(len(seeds), 32)
            self.assertEqual(len(counts), 32)
            self.assertEqual(len(traces), 32)
            self.assertEqual(len(rewards), 32)
            self.assertEqual(len(scores), 32)
            self.assertTrue(all(0 < len(trace) <= count for trace, count in zip(traces, counts)))

    def test_reward_sums_and_changed_seed_records_are_consistent(self) -> None:
        self.assertEqual(
            self.result.final_primary_raw_sum,
            sum(self.result.primary_raw_rewards),
        )
        self.assertEqual(
            self.result.final_replication_raw_sum,
            sum(self.result.replication_raw_rewards),
        )
        self.assertEqual(
            self.result.primary_delta_from_initial,
            self.result.final_primary_raw_sum - self.result.initial_primary_raw_sum,
        )
        self.assertEqual(
            self.result.replication_delta_from_initial,
            self.result.final_replication_raw_sum
            - self.result.initial_replication_raw_sum,
        )
        self.assertEqual(self.result.initial_primary_raw_sum, -312.0)
        self.assertEqual(self.result.final_primary_raw_sum, -312.0)
        self.assertEqual(self.result.primary_delta_from_initial, 0.0)
        self.assertEqual(self.result.initial_replication_raw_sum, -1056.0)
        self.assertEqual(self.result.final_replication_raw_sum, -1056.0)
        self.assertEqual(self.result.replication_delta_from_initial, 0.0)
        self.assertEqual(self.result.primary_changed_from_initial_reward_seeds, ())
        self.assertEqual(
            self.result.replication_changed_from_initial_reward_seeds,
            (),
        )

    def test_no_selection_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_scale)
        self.assertIsNone(self.result.selected_seed)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact first-pass norm-matched unit-gradient one-step behavior diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "all 64 full trajectory gradients receive identical unit-norm treatment",
            "matched once to the raw combined global norm",
            "one shared update at fixed rate 0.32 only",
            "retained regardless of sign and no selection",
            "no second update, projection, clipping, epsilon or per-seed weight",
            "no scale, rate, seed, window, optimizer or protocol search",
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
                MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError,
                "pinned norm-matched unit-gradient runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke()

    def test_source_forbids_search_selection_and_open_ended_work(self) -> None:
        source = inspect.getsource(smoke_module)
        update_source = inspect.getsource(smoke_module._build_norm_matched_update)
        self.assertEqual(source.count("_collect_protocol_gradients("), 2)
        self.assertEqual(source.count("_evaluate("), 2)
        self.assertIn("raw_global_norm / unit_global_norm", update_source)
        self.assertEqual(source.count("updated_parameters ="), 1)
        self.assertNotIn("while ", source)
        self.assertNotIn("epsilon", update_source.lower())
        self.assertNotIn("clip", update_source.lower())
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "projection_candidates",
            "scale_candidates",
            "learning_rate_candidates",
            "selected_scale =",
            "selected_seed =",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
