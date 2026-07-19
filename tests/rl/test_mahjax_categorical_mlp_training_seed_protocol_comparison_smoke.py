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

import mjlabai.rl.mahjax_categorical_mlp_training_seed_protocol_comparison_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_training_seed_protocol_comparison_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_PROTOCOL_COMPARISON_SMOKE_VERSION,
    MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult,
    MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError,
    run_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke,
)


class MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke()
        cls.selected, cls.contiguous = cls.result.branches

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_PROTOCOL_COMPARISON_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS",
                "MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError",
                "MahJaxCategoricalMlpTrainingSeedProtocolBranchResult",
                "MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult",
                "run_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_PROTOCOL_COMPARISON_SMOKE_VERSION,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.selected_protocol_id = "contiguous"  # type: ignore[misc]

    def test_exact_two_protocol_seed_contract_and_no_selection(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS,
            (1, 3, 5, 7, 11),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS,
            (0, 1, 2, 3, 4),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS,
            tuple(range(20, 52)),
        )
        self.assertEqual(len(self.result.branches), 2)
        self.assertIsNone(self.result.selected_protocol_id)

    def test_training_attempts_and_zero_return_noops_are_exact(self) -> None:
        self.assertEqual(self.selected.update_attempt_count, 5)
        self.assertEqual(self.selected.nonzero_update_count, 5)
        self.assertEqual(self.selected.zero_return_noop_seeds, ())
        self.assertEqual(self.contiguous.update_attempt_count, 5)
        self.assertEqual(self.contiguous.nonzero_update_count, 2)
        self.assertEqual(self.contiguous.zero_return_noop_seeds, (0, 2, 4))
        for index in (0, 2, 4):
            self.assertEqual(
                self.contiguous.training_cumulative_raw_rewards[index],
                (0.0, 0.0, 0.0, 0.0),
            )
            self.assertEqual(
                self.contiguous.per_attempt_parameter_delta_l2[index],
                (0.0, 0.0, 0.0, 0.0),
            )
            self.assertEqual(self.contiguous.initial_objectives[index], 0.0)
            self.assertEqual(self.contiguous.post_update_objectives[index], 0.0)

    def test_all_training_rows_and_trace_digests_are_pinned(self) -> None:
        self.assertEqual(
            self.selected.training_transition_counts,
            (77, 84, 83, 81, 84),
        )
        self.assertEqual(
            self.contiguous.training_transition_counts,
            (92, 77, 90, 84, 84),
        )
        self.assertEqual(
            self.selected.training_action_trace_sha256,
            (
                "9d9bc93cc2e85086797fde119070da58159ba3541d234fbcf3e833d7ac1122cf",
                "8e0216f01b24fa50991f1c028807d1fb265da714e5bc97ecb35b08ffb4a73a19",
                "6e9bfaa0785a543f23597d5747309ec49c68d190f16c7b104bb815fa63c0a9f0",
                "9f0dc1b42804ad209983a546f4d0a4a3acbd3adb3c4609c81286af54c8572c03",
                "7d0f0960b0864162ab54d7d5d0402843ab977c064ecdf78d5ae90e2e0409c6ad",
            ),
        )
        self.assertEqual(
            self.contiguous.training_action_trace_sha256,
            (
                "3915fd25d6b10919794ca0e7ff0052b53923c18a8398098ac31dd8961e5337ad",
                "9d9bc93cc2e85086797fde119070da58159ba3541d234fbcf3e833d7ac1122cf",
                "11e4029e2fd4841f40ceb22700a346a2b6357c97b068c6a7397c366aad15c961",
                "8e0216f01b24fa50991f1c028807d1fb265da714e5bc97ecb35b08ffb4a73a19",
                "a5b5ddea976ade42e831951e55feddcbf54273a4ee395ad273f728162a6e44b9",
            ),
        )
        for branch in self.result.branches:
            self.assertEqual(len(branch.training_actor_traces), 5)
            self.assertEqual(len(branch.training_action_traces), 5)
            self.assertEqual(len(branch.training_legal_action_traces), 5)
            for actions, legal_rows in zip(
                branch.training_action_traces,
                branch.training_legal_action_traces,
            ):
                self.assertEqual(len(actions), len(legal_rows))
                self.assertTrue(
                    all(action in legal for action, legal in zip(actions, legal_rows))
                )

    def test_final_parameter_deltas_and_branch_ownership_are_exact(self) -> None:
        for actual, expected in zip(
            self.selected.final_parameter_delta_l2,
            (0.0021020556, 0.0004550584, 0.0053585209, 0.0005585462),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        for actual, expected in zip(
            self.contiguous.final_parameter_delta_l2,
            (0.0010158311, 0.0001864599, 0.0025688238, 0.0002769242),
        ):
            self.assertAlmostEqual(actual, expected, places=6)
        self.assertTrue(self.result.branch_initial_parameters_identical)
        self.assertTrue(self.result.branch_final_parameters_distinct)

    def test_fixed_evaluation_pins_selection_bias_effect(self) -> None:
        self.assertEqual(self.result.initial_project_raw_sum, -501.0)
        self.assertEqual(self.selected.project_raw_sum, -650.0)
        self.assertEqual(self.contiguous.project_raw_sum, -501.0)
        self.assertEqual(
            self.selected.changed_from_initial_evaluation_seeds,
            (32, 39, 43, 44, 50),
        )
        self.assertEqual(self.contiguous.changed_from_initial_evaluation_seeds, ())
        self.assertEqual(
            self.contiguous.evaluation_project_raw_rewards,
            self.result.initial_evaluation_project_raw_rewards,
        )
        self.assertEqual((self.selected.positive_round_count, self.selected.negative_round_count), (0, 18))
        self.assertEqual((self.contiguous.positive_round_count, self.contiguous.negative_round_count), (1, 16))
        self.assertEqual(self.result.evaluation_update_count, 0)
        self.assertTrue(self.result.selection_bias_effect_observed)

    def test_safety_and_non_strength_scope_are_explicit(self) -> None:
        self.assertTrue(self.selected.all_actions_legal)
        self.assertTrue(self.contiguous.all_actions_legal)
        self.assertTrue(self.selected.all_rounds_terminated)
        self.assertTrue(self.contiguous.all_rounds_terminated)
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local training-seed outcome-selection-bias comparison evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "zero-return seeds 0, 2 and 4 are retained",
            "not protocol superiority or selection",
            "no third protocol, seed search",
            "not improvement, policy-quality, model-strength",
            "not tenhou, stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_wraps_initial_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError,
                "reviewed categorical MLP in-memory training failed",
            ):
                run_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke()

    def test_source_forbids_io_or_adaptive_protocol_selection(self) -> None:
        source = inspect.getsource(smoke_module)
        self.assertIn("MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS", source)
        self.assertIn("MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS", source)
        self.assertIn("selected_protocol_id=None", source)
        for forbidden in (
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
            "random.choice",
            "best_protocol",
            "third_protocol",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
