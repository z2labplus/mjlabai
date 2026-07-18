"""One on-policy MahJax raw-outcome gradient update smoke.

The reviewed imitation policy samples seat-0 actions from its legal-masked
categorical distribution against three fixed bundled rule-policy seats. One
terminal raw return drives exactly one in-memory policy-gradient update. This is
not self-play learning, evaluation, or model-strength evidence.
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
from mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke import (
    MahJaxImitationTrainingResult,
    _train_mahjax_rule_policy_imitation_parameters,
)


MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION = (
    "p8_mahjax_one_round_policy_gradient_smoke_v0.1"
)
MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED = 1
MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE = 0.1

_TRANSITION_CAP = 256
_PROJECT_SEAT = 0
_PROJECT_POLICY_ID = "project_linear_630x87_imitation_seed_123_epoch_16"
_RULE_POLICY_ID = "mahjax.red_mahjong.players.rule_based_player@0.1.2"
_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = (
    "P8 local one-round on-policy raw-outcome gradient-update smoke evidence only"
)
_WARNINGS = (
    "first environment raw-outcome policy-gradient update smoke only",
    "one seed-1 round and exactly one gradient update",
    "project seat 0 samples from the legal-masked categorical policy",
    "environment, bundled-rule and project-action RNG streams are independent",
    "seats 1, 2 and 3 remain fixed bundled non-learned rule policies",
    "return is only cumulative raw seat-0 reward divided by 100",
    "no baseline, discount, bootstrapping, critic, replay or reward shaping",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "no self-play learning, multiple rounds, seat rotation, evaluation or league",
    "no real Tenhou, real haifu, external log or platform data",
    "not improvement, policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxOneRoundPolicyGradientSmokeError(RuntimeError):
    """Raised when the exact one-round policy-gradient contract fails."""


@dataclass(frozen=True)
class _RoundTrajectory:
    features: object
    legal_masks: object
    project_actions: object
    actor_trace: Tuple[int, ...]
    action_trace: Tuple[int, ...]
    legal_action_trace: Tuple[Tuple[int, ...], ...]
    policy_id_trace: Tuple[str, ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    terminated: bool
    truncated: bool


@dataclass(frozen=True)
class _PolicyGradientUpdate:
    weights: object
    biases: object
    return_scale: float
    initial_objective: float
    post_update_objective: float
    weight_delta_l2: float
    bias_delta_l2: float


@dataclass(frozen=True)
class MahJaxOneRoundPolicyGradientResult:
    """Immutable diagnostics from one raw-outcome gradient update."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    seed: int
    project_policy_seat: int
    project_policy_id: str
    rule_policy_seats: Tuple[int, ...]
    rule_policy_id: str
    feature_count: int
    action_count: int
    parameter_count: int
    transition_cap: int
    learning_rate: float
    update_count: int
    training_result: MahJaxImitationTrainingResult
    project_decision_count: int
    sampled_project_actions: Tuple[int, ...]
    cumulative_raw_project_reward: float
    return_scale: float
    initial_objective: float
    post_update_objective: float
    weight_delta_l2: float
    bias_delta_l2: float
    pre_transition_count: int
    post_transition_count: int
    pre_actor_trace: Tuple[int, ...]
    post_actor_trace: Tuple[int, ...]
    pre_action_trace: Tuple[int, ...]
    post_action_trace: Tuple[int, ...]
    pre_legal_action_trace: Tuple[Tuple[int, ...], ...]
    post_legal_action_trace: Tuple[Tuple[int, ...], ...]
    pre_policy_id_trace: Tuple[str, ...]
    post_policy_id_trace: Tuple[str, ...]
    pre_final_rewards: Tuple[float, ...]
    post_final_rewards: Tuple[float, ...]
    pre_cumulative_rewards: Tuple[float, ...]
    post_cumulative_rewards: Tuple[float, ...]
    pre_final_scores: Tuple[int, ...]
    post_final_scores: Tuple[int, ...]
    pre_terminated: bool
    post_terminated: bool
    pre_truncated: bool
    post_truncated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _load_pinned_runtime():
    try:
        import jax
        import jax.numpy as jnp
        import mahjax
        from mahjax.red_mahjong.players import rule_based_player
    except Exception as exc:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "pinned MahJax/JAX policy-gradient runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax, rule_based_player


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def _legal_actions(mask: object) -> Tuple[int, ...]:
    if str(getattr(mask, "dtype", "")) != "bool":
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        values = tuple(bool(value) for value in mask)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(values) != MAHJAX_LINEAR_POLICY_ACTION_COUNT:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "state.legal_action_mask must contain exactly 87 actions"
        )
    actions = tuple(index for index, is_legal in enumerate(values) if is_legal)
    if not actions:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def _collect_on_policy_round(seed, weights, biases, jax, jnp, mahjax, rule_policy):
    try:
        init_key, rule_key, project_key = jax.random.split(
            jax.random.PRNGKey(seed),
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
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "failed to initialize the on-policy MahJax round"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != MAHJAX_LINEAR_POLICY_ACTION_COUNT
    ):
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "on-policy MahJax environment differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "on-policy initial state must be active"
        )

    features = []
    masks = []
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
            raise MahJaxOneRoundPolicyGradientSmokeError(
                "on-policy rollout attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxOneRoundPolicyGradientSmokeError(
                "on-policy rollout step_count must be monotonic"
            )
        actor = int(state.current_player)
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            if actor == _PROJECT_SEAT:
                public_features = jnp.asarray(
                    encode_mahjax_public_observation(environment.observe(state)),
                    dtype=jnp.float32,
                )
                scores = jax.block_until_ready(score_fn(public_features))
                if tuple(scores.shape) != (MAHJAX_LINEAR_POLICY_ACTION_COUNT,) or not bool(
                    jnp.all(jnp.isfinite(scores))
                ):
                    raise MahJaxOneRoundPolicyGradientSmokeError(
                        "project policy must produce exactly 87 finite logits"
                    )
                project_key, action_key = jax.random.split(project_key)
                action = int(
                    jax.random.categorical(
                        action_key,
                        jnp.where(state.legal_action_mask, scores, -jnp.inf),
                    )
                )
                features.append(public_features)
                masks.append(state.legal_action_mask)
                project_actions.append(action)
                policy_id = _PROJECT_POLICY_ID
            else:
                rule_key, action_key = jax.random.split(rule_key)
                action = int(rule_fn(state, action_key))
                policy_id = _RULE_POLICY_ID
        except MahJaxOneRoundPolicyGradientSmokeError:
            raise
        except Exception as exc:
            raise MahJaxOneRoundPolicyGradientSmokeError(
                f"on-policy participant failed at transition {transition_index}"
            ) from exc
        if action not in legal_actions:
            raise MahJaxOneRoundPolicyGradientSmokeError(
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
            raise MahJaxOneRoundPolicyGradientSmokeError(
                f"on-policy environment step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            f"on-policy round exceeded the {_TRANSITION_CAP}-transition cap"
        )

    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "on-policy round must terminate without truncation"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "failed to read global seat-ordered scores"
        ) from exc
    if len(final_scores) != 4 or not features:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "terminal round must expose four scores and project decisions"
        )
    return _RoundTrajectory(
        features=jnp.stack(features),
        legal_masks=jnp.stack(masks),
        project_actions=jnp.asarray(project_actions, dtype=jnp.int32),
        actor_trace=tuple(actor_trace),
        action_trace=tuple(action_trace),
        legal_action_trace=tuple(legal_trace),
        policy_id_trace=tuple(policy_trace),
        final_rewards=_four_floats(state.rewards, "state.rewards"),
        cumulative_rewards=cumulative_rewards,
        final_scores=final_scores,
        terminated=True,
        truncated=False,
    )


