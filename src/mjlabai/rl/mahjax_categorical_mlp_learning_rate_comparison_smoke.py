"""Compare four fixed raw-return learning rates on one MahJax diagnostic.

Every branch starts from identical reviewed imitation parameters, applies five
raw actor-indexed updates, and receives the same disjoint no-update evaluation.
This records a greedy behavior threshold; it does not select an optimal rate.
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


MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_learning_rate_comparison_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES = (0.01, 0.005, 0.001, 0.0001)
MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS
)
MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS = tuple(range(20, 52))


def _replace_expected_items(values, replacements):
    result = list(values)
    for index, replacement in replacements.items():
        result[index] = replacement
    return tuple(result)


_EXPECTED_EXTRA_EVALUATION_TRANSITIONS_BEFORE = (
    85,
    63,
    59,
    73,
    92,
    51,
    85,
    91,
    83,
    88,
    21,
    83,
    87,
    62,
    68,
    61,
)
_EXPECTED_EXTRA_EVALUATION_TRANSITIONS_LARGER = _replace_expected_items(
    _EXPECTED_EXTRA_EVALUATION_TRANSITIONS_BEFORE,
    {3: 72, 8: 84},
)
_EXPECTED_EXTRA_PROJECT_TRACES_BEFORE = (
    (28, 29, 27, 30, 31, 33, 32, 32, 31, 8, 84, 84, 17, 84, 71, 71, 71, 71, 84, 71, 84, 26, 84, 0),
    (28, 31, 33, 84, 71, 8, 8, 71, 71, 84, 71, 84, 71, 71, 84, 71),
    (28, 30, 84, 32, 33, 71, 84, 71, 71, 84, 71, 17, 26, 71),
    (29, 27, 31, 71, 84, 0, 84, 9, 84, 71, 17, 71, 71, 71, 71, 71, 71, 71),
    (33, 33, 8, 71, 71, 71, 71, 71, 71, 71, 84, 71, 71, 84, 71, 71, 71, 10, 84, 16),
    (32, 71, 71, 0, 8, 9, 18, 84, 29, 28, 84, 71, 17),
    (28, 29, 27, 30, 32, 33, 71, 18, 71, 8, 84, 9, 28, 30, 84, 26, 2, 71, 1, 84, 71),
    (8, 0, 71, 84, 18, 71, 84, 71, 71, 71, 71, 84, 71, 71, 71, 84, 71, 71, 84, 71, 71, 71, 71),
    (28, 30, 84, 31, 28, 8, 71, 71, 9, 71, 0, 33, 84, 32, 10, 71, 71, 84, 71, 84, 10),
    (28, 27, 30, 32, 8, 71, 71, 71, 84, 71, 84, 26, 71, 71, 84, 71, 71, 84, 71, 84, 10, 84, 84, 71, 71),
    (29, 27, 27, 30),
    (28, 30, 30, 18, 71, 71, 71, 9, 17, 71, 71, 17, 71, 84, 71, 71, 71, 71),
    (27, 8, 71, 0, 18, 71, 10, 71, 84, 71, 84, 71, 71, 71, 84, 71, 71, 84, 71, 84, 71, 71),
    (29, 30, 31, 71, 71, 0, 71, 9, 84, 71, 71, 71, 84, 71, 71),
    (28, 28, 27, 31, 31, 27, 84, 32, 71, 71, 71, 71, 84, 18, 71, 71),
    (29, 30, 33, 84, 18, 31, 71, 71, 84, 26, 84, 71, 71, 71),
)
_EXPECTED_EXTRA_PROJECT_TRACES_RATE_01 = _replace_expected_items(
    _EXPECTED_EXTRA_PROJECT_TRACES_BEFORE,
    {
        3: (29, 27, 31, 71, 84, 0, 84, 9, 84, 71, 17, 71, 71, 71, 71, 19, 71, 71),
        7: (8, 0, 71, 84, 18, 71, 84, 71, 71, 71, 71, 84, 71, 71, 71, 84, 71, 1, 71, 71, 71, 71),
        8: (28, 30, 84, 31, 28, 8, 0, 71, 71, 71, 9, 33, 84, 32, 10, 71, 71, 84, 71, 84, 10),
        14: (28, 28, 27, 31, 31, 27, 84, 32, 18, 71, 71, 71, 84, 10, 71, 71),
    },
)
_EXPECTED_EXTRA_PROJECT_TRACES_RATE_005 = _replace_expected_items(
    _EXPECTED_EXTRA_PROJECT_TRACES_BEFORE,
    {
        3: (29, 27, 31, 71, 84, 0, 84, 9, 84, 71, 17, 71, 71, 71, 71, 19, 71, 71),
        8: (28, 30, 84, 31, 28, 8, 0, 71, 71, 71, 9, 71, 84, 33, 71, 71, 71, 84, 71, 84, 10),
        14: (28, 28, 27, 31, 31, 27, 84, 32, 18, 71, 71, 71, 84, 10, 71, 71),
    },
)
_EXPECTED_EXTRA_PROJECT_REWARDS_BEFORE = (
    -15.0,
    0.0,
    -20.0,
    0.0,
    0.0,
    -39.0,
    -15.0,
    0.0,
    -15.0,
    0.0,
    0.0,
    -10.0,
    -15.0,
    -52.0,
    0.0,
    0.0,
)
_EXPECTED_EXTRA_PROJECT_REWARDS_RATE_01 = _replace_expected_items(
    _EXPECTED_EXTRA_PROJECT_REWARDS_BEFORE,
    {7: -15.0},
)
_EXPECTED_EXTRA_EVALUATION_SCORES_BEFORE = (
    (235, 255, 235, 255),
    (250, 308, 192, 250),
    (230, 320, 220, 230),
    (250, 250, 130, 370),
    (250, 250, 250, 250),
    (211, 250, 250, 289),
    (235, 235, 255, 255),
    (250, 250, 250, 250),
    (235, 235, 265, 255),
    (250, 250, 250, 250),
    (250, 276, 250, 224),
    (240, 240, 270, 240),
    (235, 235, 255, 255),
    (198, 312, 250, 240),
    (250, 322, 188, 240),
    (250, 370, 250, 130),
)
_EXPECTED_EXTRA_EVALUATION_SCORES_RATE_01 = _replace_expected_items(
    _EXPECTED_EXTRA_EVALUATION_SCORES_BEFORE,
    {7: (235, 255, 265, 235)},
)

_EXPECTED_EXPANDED_EVALUATION_TRANSITIONS_BEFORE = (
    _EXPECTED_EVALUATION_TRANSITIONS_BEFORE
    + _EXPECTED_EXTRA_EVALUATION_TRANSITIONS_BEFORE
)
_EXPECTED_EXPANDED_EVALUATION_TRANSITIONS_LARGER = (
    _EXPECTED_EVALUATION_TRANSITIONS_AFTER
    + _EXPECTED_EXTRA_EVALUATION_TRANSITIONS_LARGER
)
_EXPECTED_EXPANDED_PROJECT_TRACES_BEFORE = (
    _EXPECTED_PROJECT_TRACES_BEFORE + _EXPECTED_EXTRA_PROJECT_TRACES_BEFORE
)
_EXPECTED_EXPANDED_PROJECT_TRACES_RATE_01 = (
    _EXPECTED_PROJECT_TRACES_AFTER + _EXPECTED_EXTRA_PROJECT_TRACES_RATE_01
)
_EXPECTED_EXPANDED_PROJECT_TRACES_RATE_005 = (
    _EXPECTED_PROJECT_TRACES_AFTER + _EXPECTED_EXTRA_PROJECT_TRACES_RATE_005
)
_EXPECTED_EXPANDED_PROJECT_REWARDS_BEFORE = (
    _EXPECTED_PROJECT_REWARDS_BEFORE + _EXPECTED_EXTRA_PROJECT_REWARDS_BEFORE
)
_EXPECTED_EXPANDED_PROJECT_REWARDS_RATE_01 = (
    _EXPECTED_PROJECT_REWARDS_AFTER + _EXPECTED_EXTRA_PROJECT_REWARDS_RATE_01
)
_EXPECTED_EXPANDED_PROJECT_REWARDS_RATE_005 = (
    _EXPECTED_PROJECT_REWARDS_AFTER + _EXPECTED_EXTRA_PROJECT_REWARDS_BEFORE
)
_EXPECTED_EXPANDED_EVALUATION_SCORES_BEFORE = (
    _EXPECTED_EVALUATION_SCORES_BEFORE + _EXPECTED_EXTRA_EVALUATION_SCORES_BEFORE
)
_EXPECTED_EXPANDED_EVALUATION_SCORES_RATE_01 = (
    _EXPECTED_EVALUATION_SCORES_AFTER + _EXPECTED_EXTRA_EVALUATION_SCORES_RATE_01
)
_EXPECTED_EXPANDED_EVALUATION_SCORES_RATE_005 = (
    _EXPECTED_EVALUATION_SCORES_AFTER + _EXPECTED_EXTRA_EVALUATION_SCORES_BEFORE
)

_EXPECTED_RATE_005_INITIAL_OBJECTIVES = (
    0.0936663598,
    -0.0553493463,
    -0.0609718785,
    -0.0202473067,
    -0.0129290707,
)
_EXPECTED_RATE_005_POST_OBJECTIVES = (
    0.0933388919,
    -0.0553896092,
    -0.0609820187,
    -0.0210793577,
    -0.0130555220,
)
_EXPECTED_RATE_005_STEP_DELTAS = (
    (0.0004852958, 0.0000807953, 0.0011747192, 0.0001264173),
    (0.0001317712, 0.0000300689, 0.0004250894, 0.0000471800),
    (0.0001003441, 0.0000116674, 0.0002001078, 0.0000215250),
    (0.0008152211, 0.0001430813, 0.0018554527, 0.0001914079),
    (0.0002071165, 0.0000584576, 0.0007598695, 0.0000885036),
)
_EXPECTED_RATE_005_FINAL_DELTAS = (
    0.0010509313,
    0.0002272493,
    0.0026764988,
    0.0002789878,
)
_EXPECTED_RATE_001_INITIAL_OBJECTIVES = (
    0.0936663598,
    -0.0553418174,
    -0.0609685183,
    -0.0202602185,
    -0.0127902078,
)
_EXPECTED_RATE_001_POST_OBJECTIVES = (
    0.0936008319,
    -0.0553498678,
    -0.0609705523,
    -0.0204267260,
    -0.0128153013,
)
_EXPECTED_RATE_001_STEP_DELTAS = (
    (0.0000970641, 0.0000161616, 0.0002349455, 0.0000252838),
    (0.0000263484, 0.0000060078, 0.0000849799, 0.0000094329),
    (0.0000200717, 0.0000023308, 0.0000400643, 0.0000043088),
    (0.0001631268, 0.0000286061, 0.0003709990, 0.0000382696),
    (0.0000413553, 0.0000116567, 0.0001514444, 0.0000176446),
)
_EXPECTED_RATE_001_FINAL_DELTAS = (
    0.0002101750,
    0.0000453977,
    0.0005348558,
    0.0000557546,
)
_EXPECTED_RATE_0001_INITIAL_OBJECTIVES = (
    0.0936663598,
    -0.0553401448,
    -0.0609677881,
    -0.0202631094,
    -0.0127590531,
)
_EXPECTED_RATE_0001_POST_OBJECTIVES = (
    0.0936598107,
    -0.0553409383,
    -0.0609679930,
    -0.0202797409,
    -0.0127615593,
)
_EXPECTED_RATE_0001_STEP_DELTAS = (
    (0.0000097117, 0.0000016138, 0.0000234946, 0.0000025292),
    (0.0000026502, 0.0000006018, 0.0000085003, 0.0000009411),
    (0.0000020317, 0.0000002358, 0.0000040108, 0.0000004298),
    (0.0000163146, 0.0000028611, 0.0000370997, 0.0000038250),
    (0.0000041447, 0.0000011633, 0.0000151336, 0.0000017637),
)
_EXPECTED_RATE_0001_FINAL_DELTAS = (
    0.0000210247,
    0.0000045383,
    0.0000534743,
    0.0000055721,
)
_EVIDENCE_GRADE = (
    "P8 local fixed raw-return learning-rate sensitivity smoke evidence only"
)
_WARNINGS = (
    "four-rate bounded raw-return sensitivity diagnostic only",
    "rates are predeclared 0.01, 0.005, 0.001 and 0.0001",
    "all branches start from identical reviewed imitation parameters",
    "all fixed evaluation paths perform zero gradient updates",
    "32-seed project sums are -650, -635, -501 and -501 against initial -501",
    "rates 0.01 and 0.005 no longer have identical fixed evaluation behavior",
    "smaller rates change parameters but leave fixed greedy behavior unchanged",
    "unchanged behavior is not improvement or policy-quality evidence",
    "no rate is ranked, selected, promoted or approved for scale-up",
    "no extra/adaptive rate, early stopping or evaluation-driven update",
    "no persistence, checkpoint, model artifact, external or real data",
    "not model-strength, Tenhou, stable-dan or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpLearningRateComparisonSmokeError(RuntimeError):
    """Raised when the exact fixed-rate comparison contract fails."""


@dataclass(frozen=True)
class _LearningRateUpdate:
    parameters: object
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]


@dataclass(frozen=True)
class _LearningRateBranchResult:
    learning_rate: float
    update_count: int
    training_transition_counts: Tuple[int, ...]
    training_seat_decision_counts: Tuple[Tuple[int, ...], ...]
    training_actor_traces: Tuple[Tuple[int, ...], ...]
    training_action_traces: Tuple[Tuple[int, ...], ...]
    training_legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    training_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
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
class MahJaxCategoricalMlpLearningRateComparisonResult:
    """Immutable diagnostics from four fixed raw-return step sizes."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    learning_rates: Tuple[float, ...]
    training_seeds: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    training_result: MahJaxCategoricalMlpImitationResult
    initial_evaluation_transition_counts: Tuple[int, ...]
    initial_evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    initial_evaluation_project_raw_rewards: Tuple[float, ...]
    initial_evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    initial_project_raw_sum: float
    branches: Tuple[_LearningRateBranchResult, ...]
    branch_initial_parameters_identical: bool
    branch_final_parameters_distinct: bool
    larger_rate_evaluation_identity: bool
    smaller_rate_initial_behavior_identity: bool
    all_branches_changed_parameters: bool
    training_evaluation_seeds_disjoint: bool
    evaluation_update_count: int
    all_actions_legal: bool
    all_rounds_terminated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _apply_variable_rate_raw_return_update(
    parameters,
    trajectory,
    learning_rate,
    jax,
    jnp,
):
    seat_returns = jnp.asarray(
        trajectory.cumulative_rewards,
        dtype=jnp.float32,
    ) / 100.0
    decision_returns = seat_returns[trajectory.actors]

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
            value - learning_rate * gradient
            for value, gradient in zip(parameters, gradients)
        )
    )
    return _LearningRateUpdate(
        parameters=updated_parameters,
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
        for seed in MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS
    )


