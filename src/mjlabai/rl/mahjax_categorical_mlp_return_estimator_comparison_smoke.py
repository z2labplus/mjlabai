"""Compare three bounded return estimators on one fixed MahJax diagnostic.

Raw, per-round seat-centered, and per-round seat-standardized branches start
from identical reviewed imitation parameters. Each branch receives five local
updates and then a disjoint no-update mixed-policy evaluation. The result
records failure diagnostics; it does not select an estimator or claim strength.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    _apply_actor_indexed_raw_outcome_update,
    _collect_all_project_round,
    _load_pinned_runtime,
    _seat_decision_counts,
)
from mjlabai.rl.mahjax_categorical_mlp_five_round_training_evaluation_smoke import (
    MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE,
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS,
    _EXPECTED_EVALUATION_SCORES_AFTER,
    _EXPECTED_EVALUATION_SCORES_BEFORE,
    _EXPECTED_EVALUATION_TRANSITIONS_AFTER,
    _EXPECTED_EVALUATION_TRANSITIONS_BEFORE,
    _EXPECTED_FINAL_DELTAS,
    _EXPECTED_INITIAL_OBJECTIVES,
    _EXPECTED_PER_UPDATE_DELTAS,
    _EXPECTED_POST_OBJECTIVES,
    _EXPECTED_PROJECT_REWARDS_AFTER,
    _EXPECTED_PROJECT_REWARDS_BEFORE,
    _EXPECTED_PROJECT_TRACES_AFTER,
    _EXPECTED_PROJECT_TRACES_BEFORE,
    _EXPECTED_TRAINING_ACTION_PREFIXES,
    _EXPECTED_TRAINING_CUMULATIVE_REWARDS,
    _EXPECTED_TRAINING_FINAL_REWARDS,
    _EXPECTED_TRAINING_FINAL_SCORES,
    _EXPECTED_TRAINING_SEAT_COUNTS,
    _EXPECTED_TRAINING_TRANSITION_COUNTS,
    _collect_mixed_policy_evaluation_round,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MahJaxCategoricalMlpImitationResult,
    _mlp_logits,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_return_estimator_comparison_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS
)
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS
)
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE = (
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE
)

_RAW = "raw_actor_return"
_CENTERED = "seat_centered_actor_return"
_STANDARDIZED = "seat_standardized_actor_return"
_ESTIMATOR_IDS = (_RAW, _CENTERED, _STANDARDIZED)
_STANDARD_DEVIATION_EPSILON = 1e-6

_EXPECTED_CENTERED_INITIAL_OBJECTIVES = (
    0.0936663598,
    -0.0330250338,
    -0.0432044491,
    -0.0202107076,
    0.0090211481,
)
_EXPECTED_CENTERED_POST_OBJECTIVES = (
    0.0930117071,
    -0.0330865569,
    -0.0432192981,
    -0.0218739361,
    0.0087888129,
)
_EXPECTED_CENTERED_STEP_DELTAS = (
    (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356),
    (0.0002272531, 0.0000499290, 0.0007442888, 0.0000819775),
    (0.0001672037, 0.0000214138, 0.0003444966, 0.0000374387),
    (0.0016296259, 0.0002862654, 0.0037121978, 0.0003829691),
    (0.0004028465, 0.0001133554, 0.0014549729, 0.0001699619),
)
_EXPECTED_CENTERED_FINAL_DELTAS = (
    0.0020699743,
    0.0004389429,
    0.0052021975,
    0.0005401245,
)
_EXPECTED_STANDARDIZED_INITIAL_OBJECTIVES = (
    0.2305906415,
    -0.2544234991,
    -0.3327357769,
    -0.0240334999,
    0.0665053651,
)
_EXPECTED_STANDARDIZED_POST_OBJECTIVES = (
    0.2266280502,
    -0.2580936253,
    -0.3336068094,
    -0.0263392832,
    0.0525678620,
)
_EXPECTED_STANDARDIZED_STEP_DELTAS = (
    (0.0023894196, 0.0003978050, 0.0057839043, 0.0006224382),
    (0.0017507906, 0.0003852099, 0.0057357890, 0.0006317776),
    (0.0012885195, 0.0001660873, 0.0026326515, 0.0002865161),
    (0.0019121285, 0.0003374417, 0.0043744170, 0.0004516061),
    (0.0031031084, 0.0008749461, 0.0112318872, 0.0013115645),
)
_EXPECTED_STANDARDIZED_FINAL_DELTAS = (
    0.0056803911,
    0.0015099167,
    0.0181233995,
    0.0020000334,
)
_EXPECTED_STANDARDIZED_TRANSITIONS = (
    95, 73, 79, 51, 86, 86, 53, 59, 86, 31, 61, 64, 62, 48, 62, 85,
)
_EXPECTED_STANDARDIZED_REWARDS = (
    -10.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
    -15.0, 0.0, -180.0, 0.0, -60.0, 0.0, -40.0, -26.0,
)
_EXPECTED_STANDARDIZED_SCORES = (
    (240, 280, 240, 240),
    *_EXPECTED_EVALUATION_SCORES_BEFORE[1:7],
    _EXPECTED_EVALUATION_SCORES_BEFORE[7],
    *_EXPECTED_EVALUATION_SCORES_BEFORE[8:11],
    _EXPECTED_EVALUATION_SCORES_BEFORE[11],
    (190, 190, 430, 190),
    *_EXPECTED_EVALUATION_SCORES_BEFORE[13:15],
    (224, 240, 296, 240),
)
_EXPECTED_STANDARDIZED_TRACES = (
    (29, 29, 32, 33, 84, 0, 71, 18, 71, 84, 71, 84, 17, 84, 71, 71, 84, 71, 84, 71, 71, 84, 10, 71),
    *_EXPECTED_PROJECT_TRACES_BEFORE[1:7],
    (30, 31, 8, 84, 71, 84, 26, 29, 0, 18, 71, 26, 71, 84, 10),
    *_EXPECTED_PROJECT_TRACES_BEFORE[8:11],
    (31, 33, 71, 71, 8, 0, 17, 71, 71, 71, 84, 71, 71, 84, 10),
    (27, 8, 84, 9, 18, 31, 71, 84, 17, 0, 71, 0, 84, 71, 26, 71),
    *_EXPECTED_PROJECT_TRACES_BEFORE[13:15],
    (33, 9, 84, 17, 71, 71, 84, 71, 71, 71, 71, 71, 84, 71, 71, 71, 26, 71, 72, 14),
)
_EVIDENCE_GRADE = (
    "P8 local raw/centered/standardized return-estimator failure-comparison "
    "smoke evidence only"
)
_WARNINGS = (
    "three-estimator bounded five-round comparison diagnostic only",
    "raw, centered and standardized branches start from identical parameters",
    "all fixed evaluation paths perform zero gradient updates",
    "initial/raw/centered/standardized project sums are -320/-454/-454/-490",
    "centering changes parameters but not fixed greedy evaluation behavior",
    "standardization worsens this fixed diagnostic and is not generally ranked",
    "no estimator is selected, promoted or approved for scale-up",
    "no baseline, critic, discount, GAE, entropy, clipping or reward shaping",
    "no persistence, checkpoint, model artifact, external or real data",
    "not improvement, policy-quality, estimator-superiority or strength evidence",
    "not Tenhou, stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(RuntimeError):
    """Raised when the exact estimator comparison contract fails."""


@dataclass(frozen=True)
class _EstimatorUpdate:
    parameters: object
    estimated_seat_returns: Tuple[float, ...]
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]


@dataclass(frozen=True)
class _EstimatorBranchResult:
    estimator_id: str
    update_count: int
    training_transition_counts: Tuple[int, ...]
    training_seat_decision_counts: Tuple[Tuple[int, ...], ...]
    training_actor_traces: Tuple[Tuple[int, ...], ...]
    training_action_traces: Tuple[Tuple[int, ...], ...]
    training_legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    training_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    estimated_seat_returns: Tuple[Tuple[float, ...], ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_update_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    final_parameter_delta_l2: Tuple[float, ...]
    evaluation_transition_counts: Tuple[int, ...]
    evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    evaluation_project_raw_rewards: Tuple[float, ...]
    evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    changed_from_initial_evaluation_seeds: Tuple[int, ...]
    project_raw_sum: float
    positive_round_count: int
    negative_round_count: int


@dataclass(frozen=True)
class MahJaxCategoricalMlpReturnEstimatorComparisonResult:
    """Immutable raw/centered/standardized training/evaluation comparison."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    training_seeds: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    estimator_ids: Tuple[str, ...]
    learning_rate: float
    training_result: MahJaxCategoricalMlpImitationResult
    initial_evaluation_transition_counts: Tuple[int, ...]
    initial_evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    initial_evaluation_project_raw_rewards: Tuple[float, ...]
    initial_evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    initial_project_raw_sum: float
    raw_branch: _EstimatorBranchResult
    centered_branch: _EstimatorBranchResult
    standardized_branch: _EstimatorBranchResult
    branch_initial_parameters_identical: bool
    branch_final_parameters_distinct: bool
    raw_matches_reviewed_failure_diagnostic: bool
    centered_parameters_differ_from_raw: bool
    centered_evaluation_matches_raw: bool
    standardized_fixed_diagnostic_is_worse: bool
    training_evaluation_seeds_disjoint: bool
    evaluation_update_count: int
    all_actions_legal: bool
    all_rounds_terminated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _apply_estimated_return_update(
    parameters,
    trajectory,
    estimator_id,
    jax,
    jnp,
):
    raw_returns = jnp.asarray(
        trajectory.cumulative_rewards,
        dtype=jnp.float32,
    ) / 100.0
    centered_returns = raw_returns - jnp.mean(raw_returns)
    if estimator_id == _CENTERED:
        estimated_returns = centered_returns
    elif estimator_id == _STANDARDIZED:
        standard_deviation = jnp.std(centered_returns)
        estimated_returns = jnp.where(
            standard_deviation > _STANDARD_DEVIATION_EPSILON,
            centered_returns / standard_deviation,
            centered_returns,
        )
    else:
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            f"unsupported private estimator {estimator_id!r}"
        )
    decision_returns = estimated_returns[trajectory.actors]

    def objective(model_parameters):
        logits = _mlp_logits(model_parameters, trajectory.features, jax)
        legal_logits = jnp.where(trajectory.legal_masks, logits, -1e9)
        log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
        selected_log_probabilities = log_probabilities[
            jnp.arange(trajectory.actions.shape[0]),
            trajectory.actions,
        ]
        return -jnp.mean(decision_returns * selected_log_probabilities)

    initial_objective, gradients = jax.jit(jax.value_and_grad(objective))(
        parameters
    )
    updated_parameters = jax.block_until_ready(
        tuple(
            value
            - MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE * gradient
            for value, gradient in zip(parameters, gradients)
        )
    )
    return _EstimatorUpdate(
        parameters=updated_parameters,
        estimated_seat_returns=tuple(float(value) for value in estimated_returns),
        initial_objective=float(initial_objective),
        post_update_objective=float(objective(updated_parameters)),
        parameter_delta_l2=tuple(
            float(jnp.linalg.norm(updated - initial))
            for initial, updated in zip(parameters, updated_parameters)
        ),
    )


