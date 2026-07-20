"""One seat-0 half-game raw-outcome update plus disjoint evaluation.

The reviewed categorical MLP samples only for seat 0 during one local MahJax
half-game against three bundled rule-policy seats. Exactly one update is made
from the seat-0 terminal cumulative raw return. Initial and updated parameters
are then evaluated greedily on one disjoint seed without further updates.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from mjlabai.environment.mahjax_categorical_mlp_mixed_half_game_smoke import (
    MahJaxCategoricalMlpMixedHalfGameStep,
    _normalize_rule_action,
)
from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.environment.mahjax_rule_based_half_game_smoke import (
    MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
    MahJaxRuleBasedHalfGameRoundBoundary,
    _four_ints,
)
from mjlabai.environment.mahjax_rule_based_single_round_smoke import (
    _four_floats,
    _legal_actions,
    _load_pinned_runtime,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
    MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
    MahJaxCategoricalMlpImitationResult,
    _encode_observation_array,
    _mlp_logits,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_POLICY_GRADIENT_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED = 0
MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED = 1
MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE = 0.01

_ACTION_COUNT = 87
_HIDDEN_UNIT_COUNT = 64
_PROJECT_SEAT = 0
_PARAMETER_COUNT = (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT * _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT * _ACTION_COUNT
    + _ACTION_COUNT
)
_SAMPLED_PROJECT_POLICY_ID = (
    "mjlabai.categorical_mlp_imitation.sampled@"
    + MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION
)
_GREEDY_PROJECT_POLICY_ID = (
    "mjlabai.categorical_mlp_imitation.greedy@"
    + MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION
)
_RULE_POLICY_ID = "mahjax.red_mahjong.players.rule_based_player@0.1.2"
_EXPECTED_PARAMETER_DELTAS = (
    0.0009908609790727496,
    0.0002095902746077627,
    0.0028836142737418413,
    0.0003556902811396867,
)
_EVIDENCE_GRADE = (
    "P8 local one-update seat-0 half-game raw-outcome failure diagnostic "
    "evidence only"
)
_WARNINGS = (
    "one sampled seed-0 project-seat half-game and exactly one 0.01 update only",
    "seat 0 uses cumulative raw reward divided by 100 without shaping",
    "bundled MahJax rule policy remains fixed at seats 1 through 3",
    "only raw PON 75 to legal PON_RED 76 normalization is permitted",
    "disjoint seed-1 greedy evaluation performs zero updates",
    "negative evaluation retained: seat-0 cumulative reward -300 to -320",
    "negative evaluation retained: seat-0 final score -70 to -80",
    "no second training half-game, replay, search, selection or rollback",
    "no saved parameters, weights, checkpoint, dataset or artifact",
    "no real Tenhou, real haifu, external log or platform data",
    "not production self-play, league, evaluation or candidate promotion",
    "not improvement, policy-quality or model-strength evidence",
    "not stable-dan, LuckyJ 10.68 or P9-P12 evidence",
)


class MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(RuntimeError):
    """Raised when the exact one-update half-game contract fails."""


@dataclass(frozen=True)
class _HalfGameTrajectory:
    project_features: object
    project_legal_masks: object
    project_actions: object
    trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    cumulative_rewards: Tuple[float, ...]
    final_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    final_round_index: int
    project_decision_count: int
    red_pon_normalization_count: int
    terminated: bool
    truncated: bool


@dataclass(frozen=True)
class _HalfGameUpdate:
    parameters: object
    return_scale: float
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]


@dataclass(frozen=True)
class MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult:
    """Immutable diagnostics from one half-game update and fixed evaluation."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    imitation_smoke_version: str
    sampled_project_policy_id: str
    greedy_project_policy_id: str
    rule_policy_id: str
    feature_count: int
    hidden_unit_count: int
    action_count: int
    parameter_count: int
    project_seat: int
    training_seed: int
    evaluation_seed: int
    transition_cap: int
    learning_rate: float
    update_count: int
    evaluation_update_count: int
    training_result: MahJaxCategoricalMlpImitationResult
    training_transition_count: int
    training_project_decision_count: int
    training_trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    training_round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    training_cumulative_rewards: Tuple[float, ...]
    training_final_rewards: Tuple[float, ...]
    training_final_scores: Tuple[int, ...]
    training_final_round_index: int
    training_red_pon_normalization_count: int
    training_terminated: bool
    training_truncated: bool
    return_scale: float
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]
    initial_evaluation_transition_count: int
    initial_evaluation_project_decision_count: int
    initial_evaluation_trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    initial_evaluation_round_boundaries: Tuple[
        MahJaxRuleBasedHalfGameRoundBoundary, ...
    ]
    initial_evaluation_cumulative_rewards: Tuple[float, ...]
    initial_evaluation_final_rewards: Tuple[float, ...]
    initial_evaluation_final_scores: Tuple[int, ...]
    initial_evaluation_final_round_index: int
    initial_evaluation_red_pon_normalization_count: int
    updated_evaluation_transition_count: int
    updated_evaluation_project_decision_count: int
    updated_evaluation_trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    updated_evaluation_round_boundaries: Tuple[
        MahJaxRuleBasedHalfGameRoundBoundary, ...
    ]
    updated_evaluation_cumulative_rewards: Tuple[float, ...]
    updated_evaluation_final_rewards: Tuple[float, ...]
    updated_evaluation_final_scores: Tuple[int, ...]
    updated_evaluation_final_round_index: int
    updated_evaluation_red_pon_normalization_count: int
    all_actions_legal: bool
    all_games_terminated_without_truncation: bool
    training_evaluation_seeds_disjoint: bool
    evaluation_behavior_changed: bool
    negative_evaluation_observed: bool
    selected_model_id: None
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _collect_seat0_half_game(
    seed,
    parameters,
    sample_project_actions,
    jax,
    jnp,
    mahjax,
    rule_based_player,
):
    try:
        init_key, project_key, rule_key = jax.random.split(
            jax.random.PRNGKey(seed),
            3,
        )
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="half",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
        step_fn = jax.jit(environment.step)
        rule_policy_fn = jax.jit(rule_based_player)
        project_logits_fn = jax.jit(
            lambda model_parameters, features: _mlp_logits(
                model_parameters,
                features,
                jax,
            )
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "failed to initialize the pinned seat-0 half-game runtime"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.round_mode != "half"
        or environment.next_round_style != "auto"
        or environment.num_players != 4
        or environment.num_actions != _ACTION_COUNT
        or bool(state.terminated)
        or bool(state.truncated)
    ):
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "seat-0 half-game runtime differs from the approved contract"
        )

    project_features = []
    project_masks = []
    project_actions = []
    trace = []
    boundaries = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    round_start_transition_index = 0

    for transition_index in range(MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                "seat-0 half-game attempted a policy action after completion"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                "MahJax step_count must match the global transition index"
            )
        round_index = int(state.round_state.round)
        round_step_index = transition_index - round_start_transition_index
        actor = int(state.current_player)
        legal_actions = _legal_actions(state.legal_action_mask, _ACTION_COUNT)
        try:
            if actor == _PROJECT_SEAT:
                features = _encode_observation_array(
                    environment.observe(state),
                    jnp,
                )
                logits = jax.block_until_ready(
                    project_logits_fn(parameters, features)
                )
                if tuple(logits.shape) != (_ACTION_COUNT,) or not bool(
                    jnp.all(jnp.isfinite(logits))
                ):
                    raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                        "project policy must produce 87 finite logits"
                    )
                project_key, action_key = jax.random.split(project_key)
                legal_logits = jnp.where(
                    state.legal_action_mask,
                    logits,
                    -jnp.inf,
                )
                if sample_project_actions:
                    raw_action = int(
                        jax.random.categorical(action_key, legal_logits)
                    )
                    policy_id = _SAMPLED_PROJECT_POLICY_ID
                else:
                    raw_action = int(jnp.argmax(legal_logits))
                    policy_id = _GREEDY_PROJECT_POLICY_ID
                applied_action = raw_action
                normalized = False
                project_features.append(features)
                project_masks.append(state.legal_action_mask)
                project_actions.append(raw_action)
            else:
                rule_key, action_key = jax.random.split(rule_key)
                raw_action = int(rule_policy_fn(state, action_key))
                try:
                    applied_action, normalized = _normalize_rule_action(
                        raw_action,
                        legal_actions,
                    )
                except Exception as exc:
                    raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                        f"unsupported rule-policy action at transition {transition_index}"
                    ) from exc
                policy_id = _RULE_POLICY_ID
        except MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError:
            raise
        except Exception as exc:
            raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                f"seat-0 mixed policy failed at transition {transition_index}"
            ) from exc
        if applied_action not in legal_actions:
            raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                f"seat-0 mixed policy applied illegal action {applied_action}"
            )
        trace.append(
            MahJaxCategoricalMlpMixedHalfGameStep(
                transition_index=transition_index,
                round_index=round_index,
                round_step_index=round_step_index,
                acting_player=actor,
                policy_id=policy_id,
                legal_actions=legal_actions,
                raw_action=raw_action,
                applied_action=applied_action,
                red_pon_normalized=normalized,
            )
        )
        try:
            state = jax.block_until_ready(
                step_fn(state, jnp.int32(applied_action))
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
                f"seat-0 half-game step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        next_round_index = int(state.round_state.round)
        if next_round_index != round_index:
            boundaries.append(
                MahJaxRuleBasedHalfGameRoundBoundary(
                    completed_transition_count=transition_index + 1,
                    previous_round_index=round_index,
                    next_round_index=next_round_index,
                    scores_after_boundary=_four_ints(
                        state.round_state.score,
                        "round-boundary scores",
                    ),
                )
            )
            round_start_transition_index = transition_index + 1
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "seat-0 half-game exceeded the "
            f"{MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP}-transition cap"
        )

    if not bool(state.terminated) or bool(state.truncated) or not project_features:
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "seat-0 half-game must terminate without truncation and include decisions"
        )
    return _HalfGameTrajectory(
        project_features=jnp.stack(project_features),
        project_legal_masks=jnp.stack(project_masks),
        project_actions=jnp.asarray(project_actions, dtype=jnp.int32),
        trace=tuple(trace),
        round_boundaries=tuple(boundaries),
        cumulative_rewards=cumulative_rewards,
        final_rewards=_four_floats(state.rewards, "state.rewards"),
        final_scores=_four_ints(state.round_state.score, "final scores"),
        final_round_index=int(state.round_state.round),
        project_decision_count=len(project_actions),
        red_pon_normalization_count=sum(
            item.red_pon_normalized for item in trace
        ),
        terminated=True,
        truncated=False,
    )