def _apply_one_raw_outcome_update(weights, biases, trajectory, jax, jnp):
    return_scale_array = jnp.float32(
        trajectory.cumulative_rewards[_PROJECT_SEAT] / 100.0
    )

    def objective(model_weights, model_biases):
        logits = trajectory.features @ model_weights + model_biases
        legal_logits = jnp.where(trajectory.legal_masks, logits, -1e9)
        log_probabilities = jax.nn.log_softmax(legal_logits, axis=1)
        selected_log_probabilities = log_probabilities[
            jnp.arange(trajectory.project_actions.shape[0]),
            trajectory.project_actions,
        ]
        return -return_scale_array * jnp.mean(selected_log_probabilities)

    objective_and_gradient = jax.jit(
        jax.value_and_grad(objective, argnums=(0, 1))
    )
    initial_objective_array, gradients = objective_and_gradient(weights, biases)
    updated_weights = (
        weights - MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE * gradients[0]
    )
    updated_biases = (
        biases - MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE * gradients[1]
    )
    updated_weights, updated_biases = jax.block_until_ready(
        (updated_weights, updated_biases)
    )
    return _PolicyGradientUpdate(
        weights=updated_weights,
        biases=updated_biases,
        return_scale=float(return_scale_array),
        initial_objective=float(initial_objective_array),
        post_update_objective=float(objective(updated_weights, updated_biases)),
        weight_delta_l2=float(jnp.linalg.norm(updated_weights - weights)),
        bias_delta_l2=float(jnp.linalg.norm(updated_biases - biases)),
    )


