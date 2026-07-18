"""One shared-policy update from two project seats in one MahJax round.

Seats 0 and 2 sample from the same reviewed in-memory project policy while
seats 1 and 3 remain fixed bundled rule policies. Each project decision uses
its acting seat's terminal cumulative raw reward. This bounded bridge is not
production self-play, evaluation, or model-strength evidence.
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
from mjlabai.environment.mahjax_linear_policy_round_smoke import (
    MAHJAX_LINEAR_POLICY_ACTION_COUNT,
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
    encode_mahjax_public_observation,
)
from mjlabai.rl.mahjax_one_round_policy_gradient_smoke import (
    _load_pinned_runtime,
)
from mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke import (
    MahJaxImitationTrainingResult,
    _train_mahjax_rule_policy_imitation_parameters,
)


MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION = (
    "p8_mahjax_two_project_seat_policy_gradient_smoke_v0.1"
)
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED = 0
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS = (0, 2)
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE = 0.1

_TRANSITION_CAP = 256
_RULE_POLICY_SEATS = (1, 3)
_PROJECT_POLICY_ID = "project_linear_630x87_imitation_seed_123_epoch_16_shared"
_RULE_POLICY_ID = "mahjax.red_mahjong.players.rule_based_player@0.1.2"
_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = (
    "P8 local two-project-seat shared-policy raw-outcome update smoke evidence only"
)
_WARNINGS = (
    "one two-project-seat shared-policy raw-outcome update smoke only",
    "project seats 0 and 2 share one in-memory policy",
    "rule-policy seats 1 and 3 remain fixed and never enter the gradient batch",
    "environment, rule and project RNG streams are independent",
    "all project actions are legal-masked categorical samples",
    "each project decision uses its acting seat cumulative raw reward divided by 100",
    "exactly one terminal round and exactly one aggregate shared-policy update",
    "no per-seat update, mid-round update, replay, critic or reward shaping",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "not four-project-seat or production self-play learning",
    "no evaluation, league, candidate promotion, real data or Tenhou",
    "not improvement, policy-quality, model-strength, stable-dan or LuckyJ evidence",
)


class MahJaxTwoProjectSeatPolicyGradientSmokeError(RuntimeError):
    """Raised when the exact two-project-seat update contract fails."""


@dataclass(frozen=True)
class MahJaxTwoProjectSeatPolicyGradientResult:
    """Immutable diagnostics from one shared two-project-seat update."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    seed: int
    project_seats: Tuple[int, ...]
    rule_policy_seats: Tuple[int, ...]
    project_policy_id: str
    rule_policy_id: str
    feature_count: int
    action_count: int
    parameter_count: int
    transition_cap: int
    learning_rate: float
    round_count: int
    update_count: int
    training_result: MahJaxImitationTrainingResult
    transition_count: int
    seat_decision_counts: Tuple[int, ...]
    project_decision_counts: Tuple[int, ...]
    project_decision_count: int
    actor_trace: Tuple[int, ...]
    action_trace: Tuple[int, ...]
    legal_action_trace: Tuple[Tuple[int, ...], ...]
    policy_id_trace: Tuple[str, ...]
    project_actor_trace: Tuple[int, ...]
    project_action_trace: Tuple[int, ...]
    cumulative_raw_rewards: Tuple[float, ...]
    final_raw_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    project_return_scales: Tuple[float, ...]
    initial_objective: float
    post_update_objective: float
    weight_delta_l2: float
    bias_delta_l2: float
    terminated: bool
    truncated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def _legal_actions(mask: object) -> Tuple[int, ...]:
    if str(getattr(mask, "dtype", "")) != "bool":
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        values = tuple(bool(value) for value in mask)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(values) != MAHJAX_LINEAR_POLICY_ACTION_COUNT:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "state.legal_action_mask must contain exactly 87 actions"
        )
    actions = tuple(index for index, is_legal in enumerate(values) if is_legal)
    if not actions:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def run_mahjax_two_project_seat_policy_gradient_smoke(
) -> MahJaxTwoProjectSeatPolicyGradientResult:
    """Apply one actor-indexed update from project seats 0 and 2."""

    try:
        _, _, weights, biases, training_result = (
            _train_mahjax_rule_policy_imitation_parameters()
        )
    except Exception as exc:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "reviewed in-memory imitation training failed"
        ) from exc
    try:
        jax, jnp, mahjax, rule_policy = _load_pinned_runtime()
    except Exception as exc:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "pinned MahJax/JAX two-project-seat runtime is unavailable"
        ) from exc
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    try:
        init_key, rule_key, project_key = jax.random.split(
            jax.random.PRNGKey(MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED),
            3,
        )
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "failed to initialize the two-project-seat MahJax round"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != MAHJAX_LINEAR_POLICY_ACTION_COUNT
    ):
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "two-project-seat environment differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "two-project-seat initial state must be active"
        )

    project_features = []
    project_masks = []
    project_actors = []
    project_actions = []
    actor_trace = []
    action_trace = []
    legal_trace = []
    policy_trace = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    score_fn = jax.jit(lambda values: values @ weights + biases)
    rule_fn = jax.jit(rule_policy)
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                "two-project-seat rollout attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                "two-project-seat rollout step_count must be monotonic"
            )
        actor = int(state.current_player)
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            if actor in MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS:
                public_features = jnp.asarray(
                    encode_mahjax_public_observation(environment.observe(state)),
                    dtype=jnp.float32,
                )
                scores = jax.block_until_ready(score_fn(public_features))
                if tuple(scores.shape) != (MAHJAX_LINEAR_POLICY_ACTION_COUNT,) or not bool(
                    jnp.all(jnp.isfinite(scores))
                ):
                    raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                        "project policy must produce exactly 87 finite logits"
                    )
                project_key, action_key = jax.random.split(project_key)
                action = int(
                    jax.random.categorical(
                        action_key,
                        jnp.where(state.legal_action_mask, scores, -jnp.inf),
                    )
                )
                project_features.append(public_features)
                project_masks.append(state.legal_action_mask)
                project_actors.append(actor)
                project_actions.append(action)
                policy_id = _PROJECT_POLICY_ID
            else:
                if actor not in _RULE_POLICY_SEATS:
                    raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                        f"unexpected participant seat {actor}"
                    )
                rule_key, action_key = jax.random.split(rule_key)
                action = int(rule_fn(state, action_key))
                policy_id = _RULE_POLICY_ID
        except MahJaxTwoProjectSeatPolicyGradientSmokeError:
            raise
        except Exception as exc:
            raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                f"two-project-seat participant failed at transition {transition_index}"
            ) from exc
        if action not in legal_actions:
            raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                f"participant selected illegal action {action} at transition "
                f"{transition_index}"
            )
        actor_trace.append(actor)
        action_trace.append(action)
        legal_trace.append(legal_actions)
        policy_trace.append(policy_id)
        try:
            state = jax.block_until_ready(step_fn(state, jnp.int32(action)))
        except Exception as exc:
            raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
                f"two-project-seat step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            f"two-project-seat round exceeded the {_TRANSITION_CAP}-transition cap"
        )

    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "two-project-seat round must terminate without truncation"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "failed to read global seat-ordered scores"
        ) from exc
    if len(final_scores) != 4 or not project_features:
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "terminal round must expose four scores and project decisions"
        )

    feature_batch = jnp.stack(project_features)
    mask_batch = jnp.stack(project_masks)
    actor_batch = jnp.asarray(project_actors, dtype=jnp.int32)
    action_batch = jnp.asarray(project_actions, dtype=jnp.int32)
    return_scales = jnp.asarray(cumulative_rewards, dtype=jnp.float32) / 100.0

    def objective(model_weights, model_biases):
        logits = feature_batch @ model_weights + model_biases
        legal_logits = jnp.where(mask_batch, logits, -1e9)
        log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
        selected_log_probabilities = log_probabilities[
            jnp.arange(action_batch.shape[0]),
            action_batch,
        ]
        return -jnp.mean(return_scales[actor_batch] * selected_log_probabilities)

    objective_and_gradient = jax.jit(
        jax.value_and_grad(objective, argnums=(0, 1))
    )
    initial_objective_array, gradients = objective_and_gradient(weights, biases)
    updated_weights = (
        weights
        - MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE * gradients[0]
    )
    updated_biases = (
        biases
        - MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE * gradients[1]
    )
    updated_weights, updated_biases = jax.block_until_ready(
        (updated_weights, updated_biases)
    )
    initial_objective = float(initial_objective_array)
    post_update_objective = float(objective(updated_weights, updated_biases))
    weight_delta_l2 = float(jnp.linalg.norm(updated_weights - weights))
    bias_delta_l2 = float(jnp.linalg.norm(updated_biases - biases))
    diagnostics = (
        initial_objective,
        post_update_objective,
        weight_delta_l2,
        bias_delta_l2,
    )
    seat_counts = tuple(actor_trace.count(seat) for seat in range(4))
    project_counts = tuple(
        project_actors.count(seat)
        for seat in MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS
    )
    if not all(math.isfinite(value) for value in diagnostics):
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "two-project-seat update diagnostics must all be finite"
        )
    if (
        len(action_trace) != 92
        or seat_counts != (21, 22, 23, 26)
        or project_counts != (21, 23)
        or len(project_actions) != 44
        or cumulative_rewards != (-10.0, -10.0, -10.0, 20.0)
        or _four_floats(state.rewards, "state.rewards")
        != (-10.0, -10.0, -10.0, 30.0)
        or final_scores != (240, 240, 240, 270)
        or abs(float(return_scales[0]) - (-0.1)) > 1e-6
        or abs(float(return_scales[2]) - (-0.1)) > 1e-6
        or abs(initial_objective - (-0.19244556)) > 1e-5
        or abs(post_update_objective - (-0.19273609)) > 1e-5
        or abs(weight_delta_l2 - 0.00523261) > 1e-5
        or abs(bias_delta_l2 - 0.00124493) > 1e-5
        or weight_delta_l2 <= 0.0
        or bias_delta_l2 <= 0.0
    ):
        raise MahJaxTwoProjectSeatPolicyGradientSmokeError(
            "two-project-seat diagnostics differ from the reviewed probe"
        )

    return MahJaxTwoProjectSeatPolicyGradientResult(
        smoke_version=MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seed=MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED,
        project_seats=MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS,
        rule_policy_seats=_RULE_POLICY_SEATS,
        project_policy_id=_PROJECT_POLICY_ID,
        rule_policy_id=_RULE_POLICY_ID,
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        transition_cap=_TRANSITION_CAP,
        learning_rate=MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE,
        round_count=1,
        update_count=1,
        training_result=training_result,
        transition_count=len(action_trace),
        seat_decision_counts=seat_counts,
        project_decision_counts=project_counts,
        project_decision_count=len(project_actions),
        actor_trace=tuple(actor_trace),
        action_trace=tuple(action_trace),
        legal_action_trace=tuple(legal_trace),
        policy_id_trace=tuple(policy_trace),
        project_actor_trace=tuple(project_actors),
        project_action_trace=tuple(project_actions),
        cumulative_raw_rewards=cumulative_rewards,
        final_raw_rewards=_four_floats(state.rewards, "state.rewards"),
        final_scores=final_scores,
        project_return_scales=(float(return_scales[0]), float(return_scales[2])),
        initial_objective=initial_objective,
        post_update_objective=post_update_objective,
        weight_delta_l2=weight_delta_l2,
        bias_delta_l2=bias_delta_l2,
        terminated=True,
        truncated=False,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION",
    "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED",
    "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS",
    "MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE",
    "MahJaxTwoProjectSeatPolicyGradientSmokeError",
    "MahJaxTwoProjectSeatPolicyGradientResult",
    "run_mahjax_two_project_seat_policy_gradient_smoke",
]
