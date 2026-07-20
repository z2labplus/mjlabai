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

import mjlabai.environment.mahjax_rule_based_half_game_smoke as smoke_module  # noqa: E402
from mjlabai.environment import (  # noqa: E402
    MAHJAX_RULE_BASED_HALF_GAME_SMOKE_VERSION,
    MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
    MahJaxRuleBasedHalfGameResult,
    MahJaxRuleBasedHalfGameRoundBoundary,
    MahJaxRuleBasedHalfGameSmokeError,
    MahJaxRuleBasedHalfGameStep,
    run_mahjax_rule_based_half_game_smoke,
)


class MahJaxRuleBasedHalfGameSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_rule_based_half_game_smoke(seed=0)

    def test_exact_public_surface_and_frozen_array_free_objects(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_RULE_BASED_HALF_GAME_SMOKE_VERSION",
                "MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP",
                "MahJaxRuleBasedHalfGameSmokeError",
                "MahJaxRuleBasedHalfGameStep",
                "MahJaxRuleBasedHalfGameRoundBoundary",
                "MahJaxRuleBasedHalfGameResult",
                "run_mahjax_rule_based_half_game_smoke",
            },
        )
        self.assertIsInstance(self.result, MahJaxRuleBasedHalfGameResult)
        self.assertIsInstance(self.result.trace[0], MahJaxRuleBasedHalfGameStep)
        self.assertIsInstance(
            self.result.round_boundaries[0],
            MahJaxRuleBasedHalfGameRoundBoundary,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_RULE_BASED_HALF_GAME_SMOKE_VERSION,
        )
        for value in (
            self.result,
            self.result.trace[0],
            self.result.round_boundaries[0],
        ):
            self.assertNotIn("parameters", {field.name for field in fields(value)})
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]

    def test_pins_runtime_half_game_and_policy_identity(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.round_mode, "half")
        self.assertEqual(self.result.next_round_style, "auto")
        self.assertEqual(
            self.result.policy_id,
            "mahjax.red_mahjong.players.rule_based_player@0.1.2",
        )
        self.assertEqual(MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP, 2048)

    def test_seed_zero_exact_terminal_result(self) -> None:
        self.assertEqual(self.result.seed, 0)
        self.assertEqual(self.result.transition_count, 938)
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(self.result.illegal_action_count, 0)
        self.assertEqual(self.result.initial_scores, (250, 250, 250, 250))
        self.assertEqual(self.result.final_scores, (203, 441, 76, 280))
        self.assertEqual(self.result.final_round_index, 8)
        self.assertEqual(self.result.final_rewards, (-3.0, -3.0, -5.0, 21.0))
        self.assertEqual(
            self.result.cumulative_rewards,
            (73.0, 151.0, -284.0, 10.0),
        )

    def test_exact_round_boundary_lineage_is_complete(self) -> None:
        self.assertEqual(
            tuple(
                (
                    item.completed_transition_count,
                    item.previous_round_index,
                    item.next_round_index,
                    item.scores_after_boundary,
                )
                for item in self.result.round_boundaries
            ),
            (
                (140, 0, 1, (216, 315, 363, 106)),
                (190, 1, 2, (164, 367, 363, 106)),
                (279, 2, 3, (164, 367, 343, 126)),
                (365, 3, 4, (294, 367, 223, 116)),
                (431, 4, 5, (284, 337, 223, 156)),
                (461, 5, 6, (271, 389, 210, 130)),
                (554, 6, 7, (256, 394, 195, 145)),
                (883, 7, 8, (216, 414, 121, 249)),
            ),
        )

    def test_trace_has_global_and_round_local_identity_and_legal_actions(self) -> None:
        self.assertEqual(len(self.result.trace), self.result.transition_count)
        self.assertEqual(
            tuple(item.transition_index for item in self.result.trace),
            tuple(range(938)),
        )
        self.assertEqual(
            tuple(sorted(set(item.round_index for item in self.result.trace))),
            tuple(range(9)),
        )
        for item in self.result.trace:
            self.assertGreaterEqual(item.round_step_index, 0)
            self.assertIn(item.acting_player, range(4))
            self.assertTrue(item.legal_actions)
            self.assertEqual(item.legal_actions, tuple(sorted(item.legal_actions)))
            self.assertEqual(len(item.legal_actions), len(set(item.legal_actions)))
            self.assertTrue(all(0 <= action < 87 for action in item.legal_actions))
            self.assertIn(item.selected_action, item.legal_actions)

    def test_rejects_invalid_seed_before_runtime_use(self) -> None:
        for invalid_seed in (True, -1, 2**32, 0.0, "0", None):
            with self.subTest(seed=invalid_seed):
                with mock.patch.object(
                    smoke_module,
                    "_load_pinned_runtime",
                    side_effect=AssertionError("runtime must not load"),
                ):
                    with self.assertRaisesRegex(
                        MahJaxRuleBasedHalfGameSmokeError,
                        "seed must be an exact int",
                    ):
                        run_mahjax_rule_based_half_game_smoke(  # type: ignore[arg-type]
                            invalid_seed
                        )

    def test_cap_exhaustion_is_an_explicit_error(self) -> None:
        with mock.patch.object(
            smoke_module,
            "MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP",
            1,
        ):
            with self.assertRaisesRegex(
                MahJaxRuleBasedHalfGameSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_rule_based_half_game_smoke(0)

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P4/P8 pinned local bundled-rule-policy half-game environment smoke evidence",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "local cpu half-game environment smoke only",
            "all four seats use the same bundled non-learned",
            "environment-owned legal actions are checked",
            "complete transition and round-boundary provenance",
            "raw environment rewards and global scores",
            "no real tenhou, real haifu, external log or platform data",
            "no project model, learning, update, optimizer, checkpoint or training",
            "not production self-play, league or evaluation",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
            "not candidate-promotion or p9-p12 evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_two_jits_one_bounded_loop_and_no_scope_drift(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertEqual(source.count("jax.jit("), 2)
        self.assertIn('round_mode="half"', source)
        self.assertIn('next_round_style="auto"', source)
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
