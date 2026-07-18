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

import mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke as smoke_module  # noqa: E402
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
    MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS,
    MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS,
    MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS,
    MahJaxCategoricalMlpImitationResult,
    MahJaxCategoricalMlpImitationSmokeError,
    encode_mahjax_categorical_observation,
    run_mahjax_categorical_mlp_imitation_training_smoke,
)


class MahJaxCategoricalMlpImitationTrainingSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_imitation_training_smoke()

    def test_exact_public_surface_constants_and_frozen_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT",
                "MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS",
                "MahJaxCategoricalMlpImitationSmokeError",
                "MahJaxCategoricalMlpImitationResult",
                "encode_mahjax_categorical_observation",
                "run_mahjax_categorical_mlp_imitation_training_smoke",
            },
        )
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT, 882)
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS, tuple(range(8)))
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS, tuple(range(8, 12)))
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS, tuple(range(16)))
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS, 48)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxCategoricalMlpImitationResult)
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.epoch_count = 49  # type: ignore[misc]

    def test_categorical_encoder_exact_layout_on_pinned_initial_observation(self) -> None:
        import jax
        import mahjax

        environment = mahjax.make(
            "red_mahjong",
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        observation = environment.observe(environment.init(jax.random.PRNGKey(0)))
        features = encode_mahjax_categorical_observation(observation)
        self.assertEqual(len(features), 882)
        self.assertTrue(all(math.isfinite(value) for value in features))
        self.assertAlmostEqual(sum(features[:37]), 3.5)
        self.assertAlmostEqual(features[1], 0.25)
        self.assertAlmostEqual(features[8], 0.5)
        self.assertEqual(sum(features[37:75]), 1.0)
        self.assertEqual(features[38], 1.0)
        self.assertEqual(sum(features[75:811]), 0.0)
        self.assertEqual(features[815], 1.0)
        self.assertEqual(features[818], 0.0)
        self.assertEqual(features[819:823], (0.25, 0.25, 0.25, 0.25))
        self.assertEqual(features[823], 1.0)
        self.assertEqual(features[848], 0.25)

    def test_exact_runtime_model_optimizer_and_source_counts(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.recent_action_count, 8)
        self.assertEqual(self.result.feature_count, 882)
        self.assertEqual(self.result.hidden_unit_count, 64)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 62_167)
        self.assertEqual(self.result.model_seed, 123)
        self.assertEqual(self.result.epoch_count, 48)
        self.assertEqual(self.result.learning_rate, 0.003)
        self.assertEqual(self.result.adam_beta1, 0.9)
        self.assertEqual(self.result.adam_beta2, 0.999)
        self.assertEqual(self.result.adam_epsilon, 1e-8)
        self.assertEqual(self.result.train_example_count, 482)
        self.assertEqual(self.result.eval_example_count, 221)
        self.assertTrue(self.result.train_eval_sources_separate)

    def test_exact_training_metrics_and_loss_history(self) -> None:
        self.assertEqual(len(self.result.pre_update_loss_history), 48)
        self.assertAlmostEqual(self.result.final_train_loss, 0.36734492, places=5)
        self.assertAlmostEqual(self.result.final_eval_loss, 1.77358353, places=5)
        self.assertAlmostEqual(self.result.final_train_accuracy, 0.93153530, places=5)
        self.assertAlmostEqual(self.result.final_eval_accuracy, 0.58371043, places=5)
        self.assertLess(self.result.final_train_loss, self.result.initial_train_loss)
        self.assertLess(self.result.final_eval_loss, self.result.initial_eval_loss)
        self.assertGreater(
            self.result.final_train_accuracy,
            self.result.initial_train_accuracy,
        )
        self.assertGreater(
            self.result.final_eval_accuracy,
            self.result.initial_eval_accuracy,
        )
        self.assertGreater(self.result.parameter_delta_l2, 0.0)
        self.assertTrue(math.isfinite(self.result.parameter_delta_l2))
        self.assertTrue(self.result.training_applied)

    def test_all_project_rounds_are_legal_terminal_and_nonzero_on_exact_seeds(self) -> None:
        self.assertEqual(self.result.selfplay_round_count, 16)
        self.assertEqual(len(self.result.selfplay_transition_counts), 16)
        self.assertEqual(len(self.result.selfplay_cumulative_raw_rewards), 16)
        self.assertEqual(len(self.result.selfplay_final_raw_rewards), 16)
        self.assertEqual(len(self.result.selfplay_final_scores), 16)
        self.assertTrue(self.result.selfplay_all_actions_legal)
        self.assertTrue(self.result.selfplay_all_rounds_terminated)
        self.assertTrue(all(0 < count <= 256 for count in self.result.selfplay_transition_counts))
        self.assertEqual(
            self.result.selfplay_nonzero_outcome_seeds,
            (0, 1, 3, 5, 6, 7, 10),
        )
        expected = {
            0: (-10.0, -10.0, -10.0, 20.0),
            1: (-10.0, -10.0, 20.0, -10.0),
            3: (-10.0, -10.0, -10.0, 20.0),
            5: (32.0, -32.0, 0.0, 0.0),
            6: (-23.0, 37.0, -7.0, -7.0),
            7: (-10.0, -10.0, -10.0, 20.0),
            10: (0.0, 180.0, 0.0, -180.0),
        }
        for seed, rewards in expected.items():
            self.assertEqual(self.result.selfplay_cumulative_raw_rewards[seed], rewards)

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_categorical_mlp_imitation_training_smoke(),
        )

    def test_wraps_runtime_loading_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_load_pinned_runtime",
            side_effect=RuntimeError("runtime unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpImitationSmokeError,
                "runtime unavailable",
            ):
                run_mahjax_categorical_mlp_imitation_training_smoke()

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P7/P8 local categorical-MLP imitation and all-project outcome smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "local categorical-feature mlp imitation training smoke only",
            "train seeds 0 through 7 and evaluation seeds 8 through 11 are disjoint",
            "exact 882 current-player observation features",
            "exact 64-hidden relu mlp and 48 full-batch adam epochs",
            "all-project rounds are outcome-signal diagnostics with no rl update",
            "no saved dataset, parameters, model weights, checkpoint or artifact",
            "not production self-play, evaluation, league or candidate promotion",
            "not improvement, policy-quality, model-strength, stable-dan or luckyj",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_exact_training_and_no_io_or_rl_update(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("range(MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS)", source)
        self.assertIn("jax.value_and_grad", source)
        self.assertIn("MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS", source)
        self.assertIn("MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS", source)
        self.assertIn("MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS", source)
        self.assertNotIn("state.players.hand", source)
        self.assertNotIn("raw-outcome update", source.lower())
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
