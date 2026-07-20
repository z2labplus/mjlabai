"""Compare two fixed MahJax protocols with leave-one-out batch baselines."""

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
    _mlp_logits,
)
from mjlabai.rl.mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke import (
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS,
    _EXPECTED_INITIAL_EVALUATION_REWARDS,
    _EXPECTED_INITIAL_REPLICATION_REWARDS,
    _evaluate,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_TRAINING_PROTOCOL_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS = (
    tuple(range(116, 148))
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS = (
    tuple(range(84, 116))
)

_PASS_COUNT = 4
_TRAJECTORIES_PER_PASS = 32
_LEARNING_RATE = 0.01
_REFERENCE_PROTOCOL_ID = "reference_ordered_0_31_leave_one_out_batch"
_ALTERNATE_PROTOCOL_ID = "alternate_ordered_116_147_leave_one_out_batch"
_EXPECTED_REFERENCE_BATCH_INITIAL_OBJECTIVES = (
    -0.0085045587,
    -0.0085126634,
    -0.0084424117,
    -0.0182129891,
)
_EXPECTED_REFERENCE_BATCH_POST_OBJECTIVES = (
    -0.0085126634,
    -0.0085207718,
    -0.0084506209,
    -0.0182186403,
)
_EXPECTED_REFERENCE_PASS_PARAMETER_DELTAS = (
    (0.0001068668, 0.0000196452, 0.0002614185, 0.0000295520),
    (0.0001068688, 0.0000196514, 0.0002615240, 0.0000295630),
    (0.0001068187, 0.0000196916, 0.0002634126, 0.0000297461),
    (0.0001050941, 0.0000155412, 0.0002113017, 0.0000241913),
)
_EXPECTED_REFERENCE_FINAL_PARAMETER_DELTAS = (
    0.0004183974,
    0.0000731221,
    0.0009828927,
    0.0001114113,
)
_EXPECTED_REFERENCE_TRAINING_REWARD_SUMS = (
    (-55.0, -34.0, -150.0, 179.0),
    (-55.0, -34.0, -150.0, 179.0),
    (-55.0, -34.0, -150.0, 179.0),
    (-35.0, -104.0, -210.0, 289.0),
)
_EXPECTED_ALTERNATE_BATCH_INITIAL_OBJECTIVES = (
    -0.0105261516,
    -0.0105333736,
    -0.0105405992,
    -0.0105478288,
)
_EXPECTED_ALTERNATE_BATCH_POST_OBJECTIVES = (
    -0.0105333736,
    -0.0105405992,
    -0.0105478288,
    -0.0105550605,
)
_EXPECTED_ALTERNATE_PASS_PARAMETER_DELTAS = (
    (0.0000957660, 0.0000207672, 0.0002485136, 0.0000290311),
    (0.0000957745, 0.0000207767, 0.0002485845, 0.0000290377),
    (0.0000957837, 0.0000207842, 0.0002486675, 0.0000290442),
    (0.0000957938, 0.0000207875, 0.0002487414, 0.0000290511),
)
_EXPECTED_ALTERNATE_FINAL_PARAMETER_DELTAS = (
    0.0003831175,
    0.0000831156,
    0.0009945069,
    0.0001161640,
)
_EXPECTED_ALTERNATE_TRAINING_REWARD_SUMS = (
    (130.0, 90.0, 6.0, -286.0),
    (130.0, 90.0, 6.0, -286.0),
    (130.0, 90.0, 6.0, -286.0),
    (130.0, 90.0, 6.0, -286.0),
)
_EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 63, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 90, 51, 81,
    14, 45, 18, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
)
_EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS = (
    37, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
    84, 35, 60, 87, 82, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
)
_EVIDENCE_GRADE = (
    "P8 local exact two-protocol leave-one-out batch-baseline variance diagnostic "
    "evidence only"
)
_WARNINGS = (
    "exact two predeclared training protocols only",
    "each pass collects all 32 trajectories before one aggregate update",
    "each trajectory baseline uses the other 31 same-seat returns only",
    "four passes and four updates per protocol with fixed learning rate 0.01",
    "final zero-update evaluation uses only seeds 52 through 83 and 84 through 115",
    "all outcomes are retained regardless of sign and no protocol is selected",
    "no third protocol, seed search, fifth pass or third evaluation window",
    "no critic, GAE, entropy, KL, clipping, optimizer or rate search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError(
    RuntimeError
):
    """Raised when the exact batch-baseline diagnostic contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult:
    protocol_id: str
    training_seeds_per_pass: Tuple[int, ...]
    pass_count: int
    trajectory_count: int
    update_count: int
    per_pass_transition_counts: Tuple[Tuple[int, ...], ...]
    per_pass_actor_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_legal_action_traces: Tuple[
        Tuple[Tuple[Tuple[int, ...], ...], ...], ...
    ]
    per_pass_cumulative_raw_rewards: Tuple[Tuple[Tuple[float, ...], ...], ...]
    per_pass_final_scores: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_action_trace_sha256: Tuple[Tuple[str, ...], ...]
    per_pass_leave_one_out_seat_baselines: Tuple[
        Tuple[Tuple[float, ...], ...], ...
    ]
    per_pass_advantage_seat_returns: Tuple[
        Tuple[Tuple[float, ...], ...], ...
    ]
    per_pass_initial_trajectory_objectives: Tuple[Tuple[float, ...], ...]
    per_pass_post_update_trajectory_objectives: Tuple[Tuple[float, ...], ...]
    per_pass_batch_initial_objectives: Tuple[float, ...]
    per_pass_batch_post_update_objectives: Tuple[float, ...]
    per_pass_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    final_parameter_delta_l2: Tuple[float, ...]
    final_primary_transition_counts: Tuple[int, ...]
    final_primary_project_action_traces: Tuple[Tuple[int, ...], ...]
    final_primary_raw_rewards: Tuple[float, ...]
    final_primary_final_scores: Tuple[Tuple[int, ...], ...]
    final_replication_transition_counts: Tuple[int, ...]
    final_replication_project_action_traces: Tuple[Tuple[int, ...], ...]
    final_replication_raw_rewards: Tuple[float, ...]
    final_replication_final_scores: Tuple[Tuple[int, ...], ...]
    initial_primary_raw_sum: float
    final_primary_raw_sum: float
    primary_delta_from_initial: float
    initial_replication_raw_sum: float
    final_replication_raw_sum: float
    replication_delta_from_initial: float
    primary_positive_round_count: int
    primary_negative_round_count: int
    replication_positive_round_count: int
    replication_negative_round_count: int
    primary_changed_from_initial_reward_seeds: Tuple[int, ...]
    replication_changed_from_initial_reward_seeds: Tuple[int, ...]
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    parameters_changed: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    pass_count: int
    trajectories_per_pass: int
    learning_rate: float
    primary_evaluation_seeds: Tuple[int, ...]
    replication_evaluation_seeds: Tuple[int, ...]
    reference: MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult
    alternate: MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult
    total_training_trajectory_count: int
    total_training_update_count: int
    evaluation_call_count: int
    evaluation_update_count: int
    all_seed_sets_pairwise_disjoint: bool
    selected_training_protocol_id: Optional[str]
    selected_model_id: Optional[str]
    selected_pass_index: Optional[int]
    selected_checkpoint_id: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


@dataclass(frozen=True)
class _BatchUpdate:
    parameters: tuple
    leave_one_out_seat_baselines: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns: Tuple[Tuple[float, ...], ...]
    initial_trajectory_objectives: Tuple[float, ...]
    post_update_trajectory_objectives: Tuple[float, ...]
    batch_initial_objective: float
    batch_post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]


@dataclass(frozen=True)
class _BatchGradients:
    gradient_sums: tuple
    leave_one_out_seat_baselines: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns: Tuple[Tuple[float, ...], ...]
    decision_advantages: tuple
    initial_trajectory_objectives: Tuple[float, ...]


def _trace_sha256(trace: Tuple[int, ...]) -> str:
    return hashlib.sha256(",".join(map(str, trace)).encode("ascii")).hexdigest()


def _changed_reward_seeds(seeds, before, after):
    return tuple(
        seed
        for seed, before_value, after_value in zip(seeds, before, after)
        if before_value != after_value
    )


def _all_close(actual, expected, tolerance=1e-6):
    if isinstance(expected, tuple):
        return len(actual) == len(expected) and all(
            _all_close(actual_item, expected_item, tolerance)
            for actual_item, expected_item in zip(actual, expected)
        )
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _trajectory_objective(parameters, trajectory, decision_advantages, jax, jnp):
    logits = _mlp_logits(parameters, trajectory.features, jax)
    legal_logits = jnp.where(trajectory.legal_masks, logits, -1e9)
    log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
    selected_log_probabilities = log_probabilities[
        jnp.arange(trajectory.actions.shape[0]),
        trajectory.actions,
    ]
    return -jnp.mean(decision_advantages * selected_log_probabilities)


def _calculate_leave_one_out_batch_gradients(
    parameters,
    trajectories,
    jax,
    jnp,
):
    normalized_returns = tuple(
        tuple(float(value) / 100.0 for value in trajectory.cumulative_rewards)
        for trajectory in trajectories
    )
    seat_sums = tuple(
        sum(row[seat] for row in normalized_returns) for seat in range(4)
    )
    baselines = tuple(
        tuple(
            (seat_sums[seat] - row[seat]) / (_TRAJECTORIES_PER_PASS - 1)
            for seat in range(4)
        )
        for row in normalized_returns
    )
    advantages = tuple(
        tuple(row[seat] - baseline[seat] for seat in range(4))
        for row, baseline in zip(normalized_returns, baselines)
    )

    gradient_sums = tuple(jnp.zeros_like(value) for value in parameters)
    initial_objectives = []
    decision_advantages = []
    for trajectory, seat_advantages in zip(trajectories, advantages):
        actor_advantages = jnp.asarray(seat_advantages, dtype=jnp.float32)[
            trajectory.actors
        ]
        decision_advantages.append(actor_advantages)

        def objective(model_parameters):
            return _trajectory_objective(
                model_parameters,
                trajectory,
                actor_advantages,
                jax,
                jnp,
            )

        initial_objective, gradients = jax.jit(jax.value_and_grad(objective))(
            parameters
        )
        initial_objectives.append(float(initial_objective))
        gradient_sums = tuple(
            total + gradient for total, gradient in zip(gradient_sums, gradients)
        )

    return _BatchGradients(
        gradient_sums=gradient_sums,
        leave_one_out_seat_baselines=baselines,
        advantage_seat_returns=advantages,
        decision_advantages=tuple(decision_advantages),
        initial_trajectory_objectives=tuple(initial_objectives),
    )


def _apply_leave_one_out_batch_update(
    parameters,
    trajectories,
    gradient_multiplier,
    jax,
    jnp,
):
    batch_gradients = _calculate_leave_one_out_batch_gradients(
        parameters,
        trajectories,
        jax,
        jnp,
    )
    mean_gradients = tuple(
        gradient_multiplier * gradient / _TRAJECTORIES_PER_PASS
        for gradient in batch_gradients.gradient_sums
    )
    updated_parameters = jax.block_until_ready(
        tuple(
            value - _LEARNING_RATE * gradient
            for value, gradient in zip(parameters, mean_gradients)
        )
    )
    post_objectives = tuple(
        float(
            _trajectory_objective(
                updated_parameters,
                trajectory,
                actor_advantages,
                jax,
                jnp,
            )
        )
        for trajectory, actor_advantages in zip(
            trajectories,
            batch_gradients.decision_advantages,
        )
    )
    return _BatchUpdate(
        parameters=updated_parameters,
        leave_one_out_seat_baselines=(
            batch_gradients.leave_one_out_seat_baselines
        ),
        advantage_seat_returns=batch_gradients.advantage_seat_returns,
        initial_trajectory_objectives=(
            batch_gradients.initial_trajectory_objectives
        ),
        post_update_trajectory_objectives=post_objectives,
        batch_initial_objective=(
            sum(batch_gradients.initial_trajectory_objectives)
            / _TRAJECTORIES_PER_PASS
        ),
        batch_post_update_objective=(sum(post_objectives) / _TRAJECTORIES_PER_PASS),
        parameter_delta_l2=tuple(
            float(jnp.linalg.norm(updated - initial))
            for initial, updated in zip(parameters, updated_parameters)
        ),
    )


def _run_protocol(
    protocol_id,
    training_seeds,
    initial_parameters,
    environment,
    step_fn,
    rule_policy_fn,
    jax,
    jnp,
    mahjax,
    gradient_multiplier,
):
    parameters = tuple(initial_parameters)
    all_pass_trajectories = []
    updates = []
    for _pass_index in range(_PASS_COUNT):
        pass_parameters = parameters
        trajectories = tuple(
            _collect_all_project_round(seed, pass_parameters, jax, jnp, mahjax)
            for seed in training_seeds
        )
        update = _apply_leave_one_out_batch_update(
            pass_parameters,
            trajectories,
            gradient_multiplier,
            jax,
            jnp,
        )
        all_pass_trajectories.append(trajectories)
        updates.append(update)
        parameters = update.parameters

    final_primary = _evaluate(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
    )
    final_replication = _evaluate(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
    )
    pass_trajectories = tuple(all_pass_trajectories)
    batch_updates = tuple(updates)
    primary_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_primary
    )
    replication_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_replication
    )
    all_training_actions_legal = all(
        action in legal
        for rows in pass_trajectories
        for item in rows
        for action, legal in zip(item.action_trace, item.legal_action_trace)
    )
    all_rounds_terminated = all(
        item.final_scores is not None for rows in pass_trajectories for item in rows
    )
    final_parameter_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    return MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult(
        protocol_id=protocol_id,
        training_seeds_per_pass=training_seeds,
        pass_count=_PASS_COUNT,
        trajectory_count=sum(map(len, pass_trajectories)),
        update_count=len(batch_updates),
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
        per_pass_leave_one_out_seat_baselines=tuple(
            update.leave_one_out_seat_baselines for update in batch_updates
        ),
        per_pass_advantage_seat_returns=tuple(
            update.advantage_seat_returns for update in batch_updates
        ),
        per_pass_initial_trajectory_objectives=tuple(
            update.initial_trajectory_objectives for update in batch_updates
        ),
        per_pass_post_update_trajectory_objectives=tuple(
            update.post_update_trajectory_objectives for update in batch_updates
        ),
        per_pass_batch_initial_objectives=tuple(
            update.batch_initial_objective for update in batch_updates
        ),
        per_pass_batch_post_update_objectives=tuple(
            update.batch_post_update_objective for update in batch_updates
        ),
        per_pass_parameter_delta_l2=tuple(
            update.parameter_delta_l2 for update in batch_updates
        ),
        final_parameter_delta_l2=final_parameter_deltas,
        final_primary_transition_counts=tuple(
            item.transition_count for item in final_primary
        ),
        final_primary_project_action_traces=tuple(
            item.project_action_trace for item in final_primary
        ),
        final_primary_raw_rewards=primary_rewards,
        final_primary_final_scores=tuple(item.final_scores for item in final_primary),
        final_replication_transition_counts=tuple(
            item.transition_count for item in final_replication
        ),
        final_replication_project_action_traces=tuple(
            item.project_action_trace for item in final_replication
        ),
        final_replication_raw_rewards=replication_rewards,
        final_replication_final_scores=tuple(
            item.final_scores for item in final_replication
        ),
        initial_primary_raw_sum=sum(_EXPECTED_INITIAL_EVALUATION_REWARDS),
        final_primary_raw_sum=sum(primary_rewards),
        primary_delta_from_initial=(
            sum(primary_rewards) - sum(_EXPECTED_INITIAL_EVALUATION_REWARDS)
        ),
        initial_replication_raw_sum=sum(_EXPECTED_INITIAL_REPLICATION_REWARDS),
        final_replication_raw_sum=sum(replication_rewards),
        replication_delta_from_initial=(
            sum(replication_rewards) - sum(_EXPECTED_INITIAL_REPLICATION_REWARDS)
        ),
        primary_positive_round_count=sum(value > 0.0 for value in primary_rewards),
        primary_negative_round_count=sum(value < 0.0 for value in primary_rewards),
        replication_positive_round_count=sum(
            value > 0.0 for value in replication_rewards
        ),
        replication_negative_round_count=sum(
            value < 0.0 for value in replication_rewards
        ),
        primary_changed_from_initial_reward_seeds=_changed_reward_seeds(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
            _EXPECTED_INITIAL_EVALUATION_REWARDS,
            primary_rewards,
        ),
        replication_changed_from_initial_reward_seeds=_changed_reward_seeds(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
            _EXPECTED_INITIAL_REPLICATION_REWARDS,
            replication_rewards,
        ),
        all_training_actions_legal=all_training_actions_legal,
        all_rounds_terminated=all_rounds_terminated,
        parameters_changed=all(value > 0.0 for value in final_parameter_deltas),
    )


def run_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke(
) -> MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult:
    """Run exact reference and alternate batch-baseline branches without selection."""

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
        raise MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError(
            "pinned leave-one-out batch diagnostic runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError(
            "leave-one-out batch runtime differs from the pinned contract"
        )

    reference = _run_protocol(
        _REFERENCE_PROTOCOL_ID,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
        initial_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        mahjax,
        1.0,
    )
    alternate = _run_protocol(
        _ALTERNATE_PROTOCOL_ID,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
        initial_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        mahjax,
        1.0,
    )
    seed_sets = (
        set(reference.training_seeds_per_pass),
        set(alternate.training_seeds_per_pass),
        set(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS
        ),
        set(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS
        ),
    )
    pairwise_disjoint = all(
        left.isdisjoint(right)
        for index, left in enumerate(seed_sets)
        for right in seed_sets[index + 1 :]
    )
    reference_training_reward_sums = tuple(
        tuple(sum(row[seat] for row in rows) for seat in range(4))
        for rows in reference.per_pass_cumulative_raw_rewards
    )
    alternate_training_reward_sums = tuple(
        tuple(sum(row[seat] for row in rows) for seat in range(4))
        for rows in alternate.per_pass_cumulative_raw_rewards
    )
    all_advantage_sums_centered = all(
        abs(sum(row[seat] for row in rows)) <= 1e-9
        for branch in (reference, alternate)
        for rows in branch.per_pass_advantage_seat_returns
        for seat in range(4)
    )
    if (
        reference.trajectory_count != 128
        or alternate.trajectory_count != 128
        or reference.update_count != 4
        or alternate.update_count != 4
        or tuple(map(len, reference.per_pass_transition_counts)) != (32,) * 4
        or tuple(map(len, alternate.per_pass_transition_counts)) != (32,) * 4
        or len(reference.final_primary_raw_rewards) != 32
        or len(alternate.final_primary_raw_rewards) != 32
        or len(reference.final_replication_raw_rewards) != 32
        or len(alternate.final_replication_raw_rewards) != 32
        or not pairwise_disjoint
        or not reference.all_training_actions_legal
        or not alternate.all_training_actions_legal
        or not reference.all_rounds_terminated
        or not alternate.all_rounds_terminated
        or not reference.parameters_changed
        or not alternate.parameters_changed
        or not _all_close(
            reference.per_pass_batch_initial_objectives,
            _EXPECTED_REFERENCE_BATCH_INITIAL_OBJECTIVES,
        )
        or not _all_close(
            reference.per_pass_batch_post_update_objectives,
            _EXPECTED_REFERENCE_BATCH_POST_OBJECTIVES,
        )
        or not _all_close(
            reference.per_pass_parameter_delta_l2,
            _EXPECTED_REFERENCE_PASS_PARAMETER_DELTAS,
        )
        or not _all_close(
            reference.final_parameter_delta_l2,
            _EXPECTED_REFERENCE_FINAL_PARAMETER_DELTAS,
        )
        or reference_training_reward_sums
        != _EXPECTED_REFERENCE_TRAINING_REWARD_SUMS
        or not _all_close(
            alternate.per_pass_batch_initial_objectives,
            _EXPECTED_ALTERNATE_BATCH_INITIAL_OBJECTIVES,
        )
        or not _all_close(
            alternate.per_pass_batch_post_update_objectives,
            _EXPECTED_ALTERNATE_BATCH_POST_OBJECTIVES,
        )
        or not _all_close(
            alternate.per_pass_parameter_delta_l2,
            _EXPECTED_ALTERNATE_PASS_PARAMETER_DELTAS,
        )
        or not _all_close(
            alternate.final_parameter_delta_l2,
            _EXPECTED_ALTERNATE_FINAL_PARAMETER_DELTAS,
        )
        or alternate_training_reward_sums
        != _EXPECTED_ALTERNATE_TRAINING_REWARD_SUMS
        or not all_advantage_sums_centered
        or reference.final_primary_raw_rewards
        != _EXPECTED_INITIAL_EVALUATION_REWARDS
        or alternate.final_primary_raw_rewards
        != _EXPECTED_INITIAL_EVALUATION_REWARDS
        or reference.final_replication_raw_rewards
        != _EXPECTED_INITIAL_REPLICATION_REWARDS
        or alternate.final_replication_raw_rewards
        != _EXPECTED_INITIAL_REPLICATION_REWARDS
        or reference.final_primary_transition_counts
        != _EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS
        or alternate.final_primary_transition_counts
        != _EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS
        or reference.final_replication_transition_counts
        != _EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS
        or alternate.final_replication_transition_counts
        != _EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS
    ):
        raise MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError(
            "leave-one-out batch diagnostic differs from the approved contract"
        )

    return MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_TRAINING_PROTOCOL_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        pass_count=_PASS_COUNT,
        trajectories_per_pass=_TRAJECTORIES_PER_PASS,
        learning_rate=_LEARNING_RATE,
        primary_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS
        ),
        replication_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS
        ),
        reference=reference,
        alternate=alternate,
        total_training_trajectory_count=(
            reference.trajectory_count + alternate.trajectory_count
        ),
        total_training_update_count=reference.update_count + alternate.update_count,
        evaluation_call_count=4,
        evaluation_update_count=0,
        all_seed_sets_pairwise_disjoint=pairwise_disjoint,
        selected_training_protocol_id=None,
        selected_model_id=None,
        selected_pass_index=None,
        selected_checkpoint_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_TRAINING_PROTOCOL_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolSmokeError",
    "MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult",
    "MahJaxCategoricalMlpFourPassLeaveOneOutBatchTrainingProtocolResult",
    "run_mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke",
]
