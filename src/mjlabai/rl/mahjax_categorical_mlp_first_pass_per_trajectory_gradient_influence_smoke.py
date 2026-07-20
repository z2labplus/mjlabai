"""Measure each fixed trajectory gradient against two protocol aggregates."""

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


MAHJAX_CATEGORICAL_MLP_FIRST_PASS_PER_TRAJECTORY_GRADIENT_INFLUENCE_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke_v0.1"
)

_TRAJECTORIES_PER_PROTOCOL = 32
_REFERENCE_PROTOCOL_ID = "reference_ordered_0_31_per_trajectory_influence"
_ALTERNATE_PROTOCOL_ID = "alternate_ordered_116_147_per_trajectory_influence"
_EXPECTED_AGGREGATE_DOT_PRODUCT = -0.0001429308561853304
_EXPECTED_AGGREGATE_COSINE_SIMILARITY = -0.18687683284469966
_EXPECTED_REFERENCE_OWN_ALIGNMENT_SIGN_COUNTS = (13, 0, 19)
_EXPECTED_REFERENCE_OPPOSITE_ALIGNMENT_SIGN_COUNTS = (14, 0, 18)
_EXPECTED_ALTERNATE_OWN_ALIGNMENT_SIGN_COUNTS = (7, 0, 25)
_EXPECTED_ALTERNATE_OPPOSITE_ALIGNMENT_SIGN_COUNTS = (18, 0, 14)
_EXPECTED_REFERENCE_MAGNITUDE_CONCENTRATION = (
    -0.004573782261788395,
    -0.00014293069568088734,
    0.006063447269466948,
    0.010637229531255343,
    0.01670067680072229,
    0.27386807830390336,
    0.08289576975151124,
    12.063341748289508,
    0.16033531920600053,
    0.4870449948159291,
    0.7174696416854126,
)
_EXPECTED_ALTERNATE_MAGNITUDE_CONCENTRATION = (
    -0.004573783610487325,
    -0.00014293073782772892,
    0.002875172451524577,
    0.007448956062011902,
    0.010324128513536479,
    0.4430188566996633,
    0.19403830510218845,
    5.153621597928097,
    0.4158428046888921,
    0.5942865543230846,
    0.7457630373122845,
)
_EXPECTED_UNIT_NORM_AGGREGATE_ALIGNMENT = (
    (
        0.0641569197177887,
        0.011721663177013397,
        0.15103819966316223,
        0.01764390990138054,
    ),
    0.16546103181537164,
    (
        0.07713237404823303,
        0.019064467400312424,
        0.2229359894990921,
        0.024948330596089363,
    ),
    0.23798262889766802,
    0.00927360774949193,
    0.2355091236577188,
)
_EVIDENCE_GRADE = (
    "P8 local exact first-pass per-trajectory cross-protocol gradient influence "
    "diagnostic evidence only"
)
_WARNINGS = (
    "exact two predeclared first-pass batches from identical initial parameters",
    "all 64 already-computed other-31 trajectory gradients are retained",
    "each trajectory is compared with own and opposite aggregate mean gradients",
    "unit-norm aggregation weights every one of the same 64 gradients equally",
    "unit-norm geometry is objective-scale diagnosis, not an approved update rule",
    "negative, zero and positive signs are descriptive and no threshold is searched",
    "no trajectory is ranked, removed, clipped, selected or promoted",
    "zero parameter updates and zero policy evaluations",
    "no third protocol, seed search, additional window or real data",
    "no projection, rate, optimizer, entropy, temperature or exploration search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError(
    RuntimeError
):
    """Raised when the exact per-trajectory influence contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpTrajectoryGradientInfluenceResult:
    protocol_id: str
    seed: int
    transition_count: int
    action_trace_sha256: str
    cumulative_raw_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    parameter_group_gradient_l2: Tuple[float, ...]
    global_gradient_l2: float
    own_aggregate_dot_product: float
    own_aggregate_cosine_similarity: Optional[float]
    opposite_aggregate_dot_product: float
    opposite_aggregate_cosine_similarity: Optional[float]
    all_values_finite: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult:
    contribution_count: int
    signed_sum: float
    signed_mean: float
    positive_sum: float
    absolute_negative_sum: float
    absolute_sum: float
    net_cancellation_ratio: Optional[float]
    absolute_contribution_hhi: Optional[float]
    effective_contribution_count: Optional[float]
    largest_absolute_share: Optional[float]
    top_four_absolute_share: Optional[float]
    top_eight_absolute_share: Optional[float]


@dataclass(frozen=True)
class MahJaxCategoricalMlpUnitNormAggregateAlignmentResult:
    contribution_count_per_protocol: int
    reference_parameter_group_gradient_l2: Tuple[float, ...]
    reference_global_gradient_l2: float
    alternate_parameter_group_gradient_l2: Tuple[float, ...]
    alternate_global_gradient_l2: float
    cross_protocol_dot_product: float
    cross_protocol_cosine_similarity: Optional[float]
    all_source_gradients_finite_and_nonzero: bool
    all_values_finite: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult:
    protocol_id: str
    training_seeds: Tuple[int, ...]
    trajectory_count: int
    parameter_group_shapes: Tuple[Tuple[int, ...], ...]
    aggregate_parameter_group_gradient_l2: Tuple[float, ...]
    aggregate_global_gradient_l2: float
    batch_initial_objective: float
    transition_counts: Tuple[int, ...]
    action_trace_sha256: Tuple[str, ...]
    cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    final_scores: Tuple[Tuple[int, ...], ...]
    leave_one_out_seat_baselines: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns: Tuple[Tuple[float, ...], ...]
    initial_trajectory_objectives: Tuple[float, ...]
    trajectories: Tuple[MahJaxCategoricalMlpTrajectoryGradientInfluenceResult, ...]
    own_alignment_sign_counts: Tuple[int, int, int]
    opposite_alignment_sign_counts: Tuple[int, int, int]
    opposite_alignment_magnitude_concentration: (
        MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult
    )
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    all_advantage_sums_centered: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    trajectories_per_protocol: int
    total_training_trajectory_count: int
    training_update_count: int
    evaluation_call_count: int
    evaluation_update_count: int
    reference: MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult
    alternate: MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult
    aggregate_global_gradient_dot_product: float
    aggregate_global_gradient_cosine_similarity: float
    unit_norm_aggregate_alignment: (
        MahJaxCategoricalMlpUnitNormAggregateAlignmentResult
    )
    selected_training_protocol_id: Optional[str]
    selected_model_id: Optional[str]
    selected_trajectory_seed: Optional[int]
    selected_gradient_direction: Optional[str]
    selected_checkpoint_id: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


@dataclass(frozen=True)
class _CollectedProtocolGradients:
    protocol_id: str
    training_seeds: Tuple[int, ...]
    trajectories: tuple
    batch_gradients: object
    mean_gradients: tuple
    parameter_group_shapes: Tuple[Tuple[int, ...], ...]
    aggregate_parameter_group_gradient_l2: Tuple[float, ...]
    aggregate_global_gradient_l2: float
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    all_advantage_sums_centered: bool


def _group_norms(values, jnp):
    return tuple(float(jnp.linalg.norm(value)) for value in values)


def _global_norm(group_norms):
    return math.sqrt(sum(value * value for value in group_norms))


def _dot(left, right, jnp):
    return sum(float(jnp.vdot(a, b)) for a, b in zip(left, right))


def _cosine(dot_product, left_norm, right_norm):
    denominator = left_norm * right_norm
    return dot_product / denominator if denominator > 0.0 else None


def _alignment_sign_counts(values):
    return (
        sum(value < 0.0 for value in values),
        sum(value == 0.0 for value in values),
        sum(value > 0.0 for value in values),
    )


def _all_finite(values):
    return all(value is None or math.isfinite(value) for value in values)


def _summary_all_finite(summary):
    return _all_finite(tuple(vars(summary).values()))


def _magnitude_values(summary):
    return (
        summary.signed_sum,
        summary.signed_mean,
        summary.positive_sum,
        summary.absolute_negative_sum,
        summary.absolute_sum,
        summary.net_cancellation_ratio,
        summary.absolute_contribution_hhi,
        summary.effective_contribution_count,
        summary.largest_absolute_share,
        summary.top_four_absolute_share,
        summary.top_eight_absolute_share,
    )


def _build_magnitude_concentration(values):
    signed_sum = sum(values)
    positive_sum = sum(value for value in values if value > 0.0)
    absolute_negative_sum = -sum(value for value in values if value < 0.0)
    absolute_values = tuple(abs(value) for value in values)
    absolute_sum = sum(absolute_values)
    if absolute_sum > 0.0:
        shares = tuple(
            value / absolute_sum for value in sorted(absolute_values, reverse=True)
        )
        hhi = sum(value * value for value in shares)
        cancellation = abs(signed_sum) / absolute_sum
        effective_count = 1.0 / hhi if hhi > 0.0 else None
        largest_share = shares[0]
        top_four_share = sum(shares[:4])
        top_eight_share = sum(shares[:8])
    else:
        hhi = None
        cancellation = None
        effective_count = None
        largest_share = None
        top_four_share = None
        top_eight_share = None
    return MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult(
        contribution_count=len(values),
        signed_sum=signed_sum,
        signed_mean=signed_sum / len(values),
        positive_sum=positive_sum,
        absolute_negative_sum=absolute_negative_sum,
        absolute_sum=absolute_sum,
        net_cancellation_ratio=cancellation,
        absolute_contribution_hhi=hhi,
        effective_contribution_count=effective_count,
        largest_absolute_share=largest_share,
        top_four_absolute_share=top_four_share,
        top_eight_absolute_share=top_eight_share,
    )


def _unit_norm_mean_gradients(collected, jax, jnp):
    normalized_trajectory_gradients = []
    source_norms = []
    for gradients in collected.batch_gradients.trajectory_gradients:
        group_norms = _group_norms(gradients, jnp)
        global_norm = _global_norm(group_norms)
        if not math.isfinite(global_norm) or global_norm <= 0.0:
            raise MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError(
                "unit-norm aggregate source gradient must be finite and nonzero"
            )
        source_norms.append(global_norm)
        normalized_trajectory_gradients.append(
            tuple(
                jax.block_until_ready(value / global_norm)
                for value in gradients
            )
        )
    mean_gradients = tuple(
        jax.block_until_ready(
            sum(group_values) / _TRAJECTORIES_PER_PROTOCOL
        )
        for group_values in zip(*normalized_trajectory_gradients)
    )
    return mean_gradients, tuple(source_norms)


def _build_unit_norm_aggregate_alignment(reference, alternate, jax, jnp):
    reference_mean, reference_source_norms = _unit_norm_mean_gradients(
        reference,
        jax,
        jnp,
    )
    alternate_mean, alternate_source_norms = _unit_norm_mean_gradients(
        alternate,
        jax,
        jnp,
    )
    reference_group_norms = _group_norms(reference_mean, jnp)
    alternate_group_norms = _group_norms(alternate_mean, jnp)
    reference_global_norm = _global_norm(reference_group_norms)
    alternate_global_norm = _global_norm(alternate_group_norms)
    dot_product = _dot(reference_mean, alternate_mean, jnp)
    cosine_similarity = _cosine(
        dot_product,
        reference_global_norm,
        alternate_global_norm,
    )
    values = (
        *reference_group_norms,
        reference_global_norm,
        *alternate_group_norms,
        alternate_global_norm,
        dot_product,
        cosine_similarity,
    )
    return MahJaxCategoricalMlpUnitNormAggregateAlignmentResult(
        contribution_count_per_protocol=_TRAJECTORIES_PER_PROTOCOL,
        reference_parameter_group_gradient_l2=reference_group_norms,
        reference_global_gradient_l2=reference_global_norm,
        alternate_parameter_group_gradient_l2=alternate_group_norms,
        alternate_global_gradient_l2=alternate_global_norm,
        cross_protocol_dot_product=dot_product,
        cross_protocol_cosine_similarity=cosine_similarity,
        all_source_gradients_finite_and_nonzero=all(
            math.isfinite(value) and value > 0.0
            for value in (*reference_source_norms, *alternate_source_norms)
        ),
        all_values_finite=_all_finite(values),
    )


def _unit_norm_alignment_values(summary):
    return (
        *summary.reference_parameter_group_gradient_l2,
        summary.reference_global_gradient_l2,
        *summary.alternate_parameter_group_gradient_l2,
        summary.alternate_global_gradient_l2,
        summary.cross_protocol_dot_product,
        summary.cross_protocol_cosine_similarity,
    )


def _collect_protocol_gradients(
    protocol_id,
    training_seeds,
    parameters,
    jax,
    jnp,
    mahjax,
):
    trajectories = tuple(
        _collect_all_project_round(seed, parameters, jax, jnp, mahjax)
        for seed in training_seeds
    )
    batch_gradients = _calculate_leave_one_out_batch_gradients(
        parameters,
        trajectories,
        jax,
        jnp,
    )
    mean_gradients = tuple(
        jax.block_until_ready(gradient / _TRAJECTORIES_PER_PROTOCOL)
        for gradient in batch_gradients.gradient_sums
    )
    group_norms = _group_norms(mean_gradients, jnp)
    return _CollectedProtocolGradients(
        protocol_id=protocol_id,
        training_seeds=training_seeds,
        trajectories=trajectories,
        batch_gradients=batch_gradients,
        mean_gradients=mean_gradients,
        parameter_group_shapes=tuple(tuple(value.shape) for value in parameters),
        aggregate_parameter_group_gradient_l2=group_norms,
        aggregate_global_gradient_l2=_global_norm(group_norms),
        all_training_actions_legal=all(
            action in legal
            for trajectory in trajectories
            for action, legal in zip(
                trajectory.action_trace,
                trajectory.legal_action_trace,
            )
        ),
        all_rounds_terminated=all(
            trajectory.final_scores is not None for trajectory in trajectories
        ),
        all_advantage_sums_centered=all(
            abs(
                sum(
                    row[seat]
                    for row in batch_gradients.advantage_seat_returns
                )
            )
            <= 1e-9
            for seat in range(4)
        ),
    )


def _build_protocol_result(collected, opposite, jnp):
    trajectory_results = []
    for seed, trajectory, gradients in zip(
        collected.training_seeds,
        collected.trajectories,
        collected.batch_gradients.trajectory_gradients,
    ):
        group_norms = _group_norms(gradients, jnp)
        global_norm = _global_norm(group_norms)
        own_dot = _dot(gradients, collected.mean_gradients, jnp)
        opposite_dot = _dot(gradients, opposite.mean_gradients, jnp)
        own_cosine = _cosine(
            own_dot,
            global_norm,
            collected.aggregate_global_gradient_l2,
        )
        opposite_cosine = _cosine(
            opposite_dot,
            global_norm,
            opposite.aggregate_global_gradient_l2,
        )
        trajectory_results.append(
            MahJaxCategoricalMlpTrajectoryGradientInfluenceResult(
                protocol_id=collected.protocol_id,
                seed=seed,
                transition_count=len(trajectory.action_trace),
                action_trace_sha256=_trace_sha256(trajectory.action_trace),
                cumulative_raw_rewards=trajectory.cumulative_rewards,
                final_scores=trajectory.final_scores,
                parameter_group_gradient_l2=group_norms,
                global_gradient_l2=global_norm,
                own_aggregate_dot_product=own_dot,
                own_aggregate_cosine_similarity=own_cosine,
                opposite_aggregate_dot_product=opposite_dot,
                opposite_aggregate_cosine_similarity=opposite_cosine,
                all_values_finite=_all_finite(
                    (
                        *group_norms,
                        global_norm,
                        own_dot,
                        own_cosine,
                        opposite_dot,
                        opposite_cosine,
                    )
                ),
            )
        )
    public_trajectories = tuple(trajectory_results)
    opposite_dots = tuple(
        item.opposite_aggregate_dot_product for item in public_trajectories
    )
    return MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult(
        protocol_id=collected.protocol_id,
        training_seeds=collected.training_seeds,
        trajectory_count=len(collected.trajectories),
        parameter_group_shapes=collected.parameter_group_shapes,
        aggregate_parameter_group_gradient_l2=(
            collected.aggregate_parameter_group_gradient_l2
        ),
        aggregate_global_gradient_l2=collected.aggregate_global_gradient_l2,
        batch_initial_objective=(
            sum(collected.batch_gradients.initial_trajectory_objectives)
            / _TRAJECTORIES_PER_PROTOCOL
        ),
        transition_counts=tuple(
            len(trajectory.action_trace) for trajectory in collected.trajectories
        ),
        action_trace_sha256=tuple(
            _trace_sha256(trajectory.action_trace)
            for trajectory in collected.trajectories
        ),
        cumulative_raw_rewards=tuple(
            trajectory.cumulative_rewards for trajectory in collected.trajectories
        ),
        final_scores=tuple(
            trajectory.final_scores for trajectory in collected.trajectories
        ),
        leave_one_out_seat_baselines=(
            collected.batch_gradients.leave_one_out_seat_baselines
        ),
        advantage_seat_returns=collected.batch_gradients.advantage_seat_returns,
        initial_trajectory_objectives=(
            collected.batch_gradients.initial_trajectory_objectives
        ),
        trajectories=public_trajectories,
        own_alignment_sign_counts=_alignment_sign_counts(
            tuple(item.own_aggregate_dot_product for item in public_trajectories)
        ),
        opposite_alignment_sign_counts=_alignment_sign_counts(
            opposite_dots
        ),
        opposite_alignment_magnitude_concentration=(
            _build_magnitude_concentration(opposite_dots)
        ),
        all_training_actions_legal=collected.all_training_actions_legal,
        all_rounds_terminated=collected.all_rounds_terminated,
        all_advantage_sums_centered=collected.all_advantage_sums_centered,
    )


def run_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke(
) -> MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult:
    """Measure exact individual influence without update or evaluation."""

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
        raise MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError(
            "pinned per-trajectory gradient-influence runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError(
            "per-trajectory gradient-influence runtime differs from the pinned contract"
        )

    reference_collected = _collect_protocol_gradients(
        _REFERENCE_PROTOCOL_ID,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
        initial_parameters,
        jax,
        jnp,
        mahjax,
    )
    alternate_collected = _collect_protocol_gradients(
        _ALTERNATE_PROTOCOL_ID,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
        initial_parameters,
        jax,
        jnp,
        mahjax,
    )
    reference = _build_protocol_result(reference_collected, alternate_collected, jnp)
    alternate = _build_protocol_result(alternate_collected, reference_collected, jnp)
    aggregate_dot = _dot(
        reference_collected.mean_gradients,
        alternate_collected.mean_gradients,
        jnp,
    )
    aggregate_cosine = _cosine(
        aggregate_dot,
        reference.aggregate_global_gradient_l2,
        alternate.aggregate_global_gradient_l2,
    )
    unit_norm_alignment = _build_unit_norm_aggregate_alignment(
        reference_collected,
        alternate_collected,
        jax,
        jnp,
    )
    contract_satisfied = (
        reference.training_seeds == tuple(range(32))
        and alternate.training_seeds == tuple(range(116, 148))
        and not set(reference.training_seeds) & set(alternate.training_seeds)
        and reference.trajectory_count == _TRAJECTORIES_PER_PROTOCOL
        and alternate.trajectory_count == _TRAJECTORIES_PER_PROTOCOL
        and reference.parameter_group_shapes == alternate.parameter_group_shapes
        and reference.all_training_actions_legal
        and alternate.all_training_actions_legal
        and reference.all_rounds_terminated
        and alternate.all_rounds_terminated
        and reference.all_advantage_sums_centered
        and alternate.all_advantage_sums_centered
        and all(item.all_values_finite for item in reference.trajectories)
        and all(item.all_values_finite for item in alternate.trajectories)
        and all(item.global_gradient_l2 > 0.0 for item in reference.trajectories)
        and all(item.global_gradient_l2 > 0.0 for item in alternate.trajectories)
        and sum(reference.own_alignment_sign_counts) == 32
        and sum(reference.opposite_alignment_sign_counts) == 32
        and sum(alternate.own_alignment_sign_counts) == 32
        and sum(alternate.opposite_alignment_sign_counts) == 32
        and reference.own_alignment_sign_counts
        == _EXPECTED_REFERENCE_OWN_ALIGNMENT_SIGN_COUNTS
        and reference.opposite_alignment_sign_counts
        == _EXPECTED_REFERENCE_OPPOSITE_ALIGNMENT_SIGN_COUNTS
        and alternate.own_alignment_sign_counts
        == _EXPECTED_ALTERNATE_OWN_ALIGNMENT_SIGN_COUNTS
        and alternate.opposite_alignment_sign_counts
        == _EXPECTED_ALTERNATE_OPPOSITE_ALIGNMENT_SIGN_COUNTS
        and reference.opposite_alignment_magnitude_concentration.contribution_count
        == 32
        and alternate.opposite_alignment_magnitude_concentration.contribution_count
        == 32
        and abs(
            reference.opposite_alignment_magnitude_concentration.signed_mean
            - aggregate_dot
        )
        <= 1e-8
        and abs(
            alternate.opposite_alignment_magnitude_concentration.signed_mean
            - aggregate_dot
        )
        <= 1e-8
        and _summary_all_finite(
            reference.opposite_alignment_magnitude_concentration
        )
        and _summary_all_finite(
            alternate.opposite_alignment_magnitude_concentration
        )
        and all(
            abs(actual - expected) <= 1e-6
            for actual, expected in zip(
                _magnitude_values(
                    reference.opposite_alignment_magnitude_concentration
                ),
                _EXPECTED_REFERENCE_MAGNITUDE_CONCENTRATION,
            )
        )
        and all(
            abs(actual - expected) <= 1e-6
            for actual, expected in zip(
                _magnitude_values(
                    alternate.opposite_alignment_magnitude_concentration
                ),
                _EXPECTED_ALTERNATE_MAGNITUDE_CONCENTRATION,
            )
        )
        and abs(aggregate_dot - _EXPECTED_AGGREGATE_DOT_PRODUCT) <= 1e-8
        and aggregate_cosine is not None
        and abs(aggregate_cosine - _EXPECTED_AGGREGATE_COSINE_SIMILARITY) <= 1e-6
        and unit_norm_alignment.contribution_count_per_protocol == 32
        and unit_norm_alignment.all_source_gradients_finite_and_nonzero
        and unit_norm_alignment.all_values_finite
        and unit_norm_alignment.reference_global_gradient_l2 > 0.0
        and unit_norm_alignment.alternate_global_gradient_l2 > 0.0
        and unit_norm_alignment.cross_protocol_cosine_similarity is not None
        and all(
            abs(actual - expected) <= 1e-6
            for actual, expected in zip(
                _unit_norm_alignment_values(unit_norm_alignment),
                (
                    *_EXPECTED_UNIT_NORM_AGGREGATE_ALIGNMENT[0],
                    _EXPECTED_UNIT_NORM_AGGREGATE_ALIGNMENT[1],
                    *_EXPECTED_UNIT_NORM_AGGREGATE_ALIGNMENT[2],
                    *_EXPECTED_UNIT_NORM_AGGREGATE_ALIGNMENT[3:],
                ),
            )
        )
    )
    if not contract_satisfied:
        raise MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError(
            "per-trajectory gradient-influence diagnostic differs from the approved contract"
        )

    return MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_PER_TRAJECTORY_GRADIENT_INFLUENCE_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        trajectories_per_protocol=_TRAJECTORIES_PER_PROTOCOL,
        total_training_trajectory_count=64,
        training_update_count=0,
        evaluation_call_count=0,
        evaluation_update_count=0,
        reference=reference,
        alternate=alternate,
        aggregate_global_gradient_dot_product=aggregate_dot,
        aggregate_global_gradient_cosine_similarity=aggregate_cosine,
        unit_norm_aggregate_alignment=unit_norm_alignment,
        selected_training_protocol_id=None,
        selected_model_id=None,
        selected_trajectory_seed=None,
        selected_gradient_direction=None,
        selected_checkpoint_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_PER_TRAJECTORY_GRADIENT_INFLUENCE_SMOKE_VERSION",
    "MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceSmokeError",
    "MahJaxCategoricalMlpTrajectoryGradientInfluenceResult",
    "MahJaxCategoricalMlpOppositeAlignmentMagnitudeConcentrationResult",
    "MahJaxCategoricalMlpUnitNormAggregateAlignmentResult",
    "MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult",
    "MahJaxCategoricalMlpFirstPassPerTrajectoryGradientInfluenceResult",
    "run_mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke",
]
