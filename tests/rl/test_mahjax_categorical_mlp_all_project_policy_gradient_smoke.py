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

import mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED,
    MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION,
    MahJaxCategoricalMlpAllProjectPolicyGradientResult,
    MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError,
    run_mahjax_categorical_mlp_all_project_policy_gradient_smoke,
)


class MahJaxCategoricalMlpAllProjectPolicyGradientSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_all_project_policy_gradient_smoke()

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED",
                "MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE",
                "MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError",
                "MahJaxCategoricalMlpAllProjectPolicyGradientResult",
                "run_mahjax_categorical_mlp_all_project_policy_gradient_smoke",
            },
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpAllProjectPolicyGradientResult,
        )
        field_names = {field.name for field in fields(self.result)}
        self.assertNotIn("parameters", field_names)
        self.assertNotIn("features", field_names)
        self.assertNotIn("legal_masks", field_names)
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 2  # type: ignore[misc]

    def test_exact_runtime_model_seed_and_one_update_contract(self) -> None:
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED, 1)
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE,
            0.01,
        )
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.seed, 1)
        self.assertEqual(self.result.project_policy_seats, (0, 1, 2, 3))
        self.assertIn("categorical_mlp_882x64x87", self.result.project_policy_id)
        self.assertEqual(self.result.feature_count, 882)
        self.assertEqual(self.result.hidden_unit_count, 64)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 62_167)
        self.assertEqual(self.result.transition_cap, 256)
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.update_count, 1)
        self.assertEqual(self.result.training_result.epoch_count, 48)
        self.assertEqual(self.result.training_result.train_example_count, 482)
        self.assertEqual(self.result.training_result.eval_example_count, 221)

    def test_pre_round_is_exact_legal_terminal_all_project_trajectory(self) -> None:
        self.assertEqual(self.result.pre_transition_count, 77)
        self.assertEqual(self.result.pre_seat_decision_counts, (21, 22, 17, 17))
        self.assertEqual(len(self.result.pre_actor_trace), 77)
        self.assertEqual(len(self.result.pre_action_trace), 77)
        self.assertEqual(len(self.result.pre_legal_action_trace), 77)
        self.assertEqual(
            self.result.pre_action_trace[:12],
            (28, 27, 28, 28, 29, 33, 27, 31, 27, 0, 31, 32),
        )
        for actor, action, legal_actions in zip(
            self.result.pre_actor_trace,
            self.result.pre_action_trace,
            self.result.pre_legal_action_trace,
        ):
            self.assertIn(actor, (0, 1, 2, 3))
            self.assertIn(action, legal_actions)
            self.assertTrue(legal_actions)
        self.assertEqual(
            self.result.pre_cumulative_raw_rewards,
            (-20.0, 70.0, -20.0, -30.0),
        )
        self.assertEqual(
            self.result.pre_final_raw_rewards,
            (-20.0, 80.0, -20.0, -20.0),
        )
        self.assertEqual(self.result.pre_final_scores, (230, 320, 230, 220))
        self.assertTrue(self.result.pre_terminated)
        self.assertFalse(self.result.pre_truncated)
        self.assertTrue(self.result.all_actions_legal)

    def test_actor_indexed_returns_objective_and_all_parameter_deltas(self) -> None:
        for actual, expected in zip(
            self.result.seat_return_scales,
            (-0.2, 0.7, -0.2, -0.3),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertEqual(len(self.result.decision_return_scales), 77)
        for actor, decision_return in zip(
            self.result.pre_actor_trace,
            self.result.decision_return_scales,
        ):
            self.assertAlmostEqual(
                decision_return,
                self.result.seat_return_scales[actor],
                places=6,
            )
        self.assertAlmostEqual(self.result.initial_objective, 0.09366636, places=5)
        self.assertAlmostEqual(
            self.result.post_update_objective,
            0.09301171,
            places=5,
        )
        self.assertLess(
            self.result.post_update_objective,
            self.result.initial_objective,
        )
        expected_deltas = (
            0.0009705852,
            0.0001615889,
            0.0023494314,
            0.0002528356,
        )
        self.assertEqual(len(self.result.parameter_delta_l2), 4)
        for actual, expected in zip(self.result.parameter_delta_l2, expected_deltas):
            self.assertTrue(math.isfinite(actual))
            self.assertGreater(actual, 0.0)
            self.assertAlmostEqual(actual, expected, places=5)

    def test_post_update_replay_is_exactly_identical_and_legal(self) -> None:
        self.assertTrue(self.result.post_replay_identical)
        self.assertEqual(self.result.post_transition_count, 77)
        self.assertEqual(self.result.post_seat_decision_counts, (21, 22, 17, 17))
        self.assertEqual(self.result.post_actor_trace, self.result.pre_actor_trace)
        self.assertEqual(self.result.post_action_trace, self.result.pre_action_trace)
        self.assertEqual(
            self.result.post_legal_action_trace,
            self.result.pre_legal_action_trace,
        )
        self.assertEqual(
            self.result.post_cumulative_raw_rewards,
            self.result.pre_cumulative_raw_rewards,
        )
        self.assertEqual(
            self.result.post_final_raw_rewards,
            self.result.pre_final_raw_rewards,
        )
        self.assertEqual(self.result.post_final_scores, self.result.pre_final_scores)
        self.assertTrue(self.result.post_terminated)
        self.assertFalse(self.result.post_truncated)

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_categorical_mlp_all_project_policy_gradient_smoke(),
        )

    def test_wraps_reviewed_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_all_project_policy_gradient_smoke()

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local shared all-project-seat categorical-MLP raw-outcome update smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one shared all-project-seat categorical-mlp raw-outcome update smoke only",
            "exact seed 1 and exactly one 0.01 gradient update",
            "all four seats sample from one shared reviewed project policy",
            "each selected log probability uses its acting seat cumulative raw return",
            "no baseline, critic, discount, bootstrapping, entropy, replay or shaping",
            "no second update, second round, production self-play, evaluation or league",
            "not improvement, policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_one_actor_indexed_update_and_no_io_or_rule_participant(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("jax.value_and_grad(objective)", source)
        self.assertIn("seat_returns[trajectory.actors]", source)
        self.assertIn("jax.random.categorical", source)
        self.assertIn("range(_TRANSITION_CAP)", source)
        self.assertNotIn("rule_based_player", source)
        self.assertNotIn("state.players.hand", source)
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
