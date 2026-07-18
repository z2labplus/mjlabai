"""Two-step deterministic P8 synthetic/local policy-update sequence smoke.

This module chains exactly two already-loaded synthetic/local numerical
records through the reviewed single-step helper. It is not an environment,
episode, self-play system, model, optimizer, or production training loop.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.rl.synthetic_policy_update_smoke import (
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateResult,
    SyntheticPolicyUpdateSmokeError,
    apply_synthetic_policy_update_smoke,
)


SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION = (
    "p8_synthetic_policy_update_sequence_smoke_v0.1"
)

_EVIDENCE_GRADE = (
    "P8 synthetic/local two-step numerical policy-update sequence smoke "
    "evidence only"
)
_WARNINGS = (
    "synthetic/local two-step numerical smoke only",
    "not an environment or episode",
    "not self-play",
    "not production training",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)


class SyntheticPolicyUpdateSequenceSmokeError(ValueError):
    """Raised when the exact two-step sequence boundary is violated."""


@dataclass(frozen=True)
class SyntheticPolicyUpdateSequenceResult:
    """Immutable diagnostics from exactly two chained validated updates."""

    sequence_version: str
    step_count: int
    record_ids: Tuple[str, str]
    source_kind: str
    state_id: str
    action_id: str
    learning_rate: float
    discount_factor: float
    initial_action_value: float
    intermediate_action_value: float
    final_action_value: float
    step_results: Tuple[
        SyntheticPolicyUpdateResult,
        SyntheticPolicyUpdateResult,
    ]
    sequence_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def apply_synthetic_policy_update_sequence_smoke(
    input_records: Tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyUpdateSequenceResult:
    """Apply exactly two ordered updates through the reviewed base helper."""

    if type(input_records) is not tuple:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "input_records must be an exact tuple"
        )
    if len(input_records) != 2:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "input_records must contain exactly two records"
        )
    if not all(
        isinstance(record, SyntheticPolicyUpdateInput)
        for record in input_records
    ):
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "each step must be a SyntheticPolicyUpdateInput"
        )

    first_record, second_record = input_records
    if first_record.record_id == second_record.record_id:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "record_ids must be distinct"
        )
    for field_name in ("source_kind", "state_id", "action_id"):
        if getattr(first_record, field_name) != getattr(second_record, field_name):
            raise SyntheticPolicyUpdateSequenceSmokeError(
                f"both steps must have identical {field_name}"
            )
    if first_record.terminal is not False:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "step 1 must be non-terminal"
        )
    if second_record.terminal is not True:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "step 2 must be terminal"
        )

    first_result = _apply_step(
        first_record,
        step_index=1,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )
    if second_record.current_action_value != first_result.updated_action_value:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            "step 2 current_action_value must exactly equal step 1 "
            "updated_action_value"
        )
    second_result = _apply_step(
        second_record,
        step_index=2,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )

    return SyntheticPolicyUpdateSequenceResult(
        sequence_version=SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION,
        step_count=2,
        record_ids=(first_result.record_id, second_result.record_id),
        source_kind=first_result.source_kind,
        state_id=first_result.state_id,
        action_id=first_result.action_id,
        learning_rate=first_result.learning_rate,
        discount_factor=first_result.discount_factor,
        initial_action_value=first_result.current_action_value,
        intermediate_action_value=first_result.updated_action_value,
        final_action_value=second_result.updated_action_value,
        step_results=(first_result, second_result),
        sequence_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


def _apply_step(
    input_record: SyntheticPolicyUpdateInput,
    *,
    step_index: int,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyUpdateResult:
    try:
        return apply_synthetic_policy_update_smoke(
            input_record,
            learning_rate=learning_rate,
            discount_factor=discount_factor,
        )
    except SyntheticPolicyUpdateSmokeError as exc:
        raise SyntheticPolicyUpdateSequenceSmokeError(
            f"step {step_index} failed: {exc}"
        ) from exc


__all__ = [
    "SYNTHETIC_POLICY_UPDATE_SEQUENCE_SMOKE_VERSION",
    "SyntheticPolicyUpdateSequenceResult",
    "SyntheticPolicyUpdateSequenceSmokeError",
    "apply_synthetic_policy_update_sequence_smoke",
]
