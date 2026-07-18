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

import mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke as training_module  # noqa: E402
from mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke import (  # noqa: E402
    MAHJAX_IMITATION_EVAL_SEED,
    MAHJAX_IMITATION_LEARNING_RATE,
    MAHJAX_IMITATION_MODEL_SEED,
    MAHJAX_IMITATION_TRAIN_SEED,
    MAHJAX_IMITATION_TRAINING_EPOCHS,
    MAHJAX_IMITATION_TRAINING_SMOKE_VERSION,
    MahJaxImitationTrainingResult,
    MahJaxImitationTrainingSmokeError,
    run_mahjax_rule_policy_imitation_training_smoke,
)


class MahJaxRulePolicyImitationTrainingSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_rule_policy_imitation_training_smoke()

    def test_exact_public_surface_constants_and_frozen_result(self) -> None:
        self.assertEqual(
            set(training_module.__all__),
            {
                "MAHJAX_IMITATION_TRAINING_SMOKE_VERSION",
                "MAHJAX_IMITATION_TRAIN_SEED",
                "MAHJAX_IMITATION_EVAL_SEED",
                "MAHJAX_IMITATION_MODEL_SEED",
                "MAHJAX_IMITATION_TRAINING_EPOCHS",
                "MAHJAX_IMITATION_LEARNING_RATE",
                "MahJaxImitationTrainingSmokeError",
                "MahJaxImitationTrainingResult",
                "run_mahjax_rule_policy_imitation_training_smoke",
            },
        )
        self.assertEqual(MAHJAX_IMITATION_TRAIN_SEED, 0)
        self.assertEqual(MAHJAX_IMITATION_EVAL_SEED, 1)
        self.assertEqual(MAHJAX_IMITATION_MODEL_SEED, 123)
        self.assertEqual(MAHJAX_IMITATION_TRAINING_EPOCHS, 16)
        self.assertEqual(MAHJAX_IMITATION_LEARNING_RATE, 0.1)
        self.assertIsInstance(self.result, MahJaxImitationTrainingResult)
        self.assertEqual(
            self.result.training_version,
            MAHJAX_IMITATION_TRAINING_SMOKE_VERSION,
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.epoch_count = 1  # type: ignore[misc]
        self.assertIn("final_eval_accuracy", {field.name for field in fields(self.result)})

    def test_pins_runtime_teacher_model_and_separate_sample_sources(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(
            self.result.teacher_policy_id,
            "mahjax.red_mahjong.players.rule_based_player@0.1.2",
        )
        self.assertEqual(self.result.model_id, "project_linear_630x87_imitation_seed_123")
        self.assertEqual(self.result.train_seed, 0)
        self.assertEqual(self.result.eval_seed, 1)
        self.assertNotEqual(self.result.train_seed, self.result.eval_seed)
        self.assertTrue(self.result.train_eval_sources_separate)
        self.assertEqual(self.result.train_example_count, 54)
        self.assertEqual(self.result.eval_example_count, 64)

    def test_exact_model_and_training_shape(self) -> None:
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)
        self.assertEqual(self.result.epoch_count, 16)
        self.assertEqual(self.result.learning_rate, 0.1)
        self.assertTrue(self.result.training_applied)

    def test_losses_match_probe_and_improve(self) -> None:
        self.assertAlmostEqual(self.result.initial_train_loss, 1.70919883, places=5)
        self.assertAlmostEqual(self.result.final_train_loss, 1.38197553, places=5)
        self.assertAlmostEqual(self.result.initial_eval_loss, 1.76650584, places=5)
        self.assertAlmostEqual(self.result.final_eval_loss, 1.54172158, places=5)
        self.assertLess(self.result.final_train_loss, self.result.initial_train_loss)
        self.assertLess(self.result.final_eval_loss, self.result.initial_eval_loss)

    def test_accuracy_matches_probe_and_is_nondecreasing(self) -> None:
        self.assertAlmostEqual(self.result.initial_train_accuracy, 0.29629630, places=5)
        self.assertAlmostEqual(self.result.final_train_accuracy, 0.51851851, places=5)
        self.assertEqual(self.result.initial_eval_accuracy, 0.234375)
        self.assertEqual(self.result.final_eval_accuracy, 0.5)
        self.assertGreaterEqual(
            self.result.final_train_accuracy,
            self.result.initial_train_accuracy,
        )
        self.assertGreaterEqual(
            self.result.final_eval_accuracy,
            self.result.initial_eval_accuracy,
        )

    def test_loss_history_is_finite_strictly_decreasing_and_exact_length(self) -> None:
        history = self.result.pre_update_loss_history
        self.assertEqual(len(history), 16)
        self.assertTrue(all(math.isfinite(value) for value in history))
        self.assertTrue(
            all(history[index + 1] < history[index] for index in range(15))
        )
        self.assertAlmostEqual(history[0], self.result.initial_train_loss, places=6)
        self.assertGreater(history[-1], self.result.final_train_loss)

    def test_gradient_updates_change_weights_and_biases(self) -> None:
        self.assertAlmostEqual(self.result.weight_delta_l2, 0.67900646, places=5)
        self.assertAlmostEqual(self.result.bias_delta_l2, 0.23012902, places=5)
        self.assertGreater(self.result.weight_delta_l2, 0.0)
        self.assertGreater(self.result.bias_delta_l2, 0.0)

    def test_training_summary_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_rule_policy_imitation_training_smoke(),
        )

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P7/P8 local synthetic rule-policy imitation training smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "first environment-backed project parameter training smoke only",
            "seed 0 train and seed 1 evaluation decisions remain separate",
            "630 public features, 87 legal-masked actions and 54,897 parameters",
            "sixteen deterministic full-batch gradient updates only",
            "no persisted dataset, model weights, checkpoint or artifact",
            "no hidden opponent hand or private environment-state feature",
            "no reward objective, reinforcement-learning update or self-play learning",
            "no real tenhou, real haifu, external log or platform data",
            "not production training, evaluation, league or candidate promotion",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_is_bounded_in_memory_gradient_training_only(self) -> None:
        source = inspect.getsource(training_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 2)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertIn("encode_mahjax_public_observation", source)
        self.assertIn("jax.value_and_grad", source)
        self.assertIn("@jax.jit", source)
        self.assertIn("jnp.where(batch_masks, logits, -1e9)", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "platform_data",
            "reward_objective",
        ):
            self.assertNotIn(forbidden, source.lower())


if __name__ == "__main__":
    unittest.main()
