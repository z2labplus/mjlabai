"""Run fixed 32x batch-size compensation for two reviewed MahJax protocols."""

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
from mjlabai.rl.mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke import (
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_ALTERNATE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REFERENCE_TRAINING_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS,
    MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult,
    _run_protocol,
)
from mjlabai.rl.mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke import (
    _EXPECTED_FINAL_REPLICATION_REWARDS,
    _EXPECTED_INITIAL_EVALUATION_REWARDS,
    _EXPECTED_INITIAL_REPLICATION_REWARDS,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATED_TRAINING_PROTOCOL_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER = 32.0

_PASS_COUNT = 4
_TRAJECTORIES_PER_PASS = 32
_BASE_LEARNING_RATE = 0.01
_EFFECTIVE_MEAN_GRADIENT_LEARNING_RATE = 0.32
_REFERENCE_PROTOCOL_ID = "reference_ordered_0_31_batch_size_compensated"
_ALTERNATE_PROTOCOL_ID = "alternate_ordered_116_147_batch_size_compensated"
_EXPECTED_REFERENCE_BATCH_INITIAL_OBJECTIVES = (
    -0.0085045587,
    -0.0165455118,
    -0.0182897860,
    -0.0174096585,
)
_EXPECTED_REFERENCE_BATCH_POST_OBJECTIVES = (
    -0.0087652362,
    -0.0167149225,
    -0.0184521101,
    -0.0175859964,
)
_EXPECTED_REFERENCE_PASS_PARAMETER_DELTAS = (
    (0.0034197175, 0.0006286280, 0.0083654495, 0.0009456520),
    (0.0032516152, 0.0004498697, 0.0065280204, 0.0007454551),
    (0.0031607540, 0.0004677820, 0.0064025619, 0.0007144618),
    (0.0032675604, 0.0004869229, 0.0066801221, 0.0007454457),
)
_EXPECTED_REFERENCE_FINAL_PARAMETER_DELTAS = (
    0.0123636629,
    0.0017657150,
    0.0261666030,
    0.0029413241,
)
_EXPECTED_REFERENCE_TRAINING_REWARD_SUMS = (
    (-55.0, -34.0, -150.0, 179.0),
    (-19.0, -120.0, -220.0, 279.0),
    (43.0, -125.0, -215.0, 197.0),
    (38.0, -90.0, -240.0, 192.0),
)
_EXPECTED_REFERENCE_FINAL_PRIMARY_REWARDS = (
    -13.0, 0.0, 0.0, -5.0, -5.0, -52.0, 0.0, 70.0,
    0.0, 0.0, 0.0, 0.0, -13.0, -15.0, -30.0, 0.0,
    0.0, -26.0, -20.0, -10.0, -20.0, 80.0, -39.0, 0.0,
    -80.0, 0.0, -20.0, -10.0, 0.0, -10.0, -10.0, -30.0,
)
_EXPECTED_REFERENCE_FINAL_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 63, 67, 58, 76, 86, 36, 86, 75, 27, 70, 67, 87, 51, 81,
    14, 45, 19, 81, 29, 52, 29, 61, 70, 74, 70, 22, 89, 85, 77, 58,
)
_EXPECTED_REFERENCE_FINAL_REPLICATION_TRANSITION_COUNTS = (
    38, 88, 48, 65, 85, 81, 80, 69, 70, 81, 73, 72, 31, 65, 88, 55,
    84, 35, 59, 50, 81, 66, 36, 48, 36, 59, 74, 86, 82, 79, 75, 76,
)
_EXPECTED_ALTERNATE_BATCH_INITIAL_OBJECTIVES = (
    -0.0105261516,
    -0.0112280485,
    -0.0164435498,
    -0.0173537340,
)
_EXPECTED_ALTERNATE_BATCH_POST_OBJECTIVES = (
    -0.0107582265,
    -0.0114182580,
    -0.0167419830,
    -0.0176754166,
)
_EXPECTED_ALTERNATE_PASS_PARAMETER_DELTAS = (
    (0.0030644594, 0.0006645250, 0.0079523092, 0.0009289634),
    (0.0029482471, 0.0005702035, 0.0071361917, 0.0008293389),
    (0.0034650560, 0.0006685967, 0.0090301344, 0.0010298742),
    (0.0034736686, 0.0007890816, 0.0093804533, 0.0011097033),
)
_EXPECTED_ALTERNATE_FINAL_PARAMETER_DELTAS = (
    0.0121162534,
    0.0025018181,
    0.0312487930,
    0.0036535931,
)
_EXPECTED_ALTERNATE_TRAINING_REWARD_SUMS = (
    (130.0, 90.0, 6.0, -286.0),
    (120.0, 110.0, -4.0, -296.0),
    (176.0, -45.0, -19.0, -212.0),
    (205.0, 104.0, -28.0, -381.0),
)
_EXPECTED_ALTERNATE_FINAL_PRIMARY_REWARDS = (
    -13.0, 0.0, 0.0, -5.0, -5.0, -52.0, -15.0, 70.0,
    0.0, -39.0, 0.0, 0.0, -13.0, -15.0, -30.0, 0.0,
    0.0, -26.0, -20.0, -10.0, -20.0, 20.0, -39.0, 0.0,
    -80.0, 0.0, -20.0, -10.0, 0.0, -10.0, -10.0, -30.0,
)
_EXPECTED_ALTERNATE_FINAL_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 64, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 88, 51, 81,
    14, 45, 18, 80, 29, 90, 28, 61, 70, 75, 71, 22, 89, 85, 77, 58,
)
_EXPECTED_ALTERNATE_FINAL_REPLICATION_TRANSITION_COUNTS = (
    38, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 66, 88, 55,
    84, 35, 60, 87, 81, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
)
_EVIDENCE_GRADE = (
    "P8 local exact fixed-32x two-protocol batch-size compensation diagnostic "
    "evidence only"
)
_WARNINGS = (
    "fixed batch-size compensation multiplier 32.0 only",
    "base learning rate 0.01 and effective mean-gradient rate 0.32",
    "same exact two predeclared training protocols and four passes",
    "each pass collects all 32 trajectories before one compensated update",
    "each trajectory baseline uses the other 31 same-seat returns only",
    "mean-gradient and online branches are not rerun inside this smoke",
    "final zero-update evaluation uses only seeds 52 through 83 and 84 through 115",
    "all outcomes are retained regardless of sign and no protocol is selected",
    "no multiplier search, third protocol, fifth pass or third evaluation window",
    "no critic, GAE, entropy, KL, clipping, optimizer or rate search",
    "no replay buffer, persistence, artifact, external or real data",
    "not robustness, generalization, policy-quality or model-strength evidence",
    "not stable-dan, candidate-promotion, Tenhou or LuckyJ 10.68 evidence",
)


class MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError(
    RuntimeError
):
    """Raised when the exact fixed-32x diagnostic contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    pass_count: int
    trajectories_per_pass: int
    base_learning_rate: float
    batch_gradient_multiplier: float
    effective_mean_gradient_learning_rate: float
    primary_evaluation_seeds: Tuple[int, ...]
    replication_evaluation_seeds: Tuple[int, ...]
    reference: MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult
    alternate: MahJaxCategoricalMlpFourPassLeaveOneOutBatchProtocolResult
    reviewed_mean_reference_primary_delta: float
    reviewed_mean_reference_replication_delta: float
    reviewed_mean_alternate_primary_delta: float
    reviewed_mean_alternate_replication_delta: float
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


def _all_close(actual, expected, tolerance=1e-6):
    if isinstance(expected, tuple):
        return len(actual) == len(expected) and all(
            _all_close(actual_item, expected_item, tolerance)
            for actual_item, expected_item in zip(actual, expected)
        )
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def run_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke(
) -> MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult:
    """Run only the exact fixed-32x branches and retain results without selection."""

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
        raise MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError(
            "pinned batch-size-compensated runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError(
            "batch-size-compensated runtime differs from the pinned contract"
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
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER,
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
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER,
    )
    seed_sets = (
        set(reference.training_seeds_per_pass),
        set(alternate.training_seeds_per_pass),
        set(MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS),
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
        or reference.final_primary_raw_rewards
        != _EXPECTED_REFERENCE_FINAL_PRIMARY_REWARDS
        or reference.final_replication_raw_rewards
        != _EXPECTED_FINAL_REPLICATION_REWARDS
        or reference.final_primary_transition_counts
        != _EXPECTED_REFERENCE_FINAL_PRIMARY_TRANSITION_COUNTS
        or reference.final_replication_transition_counts
        != _EXPECTED_REFERENCE_FINAL_REPLICATION_TRANSITION_COUNTS
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
        or alternate.final_primary_raw_rewards
        != _EXPECTED_ALTERNATE_FINAL_PRIMARY_REWARDS
        or alternate.final_replication_raw_rewards
        != _EXPECTED_INITIAL_REPLICATION_REWARDS
        or alternate.final_primary_transition_counts
        != _EXPECTED_ALTERNATE_FINAL_PRIMARY_TRANSITION_COUNTS
        or alternate.final_replication_transition_counts
        != _EXPECTED_ALTERNATE_FINAL_REPLICATION_TRANSITION_COUNTS
        or not all_advantage_sums_centered
        or sum(_EXPECTED_INITIAL_EVALUATION_REWARDS) != -312.0
    ):
        raise MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError(
            "batch-size-compensated diagnostic differs from the approved contract"
        )

    return MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATED_TRAINING_PROTOCOL_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        pass_count=_PASS_COUNT,
        trajectories_per_pass=_TRAJECTORIES_PER_PASS,
        base_learning_rate=_BASE_LEARNING_RATE,
        batch_gradient_multiplier=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER
        ),
        effective_mean_gradient_learning_rate=(
            _EFFECTIVE_MEAN_GRADIENT_LEARNING_RATE
        ),
        primary_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_PRIMARY_EVALUATION_SEEDS
        ),
        replication_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_LEAVE_ONE_OUT_BATCH_REPLICATION_EVALUATION_SEEDS
        ),
        reference=reference,
        alternate=alternate,
        reviewed_mean_reference_primary_delta=0.0,
        reviewed_mean_reference_replication_delta=0.0,
        reviewed_mean_alternate_primary_delta=0.0,
        reviewed_mean_alternate_replication_delta=0.0,
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
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATED_TRAINING_PROTOCOL_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_BATCH_SIZE_COMPENSATION_MULTIPLIER",
    "MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolSmokeError",
    "MahJaxCategoricalMlpFourPassBatchSizeCompensatedTrainingProtocolResult",
    "run_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke",
]
