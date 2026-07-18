"""Census frozen all-project policy outcomes over 32 predeclared seeds.

This executable diagnostic records reward sparsity and the known training-seed
selection bias. It performs no policy/value update and selects no replacement
split or algorithm.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    _collect_all_project_round,
    _load_pinned_runtime,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS = tuple(range(32))
MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS = (1, 3, 5, 7, 11)

_EXPECTED_ROWS = (
    (0, 92, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "3915fd25d6b10919794ca0e7ff0052b53923c18a8398098ac31dd8961e5337ad"),
    (1, 77, (-20.0, 70.0, -20.0, -30.0), (230, 320, 230, 220), "9d9bc93cc2e85086797fde119070da58159ba3541d234fbcf3e833d7ac1122cf"),
    (2, 90, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "11e4029e2fd4841f40ceb22700a346a2b6357c97b068c6a7397c366aad15c961"),
    (3, 84, (-10.0, -10.0, 20.0, -10.0), (240, 240, 270, 240), "8e0216f01b24fa50991f1c028807d1fb265da714e5bc97ecb35b08ffb4a73a19"),
    (4, 84, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "a5b5ddea976ade42e831951e55feddcbf54273a4ee395ad273f728162a6e44b9"),
    (5, 83, (20.0, -10.0, -10.0, -10.0), (270, 240, 240, 240), "6e9bfaa0785a543f23597d5747309ec49c68d190f16c7b104bb815fa63c0a9f0"),
    (6, 92, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "0fabf9165d7b6fdd1db2104452cc63b3a8e55cd21781f3235b27e9d3ce059a24"),
    (7, 81, (0.0, 0.0, -120.0, 120.0), (250, 250, 130, 370), "9f0dc1b42804ad209983a546f4d0a4a3acbd3adb3c4609c81286af54c8572c03"),
    (8, 82, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "42c2d190e71dec38cba8168efb95c65f1b12bb2f7c8d73ae0e3d5b8b21f8bc15"),
    (9, 86, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "9c1c899d41e09c5976200274d3e571955c092b0d90fa5b55beded3830ac6b870"),
    (10, 86, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "af40389d90b708a1efd0923760bceef737ff798122289f76e615fe82e2f7380b"),
    (11, 84, (-10.0, 20.0, -10.0, -10.0), (240, 270, 240, 240), "7d0f0960b0864162ab54d7d5d0402843ab977c064ecdf78d5ae90e2e0409c6ad"),
    (12, 91, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "3352add626988bd4f29717e8d33c1b01e961dff2c68a67f4a5744c2f1ce38d71"),
    (13, 90, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "d24d4f7ae2e35c8b19aa2e8805d821256211f6b02147ced3229db2bad6d0d6c6"),
    (14, 89, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "4f0c1addd502b670e5dc2a42f391079d05c9f92301eb3a8e1f21af820f216492"),
    (15, 83, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "1164b26eb51efd8fcf6ededac5af3e8cb009db9cdf21af2c79901b0dbe59d199"),
    (16, 81, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "07b3bbd715ce25e49dd11a031a9b0467b4d9bd84c10c44776b2ceccc8772c6d3"),
    (17, 88, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "8a9123ba8fad95049b82c58f86870624b02c49bea9a8aab03c7cc1fa9b852152"),
    (18, 85, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "d6b4d577a99262f6ffc805562cae5edc50fcef84e22e07c8e8509b1ad67bb890"),
    (19, 81, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "37d2e74f1800e817412466e73b4a99340c01f62d3cac092695eb5719ef8c346a"),
    (20, 89, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "860d723cd81aa5fc4823f9c966eca0a49532d65f5cddfc0910d6ee8452ed2a4b"),
    (21, 83, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "9c6c4b23c2bf3ededbf4f69a43d12d1d3274d55e3c87802736a448daab79dd09"),
    (22, 83, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "9c2c42e2b9b16b05de92b634aaad1adad602022af6a22c15f57bcb6838ccaac7"),
    (23, 83, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "fdc23bbd8b9b142a98d327856e113a649443d1c174c595a865c7af02523a2aff"),
    (24, 71, (-26.0, 26.0, 0.0, 0.0), (224, 276, 250, 250), "f9208d16f0e45630b79277a398cf56293523140968692c74cbf1bb80e9f2a2dc"),
    (25, 57, (48.0, 0.0, 0.0, -58.0), (308, 250, 250, 192), "f7234f0ceba1a14e73eff70f86264a7098dc469b812f0009e387d29c80e9c585"),
    (26, 82, (-77.0, 0.0, 0.0, 67.0), (173, 250, 250, 327), "0adcca681f94542ab690489c36486f869bc2de384dd818c79862c2fae14c2caa"),
    (27, 71, (0.0, -120.0, 0.0, 120.0), (250, 130, 250, 370), "5b3b74d7b665d21a41a5800250501c7e40d0225c5994d5e04b04fefe59c6c1f2"),
    (28, 86, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "33118f2bd7f34f17a9e97bae559883c4fcefc56a28fd7f86a836784609a38b71"),
    (29, 81, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "6b433b14b8c40a083befa7abf3241dfd8e90ee356d593f8d3e29e6999f15261a"),
    (30, 83, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "bbef092da9bb95edcbc222f0f22b7108a5f33e09c041e336134831adec8492c1"),
    (31, 81, (20.0, -10.0, -10.0, -10.0), (270, 240, 240, 240), "41186e9b2b9210501b2b779593c2e59b16a92ff1c71b83dbe72f1c47ce33906f"),
)
_EXPECTED_NONZERO_SEEDS = (1, 3, 5, 7, 11, 24, 25, 26, 27, 31)
_EXPECTED_ZERO_SEEDS = (
    0,
    2,
    4,
    6,
    8,
    9,
    10,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    28,
    29,
    30,
)
_EVIDENCE_GRADE = (
    "P8 local frozen-policy signal-sparsity and seed-selection-bias evidence only"
)
_WARNINGS = (
    "frozen reviewed imitation policy census only",
    "all four seats share one frozen policy and sample only legal actions",
    "exact seeds 0 through 31 are retained once each with no exclusions",
    "zero-outcome records remain in the denominator",
    "reference training seeds are 5 of 5 nonzero versus census 10 of 32",
    "the existing training tuple is outcome-selected and not an unbiased sample",
    "no replacement training or evaluation split is selected",
    "zero policy, value, critic, baseline, optimizer or gradient updates",
    "no persistence, checkpoint, artifact, external or real data",
    "not policy-quality, model-strength, Tenhou, stable-dan or LuckyJ evidence",
)


class MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError(RuntimeError):
    """Raised when the exact frozen-policy census contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpFrozenPolicyOutcomeSeedResult:
    seed: int
    transition_count: int
    cumulative_raw_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    action_trace_sha256: str
    nonzero_outcome: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    census_seeds: Tuple[int, ...]
    reference_training_seeds: Tuple[int, ...]
    seed_results: Tuple[MahJaxCategoricalMlpFrozenPolicyOutcomeSeedResult, ...]
    nonzero_outcome_seeds: Tuple[int, ...]
    zero_outcome_seeds: Tuple[int, ...]
    nonzero_outcome_count: int
    zero_outcome_count: int
    census_nonzero_rate: float
    reference_training_nonzero_count: int
    reference_training_nonzero_rate: float
    reference_training_seeds_all_nonzero: bool
    parameters_unchanged: bool
    policy_update_count: int
    all_actions_legal: bool
    all_rounds_terminated: bool
    selection_bias_observed: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _action_trace_sha256(action_trace: Tuple[int, ...]) -> str:
    serialized = ",".join(str(action) for action in action_trace).encode("ascii")
    return hashlib.sha256(serialized).hexdigest()


