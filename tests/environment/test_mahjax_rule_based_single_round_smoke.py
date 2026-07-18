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

import mjlabai.environment.mahjax_rule_based_single_round_smoke as smoke_module  # noqa: E402
from mjlabai.environment import (  # noqa: E402
    MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION,
    MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP,
    MahJaxRuleBasedSingleRoundResult,
    MahJaxRuleBasedSingleRoundSmokeError,
    MahJaxRuleBasedSingleRoundStep,
    run_mahjax_rule_based_single_round_smoke,
)


class MahJaxRuleBasedSingleRoundSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_rule_based_single_round_smoke(seed=0)

    def test_exact_public_surface_and_frozen_objects(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION",
                "MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP",
                "MahJaxRuleBasedSingleRoundSmokeError",
                "MahJaxRuleBasedSingleRoundStep",
                "MahJaxRuleBasedSingleRoundResult",
                "run_mahjax_rule_based_single_round_smoke",
            },
        )
        self.assertEqual(MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP, 256)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxRuleBasedSingleRoundResult)
        self.assertIsInstance(self.result.trace[0], MahJaxRuleBasedSingleRoundStep)
        self.assertEqual(
            {field.name for field in fields(self.result.trace[0])},
            {"pre_step_index", "acting_player", "legal_actions", "selected_action"},
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            self.result.trace[0].selected_action = 0  # type: ignore[misc]

    def test_pins_runtime_environment_and_policy_identity(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(
            self.result.policy_id,
            "mahjax.red_mahjong.players.rule_based_player@0.1.2",
        )
        pyproject = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('"mahjax==0.1.2"', pyproject)
        self.assertIn('"jax==0.4.30"', pyproject)
        self.assertIn('"jaxlib==0.4.30"', pyproject)

    def test_seed_zero_exact_terminal_result(self) -> None:
        self.assertEqual(self.result.seed, 0)
        self.assertEqual(self.result.transition_count, 54)
        self.assertEqual(self.result.final_step_count, 54)
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(self.result.final_rewards, (0.0, 0.0, 150.0, -120.0))
        self.assertEqual(
            self.result.cumulative_rewards,
            (-20.0, 0.0, 130.0, -130.0),
        )
        self.assertEqual(self.result.final_scores, (240, 250, 390, 120))

    def test_trace_is_complete_monotonic_and_policy_actions_are_legal(self) -> None:
        self.assertEqual(len(self.result.trace), self.result.transition_count)
        self.assertEqual(
            tuple(step.pre_step_index for step in self.result.trace),
            tuple(range(self.result.transition_count)),
        )
        for step in self.result.trace:
            self.assertIn(step.acting_player, range(4))
            self.assertTrue(step.legal_actions)
            self.assertEqual(step.legal_actions, tuple(sorted(step.legal_actions)))
            self.assertEqual(len(step.legal_actions), len(set(step.legal_actions)))
            self.assertTrue(all(0 <= action < 87 for action in step.legal_actions))
            self.assertIn(step.selected_action, step.legal_actions)

    def test_round_finishes_inside_hard_bound(self) -> None:
        self.assertEqual(self.result.transition_cap, 256)
        self.assertLess(self.result.transition_count, self.result.transition_cap)
        self.assertEqual(self.result.final_step_count, self.result.transition_count)
        self.assertIn(self.result.initial_player, range(4))
        self.assertIn(self.result.final_player, range(4))

    def test_rewards_are_unshaped_four_tuples_and_scores_are_global(self) -> None:
        self.assertIs(type(self.result.final_rewards), tuple)
        self.assertIs(type(self.result.cumulative_rewards), tuple)
        self.assertEqual(len(self.result.final_rewards), 4)
        self.assertEqual(len(self.result.cumulative_rewards), 4)
        self.assertTrue(all(type(value) is float for value in self.result.final_rewards))
        self.assertTrue(
            all(type(value) is float for value in self.result.cumulative_rewards)
        )
        source = inspect.getsource(smoke_module)
        self.assertIn("state.round_state.score", source)
        self.assertNotIn('observe(state)["scores"]', source)

    def test_is_deterministic_for_equal_seed_and_rng_lineage(self) -> None:
        self.assertEqual(self.result, run_mahjax_rule_based_single_round_smoke(0))
        self.assertEqual(self.result.trace[0].acting_player, 2)
        self.assertEqual(self.result.trace[0].selected_action, 27)
        self.assertEqual(self.result.trace[-1].acting_player, 2)
        self.assertEqual(self.result.trace[-1].selected_action, 74)

    def test_rejects_invalid_seed_before_runtime_use(self) -> None:
        for invalid_seed in (True, -1, 2**32, 0.0, "0", None):
            with self.subTest(seed=invalid_seed):
                with mock.patch.object(
                    smoke_module,
                    "_load_pinned_runtime",
                    side_effect=AssertionError("runtime must not load"),
                ):
                    with self.assertRaisesRegex(
                        MahJaxRuleBasedSingleRoundSmokeError,
                        "seed must be an exact int",
                    ):
                        run_mahjax_rule_based_single_round_smoke(  # type: ignore[arg-type]
                            invalid_seed
                        )

    def test_cap_exhaustion_is_an_explicit_error(self) -> None:
        with mock.patch.object(
            smoke_module,
            "MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP",
            1,
        ):
            with self.assertRaisesRegex(
                MahJaxRuleBasedSingleRoundSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_rule_based_single_round_smoke(0)

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P4 pinned local rule-policy-to-environment single-round smoke evidence",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "bundled rule-policy local cpu round only",
            "all four seats use the same bundled non-learned red-riichi rule policy",
            "environment-owned legal actions are checked",
            "raw environment rewards are recorded without shaping",
            "no real tenhou, real haifu, external log or platform data",
            "no project model, learning, update, optimizer, checkpoint or training",
            "not production self-play, league or evaluation",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_two_jits_one_bounded_loop_and_no_scope_drift(self) -> None:
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
        self.assertEqual(len(jit_calls), 2)
        self.assertIn("init_key, policy_key = jax.random.split(root_key)", source)
        self.assertIn("policy_key, action_key = jax.random.split(policy_key)", source)
        for forbidden in (
            "Path(",
            "open(",
            "requests",
            "socket",
            "subprocess",
            "optimizer(",
            "checkpoint(",
            "model_callback",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
