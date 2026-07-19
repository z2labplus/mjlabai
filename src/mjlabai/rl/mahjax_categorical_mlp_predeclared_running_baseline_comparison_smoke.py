"""Compare reviewed raw returns with one causal running baseline.

The baseline branch uses only per-seat outcomes from earlier attempts when it
forms the current advantage. It then updates the running mean after the policy
update. Both branches remain bounded to the reviewed in-memory seed protocol;
no parameters or selected checkpoint are returned or persisted.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
from typing import Optional, Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    _collect_all_project_round,
    _load_pinned_runtime,
)
from mjlabai.rl.mahjax_categorical_mlp_learning_rate_comparison_smoke import (
    _collect_mixed_policy_evaluation_round,
)
from mjlabai.rl.mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke import (
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS,
    MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult,
    _EXPECTED_DIGESTS as _RAW_EXPECTED_TRAINING_DIGESTS,
    _EXPECTED_TRANSITIONS as _RAW_EXPECTED_TRAINING_TRANSITIONS,
    run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _mlp_logits,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_COMPARISON_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_TRAINING_SEEDS
)
MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_CENSUS_EVALUATION_SEEDS
)

_LEARNING_RATE = 0.01
_EXPECTED_NONZERO_SEEDS = tuple(range(1, 32))
_EXPECTED_FINAL_BASELINE = (-0.0121875, -0.015625, -0.05, 0.0528125)
_EXPECTED_FINAL_DELTAS = (
    0.0035393923,
    0.0006425792,
    0.0084222732,
    0.0009679428,
)
_EXPECTED_CHANGED_EVALUATION_SEEDS = (52, 65, 72)
_EVIDENCE_GRADE = (
    "P8 local causal-running-baseline signal-densification comparison "
    "evidence only"
)
_WARNINGS = (
    "raw versus one causal per-seat running-mean baseline comparison only",
    "exact ordered training seeds 0 through 31 and learning rate 0.01",
    "current advantages use prior records only and update the baseline afterward",
    "raw nonzero updates are 10 of 32 while baseline updates are 31 of 32",
    "denser update signal does not improve the fixed evaluation reward vector",
    "evaluation seeds 52 through 83 are disjoint and perform zero updates",
    "raw and baseline evaluation sums remain -312 with counts 2 positive and 20 negative",
    "no third estimator, critic, replay, epoch, selection, persistence or artifact",
    "no external or real data, production self-play, evaluation or league",
    "not improvement, policy-quality, model-strength or promotion evidence",
    "not Tenhou, stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError(
    RuntimeError
):
    """Raised when the exact causal-baseline comparison contract fails."""


@dataclass(frozen=True)
class _CausalBaselineUpdate:
    parameters: object
    baseline_before: Tuple[float, ...]
    advantage_seat_returns: Tuple[float, ...]
    baseline_after: Tuple[float, ...]
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]


@dataclass(frozen=True)
class MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    learning_rate: float
    training_seeds: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    raw_reference: MahJaxCategoricalMlpPredeclaredCensusTrainingEvaluationResult
    baseline_update_attempt_count: int
    raw_nonzero_update_count: int
    baseline_nonzero_update_count: int
    baseline_noop_seeds: Tuple[int, ...]
    baseline_nonzero_update_seeds: Tuple[int, ...]
    training_transition_counts: Tuple[int, ...]
    training_actor_traces: Tuple[Tuple[int, ...], ...]
    training_action_traces: Tuple[Tuple[int, ...], ...]
    training_legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    training_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    training_final_scores: Tuple[Tuple[int, ...], ...]
    training_action_trace_sha256: Tuple[str, ...]
    baseline_before_per_attempt: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns_per_attempt: Tuple[Tuple[float, ...], ...]
    baseline_after_per_attempt: Tuple[Tuple[float, ...], ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_attempt_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    final_running_baseline: Tuple[float, ...]
    final_parameter_delta_l2: Tuple[float, ...]
    evaluation_transition_counts: Tuple[int, ...]
    evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    evaluation_project_raw_rewards: Tuple[float, ...]
    evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    evaluation_project_raw_sum: float
    evaluation_positive_round_count: int
    evaluation_negative_round_count: int
    changed_from_initial_evaluation_seeds: Tuple[int, ...]
    changed_from_raw_evaluation_seeds: Tuple[int, ...]
    baseline_reward_vector_matches_raw: bool
    baseline_reward_counts_match_raw: bool
    signal_densified_without_reward_improvement: bool
    training_evaluation_seeds_disjoint: bool
    evaluation_update_count: int
    selected_estimator_id: Optional[str]
    selected_checkpoint_id: Optional[str]
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _trace_sha256(trace: Tuple[int, ...]) -> str:
    return hashlib.sha256(",".join(map(str, trace)).encode("ascii")).hexdigest()


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _apply_causal_running_baseline_update(
    parameters,
    trajectory,
    baseline_before,
    completed_attempt_count,
    jax,
    jnp,
):
    seat_returns = jnp.asarray(
        trajectory.cumulative_rewards,
        dtype=jnp.float32,
    ) / 100.0
    prior_baseline = jnp.asarray(baseline_before, dtype=jnp.float32)
    advantages = seat_returns - prior_baseline
    decision_advantages = advantages[trajectory.actors]

    def objective(model_parameters):
        logits = _mlp_logits(model_parameters, trajectory.features, jax)
        legal_logits = jnp.where(trajectory.legal_masks, logits, -1e9)
        log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
        selected_log_probabilities = log_probabilities[
            jnp.arange(trajectory.actions.shape[0]),
            trajectory.actions,
        ]
        return -jnp.mean(decision_advantages * selected_log_probabilities)

    initial_objective, gradients = jax.jit(jax.value_and_grad(objective))(
        parameters
    )
    updated_parameters = jax.block_until_ready(
        tuple(
            value - _LEARNING_RATE * gradient
            for value, gradient in zip(parameters, gradients)
        )
    )
    next_count = completed_attempt_count + 1
    normalized_returns = tuple(
        float(value) / 100.0 for value in trajectory.cumulative_rewards
    )
    baseline_after = tuple(
        (
            completed_attempt_count * float(baseline_before[index])
            + normalized_returns[index]
        )
        / next_count
        for index in range(4)
    )
    return _CausalBaselineUpdate(
        parameters=updated_parameters,
        baseline_before=tuple(float(value) for value in baseline_before),
        advantage_seat_returns=tuple(float(value) for value in advantages),
        baseline_after=baseline_after,
        initial_objective=float(initial_objective),
        post_update_objective=float(objective(updated_parameters)),
        parameter_delta_l2=tuple(
            float(jnp.linalg.norm(updated - initial))
            for initial, updated in zip(parameters, updated_parameters)
        ),
    )


def run_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke(
) -> MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult:
    """Run the exact reviewed raw reference and causal-baseline branch."""

    try:
        raw_reference = (
            run_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke()
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError(
            "reviewed raw full-range reference failed"
        ) from exc
    try:
        jax, jnp, initial_parameters, _ = _train_mahjax_categorical_mlp_parameters()
        _, _, mahjax = _load_pinned_runtime()
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
        raise MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError(
            "pinned causal-baseline runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError(
            "causal-baseline runtime differs from the pinned contract"
        )

    parameters = tuple(initial_parameters)
    running_baseline = (0.0, 0.0, 0.0, 0.0)
    trajectories = []
    updates = []
    nonzero_seeds = []
    noop_seeds = []
    for attempt_index, seed in enumerate(
        MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS
    ):
        trajectory = _collect_all_project_round(
            seed,
            parameters,
            jax,
            jnp,
            mahjax,
        )
        update = _apply_causal_running_baseline_update(
            parameters,
            trajectory,
            running_baseline,
            attempt_index,
            jax,
            jnp,
        )
        changed = any(value > 0.0 for value in update.parameter_delta_l2)
        if changed:
            nonzero_seeds.append(seed)
        else:
            noop_seeds.append(seed)
        trajectories.append(trajectory)
        updates.append(update)
        parameters = update.parameters
        running_baseline = update.baseline_after

    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if (
        tuple(noop_seeds) != (0,)
        or tuple(nonzero_seeds) != _EXPECTED_NONZERO_SEEDS
        or tuple(len(item.action_trace) for item in trajectories)
        != _RAW_EXPECTED_TRAINING_TRANSITIONS
        or tuple(_trace_sha256(item.action_trace) for item in trajectories)
        != _RAW_EXPECTED_TRAINING_DIGESTS
        or not all(
            _close(actual, expected)
            for actual, expected in zip(running_baseline, _EXPECTED_FINAL_BASELINE)
        )
        or not all(
            _close(actual, expected)
            for actual, expected in zip(final_deltas, _EXPECTED_FINAL_DELTAS)
        )
    ):
        raise MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError(
            "causal-baseline training summary differs from the approved probe"
        )

    evaluation = tuple(
        _collect_mixed_policy_evaluation_round(
            seed,
            parameters,
            environment,
            step_fn,
            rule_policy_fn,
            jax,
            jnp,
        )
        for seed in MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS
    )
    evaluation_rewards = tuple(
        item.project_cumulative_raw_reward for item in evaluation
    )
    changed_seeds = tuple(
        seed
        for seed, transition_count, action_trace, reward, scores, item in zip(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS,
            raw_reference.initial_evaluation_transition_counts,
            raw_reference.initial_evaluation_project_action_traces,
            raw_reference.initial_evaluation_project_raw_rewards,
            raw_reference.initial_evaluation_final_scores,
            evaluation,
        )
        if (
            transition_count != item.transition_count
            or action_trace != item.project_action_trace
            or reward != item.project_cumulative_raw_reward
            or scores != item.final_scores
        )
    )
    changed_from_raw = tuple(
        seed
        for seed, transition_count, action_trace, reward, scores, item in zip(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS,
            raw_reference.final_evaluation_transition_counts,
            raw_reference.final_evaluation_project_action_traces,
            raw_reference.final_evaluation_project_raw_rewards,
            raw_reference.final_evaluation_final_scores,
            evaluation,
        )
        if (
            transition_count != item.transition_count
            or action_trace != item.project_action_trace
            or reward != item.project_cumulative_raw_reward
            or scores != item.final_scores
        )
    )
    rewards_match = (
        evaluation_rewards
        == raw_reference.final_evaluation_project_raw_rewards
        == raw_reference.initial_evaluation_project_raw_rewards
    )
    positive_count = sum(value > 0.0 for value in evaluation_rewards)
    negative_count = sum(value < 0.0 for value in evaluation_rewards)
    counts_match = (
        positive_count == raw_reference.final_positive_round_count == 2
        and negative_count == raw_reference.final_negative_round_count == 20
    )
    disjoint = not set(
        MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS
    ).intersection(
        MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS
    )
    if (
        not rewards_match
        or sum(evaluation_rewards) != -312.0
        or not counts_match
        or changed_seeds != _EXPECTED_CHANGED_EVALUATION_SEEDS
        or changed_from_raw != (65,)
        or not disjoint
    ):
        raise MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError(
            "causal-baseline evaluation differs from the approved probe"
        )

    return MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_COMPARISON_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        learning_rate=_LEARNING_RATE,
        training_seeds=(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS
        ),
        evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS
        ),
        raw_reference=raw_reference,
        baseline_update_attempt_count=len(updates),
        raw_nonzero_update_count=raw_reference.nonzero_update_count,
        baseline_nonzero_update_count=len(nonzero_seeds),
        baseline_noop_seeds=tuple(noop_seeds),
        baseline_nonzero_update_seeds=tuple(nonzero_seeds),
        training_transition_counts=tuple(len(item.action_trace) for item in trajectories),
        training_actor_traces=tuple(item.actor_trace for item in trajectories),
        training_action_traces=tuple(item.action_trace for item in trajectories),
        training_legal_action_traces=tuple(
            item.legal_action_trace for item in trajectories
        ),
        training_cumulative_raw_rewards=tuple(
            item.cumulative_rewards for item in trajectories
        ),
        training_final_scores=tuple(item.final_scores for item in trajectories),
        training_action_trace_sha256=tuple(
            _trace_sha256(item.action_trace) for item in trajectories
        ),
        baseline_before_per_attempt=tuple(item.baseline_before for item in updates),
        advantage_seat_returns_per_attempt=tuple(
            item.advantage_seat_returns for item in updates
        ),
        baseline_after_per_attempt=tuple(item.baseline_after for item in updates),
        initial_objectives=tuple(item.initial_objective for item in updates),
        post_update_objectives=tuple(item.post_update_objective for item in updates),
        per_attempt_parameter_delta_l2=tuple(
            item.parameter_delta_l2 for item in updates
        ),
        final_running_baseline=running_baseline,
        final_parameter_delta_l2=final_deltas,
        evaluation_transition_counts=tuple(item.transition_count for item in evaluation),
        evaluation_project_action_traces=tuple(
            item.project_action_trace for item in evaluation
        ),
        evaluation_project_raw_rewards=evaluation_rewards,
        evaluation_final_scores=tuple(item.final_scores for item in evaluation),
        evaluation_project_raw_sum=sum(evaluation_rewards),
        evaluation_positive_round_count=positive_count,
        evaluation_negative_round_count=negative_count,
        changed_from_initial_evaluation_seeds=changed_seeds,
        changed_from_raw_evaluation_seeds=changed_from_raw,
        baseline_reward_vector_matches_raw=rewards_match,
        baseline_reward_counts_match_raw=counts_match,
        signal_densified_without_reward_improvement=True,
        training_evaluation_seeds_disjoint=disjoint,
        evaluation_update_count=0,
        selected_estimator_id=None,
        selected_checkpoint_id=None,
        all_training_actions_legal=True,
        all_rounds_terminated=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_COMPARISON_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonSmokeError",
    "MahJaxCategoricalMlpPredeclaredRunningBaselineComparisonResult",
    "run_mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke",
]
