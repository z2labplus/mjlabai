"""One shared categorical-MLP update from an all-project MahJax round.

All four seats sample from one reviewed in-memory project policy. Each selected
log probability receives its acting seat's terminal cumulative raw return, and
exactly one shared update is applied. This is not production self-play,
evaluation, improvement, or model-strength evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
    MahJaxCategoricalMlpImitationResult,
    _encode_observation_array,
    _mlp_logits,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_all_project_policy_gradient_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED = 1
MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE = 0.01

_ACTION_COUNT = 87
_HIDDEN_UNIT_COUNT = 64
_TRANSITION_CAP = 256
_PROJECT_POLICY_ID = (
    "project_categorical_mlp_882x64x87_imitation_seed_123_epoch_48"
)
_PARAMETER_COUNT = (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT * _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT * _ACTION_COUNT
    + _ACTION_COUNT
)
_EXPECTED_FIRST_ACTIONS = (28, 27, 28, 28, 29, 33, 27, 31, 27, 0, 31, 32)
_EVIDENCE_GRADE = (
    "P8 local shared all-project-seat categorical-MLP raw-outcome update smoke "
    "evidence only"
)
_WARNINGS = (
    "one shared all-project-seat categorical-MLP raw-outcome update smoke only",
    "exact seed 1 and exactly one 0.01 gradient update",
    "all four seats sample from one shared reviewed project policy",
    "environment initialization and project-action RNG streams are independent",
    "every selected action is checked against the environment legal mask",
    "each selected log probability uses its acting seat cumulative raw return",
    "returns are only cumulative raw rewards divided by 100",
    "no baseline, critic, discount, bootstrapping, entropy, replay or shaping",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "no second update, second round, production self-play, evaluation or league",
    "no real Tenhou, real haifu, external log or platform data",
    "not improvement, policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(RuntimeError):
    """Raised when the exact shared all-project update contract fails."""


@dataclass(frozen=True)
class _AllProjectTrajectory:
    features: object
    legal_masks: object
    actions: object
    actors: object
    actor_trace: Tuple[int, ...]
    action_trace: Tuple[int, ...]
    legal_action_trace: Tuple[Tuple[int, ...], ...]
    cumulative_rewards: Tuple[float, ...]
    final_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    terminated: bool
    truncated: bool


@dataclass(frozen=True)
class _AllProjectUpdate:
    parameters: object
    seat_return_scales: Tuple[float, ...]
    decision_return_scales: Tuple[float, ...]
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]


@dataclass(frozen=True)
class MahJaxCategoricalMlpAllProjectPolicyGradientResult:
    """Immutable diagnostics from one shared all-project update."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    seed: int
    project_policy_id: str
    project_policy_seats: Tuple[int, ...]
    feature_count: int
    hidden_unit_count: int
    action_count: int
    parameter_count: int
    transition_cap: int
    learning_rate: float
    update_count: int
    training_result: MahJaxCategoricalMlpImitationResult
    pre_transition_count: int
    post_transition_count: int
    pre_seat_decision_counts: Tuple[int, ...]
    post_seat_decision_counts: Tuple[int, ...]
    pre_actor_trace: Tuple[int, ...]
    post_actor_trace: Tuple[int, ...]
    pre_action_trace: Tuple[int, ...]
    post_action_trace: Tuple[int, ...]
    pre_legal_action_trace: Tuple[Tuple[int, ...], ...]
    post_legal_action_trace: Tuple[Tuple[int, ...], ...]
    pre_cumulative_raw_rewards: Tuple[float, ...]
    post_cumulative_raw_rewards: Tuple[float, ...]
    pre_final_raw_rewards: Tuple[float, ...]
    post_final_raw_rewards: Tuple[float, ...]
    pre_final_scores: Tuple[int, ...]
    post_final_scores: Tuple[int, ...]
    seat_return_scales: Tuple[float, ...]
    decision_return_scales: Tuple[float, ...]
    initial_objective: float
    post_update_objective: float
    parameter_delta_l2: Tuple[float, ...]
    pre_terminated: bool
    post_terminated: bool
    pre_truncated: bool
    post_truncated: bool
    all_actions_legal: bool
    post_replay_identical: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _load_pinned_runtime():
    try:
        import jax
        import jax.numpy as jnp
        import mahjax
    except Exception as exc:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "pinned MahJax/JAX all-project update runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def _legal_actions(mask: object) -> Tuple[int, ...]:
    if str(getattr(mask, "dtype", "")) != "bool":
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        values = tuple(bool(value) for value in mask)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(values) != _ACTION_COUNT:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "state.legal_action_mask must contain exactly 87 actions"
        )
    actions = tuple(index for index, is_legal in enumerate(values) if is_legal)
    if not actions:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def _collect_all_project_round(parameters, jax, jnp, mahjax):
    try:
        init_key, policy_key = jax.random.split(
            jax.random.PRNGKey(
                MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED
            )
        )
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
        step_fn = jax.jit(environment.step)
    except Exception as exc:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "failed to initialize the shared all-project MahJax round"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != _ACTION_COUNT
    ):
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "all-project MahJax environment differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "all-project initial state must be active"
        )

    features = []
    masks = []
    actions = []
    actors = []
    legal_trace = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                "all-project rollout attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                "all-project rollout step_count must be monotonic"
            )
        actor = int(state.current_player)
        if actor < 0 or actor >= 4:
            raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                "all-project actor must be an exact seat index"
            )
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            public_features = _encode_observation_array(
                environment.observe(state),
                jnp,
            )
            logits = _mlp_logits(parameters, public_features, jax)
            if tuple(logits.shape) != (_ACTION_COUNT,) or not bool(
                jnp.all(jnp.isfinite(logits))
            ):
                raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                    "shared project policy must produce 87 finite logits"
                )
            policy_key, action_key = jax.random.split(policy_key)
            action = int(
                jax.random.categorical(
                    action_key,
                    jnp.where(state.legal_action_mask, logits, -jnp.inf),
                )
            )
        except MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError:
            raise
        except Exception as exc:
            raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                f"shared project policy failed at transition {transition_index}"
            ) from exc
        if action not in legal_actions:
            raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                f"shared project policy selected illegal action {action} at "
                f"transition {transition_index}"
            )
        features.append(public_features)
        masks.append(state.legal_action_mask)
        actions.append(action)
        actors.append(actor)
        legal_trace.append(legal_actions)
        try:
            state = jax.block_until_ready(step_fn(state, jnp.int32(action)))
        except Exception as exc:
            raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
                f"all-project step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            f"all-project round exceeded the {_TRANSITION_CAP}-transition cap"
        )

    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "all-project round must terminate without truncation"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "failed to read global seat-ordered scores"
        ) from exc
    if len(final_scores) != 4 or not features:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "terminal all-project round must expose four scores and decisions"
        )
    return _AllProjectTrajectory(
        features=jnp.stack(features),
        legal_masks=jnp.stack(masks),
        actions=jnp.asarray(actions, dtype=jnp.int32),
        actors=jnp.asarray(actors, dtype=jnp.int32),
        actor_trace=tuple(actors),
        action_trace=tuple(actions),
        legal_action_trace=tuple(legal_trace),
        cumulative_rewards=cumulative_rewards,
        final_rewards=_four_floats(state.rewards, "state.rewards"),
        final_scores=final_scores,
        terminated=True,
        truncated=False,
    )