def _train_and_evaluate_rate(
    learning_rate,
    initial_parameters,
    initial_evaluation,
    environment,
    step_fn,
    rule_policy_fn,
    jax,
    jnp,
    mahjax,
):
    parameters = tuple(initial_parameters)
    trajectories = []
    updates = []
    for seed in MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS:
        trajectory = _collect_all_project_round(
            seed,
            parameters,
            jax,
            jnp,
            mahjax,
        )
        if learning_rate == 0.01:
            reviewed_update = _apply_actor_indexed_raw_outcome_update(
                parameters,
                trajectory,
                jax,
                jnp,
            )
            update = _LearningRateUpdate(
                parameters=reviewed_update.parameters,
                initial_objective=reviewed_update.initial_objective,
                post_update_objective=reviewed_update.post_update_objective,
                parameter_delta_l2=reviewed_update.parameter_delta_l2,
            )
        else:
            update = _apply_variable_rate_raw_return_update(
                parameters,
                trajectory,
                learning_rate,
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
            item.action_trace[:12] != expected
            for item, expected in zip(
                trajectories,
                _EXPECTED_TRAINING_ACTION_PREFIXES,
            )
        )
    ):
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            f"learning-rate {learning_rate} trajectories differ from the probe"
        )

    expected_by_rate = {
        0.01: (
            _EXPECTED_INITIAL_OBJECTIVES,
            _EXPECTED_POST_OBJECTIVES,
            _EXPECTED_PER_UPDATE_DELTAS,
            _EXPECTED_FINAL_DELTAS,
        ),
        0.005: (
            _EXPECTED_RATE_005_INITIAL_OBJECTIVES,
            _EXPECTED_RATE_005_POST_OBJECTIVES,
            _EXPECTED_RATE_005_STEP_DELTAS,
            _EXPECTED_RATE_005_FINAL_DELTAS,
        ),
        0.001: (
            _EXPECTED_RATE_001_INITIAL_OBJECTIVES,
            _EXPECTED_RATE_001_POST_OBJECTIVES,
            _EXPECTED_RATE_001_STEP_DELTAS,
            _EXPECTED_RATE_001_FINAL_DELTAS,
        ),
        0.0001: (
            _EXPECTED_RATE_0001_INITIAL_OBJECTIVES,
            _EXPECTED_RATE_0001_POST_OBJECTIVES,
            _EXPECTED_RATE_0001_STEP_DELTAS,
            _EXPECTED_RATE_0001_FINAL_DELTAS,
        ),
    }
    expected_initial, expected_post, expected_steps, expected_final = (
        expected_by_rate[learning_rate]
    )
    initial_objectives = tuple(item.initial_objective for item in updates)
    post_objectives = tuple(item.post_update_objective for item in updates)
    step_deltas = tuple(item.parameter_delta_l2 for item in updates)
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
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            f"learning-rate {learning_rate} updates differ from the probe"
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
    changed_seeds = tuple(
        seed
        for seed, initial_item, rate_item in zip(
            MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS,
            initial_evaluation,
            evaluation,
        )
        if initial_item != rate_item
    )
    if learning_rate == 0.01:
        expected_transitions = _EXPECTED_EXPANDED_EVALUATION_TRANSITIONS_LARGER
        expected_traces = _EXPECTED_EXPANDED_PROJECT_TRACES_RATE_01
        expected_rewards = _EXPECTED_EXPANDED_PROJECT_REWARDS_RATE_01
        expected_scores = _EXPECTED_EXPANDED_EVALUATION_SCORES_RATE_01
        expected_changed = (32, 39, 43, 44, 50)
    elif learning_rate == 0.005:
        expected_transitions = _EXPECTED_EXPANDED_EVALUATION_TRANSITIONS_LARGER
        expected_traces = _EXPECTED_EXPANDED_PROJECT_TRACES_RATE_005
        expected_rewards = _EXPECTED_EXPANDED_PROJECT_REWARDS_RATE_005
        expected_scores = _EXPECTED_EXPANDED_EVALUATION_SCORES_RATE_005
        expected_changed = (32, 39, 44, 50)
    else:
        expected_transitions = _EXPECTED_EXPANDED_EVALUATION_TRANSITIONS_BEFORE
        expected_traces = _EXPECTED_EXPANDED_PROJECT_TRACES_BEFORE
        expected_rewards = _EXPECTED_EXPANDED_PROJECT_REWARDS_BEFORE
        expected_scores = _EXPECTED_EXPANDED_EVALUATION_SCORES_BEFORE
        expected_changed = ()
    if (
        evaluation_transitions != expected_transitions
        or evaluation_traces != expected_traces
        or evaluation_rewards != expected_rewards
        or evaluation_scores != expected_scores
        or changed_seeds != expected_changed
    ):
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            f"learning-rate {learning_rate} evaluation differs from the probe"
        )

    return (
        parameters,
        _LearningRateBranchResult(
            learning_rate=learning_rate,
            update_count=5,
            training_transition_counts=transitions,
            training_seat_decision_counts=seat_counts,
            training_actor_traces=tuple(item.actor_trace for item in trajectories),
            training_action_traces=tuple(item.action_trace for item in trajectories),
            training_legal_action_traces=tuple(
                item.legal_action_trace for item in trajectories
            ),
            training_cumulative_raw_rewards=cumulative_rewards,
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


def run_mahjax_categorical_mlp_learning_rate_comparison_smoke(
) -> MahJaxCategoricalMlpLearningRateComparisonResult:
    """Run the exact four-branch raw-return rate comparison."""

    try:
        jax, jnp, initial_parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
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
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            "pinned MahJax/JAX learning-rate runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            "learning-rate runtime differs from the pinned contract"
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
        initial_transitions != _EXPECTED_EXPANDED_EVALUATION_TRANSITIONS_BEFORE
        or initial_traces != _EXPECTED_EXPANDED_PROJECT_TRACES_BEFORE
        or initial_rewards != _EXPECTED_EXPANDED_PROJECT_REWARDS_BEFORE
        or initial_scores != _EXPECTED_EXPANDED_EVALUATION_SCORES_BEFORE
        or sum(initial_rewards) != -501.0
    ):
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            "initial fixed evaluation differs from the probe"
        )

    branch_initial_parameters = {
        rate: tuple(initial_parameters)
        for rate in MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES
    }
    initial_identical = all(
        all(
            bool(jnp.array_equal(reference, candidate))
            for reference, candidate in zip(
                initial_parameters,
                branch_initial_parameters[rate],
            )
        )
        for rate in MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES
    )
    final_parameters = []
    branch_results = []
    for learning_rate in MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES:
        try:
            parameters, branch_result = _train_and_evaluate_rate(
                learning_rate,
                branch_initial_parameters[learning_rate],
                initial_evaluation,
                environment,
                step_fn,
                rule_policy_fn,
                jax,
                jnp,
                mahjax,
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
                f"learning-rate {learning_rate} branch failed"
            ) from exc
        final_parameters.append(parameters)
        branch_results.append(branch_result)

    pairwise_distinct = all(
        any(
            not bool(jnp.array_equal(left_value, right_value))
            for left_value, right_value in zip(left, right)
        )
        for left_index, left in enumerate(final_parameters)
        for right in final_parameters[left_index + 1 :]
    )
    all_changed = all(
        all(value > 0.0 for value in branch.final_parameter_delta_l2)
        for branch in branch_results
    )
    larger_identity = (
        branch_results[0].evaluation_transition_counts
        == branch_results[1].evaluation_transition_counts
        and branch_results[0].evaluation_project_action_traces
        == branch_results[1].evaluation_project_action_traces
        and branch_results[0].evaluation_project_raw_rewards
        == branch_results[1].evaluation_project_raw_rewards
        and branch_results[0].evaluation_final_scores
        == branch_results[1].evaluation_final_scores
    )
    smaller_initial_identity = all(
        branch.evaluation_transition_counts == initial_transitions
        and branch.evaluation_project_action_traces == initial_traces
        and branch.evaluation_project_raw_rewards == initial_rewards
        and branch.evaluation_final_scores == initial_scores
        for branch in branch_results[2:]
    )
    disjoint = not set(
        MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS
    ).intersection(MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS)
    if not all(
        (
            initial_identical,
            pairwise_distinct,
            all_changed,
            not larger_identity,
            smaller_initial_identity,
            disjoint,
        )
    ):
        raise MahJaxCategoricalMlpLearningRateComparisonSmokeError(
            "learning-rate comparison invariants were not demonstrated"
        )

    return MahJaxCategoricalMlpLearningRateComparisonResult(
        smoke_version=MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        learning_rates=MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES,
        training_seeds=MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS,
        evaluation_seeds=MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS,
        training_result=training_result,
        initial_evaluation_transition_counts=initial_transitions,
        initial_evaluation_project_action_traces=initial_traces,
        initial_evaluation_project_raw_rewards=initial_rewards,
        initial_evaluation_final_scores=initial_scores,
        initial_project_raw_sum=sum(initial_rewards),
        branches=tuple(branch_results),
        branch_initial_parameters_identical=initial_identical,
        branch_final_parameters_distinct=pairwise_distinct,
        larger_rate_evaluation_identity=larger_identity,
        smaller_rate_initial_behavior_identity=smaller_initial_identity,
        all_branches_changed_parameters=all_changed,
        training_evaluation_seeds_disjoint=disjoint,
        evaluation_update_count=0,
        all_actions_legal=True,
        all_rounds_terminated=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES",
    "MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpLearningRateComparisonSmokeError",
    "MahJaxCategoricalMlpLearningRateComparisonResult",
    "run_mahjax_categorical_mlp_learning_rate_comparison_smoke",
]
