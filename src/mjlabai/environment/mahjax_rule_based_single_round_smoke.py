"""Pinned MahJax bundled-rule-policy single-round smoke.

This module proves that MahJax's bundled red-riichi rule policy can drive all
four seats through one local terminal round using environment-owned legality.
It is not a learned model, training loop, production self-play system, or
strength evaluation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)


MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION = (
    "p4_mahjax_rule_based_single_round_smoke_v0.1"
)
MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP = 256

_EVIDENCE_GRADE = (
    "P4 pinned local rule-policy-to-environment single-round smoke evidence"
)
_WARNINGS = (
    "pinned MahJax v0.1.2 bundled rule-policy local CPU round only",
    "all four seats use the same bundled non-learned red-riichi rule policy",
    "environment-owned legal actions are checked before every transition",
    "raw environment rewards are recorded without shaping",
    "no real Tenhou, real haifu, external log or platform data",
    "no project model, learning, update, optimizer, checkpoint or training",
    "not production self-play, league or evaluation",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
    "not candidate-promotion evidence",
)


class MahJaxRuleBasedSingleRoundSmokeError(RuntimeError):
    """Raised when the pinned bundled-rule-policy round contract fails."""


@dataclass(frozen=True)
class MahJaxRuleBasedSingleRoundStep:
    """Immutable pre-transition policy and legality diagnostic."""

    pre_step_index: int
    acting_player: int
    legal_actions: Tuple[int, ...]
    selected_action: int


@dataclass(frozen=True)
class MahJaxRuleBasedSingleRoundResult:
    """Immutable diagnostics from one bundled-rule-policy round."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    policy_id: str
    seed: int
    transition_cap: int
    transition_count: int
    initial_player: int
    final_player: int
    final_step_count: int
    trace: Tuple[MahJaxRuleBasedSingleRoundStep, ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    terminated: bool
    truncated: bool
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
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "pinned MahJax/JAX bundled-rule-policy runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax, rule_based_player


def _legal_actions(value: object, expected_size: int) -> Tuple[int, ...]:
    if str(getattr(value, "dtype", "")) != "bool":
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        mask = tuple(bool(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(mask) != expected_size:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            f"state.legal_action_mask must contain exactly {expected_size} actions"
        )
    actions = tuple(index for index, is_legal in enumerate(mask) if is_legal)
    if not actions:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def run_mahjax_rule_based_single_round_smoke(
    seed: int = 0,
) -> MahJaxRuleBasedSingleRoundResult:
    """Run one four-seat bundled-rule-policy MahJax round under a hard cap."""

    if type(seed) is not int or seed < 0 or seed > 0xFFFFFFFF:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "seed must be an exact int from 0 through 4294967295"
        )

    jax, jnp, mahjax, rule_based_player = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    try:
        root_key = jax.random.PRNGKey(seed)
        init_key, policy_key = jax.random.split(root_key)
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "failed to initialize the pinned MahJax red-mahjong environment"
        ) from exc

    if environment.id != _MAHJAX_ENVIRONMENT_ID:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "unexpected MahJax environment id"
        )
    if environment.version != _MAHJAX_ENVIRONMENT_VERSION:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "unexpected MahJax environment version"
        )
    if environment.num_players != 4 or environment.num_actions != 87:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "MahJax environment must expose four players and 87 actions"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "initial MahJax state must be nonterminal and nontruncated"
        )

    initial_player = int(state.current_player)
    trace = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    policy_fn = jax.jit(rule_based_player)

    for transition_index in range(MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxRuleBasedSingleRoundSmokeError(
                "rollout attempted a policy action from a finished state"
            )
        pre_step_index = int(state.step_count)
        if pre_step_index != transition_index:
            raise MahJaxRuleBasedSingleRoundSmokeError(
                "MahJax step_count must match the deterministic transition index"
            )
        legal_actions = _legal_actions(
            state.legal_action_mask,
            environment.num_actions,
        )
        try:
            policy_key, action_key = jax.random.split(policy_key)
            selected_action = int(policy_fn(state, action_key))
        except Exception as exc:
            raise MahJaxRuleBasedSingleRoundSmokeError(
                f"bundled rule policy failed at transition {transition_index}"
            ) from exc
        if selected_action not in legal_actions:
            raise MahJaxRuleBasedSingleRoundSmokeError(
                f"bundled rule policy selected illegal action {selected_action} "
                f"at transition {transition_index}"
            )
        trace.append(
            MahJaxRuleBasedSingleRoundStep(
                pre_step_index=pre_step_index,
                acting_player=int(state.current_player),
                legal_actions=legal_actions,
                selected_action=selected_action,
            )
        )
        try:
            state = step_fn(state, jnp.int32(selected_action))
            state = jax.block_until_ready(state)
        except Exception as exc:
            raise MahJaxRuleBasedSingleRoundSmokeError(
                f"failed to execute MahJax transition {transition_index}"
            ) from exc
        if int(state.step_count) != pre_step_index + 1:
            raise MahJaxRuleBasedSingleRoundSmokeError(
                "MahJax transition must increment step_count exactly once"
            )
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "MahJax bundled rule-policy round exceeded the "
            f"{MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP}-transition cap"
        )

    terminated = bool(state.terminated)
    truncated = bool(state.truncated)
    if seed == 0 and (not terminated or truncated):
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "seed 0 must terminate without truncation before the transition cap"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "failed to read final global seat-ordered MahJax scores"
        ) from exc
    if len(final_scores) != 4:
        raise MahJaxRuleBasedSingleRoundSmokeError(
            "final global seat-ordered scores must contain exactly four values"
        )

    return MahJaxRuleBasedSingleRoundResult(
        smoke_version=MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        policy_id="mahjax.red_mahjong.players.rule_based_player@0.1.2",
        seed=seed,
        transition_cap=MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP,
        transition_count=len(trace),
        initial_player=initial_player,
        final_player=int(state.current_player),
        final_step_count=int(state.step_count),
        trace=tuple(trace),
        final_rewards=_four_floats(state.rewards, "state.rewards"),
        cumulative_rewards=cumulative_rewards,
        final_scores=final_scores,
        terminated=terminated,
        truncated=truncated,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_RULE_BASED_SINGLE_ROUND_SMOKE_VERSION",
    "MAHJAX_RULE_BASED_SINGLE_ROUND_TRANSITION_CAP",
    "MahJaxRuleBasedSingleRoundSmokeError",
    "MahJaxRuleBasedSingleRoundStep",
    "MahJaxRuleBasedSingleRoundResult",
    "run_mahjax_rule_based_single_round_smoke",
]