def _apply_actor_indexed_raw_outcome_update(parameters, trajectory, jax, jnp):
    seat_returns = jnp.asarray(
        trajectory.cumulative_rewards,
        dtype=jnp.float32,
    ) / 100.0
    decision_returns = seat_returns[trajectory.actors]

    def objective(model_parameters):
        logits = _mlp_logits(model_parameters, trajectory.features, jax)
        legal_logits = jnp.where(trajectory.legal_masks, logits, -1e9)
        log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
        selected_log_probabilities = log_probabilities[
            jnp.arange(trajectory.actions.shape[0]),
            trajectory.actions,
        ]
        return -jnp.mean(decision_returns * selected_log_probabilities)

    objective_and_gradient = jax.jit(jax.value_and_grad(objective))
    initial_objective, gradients = objective_and_gradient(parameters)
    updated_parameters = tuple(
        value
        - MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE
        * gradient
        for value, gradient in zip(parameters, gradients)
    )
    updated_parameters = jax.block_until_ready(updated_parameters)
    return _AllProjectUpdate(
        parameters=updated_parameters,
        seat_return_scales=tuple(float(value) for value in seat_returns),
        decision_return_scales=tuple(float(value) for value in decision_returns),
        initial_objective=float(initial_objective),
        post_update_objective=float(objective(updated_parameters)),
        parameter_delta_l2=tuple(
            float(jnp.linalg.norm(updated - initial))
            for initial, updated in zip(parameters, updated_parameters)
        ),
    )


