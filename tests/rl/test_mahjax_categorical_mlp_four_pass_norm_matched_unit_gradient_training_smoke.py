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

import mjlabai.rl.mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke as smoke_module  # noqa: E402,E501
from mjlabai.rl.mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke import (  # noqa: E402,E501
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_PASS_COUNT,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_TRAINING_SMOKE_VERSION,
    MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult,
    MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError,
    MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult,
    run_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke,
)


class MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_TRAINING_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_PASS_COUNT",
                "MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError",
                "MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult",
                "MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult",
                "run_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult,
        )
        self.assertTrue(
            all(
                isinstance(
                    item,
                    MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult,
                )
                for item in self.result.passes
            )
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_TRAINING_SMOKE_VERSION,
        )
        for value in (self.result, *self.result.passes):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("gradients", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.training_update_count = 5  # type: ignore[misc]

    def test_exact_four_pass_continuity_and_counts(self) -> None:
        self.assertEqual(
            self.result.pass_count,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_PASS_COUNT,
        )
        self.assertEqual(tuple(item.pass_index for item in self.result.passes), tuple(range(4)))
        self.assertEqual(self.result.total_training_trajectory_count, 256)
        self.assertEqual(self.result.training_update_count, 4)
        self.assertEqual(self.result.evaluation_call_count, 2)
        self.assertEqual(self.result.evaluation_update_count, 0)
        for item in self.result.passes:
            self.assertEqual(item.reference.training_seeds, tuple(range(32)))
            self.assertEqual(item.alternate.training_seeds, tuple(range(116, 148)))
            self.assertEqual(item.reference.trajectory_count, 32)
            self.assertEqual(item.alternate.trajectory_count, 32)

    def test_every_pass_has_exact_norm_match_and_nonzero_update(self) -> None:
        for item in self.result.passes:
            self.assertTrue(
                item.unit_norm_aggregate_alignment.all_source_gradients_finite_and_nonzero
            )
            self.assertTrue(item.unit_norm_aggregate_alignment.all_values_finite)
            self.assertTrue(item.geometry.all_values_finite)
            self.assertTrue(item.geometry.all_required_norms_nonzero)
            self.assertAlmostEqual(item.geometry.update_rate, 0.32)
            self.assertAlmostEqual(
                item.geometry.raw_combined_global_l2,
                item.geometry.scaled_unit_combined_global_l2,
                delta=1e-8,
            )
            self.assertTrue(
                all(value > 0.0 for value in item.geometry.parameter_delta_l2)
            )
        for actual, expected in zip(
            (
                item.unit_norm_aggregate_alignment.cross_protocol_cosine_similarity
                for item in self.result.passes
            ),
            (
                0.2355091236577188,
                -0.016413511736346326,
                0.269680770514542,
                0.31668333732574877,
            ),
        ):
            self.assertAlmostEqual(actual, expected)
        for actual, expected in zip(
            (item.geometry.norm_match_scale for item in self.result.passes),
            (
                0.11023811489123071,
                0.13533348200686113,
                0.12073883102817982,
                0.12160307419404992,
            ),
        ):
            self.assertAlmostEqual(actual, expected)

    def test_final_only_windows_retain_complete_outputs(self) -> None:
        self.assertEqual(self.result.primary_evaluation_seeds, tuple(range(52, 84)))
        self.assertEqual(self.result.replication_evaluation_seeds, tuple(range(84, 116)))
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
        self.assertEqual(self.result.final_primary_raw_sum, sum(self.result.primary_raw_rewards))
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
        self.assertEqual(self.result.final_replication_raw_sum, -1133.0)
        self.assertEqual(self.result.replication_delta_from_initial, -77.0)
        self.assertEqual(self.result.primary_changed_from_initial_reward_seeds, ())
        self.assertEqual(
            self.result.replication_changed_from_initial_reward_seeds,
            (92,),
        )

    def test_no_selection_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_scale)
        self.assertIsNone(self.result.selected_seed)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact four-pass norm-matched unit-gradient training/fixed-window diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one shared policy branch and exactly four ordered passes",
            "all 64 gradients receive identical unit-norm treatment on every pass",
            "one fixed rate 0.32 update per pass and no intermediate evaluation",
            "all pass and final outcomes are retained and no selection",
            "no fifth pass, projection, clipping, epsilon or per-seed weight",
            "no pass, scale, rate, seed, window, optimizer or protocol search",
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
                MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError,
                "pinned four-pass norm-matched unit-gradient runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke()

    def test_source_forbids_search_selection_and_intermediate_evaluation(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertEqual(source.count("_collect_protocol_gradients("), 2)
        self.assertEqual(source.count("_build_norm_matched_update("), 1)
        self.assertEqual(source.count("_evaluate("), 2)
        self.assertIn("for pass_index in range(", source)
        self.assertIn("parameters = updated_parameters", source)
        self.assertNotIn("while ", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "projection_candidates",
            "pass_candidates",
            "scale_candidates",
            "learning_rate_candidates",
            "selected_pass_index =",
            "selected_scale =",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
