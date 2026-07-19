"""Run one alternate-seed four-pass causal-baseline MahJax diagnostic."""

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
)
from mjlabai.rl.mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke import (
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS,
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS,
    _EXPECTED_FINAL_EVALUATION_REWARDS,
    _EXPECTED_FINAL_REPLICATION_REWARDS,
    _EXPECTED_INITIAL_EVALUATION_REWARDS,
    _EXPECTED_INITIAL_REPLICATION_REWARDS,
    _evaluate,
)
from mjlabai.rl.mahjax_categorical_mlp_predeclared_running_baseline_comparison_smoke import (
    _apply_causal_running_baseline_update,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_SEED_SENSITIVITY_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS = tuple(range(116, 148))
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_EVALUATION_SEEDS
)
MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS = (
    tuple(range(84, 116))
)

_PASS_COUNT = 4
_LEARNING_RATE = 0.01
_EXPECTED_PER_PASS_NONZERO_UPDATE_COUNTS = (24, 32, 32, 32)
_EXPECTED_PER_PASS_NONZERO_OUTCOME_COUNTS = (8, 8, 12, 10)
_EXPECTED_PASS_ENDING_BASELINES = (
    (0.0375, 0.034375, -0.00125, -0.0925),
    (0.0321875, 0.02265625, -0.00046875, -0.079375),
    (0.0470833333, 0.0144791667, -0.0115625, -0.0802083333),
    (0.036953125, 0.01625, -0.0159375, -0.070078125),
)
_EXPECTED_FINAL_PARAMETER_DELTAS = (
    0.0107313367,
    0.0021179726,
    0.0285595842,
    0.0033060384,
)
_EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS = (
    78, 58, 64, 67, 58, 76, 93, 36, 86, 86, 27, 70, 67, 88, 51, 81,
    14, 45, 18, 80, 29, 52, 28, 61, 70, 74, 71, 22, 89, 85, 77, 58,
)
_EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS = (
    38, 88, 48, 65, 85, 82, 80, 69, 70, 81, 73, 72, 31, 66, 88, 55,
    84, 35, 60, 87, 81, 66, 36, 48, 36, 59, 75, 86, 82, 76, 79, 76,
)
_EVIDENCE_GRADE = (
    "P8 local exact two-training-protocol deterministic sensitivity diagnostic "
    "evidence only"
)
_WARNINGS = (
    "alternate training-seed sensitivity diagnostic only",
    "alternate training uses exact ordered seeds 116 through 147 for four passes",
    "the reviewed reference training branch is not rerun",
    "evaluation occurs only after all 128 alternate attempts",
    "evaluation uses only fixed seeds 52 through 83 and 84 through 115",
    "alternate outcome is retained regardless of sign and never selected",
    "alternate primary and replication retain the exact initial reward vectors",
    "reference fixed-window improvements do not reproduce under alternate training seeds",
    "two training protocols are not robust or generalization evidence",
    "no seed search, fifth pass, third evaluation window or checkpoint selection",
    "no critic, GAE, entropy, KL, clipping, optimizer or rate change",
    "no replay buffer, persistence, artifact, external or real data",
    "not policy-quality, model-strength, stable-dan or promotion evidence",
    "not Tenhou or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError(RuntimeError):
    """Raised when the exact alternate-training diagnostic contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    pass_count: int
    learning_rate: float
    reference_training_seeds_per_pass: Tuple[int, ...]
    alternate_training_seeds_per_pass: Tuple[int, ...]
    primary_evaluation_seeds: Tuple[int, ...]
    replication_evaluation_seeds: Tuple[int, ...]
    update_attempt_count: int
    per_pass_nonzero_update_counts: Tuple[int, ...]
    per_pass_nonzero_raw_outcome_counts: Tuple[int, ...]
    per_pass_transition_counts: Tuple[Tuple[int, ...], ...]
    per_pass_actor_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_legal_action_traces: Tuple[
        Tuple[Tuple[Tuple[int, ...], ...], ...], ...
    ]
    per_pass_cumulative_raw_rewards: Tuple[Tuple[Tuple[float, ...], ...], ...]
    per_pass_final_scores: Tuple[Tuple[Tuple[int, ...], ...], ...]
    per_pass_action_trace_sha256: Tuple[Tuple[str, ...], ...]
    baseline_before_per_attempt: Tuple[Tuple[float, ...], ...]
    advantage_seat_returns_per_attempt: Tuple[Tuple[float, ...], ...]
    baseline_after_per_attempt: Tuple[Tuple[float, ...], ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_attempt_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    pass_ending_baselines: Tuple[Tuple[float, ...], ...]
    final_running_baseline: Tuple[float, ...]
    final_parameter_delta_l2: Tuple[float, ...]
    initial_primary_raw_rewards: Tuple[float, ...]
    reference_final_primary_raw_rewards: Tuple[float, ...]
    alternate_final_primary_transition_counts: Tuple[int, ...]
    alternate_final_primary_project_action_traces: Tuple[Tuple[int, ...], ...]
    alternate_final_primary_raw_rewards: Tuple[float, ...]
    alternate_final_primary_final_scores: Tuple[Tuple[int, ...], ...]
    initial_replication_raw_rewards: Tuple[float, ...]
    reference_final_replication_raw_rewards: Tuple[float, ...]
    alternate_final_replication_transition_counts: Tuple[int, ...]
    alternate_final_replication_project_action_traces: Tuple[Tuple[int, ...], ...]
    alternate_final_replication_raw_rewards: Tuple[float, ...]
    alternate_final_replication_final_scores: Tuple[Tuple[int, ...], ...]
    initial_primary_raw_sum: float
    reference_final_primary_raw_sum: float
    alternate_final_primary_raw_sum: float
    alternate_primary_delta_from_initial: float
    alternate_primary_delta_from_reference: float
    initial_replication_raw_sum: float
    reference_final_replication_raw_sum: float
    alternate_final_replication_raw_sum: float
    alternate_replication_delta_from_initial: float
    alternate_replication_delta_from_reference: float
    alternate_primary_positive_round_count: int
    alternate_primary_negative_round_count: int
    alternate_replication_positive_round_count: int
    alternate_replication_negative_round_count: int
    alternate_primary_changed_from_initial_reward_seeds: Tuple[int, ...]
    alternate_primary_changed_from_reference_reward_seeds: Tuple[int, ...]
    alternate_replication_changed_from_initial_reward_seeds: Tuple[int, ...]
    alternate_replication_changed_from_reference_reward_seeds: Tuple[int, ...]
    all_seed_sets_pairwise_disjoint: bool
    evaluation_call_count: int
    evaluation_update_count: int
    reference_training_branch_rerun_count: int
    parameters_changed: bool
    selected_training_protocol_id: Optional[str]
    selected_pass_index: Optional[int]
    selected_checkpoint_id: Optional[str]
    all_training_actions_legal: bool
    all_rounds_terminated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _trace_sha256(trace: Tuple[int, ...]) -> str:
    return hashlib.sha256(",".join(map(str, trace)).encode("ascii")).hexdigest()


def _changed_reward_seeds(seeds, before, after):
    return tuple(
        seed
        for seed, before_value, after_value in zip(seeds, before, after)
        if before_value != after_value
    )


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def run_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke(
) -> MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult:
    """Train one exact alternate branch and evaluate two fixed windows."""

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
        raise MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError(
            "pinned alternate-training sensitivity runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError(
            "alternate-training runtime differs from the pinned contract"
        )

    parameters = tuple(initial_parameters)
    running_baseline = (0.0, 0.0, 0.0, 0.0)
    completed_attempt_count = 0
    all_pass_trajectories = []
    all_updates = []
    per_pass_nonzero_updates = []
    per_pass_nonzero_outcomes = []
    pass_ending_baselines = []
    for _pass_index in range(_PASS_COUNT):
        pass_trajectories = []
        pass_updates = []
        nonzero_update_count = 0
        nonzero_outcome_count = 0
        for seed in MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS:
            trajectory = _collect_all_project_round(seed, parameters, jax, jnp, mahjax)
            update = _apply_causal_running_baseline_update(
                parameters,
                trajectory,
                running_baseline,
                completed_attempt_count,
                jax,
                jnp,
            )
            nonzero_update_count += any(
                value > 0.0 for value in update.parameter_delta_l2
            )
            nonzero_outcome_count += any(
                value != 0.0 for value in trajectory.cumulative_rewards
            )
            pass_trajectories.append(trajectory)
            pass_updates.append(update)
            parameters = update.parameters
            running_baseline = update.baseline_after
            completed_attempt_count += 1
        all_pass_trajectories.append(tuple(pass_trajectories))
        all_updates.extend(pass_updates)
        per_pass_nonzero_updates.append(nonzero_update_count)
        per_pass_nonzero_outcomes.append(nonzero_outcome_count)
        pass_ending_baselines.append(running_baseline)

    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    final_primary = _evaluate(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS,
    )
    final_replication = _evaluate(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
        MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS,
    )
    final_primary_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_primary
    )
    final_replication_rewards = tuple(
        item.project_cumulative_raw_reward for item in final_replication
    )
    seed_sets = (
        set(MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS),
        set(MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS),
        set(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS
        ),
    )
    pairwise_disjoint = all(
        left.isdisjoint(right)
        for index, left in enumerate(seed_sets)
        for right in seed_sets[index + 1 :]
    )
    all_training_actions_legal = all(
        action in legal
        for rows in all_pass_trajectories
        for item in rows
        for action, legal in zip(item.action_trace, item.legal_action_trace)
    )
    all_rounds_terminated = all(
        item.final_scores is not None
        for rows in all_pass_trajectories
        for item in rows
    )
    if (
        completed_attempt_count != 128
        or tuple(map(len, all_pass_trajectories)) != (32, 32, 32, 32)
        or tuple(per_pass_nonzero_updates)
        != _EXPECTED_PER_PASS_NONZERO_UPDATE_COUNTS
        or tuple(per_pass_nonzero_outcomes)
        != _EXPECTED_PER_PASS_NONZERO_OUTCOME_COUNTS
        or not all(
            _close(actual, expected)
            for actual_row, expected_row in zip(
                pass_ending_baselines,
                _EXPECTED_PASS_ENDING_BASELINES,
            )
            for actual, expected in zip(actual_row, expected_row)
        )
        or not all(
            _close(actual, expected)
            for actual, expected in zip(
                final_deltas,
                _EXPECTED_FINAL_PARAMETER_DELTAS,
            )
        )
        or len(final_primary) != 32
        or len(final_replication) != 32
        or tuple(item.transition_count for item in final_primary)
        != _EXPECTED_FINAL_PRIMARY_TRANSITION_COUNTS
        or tuple(item.transition_count for item in final_replication)
        != _EXPECTED_FINAL_REPLICATION_TRANSITION_COUNTS
        or final_primary_rewards != _EXPECTED_INITIAL_EVALUATION_REWARDS
        or final_replication_rewards != _EXPECTED_INITIAL_REPLICATION_REWARDS
        or not pairwise_disjoint
        or not all_training_actions_legal
        or not all_rounds_terminated
    ):
        raise MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError(
            "alternate-training diagnostic differs from the approved contract"
        )

    pass_trajectories = tuple(all_pass_trajectories)
    updates = tuple(all_updates)
    return MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult(
        smoke_version=MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_SEED_SENSITIVITY_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        pass_count=_PASS_COUNT,
        learning_rate=_LEARNING_RATE,
        reference_training_seeds_per_pass=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_CAUSAL_BASELINE_TRAINING_SEEDS
        ),
        alternate_training_seeds_per_pass=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS
        ),
        primary_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS
        ),
        replication_evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS
        ),
        update_attempt_count=completed_attempt_count,
        per_pass_nonzero_update_counts=tuple(per_pass_nonzero_updates),
        per_pass_nonzero_raw_outcome_counts=tuple(per_pass_nonzero_outcomes),
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
        baseline_before_per_attempt=tuple(item.baseline_before for item in updates),
        advantage_seat_returns_per_attempt=tuple(
            item.advantage_seat_returns for item in updates
        ),
        baseline_after_per_attempt=tuple(item.baseline_after for item in updates),
        initial_objectives=tuple(item.initial_objective for item in updates),
        post_update_objectives=tuple(item.post_update_objective for item in updates),
        per_attempt_parameter_delta_l2=tuple(
            item.parameter_delta_l2 for item in updates
        ),
        pass_ending_baselines=tuple(pass_ending_baselines),
        final_running_baseline=running_baseline,
        final_parameter_delta_l2=final_deltas,
        initial_primary_raw_rewards=_EXPECTED_INITIAL_EVALUATION_REWARDS,
        reference_final_primary_raw_rewards=_EXPECTED_FINAL_EVALUATION_REWARDS,
        alternate_final_primary_transition_counts=tuple(
            item.transition_count for item in final_primary
        ),
        alternate_final_primary_project_action_traces=tuple(
            item.project_action_trace for item in final_primary
        ),
        alternate_final_primary_raw_rewards=final_primary_rewards,
        alternate_final_primary_final_scores=tuple(
            item.final_scores for item in final_primary
        ),
        initial_replication_raw_rewards=_EXPECTED_INITIAL_REPLICATION_REWARDS,
        reference_final_replication_raw_rewards=_EXPECTED_FINAL_REPLICATION_REWARDS,
        alternate_final_replication_transition_counts=tuple(
            item.transition_count for item in final_replication
        ),
        alternate_final_replication_project_action_traces=tuple(
            item.project_action_trace for item in final_replication
        ),
        alternate_final_replication_raw_rewards=final_replication_rewards,
        alternate_final_replication_final_scores=tuple(
            item.final_scores for item in final_replication
        ),
        initial_primary_raw_sum=sum(_EXPECTED_INITIAL_EVALUATION_REWARDS),
        reference_final_primary_raw_sum=sum(_EXPECTED_FINAL_EVALUATION_REWARDS),
        alternate_final_primary_raw_sum=sum(final_primary_rewards),
        alternate_primary_delta_from_initial=(
            sum(final_primary_rewards) - sum(_EXPECTED_INITIAL_EVALUATION_REWARDS)
        ),
        alternate_primary_delta_from_reference=(
            sum(final_primary_rewards) - sum(_EXPECTED_FINAL_EVALUATION_REWARDS)
        ),
        initial_replication_raw_sum=sum(_EXPECTED_INITIAL_REPLICATION_REWARDS),
        reference_final_replication_raw_sum=sum(
            _EXPECTED_FINAL_REPLICATION_REWARDS
        ),
        alternate_final_replication_raw_sum=sum(final_replication_rewards),
        alternate_replication_delta_from_initial=(
            sum(final_replication_rewards)
            - sum(_EXPECTED_INITIAL_REPLICATION_REWARDS)
        ),
        alternate_replication_delta_from_reference=(
            sum(final_replication_rewards)
            - sum(_EXPECTED_FINAL_REPLICATION_REWARDS)
        ),
        alternate_primary_positive_round_count=sum(
            value > 0.0 for value in final_primary_rewards
        ),
        alternate_primary_negative_round_count=sum(
            value < 0.0 for value in final_primary_rewards
        ),
        alternate_replication_positive_round_count=sum(
            value > 0.0 for value in final_replication_rewards
        ),
        alternate_replication_negative_round_count=sum(
            value < 0.0 for value in final_replication_rewards
        ),
        alternate_primary_changed_from_initial_reward_seeds=_changed_reward_seeds(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS,
            _EXPECTED_INITIAL_EVALUATION_REWARDS,
            final_primary_rewards,
        ),
        alternate_primary_changed_from_reference_reward_seeds=_changed_reward_seeds(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS,
            _EXPECTED_FINAL_EVALUATION_REWARDS,
            final_primary_rewards,
        ),
        alternate_replication_changed_from_initial_reward_seeds=_changed_reward_seeds(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS,
            _EXPECTED_INITIAL_REPLICATION_REWARDS,
            final_replication_rewards,
        ),
        alternate_replication_changed_from_reference_reward_seeds=_changed_reward_seeds(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS,
            _EXPECTED_FINAL_REPLICATION_REWARDS,
            final_replication_rewards,
        ),
        all_seed_sets_pairwise_disjoint=pairwise_disjoint,
        evaluation_call_count=2,
        evaluation_update_count=0,
        reference_training_branch_rerun_count=0,
        parameters_changed=all(value > 0.0 for value in final_deltas),
        selected_training_protocol_id=None,
        selected_pass_index=None,
        selected_checkpoint_id=None,
        all_training_actions_legal=all_training_actions_legal,
        all_rounds_terminated=all_rounds_terminated,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_SEED_SENSITIVITY_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_ALTERNATE_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_PRIMARY_EVALUATION_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_SENSITIVITY_REPLICATION_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpFourPassTrainingSeedSensitivitySmokeError",
    "MahJaxCategoricalMlpFourPassTrainingSeedSensitivityResult",
    "run_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke",
]