def _apply_seat0_raw_outcome_update(parameters, trajectory, jax, jnp):
    return_scale = jnp.float32(trajectory.cumulative_rewards[_PROJECT_SEAT] / 100.0)

    def objective(model_parameters):
        logits = _mlp_logits(model_parameters, trajectory.project_features, jax)
        legal_logits = jnp.where(
            trajectory.project_legal_masks,
            logits,
            -1e9,
        )
        log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
        selected_log_probabilities = log_probabilities[
            jnp.arange(trajectory.project_actions.shape[0]),
            trajectory.project_actions,
        ]
        return -jnp.mean(return_scale * selected_log_probabilities)

    initial_objective, gradients = jax.jit(jax.value_and_grad(objective))(
        parameters
    )
    updated_parameters = tuple(
        value
        - MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE * gradient
        for value, gradient in zip(parameters, gradients)
    )
    updated_parameters = jax.block_until_ready(updated_parameters)
    return _HalfGameUpdate(
        parameters=updated_parameters,
        return_scale=float(return_scale),
        initial_objective=float(initial_objective),
        post_update_objective=float(objective(updated_parameters)),
        parameter_delta_l2=tuple(
            float(jnp.linalg.norm(updated - initial))
            for initial, updated in zip(parameters, updated_parameters)
        ),
    )


