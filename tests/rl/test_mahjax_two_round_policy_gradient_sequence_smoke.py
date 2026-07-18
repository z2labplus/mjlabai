from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
import math
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_two_round_policy_gradient_sequence_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_two_round_policy_gradient_sequence_smoke import (  # noqa: E402
    MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE,
    MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS,
    MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION,
    MahJaxTwoRoundPolicyGradientSequenceResult,
    run_mahjax_two_round_policy_gradient_sequence_smoke,
)


class MahJaxTwoRoundPolicyGradientSequenceSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_two_round_policy_gradient_sequence_smoke()

    def test_exact_public_surface_constants_and_frozen_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION",
                "MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS",
                "MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE",
                "MahJaxTwoRoundPolicyGradientSequenceSmokeError",
                "MahJaxTwoRoundPolicyGradientSequenceResult",
                "run_mahjax_two_round_policy_gradient_sequence_smoke",
            },
        )
        self.assertEqual(MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS, (1, 5))
        self.assertEqual(MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE, 0.1)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxTwoRoundPolicyGradientSequenceResult,
        )
        self.assertIn("parameter_continuity_verified", {f.name for f in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 3  # type: ignore[misc]

    def test_pins_runtime_model_and_exact_two_step_boundary(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.seeds, (1, 5))
        self.assertEqual(self.result.round_count, 2)
        self.assertEqual(self.result.update_count, 2)
        self.assertEqual(self.result.learning_rate, 0.1)
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)
        self.assertTrue(self.result.parameter_continuity_verified)

    def test_preserves_reviewed_imitation_training_summary(self) -> None:
        self.assertEqual(self.result.training_result.train_example_count, 54)
        self.assertEqual(self.result.training_result.eval_example_count, 64)
        self.assertEqual(self.result.training_result.epoch_count, 16)
        self.assertEqual(self.result.training_result.final_eval_accuracy, 0.5)

    def test_exact_round_shapes_actions_and_all_actions_legal(self) -> None:
        self.assertEqual(self.result.transition_counts, (37, 32))
        self.assertEqual(self.result.project_decision_counts, (8, 7))
        self.assertEqual(
            self.result.project_actions_by_round,
            (
                (20, 84, 16, 30, 27, 26, 3, 13),
                (12, 6, 31, 84, 13, 32, 33),
            ),
        )
        for actions, legal_history in zip(
            self.result.action_traces,
            self.result.legal_action_traces,
        ):
            self.assertEqual(len(actions), len(legal_history))
            self.assertTrue(
                all(action in legal for action, legal in zip(actions, legal_history))
            )

    def test_exact_raw_outcomes_and_scores(self) -> None:
        self.assertEqual(
            self.result.cumulative_rewards_by_round,
            ((-39.0, 39.0, 0.0, 0.0), (-40.0, -40.0, -40.0, 120.0)),
        )
        self.assertEqual(
            self.result.final_rewards_by_round,
            ((-39.0, 39.0, 0.0, 0.0), (-40.0, -40.0, -40.0, 130.0)),
        )
        self.assertEqual(
            self.result.final_scores_by_round,
            ((211, 289, 250, 250), (210, 210, 210, 370)),
        )

    def test_exact_objectives_and_step_parameter_deltas(self) -> None:
        expected_pairs = (
            (self.result.return_scales, (-0.39, -0.4)),
            (self.result.initial_objectives, (-0.86367577, -0.85308564)),
            (self.result.post_update_objectives, (-0.88331068, -0.87257367)),
            (self.result.step_weight_delta_l2, (0.04220101, 0.04183802)),
            (self.result.step_bias_delta_l2, (0.01279154, 0.01353321)),
        )
        for actual_values, expected_values in expected_pairs:
            for actual, expected in zip(actual_values, expected_values):
                self.assertAlmostEqual(actual, expected, places=5)
                self.assertTrue(math.isfinite(actual))
        self.assertGreater(self.result.final_weight_delta_l2, 0.0)
        self.assertGreater(self.result.final_bias_delta_l2, 0.0)
        self.assertTrue(math.isfinite(self.result.final_weight_delta_l2))
        self.assertTrue(math.isfinite(self.result.final_bias_delta_l2))

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_two_round_policy_gradient_sequence_smoke(),
        )

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local two-round sequential raw-outcome training smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "exact two-round sequential on-policy raw-outcome training smoke only",
            "round seeds are fixed in order as 1 then 5",
            "updated parameters carry directly from round 1 into round 5",
            "exactly two rounds and exactly two gradient updates",
            "returns are only cumulative raw seat-0 rewards divided by 100",
            "no replay, baseline, critic, discount, bootstrapping or reward shaping",
            "fixed bundled rule opponents do not learn",
            "no persisted data, parameters, model weights, checkpoint or artifact",
            "no self-play learning, evaluation, league or candidate promotion",
            "not improvement, policy-quality, model-strength, stable-dan or luckyj",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_one_exact_two_item_loop_helper_reuse_and_no_io(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertIn("MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS = (1, 5)", source)
        self.assertIn("_collect_on_policy_round", source)
        self.assertIn("_apply_one_raw_outcome_update", source)
        self.assertIn("weights, biases = update.weights, update.biases", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            ".load(",
            "pickle",
            "requests",
            "subprocess",
            "replay_buffer",
            "platform_data",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
