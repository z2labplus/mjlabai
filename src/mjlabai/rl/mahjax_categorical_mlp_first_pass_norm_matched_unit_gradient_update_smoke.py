"""Run one norm-matched update from uniformly normalized trajectory gradients."""

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
    _load_pinned_runtime,
)
from mjlabai.rl.mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke import (  # noqa: E501
    MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult,
    MahJaxCategoricalMlpUnitNormAggregateAlignmentResult,
    _ALTERNATE_PROTOCOL_ID,
    _REFERENCE_PROTOCOL_ID,
    _build_protocol_result,
    _build_unit_norm_aggregate_alignment,
    _collect_protocol_gradients,
    _dot,
    _global_norm,
    _group_norms,
    _unit_norm_mean_gradients,
)
from mjlabai.rl.mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke import (  # noqa: E501
    _EXPECTED_INITIAL_EVALUATION_REWARDS,
    _EXPECTED_INITIAL_REPLICATION_REWARDS,
    _evaluate,
)
from mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke import (  # noqa: E501
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE = 0.32

_EXPECTED_GEOMETRY = (
    (0.006833501625806093, 0.0013652854831889272, 0.0161091648042202, 0.0018771332688629627),
    0.017651899867127615,
    (0.05432562530040741, 0.013285310938954353, 0.149087592959404, 0.0168877262622118),
    0.16012519702957836,
    0.11023811489123071,
    (0.00598875479772687, 0.0014645475894212723, 0.016435137018561363, 0.0018616709858179092),
    0.017651901635441395,
    (0.0019164008554071188, 0.00046865397598594427, 0.005259246099740267, 0.0005957343964837492),
)
_EXPECTED_UNIT_NORM_DOT_PRODUCT = 0.00927360774949193
_EXPECTED_UNIT_NORM_COSINE_SIMILARITY = 0.2355091236577188
_EXPECTED_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 63, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 90, 51, 81,
    14, 45, 18, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
)
_EXPECTED_REPLICATION_TRANSITION_COUNTS = (
    37, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
    84, 35, 60, 87, 82, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
)

