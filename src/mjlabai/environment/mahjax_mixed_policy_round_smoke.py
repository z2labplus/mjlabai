"""One MahJax round with one trained project seat and three rule-policy seats.

Seat 0 uses the reviewed in-memory trained linear policy. Seats 1 through 3 use
MahJax's pinned bundled rule policy. Every action is checked against environment
legality and raw outcomes are preserved without learning or strength claims.
"""

from __future__ import annotations

from dataclasses import dataclass
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


MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION = (
    "p8_mahjax_trained_project_rule_policy_mixed_round_smoke_v0.1"
)
MAHJAX_MIXED_POLICY_ROUND_SEED = 0

_TRANSITION_CAP = 256
_PROJECT_SEAT = 0
_PROJECT_POLICY_ID = "project_linear_630x87_imitation_seed_123_epoch_16"
_RULE_POLICY_ID = "mahjax.red_mahjong.players.rule_based_player@0.1.2"
_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = "P8 local mixed-policy single-round interaction smoke evidence only"
_WARNINGS = (
    "one trained-project-seat versus three bundled-rule-seats local round only",
    "seat 0 uses reviewed in-memory imitation parameters",
    "seats 1, 2 and 3 use the pinned bundled non-learned rule policy",
    "environment legal mask is authoritative before every action",
    "raw environment rewards and global seat scores are preserved",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "no reward objective, reinforcement-learning update or self-play learning",
    "no multiple rounds, seat rotation, aggregate evaluation or league",
    "no real Tenhou, real haifu, external log or platform data",
    "not production self-play, evaluation or candidate promotion",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxMixedPolicyRoundSmokeError(RuntimeError):
    """Raised when the exact mixed-policy round contract fails."""


@dataclass(frozen=True)
class MahJaxMixedPolicyRoundStep:
    """Immutable seat, policy and legality diagnostic before one transition."""

    pre_step_index: int
    acting_player: int
    policy_id: str
    legal_actions: Tuple[int, ...]
    selected_action: int


@dataclass(frozen=True)
class MahJaxMixedPolicyRoundResult:
    """Immutable diagnostics from the exact one-project/three-rule round."""

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
    transition_count: int
    project_policy_turn_count: int
    rule_policy_turn_count: int
    trace: Tuple[MahJaxMixedPolicyRoundStep, ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    terminated: bool
    truncated: bool
    training_result: MahJaxImitationTrainingResult
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
        raise MahJaxMixedPolicyRoundSmokeError(
            "pinned MahJax/JAX mixed-policy runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax, rule_based_player


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxMixedPolicyRoundSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxMixedPolicyRoundSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def _legal_actions(mask: object) -> Tuple[int, ...]:
    if str(getattr(mask, "dtype", "")) != "bool":
        raise MahJaxMixedPolicyRoundSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        values = tuple(bool(value) for value in mask)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxMixedPolicyRoundSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(values) != MAHJAX_LINEAR_POLICY_ACTION_COUNT:
        raise MahJaxMixedPolicyRoundSmokeError(
            "state.legal_action_mask must contain exactly 87 actions"
        )
    actions = tuple(index for index, is_legal in enumerate(values) if is_legal)
    if not actions:
        raise MahJaxMixedPolicyRoundSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def run_mahjax_mixed_policy_round_smoke() -> MahJaxMixedPolicyRoundResult:
    """Run the exact trained-seat-0 versus rule-seats-1/2/3 local round."""

    try:
        _, _, trained_weights, trained_biases, training_result = (
            _train_mahjax_rule_policy_imitation_parameters()
        )
    except Exception as exc:
        raise MahJaxMixedPolicyRoundSmokeError(
            "reviewed in-memory imitation training failed"
        ) from exc

    jax, jnp, mahjax, rule_based_player = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxMixedPolicyRoundSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )
    try:
        root_key = jax.random.PRNGKey(MAHJAX_MIXED_POLICY_ROUND_SEED)
        init_key, policy_key = jax.random.split(root_key)
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxMixedPolicyRoundSmokeError(
            "failed to initialize the mixed-policy MahJax environment"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != MAHJAX_LINEAR_POLICY_ACTION_COUNT
    ):
        raise MahJaxMixedPolicyRoundSmokeError(
            "mixed-policy MahJax environment differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxMixedPolicyRoundSmokeError(
            "mixed-policy initial state must be active"
        )

    trace = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    project_score_fn = jax.jit(
        lambda features: features @ trained_weights + trained_biases
    )
    rule_policy_fn = jax.jit(rule_based_player)
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxMixedPolicyRoundSmokeError(
                "mixed-policy rollout attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxMixedPolicyRoundSmokeError(
                "mixed-policy rollout step_count must be monotonic"
            )
        acting_player = int(state.current_player)
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            if acting_player == _PROJECT_SEAT:
                features = jnp.asarray(
                    encode_mahjax_public_observation(environment.observe(state)),
                    dtype=jnp.float32,
                )
                scores = jax.block_until_ready(project_score_fn(features))
                if tuple(scores.shape) != (MAHJAX_LINEAR_POLICY_ACTION_COUNT,) or not bool(
                    jnp.all(jnp.isfinite(scores))
                ):
                    raise MahJaxMixedPolicyRoundSmokeError(
                        "project policy must produce exactly 87 finite scores"
                    )
                selected_action = int(
                    jnp.argmax(
                        jnp.where(state.legal_action_mask, scores, -jnp.inf)
                    )
                )
                policy_id = _PROJECT_POLICY_ID
            else:
                policy_key, action_key = jax.random.split(policy_key)
                selected_action = int(rule_policy_fn(state, action_key))
                policy_id = _RULE_POLICY_ID
        except MahJaxMixedPolicyRoundSmokeError:
            raise
        except Exception as exc:
            raise MahJaxMixedPolicyRoundSmokeError(
                f"mixed policy failed at transition {transition_index}"
            ) from exc
        if selected_action not in legal_actions:
            raise MahJaxMixedPolicyRoundSmokeError(
                f"policy selected illegal action {selected_action} at transition "
                f"{transition_index}"
            )
        trace.append(
            MahJaxMixedPolicyRoundStep(
                pre_step_index=transition_index,
                acting_player=acting_player,
                policy_id=policy_id,
                legal_actions=legal_actions,
                selected_action=selected_action,
            )
        )
        try:
            state = jax.block_until_ready(
                step_fn(state, jnp.int32(selected_action))
            )
        except Exception as exc:
            raise MahJaxMixedPolicyRoundSmokeError(
                f"mixed-policy environment step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxMixedPolicyRoundSmokeError(
            f"mixed-policy round exceeded the {_TRANSITION_CAP}-transition cap"
        )

    terminated = bool(state.terminated)
    truncated = bool(state.truncated)
    if not terminated or truncated:
        raise MahJaxMixedPolicyRoundSmokeError(
            "mixed-policy round must terminate without truncation"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxMixedPolicyRoundSmokeError(
            "failed to read global seat-ordered scores"
        ) from exc
    if len(final_scores) != 4:
        raise MahJaxMixedPolicyRoundSmokeError(
            "global seat-ordered scores must contain four values"
        )
    project_steps = tuple(step for step in trace if step.acting_player == _PROJECT_SEAT)
    final_rewards = _four_floats(state.rewards, "state.rewards")
    if (
        len(trace) != 54
        or len(project_steps) != 10
        or any(step.selected_action != 71 for step in project_steps)
        or final_rewards != (0.0, 0.0, 140.0, -120.0)
        or cumulative_rewards != (0.0, 0.0, 120.0, -140.0)
        or final_scores != (250, 250, 380, 120)
    ):
        raise MahJaxMixedPolicyRoundSmokeError(
            "mixed-policy seed-0 diagnostics differ from the reviewed probe"
        )

    return MahJaxMixedPolicyRoundResult(
        smoke_version=MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seed=MAHJAX_MIXED_POLICY_ROUND_SEED,
        project_policy_seat=_PROJECT_SEAT,
        project_policy_id=_PROJECT_POLICY_ID,
        rule_policy_seats=(1, 2, 3),
        rule_policy_id=_RULE_POLICY_ID,
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        transition_cap=_TRANSITION_CAP,
        transition_count=len(trace),
        project_policy_turn_count=len(project_steps),
        rule_policy_turn_count=len(trace) - len(project_steps),
        trace=tuple(trace),
        final_rewards=final_rewards,
        cumulative_rewards=cumulative_rewards,
        final_scores=final_scores,
        terminated=terminated,
        truncated=truncated,
        training_result=training_result,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_MIXED_POLICY_ROUND_SMOKE_VERSION",
    "MAHJAX_MIXED_POLICY_ROUND_SEED",
    "MahJaxMixedPolicyRoundSmokeError",
    "MahJaxMixedPolicyRoundStep",
    "MahJaxMixedPolicyRoundResult",
    "run_mahjax_mixed_policy_round_smoke",
]
