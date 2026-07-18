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

import mjlabai.rl.mahjax_two_project_seat_policy_gradient_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_two_project_seat_policy_gradient_smoke import (  # noqa: E402
    MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE,
    MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS,
    MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED,
    MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION,
    MahJaxTwoProjectSeatPolicyGradientResult,
    run_mahjax_two_project_seat_policy_gradient_smoke,
)


class MahJaxTwoProjectSeatPolicyGradientSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_two_project_seat_policy_gradient_smoke()

    def test_exact_public_surface_constants_and_frozen_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION",
                "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED",
                "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS",
                "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE",
                "MahJaxTwoProjectSeatPolicyGradientSmokeError",
                "MahJaxTwoProjectSeatPolicyGradientResult",
                "run_mahjax_two_project_seat_policy_gradient_smoke",
            },
        )
        self.assertEqual(MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED, 0)
        self.assertEqual(MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS, (0, 2))
        self.assertEqual(MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE, 0.1)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxTwoProjectSeatPolicyGradientResult)
        self.assertIn("project_actor_trace", {f.name for f in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 2  # type: ignore[misc]

    def test_pins_runtime_participants_model_and_update_boundary(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.seed, 0)
        self.assertEqual(self.result.project_seats, (0, 2))
        self.assertEqual(self.result.rule_policy_seats, (1, 3))
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)
        self.assertEqual(self.result.transition_cap, 256)
        self.assertEqual(self.result.learning_rate, 0.1)
        self.assertEqual(self.result.round_count, 1)
        self.assertEqual(self.result.update_count, 1)

    def test_preserves_reviewed_imitation_training_summary(self) -> None:
        self.assertEqual(self.result.training_result.train_example_count, 54)
        self.assertEqual(self.result.training_result.eval_example_count, 64)
        self.assertEqual(self.result.training_result.epoch_count, 16)
        self.assertEqual(self.result.training_result.final_eval_accuracy, 0.5)

    def test_exact_round_participant_counts_and_project_actions(self) -> None:
        self.assertEqual(self.result.transition_count, 92)
        self.assertEqual(self.result.seat_decision_counts, (21, 22, 23, 26))
        self.assertEqual(self.result.project_decision_counts, (21, 23))
        self.assertEqual(self.result.project_decision_count, 44)
        self.assertEqual(
            self.result.project_actor_trace,
            tuple(actor for actor in self.result.actor_trace if actor in (0, 2)),
        )
        self.assertEqual(
            self.result.project_action_trace,
            tuple(
                action
                for actor, action in zip(
                    self.result.actor_trace,
                    self.result.action_trace,
                )
                if actor in (0, 2)
            ),
        )
        self.assertEqual(
            self.result.project_action_trace[:8],
            (10, 75, 19, 14, 18, 31, 33, 25),
        )

    def test_every_action_is_legal_and_policy_ownership_is_exact(self) -> None:
        self.assertEqual(len(self.result.actor_trace), self.result.transition_count)
        self.assertEqual(len(self.result.action_trace), self.result.transition_count)
        self.assertEqual(len(self.result.legal_action_trace), self.result.transition_count)
        self.assertEqual(len(self.result.policy_id_trace), self.result.transition_count)
        for actor, action, legal, policy_id in zip(
            self.result.actor_trace,
            self.result.action_trace,
            self.result.legal_action_trace,
            self.result.policy_id_trace,
        ):
            self.assertIn(action, legal)
            if actor in (0, 2):
                self.assertEqual(policy_id, self.result.project_policy_id)
            else:
                self.assertIn(actor, (1, 3))
                self.assertEqual(policy_id, self.result.rule_policy_id)
        self.assertEqual(
            self.result.policy_id_trace.count(self.result.project_policy_id),
            44,
        )
        self.assertEqual(
            self.result.policy_id_trace.count(self.result.rule_policy_id),
            48,
        )

    def test_exact_raw_outcomes_actor_returns_and_scores(self) -> None:
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(
            self.result.cumulative_raw_rewards,
            (-10.0, -10.0, -10.0, 20.0),
        )
        self.assertEqual(
            self.result.final_raw_rewards,
            (-10.0, -10.0, -10.0, 30.0),
        )
        self.assertEqual(self.result.final_scores, (240, 240, 240, 270))
        for actual in self.result.project_return_scales:
            self.assertAlmostEqual(actual, -0.1, places=6)

    def test_exact_objective_and_nonzero_shared_parameter_update(self) -> None:
        self.assertAlmostEqual(self.result.initial_objective, -0.19244556, places=5)
        self.assertAlmostEqual(
            self.result.post_update_objective,
            -0.19273609,
            places=5,
        )
        self.assertAlmostEqual(self.result.weight_delta_l2, 0.00523261, places=5)
        self.assertAlmostEqual(self.result.bias_delta_l2, 0.00124493, places=5)
        for value in (
            self.result.initial_objective,
            self.result.post_update_objective,
            self.result.weight_delta_l2,
            self.result.bias_delta_l2,
        ):
            self.assertTrue(math.isfinite(value))
        self.assertGreater(self.result.weight_delta_l2, 0.0)
        self.assertGreater(self.result.bias_delta_l2, 0.0)

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_two_project_seat_policy_gradient_smoke(),
        )

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local two-project-seat shared-policy raw-outcome update smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one two-project-seat shared-policy raw-outcome update smoke only",
            "project seats 0 and 2 share one in-memory policy",
            "rule-policy seats 1 and 3 remain fixed and never enter the gradient batch",
            "each project decision uses its acting seat cumulative raw reward",
            "exactly one terminal round and exactly one aggregate shared-policy update",
            "no per-seat update, mid-round update, replay, critic or reward shaping",
            "no persisted data, parameters, model weights, checkpoint or artifact",
            "not four-project-seat or production self-play learning",
            "not improvement, policy-quality, model-strength, stable-dan or luckyj",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_actor_indexing_one_loop_one_update_and_no_io(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertIn("jax.random.split", source)
        self.assertIn("jax.random.categorical", source)
        self.assertIn("return_scales[actor_batch]", source)
        self.assertIn("jax.value_and_grad(objective", source)
        self.assertLess(source.index("for transition_index"), source.index("def objective"))
        self.assertEqual(source.count("objective_and_gradient(weights, biases)"), 1)
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
