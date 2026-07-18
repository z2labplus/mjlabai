"""Fixed two-pass P8 synthetic/local policy-table update sequence smoke.

This module chains exactly two reviewed fixed-table updates. It is not a
variable epoch, trainer, persistent policy, environment, replay buffer,
self-play system, model, optimizer, or production training loop.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.rl.synthetic_policy_table_update_smoke import (
    SyntheticPolicyTableEntry,
    SyntheticPolicyTableUpdateResult,
    SyntheticPolicyTableUpdateSmokeError,
    apply_synthetic_policy_table_update_smoke,
)
from mjlabai.rl.synthetic_policy_update_smoke import SyntheticPolicyUpdateInput


SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION = (
    "p8_synthetic_policy_table_update_sequence_smoke_v0.1"
)

_EVIDENCE_GRADE = (
    "P8 synthetic/local fixed two-pass policy-table update sequence smoke "
    "evidence only"
)
_WARNINGS = (
    "synthetic/local fixed two-pass policy-table update sequence smoke only",
    "not a variable epoch, trainer or production training loop",
    "not a persistent policy, model or checkpoint",
    "not an environment, episode or replay buffer",
    "not self-play",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)


class SyntheticPolicyTableUpdateSequenceSmokeError(ValueError):
    """Raised when the exact two-pass sequence boundary is violated."""


@dataclass(frozen=True)
class SyntheticPolicyTableUpdateSequenceResult:
    """Immutable diagnostics from exactly two table-update passes."""

    sequence_version: str
    pass_count: int
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]
    intermediate_entries: Tuple[
        SyntheticPolicyTableEntry,
        SyntheticPolicyTableEntry,
    ]
    final_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]
    pass_results: Tuple[
        SyntheticPolicyTableUpdateResult,
        SyntheticPolicyTableUpdateResult,
    ]
    sequence_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def apply_synthetic_policy_table_update_sequence_smoke(
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry],
    trace_inputs: Tuple[
        Tuple[
            SyntheticPolicyUpdateInput,
            SyntheticPolicyUpdateInput,
            SyntheticPolicyUpdateInput,
            SyntheticPolicyUpdateInput,
        ],
        Tuple[
            SyntheticPolicyUpdateInput,
            SyntheticPolicyUpdateInput,
            SyntheticPolicyUpdateInput,
            SyntheticPolicyUpdateInput,
        ],
    ],
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyTableUpdateSequenceResult:
    """Apply exactly two chained updates through the reviewed table helper."""

    if type(trace_inputs) is not tuple:
        raise SyntheticPolicyTableUpdateSequenceSmokeError(
            "trace_inputs must be an exact tuple"
        )
    if len(trace_inputs) != 2:
        raise SyntheticPolicyTableUpdateSequenceSmokeError(
            "trace_inputs must contain exactly two trace tuples"
        )

    first_trace, second_trace = trace_inputs
    first_result = _apply_pass(
        initial_entries,
        first_trace,
        pass_index=1,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )
    second_result = _apply_pass(
        first_result.final_entries,
        second_trace,
        pass_index=2,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )

    record_ids = (
        first_result.trace_result.record_ids
        + second_result.trace_result.record_ids
    )
    if _has_duplicate_record_ids(record_ids):
        raise SyntheticPolicyTableUpdateSequenceSmokeError(
            "record_ids across both passes must be pairwise distinct"
        )

    return SyntheticPolicyTableUpdateSequenceResult(
        sequence_version=SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION,
        pass_count=2,
        initial_entries=first_result.initial_entries,
        intermediate_entries=first_result.final_entries,
        final_entries=second_result.final_entries,
        pass_results=(first_result, second_result),
        sequence_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


def _apply_pass(
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry],
    input_records: Tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
    *,
    pass_index: int,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyTableUpdateResult:
    try:
        return apply_synthetic_policy_table_update_smoke(
            initial_entries,
            input_records,
            learning_rate=learning_rate,
            discount_factor=discount_factor,
        )
    except SyntheticPolicyTableUpdateSmokeError as exc:
        raise SyntheticPolicyTableUpdateSequenceSmokeError(
            f"pass {pass_index} failed: {exc}"
        ) from exc


def _has_duplicate_record_ids(
    record_ids: Tuple[str, str, str, str, str, str, str, str],
) -> bool:
    return any(
        left == right
        for left_index, left in enumerate(record_ids)
        for right in record_ids[left_index + 1 :]
    )


__all__ = [
    "SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION",
    "SyntheticPolicyTableUpdateSequenceResult",
    "SyntheticPolicyTableUpdateSequenceSmokeError",
    "apply_synthetic_policy_table_update_sequence_smoke",
]
