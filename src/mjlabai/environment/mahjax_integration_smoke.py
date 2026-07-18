"""Pinned MahJax P4 local environment integration smoke.

This module proves that the selected third-party riichi environment owns a
legal-action mask, observation, and one executable state transition. It is not
a project action adapter, episode runner, self-play loop, or training system.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


MAHJAX_INTEGRATION_SMOKE_VERSION = "p4_mahjax_integration_smoke_v0.1"
MAHJAX_PACKAGE_VERSION = "0.1.2"
MAHJAX_ENVIRONMENT_ID = "red_mahjong"
MAHJAX_ENVIRONMENT_VERSION = "beta"

_EXPECTED_OBSERVATION_KEYS = frozenset(
    {
        "action_history",
        "dora_indicators",
        "furiten",
        "hand",
        "honba",
        "kyotaku",
        "last_draw",
        "prevalent_wind",
        "round",
        "scores",
        "seat_wind",
        "shanten_count",
    }
)
_EVIDENCE_GRADE = (
    "P4 pinned third-party local riichi environment integration smoke evidence only"
)
_WARNINGS = (
    "pinned MahJax v0.1.2 local CPU integration smoke only",
    "one environment-owned legal action and one state transition only",
    "not full Tenhou-rule conformance or complete gameplay evidence",
    "no real Tenhou, real haifu, external log or platform data",
    "no model output, training, self-play, league or production evaluation",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
    "not candidate-promotion evidence",
)


class MahJaxIntegrationSmokeError(RuntimeError):
    """Raised when the pinned MahJax integration contract is unavailable."""


@dataclass(frozen=True)
class MahJaxIntegrationSmokeResult:
    """Immutable diagnostics from one pinned MahJax legal transition."""

    integration_version: str
    package_version: str
    environment_id: str
    environment_version: str
    num_players: int
    num_actions: int
    seed: int
    initial_player: int
    initial_step_count: int
    initial_legal_action_count: int
    selected_action: int
    observation_keys: Tuple[str, ...]
    next_player: int
    next_step_count: int
    next_legal_action_count: int
    rewards: Tuple[float, ...]
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
        raise MahJaxIntegrationSmokeError(
            "pinned MahJax/JAX runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax


def _bool_mask(
    value: object,
    field_name: str,
    expected_size: int,
) -> Tuple[bool, ...]:
    if str(getattr(value, "dtype", "")) != "bool":
        raise MahJaxIntegrationSmokeError(f"{field_name} must have bool dtype")
    try:
        mask = tuple(bool(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxIntegrationSmokeError(
            f"{field_name} must be an iterable boolean mask"
        ) from exc
    if len(mask) != expected_size:
        raise MahJaxIntegrationSmokeError(
            f"{field_name} must contain exactly {expected_size} actions"
        )
    return mask


def run_mahjax_integration_smoke(seed: int = 0) -> MahJaxIntegrationSmokeResult:
    """Initialize pinned MahJax and apply its lowest-index legal action once."""

    if type(seed) is not int or seed < 0 or seed > 0xFFFFFFFF:
        raise MahJaxIntegrationSmokeError(
            "seed must be an exact int from 0 through 4294967295"
        )

    jax, jnp, mahjax = _load_pinned_runtime()
    if mahjax.__version__ != MAHJAX_PACKAGE_VERSION:
        raise MahJaxIntegrationSmokeError(
            f"mahjax version must be {MAHJAX_PACKAGE_VERSION!r}"
        )

    try:
        environment = mahjax.make(
            MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(jax.random.PRNGKey(seed))
    except Exception as exc:
        raise MahJaxIntegrationSmokeError(
            "failed to initialize the pinned MahJax red-mahjong environment"
        ) from exc

    if environment.id != MAHJAX_ENVIRONMENT_ID:
        raise MahJaxIntegrationSmokeError("unexpected MahJax environment id")
    if environment.version != MAHJAX_ENVIRONMENT_VERSION:
        raise MahJaxIntegrationSmokeError("unexpected MahJax environment version")
    if environment.num_players != 4 or environment.num_actions != 87:
        raise MahJaxIntegrationSmokeError(
            "MahJax environment must expose four players and 87 actions"
        )

    initial_mask = _bool_mask(
        state.legal_action_mask,
        "state.legal_action_mask",
        environment.num_actions,
    )
    legal_actions = tuple(
        action_index for action_index, is_legal in enumerate(initial_mask) if is_legal
    )
    if not legal_actions:
        raise MahJaxIntegrationSmokeError(
            "initial environment-owned legal-action mask must contain an action"
        )
    selected_action = legal_actions[0]

    try:
        observation = environment.observe(state)
    except Exception as exc:
        raise MahJaxIntegrationSmokeError(
            "failed to obtain the public MahJax observation"
        ) from exc
    if type(observation) is not dict:
        raise MahJaxIntegrationSmokeError("MahJax observation must be an exact dict")
    observation_keys = tuple(sorted(observation))
    if set(observation_keys) != _EXPECTED_OBSERVATION_KEYS:
        raise MahJaxIntegrationSmokeError(
            "MahJax observation keys differ from the pinned public interface"
        )

    initial_step_count = int(state.step_count)
    initial_player = int(state.current_player)
    try:
        next_state = environment.step(state, jnp.int32(selected_action))
    except Exception as exc:
        raise MahJaxIntegrationSmokeError(
            "failed to execute one environment-owned legal MahJax action"
        ) from exc

    next_step_count = int(next_state.step_count)
    if next_step_count != initial_step_count + 1:
        raise MahJaxIntegrationSmokeError(
            "MahJax legal transition must increment step_count exactly once"
        )
    terminated = bool(next_state.terminated)
    truncated = bool(next_state.truncated)
    if terminated or truncated:
        raise MahJaxIntegrationSmokeError(
            "first lowest-index legal discard must not end or truncate the game"
        )

    next_mask = _bool_mask(
        next_state.legal_action_mask,
        "next_state.legal_action_mask",
        environment.num_actions,
    )
    next_legal_action_count = sum(next_mask)
    if next_legal_action_count < 1:
        raise MahJaxIntegrationSmokeError(
            "next state must expose at least one environment-owned legal action"
        )

    rewards = tuple(float(value) for value in next_state.rewards)
    if len(rewards) != 4:
        raise MahJaxIntegrationSmokeError("MahJax rewards must contain four values")

    return MahJaxIntegrationSmokeResult(
        integration_version=MAHJAX_INTEGRATION_SMOKE_VERSION,
        package_version=MAHJAX_PACKAGE_VERSION,
        environment_id=MAHJAX_ENVIRONMENT_ID,
        environment_version=MAHJAX_ENVIRONMENT_VERSION,
        num_players=4,
        num_actions=87,
        seed=seed,
        initial_player=initial_player,
        initial_step_count=initial_step_count,
        initial_legal_action_count=len(legal_actions),
        selected_action=selected_action,
        observation_keys=observation_keys,
        next_player=int(next_state.current_player),
        next_step_count=next_step_count,
        next_legal_action_count=next_legal_action_count,
        rewards=rewards,
        terminated=terminated,
        truncated=truncated,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_ENVIRONMENT_ID",
    "MAHJAX_ENVIRONMENT_VERSION",
    "MAHJAX_INTEGRATION_SMOKE_VERSION",
    "MAHJAX_PACKAGE_VERSION",
    "MahJaxIntegrationSmokeError",
    "MahJaxIntegrationSmokeResult",
    "run_mahjax_integration_smoke",
]
