"""Fixed two-key P8 synthetic/local policy-value table update smoke.

This module binds one exact two-entry in-memory table to the reviewed
four-record trace helper. It is not a mutable or persistent policy store,
environment, replay buffer, model, optimizer, or production training loop.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from mjlabai.rl.synthetic_policy_update_smoke import SyntheticPolicyUpdateInput
from mjlabai.rl.synthetic_policy_update_trace_smoke import (
    SyntheticPolicyUpdateTraceResult,
    SyntheticPolicyUpdateTraceSmokeError,
    apply_synthetic_policy_update_trace_smoke,
)


SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION = (
    "p8_synthetic_policy_table_update_smoke_v0.1"
)

_EVIDENCE_GRADE = (
    "P8 synthetic/local fixed two-key policy-value table update smoke "
    "evidence only"
)
_WARNINGS = (
    "synthetic/local fixed two-key policy-value table update smoke only",
    "not a persistent policy, model or checkpoint",
    "not an environment, episode or replay buffer",
    "not self-play",
    "not a variable batch, epoch or production training loop",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)


class SyntheticPolicyTableUpdateSmokeError(ValueError):
    """Raised when the exact two-entry table boundary is violated."""


@dataclass(frozen=True)
class SyntheticPolicyTableEntry:
    """One immutable synthetic/local policy-value table entry."""

    state_id: str
    action_id: str
    action_value: float


@dataclass(frozen=True)
class SyntheticPolicyTableUpdateResult:
    """Immutable diagnostics from one exact fixed table update."""

    table_update_version: str
    entry_count: int
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]
    final_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]
    trace_result: SyntheticPolicyUpdateTraceResult
    update_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def apply_synthetic_policy_table_update_smoke(
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry],
    input_records: Tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyTableUpdateResult:
    """Apply one exact trace to one fixed two-entry policy-value table."""

    if type(initial_entries) is not tuple:
        raise SyntheticPolicyTableUpdateSmokeError(
            "initial_entries must be an exact tuple"
        )
    if len(initial_entries) != 2:
        raise SyntheticPolicyTableUpdateSmokeError(
            "initial_entries must contain exactly two entries"
        )
    if not all(type(entry) is SyntheticPolicyTableEntry for entry in initial_entries):
        raise SyntheticPolicyTableUpdateSmokeError(
            "each initial entry must be an exact SyntheticPolicyTableEntry"
        )
    for entry_index, entry in enumerate(initial_entries, start=1):
        if type(entry.state_id) is not str or type(entry.action_id) is not str:
            raise SyntheticPolicyTableUpdateSmokeError(
                f"entry {entry_index} identifiers must be exact strings"
            )
        if type(entry.action_value) is not float or not math.isfinite(
            entry.action_value
        ):
            raise SyntheticPolicyTableUpdateSmokeError(
                f"entry {entry_index} action_value must be an exact finite float"
            )

    try:
        trace_result = apply_synthetic_policy_update_trace_smoke(
            input_records,
            learning_rate=learning_rate,
            discount_factor=discount_factor,
        )
    except SyntheticPolicyUpdateTraceSmokeError as exc:
        raise SyntheticPolicyTableUpdateSmokeError(
            f"trace update failed: {exc}"
        ) from exc

    for entry_index, (entry, expected_key, expected_value) in enumerate(
        zip(
            initial_entries,
            trace_result.state_action_keys,
            trace_result.initial_action_values,
        ),
        start=1,
    ):
        if (entry.state_id, entry.action_id) != expected_key:
            raise SyntheticPolicyTableUpdateSmokeError(
                f"entry {entry_index} must match trace key {expected_key!r}"
            )
        if entry.action_value != expected_value:
            raise SyntheticPolicyTableUpdateSmokeError(
                f"entry {entry_index} action_value must exactly match the trace "
                "initial value"
            )

    normalized_initial_entries = tuple(
        SyntheticPolicyTableEntry(
            state_id=state_id,
            action_id=action_id,
            action_value=action_value,
        )
        for (state_id, action_id), action_value in zip(
            trace_result.state_action_keys,
            trace_result.initial_action_values,
        )
    )
    final_entries = tuple(
        SyntheticPolicyTableEntry(
            state_id=state_id,
            action_id=action_id,
            action_value=action_value,
        )
        for (state_id, action_id), action_value in zip(
            trace_result.state_action_keys,
            trace_result.final_action_values,
        )
    )

    return SyntheticPolicyTableUpdateResult(
        table_update_version=SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION,
        entry_count=2,
        initial_entries=normalized_initial_entries,  # type: ignore[arg-type]
        final_entries=final_entries,  # type: ignore[arg-type]
        trace_result=trace_result,
        update_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION",
    "SyntheticPolicyTableEntry",
    "SyntheticPolicyTableUpdateResult",
    "SyntheticPolicyTableUpdateSmokeError",
    "apply_synthetic_policy_table_update_smoke",
]
