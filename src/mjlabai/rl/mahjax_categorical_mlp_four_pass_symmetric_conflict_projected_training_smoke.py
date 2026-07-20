"""Run four fixed shared-policy symmetric conflict-projected updates."""

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
from mjlabai.rl.mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke import (  # noqa: E501
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE,
    MahJaxCategoricalMlpSymmetricConflictProjectionGeometry,
    _apply_symmetric_conflict_projected_update,
)
from mjlabai.rl.mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke import (  # noqa: E501
    MahJaxCategoricalMlpFirstPassProtocolGradientResult,
    _ALTERNATE_PROTOCOL_ID,
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


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SYMMETRIC_CONFLICT_PROJECTED_TRAINING_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke_v0.1"
)

_PASS_COUNT = 4
_TRAJECTORIES_PER_PROTOCOL_PER_PASS = 32
_EXPECTED_REFERENCE_BATCH_OBJECTIVES = (
    -0.008504558742060908,
    -0.007067036636726698,
    -0.006982960483583156,
    -0.012816564129934704,
)
_EXPECTED_ALTERNATE_BATCH_OBJECTIVES = (
    -0.010526151631779612,
    -0.01076443560828011,
    -0.015468770856386982,
    -0.011717958757799352,
)
_EXPECTED_ORIGINAL_DOT_PRODUCTS = (
    -0.0001429308561853304,
    -0.00010963048507051099,
    -0.0003094144188935388,
    -0.000359444063576575,
)
_EXPECTED_ORIGINAL_COSINE_SIMILARITIES = (
    -0.18687750082306825,
    -0.14942482899110554,
    -0.4011737460616803,
    -0.3252072255045935,
)
_EXPECTED_PROJECTED_DOT_PRODUCTS = (
    0.00013794030803637725,
    0.00010718287370536927,
    0.0002596180897853628,
    0.00032142985332939134,
)
_EXPECTED_PROJECTED_COSINE_SIMILARITIES = (
    0.18687816233561955,
    0.14942474248546794,
    0.40117368232699746,
    0.3252071743795551,
)
_EXPECTED_COMBINED_GLOBAL_L2 = (
    0.020943923926851044,
    0.020351296588768303,
    0.021302940176116714,
    0.025686131890207718,
)
_EXPECTED_PASS_PARAMETER_DELTA_L2 = (
    (0.0025933366268873215, 0.0005189825315028429, 0.006116729229688644, 0.0007130251615308225),
    (0.002448925282806158, 0.0004911418654955924, 0.005974698346108198, 0.0006899700383655727),
    (0.002950591966509819, 0.00048456210060976446, 0.0060872542671859264, 0.0006893530953675508),
    (0.0029726026114076376, 0.0006346293957903981, 0.007589839398860931, 0.0008464462007395923),
)
_EXPECTED_FINAL_PARAMETER_DELTA_L2 = (
    0.010112007148563862,
    0.002028877381235361,
    0.024002619087696075,
    0.0027637341991066933,
)
_EXPECTED_REFERENCE_REWARD_SUMS = (
    (-55.0, -34.0, -150.0, 179.0),
    (-55.0, -34.0, -30.0, 59.0),
    (-55.0, -34.0, -30.0, 59.0),
    (-44.0, 18.0, -116.0, 82.0),
)
_EXPECTED_ALTERNATE_REWARD_SUMS = (
    (130.0, 90.0, 6.0, -286.0),
    (130.0, 90.0, 6.0, -286.0),
    (81.0, 90.0, -24.0, -217.0),
    (81.0, 66.0, -34.0, -163.0),
)
_EXPECTED_FINAL_PRIMARY_REWARDS = (
    -13.0, 0.0, 0.0, -5.0, -5.0, -52.0, -15.0, 70.0,
    0.0, -39.0, 0.0, 0.0, -13.0, -15.0, -30.0, 0.0,
    0.0, -26.0, -20.0, -10.0, -20.0, 80.0, -39.0, 0.0,
    -80.0, 0.0, -20.0, -10.0, 0.0, -10.0, -10.0, -30.0,
)
_EXPECTED_FINAL_REPLICATION_REWARDS = (
    -13.0, -10.0, 0.0, -77.0, -40.0, -10.0, 0.0, 0.0,
    -257.0, -116.0, 0.0, -10.0, -160.0, 0.0, 0.0, 0.0,
    0.0, -77.0, -20.0, -15.0, -10.0, 0.0, -10.0, -77.0,
    0.0, -80.0, 0.0, -20.0, -15.0, -116.0, 0.0, 0.0,
)
_EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 64, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 88, 51, 81,
    14, 45, 18, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
)
_EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS = (
    38, 88, 48, 65, 85, 82, 80, 69, 73, 81, 73, 72, 31, 66, 88, 55,
    84, 35, 60, 87, 81, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
)
_EVIDENCE_GRADE = (
    "P8 local exact four-pass shared-policy symmetric conflict-projected "
    "training diagnostic evidence only"
)
_WARNINGS = (
    "one shared branch and exactly four predeclared training passes only",
    "every pass uses exact frozen-policy batches 0 through 31 and 116 through 147",
    "every pass applies the same simultaneous symmetric projection and one update",
    "all update rates are fixed at 0.32 and all pass signs are retained",
    "no intermediate evaluation, pass selection or checkpoint selection",
    "final zero-update evaluation uses only seeds 52 through 83 and 84 through 115",
    "no fifth pass, third protocol, seed search or third evaluation window",
    "no formula, order, coefficient, rate, optimizer or exploration search",
    "no critic, GAE, clipping, replay, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError(
    RuntimeError
):
    """Raised when the exact four-pass projected-training contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult:
    pass_index: int
    reference: MahJaxCategoricalMlpFirstPassProtocolGradientResult
    alternate: MahJaxCategoricalMlpFirstPassProtocolGradientResult
    geometry: MahJaxCategoricalMlpSymmetricConflictProjectionGeometry
    start_parameter_delta_from_initial_l2: Tuple[float, ...]
    end_parameter_delta_from_initial_l2: Tuple[float, ...]


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    pass_count: int
    trajectories_per_protocol_per_pass: int
    passes: Tuple[
        MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult,
        ...,
    ]
    total_training_trajectory_count: int
    training_update_count: int
    intermediate_evaluation_call_count: int
    primary_evaluation_seeds: Tuple[int, ...]
    replication_evaluation_seeds: Tuple[int, ...]
    evaluation_call_count: int
    evaluation_update_count: int
    final_parameter_delta_l2: Tuple[float, ...]
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
    all_seed_sets_pairwise_disjoint: bool
    selected_training_protocol_id: Optional[str]
    selected_model_id: Optional[str]
    selected_multiplier: Optional[float]
    selected_projection_id: Optional[str]
    selected_pass_index: Optional[int]
    selected_checkpoint_id: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _parameter_delta_l2(initial, current, jnp):
    return tuple(
        float(jnp.linalg.norm(current_value - initial_value))
        for initial_value, current_value in zip(initial, current)
    )


def _changed_reward_seeds(seeds, before, after):
    return tuple(
        seed
        for seed, before_value, after_value in zip(seeds, before, after)
        if before_value != after_value
    )


def _seed_sets_pairwise_disjoint(seed_sets):
    normalized = tuple(set(values) for values in seed_sets)
    return all(
        not normalized[left] & normalized[right]
        for left in range(len(normalized))
        for right in range(left + 1, len(normalized))
    )


def _all_finite(values):
    return all(math.isfinite(value) for value in values)


def _all_close(actual, expected, tolerance=1e-6):
    if isinstance(expected, tuple):
        return len(actual) == len(expected) and all(
            _all_close(actual_item, expected_item, tolerance)
            for actual_item, expected_item in zip(actual, expected)
        )
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _seat_reward_sums(summary):
    return tuple(
        sum(row[seat] for row in summary.cumulative_raw_rewards)
        for seat in range(4)
    )


def run_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke(
) -> MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult:
    """Train one shared branch for four fixed passes, then evaluate once."""

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
        raise MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError(
            "pinned four-pass conflict-projected runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError(
            "four-pass conflict-projected runtime differs from the pinned contract"
        )

    parameters = tuple(initial_parameters)
    pass_results = []
    for pass_index in range(_PASS_COUNT):
        pass_start_parameters = parameters
        reference, reference_gradients = _summarize_protocol(
            _REFERENCE_PROTOCOL_ID,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
            pass_start_parameters,
            jax,
            jnp,
            mahjax,
        )
        alternate, alternate_gradients = _summarize_protocol(
            _ALTERNATE_PROTOCOL_ID,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
            pass_start_parameters,
            jax,
            jnp,
            mahjax,
        )
        update = _apply_symmetric_conflict_projected_update(
            pass_start_parameters,
            reference_gradients,
            alternate_gradients,
            jax,
            jnp,
        )
        parameters = update.parameters
        pass_results.append(
            MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult(
                pass_index=pass_index,
                reference=reference,
                alternate=alternate,
                geometry=update.geometry,
                start_parameter_delta_from_initial_l2=_parameter_delta_l2(
                    initial_parameters,
                    pass_start_parameters,
                    jnp,
                ),
                end_parameter_delta_from_initial_l2=_parameter_delta_l2(
                    initial_parameters,
                    parameters,
                    jnp,
                ),
            )
        )

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

    passes = tuple(pass_results)
    primary_rewards = tuple(item.project_cumulative_raw_reward for item in final_primary)
    replication_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_replication
    )
    final_parameter_delta_l2 = _parameter_delta_l2(
        initial_parameters,
        parameters,
        jnp,
    )
    seed_sets_disjoint = _seed_sets_pairwise_disjoint(
        (
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
        )
    )
    continuity_satisfied = all(
        current.start_parameter_delta_from_initial_l2
        == previous.end_parameter_delta_from_initial_l2
        for previous, current in zip(passes, passes[1:])
    )
    contract_satisfied = (
        len(passes) == _PASS_COUNT
        and tuple(item.pass_index for item in passes) == tuple(range(_PASS_COUNT))
        and all(
            item.reference.training_seeds == tuple(range(32))
            and item.alternate.training_seeds == tuple(range(116, 148))
            and item.reference.trajectory_count == _TRAJECTORIES_PER_PROTOCOL_PER_PASS
            and item.alternate.trajectory_count == _TRAJECTORIES_PER_PROTOCOL_PER_PASS
            and item.reference.all_training_actions_legal
            and item.alternate.all_training_actions_legal
            and item.reference.all_rounds_terminated
            and item.alternate.all_rounds_terminated
            and item.reference.all_advantage_sums_centered
            and item.alternate.all_advantage_sums_centered
            and item.geometry.update_rate
            == MAHJAX_CATEGORICAL_MLP_FIRST_PASS_SYMMETRIC_CONFLICT_PROJECTED_UPDATE_RATE
            and item.geometry.all_values_finite
            and item.geometry.all_required_norms_nonzero
            and _all_finite(item.start_parameter_delta_from_initial_l2)
            and _all_finite(item.end_parameter_delta_from_initial_l2)
            for item in passes
        )
        and passes[0].start_parameter_delta_from_initial_l2
        == tuple(0.0 for _ in initial_parameters)
        and continuity_satisfied
        and _all_finite(final_parameter_delta_l2)
        and all(value > 0.0 for value in final_parameter_delta_l2)
        and _all_close(
            tuple(item.reference.batch_initial_objective for item in passes),
            _EXPECTED_REFERENCE_BATCH_OBJECTIVES,
        )
        and _all_close(
            tuple(item.alternate.batch_initial_objective for item in passes),
            _EXPECTED_ALTERNATE_BATCH_OBJECTIVES,
        )
        and _all_close(
            tuple(item.geometry.original_global_dot_product for item in passes),
            _EXPECTED_ORIGINAL_DOT_PRODUCTS,
            tolerance=1e-8,
        )
        and _all_close(
            tuple(
                item.geometry.original_global_cosine_similarity for item in passes
            ),
            _EXPECTED_ORIGINAL_COSINE_SIMILARITIES,
        )
        and _all_close(
            tuple(item.geometry.projected_global_dot_product for item in passes),
            _EXPECTED_PROJECTED_DOT_PRODUCTS,
            tolerance=1e-8,
        )
        and _all_close(
            tuple(
                item.geometry.projected_global_cosine_similarity for item in passes
            ),
            _EXPECTED_PROJECTED_COSINE_SIMILARITIES,
        )
        and _all_close(
            tuple(item.geometry.combined_global_l2 for item in passes),
            _EXPECTED_COMBINED_GLOBAL_L2,
        )
        and _all_close(
            tuple(item.geometry.parameter_delta_l2 for item in passes),
            _EXPECTED_PASS_PARAMETER_DELTA_L2,
        )
        and _all_close(
            final_parameter_delta_l2,
            _EXPECTED_FINAL_PARAMETER_DELTA_L2,
        )
        and tuple(_seat_reward_sums(item.reference) for item in passes)
        == _EXPECTED_REFERENCE_REWARD_SUMS
        and tuple(_seat_reward_sums(item.alternate) for item in passes)
        == _EXPECTED_ALTERNATE_REWARD_SUMS
        and len(final_primary) == 32
        and len(final_replication) == 32
        and primary_rewards == _EXPECTED_FINAL_PRIMARY_REWARDS
        and replication_rewards == _EXPECTED_FINAL_REPLICATION_REWARDS
        and tuple(item.transition_count for item in final_primary)
        == _EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS
        and tuple(item.transition_count for item in final_replication)
        == _EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS
        and seed_sets_disjoint
    )
    if not contract_satisfied:
        raise MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError(
            "four-pass conflict-projected diagnostic differs from the approved contract"
        )

    return MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SYMMETRIC_CONFLICT_PROJECTED_TRAINING_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        pass_count=_PASS_COUNT,
        trajectories_per_protocol_per_pass=_TRAJECTORIES_PER_PROTOCOL_PER_PASS,
        passes=passes,
        total_training_trajectory_count=(
            _PASS_COUNT * _TRAJECTORIES_PER_PROTOCOL_PER_PASS * 2
        ),
        training_update_count=_PASS_COUNT,
        intermediate_evaluation_call_count=0,
        primary_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS
        ),
        replication_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS
        ),
        evaluation_call_count=2,
        evaluation_update_count=0,
        final_parameter_delta_l2=final_parameter_delta_l2,
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
        all_seed_sets_pairwise_disjoint=seed_sets_disjoint,
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
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SYMMETRIC_CONFLICT_PROJECTED_TRAINING_SMOKE_VERSION",
    "MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingSmokeError",
    "MahJaxCategoricalMlpSymmetricConflictProjectedTrainingPassResult",
    "MahJaxCategoricalMlpFourPassSymmetricConflictProjectedTrainingResult",
    "run_mahjax_categorical_mlp_four_pass_symmetric_conflict_projected_training_smoke",
]