_EVIDENCE_GRADE = (
    "P8 local exact first-pass norm-matched unit-gradient one-step behavior "
    "diagnostic evidence only"
)
_WARNINGS = (
    "exact two predeclared first-pass training batches only",
    "all 64 full trajectory gradients receive identical unit-norm treatment",
    "combined unit direction is matched once to the raw combined global norm",
    "one shared update at fixed rate 0.32 only",
    "final zero-update evaluation uses only seeds 52 through 83 and 84 through 115",
    "all outcomes are retained regardless of sign and no selection is performed",
    "no second update, projection, clipping, epsilon or per-seed weight",
    "no scale, rate, seed, window, optimizer or protocol search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError(
    RuntimeError
):
    """Raised when the exact norm-matched update contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry:
    raw_combined_parameter_group_l2: Tuple[float, ...]
    raw_combined_global_l2: float
    unit_combined_parameter_group_l2_before_scale: Tuple[float, ...]
    unit_combined_global_l2_before_scale: float
    norm_match_scale: float
    scaled_unit_combined_parameter_group_l2: Tuple[float, ...]
    scaled_unit_combined_global_l2: float
    update_rate: float
    parameter_delta_l2: Tuple[float, ...]
    all_values_finite: bool
    all_required_norms_nonzero: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    reference: MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult
    alternate: MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult
    unit_norm_aggregate_alignment: MahJaxCategoricalMlpUnitNormAggregateAlignmentResult
    geometry: MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry
    total_training_trajectory_count: int
    training_update_count: int
    primary_evaluation_seeds: Tuple[int, ...]
    replication_evaluation_seeds: Tuple[int, ...]
    evaluation_call_count: int
    evaluation_update_count: int
    primary_transition_counts: Tuple[int, ...]
    primary_project_action_traces: Tuple[Tuple[int, ...], ...]
    primary_raw_rewards: Tuple[float, ...]
    primary_final_scores: Tuple[Tuple[int, ...], ...]
    replication_transition_counts: Tuple[int, ...]
    replication_project_action_traces: Tuple[Tuple[int, ...], ...]
    replication_raw_rewards: Tuple[float, ...]
    replication_final_scores: Tuple[Tuple[int, ...], ...]
    initial_primary_raw_sum: float
    final_primary_raw_sum: float
    primary_delta_from_initial: float
    initial_replication_raw_sum: float
    final_replication_raw_sum: float
    replication_delta_from_initial: float
    primary_changed_from_initial_reward_seeds: Tuple[int, ...]
    replication_changed_from_initial_reward_seeds: Tuple[int, ...]
    selected_training_protocol_id: Optional[str]
    selected_model_id: Optional[str]
    selected_scale: Optional[float]
    selected_seed: Optional[int]
    selected_checkpoint_id: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


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


def _geometry_values(geometry):
    return (
        geometry.raw_combined_parameter_group_l2,
        geometry.raw_combined_global_l2,
        geometry.unit_combined_parameter_group_l2_before_scale,
        geometry.unit_combined_global_l2_before_scale,
        geometry.norm_match_scale,
        geometry.scaled_unit_combined_parameter_group_l2,
        geometry.scaled_unit_combined_global_l2,
        geometry.parameter_delta_l2,
    )


def _build_norm_matched_update(
    parameters,
    reference_collected,
    alternate_collected,
    jax,
    jnp,
):
    raw_combined = tuple(
        (reference_value + alternate_value) / 2.0
        for reference_value, alternate_value in zip(
            reference_collected.mean_gradients,
            alternate_collected.mean_gradients,
        )
    )
    reference_unit_mean, _ = _unit_norm_mean_gradients(
        reference_collected,
        jax,
        jnp,
    )
    alternate_unit_mean, _ = _unit_norm_mean_gradients(
        alternate_collected,
        jax,
        jnp,
    )
    unit_combined = tuple(
        (reference_value + alternate_value) / 2.0
        for reference_value, alternate_value in zip(
            reference_unit_mean,
            alternate_unit_mean,
        )
    )
    raw_group_norms = _group_norms(raw_combined, jnp)
    unit_group_norms = _group_norms(unit_combined, jnp)
    raw_global_norm = _global_norm(raw_group_norms)
    unit_global_norm = _global_norm(unit_group_norms)
    if raw_global_norm <= 0.0 or unit_global_norm <= 0.0:
        raise MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError(
            "norm matching requires nonzero raw and unit combined gradients"
        )
    scale = raw_global_norm / unit_global_norm
    scaled_unit_combined = tuple(value * scale for value in unit_combined)
    scaled_group_norms = _group_norms(scaled_unit_combined, jnp)
    scaled_global_norm = _global_norm(scaled_group_norms)
    updated_parameters = jax.block_until_ready(
        tuple(
            initial_value
            - MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE
            * gradient
            for initial_value, gradient in zip(parameters, scaled_unit_combined)
        )
    )
    parameter_delta_l2 = tuple(
        float(jnp.linalg.norm(updated - initial))
        for initial, updated in zip(parameters, updated_parameters)
    )
    values = (
        *raw_group_norms,
        raw_global_norm,
        *unit_group_norms,
        unit_global_norm,
        scale,
        *scaled_group_norms,
        scaled_global_norm,
        *parameter_delta_l2,
    )
    geometry = MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry(
        raw_combined_parameter_group_l2=raw_group_norms,
        raw_combined_global_l2=raw_global_norm,
        unit_combined_parameter_group_l2_before_scale=unit_group_norms,
        unit_combined_global_l2_before_scale=unit_global_norm,
        norm_match_scale=scale,
        scaled_unit_combined_parameter_group_l2=scaled_group_norms,
        scaled_unit_combined_global_l2=scaled_global_norm,
        update_rate=(
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE
        ),
        parameter_delta_l2=parameter_delta_l2,
        all_values_finite=all(math.isfinite(value) for value in values),
        all_required_norms_nonzero=all(
            value > 0.0
            for value in (raw_global_norm, unit_global_norm, scaled_global_norm)
        ),
    )
    return updated_parameters, geometry


def run_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke(
) -> MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult:
    """Apply one norm-matched unit-gradient update and fixed evaluation."""

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
        raise MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError(
            "pinned norm-matched unit-gradient runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError(
            "norm-matched unit-gradient runtime differs from the pinned contract"
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
    unit_norm_alignment = _build_unit_norm_aggregate_alignment(
        reference_collected,
        alternate_collected,
        jax,
        jnp,
    )
    updated_parameters, geometry = _build_norm_matched_update(
        initial_parameters,
        reference_collected,
        alternate_collected,
        jax,
        jnp,
    )
    final_primary = _evaluate(
        updated_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
    )
    final_replication = _evaluate(
        updated_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
    )
    primary_rewards = tuple(item.project_cumulative_raw_reward for item in final_primary)
    replication_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_replication
    )
    if (
        reference.training_seeds != tuple(range(32))
        or alternate.training_seeds != tuple(range(116, 148))
        or reference.trajectory_count != 32
        or alternate.trajectory_count != 32
        or not unit_norm_alignment.all_source_gradients_finite_and_nonzero
        or not unit_norm_alignment.all_values_finite
        or unit_norm_alignment.cross_protocol_cosine_similarity is None
        or abs(
            unit_norm_alignment.cross_protocol_dot_product
            - _EXPECTED_UNIT_NORM_DOT_PRODUCT
        )
        > 1e-8
        or abs(
            unit_norm_alignment.cross_protocol_cosine_similarity
            - _EXPECTED_UNIT_NORM_COSINE_SIMILARITY
        )
        > 1e-6
        or not geometry.all_values_finite
        or not geometry.all_required_norms_nonzero
        or not _all_close(_geometry_values(geometry), _EXPECTED_GEOMETRY)
        or abs(geometry.raw_combined_global_l2 - geometry.scaled_unit_combined_global_l2)
        > 1e-8
        or geometry.update_rate != 0.32
        or not all(value > 0.0 for value in geometry.parameter_delta_l2)
        or len(final_primary) != 32
        or len(final_replication) != 32
        or primary_rewards != _EXPECTED_INITIAL_EVALUATION_REWARDS
        or replication_rewards != _EXPECTED_INITIAL_REPLICATION_REWARDS
        or tuple(item.transition_count for item in final_primary)
        != _EXPECTED_PRIMARY_TRANSITION_COUNTS
        or tuple(item.transition_count for item in final_replication)
        != _EXPECTED_REPLICATION_TRANSITION_COUNTS
    ):
        raise MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError(
            "norm-matched unit-gradient diagnostic differs from the approved contract"
        )

    initial_primary_sum = sum(_EXPECTED_INITIAL_EVALUATION_REWARDS)
    initial_replication_sum = sum(_EXPECTED_INITIAL_REPLICATION_REWARDS)
    final_primary_sum = sum(primary_rewards)
    final_replication_sum = sum(replication_rewards)
    return MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        reference=reference,
        alternate=alternate,
        unit_norm_aggregate_alignment=unit_norm_alignment,
        geometry=geometry,
        total_training_trajectory_count=64,
        training_update_count=1,
        primary_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS
        ),
        replication_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS
        ),
        evaluation_call_count=2,
        evaluation_update_count=0,
        primary_transition_counts=tuple(item.transition_count for item in final_primary),
        primary_project_action_traces=tuple(
            item.project_action_trace for item in final_primary
        ),
        primary_raw_rewards=primary_rewards,
        primary_final_scores=tuple(item.final_scores for item in final_primary),
        replication_transition_counts=tuple(
            item.transition_count for item in final_replication
        ),
        replication_project_action_traces=tuple(
            item.project_action_trace for item in final_replication
        ),
        replication_raw_rewards=replication_rewards,
        replication_final_scores=tuple(
            item.final_scores for item in final_replication
        ),
        initial_primary_raw_sum=initial_primary_sum,
        final_primary_raw_sum=final_primary_sum,
        primary_delta_from_initial=final_primary_sum - initial_primary_sum,
        initial_replication_raw_sum=initial_replication_sum,
        final_replication_raw_sum=final_replication_sum,
        replication_delta_from_initial=(
            final_replication_sum - initial_replication_sum
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
        selected_training_protocol_id=None,
        selected_model_id=None,
        selected_scale=None,
        selected_seed=None,
        selected_checkpoint_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE",
    "MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateSmokeError",
    "MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry",
    "MahJaxCategoricalMlpFirstPassNormMatchedUnitGradientUpdateResult",
    "run_mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke",
]
