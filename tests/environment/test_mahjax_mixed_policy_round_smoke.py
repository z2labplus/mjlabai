from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.environment.mahjax_mixed_policy_round_smoke as smoke_module  # noqa: E402
from mjlabai.environment.mahjax_mixed_policy_round_smoke import (  # noqa: E402
    MAHJAX_MIXED_POLICY_ROUND_SEED,
    MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION,
    MahJaxMixedPolicyRoundResult,
    MahJaxMixedPolicyRoundSmokeError,
    MahJaxMixedPolicyRoundStep,
    run_mahjax_mixed_policy_round_smoke,
)


class MahJaxMixedPolicyRoundSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_mixed_policy_round_smoke()

    def test_exact_public_surface_and_frozen_objects(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION",
                "MAHJAX_MIXED_POLICY_ROUND_SEED",
                "MahJaxMixedPolicyRoundSmokeError",
                "MahJaxMixedPolicyRoundStep",
                "MahJaxMixedPolicyRoundResult",
                "run_mahjax_mixed_policy_round_smoke",
            },
        )
        self.assertEqual(MAHJAX_MIXED_POLICY_ROUND_SEED, 0)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxMixedPolicyRoundResult)
        self.assertIsInstance(self.result.trace[0], MahJaxMixedPolicyRoundStep)
        self.assertEqual(
            {field.name for field in fields(self.result.trace[0])},
            {
                "pre_step_index",
                "acting_player",
                "policy_id",
                "legal_actions",
                "selected_action",
            },
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]

    def test_pins_environment_model_and_seat_policy_identity(self) -> None:
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
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)

    def test_preserves_reviewed_training_summary(self) -> None:
        training = self.result.training_result
        self.assertEqual(training.train_example_count, 54)
        self.assertEqual(training.eval_example_count, 64)
        self.assertEqual(training.epoch_count, 16)
        self.assertAlmostEqual(training.final_train_loss, 1.38197553, places=5)
        self.assertAlmostEqual(training.final_eval_loss, 1.54172158, places=5)
        self.assertEqual(training.final_eval_accuracy, 0.5)

    def test_exact_seed_zero_terminal_raw_outcome(self) -> None:
        self.assertEqual(self.result.transition_cap, 256)
        self.assertEqual(self.result.transition_count, 54)
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(self.result.final_rewards, (0.0, 0.0, 140.0, -120.0))
        self.assertEqual(
            self.result.cumulative_rewards,
            (0.0, 0.0, 120.0, -140.0),
        )
        self.assertEqual(self.result.final_scores, (250, 250, 380, 120))

    def test_trace_is_complete_legal_and_policy_bound_by_seat(self) -> None:
        self.assertEqual(len(self.result.trace), self.result.transition_count)
        self.assertEqual(
            tuple(step.pre_step_index for step in self.result.trace),
            tuple(range(self.result.transition_count)),
        )
        for step in self.result.trace:
            self.assertIn(step.selected_action, step.legal_actions)
            self.assertEqual(step.legal_actions, tuple(sorted(step.legal_actions)))
            expected_policy = (
                self.result.project_policy_id
                if step.acting_player == self.result.project_policy_seat
                else self.result.rule_policy_id
            )
            self.assertEqual(step.policy_id, expected_policy)

    def test_project_policy_turns_are_exact_and_legal(self) -> None:
        project_steps = tuple(
            step
            for step in self.result.trace
            if step.acting_player == self.result.project_policy_seat
        )
        self.assertEqual(self.result.project_policy_turn_count, 10)
        self.assertEqual(self.result.rule_policy_turn_count, 44)
        self.assertEqual(len(project_steps), 10)
        self.assertEqual(tuple(step.selected_action for step in project_steps), (71,) * 10)
        self.assertTrue(all(71 in step.legal_actions for step in project_steps))

    def test_is_deterministic(self) -> None:
        self.assertEqual(self.result, run_mahjax_mixed_policy_round_smoke())

    def test_cap_exhaustion_is_explicit(self) -> None:
        with mock.patch.object(smoke_module, "_TRANSITION_CAP", 1):
            with self.assertRaisesRegex(
                MahJaxMixedPolicyRoundSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_mixed_policy_round_smoke()

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local mixed-policy single-round interaction smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one trained-project-seat versus three bundled-rule-seats",
            "seat 0 uses reviewed in-memory imitation parameters",
            "seats 1, 2 and 3 use the pinned bundled non-learned rule policy",
            "environment legal mask is authoritative",
            "raw environment rewards and global seat scores are preserved",
            "no persisted data, parameters, model weights, checkpoint or artifact",
            "no reward objective, reinforcement-learning update or self-play learning",
            "no multiple rounds, seat rotation, aggregate evaluation or league",
            "no real tenhou, real haifu, external log or platform data",
            "not production self-play, evaluation or candidate promotion",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_exact_jits_loop_rng_legality_and_no_persistence(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        jit_calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "jax"
            and node.func.attr == "jit"
        ]
        self.assertEqual(len(jit_calls), 3)
        self.assertIn("init_key, policy_key = jax.random.split(root_key)", source)
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