def _evaluate_parameters(
    parameters,
    environment,
    step_fn,
    rule_policy_fn,
    jax,
    jnp,
):
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
        for seed in MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS
    )


def _branch_result(
    estimator_id,
    initial_parameters,
    environment,
    step_fn,
    rule_policy_fn,
    initial_evaluation,
    jax,
    jnp,
    mahjax,
):
    parameters = tuple(initial_parameters)
    trajectories = []
    updates = []
    for seed in MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS:
        trajectory = _collect_all_project_round(
            seed,
            parameters,
            jax,
            jnp,
            mahjax,
        )
        if estimator_id == _RAW:
            raw_update = _apply_actor_indexed_raw_outcome_update(
                parameters,
                trajectory,
                jax,
                jnp,
            )
            update = _EstimatorUpdate(
                parameters=raw_update.parameters,
                estimated_seat_returns=raw_update.seat_return_scales,
                initial_objective=raw_update.initial_objective,
                post_update_objective=raw_update.post_update_objective,
                parameter_delta_l2=raw_update.parameter_delta_l2,
            )
        else:
            update = _apply_estimated_return_update(
                parameters,
                trajectory,
                estimator_id,
                jax,
                jnp,
            )
        trajectories.append(trajectory)
        updates.append(update)
        parameters = update.parameters

    transitions = tuple(len(item.action_trace) for item in trajectories)
    seat_counts = tuple(
        _seat_decision_counts(item.actor_trace) for item in trajectories
    )
    cumulative_rewards = tuple(item.cumulative_rewards for item in trajectories)
    if (
        transitions != _EXPECTED_TRAINING_TRANSITION_COUNTS
        or seat_counts != _EXPECTED_TRAINING_SEAT_COUNTS
        or cumulative_rewards != _EXPECTED_TRAINING_CUMULATIVE_REWARDS
        or tuple(item.final_rewards for item in trajectories)
        != _EXPECTED_TRAINING_FINAL_REWARDS
        or tuple(item.final_scores for item in trajectories)
        != _EXPECTED_TRAINING_FINAL_SCORES
        or any(
            trajectory.action_trace[:12] != expected
            for trajectory, expected in zip(
                trajectories,
                _EXPECTED_TRAINING_ACTION_PREFIXES,
            )
        )
    ):
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            f"{estimator_id} training trajectories differ from the reviewed probe"
        )

    initial_objectives = tuple(item.initial_objective for item in updates)
    post_objectives = tuple(item.post_update_objective for item in updates)
    step_deltas = tuple(item.parameter_delta_l2 for item in updates)
    expected_by_estimator = {
        _RAW: (
            _EXPECTED_INITIAL_OBJECTIVES,
            _EXPECTED_POST_OBJECTIVES,
            _EXPECTED_PER_UPDATE_DELTAS,
            _EXPECTED_FINAL_DELTAS,
        ),
        _CENTERED: (
            _EXPECTED_CENTERED_INITIAL_OBJECTIVES,
            _EXPECTED_CENTERED_POST_OBJECTIVES,
            _EXPECTED_CENTERED_STEP_DELTAS,
            _EXPECTED_CENTERED_FINAL_DELTAS,
        ),
        _STANDARDIZED: (
            _EXPECTED_STANDARDIZED_INITIAL_OBJECTIVES,
            _EXPECTED_STANDARDIZED_POST_OBJECTIVES,
            _EXPECTED_STANDARDIZED_STEP_DELTAS,
            _EXPECTED_STANDARDIZED_FINAL_DELTAS,
        ),
    }
    expected_initial, expected_post, expected_steps, expected_final = (
        expected_by_estimator[estimator_id]
    )
    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if (
        any(
            not _close(actual, expected)
            for actual, expected in zip(initial_objectives, expected_initial)
        )
        or any(
            not _close(actual, expected)
            for actual, expected in zip(post_objectives, expected_post)
        )
        or any(
            not _close(actual, expected)
            for actual_row, expected_row in zip(step_deltas, expected_steps)
            for actual, expected in zip(actual_row, expected_row)
        )
        or any(
            not _close(actual, expected)
            for actual, expected in zip(final_deltas, expected_final)
        )
        or any(post >= initial for initial, post in zip(initial_objectives, post_objectives))
    ):
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            f"{estimator_id} update diagnostics differ from the reviewed probe"
        )

    evaluation = _evaluate_parameters(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
    )
    evaluation_transitions = tuple(item.transition_count for item in evaluation)
    evaluation_traces = tuple(item.project_action_trace for item in evaluation)
    evaluation_rewards = tuple(
        item.project_cumulative_raw_reward for item in evaluation
    )
    evaluation_scores = tuple(item.final_scores for item in evaluation)
    initial_traces = tuple(item.project_action_trace for item in initial_evaluation)
    changed_seeds = tuple(
        seed
        for seed, initial_item, branch_item in zip(
            MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS,
            initial_evaluation,
            evaluation,
        )
        if initial_item != branch_item
    )
    if estimator_id in (_RAW, _CENTERED):
        expected_transitions = _EXPECTED_EVALUATION_TRANSITIONS_AFTER
        expected_traces = _EXPECTED_PROJECT_TRACES_AFTER
        expected_rewards = _EXPECTED_PROJECT_REWARDS_AFTER
        expected_scores = _EXPECTED_EVALUATION_SCORES_AFTER
        expected_changed = (32,)
    else:
        expected_transitions = _EXPECTED_STANDARDIZED_TRANSITIONS
        expected_traces = _EXPECTED_STANDARDIZED_TRACES
        expected_rewards = _EXPECTED_STANDARDIZED_REWARDS
        expected_scores = _EXPECTED_STANDARDIZED_SCORES
        expected_changed = (20, 27, 31, 32, 35)
    if (
        evaluation_transitions != expected_transitions
        or evaluation_traces != expected_traces
        or evaluation_rewards != expected_rewards
        or evaluation_scores != expected_scores
        or changed_seeds != expected_changed
        or len(initial_traces) != len(evaluation_traces)
    ):
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            f"{estimator_id} evaluation differs from the reviewed probe"
        )

    return (
        parameters,
        _EstimatorBranchResult(
            estimator_id=estimator_id,
            update_count=5,
            training_transition_counts=transitions,
            training_seat_decision_counts=seat_counts,
            training_actor_traces=tuple(item.actor_trace for item in trajectories),
            training_action_traces=tuple(item.action_trace for item in trajectories),
            training_legal_action_traces=tuple(
                item.legal_action_trace for item in trajectories
            ),
            training_cumulative_raw_rewards=cumulative_rewards,
            estimated_seat_returns=tuple(
                item.estimated_seat_returns for item in updates
            ),
            initial_objectives=initial_objectives,
            post_update_objectives=post_objectives,
            per_update_parameter_delta_l2=step_deltas,
            final_parameter_delta_l2=final_deltas,
            evaluation_transition_counts=evaluation_transitions,
            evaluation_project_action_traces=evaluation_traces,
            evaluation_project_raw_rewards=evaluation_rewards,
            evaluation_final_scores=evaluation_scores,
            changed_from_initial_evaluation_seeds=changed_seeds,
            project_raw_sum=sum(evaluation_rewards),
            positive_round_count=sum(value > 0.0 for value in evaluation_rewards),
            negative_round_count=sum(value < 0.0 for value in evaluation_rewards),
        ),
    )


