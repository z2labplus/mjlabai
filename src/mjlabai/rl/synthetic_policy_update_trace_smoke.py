"""Four-record interleaved P8 synthetic/local policy-update trace smoke.

This module applies exactly four A/B/A/B numerical update records through the
reviewed single-step helper. It is not a variable batch, replay buffer,
environment, episode, self-play system, model, optimizer, or training loop.
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


SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION = (
    "p8_synthetic_policy_update_trace_smoke_v0.1"
)

_EVIDENCE_GRADE = (
    "P8 synthetic/local four-record interleaved two-key numerical "
    "policy-update trace smoke evidence only"
)
_WARNINGS = (
    "synthetic/local four-record interleaved numerical smoke only",
    "not an environment, episode or replay buffer",
    "not self-play",
    "not a variable or production training loop",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)


class SyntheticPolicyUpdateTraceSmokeError(ValueError):
    """Raised when the exact four-record trace boundary is violated."""


@dataclass(frozen=True)
class SyntheticPolicyUpdateTraceResult:
    """Immutable diagnostics from one exact A/B/A/B update trace."""

    trace_version: str
    step_count: int
    record_ids: Tuple[str, str, str, str]
    source_kind: str
    learning_rate: float
    discount_factor: float
    state_action_keys: Tuple[Tuple[str, str], Tuple[str, str]]
    initial_action_values: Tuple[float, float]
    intermediate_action_values: Tuple[float, float]
    final_action_values: Tuple[float, float]
    step_results: Tuple[
        SyntheticPolicyUpdateResult,
        SyntheticPolicyUpdateResult,
        SyntheticPolicyUpdateResult,
        SyntheticPolicyUpdateResult,
    ]
    trace_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def apply_synthetic_policy_update_trace_smoke(
    input_records: Tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticPolicyUpdateTraceResult:
    """Apply the exact four-record A/B/A/B trace through the base helper."""

    if type(input_records) is not tuple:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "input_records must be an exact tuple"
        )
    if len(input_records) != 4:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "input_records must contain exactly four records"
        )
    if not all(
        isinstance(record, SyntheticPolicyUpdateInput)
        for record in input_records
    ):
        raise SyntheticPolicyUpdateTraceSmokeError(
            "each step must be a SyntheticPolicyUpdateInput"
        )

    first_a, first_b, second_a, second_b = input_records
    if _has_duplicate_record_ids(input_records):
        raise SyntheticPolicyUpdateTraceSmokeError(
            "record_ids must be pairwise distinct"
        )
    if any(
        record.source_kind != first_a.source_kind
        for record in input_records[1:]
    ):
        raise SyntheticPolicyUpdateTraceSmokeError(
            "all steps must have identical source_kind"
        )

    key_a = _state_action_key(first_a)
    key_b = _state_action_key(first_b)
    if key_a == key_b:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "the trace must contain exactly two distinct state-action keys"
        )
    if _state_action_key(second_a) != key_a:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "step 3 must repeat the step 1 state-action key"
        )
    if _state_action_key(second_b) != key_b:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "step 4 must repeat the step 2 state-action key"
        )

    for step_index, record in enumerate(input_records, start=1):
        expected_terminal = step_index > 2
        if record.terminal is not expected_terminal:
            expected_label = "terminal" if expected_terminal else "non-terminal"
            raise SyntheticPolicyUpdateTraceSmokeError(
                f"step {step_index} must be {expected_label}"
            )

    result_1 = _apply_step(
        first_a,
        step_index=1,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )
    result_2 = _apply_step(
        first_b,
        step_index=2,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )
    if second_a.current_action_value != result_1.updated_action_value:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "step 3 current_action_value must exactly equal step 1 "
            "updated_action_value"
        )
    result_3 = _apply_step(
        second_a,
        step_index=3,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )
    if second_b.current_action_value != result_2.updated_action_value:
        raise SyntheticPolicyUpdateTraceSmokeError(
            "step 4 current_action_value must exactly equal step 2 "
            "updated_action_value"
        )
    result_4 = _apply_step(
        second_b,
        step_index=4,
        learning_rate=learning_rate,
        discount_factor=discount_factor,
    )

    return SyntheticPolicyUpdateTraceResult(
        trace_version=SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION,
        step_count=4,
        record_ids=(
            result_1.record_id,
            result_2.record_id,
            result_3.record_id,
            result_4.record_id,
        ),
        source_kind=result_1.source_kind,
        learning_rate=result_1.learning_rate,
        discount_factor=result_1.discount_factor,
        state_action_keys=(key_a, key_b),
        initial_action_values=(
            result_1.current_action_value,
            result_2.current_action_value,
        ),
        intermediate_action_values=(
            result_1.updated_action_value,
            result_2.updated_action_value,
        ),
        final_action_values=(
            result_3.updated_action_value,
            result_4.updated_action_value,
        ),
        step_results=(result_1, result_2, result_3, result_4),
        trace_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


def _has_duplicate_record_ids(
    input_records: Tuple[
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
        SyntheticPolicyUpdateInput,
    ],
) -> bool:
    return any(
        left.record_id == right.record_id
        for left_index, left in enumerate(input_records)
        for right in input_records[left_index + 1 :]
    )


def _state_action_key(
    input_record: SyntheticPolicyUpdateInput,
) -> Tuple[str, str]:
    return (input_record.state_id, input_record.action_id)


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
        raise SyntheticPolicyUpdateTraceSmokeError(
            f"step {step_index} failed: {exc}"
        ) from exc


__all__ = [
    "SYNTHETIC_POLICY_UPDATE_TRACE_SMOKE_VERSION",
    "SyntheticPolicyUpdateTraceResult",
    "SyntheticPolicyUpdateTraceSmokeError",
    "apply_synthetic_policy_update_trace_smoke",
]
