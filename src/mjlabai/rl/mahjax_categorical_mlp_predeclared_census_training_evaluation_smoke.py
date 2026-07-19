"""Train once over a predeclared seed census and evaluate disjoint seeds.

Every seed from 0 through 31 is retained in order, including zero-return no-op
attempts. Initial and final parameters are evaluated without updates on seeds
52 through 83. No checkpoint is selected or persisted.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import hashlib
import math
from typing import Optional, Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    _apply_actor_indexed_raw_outcome_update,
    _collect_all_project_round,
    _load_pinned_runtime,
)
from mjlabai.rl.mahjax_categorical_mlp_learning_rate_comparison_smoke import (
    _collect_mixed_policy_evaluation_round,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_EVALUATION_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS = tuple(range(32))
MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS = tuple(range(52, 84))

_EXPECTED_TRANSITIONS = (
    92, 77, 90, 84, 84, 83, 92, 81, 83, 86, 86, 84, 91, 85, 89, 83,
    81, 84, 85, 81, 89, 83, 83, 89, 83, 57, 82, 71, 86, 81, 83, 81,
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
    "9edb3c167edbd3f13c0e13016bc2acf0fa72ecaa18d4f7b4fbbe66610a5a9f8c",
    "9c1c899d41e09c5976200274d3e571955c092b0d90fa5b55beded3830ac6b870",
    "af40389d90b708a1efd0923760bceef737ff798122289f76e615fe82e2f7380b",
    "7d0f0960b0864162ab54d7d5d0402843ab977c064ecdf78d5ae90e2e0409c6ad",
    "3352add626988bd4f29717e8d33c1b01e961dff2c68a67f4a5744c2f1ce38d71",
    "8745a07661c6fa40c77aa01a373d07b3810e6e5ce8003ef2feafd5f2bc3546d5",
    "4f0c1addd502b670e5dc2a42f391079d05c9f92301eb3a8e1f21af820f216492",
    "1164b26eb51efd8fcf6ededac5af3e8cb009db9cdf21af2c79901b0dbe59d199",
    "07b3bbd715ce25e49dd11a031a9b0467b4d9bd84c10c44776b2ceccc8772c6d3",
    "0f1e947e7e435c6494a0e5264f46e3c654c909d98f7a58cb059100e8905c34d5",
    "d6b4d577a99262f6ffc805562cae5edc50fcef84e22e07c8e8509b1ad67bb890",
    "9cc6932b9fdfd1225ce847a5e794b3af0c8889a45dd43b849933b14c97797c78",
    "860d723cd81aa5fc4823f9c966eca0a49532d65f5cddfc0910d6ee8452ed2a4b",
    "9c6c4b23c2bf3ededbf4f69a43d12d1d3274d55e3c87802736a448daab79dd09",
    "9c2c42e2b9b16b05de92b634aaad1adad602022af6a22c15f57bcb6838ccaac7",
    "11f8d05b4634f3bed5903519ea210f9adabdf784a1cc10a72ba95197ce1ce91f",
    "f5144aa96a79961dddcf8ab99f3646d26f50e4bc7e7cb29754ec11ba57c898ba",
    "f7234f0ceba1a14e73eff70f86264a7098dc469b812f0009e387d29c80e9c585",
    "0adcca681f94542ab690489c36486f869bc2de384dd818c79862c2fae14c2caa",
    "5b3b74d7b665d21a41a5800250501c7e40d0225c5994d5e04b04fefe59c6c1f2",
    "33118f2bd7f34f17a9e97bae559883c4fcefc56a28fd7f86a836784609a38b71",
    "6b433b14b8c40a083befa7abf3241dfd8e90ee356d593f8d3e29e6999f15261a",
    "bbef092da9bb95edcbc222f0f22b7108a5f33e09c041e336134831adec8492c1",
    "41186e9b2b9210501b2b779593c2e59b16a92ff1c71b83dbe72f1c47ce33906f",
)
_EXPECTED_NONZERO = (1, 3, 5, 7, 11, 17, 25, 26, 27, 31)
_EXPECTED_ZERO = (
    0, 2, 4, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22,
    23, 24, 28, 29, 30,
)
_NONZERO_REWARDS = {
    1: (-20.0, 70.0, -20.0, -30.0),
    3: (-10.0, -10.0, 20.0, -10.0),
    5: (20.0, -10.0, -10.0, -10.0),
    7: (0.0, 0.0, -120.0, 120.0),
    11: (-10.0, 20.0, -10.0, -10.0),
    17: (-10.0, 10.0, -10.0, -10.0),
    25: (48.0, 0.0, 0.0, -58.0),
    26: (-77.0, 0.0, 0.0, 67.0),
    27: (0.0, -120.0, 0.0, 120.0),
    31: (20.0, -10.0, -10.0, -10.0),
}
_NONZERO_SCORES = {
    1: (230, 320, 230, 220),
    3: (240, 240, 270, 240),
    5: (270, 240, 240, 240),
    7: (250, 250, 130, 370),
    11: (240, 270, 240, 240),
    17: (240, 270, 240, 240),
    25: (308, 250, 250, 192),
    26: (173, 250, 250, 327),
    27: (250, 130, 250, 370),
    31: (270, 240, 240, 240),
}
_NONZERO_UPDATES = {
    1: (0.0936663598, 0.0930117071, (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356)),
    3: (-0.0553588867, -0.0554395691, (0.0002636357, 0.0000601950, 0.0008506179, 0.0000944084)),
    5: (-0.0609763190, -0.0609965809, (0.0002007297, 0.0000233677, 0.0003997849, 0.0000430078)),
    7: (-0.0202308446, -0.0218939111, (0.0016294104, 0.0002862717, 0.0037121067, 0.0003829675)),
    11: (-0.0131035689, -0.0133588845, (0.0004151060, 0.0001173344, 0.0015263907, 0.0001777170)),
    17: (-0.0656873733, -0.0657203421, (0.0002210556, 0.0000418098, 0.0005244048, 0.0000630238)),
    25: (-0.1018431187, -0.1028154343, (0.0010455290, 0.0002143072, 0.0029083926, 0.0003175597)),
    26: (0.0095330151, 0.0083843637, (0.0013441463, 0.0003039865, 0.0030778204, 0.0003591960)),
    27: (-0.1625065506, -0.1646067649, (0.0019092270, 0.0003044539, 0.0041187736, 0.0004838501)),
    31: (-0.0256492477, -0.0257271845, (0.0003255363, 0.0000522496, 0.0008141054, 0.0000850710)),
}
_EXPECTED_FINAL_DELTAS = (
    0.0033048680,
    0.0006281338,
    0.0085437289,
    0.0009697253,
)
_EXPECTED_EVALUATION_REWARDS = (
    -13.0, 0.0, 0.0, -5.0, -5.0, -52.0, -15.0, 70.0,
    0.0, -39.0, 0.0, 0.0, -13.0, -15.0, -30.0, 0.0,
    0.0, -26.0, -20.0, -10.0, -20.0, 80.0, -39.0, 0.0,
    -80.0, 0.0, -20.0, -10.0, 0.0, -10.0, -10.0, -30.0,
)
_EVIDENCE_GRADE = (
    "P8 local predeclared full-range training behavior-change evidence only"
)
_WARNINGS = (
    "one ordered predeclared 0 through 31 training pass only",
    "all zero-return records remain as no-op update attempts",
    "evaluation seeds 52 through 83 are disjoint and perform zero updates",
    "initial and final evaluation raw rewards are identical at sum -312",
    "evaluation records 52, 65 and 72 change without raw-reward improvement",
    "sequential nonzero outcomes differ from the frozen-policy census",
    "no filtering, replacement, shuffle, replay, epoch or second pass",
    "no selected checkpoint, persistence, artifact, external or real data",
    "not improvement, policy-quality, model-strength or promotion evidence",
    "not Tenhou, stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
    RuntimeError
):
    """Raised when the exact full-range diagnostic contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    training_seeds: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    update_attempt_count: int
    nonzero_update_count: int
    zero_return_noop_count: int
    nonzero_update_seeds: Tuple[int, ...]
    zero_return_noop_seeds: Tuple[int, ...]
    training_transition_counts: Tuple[int, ...]
    training_actor_traces: Tuple[Tuple[int, ...], ...]
    training_action_traces: Tuple[Tuple[int, ...], ...]
    training_legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    training_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    training_final_scores: Tuple[Tuple[int, ...], ...]
    training_action_trace_sha256: Tuple[str, ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_attempt_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    final_parameter_delta_l2: Tuple[float, ...]
    initial_evaluation_transition_counts: Tuple[int, ...]
    final_evaluation_transition_counts: Tuple[int, ...]
    initial_evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    final_evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    initial_evaluation_project_raw_rewards: Tuple[float, ...]
    final_evaluation_project_raw_rewards: Tuple[float, ...]
    initial_evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    final_evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    initial_project_raw_sum: float
    final_project_raw_sum: float
    initial_positive_round_count: int
    final_positive_round_count: int
    initial_negative_round_count: int
    final_negative_round_count: int
    changed_evaluation_seeds: Tuple[int, ...]
    training_evaluation_seeds_disjoint: bool
    parameters_changed: bool
    evaluation_update_count: int
    selected_checkpoint_id: Optional[str]
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    behavior_changed_without_reward_change: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _trace_sha256(trace: Tuple[int, ...]) -> str:
    return hashlib.sha256(",".join(map(str, trace)).encode("ascii")).hexdigest()


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _evaluate(
    parameters,
    environment,
    step_fn,
    rule_policy_fn,
    jax,
    jnp,
    collect_evaluation_round_fn,
):
    return tuple(
        collect_evaluation_round_fn(
            seed,
            parameters,
            environment,
            step_fn,
            rule_policy_fn,
            jax,
            jnp,
        )
        for seed in MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS
    )


@lru_cache(maxsize=1)
def _run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke_cached(
    train_parameters_fn,
    load_runtime_fn,
    collect_training_round_fn,
    collect_evaluation_round_fn,
) -> MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult:
    """Compute and retain one immutable result for exact dependency identities."""

    try:
        jax, jnp, initial_parameters, _ = train_parameters_fn()
    except Exception as exc:
        raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
            "reviewed categorical MLP in-memory training failed"
        ) from exc
    try:
        _, _, mahjax = load_runtime_fn()
        from mahjax.red_mahjong.players import rule_based_player

        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        step_fn = jax.jit(environment.step)
        rule_policy_fn = jax.jit(rule_based_player)
    except Exception as exc:
        raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
            "pinned MahJax/JAX full-range runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
            "full-range runtime differs from the pinned contract"
        )

    initial_evaluation = _evaluate(
        initial_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        collect_evaluation_round_fn,
    )
    initial_rewards = tuple(
        item.project_cumulative_raw_reward for item in initial_evaluation
    )
    if initial_rewards != _EXPECTED_EVALUATION_REWARDS or sum(initial_rewards) != -312.0:
        raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
            "initial disjoint evaluation differs from the approved probe"
        )

    parameters = tuple(initial_parameters)
    trajectories = []
    updates = []
    nonzero_seeds = []
    zero_seeds = []
    for seed in MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS:
        trajectory = collect_training_round_fn(seed, parameters, jax, jnp, mahjax)
        before = tuple(parameters)
        update = _apply_actor_indexed_raw_outcome_update(
            parameters,
            trajectory,
            jax,
            jnp,
        )
        zero_return = all(value == 0.0 for value in trajectory.cumulative_rewards)
        unchanged = all(
            bool(jnp.array_equal(left, right))
            for left, right in zip(before, update.parameters)
        )
        if zero_return:
            zero_seeds.append(seed)
            if not unchanged or any(value != 0.0 for value in update.parameter_delta_l2):
                raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
                    f"zero-return seed {seed} was not an exact no-op"
                )
        else:
            nonzero_seeds.append(seed)

        expected_rewards = _NONZERO_REWARDS.get(seed, (0.0, 0.0, 0.0, 0.0))
        expected_scores = _NONZERO_SCORES.get(seed, (250, 250, 250, 250))
        expected_update = _NONZERO_UPDATES.get(
            seed,
            (0.0, 0.0, (0.0, 0.0, 0.0, 0.0)),
        )
        if (
            len(trajectory.action_trace) != _EXPECTED_TRANSITIONS[seed]
            or trajectory.cumulative_rewards != expected_rewards
            or trajectory.final_scores != expected_scores
            or _trace_sha256(trajectory.action_trace) != _EXPECTED_DIGESTS[seed]
            or not _close(update.initial_objective, expected_update[0])
            or not _close(update.post_update_objective, expected_update[1])
            or not all(
                _close(actual, expected)
                for actual, expected in zip(
                    update.parameter_delta_l2,
                    expected_update[2],
                )
            )
        ):
            raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
                f"training seed {seed} differs from the approved probe"
            )
        trajectories.append(trajectory)
        updates.append(update)
        parameters = update.parameters

    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if (
        tuple(nonzero_seeds) != _EXPECTED_NONZERO
        or tuple(zero_seeds) != _EXPECTED_ZERO
        or not all(
            _close(actual, expected)
            for actual, expected in zip(final_deltas, _EXPECTED_FINAL_DELTAS)
        )
    ):
        raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
            "full-range update summary differs from the approved probe"
        )

    final_evaluation = _evaluate(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        collect_evaluation_round_fn,
    )
    final_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_evaluation
    )
    changed_seeds = tuple(
        seed
        for seed, before, after in zip(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS,
            initial_evaluation,
            final_evaluation,
        )
        if before != after
    )
    disjoint = not set(
        MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS
    ).intersection(MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS)
    parameters_changed = any(value > 0.0 for value in final_deltas)
    if (
        final_rewards != _EXPECTED_EVALUATION_REWARDS
        or changed_seeds != (52, 65, 72)
        or not disjoint
        or not parameters_changed
    ):
        raise MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError(
            "final disjoint evaluation differs from the approved probe"
        )

    return MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_EVALUATION_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        training_seeds=MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS,
        evaluation_seeds=MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS,
        update_attempt_count=len(updates),
        nonzero_update_count=len(nonzero_seeds),
        zero_return_noop_count=len(zero_seeds),
        nonzero_update_seeds=tuple(nonzero_seeds),
        zero_return_noop_seeds=tuple(zero_seeds),
        training_transition_counts=tuple(len(item.action_trace) for item in trajectories),
        training_actor_traces=tuple(item.actor_trace for item in trajectories),
        training_action_traces=tuple(item.action_trace for item in trajectories),
        training_legal_action_traces=tuple(item.legal_action_trace for item in trajectories),
        training_cumulative_raw_rewards=tuple(item.cumulative_rewards for item in trajectories),
        training_final_scores=tuple(item.final_scores for item in trajectories),
        training_action_trace_sha256=tuple(_trace_sha256(item.action_trace) for item in trajectories),
        initial_objectives=tuple(item.initial_objective for item in updates),
        post_update_objectives=tuple(item.post_update_objective for item in updates),
        per_attempt_parameter_delta_l2=tuple(item.parameter_delta_l2 for item in updates),
        final_parameter_delta_l2=final_deltas,
        initial_evaluation_transition_counts=tuple(item.transition_count for item in initial_evaluation),
        final_evaluation_transition_counts=tuple(item.transition_count for item in final_evaluation),
        initial_evaluation_project_action_traces=tuple(item.project_action_trace for item in initial_evaluation),
        final_evaluation_project_action_traces=tuple(item.project_action_trace for item in final_evaluation),
        initial_evaluation_project_raw_rewards=initial_rewards,
        final_evaluation_project_raw_rewards=final_rewards,
        initial_evaluation_final_scores=tuple(item.final_scores for item in initial_evaluation),
        final_evaluation_final_scores=tuple(item.final_scores for item in final_evaluation),
        initial_project_raw_sum=sum(initial_rewards),
        final_project_raw_sum=sum(final_rewards),
        initial_positive_round_count=sum(value > 0.0 for value in initial_rewards),
        final_positive_round_count=sum(value > 0.0 for value in final_rewards),
        initial_negative_round_count=sum(value < 0.0 for value in initial_rewards),
        final_negative_round_count=sum(value < 0.0 for value in final_rewards),
        changed_evaluation_seeds=changed_seeds,
        training_evaluation_seeds_disjoint=disjoint,
        parameters_changed=parameters_changed,
        evaluation_update_count=0,
        selected_checkpoint_id=None,
        all_training_actions_legal=True,
        all_rounds_terminated=True,
        behavior_changed_without_reward_change=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


def run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke(
) -> MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult:
    """Run once per exact dependency set and reuse the frozen result in-process."""

    return _run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke_cached(
        _train_mahjax_categorical_mlp_parameters,
        _load_pinned_runtime,
        _collect_all_project_round,
        _collect_mixed_policy_evaluation_round,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_EVALUATION_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationSmokeError",
    "MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult",
    "run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke",
]
