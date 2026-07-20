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

import mjlabai.environment.mahjax_categorical_mlp_mixed_half_game_smoke as smoke_module  # noqa: E402,E501
from mjlabai.environment import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT,
    MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_SMOKE_VERSION,
    MahJaxCategoricalMlpMixedHalfGameResult,
    MahJaxCategoricalMlpMixedHalfGameSmokeError,
    MahJaxCategoricalMlpMixedHalfGameStep,
    run_mahjax_categorical_mlp_mixed_half_game_smoke,
)


class MahJaxCategoricalMlpMixedHalfGameSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_mixed_half_game_smoke(0)

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT",
                "MahJaxCategoricalMlpMixedHalfGameSmokeError",
                "MahJaxCategoricalMlpMixedHalfGameStep",
                "MahJaxCategoricalMlpMixedHalfGameResult",
                "run_mahjax_categorical_mlp_mixed_half_game_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpMixedHalfGameResult,
        )
        self.assertIsInstance(
            self.result.trace[0],
            MahJaxCategoricalMlpMixedHalfGameStep,
        )
        for value in (self.result, self.result.trace[0]):
            names = {field.name for field in fields(value)}
            self.assertNotIn("parameters", names)
            self.assertNotIn("weights", names)
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]

    def test_pins_model_environment_and_policy_roles(self) -> None:
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_SMOKE_VERSION,
        )
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.feature_count, 882)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(
            self.result.project_seat,
            MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT,
        )
        self.assertEqual(self.result.project_seat, 0)
        self.assertIn("categorical_mlp_imitation", self.result.project_policy_id)
        self.assertIn("rule_based_player", self.result.rule_policy_id)

    def test_seed_zero_exact_terminal_result(self) -> None:
        self.assertEqual(self.result.seed, 0)
        self.assertEqual(self.result.transition_cap, 2048)
        self.assertEqual(self.result.transition_count, 825)
        self.assertEqual(self.result.project_decision_count, 200)
        self.assertEqual(self.result.rule_decision_count, 625)
        self.assertEqual(self.result.final_round_index, 8)
        self.assertEqual(self.result.final_scores, (40, 265, 379, 316))
        self.assertEqual(self.result.final_rewards, (-20.0, 0.0, 30.0, 0.0))
        self.assertEqual(
            self.result.cumulative_rewards,
            (-200.0, 15.0, 12.0, 123.0),
        )
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(self.result.half_game_update_count, 0)
        self.assertIsNone(self.result.selected_model_id)

    def test_exact_round_boundary_lineage(self) -> None:
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
                (121, 0, 1, (250, 285, 345, 120)),
                (158, 1, 2, (198, 337, 345, 120)),
                (228, 2, 3, (188, 332, 340, 140)),
                (304, 3, 4, (188, 332, 263, 217)),
                (477, 4, 5, (162, 296, 257, 285)),
                (557, 5, 6, (85, 373, 257, 285)),
                (600, 6, 7, (85, 363, 231, 321)),
                (769, 7, 8, (90, 275, 329, 306)),
            ),
        )

    def test_trace_is_complete_legal_and_has_true_round_local_steps(self) -> None:
        self.assertEqual(len(self.result.trace), 825)
        self.assertEqual(
            tuple(item.transition_index for item in self.result.trace),
            tuple(range(825)),
        )
        for round_index in range(9):
            round_steps = tuple(
                item.round_step_index
                for item in self.result.trace
                if item.round_index == round_index
            )
            self.assertEqual(round_steps, tuple(range(len(round_steps))))
        for item in self.result.trace:
            self.assertIn(item.acting_player, range(4))
            self.assertTrue(item.legal_actions)
            self.assertIn(item.applied_action, item.legal_actions)
            if item.acting_player == 0:
                self.assertEqual(item.policy_id, self.result.project_policy_id)
                self.assertEqual(item.raw_action, item.applied_action)
                self.assertFalse(item.red_pon_normalized)
            else:
                self.assertEqual(item.policy_id, self.result.rule_policy_id)

    def test_only_exact_red_pon_normalization_occurs(self) -> None:
        normalized = tuple(
            item for item in self.result.trace if item.red_pon_normalized
        )
        self.assertEqual(self.result.red_pon_normalization_count, 1)
        self.assertEqual(len(normalized), 1)
        item = normalized[0]
        self.assertEqual(
            (
                item.transition_index,
                item.acting_player,
                item.raw_action,
                item.applied_action,
                item.legal_actions,
            ),
            (450, 3, 75, 76, (76, 84)),
        )
        self.assertNotIn(item.raw_action, item.legal_actions)
        self.assertIn(item.applied_action, item.legal_actions)

    def test_normalizer_rejects_every_other_illegal_action(self) -> None:
        self.assertEqual(smoke_module._normalize_rule_action(75, (76, 84)), (76, True))
        self.assertEqual(smoke_module._normalize_rule_action(84, (76, 84)), (84, False))
        for action, legal in ((74, (84,)), (75, (84,)), (76, (75, 84))):
            with self.subTest(action=action, legal=legal):
                with self.assertRaisesRegex(
                    MahJaxCategoricalMlpMixedHalfGameSmokeError,
                    "unsupported illegal action",
                ):
                    smoke_module._normalize_rule_action(action, legal)

    def test_rejects_invalid_seed_before_parameter_training(self) -> None:
        for invalid_seed in (True, -1, 2**32, 0.0, "0", None):
            with self.subTest(seed=invalid_seed):
                with mock.patch.object(
                    smoke_module,
                    "_train_mahjax_categorical_mlp_parameters",
                    side_effect=AssertionError("training helper must not run"),
                ):
                    with self.assertRaisesRegex(
                        MahJaxCategoricalMlpMixedHalfGameSmokeError,
                        "seed must be an exact int",
                    ):
                        run_mahjax_categorical_mlp_mixed_half_game_smoke(  # type: ignore[arg-type]
                            invalid_seed
                        )

    def test_cap_exhaustion_is_an_explicit_error(self) -> None:
        with mock.patch.object(
            smoke_module,
            "MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP",
            1,
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpMixedHalfGameSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_categorical_mlp_mixed_half_game_smoke(0)

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P4/P7/P8 pinned local read-only categorical-MLP mixed half-game smoke evidence",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one pinned local seed-0",
            "without half-game updates",
            "bundled mahjax rule policy drives seats 1 through 3",
            "only raw pon 75 to legal pon_red 76 normalization",
            "every raw and applied action",
            "complete transition and round-boundary provenance",
            "no saved parameters, weights, checkpoint, dataset or artifact",
            "no real tenhou, real haifu, external log or platform data",
            "not production self-play, evaluation, league or candidate promotion",
            "not improvement, policy-quality or model-strength evidence",
            "not stable-dan, luckyj 10.68 or p9-p12 evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_one_loop_three_jits_and_no_general_fallback(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertEqual(source.count("jax.jit("), 3)
        self.assertIn("raw_action == _PON_ACTION", source)
        self.assertIn("_PON_RED_ACTION in legal_actions", source)
        for forbidden in (
            "random.choice",
            "legal_actions[0]",
            "Path(",
            "open(",
            "requests",
            "socket",
            "subprocess",
            "checkpoint(",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