def run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke(
) -> MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult:
    """Run the exact frozen-policy all-project seed census."""

    try:
        jax, jnp, parameters, _ = _train_mahjax_categorical_mlp_parameters()
        _, _, mahjax = _load_pinned_runtime()
    except Exception as exc:
        raise MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError(
            "reviewed frozen categorical MLP runtime is unavailable"
        ) from exc
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError(
            "frozen-policy census package version differs from the pinned contract"
        )

    parameter_snapshot = tuple(jnp.array(value) for value in parameters)
    trajectories = []
    for seed in MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS:
        try:
            trajectories.append(
                _collect_all_project_round(seed, parameters, jax, jnp, mahjax)
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError(
                f"frozen-policy census seed {seed} failed"
            ) from exc

    observed_rows = tuple(
        (
            seed,
            len(trajectory.action_trace),
            trajectory.cumulative_rewards,
            trajectory.final_scores,
            _action_trace_sha256(trajectory.action_trace),
        )
        for seed, trajectory in zip(
            MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS,
            trajectories,
        )
    )
    if observed_rows != _EXPECTED_ROWS:
        raise MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError(
            "frozen-policy census rows differ from the approved probe"
        )

    nonzero_seeds = tuple(
        seed
        for seed, _, rewards, _, _ in observed_rows
        if any(reward != 0.0 for reward in rewards)
    )
    zero_seeds = tuple(
        seed
        for seed, _, rewards, _, _ in observed_rows
        if all(reward == 0.0 for reward in rewards)
    )
    reference_nonzero_count = sum(
        seed in nonzero_seeds
        for seed in MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS
    )
    parameters_unchanged = all(
        bool(jnp.array_equal(before, after))
        for before, after in zip(parameter_snapshot, parameters)
    )
    if (
        nonzero_seeds != _EXPECTED_NONZERO_SEEDS
        or zero_seeds != _EXPECTED_ZERO_SEEDS
        or len(observed_rows) != 32
        or set(nonzero_seeds).intersection(zero_seeds)
        or set(nonzero_seeds).union(zero_seeds)
        != set(MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS)
        or reference_nonzero_count != 5
        or not parameters_unchanged
    ):
        raise MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError(
            "frozen-policy census selection-bias invariants were not demonstrated"
        )

    seed_results = tuple(
        MahJaxCategoricalMlpFrozenPolicyOutcomeSeedResult(
            seed=seed,
            transition_count=transition_count,
            cumulative_raw_rewards=rewards,
            final_scores=scores,
            action_trace_sha256=digest,
            nonzero_outcome=seed in nonzero_seeds,
        )
        for seed, transition_count, rewards, scores, digest in observed_rows
    )
    return MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        census_seeds=MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS,
        reference_training_seeds=(
            MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS
        ),
        seed_results=seed_results,
        nonzero_outcome_seeds=nonzero_seeds,
        zero_outcome_seeds=zero_seeds,
        nonzero_outcome_count=len(nonzero_seeds),
        zero_outcome_count=len(zero_seeds),
        census_nonzero_rate=len(nonzero_seeds) / len(observed_rows),
        reference_training_nonzero_count=reference_nonzero_count,
        reference_training_nonzero_rate=(
            reference_nonzero_count
            / len(MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS)
        ),
        reference_training_seeds_all_nonzero=True,
        parameters_unchanged=parameters_unchanged,
        policy_update_count=0,
        all_actions_legal=True,
        all_rounds_terminated=True,
        selection_bias_observed=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS",
    "MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError",
    "MahJaxCategoricalMlpFrozenPolicyOutcomeSeedResult",
    "MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult",
    "run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke",
]
