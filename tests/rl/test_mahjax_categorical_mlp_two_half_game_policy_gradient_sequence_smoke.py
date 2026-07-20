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

import mjlabai.rl.mahjax_categorical_mlp_two_half_game_policy_gradient_sequence_smoke as smoke_module  # noqa: E402,E501
from mjlabai.rl import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_SEQUENCE_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS,
    MahJaxCategoricalMlpTwoHalfGameEvaluationRecord,
    MahJaxCategoricalMlpTwoHalfGameSequenceResult,
    MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError,
    MahJaxCategoricalMlpTwoHalfGameTrainingRecord,
    run_mahjax_categorical_mlp_two_half_game_sequence_smoke,
)


class MahJaxCategoricalMlpTwoHalfGameSequenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_two_half_game_sequence_smoke()

    def test_exact_public_surface_and_frozen_array_free_output(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_SEQUENCE_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_LEARNING_RATE",
                "MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError",
                "MahJaxCategoricalMlpTwoHalfGameTrainingRecord",
                "MahJaxCategoricalMlpTwoHalfGameEvaluationRecord",
                "MahJaxCategoricalMlpTwoHalfGameSequenceResult",
                "run_mahjax_categorical_mlp_two_half_game_sequence_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpTwoHalfGameSequenceResult,
        )
        self.assertIsInstance(
            self.result.training_records[0],
            MahJaxCategoricalMlpTwoHalfGameTrainingRecord,
        )
        self.assertIsInstance(
            self.result.evaluation_records[0],
            MahJaxCategoricalMlpTwoHalfGameEvaluationRecord,
        )
        for value in (
            self.result,
            self.result.training_records[0],
            self.result.evaluation_records[0],
        ):
            names = {field.name for field in fields(value)}
            for forbidden in ("parameters", "features", "legal_masks"):
                self.assertNotIn(forbidden, names)
        with self.assertRaises(FrozenInstanceError):
            self.result.update_count = 3  # type: ignore[misc]

    def test_exact_runtime_seeds_counts_and_continuity_contract(self) -> None:
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_SEQUENCE_SMOKE_VERSION,
        )
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(self.result.feature_count, 882)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 62_167)
        self.assertEqual(
            self.result.training_seeds,
            MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS,
        )
        self.assertEqual(self.result.training_seeds, (0, 1))
        self.assertEqual(
            self.result.evaluation_seeds,
            MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS,
        )
        self.assertEqual(self.result.evaluation_seeds, (2, 3))
        self.assertEqual(
            self.result.learning_rate,
            MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_LEARNING_RATE,
        )
        self.assertEqual(self.result.learning_rate, 0.01)
        self.assertEqual(self.result.training_half_game_count, 2)
        self.assertEqual(self.result.update_count, 2)
        self.assertEqual(self.result.evaluation_half_game_count, 2)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertTrue(self.result.parameter_continuity_proven)
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertIsNone(self.result.selected_model_id)

    def test_exact_ordered_training_records_and_updates(self) -> None:
        expected = (
            (
                0, 427, 102, (-53.0, 82.0, 429.0, -468.0),
                (0.0, 87.0, 0.0, -77.0), (201, 297, 556, -54), 5,
                -0.53, -0.5453851223, -0.5463446379,
                (0.0009908610, 0.0002095903, 0.0028836143, 0.0003556903),
            ),
            (
                1, 797, 196, (-259.0, 140.0, 155.0, -56.0),
                (-27.0, 65.0, -14.0, -14.0), (-16, 440, 382, 194), 8,
                -2.59, -3.4532430172, -3.4597692490,
                (0.0031369785, 0.0007574092, 0.0072538634, 0.0013632783),
            ),
        )
        self.assertEqual(len(self.result.training_records), 2)
        for record, target in zip(self.result.training_records, expected):
            self.assertEqual(record.seed, target[0])
            self.assertEqual(record.transition_count, target[1])
            self.assertEqual(record.project_decision_count, target[2])
            self.assertEqual(record.cumulative_rewards, target[3])
            self.assertEqual(record.final_rewards, target[4])
            self.assertEqual(record.final_scores, target[5])
            self.assertEqual(record.final_round_index, target[6])
            self.assertEqual(record.red_pon_normalization_count, 0)
            self.assertTrue(record.terminated)
            self.assertFalse(record.truncated)
            self.assertAlmostEqual(record.return_scale, target[7], places=5)
            self.assertAlmostEqual(record.initial_objective, target[8], places=5)
            self.assertAlmostEqual(
                record.post_update_objective,
                target[9],
                places=5,
            )
            self.assertLess(record.post_update_objective, record.initial_objective)
            for actual, value in zip(record.parameter_delta_l2, target[10]):
                self.assertTrue(math.isfinite(actual))
                self.assertGreater(actual, 0.0)
                self.assertAlmostEqual(actual, value, places=5)

    def test_exact_disjoint_evaluation_records_and_aggregate(self) -> None:
        expected = (
            (
                2, 780, 202, (-344.0, 157.0, -242.0, 419.0),
                (0.0, 29.0, -29.0, 0.0), (-26, 412, 23, 591),
                820, 215, (-387.0, 207.0, -236.0, 396.0),
                (-43.0, 99.0, -23.0, -23.0), (-69, 472, 29, 568),
            ),
            (
                3, 907, 228, (-288.0, -29.0, 389.0, -102.0),
                (-32.0, -32.0, 136.0, -62.0), (-48, 221, 549, 278),
                1099, 262, (-247.0, -37.0, 482.0, -268.0),
                (0.0, 0.0, 0.0, 0.0), (-7, 263, 642, 102),
            ),
        )
        self.assertEqual(len(self.result.evaluation_records), 2)
        for record, target in zip(self.result.evaluation_records, expected):
            self.assertEqual(record.seed, target[0])
            self.assertEqual(record.initial_transition_count, target[1])
            self.assertEqual(record.initial_project_decision_count, target[2])
            self.assertEqual(record.initial_cumulative_rewards, target[3])
            self.assertEqual(record.initial_final_rewards, target[4])
            self.assertEqual(record.initial_final_scores, target[5])
            self.assertEqual(record.initial_final_round_index, 8)
            self.assertEqual(record.initial_red_pon_normalization_count, 0)
            self.assertEqual(record.final_transition_count, target[6])
            self.assertEqual(record.final_project_decision_count, target[7])
            self.assertEqual(record.final_cumulative_rewards, target[8])
            self.assertEqual(record.final_final_rewards, target[9])
            self.assertEqual(record.final_final_scores, target[10])
            self.assertEqual(record.final_final_round_index, 8)
            self.assertEqual(record.final_red_pon_normalization_count, 0)
            self.assertTrue(record.behavior_changed)
        self.assertEqual(self.result.changed_evaluation_seeds, (2, 3))
        self.assertEqual(self.result.initial_evaluation_project_raw_sum, -632.0)
        self.assertEqual(self.result.final_evaluation_project_raw_sum, -634.0)
        self.assertEqual(self.result.evaluation_project_raw_delta, -2.0)
        self.assertTrue(self.result.aggregate_negative_evaluation_observed)

    def test_all_six_traces_are_complete_legal_and_round_local(self) -> None:
        traces = tuple(item.trace for item in self.result.training_records) + tuple(
            trace
            for item in self.result.evaluation_records
            for trace in (item.initial_trace, item.final_trace)
        )
        self.assertEqual(len(traces), 6)
        for trace in traces:
            self.assertEqual(
                tuple(item.transition_index for item in trace),
                tuple(range(len(trace))),
            )
            for round_index in {item.round_index for item in trace}:
                local = tuple(
                    item.round_step_index
                    for item in trace
                    if item.round_index == round_index
                )
                self.assertEqual(local, tuple(range(len(local))))
            for item in trace:
                self.assertTrue(item.legal_actions)
                self.assertIn(item.applied_action, item.legal_actions)
                self.assertFalse(item.red_pon_normalized)
        self.assertTrue(self.result.all_actions_legal)
        self.assertTrue(self.result.all_games_terminated_without_truncation)

    def test_wraps_initialization_failure_before_any_half_game(self) -> None:
        with mock.patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError,
                "reviewed categorical MLP or pinned runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_two_half_game_sequence_smoke()

    def test_evidence_grade_and_warnings_retain_opposing_outcomes(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local two-half-game sequential raw-outcome training failure diagnostic evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "exact ordered training half-games 0 then 1 and exactly two 0.01 updates",
            "updated parameters from seed 0 feed seed 1 directly without reset",
            "disjoint greedy evaluation seeds 2 and 3 perform zero updates",
            "aggregate seat-0 evaluation raw reward changes from -632 to -634",
            "seed 2 degrades from -344 to -387 while seed 3 improves -288 to -247",
            "all opposing seed-level outcomes are retained without selection",
            "no third training half-game, replay, search, early stop or rollback",
            "not improvement, robustness, policy-quality or model-strength evidence",
            "not stable-dan, luckyj 10.68 or p9-p12 evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_two_explicit_loops_direct_continuity_and_no_io(self) -> None:
        source = inspect.getsource(smoke_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 2)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        self.assertIn("parameters = update.parameters", source)
        self.assertIn("initial_parameters", source)
        self.assertEqual(source.count("_apply_seat0_raw_outcome_update("), 1)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            ".load(",
            "pickle",
            "requests",
            "subprocess",
            "selected_parameters",
            "learning_rate_candidates",
            "early_stopping",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