def run_mahjax_categorical_mlp_return_estimator_comparison_smoke(
) -> MahJaxCategoricalMlpReturnEstimatorComparisonResult:
    """Run the exact three-branch bounded estimator comparison."""

    try:
        jax, jnp, initial_parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            "reviewed categorical MLP in-memory training failed"
        ) from exc
    try:
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
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            "pinned MahJax/JAX comparison runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            "comparison runtime differs from the pinned contract"
        )

    initial_evaluation = _evaluate_parameters(
        initial_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
    )
    initial_transitions = tuple(
        item.transition_count for item in initial_evaluation
    )
    initial_traces = tuple(item.project_action_trace for item in initial_evaluation)
    initial_rewards = tuple(
        item.project_cumulative_raw_reward for item in initial_evaluation
    )
    initial_scores = tuple(item.final_scores for item in initial_evaluation)
    if (
        initial_transitions != _EXPECTED_EVALUATION_TRANSITIONS_BEFORE
        or initial_traces != _EXPECTED_PROJECT_TRACES_BEFORE
        or initial_rewards != _EXPECTED_PROJECT_REWARDS_BEFORE
        or initial_scores != _EXPECTED_EVALUATION_SCORES_BEFORE
        or sum(initial_rewards) != -320.0
    ):
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            "initial fixed evaluation differs from the reviewed probe"
        )

    branch_initial_parameters = {
        estimator_id: tuple(initial_parameters) for estimator_id in _ESTIMATOR_IDS
    }
    branch_initial_identical = all(
        all(
            bool(jnp.array_equal(reference, candidate))
            for reference, candidate in zip(
                initial_parameters,
                branch_initial_parameters[estimator_id],
            )
        )
        for estimator_id in _ESTIMATOR_IDS
    )
    branch_parameters = {}
    branch_results = {}
    for estimator_id in _ESTIMATOR_IDS:
        try:
            final_parameters, branch_result = _branch_result(
                estimator_id,
                branch_initial_parameters[estimator_id],
                environment,
                step_fn,
                rule_policy_fn,
                initial_evaluation,
                jax,
                jnp,
                mahjax,
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
                f"{estimator_id} comparison branch failed"
            ) from exc
        branch_parameters[estimator_id] = final_parameters
        branch_results[estimator_id] = branch_result

    raw_parameters = branch_parameters[_RAW]
    centered_parameters = branch_parameters[_CENTERED]
    standardized_parameters = branch_parameters[_STANDARDIZED]
    raw_centered_differ = any(
        not bool(jnp.array_equal(raw, centered))
        for raw, centered in zip(raw_parameters, centered_parameters)
    )
    all_branches_distinct = (
        raw_centered_differ
        and any(
            not bool(jnp.array_equal(raw, standardized))
            for raw, standardized in zip(raw_parameters, standardized_parameters)
        )
        and any(
            not bool(jnp.array_equal(centered, standardized))
            for centered, standardized in zip(
                centered_parameters,
                standardized_parameters,
            )
        )
    )
    raw_result = branch_results[_RAW]
    centered_result = branch_results[_CENTERED]
    standardized_result = branch_results[_STANDARDIZED]
    raw_matches_reviewed = (
        raw_result.project_raw_sum == -454.0
        and raw_result.changed_from_initial_evaluation_seeds == (32,)
    )
    centered_matches_raw = (
        centered_result.evaluation_transition_counts
        == raw_result.evaluation_transition_counts
        and centered_result.evaluation_project_action_traces
        == raw_result.evaluation_project_action_traces
        and centered_result.evaluation_project_raw_rewards
        == raw_result.evaluation_project_raw_rewards
        and centered_result.evaluation_final_scores
        == raw_result.evaluation_final_scores
    )
    standardized_worse = (
        standardized_result.project_raw_sum == -490.0
        and standardized_result.project_raw_sum < raw_result.project_raw_sum
        and standardized_result.positive_round_count == 0
        and standardized_result.negative_round_count == 11
    )
    disjoint = not set(
        MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS
    ).intersection(MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS)
    if not all(
        (
            branch_initial_identical,
            all_branches_distinct,
            raw_matches_reviewed,
            raw_centered_differ,
            centered_matches_raw,
            standardized_worse,
            disjoint,
        )
    ):
        raise MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError(
            "estimator comparison invariants were not demonstrated"
        )

    return MahJaxCategoricalMlpReturnEstimatorComparisonResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        training_seeds=MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS,
        evaluation_seeds=MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS,
        estimator_ids=_ESTIMATOR_IDS,
        learning_rate=MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE,
        training_result=training_result,
        initial_evaluation_transition_counts=initial_transitions,
        initial_evaluation_project_action_traces=initial_traces,
        initial_evaluation_project_raw_rewards=initial_rewards,
        initial_evaluation_final_scores=initial_scores,
        initial_project_raw_sum=sum(initial_rewards),
        raw_branch=raw_result,
        centered_branch=centered_result,
        standardized_branch=standardized_result,
        branch_initial_parameters_identical=branch_initial_identical,
        branch_final_parameters_distinct=all_branches_distinct,
        raw_matches_reviewed_failure_diagnostic=raw_matches_reviewed,
        centered_parameters_differ_from_raw=raw_centered_differ,
        centered_evaluation_matches_raw=centered_matches_raw,
        standardized_fixed_diagnostic_is_worse=standardized_worse,
        training_evaluation_seeds_disjoint=disjoint,
        evaluation_update_count=0,
        all_actions_legal=True,
        all_rounds_terminated=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE",
    "MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError",
    "MahJaxCategoricalMlpReturnEstimatorComparisonResult",
    "run_mahjax_categorical_mlp_return_estimator_comparison_smoke",
]
