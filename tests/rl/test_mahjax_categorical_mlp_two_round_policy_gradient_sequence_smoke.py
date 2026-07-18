from __future__ import annotations

from dataclasses import FrozenInstanceError, fields
import inspect
import math
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS,
    MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION,
    MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult,
    MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError,
    run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke,
)
class MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke()

    def test_exact_public_surface_constants_and_frozen_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE",
                "MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError",
                "MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult",
                "run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke",
            },
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 3  # type: ignore[misc]

    def test_exact_order_count_learning_rate_and_training_identity(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS,
            (1, 3),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE,
            0.01,
        )
        self.assertEqual(self.result.seeds, (1, 3))
        self.assertEqual(self.result.round_count, 2)
        self.assertEqual(self.result.update_count, 2)
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.training_result.epoch_count, 48)
        self.assertEqual(self.result.training_result.train_example_count, 482)
        self.assertEqual(self.result.training_result.eval_example_count, 221)

    def test_first_round_preserves_reviewed_public_seed1_behavior(self) -> None:
        self.assertEqual(self.result.transition_counts[0], 77)
        self.assertEqual(self.result.seat_decision_counts[0], (21, 22, 17, 17))
        self.assertEqual(
            self.result.cumulative_raw_rewards[0],
            (-20.0, 70.0, -20.0, -30.0),
        )
        self.assertAlmostEqual(
            self.result.initial_objectives[0],
            0.0936663598,
            places=6,
        )

    def test_exact_two_round_trajectories_are_legal_terminal_and_nonzero(self) -> None:
        self.assertEqual(self.result.transition_counts, (77, 84))
        self.assertEqual(
            self.result.seat_decision_counts,
            ((21, 22, 17, 17), (23, 22, 19, 20)),
        )
        self.assertEqual(
            tuple(trace[:12] for trace in self.result.action_traces),
            (
                (28, 27, 28, 28, 29, 33, 27, 31, 27, 0, 31, 32),
                (29, 28, 29, 27, 71, 84, 27, 31, 8, 71, 30, 33),
            ),
        )
        self.assertEqual(
            self.result.cumulative_raw_rewards,
            ((-20.0, 70.0, -20.0, -30.0), (-10.0, -10.0, 20.0, -10.0)),
        )
        self.assertEqual(
            self.result.final_raw_rewards,
            ((-20.0, 80.0, -20.0, -20.0), (-10.0, -10.0, 30.0, -10.0)),
        )
        self.assertEqual(
            self.result.final_scores,
            ((230, 320, 230, 220), (240, 240, 270, 240)),
        )
        for actors, actions, legal_trace in zip(
            self.result.actor_traces,
            self.result.action_traces,
            self.result.legal_action_traces,
        ):
            self.assertEqual(len(actors), len(actions))
            self.assertEqual(len(actions), len(legal_trace))
            for actor, action, legal_actions in zip(actors, actions, legal_trace):
                self.assertIn(actor, (0, 1, 2, 3))
                self.assertIn(action, legal_actions)
        self.assertTrue(self.result.all_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)

    def test_two_objectives_step_deltas_and_final_deltas_are_exact(self) -> None:
        expected_initial = (0.0936663598, -0.0553588867)
        expected_post = (0.0930117071, -0.0554395691)
        expected_steps = (
            (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356),
            (0.0002636357, 0.0000601950, 0.0008506179, 0.0000944084),
        )
        expected_final = (
            0.0010158311,
            0.0001864599,
            0.0025688238,
            0.0002769242,
        )
        for actual, expected in zip(self.result.initial_objectives, expected_initial):
            self.assertAlmostEqual(actual, expected, places=5)
        for actual, expected in zip(self.result.post_update_objectives, expected_post):
            self.assertAlmostEqual(actual, expected, places=5)
        for before, after in zip(
            self.result.initial_objectives,
            self.result.post_update_objectives,
        ):
            self.assertLess(after, before)
        for actual_row, expected_row in zip(
            self.result.per_update_parameter_delta_l2,
            expected_steps,
        ):
            for actual, expected in zip(actual_row, expected_row):
                self.assertTrue(math.isfinite(actual))
                self.assertGreater(actual, 0.0)
                self.assertAlmostEqual(actual, expected, places=5)
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            expected_final,
        ):
            self.assertTrue(math.isfinite(actual))
            self.assertGreater(actual, 0.0)
            self.assertAlmostEqual(actual, expected, places=5)

    def test_round2_direct_parameter_continuity_and_post_replay(self) -> None:
        self.assertTrue(self.result.parameter_continuity_proven)
        self.assertAlmostEqual(
            self.result.fresh_seed3_initial_objective,
            -0.0553399548,
            places=6,
        )
        self.assertAlmostEqual(
            self.result.carried_seed3_initial_objective,
            -0.0553588867,
            places=6,
        )
        self.assertNotAlmostEqual(
            self.result.fresh_seed3_initial_objective,
            self.result.carried_seed3_initial_objective,
            places=6,
        )
        self.assertTrue(self.result.post_round2_replay_identical)
        self.assertEqual(self.result.post_round2_transition_count, 84)
        self.assertEqual(self.result.post_round2_actor_trace, self.result.actor_traces[1])
        self.assertEqual(self.result.post_round2_action_trace, self.result.action_traces[1])
        self.assertEqual(
            self.result.post_round2_legal_action_trace,
            self.result.legal_action_traces[1],
        )
        self.assertEqual(
            self.result.post_round2_cumulative_raw_rewards,
            self.result.cumulative_raw_rewards[1],
        )

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke(),
        )

    def test_wraps_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke()

    def test_evidence_warnings_and_source_prevent_scope_drift(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local two-round sequential shared all-project-seat raw-outcome training smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "two-round sequential shared all-project-seat training smoke only",
            "exact ordered seeds 1 then 3 and exactly two 0.01 updates",
            "round-1 updated arrays feed round 2 directly without reinitialization",
            "no baseline, critic, discount, bootstrapping, entropy, replay or shaping",
            "no third round, production self-play, evaluation, league or promotion",
            "not improvement, policy-quality or model-strength evidence",
        ):
            self.assertIn(phrase, warning_text)
        source = inspect.getsource(smoke_module)
        self.assertIn(
            "for seed in MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS",
            source,
        )
        self.assertIn("parameters = update.parameters", source)
        self.assertIn("_collect_all_project_round(", source)
        self.assertIn("_apply_actor_indexed_raw_outcome_update(", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            ".load(",
            "pickle",
            "requests",
            "subprocess",
            "rule_based_player",
            "platform_data",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