def _seat_decision_counts(actor_trace: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(actor_trace.count(seat) for seat in range(4))


def run_mahjax_categorical_mlp_all_project_policy_gradient_smoke(
) -> MahJaxCategoricalMlpAllProjectPolicyGradientResult:
    """Apply exactly one shared actor-indexed raw-outcome update in memory."""

    try:
        _, _, parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "reviewed categorical MLP in-memory training failed"
        ) from exc
    jax, jnp, mahjax = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    pre = _collect_all_project_round(parameters, jax, jnp, mahjax)
    pre_seat_counts = _seat_decision_counts(pre.actor_trace)
    if (
        len(pre.action_trace) != 77
        or pre_seat_counts != (21, 22, 17, 17)
        or pre.action_trace[:12] != _EXPECTED_FIRST_ACTIONS
        or pre.cumulative_rewards != (-20.0, 70.0, -20.0, -30.0)
        or pre.final_rewards != (-20.0, 80.0, -20.0, -20.0)
        or pre.final_scores != (230, 320, 230, 220)
    ):
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "seed-1 pre-update diagnostics differ from the reviewed probe"
        )

    update = _apply_actor_indexed_raw_outcome_update(
        parameters,
        pre,
        jax,
        jnp,
    )
    expected_deltas = (
        0.0009705852,
        0.0001615889,
        0.0023494314,
        0.0002528356,
    )
    diagnostics = (
        update.initial_objective,
        update.post_update_objective,
        *update.parameter_delta_l2,
    )
    if (
        not all(math.isfinite(value) for value in diagnostics)
        or any(
            abs(actual - expected) > 1e-6
            for actual, expected in zip(
                update.seat_return_scales,
                (-0.2, 0.7, -0.2, -0.3),
            )
        )
        or abs(update.initial_objective - 0.09366636) > 1e-5
        or abs(update.post_update_objective - 0.09301171) > 1e-5
        or update.post_update_objective >= update.initial_objective
        or any(
            abs(actual - expected) > 1e-5 or actual <= 0.0
            for actual, expected in zip(update.parameter_delta_l2, expected_deltas)
        )
    ):
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "shared update diagnostics differ from the reviewed probe"
        )

    post = _collect_all_project_round(update.parameters, jax, jnp, mahjax)
    post_seat_counts = _seat_decision_counts(post.actor_trace)
    post_replay_identical = (
        post.actor_trace == pre.actor_trace
        and post.action_trace == pre.action_trace
        and post.legal_action_trace == pre.legal_action_trace
        and post.cumulative_rewards == pre.cumulative_rewards
        and post.final_rewards == pre.final_rewards
        and post.final_scores == pre.final_scores
    )
    if post_seat_counts != pre_seat_counts or not post_replay_identical:
        raise MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError(
            "post-update replay diagnostics differ from the reviewed probe"
        )

    return MahJaxCategoricalMlpAllProjectPolicyGradientResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seed=MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED,
        project_policy_id=_PROJECT_POLICY_ID,
        project_policy_seats=(0, 1, 2, 3),
        feature_count=MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
        hidden_unit_count=_HIDDEN_UNIT_COUNT,
        action_count=_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        transition_cap=_TRANSITION_CAP,
        learning_rate=(
            MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE
        ),
        update_count=1,
        training_result=training_result,
        pre_transition_count=len(pre.action_trace),
        post_transition_count=len(post.action_trace),
        pre_seat_decision_counts=pre_seat_counts,
        post_seat_decision_counts=post_seat_counts,
        pre_actor_trace=pre.actor_trace,
        post_actor_trace=post.actor_trace,
        pre_action_trace=pre.action_trace,
        post_action_trace=post.action_trace,
        pre_legal_action_trace=pre.legal_action_trace,
        post_legal_action_trace=post.legal_action_trace,
        pre_cumulative_raw_rewards=pre.cumulative_rewards,
        post_cumulative_raw_rewards=post.cumulative_rewards,
        pre_final_raw_rewards=pre.final_rewards,
        post_final_raw_rewards=post.final_rewards,
        pre_final_scores=pre.final_scores,
        post_final_scores=post.final_scores,
        seat_return_scales=update.seat_return_scales,
        decision_return_scales=update.decision_return_scales,
        initial_objective=update.initial_objective,
        post_update_objective=update.post_update_objective,
        parameter_delta_l2=update.parameter_delta_l2,
        pre_terminated=pre.terminated,
        post_terminated=post.terminated,
        pre_truncated=pre.truncated,
        post_truncated=post.truncated,
        all_actions_legal=True,
        post_replay_identical=post_replay_identical,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED",
    "MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE",
    "MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError",
    "MahJaxCategoricalMlpAllProjectPolicyGradientResult",
    "run_mahjax_categorical_mlp_all_project_policy_gradient_smoke",
]
