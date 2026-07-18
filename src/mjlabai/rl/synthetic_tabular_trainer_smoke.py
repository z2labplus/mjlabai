"""Bounded P8 synthetic/local tabular training-loop smoke.

This module applies one through eight already-loaded synthetic/local traces in
order through the reviewed table helper. It is not model/network training,
an environment, replay buffer, self-play system, optimizer, checkpointing
system, or production training/evaluation pipeline.
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


SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION = (
    "p8_synthetic_tabular_trainer_smoke_v0.1"
)
MAX_SYNTHETIC_TABULAR_TRAINING_PASSES = 8

_EVIDENCE_GRADE = (
    "P8 bounded synthetic/local tabular training-loop smoke evidence only"
)
_WARNINGS = (
    "bounded synthetic/local tabular training smoke only",
    "maximum eight ordered in-memory passes",
    "no shuffle, minibatch, optimizer, checkpoint or resume",
    "not a model or network training system",
    "not an environment, episode, replay buffer or self-play",
    "not production training or evaluation",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)

_TraceInput = Tuple[
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
    SyntheticPolicyUpdateInput,
]


class SyntheticTabularTrainerSmokeError(ValueError):
    """Raised when the bounded synthetic trainer contract is violated."""


@dataclass(frozen=True)
class SyntheticTabularTrainingResult:
    """Immutable diagnostics from one bounded ordered training run."""

    trainer_version: str
    pass_count: int
    max_passes: int
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]
    final_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry]
    pass_results: Tuple[SyntheticPolicyTableUpdateResult, ...]
    record_ids: Tuple[str, ...]
    training_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def train_synthetic_policy_table_smoke(
    initial_entries: Tuple[SyntheticPolicyTableEntry, SyntheticPolicyTableEntry],
    training_traces: Tuple[_TraceInput, ...],
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticTabularTrainingResult:
    """Run one bounded ordered synthetic/local tabular training loop."""

    if type(training_traces) is not tuple:
        raise SyntheticTabularTrainerSmokeError(
            "training_traces must be an exact tuple"
        )
    pass_count = len(training_traces)
    if not 1 <= pass_count <= MAX_SYNTHETIC_TABULAR_TRAINING_PASSES:
        raise SyntheticTabularTrainerSmokeError(
            "training_traces must contain from 1 through 8 traces"
        )

    current_entries = initial_entries
    pass_results = []
    record_ids = []
    for pass_index, input_records in enumerate(training_traces, start=1):
        try:
            pass_result = apply_synthetic_policy_table_update_smoke(
                current_entries,
                input_records,
                learning_rate=learning_rate,
                discount_factor=discount_factor,
            )
        except SyntheticPolicyTableUpdateSmokeError as exc:
            raise SyntheticTabularTrainerSmokeError(
                f"pass {pass_index} failed: {exc}"
            ) from exc

        for record_id in pass_result.trace_result.record_ids:
            if record_id in record_ids:
                raise SyntheticTabularTrainerSmokeError(
                    "record_ids across all passes must be pairwise distinct"
                )
            record_ids.append(record_id)
        pass_results.append(pass_result)
        current_entries = pass_result.final_entries

    first_result = pass_results[0]
    return SyntheticTabularTrainingResult(
        trainer_version=SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION,
        pass_count=pass_count,
        max_passes=MAX_SYNTHETIC_TABULAR_TRAINING_PASSES,
        initial_entries=first_result.initial_entries,
        final_entries=current_entries,
        pass_results=tuple(pass_results),
        record_ids=tuple(record_ids),
        training_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAX_SYNTHETIC_TABULAR_TRAINING_PASSES",
    "SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION",
    "SyntheticTabularTrainerSmokeError",
    "SyntheticTabularTrainingResult",
    "train_synthetic_policy_table_smoke",
]
