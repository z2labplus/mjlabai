"""One deterministic P8 synthetic/local numerical policy-update smoke.

This module applies one tabular action-value update to one already-loaded,
project-authored synthetic/local record. It does not implement an environment,
episode, self-play, action selection, model, optimizer, training loop,
evaluation, persistence, or external-data access.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Real
import re
from typing import Optional, Tuple


SYNTHETIC_POLICY_UPDATE_SMOKE_VERSION = "p8_synthetic_policy_update_smoke_v0.1"
SYNTHETIC_LOCAL_SOURCE_KIND = "project_authored_synthetic_local"

_EVIDENCE_GRADE = (
    "P8 synthetic/local numerical policy-update smoke evidence only"
)
_WARNINGS = (
    "synthetic/local only",
    "not real Tenhou or haifu data",
    "not self-play",
    "not production training",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)
_IDENTIFIER_PATTERN = re.compile(r"[A-Za-z0-9_.:-]+\Z")


class SyntheticPolicyUpdateSmokeError(ValueError):
    """Raised when the exact synthetic/local update boundary is violated."""


@dataclass(frozen=True)
class SyntheticPolicyUpdateInput:
    """One already-loaded project-authored synthetic/local update record."""

    record_id: str
    source_kind: str
    state_id: str
    action_id: str
    current_action_value: float
    reward: float
    next_max_action_value: Optional[float]
    terminal: bool
    project_authored: bool
    synthetic: bool
    local_only: bool
    uses_real_data: bool
    uses_external_log: bool
    uses_platform_data: bool
    uses_model_output: bool
    uses_self_play: bool


@dataclass(frozen=True)
class SyntheticPolicyUpdateResult:
    """Numerical diagnostics from one validated synthetic/local update."""

    smoke_version: str
    record_id: str
    source_kind: str
    state_id: str
    action_id: str
    terminal: bool
    learning_rate: float
    discount_factor: float
    current_action_value: float
    reward: float
    next_max_action_value: Optional[float]
    target_value: float
    td_error: float
    updated_action_value: float
    update_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def apply_synthetic_policy_update_smoke(
    input_record: SyntheticPolicyUpdateInput,
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyUpdateResult:
    """Apply the one approved deterministic tabular numerical update."""

    if not isinstance(input_record, SyntheticPolicyUpdateInput):
        raise SyntheticPolicyUpdateSmokeError(
            "input_record must be a SyntheticPolicyUpdateInput"
        )

    _validate_identifier("record_id", input_record.record_id)
    _validate_identifier("state_id", input_record.state_id)
    _validate_identifier("action_id", input_record.action_id)
    if input_record.source_kind != SYNTHETIC_LOCAL_SOURCE_KIND:
        raise SyntheticPolicyUpdateSmokeError(
            f"source_kind must be {SYNTHETIC_LOCAL_SOURCE_KIND!r}"
        )
    if type(input_record.terminal) is not bool:
        raise SyntheticPolicyUpdateSmokeError("terminal must be a bool")

    _require_guardrail("project_authored", input_record.project_authored, True)
    _require_guardrail("synthetic", input_record.synthetic, True)
    _require_guardrail("local_only", input_record.local_only, True)
    _require_guardrail("uses_real_data", input_record.uses_real_data, False)
    _require_guardrail("uses_external_log", input_record.uses_external_log, False)
    _require_guardrail("uses_platform_data", input_record.uses_platform_data, False)
    _require_guardrail("uses_model_output", input_record.uses_model_output, False)
    _require_guardrail("uses_self_play", input_record.uses_self_play, False)

    current_action_value = _finite_real(
        "current_action_value", input_record.current_action_value
    )
    reward = _finite_real("reward", input_record.reward)
    learning_rate_value = _finite_real("learning_rate", learning_rate)
    discount_factor_value = _finite_real("discount_factor", discount_factor)
    if not 0.0 < learning_rate_value <= 1.0:
        raise SyntheticPolicyUpdateSmokeError(
            "learning_rate must satisfy 0 < learning_rate <= 1"
        )
    if not 0.0 <= discount_factor_value <= 1.0:
        raise SyntheticPolicyUpdateSmokeError(
            "discount_factor must satisfy 0 <= discount_factor <= 1"
        )

    if input_record.terminal:
        if input_record.next_max_action_value is not None:
            raise SyntheticPolicyUpdateSmokeError(
                "terminal records require next_max_action_value to be None"
            )
        next_max_action_value = None
        target_value = reward
    else:
        if input_record.next_max_action_value is None:
            raise SyntheticPolicyUpdateSmokeError(
                "non-terminal records require a finite next_max_action_value"
            )
        next_max_action_value = _finite_real(
            "next_max_action_value", input_record.next_max_action_value
        )
        target_value = reward + discount_factor_value * next_max_action_value

    target_value = _finite_derived("target_value", target_value)
    td_error = _finite_derived(
        "td_error", target_value - current_action_value
    )
    updated_action_value = _finite_derived(
        "updated_action_value",
        current_action_value + learning_rate_value * td_error,
    )

    return SyntheticPolicyUpdateResult(
        smoke_version=SYNTHETIC_POLICY_UPDATE_SMOKE_VERSION,
        record_id=input_record.record_id,
        source_kind=input_record.source_kind,
        state_id=input_record.state_id,
        action_id=input_record.action_id,
        terminal=input_record.terminal,
        learning_rate=learning_rate_value,
        discount_factor=discount_factor_value,
        current_action_value=current_action_value,
        reward=reward,
        next_max_action_value=next_max_action_value,
        target_value=target_value,
        td_error=td_error,
        updated_action_value=updated_action_value,
        update_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


def _validate_identifier(name: str, value: object) -> None:
    if not isinstance(value, str) or not value:
        raise SyntheticPolicyUpdateSmokeError(
            f"{name} must be a non-empty ASCII identifier token"
        )
    if value in {".", ".."} or _IDENTIFIER_PATTERN.fullmatch(value) is None:
        raise SyntheticPolicyUpdateSmokeError(
            f"{name} must contain only ASCII letters, digits, _, -, ., and :"
        )


def _require_guardrail(name: str, value: object, expected: bool) -> None:
    if type(value) is not bool or value is not expected:
        raise SyntheticPolicyUpdateSmokeError(f"{name} must be exactly {expected}")


def _finite_real(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise SyntheticPolicyUpdateSmokeError(
            f"{name} must be a finite real number excluding bool"
        )
    numeric_value = float(value)
    if not math.isfinite(numeric_value):
        raise SyntheticPolicyUpdateSmokeError(f"{name} must be finite")
    return numeric_value


def _finite_derived(name: str, value: float) -> float:
    if not math.isfinite(value):
        raise SyntheticPolicyUpdateSmokeError(f"derived {name} must be finite")
    return value


__all__ = [
    "SYNTHETIC_LOCAL_SOURCE_KIND",
    "SYNTHETIC_POLICY_UPDATE_SMOKE_VERSION",
    "SyntheticPolicyUpdateInput",
    "SyntheticPolicyUpdateResult",
    "SyntheticPolicyUpdateSmokeError",
    "apply_synthetic_policy_update_smoke",
]
