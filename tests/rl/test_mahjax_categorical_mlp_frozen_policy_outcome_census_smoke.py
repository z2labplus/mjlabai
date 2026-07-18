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

import mjlabai.rl.mahjax_categorical_mlp_frozen_policy_outcome_census_smoke as smoke_module  # noqa: E402
from mjlabai.rl.mahjax_categorical_mlp_frozen_policy_outcome_census_smoke import (  # noqa: E402
    MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION,
    MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult,
    MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError,
    run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke,
)


_EXPECTED_TRANSITIONS = (
    92, 77, 90, 84, 84, 83, 92, 81, 82, 86, 86, 84, 91, 90, 89, 83,
    81, 88, 85, 81, 89, 83, 83, 83, 71, 57, 82, 71, 86, 81, 83, 81,
)
_EXPECTED_REWARDS = (
    (0.0, 0.0, 0.0, 0.0),
    (-20.0, 70.0, -20.0, -30.0),
    (0.0, 0.0, 0.0, 0.0),
    (-10.0, -10.0, 20.0, -10.0),
    (0.0, 0.0, 0.0, 0.0),
    (20.0, -10.0, -10.0, -10.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, -120.0, 120.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (-10.0, 20.0, -10.0, -10.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (-26.0, 26.0, 0.0, 0.0),
    (48.0, 0.0, 0.0, -58.0),
    (-77.0, 0.0, 0.0, 67.0),
    (0.0, -120.0, 0.0, 120.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (20.0, -10.0, -10.0, -10.0),
)
_EXPECTED_SCORES = (
    (250, 250, 250, 250),
    (230, 320, 230, 220),
    (250, 250, 250, 250),
    (240, 240, 270, 240),
    (250, 250, 250, 250),
    (270, 240, 240, 240),
    (250, 250, 250, 250),
    (250, 250, 130, 370),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (240, 270, 240, 240),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (224, 276, 250, 250),
    (308, 250, 250, 192),
    (173, 250, 250, 327),
    (250, 130, 250, 370),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (250, 250, 250, 250),
    (270, 240, 240, 240),
)
_EXPECTED_DIGESTS = (
    "3915fd25d6b10919794ca0e7ff0052b53923c18a8398098ac31dd8961e5337ad",
    "9d9bc93cc2e85086797fde119070da58159ba3541d234fbcf3e833d7ac1122cf",
    "11e4029e2fd4841f40ceb22700a346a2b6357c97b068c6a7397c366aad15c961",
    "8e0216f01b24fa50991f1c028807d1fb265da714e5bc97ecb35b08ffb4a73a19",
    "a5b5ddea976ade42e831951e55feddcbf54273a4ee395ad273f728162a6e44b9",
    "6e9bfaa0785a543f23597d5747309ec49c68d190f16c7b104bb815fa63c0a9f0",
    "0fabf9165d7b6fdd1db2104452cc63b3a8e55cd21781f3235b27e9d3ce059a24",
    "9f0dc1b42804ad209983a546f4d0a4a3acbd3adb3c4609c81286af54c8572c03",
    "42c2d190e71dec38cba8168efb95c65f1b12bb2f7c8d73ae0e3d5b8b21f8bc15",
    "9c1c899d41e09c5976200274d3e571955c092b0d90fa5b55beded3830ac6b870",
    "af40389d90b708a1efd0923760bceef737ff798122289f76e615fe82e2f7380b",
    "7d0f0960b0864162ab54d7d5d0402843ab977c064ecdf78d5ae90e2e0409c6ad",
    "3352add626988bd4f29717e8d33c1b01e961dff2c68a67f4a5744c2f1ce38d71",
    "d24d4f7ae2e35c8b19aa2e8805d821256211f6b02147ced3229db2bad6d0d6c6",
    "4f0c1addd502b670e5dc2a42f391079d05c9f92301eb3a8e1f21af820f216492",
    "1164b26eb51efd8fcf6ededac5af3e8cb009db9cdf21af2c79901b0dbe59d199",
    "07b3bbd715ce25e49dd11a031a9b0467b4d9bd84c10c44776b2ceccc8772c6d3",
    "8a9123ba8fad95049b82c58f86870624b02c49bea9a8aab03c7cc1fa9b852152",
    "d6b4d577a99262f6ffc805562cae5edc50fcef84e22e07c8e8509b1ad67bb890",
    "37d2e74f1800e817412466e73b4a99340c01f62d3cac092695eb5719ef8c346a",
    "860d723cd81aa5fc4823f9c966eca0a49532d65f5cddfc0910d6ee8452ed2a4b",
    "9c6c4b23c2bf3ededbf4f69a43d12d1d3274d55e3c87802736a448daab79dd09",
    "9c2c42e2b9b16b05de92b634aaad1adad602022af6a22c15f57bcb6838ccaac7",
    "fdc23bbd8b9b142a98d327856e113a649443d1c174c595a865c7af02523a2aff",
    "f9208d16f0e45630b79277a398cf56293523140968692c74cbf1bb80e9f2a2dc",
    "f7234f0ceba1a14e73eff70f86264a7098dc469b812f0009e387d29c80e9c585",
    "0adcca681f94542ab690489c36486f869bc2de384dd818c79862c2fae14c2caa",
    "5b3b74d7b665d21a41a5800250501c7e40d0225c5994d5e04b04fefe59c6c1f2",
    "33118f2bd7f34f17a9e97bae559883c4fcefc56a28fd7f86a836784609a38b71",
    "6b433b14b8c40a083befa7abf3241dfd8e90ee356d593f8d3e29e6999f15261a",
    "bbef092da9bb95edcbc222f0f22b7108a5f33e09c041e336134831adec8492c1",
    "41186e9b2b9210501b2b779593c2e59b16a92ff1c71b83dbe72f1c47ce33906f",
)


class MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke()

    def test_exact_public_surface_and_frozen_array_free_result(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION",
                "MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS",
                "MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS",
                "MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError",
                "MahJaxCategoricalMlpFrozenPolicyOutcomeSeedResult",
                "MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult",
                "run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke",
            },
        )
        self.assertIsInstance(
            self.result,
            MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult,
        )
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION,
        )
        self.assertNotIn("parameters", {field.name for field in fields(self.result)})
        with self.assertRaises(FrozenInstanceError):
            self.result.policy_update_count = 1  # type: ignore[misc]

    def test_exact_seed_and_reference_training_contract(self) -> None:
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS,
            tuple(range(32)),
        )
        self.assertEqual(
            MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS,
            (1, 3, 5, 7, 11),
        )
        self.assertEqual(len(self.result.seed_results), 32)
        self.assertEqual(
            tuple(item.seed for item in self.result.seed_results),
            tuple(range(32)),
        )

    def test_all_per_seed_transition_reward_and_score_values_are_pinned(self) -> None:
        self.assertEqual(
            tuple(item.transition_count for item in self.result.seed_results),
            _EXPECTED_TRANSITIONS,
        )
        self.assertEqual(
            tuple(item.cumulative_raw_rewards for item in self.result.seed_results),
            _EXPECTED_REWARDS,
        )
        self.assertEqual(
            tuple(item.final_scores for item in self.result.seed_results),
            _EXPECTED_SCORES,
        )

    def test_all_action_trace_sha256_digests_are_pinned(self) -> None:
        self.assertEqual(
            tuple(item.action_trace_sha256 for item in self.result.seed_results),
            _EXPECTED_DIGESTS,
        )
        self.assertTrue(
            all(len(item.action_trace_sha256) == 64 for item in self.result.seed_results)
        )

    def test_zero_nonzero_partition_and_rates_are_exact(self) -> None:
        self.assertEqual(
            self.result.nonzero_outcome_seeds,
            (1, 3, 5, 7, 11, 24, 25, 26, 27, 31),
        )
        self.assertEqual(
            self.result.zero_outcome_seeds,
            (0, 2, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30),
        )
        self.assertEqual(self.result.nonzero_outcome_count, 10)
        self.assertEqual(self.result.zero_outcome_count, 22)
        self.assertEqual(self.result.census_nonzero_rate, 0.3125)

    def test_reference_training_selection_bias_is_explicit(self) -> None:
        self.assertEqual(self.result.reference_training_nonzero_count, 5)
        self.assertEqual(self.result.reference_training_nonzero_rate, 1.0)
        self.assertTrue(self.result.reference_training_seeds_all_nonzero)
        self.assertTrue(self.result.selection_bias_observed)
        self.assertTrue(
            set(self.result.reference_training_seeds).issubset(
                self.result.nonzero_outcome_seeds
            )
        )

    def test_policy_is_frozen_and_all_rounds_are_legal_terminal(self) -> None:
        self.assertTrue(self.result.parameters_unchanged)
        self.assertEqual(self.result.policy_update_count, 0)
        self.assertTrue(self.result.all_actions_legal)
        self.assertTrue(self.result.all_rounds_terminated)
        self.assertTrue(self.result.safety_guardrails_all_satisfied)

    def test_wraps_frozen_policy_training_failure(self) -> None:
        with patch.object(
            smoke_module,
            "_train_mahjax_categorical_mlp_parameters",
            side_effect=RuntimeError("training unavailable"),
        ):
            with self.assertRaisesRegex(
                MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError,
                "reviewed frozen categorical MLP runtime is unavailable",
            ):
                run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke()

    def test_warnings_and_source_forbid_updates_or_split_selection(self) -> None:
        self.assertEqual(
            self.result.evidence_grade,
            "P8 local frozen-policy signal-sparsity and seed-selection-bias evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "zero-outcome records remain in the denominator",
            "reference training seeds are 5 of 5 nonzero versus census 10 of 32",
            "existing training tuple is outcome-selected",
            "no replacement training or evaluation split is selected",
            "zero policy, value, critic, baseline, optimizer or gradient updates",
            "not policy-quality, model-strength, tenhou, stable-dan or luckyj evidence",
        ):
            self.assertIn(phrase, warning_text)
        source = inspect.getsource(smoke_module)
        self.assertIn("for seed in MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS", source)
        self.assertNotIn("selected_split", source)
        for forbidden in (
            "value_and_grad",
            "grad(",
            "Path(",
            "open(",
            ".save(",
            "pickle",
            "requests",
            "subprocess",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
