"""Two continuous seat-0 half-game updates plus disjoint evaluation."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from mjlabai.environment.mahjax_categorical_mlp_mixed_half_game_smoke import (
    MahJaxCategoricalMlpMixedHalfGameStep,
)
from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.environment.mahjax_rule_based_half_game_smoke import (
    MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
    MahJaxRuleBasedHalfGameRoundBoundary,
)
from mjlabai.environment.mahjax_rule_based_single_round_smoke import (
    _load_pinned_runtime,
)
from mjlabai.rl.mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke import (
    MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE,
    MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError,
    _apply_seat0_raw_outcome_update,
    _collect_seat0_half_game,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
    MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
    MahJaxCategoricalMlpImitationResult,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_SEQUENCE_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_two_half_game_sequence_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS = (0, 1)
MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS = (2, 3)
MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_LEARNING_RATE = (
    MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE
)

_ACTION_COUNT = 87
_HIDDEN_UNIT_COUNT = 64
_PROJECT_SEAT = 0
_PARAMETER_COUNT = (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT * _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT * _ACTION_COUNT
    + _ACTION_COUNT
)
_EXPECTED_TRAINING = (
    (
        427,
        102,
        (-53.0, 82.0, 429.0, -468.0),
        (0.0, 87.0, 0.0, -77.0),
        (201, 297, 556, -54),
        5,
        -0.5299999713897705,
        -0.5453851222991943,
        -0.5463446378707886,
        (0.0009908610, 0.0002095903, 0.0028836143, 0.0003556903),
    ),
    (
        797,
        196,
        (-259.0, 140.0, 155.0, -56.0),
        (-27.0, 65.0, -14.0, -14.0),
        (-16, 440, 382, 194),
        8,
        -2.5899999141693115,
        -3.4532430171966553,
        -3.4597692489624023,
        (0.0031369785, 0.0007574092, 0.0072538634, 0.0013632783),
    ),
)
_EXPECTED_EVALUATION = (
    (
        780,
        202,
        (-344.0, 157.0, -242.0, 419.0),
        (0.0, 29.0, -29.0, 0.0),
        (-26, 412, 23, 591),
        820,
        215,
        (-387.0, 207.0, -236.0, 396.0),
        (-43.0, 99.0, -23.0, -23.0),
        (-69, 472, 29, 568),
    ),
    (
        907,
        228,
        (-288.0, -29.0, 389.0, -102.0),
        (-32.0, -32.0, 136.0, -62.0),
        (-48, 221, 549, 278),
        1099,
        262,
        (-247.0, -37.0, 482.0, -268.0),
        (0.0, 0.0, 0.0, 0.0),
        (-7, 263, 642, 102),
    ),
)
_EVIDENCE_GRADE = (
    "P8 local two-half-game sequential raw-outcome training failure diagnostic "
    "evidence only"
)
_WARNINGS = (
    "exact ordered training half-games 0 then 1 and exactly two 0.01 updates",
    "updated parameters from seed 0 feed seed 1 directly without reset",
    "project seat 0 samples while bundled rule seats 1 through 3 remain fixed",
    "disjoint greedy evaluation seeds 2 and 3 perform zero updates",
    "aggregate seat-0 evaluation raw reward changes from -632 to -634",
    "seed 2 degrades from -344 to -387 while seed 3 improves -288 to -247",
    "all opposing seed-level outcomes are retained without selection",
    "no third training half-game, replay, search, early stop or rollback",
    "no saved parameters, weights, checkpoint, dataset or artifact",
    "no real Tenhou, real haifu, external log or platform data",
    "not production self-play, league, evaluation or candidate promotion",
    "not improvement, robustness, policy-quality or model-strength evidence",
    "not stable-dan, LuckyJ 10.68 or P9-P12 evidence",
)


class MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(RuntimeError):
    """Raised when the exact two-half-game sequence contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpTwoHalfGameTrainingRecord:
    seed: int
    transition_count: int
    project_decision_count: int
    trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    cumulative_rewards: Tuple[float, ...]
    final_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    final_round_index: int
    red_pon_normalization_count: int
    return_scale: float
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]
    terminated: bool
    truncated: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpTwoHalfGameEvaluationRecord:
    seed: int
    initial_transition_count: int
    initial_project_decision_count: int
    initial_trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    initial_round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    initial_cumulative_rewards: Tuple[float, ...]
    initial_final_rewards: Tuple[float, ...]
    initial_final_scores: Tuple[int, ...]
    initial_final_round_index: int
    initial_red_pon_normalization_count: int
    final_transition_count: int
    final_project_decision_count: int
    final_trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    final_round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    final_cumulative_rewards: Tuple[float, ...]
    final_final_rewards: Tuple[float, ...]
    final_final_scores: Tuple[int, ...]
    final_final_round_index: int
    final_red_pon_normalization_count: int
    behavior_changed: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpTwoHalfGameSequenceResult:
    """Immutable diagnostics from two updates and two-seed evaluation."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    imitation_smoke_version: str
    feature_count: int
    hidden_unit_count: int
    action_count: int
    parameter_count: int
    project_seat: int
    training_seeds: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    transition_cap: int
    learning_rate: float
    training_half_game_count: int
    update_count: int
    evaluation_half_game_count: int
    evaluation_update_count: int
    training_result: MahJaxCategoricalMlpImitationResult
    training_records: Tuple[MahJaxCategoricalMlpTwoHalfGameTrainingRecord, ...]
    evaluation_records: Tuple[
        MahJaxCategoricalMlpTwoHalfGameEvaluationRecord, ...
    ]
    changed_evaluation_seeds: Tuple[int, ...]
    initial_evaluation_project_raw_sum: float
    final_evaluation_project_raw_sum: float
    evaluation_project_raw_delta: float
    parameter_continuity_proven: bool
    all_actions_legal: bool
    all_games_terminated_without_truncation: bool
    training_evaluation_seeds_disjoint: bool
    aggregate_negative_evaluation_observed: bool
    selected_model_id: None
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _close(actual, expected, tolerance=1e-5):
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _trajectory_matches(trajectory, expected, expected_boundary_count):
    return (
        len(trajectory.trace) == expected[0]
        and trajectory.project_decision_count == expected[1]
        and trajectory.cumulative_rewards == expected[2]
        and trajectory.final_rewards == expected[3]
        and trajectory.final_scores == expected[4]
        and trajectory.final_round_index == expected[5]
        and trajectory.red_pon_normalization_count == 0
        and len(trajectory.round_boundaries) == expected_boundary_count
        and trajectory.terminated
        and not trajectory.truncated
    )


def run_mahjax_categorical_mlp_two_half_game_sequence_smoke(
) -> MahJaxCategoricalMlpTwoHalfGameSequenceResult:
    """Run two continuous updates and fixed disjoint two-seed evaluation."""

    try:
        jax, jnp, initial_parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
        _, _, mahjax, rule_based_player = _load_pinned_runtime()
    except Exception as exc:
        raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
            "reviewed categorical MLP or pinned runtime is unavailable"
        ) from exc
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    parameters = initial_parameters
    training_records = []
    for index, seed in enumerate(
        MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS
    ):
        try:
            trajectory = _collect_seat0_half_game(
                seed,
                parameters,
                True,
                jax,
                jnp,
                mahjax,
                rule_based_player,
            )
            update = _apply_seat0_raw_outcome_update(
                parameters,
                trajectory,
                jax,
                jnp,
            )
        except MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError as exc:
            raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
                f"training half-game {index} failed"
            ) from exc
        expected = _EXPECTED_TRAINING[index]
        if (
            not _trajectory_matches(trajectory, expected, expected[5])
            or not _close(update.return_scale, expected[6])
            or not _close(update.initial_objective, expected[7])
            or not _close(update.post_update_objective, expected[8])
            or update.post_update_objective >= update.initial_objective
            or any(
                not _close(actual, target) or actual <= 0.0
                for actual, target in zip(
                    update.parameter_delta_l2,
                    expected[9],
                )
            )
        ):
            raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
                f"training half-game {index} differs from the approved probe"
            )
        training_records.append(
            MahJaxCategoricalMlpTwoHalfGameTrainingRecord(
                seed=seed,
                transition_count=len(trajectory.trace),
                project_decision_count=trajectory.project_decision_count,
                trace=trajectory.trace,
                round_boundaries=trajectory.round_boundaries,
                cumulative_rewards=trajectory.cumulative_rewards,
                final_rewards=trajectory.final_rewards,
                final_scores=trajectory.final_scores,
                final_round_index=trajectory.final_round_index,
                red_pon_normalization_count=(
                    trajectory.red_pon_normalization_count
                ),
                return_scale=update.return_scale,
                initial_objective=update.initial_objective,
                post_update_objective=update.post_update_objective,
                parameter_delta_l2=update.parameter_delta_l2,
                terminated=trajectory.terminated,
                truncated=trajectory.truncated,
            )
        )
        parameters = update.parameters

    evaluation_records = []
    for index, seed in enumerate(
        MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS
    ):
        try:
            initial = _collect_seat0_half_game(
                seed,
                initial_parameters,
                False,
                jax,
                jnp,
                mahjax,
                rule_based_player,
            )
            final = _collect_seat0_half_game(
                seed,
                parameters,
                False,
                jax,
                jnp,
                mahjax,
                rule_based_player,
            )
        except MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError as exc:
            raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
                f"evaluation half-game {index} failed"
            ) from exc
        expected = _EXPECTED_EVALUATION[index]
        if not _trajectory_matches(
            initial,
            (*expected[:5], 8),
            8,
        ) or not _trajectory_matches(
            final,
            (*expected[5:10], 8),
            8,
        ):
            raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
                f"evaluation seed {seed} differs from the approved probe"
            )
        evaluation_records.append(
            MahJaxCategoricalMlpTwoHalfGameEvaluationRecord(
                seed=seed,
                initial_transition_count=len(initial.trace),
                initial_project_decision_count=initial.project_decision_count,
                initial_trace=initial.trace,
                initial_round_boundaries=initial.round_boundaries,
                initial_cumulative_rewards=initial.cumulative_rewards,
                initial_final_rewards=initial.final_rewards,
                initial_final_scores=initial.final_scores,
                initial_final_round_index=initial.final_round_index,
                initial_red_pon_normalization_count=(
                    initial.red_pon_normalization_count
                ),
                final_transition_count=len(final.trace),
                final_project_decision_count=final.project_decision_count,
                final_trace=final.trace,
                final_round_boundaries=final.round_boundaries,
                final_cumulative_rewards=final.cumulative_rewards,
                final_final_rewards=final.final_rewards,
                final_final_scores=final.final_scores,
                final_final_round_index=final.final_round_index,
                final_red_pon_normalization_count=(
                    final.red_pon_normalization_count
                ),
                behavior_changed=(
                    initial.trace != final.trace
                    or initial.cumulative_rewards != final.cumulative_rewards
                    or initial.final_scores != final.final_scores
                ),
            )
        )

    initial_sum = sum(
        item.initial_cumulative_rewards[_PROJECT_SEAT]
        for item in evaluation_records
    )
    final_sum = sum(
        item.final_cumulative_rewards[_PROJECT_SEAT]
        for item in evaluation_records
    )
    changed_seeds = tuple(
        item.seed for item in evaluation_records if item.behavior_changed
    )
    if initial_sum != -632.0 or final_sum != -634.0 or changed_seeds != (2, 3):
        raise MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError(
            "aggregate evaluation differs from the approved probe"
        )

    return MahJaxCategoricalMlpTwoHalfGameSequenceResult(
        smoke_version=MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_SEQUENCE_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        imitation_smoke_version=MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
        feature_count=MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
        hidden_unit_count=_HIDDEN_UNIT_COUNT,
        action_count=_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        project_seat=_PROJECT_SEAT,
        training_seeds=MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS,
        evaluation_seeds=MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS,
        transition_cap=MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
        learning_rate=MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_LEARNING_RATE,
        training_half_game_count=2,
        update_count=2,
        evaluation_half_game_count=2,
        evaluation_update_count=0,
        training_result=training_result,
        training_records=tuple(training_records),
        evaluation_records=tuple(evaluation_records),
        changed_evaluation_seeds=changed_seeds,
        initial_evaluation_project_raw_sum=initial_sum,
        final_evaluation_project_raw_sum=final_sum,
        evaluation_project_raw_delta=final_sum - initial_sum,
        parameter_continuity_proven=True,
        all_actions_legal=True,
        all_games_terminated_without_truncation=True,
        training_evaluation_seeds_disjoint=True,
        aggregate_negative_evaluation_observed=True,
        selected_model_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_SEQUENCE_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_EVALUATION_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_TWO_HALF_GAME_LEARNING_RATE",
    "MahJaxCategoricalMlpTwoHalfGameSequenceSmokeError",
    "MahJaxCategoricalMlpTwoHalfGameTrainingRecord",
    "MahJaxCategoricalMlpTwoHalfGameEvaluationRecord",
    "MahJaxCategoricalMlpTwoHalfGameSequenceResult",
    "run_mahjax_categorical_mlp_two_half_game_sequence_smoke",
]
