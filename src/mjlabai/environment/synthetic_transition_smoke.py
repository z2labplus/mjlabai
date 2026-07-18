"""Exact single-transition P4 synthetic/local environment-contract smoke.

The helper owns legality selection and one immutable state progression for a
fixed project-authored input. It is not a Mahjong rules engine, hand simulator,
multi-step episode, self-play system, or production environment.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


SYNTHETIC_ENVIRONMENT_ID = "mjlabai_synthetic_local_environment"
SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION = (
    "p4_synthetic_environment_transition_smoke_v0.1"
)
SYNTHETIC_FOUR_PLAYER_RULESET_ID = "synthetic_four_player_riichi_contract_v0.1"

_EVIDENCE_GRADE = (
    "P4 exact single-transition synthetic/local environment-contract smoke "
    "evidence only"
)
_WARNINGS = (
    "exact single-transition synthetic/local environment smoke only",
    "four-seat contract identity and strict dahai matching only",
    "no Mahjong hand, tile ownership, rules, scoring, hidden state, RNG or multi-step episode",
    "no model, reward, training, self-play or evaluation",
    "no persistence, external dependency or real data",
    "not policy-quality or model-strength evidence",
    "not Tenhou, stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)


class SyntheticEnvironmentTransitionSmokeError(ValueError):
    """Raised when the exact synthetic transition contract is violated."""


@dataclass(frozen=True)
class SyntheticEnvironmentAction:
    """One immutable strict-discard action at the environment boundary."""

    action_id: str
    actor: int
    action_type: str
    tile: str
    tsumogiri: bool


@dataclass(frozen=True)
class SyntheticEnvironmentState:
    """One immutable authoritative state for the single-transition smoke."""

    environment_id: str
    environment_version: str
    ruleset_id: str
    episode_id: str
    step_index: int
    acting_seat: int
    legal_actions: Tuple[SyntheticEnvironmentAction, ...]
    terminal: bool
    project_authored: bool
    synthetic: bool
    local_only: bool
    uses_real_data: bool
    uses_external_log: bool
    uses_platform_data: bool


@dataclass(frozen=True)
class SyntheticEnvironmentTransitionResult:
    """Immutable diagnostics from one authoritative synthetic transition."""

    transition_version: str
    pre_state: SyntheticEnvironmentState
    proposed_action: SyntheticEnvironmentAction
    applied_action: SyntheticEnvironmentAction
    legal_action_index: int
    event_id: str
    post_state: SyntheticEnvironmentState
    transition_applied: bool
    terminal_reached: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _normalize_action(
    value: object,
    field_name: str,
) -> SyntheticEnvironmentAction:
    if type(value) is not SyntheticEnvironmentAction:
        raise SyntheticEnvironmentTransitionSmokeError(
            f"{field_name} must be an exact SyntheticEnvironmentAction"
        )
    if type(value.action_id) is not str or not value.action_id.strip():
        raise SyntheticEnvironmentTransitionSmokeError(
            f"{field_name}.action_id must be a non-empty string"
        )
    if type(value.actor) is not int or value.actor not in (0, 1, 2, 3):
        raise SyntheticEnvironmentTransitionSmokeError(
            f"{field_name}.actor must be exact int from 0 through 3"
        )
    if value.action_type != "dahai":
        raise SyntheticEnvironmentTransitionSmokeError(
            f"{field_name}.action_type must be 'dahai'"
        )
    if type(value.tile) is not str or not value.tile.strip():
        raise SyntheticEnvironmentTransitionSmokeError(
            f"{field_name}.tile must be a non-empty string"
        )
    if type(value.tsumogiri) is not bool:
        raise SyntheticEnvironmentTransitionSmokeError(
            f"{field_name}.tsumogiri must be bool"
        )
    return SyntheticEnvironmentAction(
        action_id=value.action_id,
        actor=value.actor,
        action_type="dahai",
        tile=value.tile,
        tsumogiri=value.tsumogiri,
    )


def _strict_action_key(action: SyntheticEnvironmentAction) -> tuple[object, ...]:
    return (
        action.actor,
        action.action_type,
        action.tile,
        action.tsumogiri,
    )


def _normalize_pre_state(value: object) -> SyntheticEnvironmentState:
    if type(value) is not SyntheticEnvironmentState:
        raise SyntheticEnvironmentTransitionSmokeError(
            "state must be an exact SyntheticEnvironmentState"
        )
    if value.environment_id != SYNTHETIC_ENVIRONMENT_ID:
        raise SyntheticEnvironmentTransitionSmokeError(
            f"state.environment_id must be {SYNTHETIC_ENVIRONMENT_ID!r}"
        )
    if value.environment_version != SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION:
        raise SyntheticEnvironmentTransitionSmokeError(
            "state.environment_version must match the transition smoke version"
        )
    if value.ruleset_id != SYNTHETIC_FOUR_PLAYER_RULESET_ID:
        raise SyntheticEnvironmentTransitionSmokeError(
            f"state.ruleset_id must be {SYNTHETIC_FOUR_PLAYER_RULESET_ID!r}"
        )
    if type(value.episode_id) is not str or not value.episode_id.strip():
        raise SyntheticEnvironmentTransitionSmokeError(
            "state.episode_id must be a non-empty string"
        )
    if type(value.step_index) is not int or value.step_index != 0:
        raise SyntheticEnvironmentTransitionSmokeError(
            "state.step_index must be exact int 0"
        )
    if type(value.acting_seat) is not int or value.acting_seat not in (0, 1, 2, 3):
        raise SyntheticEnvironmentTransitionSmokeError(
            "state.acting_seat must be exact int from 0 through 3"
        )
    if type(value.terminal) is not bool or value.terminal is not False:
        raise SyntheticEnvironmentTransitionSmokeError(
            "state.terminal must be false"
        )
    if type(value.legal_actions) is not tuple or len(value.legal_actions) != 2:
        raise SyntheticEnvironmentTransitionSmokeError(
            "state.legal_actions must be an exact two-action tuple"
        )
    legal_action_zero = _normalize_action(
        value.legal_actions[0],
        "state.legal_actions[0]",
    )
    legal_action_one = _normalize_action(
        value.legal_actions[1],
        "state.legal_actions[1]",
    )
    if (
        legal_action_zero.actor != value.acting_seat
        or legal_action_one.actor != value.acting_seat
    ):
        raise SyntheticEnvironmentTransitionSmokeError(
            "every legal action actor must match state.acting_seat"
        )
    if legal_action_zero.action_id == legal_action_one.action_id:
        raise SyntheticEnvironmentTransitionSmokeError(
            "legal action action_ids must be distinct"
        )
    if _strict_action_key(legal_action_zero) == _strict_action_key(legal_action_one):
        raise SyntheticEnvironmentTransitionSmokeError(
            "legal action strict canonical tuples must be distinct"
        )
    required_flags = (
        ("project_authored", value.project_authored, True),
        ("synthetic", value.synthetic, True),
        ("local_only", value.local_only, True),
        ("uses_real_data", value.uses_real_data, False),
        ("uses_external_log", value.uses_external_log, False),
        ("uses_platform_data", value.uses_platform_data, False),
    )
    for field_name, actual, expected in required_flags:
        if type(actual) is not bool or actual is not expected:
            raise SyntheticEnvironmentTransitionSmokeError(
                f"state.{field_name} must be {expected}"
            )
    return SyntheticEnvironmentState(
        environment_id=SYNTHETIC_ENVIRONMENT_ID,
        environment_version=SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION,
        ruleset_id=SYNTHETIC_FOUR_PLAYER_RULESET_ID,
        episode_id=value.episode_id,
        step_index=0,
        acting_seat=value.acting_seat,
        legal_actions=(legal_action_zero, legal_action_one),
        terminal=False,
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
    )


def apply_synthetic_environment_transition_smoke(
    state: SyntheticEnvironmentState,
    proposed_action: SyntheticEnvironmentAction,
) -> SyntheticEnvironmentTransitionResult:
    """Apply one strictly legal authored discard and terminate the smoke."""

    pre_state = _normalize_pre_state(state)
    normalized_proposal = _normalize_action(proposed_action, "proposed_action")
    match_zero = _strict_action_key(normalized_proposal) == _strict_action_key(
        pre_state.legal_actions[0]
    )
    match_one = _strict_action_key(normalized_proposal) == _strict_action_key(
        pre_state.legal_actions[1]
    )
    if match_zero == match_one:
        raise SyntheticEnvironmentTransitionSmokeError(
            "proposed_action must strictly match exactly one legal action"
        )
    legal_action_index = 0 if match_zero else 1
    applied_action = pre_state.legal_actions[legal_action_index]
    event_id = f"{pre_state.episode_id}:step:{pre_state.step_index}:dahai"
    post_state = SyntheticEnvironmentState(
        environment_id=pre_state.environment_id,
        environment_version=pre_state.environment_version,
        ruleset_id=pre_state.ruleset_id,
        episode_id=pre_state.episode_id,
        step_index=1,
        acting_seat=(pre_state.acting_seat + 1) % 4,
        legal_actions=(),
        terminal=True,
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
    )
    return SyntheticEnvironmentTransitionResult(
        transition_version=SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION,
        pre_state=pre_state,
        proposed_action=normalized_proposal,
        applied_action=applied_action,
        legal_action_index=legal_action_index,
        event_id=event_id,
        post_state=post_state,
        transition_applied=True,
        terminal_reached=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_ENVIRONMENT_ID",
    "SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION",
    "SYNTHETIC_FOUR_PLAYER_RULESET_ID",
    "SyntheticEnvironmentAction",
    "SyntheticEnvironmentState",
    "SyntheticEnvironmentTransitionResult",
    "SyntheticEnvironmentTransitionSmokeError",
    "apply_synthetic_environment_transition_smoke",
]
