"""Deterministic pinned-MahJax single-round rollout smoke.

The helper exercises one complete local round through MahJax-owned legal
masks and transitions. It intentionally has no model, policy callback,
reward shaping, persistence, or multi-game orchestration.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)


MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION = (
    "p4_mahjax_single_round_rollout_smoke_v0.1"
)
MAHJAX_SINGLE_ROUND_TRANSITION_CAP = 256

_EVIDENCE_GRADE = "P4 pinned local single-round environment rollout smoke evidence"
_WARNINGS = (
    "pinned MahJax v0.1.2 local CPU single-round rollout smoke only",
    "deterministic lowest-legal-action diagnostic policy only",
    "not full Tenhou-rule conformance or complete gameplay evidence",
    "no real Tenhou, real haifu, external log or platform data",
    "no model output, learning, training, production self-play or league",
    "raw environment rewards are recorded without shaping",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
    "not candidate-promotion evidence",
)


class MahJaxSingleRoundRolloutSmokeError(RuntimeError):
    """Raised when the bounded pinned-MahJax rollout contract fails."""


@dataclass(frozen=True)
class MahJaxSingleRoundStep:
    """Immutable pre-transition diagnostic from one legal MahJax step."""

    pre_step_index: int
    acting_player: int
    legal_actions: Tuple[int, ...]
    selected_action: int


@dataclass(frozen=True)
class MahJaxSingleRoundRolloutResult:
    """Immutable diagnostics from one complete bounded MahJax round."""

    rollout_version: str
    package_version: str
    environment_id: str
    environment_version: str
    seed: int
    transition_cap: int
    transition_count: int
    initial_player: int
    final_player: int
    final_step_count: int
    trace: Tuple[MahJaxSingleRoundStep, ...]
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
    except Exception as exc:
        raise MahJaxSingleRoundRolloutSmokeError(
            "pinned MahJax/JAX runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax


def _legal_actions(value: object, expected_size: int) -> Tuple[int, ...]:
    if str(getattr(value, "dtype", "")) != "bool":
        raise MahJaxSingleRoundRolloutSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        mask = tuple(bool(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxSingleRoundRolloutSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(mask) != expected_size:
        raise MahJaxSingleRoundRolloutSmokeError(
            f"state.legal_action_mask must contain exactly {expected_size} actions"
        )
    legal_actions = tuple(
        action_index for action_index, is_legal in enumerate(mask) if is_legal
    )
    if not legal_actions:
        raise MahJaxSingleRoundRolloutSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return legal_actions


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxSingleRoundRolloutSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxSingleRoundRolloutSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def run_mahjax_single_round_rollout_smoke(
    seed: int = 0,
) -> MahJaxSingleRoundRolloutResult:
    """Run one lowest-legal-action MahJax round under a hard transition cap."""

    if type(seed) is not int or seed < 0 or seed > 0xFFFFFFFF:
        raise MahJaxSingleRoundRolloutSmokeError(
            "seed must be an exact int from 0 through 4294967295"
        )

    jax, jnp, mahjax = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxSingleRoundRolloutSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    try:
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(jax.random.PRNGKey(seed))
    except Exception as exc:
        raise MahJaxSingleRoundRolloutSmokeError(
            "failed to initialize the pinned MahJax red-mahjong environment"
        ) from exc

    if environment.id != _MAHJAX_ENVIRONMENT_ID:
        raise MahJaxSingleRoundRolloutSmokeError("unexpected MahJax environment id")
    if environment.version != _MAHJAX_ENVIRONMENT_VERSION:
        raise MahJaxSingleRoundRolloutSmokeError(
            "unexpected MahJax environment version"
        )
    if environment.num_players != 4 or environment.num_actions != 87:
        raise MahJaxSingleRoundRolloutSmokeError(
            "MahJax environment must expose four players and 87 actions"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxSingleRoundRolloutSmokeError(
            "initial MahJax state must be nonterminal and nontruncated"
        )

    initial_player = int(state.current_player)
    trace = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)

    for transition_index in range(MAHJAX_SINGLE_ROUND_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxSingleRoundRolloutSmokeError(
                "rollout attempted a transition from a finished state"
            )
        pre_step_index = int(state.step_count)
        if pre_step_index != transition_index:
            raise MahJaxSingleRoundRolloutSmokeError(
                "MahJax step_count must match the deterministic transition index"
            )
        legal_actions = _legal_actions(
            state.legal_action_mask,
            environment.num_actions,
        )
        selected_action = legal_actions[0]
        trace.append(
            MahJaxSingleRoundStep(
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
            raise MahJaxSingleRoundRolloutSmokeError(
                f"failed to execute MahJax transition {transition_index}"
            ) from exc
        if int(state.step_count) != pre_step_index + 1:
            raise MahJaxSingleRoundRolloutSmokeError(
                "MahJax transition must increment step_count exactly once"
            )
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxSingleRoundRolloutSmokeError(
            f"MahJax round exceeded the {MAHJAX_SINGLE_ROUND_TRANSITION_CAP}-transition cap"
        )

    terminated = bool(state.terminated)
    truncated = bool(state.truncated)
    if seed == 0 and (not terminated or truncated):
        raise MahJaxSingleRoundRolloutSmokeError(
            "seed 0 must terminate without truncation before the transition cap"
        )

    try:
        final_observation = environment.observe(state)
        final_scores = tuple(int(value) for value in final_observation["scores"])
    except Exception as exc:
        raise MahJaxSingleRoundRolloutSmokeError(
            "failed to read final scores from the public MahJax observation"
        ) from exc
    if len(final_scores) != 4:
        raise MahJaxSingleRoundRolloutSmokeError(
            "final observation scores must contain exactly four values"
        )

    return MahJaxSingleRoundRolloutResult(
        rollout_version=MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seed=seed,
        transition_cap=MAHJAX_SINGLE_ROUND_TRANSITION_CAP,
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
    "MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION",
    "MAHJAX_SINGLE_ROUND_TRANSITION_CAP",
    "MahJaxSingleRoundRolloutSmokeError",
    "MahJaxSingleRoundStep",
    "MahJaxSingleRoundRolloutResult",
    "run_mahjax_single_round_rollout_smoke",
]
