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

import mjlabai.rl.mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke as smoke_module  # noqa: E402,E501
from mjlabai.rl.mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke import (  # noqa: E402,E501
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE,
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_SMOKE_VERSION,
    MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult,
    MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError,
    MahJaxCategoricalMlpSymmetricConflictProjectionGeometry,
    run_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke,
)


class MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE",
                "MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError",
                "MahJaxCategoricalMlpSymmetricConflictProjectionGeometry",
                "MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult",
                "run_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult,
        )
        self.assertIsInstance(
            self.result.geometry,
            MahJaxCategoricalMlpSymmetricConflictProjectionGeometry,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_SMOKE_VERSION,
        )
        for value in (
            self.result,
            self.result.geometry,
            self.result.reference,
            self.result.alternate,
        ):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("gradients", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.geometry.update_rate = 0.0  # type: ignore[misc]

    def test_exact_batch_update_and_evaluation_counts(self) -> None:
        self.assertEqual(self.result.reference.training_seeds, tuple(range(32)))
        self.assertEqual(
            self.result.alternate.training_seeds,
            tuple(range(116, 148)),
        )
        self.assertEqual(self.result.total_training_trajectory_count, 64)
        self.assertEqual(self.result.training_update_count, 1)
        self.assertEqual(self.result.evaluation_call_count, 2)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertEqual(self.result.primary_evaluation_seeds, tuple(range(52, 84)))
        self.assertEqual(
            self.result.replication_evaluation_seeds,
            tuple(range(84, 116)),
        )

    def test_exact_original_and_projected_gradient_geometry(self) -> None:
        geometry = self.result.geometry
        self.assertAlmostEqual(
            geometry.original_global_dot_product,
            -0.0001429308561853304,
            places=9,
        )
        self.assertAlmostEqual(
            geometry.original_global_cosine_similarity,
            -0.18687750082306825,
            places=6,
        )
        self.assertAlmostEqual(
            geometry.reference_projection_coefficient,
            -0.19796082870996487,
            places=6,
        )
        self.assertAlmostEqual(
            geometry.alternate_projection_coefficient,
            -0.17641470053170136,
            places=6,
        )
        self.assertAlmostEqual(
            geometry.projected_global_dot_product,
            0.00013794030803637725,
            places=9,
        )
        self.assertAlmostEqual(
            geometry.projected_global_cosine_similarity,
            0.18687816233561955,
            places=6,
        )
        self.assertLess(geometry.original_global_cosine_similarity, 0.0)
        self.assertGreater(geometry.projected_global_cosine_similarity, 0.0)
        self.assertTrue(geometry.all_values_finite)
        self.assertTrue(geometry.all_required_norms_nonzero)

    def test_exact_combined_gradient_and_parameter_update(self) -> None:
        geometry = self.result.geometry
        self.assertEqual(
            geometry.update_rate,
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE,
        )
        expected_combined = (
            0.008104180917143822,
            0.0016218236414715648,
            0.01911478489637375,
            0.0022282027639448643,
        )
        expected_delta = (
            0.0025933366268873215,
            0.0005189825315028429,
            0.006116729229688644,
            0.0007130251615308225,
        )
        for actual, expected in zip(
            geometry.combined_parameter_group_l2,
            expected_combined,
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertAlmostEqual(
            geometry.combined_global_l2,
            0.020943923926851044,
            places=6,
        )
        for actual, expected in zip(geometry.parameter_delta_l2, expected_delta):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertTrue(all(value > 0.0 for value in geometry.parameter_delta_l2))

    def test_fixed_windows_retain_initial_reward_vectors(self) -> None:
        self.assertEqual(self.result.initial_primary_raw_sum, -312.0)
        self.assertEqual(self.result.final_primary_raw_sum, -312.0)
        self.assertEqual(self.result.primary_delta_from_initial, 0.0)
        self.assertEqual(self.result.primary_changed_from_initial_reward_seeds, ())
        self.assertEqual(self.result.initial_replication_raw_sum, -1056.0)
        self.assertEqual(self.result.final_replication_raw_sum, -1056.0)
        self.assertEqual(self.result.replication_delta_from_initial, 0.0)
        self.assertEqual(
            self.result.replication_changed_from_initial_reward_seeds,
            (),
        )
        self.assertEqual(len(self.result.primary_raw_rewards), 32)
        self.assertEqual(len(self.result.replication_raw_rewards), 32)
        self.assertEqual(len(self.result.primary_transition_counts), 32)
        self.assertEqual(len(self.result.replication_transition_counts), 32)

    def test_training_and_evaluation_provenance_is_complete(self) -> None:
        for branch in (self.result.reference, self.result.alternate):
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
                all(
                    0 < len(trace) <= count
                    for trace, count in zip(traces, counts)
                )
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
            "P8 local exact first-pass symmetric conflict-projected one-step update diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "original negative-dot pair only",
            "one fixed formula, one average and one update at rate 0.32 only",
            "no alternative projection order, coefficient, epsilon or threshold",
            "retained regardless of sign and no selection",
            "no second update, third protocol, seed search",
            "no scale, rate, optimizer, entropy, temperature or exploration search",
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
                MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError,
                "pinned symmetric conflict-projected runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke()

    def test_source_forbids_projection_search_and_open_ended_work(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertEqual(source.count("_summarize_protocol("), 2)
        self.assertEqual(source.count("_evaluate("), 2)
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
