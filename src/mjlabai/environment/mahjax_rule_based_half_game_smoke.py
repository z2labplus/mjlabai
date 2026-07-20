"""Pinned MahJax bundled-rule-policy half-game rollout smoke.

This module verifies one complete local half-game environment path with four
bundled rule-policy seats. It does not use a project model, train a policy, run
production self-play, or provide strength evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.environment.mahjax_rule_based_single_round_smoke import (
    _four_floats,
    _legal_actions,
    _load_pinned_runtime,
)


MAHJAX_RULE_BASED_HALF_GAME_SMOKE_VERSION = (
    "p4_p8_mahjax_rule_based_half_game_smoke_v0.1"
)
MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP = 2048

_EXPECTED_ROUND_BOUNDARIES = (
    (140, 0, 1, (216, 315, 363, 106)),
    (190, 1, 2, (164, 367, 363, 106)),
    (279, 2, 3, (164, 367, 343, 126)),
    (365, 3, 4, (294, 367, 223, 116)),
    (431, 4, 5, (284, 337, 223, 156)),
    (461, 5, 6, (271, 389, 210, 130)),
    (554, 6, 7, (256, 394, 195, 145)),
    (883, 7, 8, (216, 414, 121, 249)),
)
_EXPECTED_FINAL_SCORES = (203, 441, 76, 280)
_EXPECTED_FINAL_REWARDS = (-3.0, -3.0, -5.0, 21.0)
_EXPECTED_CUMULATIVE_REWARDS = (73.0, 151.0, -284.0, 10.0)

_EVIDENCE_GRADE = (
    "P4/P8 pinned local bundled-rule-policy half-game environment smoke evidence"
)
_WARNINGS = (
    "pinned MahJax v0.1.2 local CPU half-game environment smoke only",
    "all four seats use the same bundled non-learned red-riichi rule policy",
    "environment-owned legal actions are checked before every transition",
    "complete transition and round-boundary provenance is retained",
    "raw environment rewards and global scores are recorded without shaping",
    "no real Tenhou, real haifu, external log or platform data",
    "no project model, learning, update, optimizer, checkpoint or training",
    "not production self-play, league or evaluation",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
    "not candidate-promotion or P9-P12 evidence",
)


class MahJaxRuleBasedHalfGameSmokeError(RuntimeError):
    """Raised when the pinned bundled-rule-policy half-game contract fails."""


@dataclass(frozen=True)
class MahJaxRuleBasedHalfGameStep:
    """One immutable global transition with round-local identity."""

    transition_index: int
    round_index: int
    round_step_index: int
    acting_player: int
    legal_actions: Tuple[int, ...]
    selected_action: int


@dataclass(frozen=True)
class MahJaxRuleBasedHalfGameRoundBoundary:
    """Environment-owned transition from one numbered round to the next."""

    completed_transition_count: int
    previous_round_index: int
    next_round_index: int
    scores_after_boundary: Tuple[int, ...]


@dataclass(frozen=True)
class MahJaxRuleBasedHalfGameResult:
    """Frozen diagnostics for one complete bundled-rule-policy half-game."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    round_mode: str
    next_round_style: str
    policy_id: str
    seed: int
    transition_cap: int
    transition_count: int
    initial_player: int
    final_player: int
    initial_scores: Tuple[int, ...]
    final_scores: Tuple[int, ...]
    final_round_index: int
    final_round_step_count: int
    round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    trace: Tuple[MahJaxRuleBasedHalfGameStep, ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    terminated: bool
    truncated: bool
    illegal_action_count: int
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _four_ints(value: object, field_name: str) -> Tuple[int, ...]:
    try:
        normalized = tuple(int(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxRuleBasedHalfGameSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxRuleBasedHalfGameSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def run_mahjax_rule_based_half_game_smoke(
    seed: int = 0,
) -> MahJaxRuleBasedHalfGameResult:
    """Run one complete pinned local half-game under a hard transition cap."""

    if type(seed) is not int or seed < 0 or seed > 0xFFFFFFFF:
        raise MahJaxRuleBasedHalfGameSmokeError(
            "seed must be an exact int from 0 through 4294967295"
        )

    try:
        jax, jnp, mahjax, rule_based_player = _load_pinned_runtime()
        root_key = jax.random.PRNGKey(seed)
        init_key, policy_key = jax.random.split(root_key)
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="half",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxRuleBasedHalfGameSmokeError(
            "failed to initialize the pinned MahJax half-game environment"
        ) from exc

    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
        or environment.round_mode != "half"
        or environment.next_round_style != "auto"
    ):
        raise MahJaxRuleBasedHalfGameSmokeError(
            "half-game runtime differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxRuleBasedHalfGameSmokeError(
            "initial half-game state must be nonterminal and nontruncated"
        )

    initial_player = int(state.current_player)
    initial_scores = _four_ints(state.round_state.score, "initial scores")
    trace = []
    boundaries = []
    round_start_transition_index = 0
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    policy_fn = jax.jit(rule_based_player)

    for transition_index in range(MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxRuleBasedHalfGameSmokeError(
                "rollout attempted a policy action from a finished state"
            )
        round_index = int(state.round_state.round)
        environment_step_index = int(state.step_count)
        if environment_step_index != transition_index:
            raise MahJaxRuleBasedHalfGameSmokeError(
                "MahJax step_count must match the global transition index"
            )
        round_step_index = transition_index - round_start_transition_index
        legal_actions = _legal_actions(
            state.legal_action_mask,
            environment.num_actions,
        )
        try:
            policy_key, action_key = jax.random.split(policy_key)
            selected_action = int(policy_fn(state, action_key))
        except Exception as exc:
            raise MahJaxRuleBasedHalfGameSmokeError(
                f"bundled rule policy failed at transition {transition_index}"
            ) from exc
        if selected_action not in legal_actions:
            raise MahJaxRuleBasedHalfGameSmokeError(
                f"bundled rule policy selected illegal action {selected_action} "
                f"at transition {transition_index}"
            )
        trace.append(
            MahJaxRuleBasedHalfGameStep(
                transition_index=transition_index,
                round_index=round_index,
                round_step_index=round_step_index,
                acting_player=int(state.current_player),
                legal_actions=legal_actions,
                selected_action=selected_action,
            )
        )
        try:
            state = step_fn(state, jnp.int32(selected_action))
            state = jax.block_until_ready(state)
        except Exception as exc:
            raise MahJaxRuleBasedHalfGameSmokeError(
                f"failed to execute half-game transition {transition_index}"
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
        raise MahJaxRuleBasedHalfGameSmokeError(
            "MahJax bundled rule-policy half-game exceeded the "
            f"{MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP}-transition cap"
        )

    final_scores = _four_ints(state.round_state.score, "final scores")
    final_rewards = _four_floats(state.rewards, "final rewards")
    boundary_values = tuple(
        (
            item.completed_transition_count,
            item.previous_round_index,
            item.next_round_index,
            item.scores_after_boundary,
        )
        for item in boundaries
    )
    if seed == 0 and (
        len(trace) != 938
        or not bool(state.terminated)
        or bool(state.truncated)
        or int(state.round_state.round) != 8
        or boundary_values != _EXPECTED_ROUND_BOUNDARIES
        or final_scores != _EXPECTED_FINAL_SCORES
        or final_rewards != _EXPECTED_FINAL_REWARDS
        or cumulative_rewards != _EXPECTED_CUMULATIVE_REWARDS
    ):
        raise MahJaxRuleBasedHalfGameSmokeError(
            "seed-0 half-game result differs from the approved contract"
        )

    return MahJaxRuleBasedHalfGameResult(
        smoke_version=MAHJAX_RULE_BASED_HALF_GAME_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        round_mode="half",
        next_round_style="auto",
        policy_id="mahjax.red_mahjong.players.rule_based_player@0.1.2",
        seed=seed,
        transition_cap=MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
        transition_count=len(trace),
        initial_player=initial_player,
        final_player=int(state.current_player),
        initial_scores=initial_scores,
        final_scores=final_scores,
        final_round_index=int(state.round_state.round),
        final_round_step_count=int(state.step_count),
        round_boundaries=tuple(boundaries),
        trace=tuple(trace),
        final_rewards=final_rewards,
        cumulative_rewards=cumulative_rewards,
        terminated=bool(state.terminated),
        truncated=bool(state.truncated),
        illegal_action_count=0,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_RULE_BASED_HALF_GAME_SMOKE_VERSION",
    "MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP",
    "MahJaxRuleBasedHalfGameSmokeError",
    "MahJaxRuleBasedHalfGameStep",
    "MahJaxRuleBasedHalfGameRoundBoundary",
    "MahJaxRuleBasedHalfGameResult",
    "run_mahjax_rule_based_half_game_smoke",
]
