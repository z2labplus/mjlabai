from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
import math
from pathlib import Path
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_one_round_policy_gradient_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_one_round_policy_gradient_smoke import (  # noqa: E402
    MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE,
    MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED,
    MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION,
    MahJaxOneRoundPolicyGradientResult,
    MahJaxOneRoundPolicyGradientSmokeError,
    run_mahjax_one_round_policy_gradient_smoke,
)


class MahJaxOneRoundPolicyGradientSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_one_round_policy_gradient_smoke()

    def test_exact_public_surface_constants_and_frozen_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION",
                "MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED",
                "MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE",
                "MahJaxOneRoundPolicyGradientSmokeError",
                "MahJaxOneRoundPolicyGradientResult",
                "run_mahjax_one_round_policy_gradient_smoke",
            },
        )
        self.assertEqual(MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED, 1)
        self.assertEqual(MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE, 0.1)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxOneRoundPolicyGradientResult)
        self.assertIn("return_scale", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 2  # type: ignore[misc]

    def test_pins_runtime_participants_and_reviewed_training(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.project_policy_seat, 0)
        self.assertEqual(self.result.rule_policy_seats, (1, 2, 3))
        self.assertEqual(
            self.result.project_policy_id,
            "project_linear_630x87_imitation_seed_123_epoch_16",
        )
        self.assertEqual(
            self.result.rule_policy_id,
            "mahjax.red_mahjong.players.rule_based_player@0.1.2",
        )
        self.assertEqual(self.result.training_result.train_example_count, 54)
        self.assertEqual(self.result.training_result.eval_example_count, 64)
        self.assertEqual(self.result.training_result.epoch_count, 16)

    def test_exact_model_update_and_raw_return_boundary(self) -> None:
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)
        self.assertEqual(self.result.transition_cap, 256)
        self.assertEqual(self.result.update_count, 1)
        self.assertEqual(self.result.learning_rate, 0.1)
        self.assertEqual(self.result.cumulative_raw_project_reward, -39.0)
        self.assertAlmostEqual(self.result.return_scale, -0.39, places=6)
        self.assertEqual(self.result.project_decision_count, 8)
        self.assertEqual(
            self.result.sampled_project_actions,
            (20, 84, 16, 30, 27, 26, 3, 13),
        )

    def test_objective_and_parameter_deltas_match_probe(self) -> None:
        self.assertAlmostEqual(self.result.initial_objective, -0.86367577, places=5)
        self.assertAlmostEqual(
            self.result.post_update_objective,
            -0.88331068,
            places=5,
        )
        self.assertAlmostEqual(self.result.weight_delta_l2, 0.04220101, places=5)
        self.assertAlmostEqual(self.result.bias_delta_l2, 0.01279154, places=5)
        self.assertTrue(
            all(
                math.isfinite(value)
                for value in (
                    self.result.initial_objective,
                    self.result.post_update_objective,
                    self.result.weight_delta_l2,
                    self.result.bias_delta_l2,
                )
            )
        )
        self.assertGreater(self.result.weight_delta_l2, 0.0)
        self.assertGreater(self.result.bias_delta_l2, 0.0)

    def test_pre_and_post_rounds_are_exact_terminal_raw_outcomes(self) -> None:
        self.assertEqual(self.result.pre_transition_count, 37)
        self.assertEqual(self.result.post_transition_count, 37)
        self.assertTrue(self.result.pre_terminated)
        self.assertTrue(self.result.post_terminated)
        self.assertFalse(self.result.pre_truncated)
        self.assertFalse(self.result.post_truncated)
        self.assertEqual(self.result.pre_final_rewards, (-39.0, 39.0, 0.0, 0.0))
        self.assertEqual(self.result.post_final_rewards, self.result.pre_final_rewards)
        self.assertEqual(
            self.result.pre_cumulative_rewards,
            (-39.0, 39.0, 0.0, 0.0),
        )
        self.assertEqual(
            self.result.post_cumulative_rewards,
            self.result.pre_cumulative_rewards,
        )
        self.assertEqual(self.result.pre_final_scores, (211, 289, 250, 250))
        self.assertEqual(self.result.post_final_scores, self.result.pre_final_scores)

    def test_complete_pre_and_post_traces_are_legal_and_policy_bound(self) -> None:
        for actors, actions, legal_history, policy_ids in (
            (
                self.result.pre_actor_trace,
                self.result.pre_action_trace,
                self.result.pre_legal_action_trace,
                self.result.pre_policy_id_trace,
            ),
            (
                self.result.post_actor_trace,
                self.result.post_action_trace,
                self.result.post_legal_action_trace,
                self.result.post_policy_id_trace,
            ),
        ):
            self.assertEqual(len(actors), 37)
            self.assertEqual(len(actions), len(legal_history))
            self.assertEqual(len(actions), len(policy_ids))
            for actor, action, legal_actions, policy_id in zip(
                actors,
                actions,
                legal_history,
                policy_ids,
            ):
                self.assertIn(action, legal_actions)
                expected_policy = (
                    self.result.project_policy_id
                    if actor == self.result.project_policy_seat
                    else self.result.rule_policy_id
                )
                self.assertEqual(policy_id, expected_policy)
        self.assertEqual(self.result.post_action_trace, self.result.pre_action_trace)

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_one_round_policy_gradient_smoke(),
        )

    def test_cap_exhaustion_is_explicit(self) -> None:
        with mock.patch.object(smoke_module, "_TRANSITION_CAP", 1):
            with self.assertRaisesRegex(
                MahJaxOneRoundPolicyGradientSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_one_round_policy_gradient_smoke()

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local one-round on-policy raw-outcome gradient-update smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "first environment raw-outcome policy-gradient update smoke only",
            "one seed-1 round and exactly one gradient update",
            "project seat 0 samples from the legal-masked categorical policy",
            "environment, bundled-rule and project-action rng streams are independent",
            "return is only cumulative raw seat-0 reward divided by 100",
            "no baseline, discount, bootstrapping, critic, replay or reward shaping",
            "no persisted data, parameters, model weights, checkpoint or artifact",
            "no self-play learning, multiple rounds, seat rotation, evaluation or league",
            "no real tenhou, real haifu, external log or platform data",
            "not improvement, policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_on_policy_sampling_one_loop_one_update_and_no_io(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertIn("init_key, rule_key, project_key = jax.random.split", source)
        self.assertIn("jax.random.categorical", source)
        self.assertIn("encode_mahjax_public_observation", source)
        self.assertIn("jax.value_and_grad(objective", source)
        self.assertIn(
            "trajectory.cumulative_rewards[_PROJECT_SEAT] / 100.0",
            source,
        )
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
            "replay_buffer",
            "platform_data",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
