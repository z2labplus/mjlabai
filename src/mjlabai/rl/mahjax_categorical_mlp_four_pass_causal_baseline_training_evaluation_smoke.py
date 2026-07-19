"""Run four exact causal-baseline MahJax training passes.

The policy and prior-record per-seat baseline remain continuous across four
ordered passes over seeds 0 through 31. Evaluation occurs only before training
and after all 128 attempts on disjoint seeds 52 through 83. No intermediate
selection, checkpoint, or parameter artifact exists.
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
    _EXPECTED_EVALUATION_REWARDS as _EXPECTED_INITIAL_EVALUATION_REWARDS,
)
from mjlabai.rl.mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke import (
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS,
    _apply_causal_running_baseline_update,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_EVALUATION_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_TRAINING_SEEDS
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_PREDECLARED_RUNNING_BASELINE_EVALUATION_SEEDS
)

_PASS_COUNT = 4
_LEARNING_RATE = 0.01
_EXPECTED_PER_PASS_NONZERO_UPDATE_COUNTS = (31, 32, 32, 32)
_EXPECTED_PER_PASS_NONZERO_OUTCOME_COUNTS = (10, 10, 10, 11)
_EXPECTED_PASS_ENDING_BASELINES = (
    (-0.0121875, -0.015625, -0.05, 0.0528125),
    (0.000625, -0.02734375, -0.05859375, 0.0571875),
    (0.0054166667, -0.0296875, -0.0630208333, 0.0591666667),
    (0.00625, -0.040390625, -0.054140625, 0.0609375),
)
_EXPECTED_FINAL_DELTAS = (
    0.0119271539,
    0.0016169089,
    0.0243039839,
    0.0027456258,
)
_EXPECTED_FINAL_EVALUATION_REWARDS = (
    -13.0, 0.0, 0.0, -5.0, -5.0, -52.0, 0.0, 70.0,
    0.0, -39.0, 0.0, 0.0, -13.0, -15.0, -30.0, 0.0,
    0.0, -26.0, -20.0, -10.0, -20.0, 80.0, -39.0, 0.0,
    -80.0, 0.0, -20.0, -10.0, 0.0, -10.0, -10.0, -30.0,
)
_EXPECTED_CHANGED_EVALUATION_SEEDS = (52, 58, 65, 70, 72)
_EVIDENCE_GRADE = (
    "P8 local exact four-pass causal-baseline deterministic improvement "
    "diagnostic evidence only"
)
_WARNINGS = (
    "exact four-pass causal per-seat running-baseline training diagnostic only",
    "each pass uses ordered seeds 0 through 31 for exactly 128 attempts",
    "policy parameters and prior-record baseline remain continuous across passes",
    "evaluation occurs only before training and after all four passes",
    "disjoint evaluation sum changes from -312 to -297",
    "negative rounds change from 20 to 19; positive rounds remain 2",
    "one bounded deterministic diagnostic is not robust improvement",
    "no fifth pass, alternate count, early stop, tuning or checkpoint selection",
    "no critic, GAE, entropy, KL, clipping, optimizer or rate change",
    "no replay buffer, persistence, artifact, external or real data",
    "not policy-quality, model-strength, stable-dan or promotion evidence",
    "not Tenhou or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError(
    RuntimeError
):
    """Raised when the exact four-pass diagnostic contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    pass_count: int
    learning_rate: float
    training_seeds_per_pass: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    update_attempt_count: int
    per_pass_nonzero_update_counts: Tuple[int, ...]
    per_pass_nonzero_raw_outcome_counts: Tuple[int, ...]
    per_pass_transition_counts: Tuple[Tuple[int, ...], ...]
    per_pass_actor_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_legal_action_traces: Tuple[
        Tuple[Tuple[Tuple[int, ...], ...], ...], ...
    ]
    per_pass_cumulative_raw_rewards: Tuple[Tuple[Tuple[float, ...], ...], ...]
    per_pass_final_scores: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_action_trace_sha256: Tuple[Tuple[str, ...], ...]
    baseline_before_per_attempt: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns_per_attempt: Tuple[Tuple[float, ...], ...]
    baseline_after_per_attempt: Tuple[Tuple[float, ...], ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_attempt_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    pass_ending_baselines: Tuple[Tuple[float, ...], ...]
    final_running_baseline: Tuple[float, ...]
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
    project_raw_sum_delta: float
    initial_positive_round_count: int
    final_positive_round_count: int
    initial_negative_round_count: int
    final_negative_round_count: int
    changed_evaluation_seeds: Tuple[int, ...]
    training_evaluation_seeds_disjoint: bool
    evaluation_call_count: int
    evaluation_update_count: int
    parameters_changed: bool
    bounded_diagnostic_improved: bool
    selected_pass_index: Optional[int]
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


def _evaluate(parameters, environment, step_fn, rule_policy_fn, jax, jnp):
    return tuple(
        _collect_mixed_policy_evaluation_round(
            seed,
            parameters,
            environment,
            step_fn,
            rule_policy_fn,
            jax,
            jnp,
        )
        for seed in MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS
    )


def run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke(
) -> MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult:
    """Run exactly four passes and one disjoint before/after evaluation."""

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
        raise MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError(
            "pinned four-pass causal-baseline runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError(
            "four-pass runtime differs from the pinned contract"
        )

    initial_evaluation = _evaluate(
        initial_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
    )
    initial_rewards = tuple(
        item.project_cumulative_raw_reward for item in initial_evaluation
    )
    if initial_rewards != _EXPECTED_INITIAL_EVALUATION_REWARDS:
        raise MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError(
            "initial evaluation differs from the approved probe"
        )

    parameters = tuple(initial_parameters)
    running_baseline = (0.0, 0.0, 0.0, 0.0)
    completed_attempt_count = 0
    all_pass_trajectories = []
    all_updates = []
    per_pass_nonzero_updates = []
    per_pass_nonzero_outcomes = []
    pass_ending_baselines = []
    for _pass_index in range(_PASS_COUNT):
        pass_trajectories = []
        pass_updates = []
        nonzero_update_count = 0
        nonzero_outcome_count = 0
        for seed in MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS:
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
                completed_attempt_count,
                jax,
                jnp,
            )
            nonzero_update_count += any(
                value > 0.0 for value in update.parameter_delta_l2
            )
            nonzero_outcome_count += any(
                value != 0.0 for value in trajectory.cumulative_rewards
            )
            pass_trajectories.append(trajectory)
            pass_updates.append(update)
            parameters = update.parameters
            running_baseline = update.baseline_after
            completed_attempt_count += 1
        all_pass_trajectories.append(tuple(pass_trajectories))
        all_updates.extend(pass_updates)
        per_pass_nonzero_updates.append(nonzero_update_count)
        per_pass_nonzero_outcomes.append(nonzero_outcome_count)
        pass_ending_baselines.append(running_baseline)

    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if (
        completed_attempt_count != 128
        or tuple(per_pass_nonzero_updates)
        != _EXPECTED_PER_PASS_NONZERO_UPDATE_COUNTS
        or tuple(per_pass_nonzero_outcomes)
        != _EXPECTED_PER_PASS_NONZERO_OUTCOME_COUNTS
        or not all(
            _close(actual, expected)
            for actual_row, expected_row in zip(
                pass_ending_baselines,
                _EXPECTED_PASS_ENDING_BASELINES,
            )
            for actual, expected in zip(actual_row, expected_row)
        )
        or not all(
            _close(actual, expected)
            for actual, expected in zip(final_deltas, _EXPECTED_FINAL_DELTAS)
        )
    ):
        raise MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError(
            "four-pass training summary differs from the approved probe"
        )

    final_evaluation = _evaluate(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
    )
    final_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_evaluation
    )
    changed_seeds = tuple(
        seed
        for seed, before, after in zip(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS,
            initial_evaluation,
            final_evaluation,
        )
        if before != after
    )
    initial_positive = sum(value > 0.0 for value in initial_rewards)
    final_positive = sum(value > 0.0 for value in final_rewards)
    initial_negative = sum(value < 0.0 for value in initial_rewards)
    final_negative = sum(value < 0.0 for value in final_rewards)
    disjoint = not set(
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS
    ).intersection(
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS
    )
    if (
        final_rewards != _EXPECTED_FINAL_EVALUATION_REWARDS
        or sum(initial_rewards) != -312.0
        or sum(final_rewards) != -297.0
        or (initial_positive, final_positive) != (2, 2)
        or (initial_negative, final_negative) != (20, 19)
        or changed_seeds != _EXPECTED_CHANGED_EVALUATION_SEEDS
        or not disjoint
    ):
        raise MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError(
            "final evaluation differs from the approved probe"
        )

    pass_trajectories = tuple(all_pass_trajectories)
    updates = tuple(all_updates)
    return MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_EVALUATION_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        pass_count=_PASS_COUNT,
        learning_rate=_LEARNING_RATE,
        training_seeds_per_pass=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS
        ),
        evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS
        ),
        update_attempt_count=completed_attempt_count,
        per_pass_nonzero_update_counts=tuple(per_pass_nonzero_updates),
        per_pass_nonzero_raw_outcome_counts=tuple(per_pass_nonzero_outcomes),
        per_pass_transition_counts=tuple(
            tuple(len(item.action_trace) for item in rows)
            for rows in pass_trajectories
        ),
        per_pass_actor_traces=tuple(
            tuple(item.actor_trace for item in rows) for rows in pass_trajectories
        ),
        per_pass_action_traces=tuple(
            tuple(item.action_trace for item in rows) for rows in pass_trajectories
        ),
        per_pass_legal_action_traces=tuple(
            tuple(item.legal_action_trace for item in rows)
            for rows in pass_trajectories
        ),
        per_pass_cumulative_raw_rewards=tuple(
            tuple(item.cumulative_rewards for item in rows)
            for rows in pass_trajectories
        ),
        per_pass_final_scores=tuple(
            tuple(item.final_scores for item in rows) for rows in pass_trajectories
        ),
        per_pass_action_trace_sha256=tuple(
            tuple(_trace_sha256(item.action_trace) for item in rows)
            for rows in pass_trajectories
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
        pass_ending_baselines=tuple(pass_ending_baselines),
        final_running_baseline=running_baseline,
        final_parameter_delta_l2=final_deltas,
        initial_evaluation_transition_counts=tuple(
            item.transition_count for item in initial_evaluation
        ),
        final_evaluation_transition_counts=tuple(
            item.transition_count for item in final_evaluation
        ),
        initial_evaluation_project_action_traces=tuple(
            item.project_action_trace for item in initial_evaluation
        ),
        final_evaluation_project_action_traces=tuple(
            item.project_action_trace for item in final_evaluation
        ),
        initial_evaluation_project_raw_rewards=initial_rewards,
        final_evaluation_project_raw_rewards=final_rewards,
        initial_evaluation_final_scores=tuple(
            item.final_scores for item in initial_evaluation
        ),
        final_evaluation_final_scores=tuple(
            item.final_scores for item in final_evaluation
        ),
        initial_project_raw_sum=sum(initial_rewards),
        final_project_raw_sum=sum(final_rewards),
        project_raw_sum_delta=sum(final_rewards) - sum(initial_rewards),
        initial_positive_round_count=initial_positive,
        final_positive_round_count=final_positive,
        initial_negative_round_count=initial_negative,
        final_negative_round_count=final_negative,
        changed_evaluation_seeds=changed_seeds,
        training_evaluation_seeds_disjoint=disjoint,
        evaluation_call_count=2,
        evaluation_update_count=0,
        parameters_changed=all(value > 0.0 for value in final_deltas),
        bounded_diagnostic_improved=True,
        selected_pass_index=None,
        selected_checkpoint_id=None,
        all_training_actions_legal=True,
        all_rounds_terminated=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_EVALUATION_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationSmokeError",
    "MahJaxCategoricalMlpFourPassCausalBaselineTrainingEvaluationResult",
    "run_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke",
]
