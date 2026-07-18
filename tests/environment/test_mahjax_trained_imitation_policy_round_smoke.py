from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.environment.mahjax_trained_imitation_policy_round_smoke as smoke_module  # noqa: E402
import mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke as training_module  # noqa: E402
from mjlabai.environment.mahjax_trained_imitation_policy_round_smoke import (  # noqa: E402
    MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED,
    MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION,
    MahJaxTrainedImitationPolicyRoundResult,
    run_mahjax_trained_imitation_policy_round_smoke,
)


class MahJaxTrainedImitationPolicyRoundSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_trained_imitation_policy_round_smoke()

    def test_exact_public_surface_and_frozen_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION",
                "MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED",
                "MahJaxTrainedImitationPolicyRoundSmokeError",
                "MahJaxTrainedImitationPolicyRoundResult",
                "run_mahjax_trained_imitation_policy_round_smoke",
            },
        )
        self.assertEqual(MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED, 2)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxTrainedImitationPolicyRoundResult,
        )
        self.assertIn("trajectory_changed", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.rollout_seed = 3  # type: ignore[misc]

    def test_pins_runtime_models_and_seed_separation(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.rollout_seed, 2)
        self.assertEqual(self.result.training_result.train_seed, 0)
        self.assertEqual(self.result.training_result.eval_seed, 1)
        self.assertEqual({0, 1, 2}, {self.result.training_result.train_seed, self.result.training_result.eval_seed, self.result.rollout_seed})
        self.assertEqual(
            self.result.initial_model_id,
            "project_linear_630x87_initial_seed_123",
        )
        self.assertEqual(
            self.result.trained_model_id,
            "project_linear_630x87_imitation_seed_123_epoch_16",
        )

    def test_preserves_reviewed_training_summary_and_private_handoff(self) -> None:
        training = self.result.training_result
        self.assertEqual(training.train_example_count, 54)
        self.assertEqual(training.eval_example_count, 64)
        self.assertEqual(training.epoch_count, 16)
        self.assertAlmostEqual(training.initial_train_loss, 1.70919883, places=5)
        self.assertAlmostEqual(training.final_train_loss, 1.38197553, places=5)
        self.assertAlmostEqual(training.initial_eval_loss, 1.76650584, places=5)
        self.assertAlmostEqual(training.final_eval_loss, 1.54172158, places=5)
        self.assertNotIn(
            "_train_mahjax_rule_policy_imitation_parameters",
            training_module.__all__,
        )

    def test_exact_model_shape_and_seed_two_outcomes(self) -> None:
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)
        self.assertEqual(self.result.transition_cap, 256)
        self.assertEqual(self.result.initial_transition_count, 88)
        self.assertEqual(self.result.trained_transition_count, 94)
        self.assertTrue(self.result.initial_terminated)
        self.assertTrue(self.result.trained_terminated)
        self.assertFalse(self.result.initial_truncated)
        self.assertFalse(self.result.trained_truncated)
        self.assertEqual(self.result.initial_final_scores, (250, 250, 250, 250))
        self.assertEqual(self.result.trained_final_scores, (250, 250, 250, 250))
        self.assertEqual(self.result.initial_final_rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(self.result.trained_final_rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(
            self.result.initial_cumulative_rewards,
            (0.0, 0.0, 0.0, 0.0),
        )
        self.assertEqual(
            self.result.trained_cumulative_rewards,
            (0.0, 0.0, 0.0, 0.0),
        )

    def test_complete_traces_are_legal_and_immutable(self) -> None:
        self.assertIs(type(self.result.initial_actions), tuple)
        self.assertIs(type(self.result.trained_actions), tuple)
        self.assertEqual(
            len(self.result.initial_actions),
            len(self.result.initial_legal_actions),
        )
        self.assertEqual(
            len(self.result.trained_actions),
            len(self.result.trained_legal_actions),
        )
        for actions, legal_history in (
            (self.result.initial_actions, self.result.initial_legal_actions),
            (self.result.trained_actions, self.result.trained_legal_actions),
        ):
            for action, legal_actions in zip(actions, legal_history):
                self.assertTrue(legal_actions)
                self.assertEqual(legal_actions, tuple(sorted(legal_actions)))
                self.assertIn(action, legal_actions)

    def test_training_changes_held_out_action_trajectory(self) -> None:
        self.assertEqual(self.result.initial_actions[0], 12)
        self.assertEqual(self.result.trained_actions[0], 71)
        self.assertNotEqual(self.result.initial_actions, self.result.trained_actions)
        self.assertTrue(self.result.trajectory_changed)

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_trained_imitation_policy_round_smoke(),
        )

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P7/P8 local trained-imitation-policy held-out environment smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one held-out mahjax seed only",
            "seed 2 is distinct from seed 0 training and seed 1 label evaluation",
            "environment legal mask remains authoritative",
            "changed action trajectory is behavior smoke only",
            "no persisted data, parameters, model weights, checkpoint or artifact",
            "no hidden opponent hand or private environment-state feature",
            "no reward objective, reinforcement-learning update or self-play learning",
            "no real tenhou, real haifu, external log or platform data",
            "not production training, evaluation, league or candidate promotion",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_is_private_in_memory_legal_masked_round_only(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertIn("_train_mahjax_rule_policy_imitation_parameters", source)
        self.assertIn("encode_mahjax_public_observation", source)
        self.assertIn("state.legal_action_mask", source)
        self.assertIn("state.round_state.score", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            ".load(",
            "pickle",
            "requests",
            "subprocess",
            "platform_data",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
