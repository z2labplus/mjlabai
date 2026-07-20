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

import mjlabai.rl.mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke as smoke_module  # noqa: E402
import mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke as batch_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_TRAINING_PROTOCOL_GRADIENT_ALIGNMENT_SMOKE_VERSION,
    MahJaxCategoricalMlpFirstPassProtocolGradientResult,
    MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult,
    MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError,
    run_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke,
)


class MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_TRAINING_PROTOCOL_GRADIENT_ALIGNMENT_SMOKE_VERSION",
                "MahJaxCategoricalMlpFirstPassProtocolGradientResult",
                "MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError",
                "MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult",
                "run_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult,
        )
        self.assertIsInstance(
            self.result.reference,
            MahJaxCategoricalMlpFirstPassProtocolGradientResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_TRAINING_PROTOCOL_GRADIENT_ALIGNMENT_SMOKE_VERSION,
        )
        for value in (self.result, self.result.reference, self.result.alternate):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("gradients", names)
            self.assertNotIn("mean_gradients", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.global_gradient_cosine_similarity = 1.0  # type: ignore[misc]

    def test_exact_two_protocol_first_pass_contract_has_no_update_or_evaluation(
        self,
    ) -> None:
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
        self.assertTrue(
            set(self.result.reference.training_seeds).isdisjoint(
                self.result.alternate.training_seeds
            )
        )

    def test_exact_gradient_geometry_is_finite_nonzero_and_conflicting(self) -> None:
        expected_reference = (
            0.010686613619327545,
            0.001964464085176587,
            0.026142027229070663,
            0.0029551691841334105,
        )
        expected_alternate = (
            0.009576422162353992,
            0.002076641656458378,
            0.024850960820913315,
            0.002903012791648507,
        )
        for actual, expected in zip(
            self.result.reference.parameter_group_gradient_l2,
            expected_reference,
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            self.result.alternate.parameter_group_gradient_l2,
            expected_alternate,
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertAlmostEqual(
            self.result.reference.global_gradient_l2,
            0.028464037702741144,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.alternate.global_gradient_l2,
            0.026870393353875678,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.global_gradient_dot_product,
            -0.0001429308561853304,
            places=9,
        )
        self.assertAlmostEqual(
            self.result.global_gradient_cosine_similarity,
            -0.18687683284469966,
            places=6,
        )
        self.assertLess(self.result.global_gradient_dot_product, 0.0)
        self.assertLess(self.result.global_gradient_cosine_similarity, 0.0)
        self.assertTrue(self.result.all_gradient_values_finite)
        self.assertTrue(self.result.both_global_gradients_nonzero)

    def test_exact_objectives_rewards_and_transition_provenance(self) -> None:
        self.assertAlmostEqual(
            self.result.reference.batch_initial_objective,
            -0.008504558742060908,
            places=9,
        )
        self.assertAlmostEqual(
            self.result.alternate.batch_initial_objective,
            -0.010526151631779612,
            places=9,
        )
        self.assertEqual(
            tuple(
                sum(row[seat] for row in self.result.reference.cumulative_raw_rewards)
                for seat in range(4)
            ),
            (-55.0, -34.0, -150.0, 179.0),
        )
        self.assertEqual(
            tuple(
                sum(row[seat] for row in self.result.alternate.cumulative_raw_rewards)
                for seat in range(4)
            ),
            (130.0, 90.0, 6.0, -286.0),
        )
        for branch in (self.result.reference, self.result.alternate):
            self.assertEqual(len(branch.transition_counts), 32)
            self.assertEqual(
                tuple(map(len, branch.action_traces)),
                branch.transition_counts,
            )
            self.assertEqual(len(branch.action_trace_sha256), 32)
            self.assertTrue(
                all(
                    len(digest) == 64
                    and all(character in "0123456789abcdef" for character in digest)
                    for digest in branch.action_trace_sha256
                )
            )

    def test_leave_one_out_baselines_are_exact_and_centered(self) -> None:
        for branch in (self.result.reference, self.result.alternate):
            normalized = tuple(
                tuple(value / 100.0 for value in row)
                for row in branch.cumulative_raw_rewards
            )
            for row_index, (row, baseline, advantage) in enumerate(
                zip(
                    normalized,
                    branch.leave_one_out_seat_baselines,
                    branch.advantage_seat_returns,
                )
            ):
                for seat in range(4):
                    expected = sum(
                        other[seat]
                        for other_index, other in enumerate(normalized)
                        if other_index != row_index
                    ) / 31
                    self.assertAlmostEqual(baseline[seat], expected, places=12)
                    self.assertAlmostEqual(
                        advantage[seat],
                        row[seat] - expected,
                        places=12,
                    )
            self.assertTrue(branch.all_advantage_sums_centered)
            for seat in range(4):
                self.assertAlmostEqual(
                    sum(row[seat] for row in branch.advantage_seat_returns),
                    0.0,
                    places=12,
                )

    def test_complete_training_actions_are_legal_and_rounds_terminate(self) -> None:
        for branch in (self.result.reference, self.result.alternate):
            self.assertTrue(branch.all_training_actions_legal)
            self.assertTrue(branch.all_rounds_terminated)
            self.assertEqual(len(branch.final_scores), 32)
            self.assertEqual(
                branch.parameter_group_shapes,
                self.result.reference.parameter_group_shapes,
            )
            for actions, legal_rows in zip(
                branch.action_traces,
                branch.legal_action_traces,
            ):
                self.assertTrue(
                    all(
                        action in legal
                        for action, legal in zip(actions, legal_rows)
                    )
                )

    def test_no_selection_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertIsNone(self.result.selected_training_protocol_id)
        self.assertIsNone(self.result.selected_model_id)
        self.assertIsNone(self.result.selected_multiplier)
        self.assertIsNone(self.result.selected_pass_index)
        self.assertIsNone(self.result.selected_checkpoint_id)
        self.assertIsNone(self.result.selected_gradient_direction)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local exact first-pass two-protocol aggregate-gradient alignment diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "identical initial parameters",
            "without applying an update",
            "no primary, replication or other policy evaluation",
            "retained regardless of cosine sign or magnitude",
            "no protocol, model, multiplier, pass, checkpoint or direction",
            "no scale, rate, optimizer, exploration, seed or protocol search",
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
                MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError,
                "pinned first-pass gradient-alignment runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke()

    def test_source_preserves_reviewed_update_paths_and_forbids_search(self) -> None:
        source = inspect.getsource(smoke_module)
        batch_source = inspect.getsource(batch_module)
        self.assertEqual(source.count("_summarize_protocol("), 3)
        self.assertNotIn("_apply_leave_one_out_batch_update", source)
        self.assertNotIn("_evaluate(", source)
        self.assertNotIn("while ", source)
        self.assertIn("gradient_multiplier * gradient", batch_source)
        self.assertGreaterEqual(batch_source.count("        1.0,"), 2)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "best_checkpoint",
            "multiplier_candidates",
            "learning_rate_candidates",
            "temperature_candidates",
            "entropy_candidates",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