def _trajectory_contract(
    trajectory,
    transition_count,
    project_decision_count,
    cumulative_rewards,
    final_rewards,
    final_scores,
):
    return (
        len(trajectory.trace) == transition_count
        and trajectory.project_decision_count == project_decision_count
        and trajectory.cumulative_rewards == cumulative_rewards
        and trajectory.final_rewards == final_rewards
        and trajectory.final_scores == final_scores
        and trajectory.final_round_index == 5
        and trajectory.red_pon_normalization_count == 0
        and trajectory.terminated
        and not trajectory.truncated
    )


def run_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke(
) -> MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult:
    """Run the exact one-update training and disjoint evaluation diagnostic."""

    try:
        jax, jnp, parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
        _, _, mahjax, rule_based_player = _load_pinned_runtime()
    except Exception as exc:
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "reviewed categorical MLP or pinned runtime is unavailable"
        ) from exc
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    training = _collect_seat0_half_game(
        MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED,
        parameters,
        True,
        jax,
        jnp,
        mahjax,
        rule_based_player,
    )
    if not _trajectory_contract(
        training,
        427,
        102,
        (-53.0, 82.0, 429.0, -468.0),
        (0.0, 87.0, 0.0, -77.0),
        (201, 297, 556, -54),
    ):
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "seed-0 training half-game differs from the approved probe"
        )

    update = _apply_seat0_raw_outcome_update(
        parameters,
        training,
        jax,
        jnp,
    )
    diagnostics = (
        update.return_scale,
        update.initial_objective,
        update.post_update_objective,
        *update.parameter_delta_l2,
    )
    if (
        not all(math.isfinite(value) for value in diagnostics)
        or abs(update.return_scale - (-0.53)) > 1e-6
        or abs(update.initial_objective - (-0.5453851223)) > 1e-5
        or abs(update.post_update_objective - (-0.5463446379)) > 1e-5
        or update.post_update_objective >= update.initial_objective
        or any(
            abs(actual - expected) > 1e-5 or actual <= 0.0
            for actual, expected in zip(
                update.parameter_delta_l2,
                _EXPECTED_PARAMETER_DELTAS,
            )
        )
    ):
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "seat-0 update differs from the approved probe"
        )

    initial_evaluation = _collect_seat0_half_game(
        MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED,
        parameters,
        False,
        jax,
        jnp,
        mahjax,
        rule_based_player,
    )
    updated_evaluation = _collect_seat0_half_game(
        MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED,
        update.parameters,
        False,
        jax,
        jnp,
        mahjax,
        rule_based_player,
    )
    if not _trajectory_contract(
        initial_evaluation,
        526,
        132,
        (-300.0, -34.0, 178.0, 96.0),
        (-80.0, 0.0, 0.0, 110.0),
        (-70, 278, 376, 416),
    ) or not _trajectory_contract(
        updated_evaluation,
        524,
        130,
        (-320.0, -54.0, 158.0, 156.0),
        (-80.0, 0.0, 0.0, 110.0),
        (-80, 268, 366, 446),
    ):
        raise MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError(
            "seed-1 evaluation differs from the approved probe"
        )

    return MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_POLICY_GRADIENT_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        imitation_smoke_version=MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
        sampled_project_policy_id=_SAMPLED_PROJECT_POLICY_ID,
        greedy_project_policy_id=_GREEDY_PROJECT_POLICY_ID,
        rule_policy_id=_RULE_POLICY_ID,
        feature_count=MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
        hidden_unit_count=_HIDDEN_UNIT_COUNT,
        action_count=_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        project_seat=_PROJECT_SEAT,
        training_seed=MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED,
        evaluation_seed=MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED,
        transition_cap=MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
        learning_rate=MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE,
        update_count=1,
        evaluation_update_count=0,
        training_result=training_result,
        training_transition_count=len(training.trace),
        training_project_decision_count=training.project_decision_count,
        training_trace=training.trace,
        training_round_boundaries=training.round_boundaries,
        training_cumulative_rewards=training.cumulative_rewards,
        training_final_rewards=training.final_rewards,
        training_final_scores=training.final_scores,
        training_final_round_index=training.final_round_index,
        training_red_pon_normalization_count=(
            training.red_pon_normalization_count
        ),
        training_terminated=training.terminated,
        training_truncated=training.truncated,
        return_scale=update.return_scale,
        initial_objective=update.initial_objective,
        post_update_objective=update.post_update_objective,
        parameter_delta_l2=update.parameter_delta_l2,
        initial_evaluation_transition_count=len(initial_evaluation.trace),
        initial_evaluation_project_decision_count=(
            initial_evaluation.project_decision_count
        ),
        initial_evaluation_trace=initial_evaluation.trace,
        initial_evaluation_round_boundaries=initial_evaluation.round_boundaries,
        initial_evaluation_cumulative_rewards=(
            initial_evaluation.cumulative_rewards
        ),
        initial_evaluation_final_rewards=initial_evaluation.final_rewards,
        initial_evaluation_final_scores=initial_evaluation.final_scores,
        initial_evaluation_final_round_index=(
            initial_evaluation.final_round_index
        ),
        initial_evaluation_red_pon_normalization_count=(
            initial_evaluation.red_pon_normalization_count
        ),
        updated_evaluation_transition_count=len(updated_evaluation.trace),
        updated_evaluation_project_decision_count=(
            updated_evaluation.project_decision_count
        ),
        updated_evaluation_trace=updated_evaluation.trace,
        updated_evaluation_round_boundaries=updated_evaluation.round_boundaries,
        updated_evaluation_cumulative_rewards=(
            updated_evaluation.cumulative_rewards
        ),
        updated_evaluation_final_rewards=updated_evaluation.final_rewards,
        updated_evaluation_final_scores=updated_evaluation.final_scores,
        updated_evaluation_final_round_index=(
            updated_evaluation.final_round_index
        ),
        updated_evaluation_red_pon_normalization_count=(
            updated_evaluation.red_pon_normalization_count
        ),
        all_actions_legal=True,
        all_games_terminated_without_truncation=True,
        training_evaluation_seeds_disjoint=True,
        evaluation_behavior_changed=True,
        negative_evaluation_observed=True,
        selected_model_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_POLICY_GRADIENT_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_TRAINING_SEED",
    "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_EVALUATION_SEED",
    "MAHJAX_CATEGORICAL_MLP_SEAT0_HALF_GAME_LEARNING_RATE",
    "MahJaxCategoricalMlpSeat0HalfGamePolicyGradientSmokeError",
    "MahJaxCategoricalMlpSeat0HalfGamePolicyGradientResult",
    "run_mahjax_categorical_mlp_seat0_half_game_policy_gradient_smoke",
]
