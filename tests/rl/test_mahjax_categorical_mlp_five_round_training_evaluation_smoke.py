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

import mjlabai.rl.mahjax_categorical_mlp_five_round_training_evaluation_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_five_round_training_evaluation_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS,
    MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult,
    MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError,
    run_mahjax_categorical_mlp_five_round_training_evaluation_smoke,
)


class MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_five_round_training_evaluation_smoke()
        )

    def test_exact_public_surface_constants_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE",
                "MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError",
                "MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult",
                "run_mahjax_categorical_mlp_five_round_training_evaluation_smoke",
            },
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION,
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult,
        )
        result_fields = {field.name for field in fields(self.result)}
        self.assertNotIn("parameters", result_fields)
        self.assertNotIn("gradients", result_fields)
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 6  # type: ignore[misc]

    def test_exact_training_and_evaluation_seed_contract(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS,
            (1, 3, 5, 7, 11),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS,
            tuple(range(20, 36)),
        )
        self.assertEqual(MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE, 0.01)
        self.assertEqual(self.result.round_count, 5)
        self.assertEqual(self.result.update_count, 5)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertTrue(
            set(self.result.training_seeds).isdisjoint(self.result.evaluation_seeds)
        )
        self.assertEqual(self.result.training_result.epoch_count, 48)

    def test_five_training_rounds_are_exact_legal_terminal_and_continuous(self) -> None:
        self.assertEqual(
            self.result.training_transition_counts,
            (77, 84, 83, 81, 84),
        )
        self.assertEqual(
            self.result.training_seat_decision_counts,
            (
                (21, 22, 17, 17),
                (23, 22, 19, 20),
                (18, 23, 21, 21),
                (18, 21, 23, 19),
                (22, 23, 19, 20),
            ),
        )
        self.assertEqual(
            self.result.training_cumulative_raw_rewards,
            (
                (-20.0, 70.0, -20.0, -30.0),
                (-10.0, -10.0, 20.0, -10.0),
                (20.0, -10.0, -10.0, -10.0),
                (0.0, 0.0, -120.0, 120.0),
                (-10.0, 20.0, -10.0, -10.0),
            ),
        )
        for actors, actions, legal_trace in zip(
            self.result.training_actor_traces,
            self.result.training_action_traces,
            self.result.training_legal_action_traces,
        ):
            self.assertEqual(len(actors), len(actions))
            self.assertEqual(len(actions), len(legal_trace))
            for actor, action, legal_actions in zip(actors, actions, legal_trace):
                self.assertIn(actor, (0, 1, 2, 3))
                self.assertIn(action, legal_actions)
        self.assertTrue(self.result.parameter_continuity_proven)
        self.assertTrue(self.result.all_training_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)

    def test_five_objective_pairs_and_parameter_deltas_are_exact(self) -> None:
        expected_initial = (
            0.0936663598,
            -0.0553588867,
            -0.0609763190,
            -0.0202308446,
            -0.0131035689,
        )
        expected_post = (
            0.0930117071,
            -0.0554395691,
            -0.0609965809,
            -0.0218939111,
            -0.0133588845,
        )
        expected_final = (
            0.0021020556,
            0.0004550584,
            0.0053585209,
            0.0005585462,
        )
        for initial, post, expected_i, expected_p in zip(
            self.result.training_initial_objectives,
            self.result.training_post_update_objectives,
            expected_initial,
            expected_post,
        ):
            self.assertAlmostEqual(initial, expected_i, places=5)
            self.assertAlmostEqual(post, expected_p, places=5)
            self.assertLess(post, initial)
        self.assertEqual(len(self.result.per_update_parameter_delta_l2), 5)
        for delta_row in self.result.per_update_parameter_delta_l2:
            self.assertEqual(len(delta_row), 4)
            self.assertTrue(all(math.isfinite(value) for value in delta_row))
            self.assertTrue(all(value > 0.0 for value in delta_row))
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            expected_final,
        ):
            self.assertAlmostEqual(actual, expected, places=5)

    def test_fixed_mixed_policy_evaluation_is_exact_and_has_no_updates(self) -> None:
        self.assertEqual(
            self.result.evaluation_transition_counts_before,
            (82, 73, 79, 51, 86, 86, 53, 64, 86, 31, 61, 63, 58, 48, 62, 91),
        )
        self.assertEqual(
            self.result.evaluation_transition_counts_after,
            (82, 73, 79, 51, 86, 86, 53, 64, 86, 31, 61, 63, 62, 48, 62, 91),
        )
        self.assertEqual(
            self.result.evaluation_project_raw_rewards_before,
            (
                0.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
                -15.0, 0.0, -180.0, 0.0, 74.0, 0.0, -40.0, 0.0,
            ),
        )
        self.assertEqual(
            self.result.evaluation_project_raw_rewards_after,
            (
                0.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
                -15.0, 0.0, -180.0, 0.0, -60.0, 0.0, -40.0, 0.0,
            ),
        )
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertTrue(self.result.all_evaluation_actions_legal)

    def test_only_seed32_changes_and_fixed_diagnostic_regresses(self) -> None:
        self.assertEqual(self.result.changed_evaluation_seeds, (32,))
        for index, seed in enumerate(self.result.evaluation_seeds):
            if seed == 32:
                self.assertNotEqual(
                    self.result.evaluation_project_action_traces_before[index],
                    self.result.evaluation_project_action_traces_after[index],
                )
                self.assertEqual(
                    self.result.evaluation_final_scores_before[index],
                    (324, 186, 240, 250),
                )
                self.assertEqual(
                    self.result.evaluation_final_scores_after[index],
                    (190, 190, 430, 190),
                )
            else:
                self.assertEqual(
                    self.result.evaluation_project_action_traces_before[index],
                    self.result.evaluation_project_action_traces_after[index],
                )
                self.assertEqual(
                    self.result.evaluation_final_scores_before[index],
                    self.result.evaluation_final_scores_after[index],
                )
        self.assertEqual(self.result.before_project_raw_sum, -320.0)
        self.assertEqual(self.result.after_project_raw_sum, -454.0)
        self.assertEqual(self.result.before_positive_round_count, 1)
        self.assertEqual(self.result.after_positive_round_count, 0)
        self.assertEqual(self.result.before_negative_round_count, 8)
        self.assertEqual(self.result.after_negative_round_count, 9)
        self.assertTrue(self.result.evaluation_regression_observed)

    def test_is_deterministic(self) -> None:
        self.assertEqual(
            self.result,
            run_mahjax_categorical_mlp_five_round_training_evaluation_smoke(),
        )

    def test_wraps_imitation_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_five_round_training_evaluation_smoke()

    def test_warnings_and_source_preserve_failure_evidence_scope(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local five-round shared-policy training and fixed mixed-policy failure diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "evaluation regression observed: project raw sum -320 to -454",
            "objective decreases during training are not policy-improvement evidence",
            "fixed disjoint mixed-policy evaluation performs no gradient update",
            "no persistence, checkpoint, model artifact, external or real data",
            "not improvement, policy-quality or model-strength evidence",
        ):
            self.assertIn(phrase, warning_text)
        source = inspect.getsource(smoke_module)
        self.assertIn(
            "for seed in MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS",
            source,
        )
        self.assertIn(
            "for seed in MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS",
            source,
        )
        self.assertIn("parameters = update.parameters", source)
        self.assertIn("rule_based_player", source)
        self.assertIn("actor == _PROJECT_SEAT", source)
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
