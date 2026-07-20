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

import mjlabai.rl.mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke as smoke_module  # noqa: E402,E501
from mjlabai.rl import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED,
    MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_POLICY_GRADIENT_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED,
    MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult,
    MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError,
    run_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke,
)


class MahJaxCategoricalMlpSeat0HalfGamePolicyGradientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_POLICY_GRADIENT_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED",
                "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED",
                "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE",
                "MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError",
                "MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult",
                "run_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult,
        )
        names = {field.name for field in fields(self.result)}
        for forbidden in ("parameters", "features", "legal_masks"):
            self.assertNotIn(forbidden, names)
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 2  # type: ignore[misc]

    def test_exact_runtime_model_seed_and_update_contract(self) -> None:
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_POLICY_GRADIENT_SMOKE_VERSION,
        )
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.feature_count, 882)
        self.assertEqual(self.result.hidden_unit_count, 64)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 62_167)
        self.assertEqual(self.result.project_seat, 0)
        self.assertEqual(
            self.result.training_seed,
            MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED,
        )
        self.assertEqual(
            self.result.evaluation_seed,
            MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED,
        )
        self.assertEqual(self.result.training_seed, 0)
        self.assertEqual(self.result.evaluation_seed, 1)
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertEqual(
            self.result.learning_rate,
            MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE,
        )
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.update_count, 1)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertIsNone(self.result.selected_model_id)

    def test_training_half_game_and_raw_return_are_exact(self) -> None:
        self.assertEqual(self.result.training_transition_count, 427)
        self.assertEqual(self.result.training_project_decision_count, 102)
        self.assertEqual(
            self.result.training_cumulative_rewards,
            (-53.0, 82.0, 429.0, -468.0),
        )
        self.assertEqual(
            self.result.training_final_rewards,
            (0.0, 87.0, 0.0, -77.0),
        )
        self.assertEqual(
            self.result.training_final_scores,
            (201, 297, 556, -54),
        )
        self.assertEqual(self.result.training_final_round_index, 5)
        self.assertEqual(self.result.training_red_pon_normalization_count, 0)
        self.assertTrue(self.result.training_terminated)
        self.assertFalse(self.result.training_truncated)
        self.assertAlmostEqual(self.result.return_scale, -0.53, places=6)

    def test_objective_and_all_parameter_deltas_are_exact(self) -> None:
        self.assertAlmostEqual(
            self.result.initial_objective,
            -0.5453851223,
            places=5,
        )
        self.assertAlmostEqual(
            self.result.post_update_objective,
            -0.5463446379,
            places=5,
        )
        self.assertLess(
            self.result.post_update_objective,
            self.result.initial_objective,
        )
        expected = (
            0.0009908610,
            0.0002095903,
            0.0028836143,
            0.0003556903,
        )
        self.assertEqual(len(self.result.parameter_delta_l2), 4)
        for actual, target in zip(self.result.parameter_delta_l2, expected):
            self.assertTrue(math.isfinite(actual))
            self.assertGreater(actual, 0.0)
            self.assertAlmostEqual(actual, target, places=5)

    def test_disjoint_evaluation_retains_exact_negative_result(self) -> None:
        self.assertEqual(self.result.initial_evaluation_transition_count, 526)
        self.assertEqual(
            self.result.initial_evaluation_project_decision_count,
            132,
        )
        self.assertEqual(
            self.result.initial_evaluation_cumulative_rewards,
            (-300.0, -34.0, 178.0, 96.0),
        )
        self.assertEqual(
            self.result.initial_evaluation_final_rewards,
            (-80.0, 0.0, 0.0, 110.0),
        )
        self.assertEqual(
            self.result.initial_evaluation_final_scores,
            (-70, 278, 376, 416),
        )
        self.assertEqual(self.result.initial_evaluation_final_round_index, 5)
        self.assertEqual(self.result.updated_evaluation_transition_count, 524)
        self.assertEqual(
            self.result.updated_evaluation_project_decision_count,
            130,
        )
        self.assertEqual(
            self.result.updated_evaluation_cumulative_rewards,
            (-320.0, -54.0, 158.0, 156.0),
        )
        self.assertEqual(
            self.result.updated_evaluation_final_rewards,
            (-80.0, 0.0, 0.0, 110.0),
        )
        self.assertEqual(
            self.result.updated_evaluation_final_scores,
            (-80, 268, 366, 446),
        )
        self.assertEqual(self.result.updated_evaluation_final_round_index, 5)
        self.assertEqual(
            self.result.initial_evaluation_red_pon_normalization_count,
            0,
        )
        self.assertEqual(
            self.result.updated_evaluation_red_pon_normalization_count,
            0,
        )
        self.assertTrue(self.result.evaluation_behavior_changed)
        self.assertTrue(self.result.negative_evaluation_observed)

    def test_all_traces_are_complete_legal_and_round_local(self) -> None:
        traces = (
            self.result.training_trace,
            self.result.initial_evaluation_trace,
            self.result.updated_evaluation_trace,
        )
        for trace in traces:
            self.assertEqual(
                tuple(item.transition_index for item in trace),
                tuple(range(len(trace))),
            )
            rounds = {item.round_index for item in trace}
            for round_index in rounds:
                local_steps = tuple(
                    item.round_step_index
                    for item in trace
                    if item.round_index == round_index
                )
                self.assertEqual(local_steps, tuple(range(len(local_steps))))
            for item in trace:
                self.assertIn(item.acting_player, range(4))
                self.assertTrue(item.legal_actions)
                self.assertIn(item.applied_action, item.legal_actions)
                self.assertFalse(item.red_pon_normalized)
        training_project = tuple(
            item for item in self.result.training_trace if item.acting_player == 0
        )
        initial_project = tuple(
            item
            for item in self.result.initial_evaluation_trace
            if item.acting_player == 0
        )
        updated_project = tuple(
            item
            for item in self.result.updated_evaluation_trace
            if item.acting_player == 0
        )
        self.assertEqual(len(training_project), 102)
        self.assertEqual(len(initial_project), 132)
        self.assertEqual(len(updated_project), 130)
        for item in training_project:
            self.assertEqual(item.policy_id, self.result.sampled_project_policy_id)
        for item in (*initial_project, *updated_project):
            self.assertEqual(item.policy_id, self.result.greedy_project_policy_id)

    def test_boundary_and_terminal_flags_remain_environment_owned(self) -> None:
        self.assertTrue(self.result.all_actions_legal)
        self.assertTrue(self.result.all_games_terminated_without_truncation)
        for boundaries, final_round in (
            (self.result.training_round_boundaries, 5),
            (self.result.initial_evaluation_round_boundaries, 5),
            (self.result.updated_evaluation_round_boundaries, 5),
        ):
            self.assertTrue(boundaries)
            self.assertEqual(boundaries[-1].next_round_index, final_round)
            self.assertEqual(
                tuple(item.next_round_index for item in boundaries),
                tuple(range(1, final_round + 1)),
            )

    def test_wraps_reviewed_training_or_runtime_failure(self) -> None:
        with mock.patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError,
                "reviewed categorical MLP or pinned runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke()

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local one-update seat-0 half-game raw-outcome failure diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "one sampled seed-0 project-seat half-game and exactly one 0.01 update",
            "seat 0 uses cumulative raw reward divided by 100",
            "disjoint seed-1 greedy evaluation performs zero updates",
            "negative evaluation retained: seat-0 cumulative reward -300 to -320",
            "negative evaluation retained: seat-0 final score -70 to -80",
            "no second training half-game, replay, search, selection or rollback",
            "no saved parameters, weights, checkpoint, dataset or artifact",
            "no real tenhou, real haifu, external log or platform data",
            "not improvement, policy-quality or model-strength evidence",
            "not stable-dan, luckyj 10.68 or p9-p12 evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_one_rollout_loop_one_update_and_no_io(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertEqual(source.count("jax.value_and_grad(objective)"), 1)
        self.assertIn("jax.random.categorical", source)
        self.assertIn("return_scale * selected_log_probabilities", source)
        self.assertIn("_normalize_rule_action", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            ".load(",
            "pickle",
            "requests",
            "socket",
            "subprocess",
            "selected_parameters",
            "learning_rate_candidates",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
