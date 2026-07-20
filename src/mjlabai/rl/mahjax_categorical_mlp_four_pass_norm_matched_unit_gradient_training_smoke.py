"""Run four fixed shared norm-matched unit-gradient training passes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    _load_pinned_runtime,
)
from mjlabai.rl.mahjax_categorical_mlp_first_pass_norm_matched_unit_gradient_update_smoke import (  # noqa: E501
    MAHJAX_CATEGORICAL_MLP_FIRST_PASS_NORM_MATCHED_UNIT_GRADIENT_UPDATE_RATE,
    MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry,
    _all_close,
    _build_norm_matched_update,
    _changed_reward_seeds,
    _geometry_values,
)
from mjlabai.rl.mahjax_categorical_mlp_first_pass_per_trajectory_gradient_influence_smoke import (  # noqa: E501
    MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult,
    MahJaxCategoricalMlpUnitNormAggregateAlignmentResult,
    _ALTERNATE_PROTOCOL_ID,
    _REFERENCE_PROTOCOL_ID,
    _build_protocol_result,
    _build_unit_norm_aggregate_alignment,
    _collect_protocol_gradients,
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


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_TRAINING_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_PASS_COUNT = 4

_EXPECTED_PASS_ALIGNMENTS = (
    (0.00927360774949193, 0.2355091236577188),
    (-0.000518294982612133, -0.016413511736346326),
    (0.012192364418297075, 0.269680770514542),
    (0.013577491845353507, 0.31668333732574877),
)
_EXPECTED_PASS_GEOMETRIES = (
    (
        (0.006833501625806093, 0.0013652854831889272, 0.0161091648042202, 0.0018771332688629627),
        0.017651899867127615,
        (0.05432562530040741, 0.013285310938954353, 0.149087592959404, 0.0168877262622118),
        0.16012519702957836,
        0.11023811489123071,
        (0.00598875479772687, 0.0014645475894212723, 0.016435137018561363, 0.0018616709858179092),
        0.017651901635441395,
        (0.0019164008554071188, 0.00046865397598594427, 0.005259246099740267, 0.0005957343964837492),
    ),
    (
        (0.006647044792771339, 0.001332695595920086, 0.015908753499388695, 0.0018333372427150607),
        0.017389906422356948,
        (0.051188647747039795, 0.01032130979001522, 0.11667542159557343, 0.013093583285808563),
        0.1284967043224035,
        0.13533348200686113,
        (0.006927537731826305, 0.0013968187849968672, 0.015790091827511787, 0.0017720001051202416),
        0.017389907016364347,
        (0.0022168103605508804, 0.00044698099372908473, 0.005052824504673481, 0.0005670403479598463),
    ),
    (
        (0.007176266983151436, 0.0017344861989840865, 0.019098618999123573, 0.002241656882688403),
        0.02059828933288694,
        (0.056966815143823624, 0.014358537271618843, 0.1591431051492691, 0.018086960539221764),
        0.17060202718112621,
        0.12073883102817982,
        (0.006878107786178589, 0.0017336331075057387, 0.019214745610952377, 0.0021837984677404165),
        0.020598283304951642,
        (0.002200994174927473, 0.0005547652253881097, 0.006148719694465399, 0.000698816787917167),
    ),
    (
        (0.007560965605080128, 0.0016542786033824086, 0.01898675225675106, 0.002227476332336664),
        0.02062433636869742,
        (0.05545515567064285, 0.014246499165892601, 0.15862621366977692, 0.018025439232587814),
        0.16960374156154825,
        0.12160307419404992,
        (0.006743516772985458, 0.001732418080791831, 0.019289430230855942, 0.002191948937252164),
        0.020624331495802978,
        (0.002157926093786955, 0.0005543729057535529, 0.006172618828713894, 0.0007014230941422284),
    ),
)
_EXPECTED_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 64, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 88, 51, 81,
    14, 45, 18, 81, 29, 52, 28, 61, 70, 74, 70, 22, 89, 85, 77, 58,
)
_EXPECTED_REPLICATION_TRANSITION_COUNTS = (
    38, 88, 48, 65, 85, 83, 80, 69, 73, 81, 73, 72, 31, 66, 88, 55,
    84, 35, 60, 87, 81, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 77,
)
_EXPECTED_REPLICATION_REWARDS = (
    -13.0, -10.0, 0.0, -77.0, -40.0, -10.0, 0.0, 0.0,
    -257.0, -116.0, 0.0, -10.0, -160.0, 0.0, 0.0, 0.0,
    0.0, -77.0, -20.0, -15.0, -10.0, 0.0, -10.0, -77.0,
    0.0, -80.0, 0.0, -20.0, -15.0, -116.0, 0.0, 0.0,
)

_EVIDENCE_GRADE = (
    "P8 local exact four-pass norm-matched unit-gradient training/fixed-window "
    "diagnostic evidence only"
)
_WARNINGS = (
    "one shared policy branch and exactly four ordered passes",
    "each pass uses exact batches 0 through 31 and 116 through 147 only",
    "all 64 gradients receive identical unit-norm treatment on every pass",
    "each combined unit direction is matched once to that pass raw global norm",
    "one fixed rate 0.32 update per pass and no intermediate evaluation",
    "final evaluation uses only seeds 52 through 83 and 84 through 115",
    "all pass and final outcomes are retained and no selection is performed",
    "no fifth pass, projection, clipping, epsilon or per-seed weight",
    "no pass, scale, rate, seed, window, optimizer or protocol search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError(
    RuntimeError
):
    """Raised when the exact four-pass unit-gradient contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult:
    pass_index: int
    reference: MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult
    alternate: MahJaxCategoricalMlpProtocolTrajectoryGradientInfluenceResult
    unit_norm_aggregate_alignment: MahJaxCategoricalMlpUnitNormAggregateAlignmentResult
    geometry: MahJaxCategoricalMlpNormMatchedUnitGradientUpdateGeometry


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    pass_count: int
    passes: Tuple[MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult, ...]
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
    selected_pass_index: Optional[int]
    selected_model_id: Optional[str]
    selected_scale: Optional[float]
    selected_seed: Optional[int]
    selected_checkpoint_id: Optional[str]
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def run_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke(
) -> MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult:
    """Apply four continuous fixed updates and evaluate only after pass four."""

    try:
        jax, jnp, parameters, _ = _train_mahjax_categorical_mlp_parameters()
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
        raise MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError(
            "pinned four-pass norm-matched unit-gradient runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError(
            "four-pass norm-matched unit-gradient runtime differs from the pinned contract"
        )

    pass_results = []
    for pass_index in range(
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_PASS_COUNT
    ):
        reference_collected = _collect_protocol_gradients(
            _REFERENCE_PROTOCOL_ID,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
            parameters,
            jax,
            jnp,
            mahjax,
        )
        alternate_collected = _collect_protocol_gradients(
            _ALTERNATE_PROTOCOL_ID,
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
            parameters,
            jax,
            jnp,
            mahjax,
        )
        reference = _build_protocol_result(
            reference_collected,
            alternate_collected,
            jnp,
        )
        alternate = _build_protocol_result(
            alternate_collected,
            reference_collected,
            jnp,
        )
        unit_norm_alignment = _build_unit_norm_aggregate_alignment(
            reference_collected,
            alternate_collected,
            jax,
            jnp,
        )
        updated_parameters, geometry = _build_norm_matched_update(
            parameters,
            reference_collected,
            alternate_collected,
            jax,
            jnp,
        )
        pass_results.append(
            MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult(
                pass_index=pass_index,
                reference=reference,
                alternate=alternate,
                unit_norm_aggregate_alignment=unit_norm_alignment,
                geometry=geometry,
            )
        )
        parameters = updated_parameters
    public_passes = tuple(pass_results)

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
    primary_rewards = tuple(item.project_cumulative_raw_reward for item in final_primary)
    replication_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_replication
    )
    if (
        len(public_passes) != 4
        or tuple(item.pass_index for item in public_passes) != tuple(range(4))
        or any(item.reference.training_seeds != tuple(range(32)) for item in public_passes)
        or any(
            item.alternate.training_seeds != tuple(range(116, 148))
            for item in public_passes
        )
        or any(item.reference.trajectory_count != 32 for item in public_passes)
        or any(item.alternate.trajectory_count != 32 for item in public_passes)
        or any(
            not item.unit_norm_aggregate_alignment.all_source_gradients_finite_and_nonzero
            for item in public_passes
        )
        or any(not item.unit_norm_aggregate_alignment.all_values_finite for item in public_passes)
        or any(not item.geometry.all_values_finite for item in public_passes)
        or any(not item.geometry.all_required_norms_nonzero for item in public_passes)
        or any(
            not _all_close(
                (
                    item.unit_norm_aggregate_alignment.cross_protocol_dot_product,
                    item.unit_norm_aggregate_alignment.cross_protocol_cosine_similarity,
                ),
                expected,
            )
            for item, expected in zip(public_passes, _EXPECTED_PASS_ALIGNMENTS)
        )
        or any(
            not _all_close(_geometry_values(item.geometry), expected)
            for item, expected in zip(public_passes, _EXPECTED_PASS_GEOMETRIES)
        )
        or any(
            abs(
                item.geometry.raw_combined_global_l2
                - item.geometry.scaled_unit_combined_global_l2
            )
            > 1e-8
            for item in public_passes
        )
        or any(item.geometry.update_rate != 0.32 for item in public_passes)
        or any(
            not all(value > 0.0 for value in item.geometry.parameter_delta_l2)
            for item in public_passes
        )
        or len(final_primary) != 32
        or len(final_replication) != 32
        or primary_rewards != _EXPECTED_INITIAL_EVALUATION_REWARDS
        or replication_rewards != _EXPECTED_REPLICATION_REWARDS
        or tuple(item.transition_count for item in final_primary)
        != _EXPECTED_PRIMARY_TRANSITION_COUNTS
        or tuple(item.transition_count for item in final_replication)
        != _EXPECTED_REPLICATION_TRANSITION_COUNTS
    ):
        raise MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError(
            "four-pass norm-matched unit-gradient diagnostic differs from the approved contract"
        )

    initial_primary_sum = sum(_EXPECTED_INITIAL_EVALUATION_REWARDS)
    initial_replication_sum = sum(_EXPECTED_INITIAL_REPLICATION_REWARDS)
    final_primary_sum = sum(primary_rewards)
    final_replication_sum = sum(replication_rewards)
    return MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_TRAINING_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        pass_count=4,
        passes=public_passes,
        total_training_trajectory_count=256,
        training_update_count=4,
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
        selected_pass_index=None,
        selected_model_id=None,
        selected_scale=None,
        selected_seed=None,
        selected_checkpoint_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_TRAINING_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_NORM_MATCHED_UNIT_GRADIENT_PASS_COUNT",
    "MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingSmokeError",
    "MahJaxCategoricalMlpNormMatchedUnitGradientTrainingPassResult",
    "MahJaxCategoricalMlpFourPassNormMatchedUnitGradientTrainingResult",
    "run_mahjax_categorical_mlp_four_pass_norm_matched_unit_gradient_training_smoke",
]
