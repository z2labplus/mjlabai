from __future__ import annotations

from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_EVALUATION_SMOKE_VERSION,
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS,
    MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult,
    MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError,
    run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke,
)


class MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = (
            run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke()
        )

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_EVALUATION_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError",
                "MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult",
                "run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_EVALUATION_SMOKE_VERSION,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.selected_checkpoint_id = "candidate"  # type: ignore[misc]

    def test_exact_predeclared_disjoint_seed_contract(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS,
            tuple(range(32)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS,
            tuple(range(52, 84)),
        )
        self.assertTrue(self.result.training_evaluation_seeds_disjoint)
        self.assertEqual(self.result.update_attempt_count, 32)
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertIsNone(self.result.selected_checkpoint_id)

    def test_completed_frozen_result_is_reused_in_process(self) -> None:
        cache = (
            smoke_module._run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke_cached
        )
        before = cache.cache_info()
        reused = run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke()
        after = cache.cache_info()

        self.assertIs(reused, self.result)
        self.assertEqual(after.maxsize, 1)
        self.assertEqual(after.currsize, 1)
        self.assertEqual(after.hits, before.hits + 1)

    def test_nonzero_and_noop_attempt_partition_is_exact(self) -> None:
        self.assertEqual(self.result.nonzero_update_count, 10)
        self.assertEqual(self.result.zero_return_noop_count, 22)
        self.assertEqual(
            self.result.nonzero_update_seeds,
            (1, 3, 5, 7, 11, 17, 25, 26, 27, 31),
        )
        self.assertEqual(
            self.result.zero_return_noop_seeds,
            (0, 2, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 28, 29, 30),
        )
        for seed in self.result.zero_return_noop_seeds:
            self.assertEqual(
                self.result.training_cumulative_raw_rewards[seed],
                (0.0, 0.0, 0.0, 0.0),
            )
            self.assertEqual(
                self.result.per_attempt_parameter_delta_l2[seed],
                (0.0, 0.0, 0.0, 0.0),
            )

    def test_all_training_trajectories_are_pinned_and_legal(self) -> None:
        self.assertEqual(
            self.result.training_transition_counts,
            (92,77,90,84,84,83,92,81,83,86,86,84,91,85,89,83,81,84,85,81,89,83,83,89,83,57,82,71,86,81,83,81),
        )
        self.assertEqual(len(self.result.training_action_trace_sha256), 32)
        self.assertEqual(
            self.result.training_action_trace_sha256[17],
            "0f1e947e7e435c6494a0e5264f46e3c654c909d98f7a58cb059100e8905c34d5",
        )
        self.assertEqual(
            self.result.training_action_trace_sha256[24],
            "f5144aa96a79961dddcf8ab99f3646d26f50e4bc7e7cb29754ec11ba57c898ba",
        )
        for actions, legal_rows in zip(
            self.result.training_action_traces,
            self.result.training_legal_action_traces,
        ):
            self.assertEqual(len(actions), len(legal_rows))
            self.assertTrue(
                all(action in legal for action, legal in zip(actions, legal_rows))
            )

    def test_parameter_change_and_final_deltas_are_exact(self) -> None:
        self.assertTrue(self.result.parameters_changed)
        for actual, expected in zip(
            self.result.final_parameter_delta_l2,
            (0.0033048680, 0.0006281338, 0.0085437289, 0.0009697253),
        ):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_disjoint_evaluation_pins_behavior_change_without_reward_change(self) -> None:
        self.assertEqual(self.result.initial_project_raw_sum, -312.0)
        self.assertEqual(self.result.final_project_raw_sum, -312.0)
        self.assertEqual(
            self.result.initial_evaluation_project_raw_rewards,
            self.result.final_evaluation_project_raw_rewards,
        )
        self.assertEqual(self.result.initial_positive_round_count, 2)
        self.assertEqual(self.result.final_positive_round_count, 2)
        self.assertEqual(self.result.initial_negative_round_count, 20)
        self.assertEqual(self.result.final_negative_round_count, 20)
        self.assertEqual(self.result.changed_evaluation_seeds, (52, 65, 72))
        self.assertTrue(self.result.behavior_changed_without_reward_change)
        self.assertNotEqual(
            self.result.initial_evaluation_project_action_traces,
            self.result.final_evaluation_project_action_traces,
        )

    def test_safety_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.result.all_training_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local predeclared full-range training behavior-change evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "all zero-return records remain",
            "initial and final evaluation raw rewards are identical",
            "change without raw-reward improvement",
            "no filtering, replacement, shuffle, replay, epoch or second pass",
            "not improvement, policy-quality, model-strength",
            "not tenhou, stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_wraps_initial_training_failure(self) -> None:
        cache = (
            smoke_module._run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke_cached
        )
        before = cache.cache_info()
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke()
        after = cache.cache_info()
        self.assertEqual(after.currsize, before.currsize)
        self.assertEqual(after.misses, before.misses + 1)
        self.assertIs(
            run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke(),
            self.result,
        )

    def test_source_forbids_persistence_or_training_range_adaptation(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("tuple(range(32))", source)
        self.assertIn("tuple(range(52, 84))", source)
        self.assertIn("selected_checkpoint_id=None", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "random.shuffle",
            "random.choice",
            "replay_buffer",
            "best_checkpoint",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
