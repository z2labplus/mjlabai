"""Run one fixed symmetric conflict-projected update for two protocol batches."""

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
from mjlabai.rl.mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke import (  # noqa: E501
    MahJaxCategoricalMlpFirstPassProtocolGradientResult,
    _ALTERNATE_PROTOCOL_ID,
    _EXPECTED_GLOBAL_GRADIENT_COSINE_SIMILARITY,
    _EXPECTED_GLOBAL_GRADIENT_DOT_PRODUCT,
    _REFERENCE_PROTOCOL_ID,
    _summarize_protocol,
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


MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE = 0.32

_EXPECTED_REFERENCE_PROJECTION_COEFFICIENT = -0.19796082870996487
_EXPECTED_ALTERNATE_PROJECTION_COEFFICIENT = -0.17641470053170136
_EXPECTED_REFERENCE_PROJECTED_GROUP_L2 = (
    0.010677625425159931,
    0.001971412682905793,
    0.0256037600338459,
    0.002907978370785713,
)
_EXPECTED_ALTERNATE_PROJECTED_GROUP_L2 = (
    0.009585835970938206,
    0.002075165743008256,
    0.024340301752090454,
    0.0028562890365719795,
)
_EXPECTED_REFERENCE_PROJECTED_GLOBAL_L2 = 0.02796260035765747
_EXPECTED_ALTERNATE_PROJECTED_GLOBAL_L2 = 0.026397030904363974
_EXPECTED_PROJECTED_DOT_PRODUCT = 0.00013794030803637725
_EXPECTED_PROJECTED_COSINE_SIMILARITY = 0.18687816233561955
_EXPECTED_COMBINED_GROUP_L2 = (
    0.008104180917143822,
    0.0016218236414715648,
    0.01911478489637375,
    0.0022282027639448643,
)
_EXPECTED_COMBINED_GLOBAL_L2 = 0.020943923926851044
_EXPECTED_PARAMETER_DELTA_L2 = (
    0.0025933366268873215,
    0.0005189825315028429,
    0.006116729229688644,
    0.0007130251615308225,
)
_EXPECTED_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 63, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 90, 51, 81,
    14, 45, 18, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
)
_EXPECTED_REPLICATION_TRANSITION_COUNTS = (
    37, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
    84, 35, 60, 87, 82, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
)
_EVIDENCE_GRADE = (
    "P8 local exact first-pass symmetric conflict-projected one-step update "
    "diagnostic evidence only"
)
_WARNINGS = (
    "exact two predeclared first-pass training batches only",
    "simultaneous symmetric projection uses the original negative-dot pair only",
    "one fixed formula, one average and one update at rate 0.32 only",
    "no alternative projection order, coefficient, epsilon or threshold",
    "final zero-update evaluation uses only seeds 52 through 83 and 84 through 115",
    "all outcomes are retained regardless of sign and no selection is performed",
    "no second update, third protocol, seed search or third evaluation window",
    "no scale, rate, optimizer, entropy, temperature or exploration search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError(
    RuntimeError
):
    """Raised when the exact projected-update contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpSymmetricConflictProjectionGeometry:
    original_global_dot_product: float
    original_global_cosine_similarity: float
    reference_original_squared_norm: float
    alternate_original_squared_norm: float
    reference_projection_coefficient: float
    alternate_projection_coefficient: float
    reference_projected_parameter_group_l2: Tuple[float, ...]
    alternate_projected_parameter_group_l2: Tuple[float, ...]
    reference_projected_global_l2: float
    alternate_projected_global_l2: float
    projected_global_dot_product: float
    projected_global_cosine_similarity: float
    combined_parameter_group_l2: Tuple[float, ...]
    combined_global_l2: float
    update_rate: float
    parameter_delta_l2: Tuple[float, ...]
    all_values_finite: bool
    all_required_norms_nonzero: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    reference: MahJaxCategoricalMlpFirstPassProtocolGradientResult
    alternate: MahJaxCategoricalMlpFirstPassProtocolGradientResult
    geometry: MahJaxCategoricalMlpSymmetricConflictProjectionGeometry
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
    selected_multiplier: Optional[float]
    selected_projection_id: Optional[str]
    selected_pass_index: Optional[int]
    selected_checkpoint_id: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


@dataclass(frozen=True)
class _SymmetricConflictProjectedUpdate:
    parameters: tuple
    geometry: MahJaxCategoricalMlpSymmetricConflictProjectionGeometry


def _group_norms(values, jnp):
    return tuple(float(jnp.linalg.norm(value)) for value in values)


def _global_norm(group_norms):
    return math.sqrt(sum(value * value for value in group_norms))


def _dot(left, right, jnp):
    return sum(float(jnp.vdot(a, b)) for a, b in zip(left, right))


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


def _apply_symmetric_conflict_projected_update(
    parameters,
    reference_gradients,
    alternate_gradients,
    jax,
    jnp,
):
    original_dot = _dot(reference_gradients, alternate_gradients, jnp)
    reference_squared_norm = _dot(reference_gradients, reference_gradients, jnp)
    alternate_squared_norm = _dot(alternate_gradients, alternate_gradients, jnp)
    if reference_squared_norm <= 0.0 or alternate_squared_norm <= 0.0:
        raise MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError(
            "approved projection requires two nonzero gradient vectors"
        )
    reference_coefficient = original_dot / alternate_squared_norm
    alternate_coefficient = original_dot / reference_squared_norm
    reference_projected = tuple(
        reference_value - reference_coefficient * alternate_value
        for reference_value, alternate_value in zip(
            reference_gradients,
            alternate_gradients,
        )
    )
    alternate_projected = tuple(
        alternate_value - alternate_coefficient * reference_value
        for reference_value, alternate_value in zip(
            reference_gradients,
            alternate_gradients,
        )
    )
    combined = tuple(
        (reference_value + alternate_value) / 2.0
        for reference_value, alternate_value in zip(
            reference_projected,
            alternate_projected,
        )
    )
    updated_parameters = jax.block_until_ready(
        tuple(
            initial_value
            - MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE
            * gradient
            for initial_value, gradient in zip(parameters, combined)
        )
    )

    reference_projected_group_norms = _group_norms(reference_projected, jnp)
    alternate_projected_group_norms = _group_norms(alternate_projected, jnp)
    combined_group_norms = _group_norms(combined, jnp)
    reference_projected_global_norm = _global_norm(reference_projected_group_norms)
    alternate_projected_global_norm = _global_norm(alternate_projected_group_norms)
    combined_global_norm = _global_norm(combined_group_norms)
    projected_dot = _dot(reference_projected, alternate_projected, jnp)
    projected_denominator = (
        reference_projected_global_norm * alternate_projected_global_norm
    )
    projected_cosine = (
        projected_dot / projected_denominator
        if projected_denominator > 0.0
        else math.nan
    )
    original_cosine = original_dot / math.sqrt(
        reference_squared_norm * alternate_squared_norm
    )
    parameter_delta_l2 = tuple(
        float(jnp.linalg.norm(updated - initial))
        for initial, updated in zip(parameters, updated_parameters)
    )
    scalar_diagnostics = (
        original_dot,
        original_cosine,
        reference_squared_norm,
        alternate_squared_norm,
        reference_coefficient,
        alternate_coefficient,
        *reference_projected_group_norms,
        *alternate_projected_group_norms,
        reference_projected_global_norm,
        alternate_projected_global_norm,
        projected_dot,
        projected_cosine,
        *combined_group_norms,
        combined_global_norm,
        *parameter_delta_l2,
    )
    all_finite = all(math.isfinite(value) for value in scalar_diagnostics)
    all_nonzero = all(
        value > 0.0
        for value in (
            reference_squared_norm,
            alternate_squared_norm,
            reference_projected_global_norm,
            alternate_projected_global_norm,
            combined_global_norm,
        )
    )
    geometry = MahJaxCategoricalMlpSymmetricConflictProjectionGeometry(
        original_global_dot_product=original_dot,
        original_global_cosine_similarity=original_cosine,
        reference_original_squared_norm=reference_squared_norm,
        alternate_original_squared_norm=alternate_squared_norm,
        reference_projection_coefficient=reference_coefficient,
        alternate_projection_coefficient=alternate_coefficient,
        reference_projected_parameter_group_l2=reference_projected_group_norms,
        alternate_projected_parameter_group_l2=alternate_projected_group_norms,
        reference_projected_global_l2=reference_projected_global_norm,
        alternate_projected_global_l2=alternate_projected_global_norm,
        projected_global_dot_product=projected_dot,
        projected_global_cosine_similarity=projected_cosine,
        combined_parameter_group_l2=combined_group_norms,
        combined_global_l2=combined_global_norm,
        update_rate=(
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE
        ),
        parameter_delta_l2=parameter_delta_l2,
        all_values_finite=all_finite,
        all_required_norms_nonzero=all_nonzero,
    )
    return _SymmetricConflictProjectedUpdate(
        parameters=updated_parameters,
        geometry=geometry,
    )


def run_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke(
) -> MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult:
    """Apply one exact projected update and evaluate only fixed final windows."""

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
        raise MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError(
            "pinned symmetric conflict-projected runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError(
            "symmetric conflict-projected runtime differs from the pinned contract"
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
    update = _apply_symmetric_conflict_projected_update(
        initial_parameters,
        reference_gradients,
        alternate_gradients,
        jax,
        jnp,
    )
    updated_parameters = update.parameters
    geometry = update.geometry
    if geometry.original_global_dot_product >= 0.0:
        raise MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError(
            "approved projection requires the reviewed negative-dot nonzero pair"
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
        abs(
            geometry.original_global_dot_product
            - _EXPECTED_GLOBAL_GRADIENT_DOT_PRODUCT
        )
        > 1e-8
        or abs(
            geometry.original_global_cosine_similarity
            - _EXPECTED_GLOBAL_GRADIENT_COSINE_SIMILARITY
        )
        > 1e-6
        or not geometry.all_values_finite
        or not geometry.all_required_norms_nonzero
        or not all(value > 0.0 for value in geometry.parameter_delta_l2)
        or len(final_primary) != 32
        or len(final_replication) != 32
        or not _all_close(
            geometry.reference_projection_coefficient,
            _EXPECTED_REFERENCE_PROJECTION_COEFFICIENT,
        )
        or not _all_close(
            geometry.alternate_projection_coefficient,
            _EXPECTED_ALTERNATE_PROJECTION_COEFFICIENT,
        )
        or not _all_close(
            geometry.reference_projected_parameter_group_l2,
            _EXPECTED_REFERENCE_PROJECTED_GROUP_L2,
        )
        or not _all_close(
            geometry.alternate_projected_parameter_group_l2,
            _EXPECTED_ALTERNATE_PROJECTED_GROUP_L2,
        )
        or not _all_close(
            geometry.reference_projected_global_l2,
            _EXPECTED_REFERENCE_PROJECTED_GLOBAL_L2,
        )
        or not _all_close(
            geometry.alternate_projected_global_l2,
            _EXPECTED_ALTERNATE_PROJECTED_GLOBAL_L2,
        )
        or not _all_close(
            geometry.projected_global_dot_product,
            _EXPECTED_PROJECTED_DOT_PRODUCT,
            tolerance=1e-8,
        )
        or not _all_close(
            geometry.projected_global_cosine_similarity,
            _EXPECTED_PROJECTED_COSINE_SIMILARITY,
        )
        or not _all_close(
            geometry.combined_parameter_group_l2,
            _EXPECTED_COMBINED_GROUP_L2,
        )
        or not _all_close(
            geometry.combined_global_l2,
            _EXPECTED_COMBINED_GLOBAL_L2,
        )
        or not _all_close(
            geometry.parameter_delta_l2,
            _EXPECTED_PARAMETER_DELTA_L2,
        )
        or primary_rewards != _EXPECTED_INITIAL_EVALUATION_REWARDS
        or replication_rewards != _EXPECTED_INITIAL_REPLICATION_REWARDS
        or tuple(item.transition_count for item in final_primary)
        != _EXPECTED_PRIMARY_TRANSITION_COUNTS
        or tuple(item.transition_count for item in final_replication)
        != _EXPECTED_REPLICATION_TRANSITION_COUNTS
    ):
        raise MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError(
            "symmetric conflict-projected diagnostic differs from the approved contract"
        )

    return MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        reference=reference,
        alternate=alternate,
        geometry=geometry,
        total_training_trajectory_count=(
            reference.trajectory_count + alternate.trajectory_count
        ),
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
        selected_multiplier=None,
        selected_projection_id=None,
        selected_pass_index=None,
        selected_checkpoint_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE",
    "MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateSmokeError",
    "MahJaxCategoricalMlpSymmetricConflictProjectionGeometry",
    "MahJaxCategoricalMlpFirstPassSymmetricConflictProjectedUpdateResult",
    "run_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke",
]