def run_mahjax_one_round_policy_gradient_smoke(
) -> MahJaxOneRoundPolicyGradientResult:
    """Apply exactly one raw-outcome policy-gradient update in memory."""

    try:
        _, _, weights, biases, training_result = (
            _train_mahjax_rule_policy_imitation_parameters()
        )
    except Exception as exc:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "reviewed in-memory imitation training failed"
        ) from exc
    jax, jnp, mahjax, rule_policy = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxOneRoundPolicyGradientSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    pre = _collect_on_policy_round(
        MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED,
        weights,
        biases,
        jax,
        jnp,
        mahjax,
        rule_policy,
    )
    sampled_actions = tuple(int(value) for value in pre.project_actions.tolist())
    if (
        len(pre.action_trace) != 37
        or sampled_actions != (20, 84, 16, 30, 27, 26, 3, 13)
        or pre.cumulative_rewards != (-39.0, 39.0, 0.0, 0.0)
        or pre.final_rewards != (-39.0, 39.0, 0.0, 0.0)
        or pre.final_scores != (211, 289, 250, 250)
    ):
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "seed-1 pre-update diagnostics differ from the reviewed probe"
        )

    update = _apply_one_raw_outcome_update(weights, biases, pre, jax, jnp)
    updated_weights = update.weights
    updated_biases = update.biases
    initial_objective = update.initial_objective
    post_update_objective = update.post_update_objective
    weight_delta_l2 = update.weight_delta_l2
    bias_delta_l2 = update.bias_delta_l2

    post = _collect_on_policy_round(
        MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED,
        updated_weights,
        updated_biases,
        jax,
        jnp,
        mahjax,
        rule_policy,
    )
    diagnostics = (
        update.return_scale,
        initial_objective,
        post_update_objective,
        weight_delta_l2,
        bias_delta_l2,
    )
    if not all(math.isfinite(value) for value in diagnostics):
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "policy-gradient diagnostics must all be finite"
        )
    if (
        abs(update.return_scale - (-0.39)) > 1e-6
        or abs(initial_objective - (-0.86367577)) > 1e-5
        or abs(post_update_objective - (-0.88331068)) > 1e-5
        or abs(weight_delta_l2 - 0.04220101) > 1e-5
        or abs(bias_delta_l2 - 0.01279154) > 1e-5
        or weight_delta_l2 <= 0.0
        or bias_delta_l2 <= 0.0
        or post.action_trace != pre.action_trace
        or post.legal_action_trace != pre.legal_action_trace
        or post.final_rewards != pre.final_rewards
        or post.cumulative_rewards != pre.cumulative_rewards
        or post.final_scores != pre.final_scores
    ):
        raise MahJaxOneRoundPolicyGradientSmokeError(
            "one-step update diagnostics differ from the reviewed probe"
        )

    return MahJaxOneRoundPolicyGradientResult(
        smoke_version=MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seed=MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED,
        project_policy_seat=_PROJECT_SEAT,
        project_policy_id=_PROJECT_POLICY_ID,
        rule_policy_seats=(1, 2, 3),
        rule_policy_id=_RULE_POLICY_ID,
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        transition_cap=_TRANSITION_CAP,
        learning_rate=MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE,
        update_count=1,
        training_result=training_result,
        project_decision_count=len(sampled_actions),
        sampled_project_actions=sampled_actions,
        cumulative_raw_project_reward=pre.cumulative_rewards[_PROJECT_SEAT],
        return_scale=update.return_scale,
        initial_objective=initial_objective,
        post_update_objective=post_update_objective,
        weight_delta_l2=weight_delta_l2,
        bias_delta_l2=bias_delta_l2,
        pre_transition_count=len(pre.action_trace),
        post_transition_count=len(post.action_trace),
        pre_actor_trace=pre.actor_trace,
        post_actor_trace=post.actor_trace,
        pre_action_trace=pre.action_trace,
        post_action_trace=post.action_trace,
        pre_legal_action_trace=pre.legal_action_trace,
        post_legal_action_trace=post.legal_action_trace,
        pre_policy_id_trace=pre.policy_id_trace,
        post_policy_id_trace=post.policy_id_trace,
        pre_final_rewards=pre.final_rewards,
        post_final_rewards=post.final_rewards,
        pre_cumulative_rewards=pre.cumulative_rewards,
        post_cumulative_rewards=post.cumulative_rewards,
        pre_final_scores=pre.final_scores,
        post_final_scores=post.final_scores,
        pre_terminated=pre.terminated,
        post_terminated=post.terminated,
        pre_truncated=pre.truncated,
        post_truncated=post.truncated,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION",
    "MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED",
    "MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE",
    "MahJaxOneRoundPolicyGradientSmokeError",
    "MahJaxOneRoundPolicyGradientResult",
    "run_mahjax_one_round_policy_gradient_smoke",
]
