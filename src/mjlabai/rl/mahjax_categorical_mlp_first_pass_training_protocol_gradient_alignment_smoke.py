"""Measure first-pass aggregate-gradient alignment for two fixed protocols."""

from __future__ import annotations

from dataclasses import dataclass
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
from mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke import (  # noqa: E501
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
    _calculate_leave_one_out_batch_gradients,
    _trace_sha256,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FIRST_PASS_TRAINING_PROTOCOL_GRADIENT_ALIGNMENT_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke_v0.1"
)

_TRAJECTORIES_PER_PROTOCOL = 32
_REFERENCE_PROTOCOL_ID = "reference_ordered_0_31_first_pass_gradient"
_ALTERNATE_PROTOCOL_ID = "alternate_ordered_116_147_first_pass_gradient"
_EXPECTED_REFERENCE_TRANSITION_COUNTS = (
    92, 77, 90, 84, 84, 83, 92, 81, 82, 86, 86, 84, 91, 90, 89, 83,
    81, 88, 85, 81, 89, 83, 83, 83, 71, 57, 82, 71, 86, 81, 83, 81,
)
_EXPECTED_ALTERNATE_TRANSITION_COUNTS = (
    85, 85, 90, 90, 95, 86, 90, 96, 43, 86, 86, 66, 74, 76, 82, 87,
    87, 87, 81, 90, 85, 82, 84, 88, 91, 85, 93, 88, 87, 85, 87, 82,
)
_EXPECTED_REFERENCE_REWARD_SUMS = (-55.0, -34.0, -150.0, 179.0)
_EXPECTED_ALTERNATE_REWARD_SUMS = (130.0, 90.0, 6.0, -286.0)
_EXPECTED_REFERENCE_BATCH_OBJECTIVE = -0.008504558742060908
_EXPECTED_ALTERNATE_BATCH_OBJECTIVE = -0.010526151631779612
_EXPECTED_REFERENCE_GROUP_GRADIENT_L2 = (
    0.010686613619327545,
    0.001964464085176587,
    0.026142027229070663,
    0.0029551691841334105,
)
_EXPECTED_ALTERNATE_GROUP_GRADIENT_L2 = (
    0.009576422162353992,
    0.002076641656458378,
    0.024850960820913315,
    0.002903012791648507,
)
_EXPECTED_REFERENCE_GLOBAL_GRADIENT_L2 = 0.028464037702741144
_EXPECTED_ALTERNATE_GLOBAL_GRADIENT_L2 = 0.026870393353875678
_EXPECTED_GLOBAL_GRADIENT_DOT_PRODUCT = -0.0001429308561853304
_EXPECTED_GLOBAL_GRADIENT_COSINE_SIMILARITY = -0.18687683284469966
_EVIDENCE_GRADE = (
    "P8 local exact first-pass two-protocol aggregate-gradient alignment "
    "diagnostic evidence only"
)
_WARNINGS = (
    "exact two predeclared training protocols from identical initial parameters",
    "one frozen-policy batch of 32 trajectories per protocol only",
    "each trajectory baseline uses the other 31 same-seat returns only",
    "aggregate mean gradients are measured without applying an update",
    "no primary, replication or other policy evaluation is performed",
    "all outcomes are retained regardless of cosine sign or magnitude",
    "no protocol, model, multiplier, pass, checkpoint or direction is selected",
    "no scale, rate, optimizer, exploration, seed or protocol search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError(
    RuntimeError
):
    """Raised when the exact gradient-alignment contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpFirstPassProtocolGradientResult:
    protocol_id: str
    training_seeds: Tuple[int, ...]
    trajectory_count: int
    transition_counts: Tuple[int, ...]
    actor_traces: Tuple[Tuple[int, ...], ...]
    action_traces: Tuple[Tuple[int, ...], ...]
    legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    final_scores: Tuple[Tuple[int, ...], ...]
    action_trace_sha256: Tuple[str, ...]
    leave_one_out_seat_baselines: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns: Tuple[Tuple[float, ...], ...]
    initial_trajectory_objectives: Tuple[float, ...]
    batch_initial_objective: float
    parameter_group_shapes: Tuple[Tuple[int, ...], ...]
    parameter_group_gradient_l2: Tuple[float, ...]
    global_gradient_l2: float
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    all_advantage_sums_centered: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    trajectories_per_protocol: int
    total_training_trajectory_count: int
    training_update_count: int
    evaluation_call_count: int
    evaluation_update_count: int
    reference: MahJaxCategoricalMlpFirstPassProtocolGradientResult
    alternate: MahJaxCategoricalMlpFirstPassProtocolGradientResult
    global_gradient_dot_product: float
    global_gradient_cosine_similarity: float
    all_gradient_values_finite: bool
    both_global_gradients_nonzero: bool
    selected_training_protocol_id: Optional[str]
    selected_model_id: Optional[str]
    selected_multiplier: Optional[float]
    selected_pass_index: Optional[int]
    selected_checkpoint_id: Optional[str]
    selected_gradient_direction: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _all_close(actual, expected, tolerance=1e-6):
    if isinstance(expected, tuple):
        return len(actual) == len(expected) and all(
            _all_close(actual_item, expected_item, tolerance)
            for actual_item, expected_item in zip(actual, expected)
        )
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _summarize_protocol(
    protocol_id,
    training_seeds,
    initial_parameters,
    jax,
    jnp,
    mahjax,
):
    trajectories = tuple(
        _collect_all_project_round(seed, initial_parameters, jax, jnp, mahjax)
        for seed in training_seeds
    )
    batch_gradients = _calculate_leave_one_out_batch_gradients(
        initial_parameters,
        trajectories,
        jax,
        jnp,
    )
    mean_gradients = tuple(
        jax.block_until_ready(gradient / _TRAJECTORIES_PER_PROTOCOL)
        for gradient in batch_gradients.gradient_sums
    )
    group_norms = tuple(float(jnp.linalg.norm(value)) for value in mean_gradients)
    global_norm = math.sqrt(sum(value * value for value in group_norms))
    all_actions_legal = all(
        action in legal
        for trajectory in trajectories
        for action, legal in zip(
            trajectory.action_trace,
            trajectory.legal_action_trace,
        )
    )
    all_terminated = all(
        trajectory.final_scores is not None for trajectory in trajectories
    )
    all_advantages_centered = all(
        abs(sum(row[seat] for row in batch_gradients.advantage_seat_returns))
        <= 1e-9
        for seat in range(4)
    )
    summary = MahJaxCategoricalMlpFirstPassProtocolGradientResult(
        protocol_id=protocol_id,
        training_seeds=training_seeds,
        trajectory_count=len(trajectories),
        transition_counts=tuple(
            len(trajectory.action_trace) for trajectory in trajectories
        ),
        actor_traces=tuple(trajectory.actor_trace for trajectory in trajectories),
        action_traces=tuple(trajectory.action_trace for trajectory in trajectories),
        legal_action_traces=tuple(
            trajectory.legal_action_trace for trajectory in trajectories
        ),
        cumulative_raw_rewards=tuple(
            trajectory.cumulative_rewards for trajectory in trajectories
        ),
        final_scores=tuple(trajectory.final_scores for trajectory in trajectories),
        action_trace_sha256=tuple(
            _trace_sha256(trajectory.action_trace) for trajectory in trajectories
        ),
        leave_one_out_seat_baselines=(
            batch_gradients.leave_one_out_seat_baselines
        ),
        advantage_seat_returns=batch_gradients.advantage_seat_returns,
        initial_trajectory_objectives=(
            batch_gradients.initial_trajectory_objectives
        ),
        batch_initial_objective=(
            sum(batch_gradients.initial_trajectory_objectives)
            / _TRAJECTORIES_PER_PROTOCOL
        ),
        parameter_group_shapes=tuple(
            tuple(value.shape) for value in initial_parameters
        ),
        parameter_group_gradient_l2=group_norms,
        global_gradient_l2=global_norm,
        all_training_actions_legal=all_actions_legal,
        all_rounds_terminated=all_terminated,
        all_advantage_sums_centered=all_advantages_centered,
    )
    return summary, mean_gradients


def run_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke(
) -> MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult:
    """Measure exact first-pass gradient agreement without update or evaluation."""

    try:
        jax, jnp, initial_parameters, _ = _train_mahjax_categorical_mlp_parameters()
        _, _, mahjax = _load_pinned_runtime()
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError(
            "pinned first-pass gradient-alignment runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError(
            "first-pass gradient-alignment runtime differs from the pinned contract"
        )

    reference, reference_gradients = _summarize_protocol(
        _REFERENCE_PROTOCOL_ID,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
        initial_parameters,
        jax,
        jnp,
        mahjax,
    )
    alternate, alternate_gradients = _summarize_protocol(
        _ALTERNATE_PROTOCOL_ID,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
        initial_parameters,
        jax,
        jnp,
        mahjax,
    )
    dot_product = sum(
        float(jnp.vdot(reference_value, alternate_value))
        for reference_value, alternate_value in zip(
            reference_gradients,
            alternate_gradients,
        )
    )
    denominator = reference.global_gradient_l2 * alternate.global_gradient_l2
    cosine = dot_product / denominator if denominator > 0.0 else math.nan
    reference_reward_sums = tuple(
        sum(row[seat] for row in reference.cumulative_raw_rewards)
        for seat in range(4)
    )
    alternate_reward_sums = tuple(
        sum(row[seat] for row in alternate.cumulative_raw_rewards)
        for seat in range(4)
    )
    scalar_diagnostics = (
        *reference.parameter_group_gradient_l2,
        reference.global_gradient_l2,
        *alternate.parameter_group_gradient_l2,
        alternate.global_gradient_l2,
        dot_product,
        cosine,
    )
    all_finite = all(math.isfinite(value) for value in scalar_diagnostics)
    both_nonzero = denominator > 0.0
    if (
        reference.trajectory_count != _TRAJECTORIES_PER_PROTOCOL
        or alternate.trajectory_count != _TRAJECTORIES_PER_PROTOCOL
        or reference.training_seeds != tuple(range(32))
        or alternate.training_seeds != tuple(range(116, 148))
        or set(reference.training_seeds) & set(alternate.training_seeds)
        or reference.parameter_group_shapes != alternate.parameter_group_shapes
        or not reference.all_training_actions_legal
        or not alternate.all_training_actions_legal
        or not reference.all_rounds_terminated
        or not alternate.all_rounds_terminated
        or not reference.all_advantage_sums_centered
        or not alternate.all_advantage_sums_centered
        or not all_finite
        or not both_nonzero
        or cosine < -1.000001
        or cosine > 1.000001
        or reference.transition_counts != _EXPECTED_REFERENCE_TRANSITION_COUNTS
        or alternate.transition_counts != _EXPECTED_ALTERNATE_TRANSITION_COUNTS
        or reference_reward_sums != _EXPECTED_REFERENCE_REWARD_SUMS
        or alternate_reward_sums != _EXPECTED_ALTERNATE_REWARD_SUMS
        or not _all_close(
            reference.batch_initial_objective,
            _EXPECTED_REFERENCE_BATCH_OBJECTIVE,
        )
        or not _all_close(
            alternate.batch_initial_objective,
            _EXPECTED_ALTERNATE_BATCH_OBJECTIVE,
        )
        or not _all_close(
            reference.parameter_group_gradient_l2,
            _EXPECTED_REFERENCE_GROUP_GRADIENT_L2,
        )
        or not _all_close(
            alternate.parameter_group_gradient_l2,
            _EXPECTED_ALTERNATE_GROUP_GRADIENT_L2,
        )
        or not _all_close(
            reference.global_gradient_l2,
            _EXPECTED_REFERENCE_GLOBAL_GRADIENT_L2,
        )
        or not _all_close(
            alternate.global_gradient_l2,
            _EXPECTED_ALTERNATE_GLOBAL_GRADIENT_L2,
        )
        or not _all_close(
            dot_product,
            _EXPECTED_GLOBAL_GRADIENT_DOT_PRODUCT,
            tolerance=1e-8,
        )
        or not _all_close(
            cosine,
            _EXPECTED_GLOBAL_GRADIENT_COSINE_SIMILARITY,
        )
    ):
        raise MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError(
            "first-pass gradient-alignment diagnostic differs from the approved contract"
        )

    return MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_TRAINING_PROTOCOL_GRADIENT_ALIGNMENT_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        trajectories_per_protocol=_TRAJECTORIES_PER_PROTOCOL,
        total_training_trajectory_count=(
            reference.trajectory_count + alternate.trajectory_count
        ),
        training_update_count=0,
        evaluation_call_count=0,
        evaluation_update_count=0,
        reference=reference,
        alternate=alternate,
        global_gradient_dot_product=dot_product,
        global_gradient_cosine_similarity=cosine,
        all_gradient_values_finite=all_finite,
        both_global_gradients_nonzero=both_nonzero,
        selected_training_protocol_id=None,
        selected_model_id=None,
        selected_multiplier=None,
        selected_pass_index=None,
        selected_checkpoint_id=None,
        selected_gradient_direction=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_TRAINING_PROTOCOL_GRADIENT_ALIGNMENT_SMOKE_VERSION",
    "MahJaxCategoricalMlpFirstPassProtocolGradientResult",
    "MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentSmokeError",
    "MahJaxCategoricalMlpFirstPassTrainingProtocolGradientAlignmentResult",
    "run_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke",
]
