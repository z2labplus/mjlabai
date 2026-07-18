"""Bounded P8 synthetic/local policy-improvement sequence smoke.

This module chains one through four reviewed one-step closed loops. It is not
an environment, episode generator, replay buffer, self-play system, or
production training/evaluation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.rl.synthetic_linear_action_value_training_smoke import (
    SyntheticLinearActionValueModel,
    SyntheticLinearQTransition,
)
from mjlabai.rl.synthetic_linear_greedy_decision_smoke import (
    SyntheticLinearDecisionProbe,
)
from mjlabai.rl.synthetic_one_step_policy_improvement_smoke import (
    SyntheticOneStepPolicyImprovementResult,
    SyntheticOneStepPolicyImprovementSmokeError,
    _normalize_candidate_batches,
    run_synthetic_one_step_policy_improvement_smoke,
)


SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION = (
    "p8_synthetic_policy_improvement_sequence_smoke_v0.1"
)
MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS = 4

_EVIDENCE_GRADE = (
    "P8 exact bounded synthetic/local policy-improvement sequence smoke "
    "evidence only"
)
_WARNINGS = (
    "bounded synthetic/local policy-improvement sequence smoke only",
    "maximum four steps and one reviewed closed-loop call per step",
    "no general environment, episode, replay buffer or self-play",
    "no model loading, persistence, checkpoint or external dependency",
    "not production training, inference or evaluation",
    "action changes are not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)

_DecisionProbes = Tuple[
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
]
_TransitionBatch = Tuple[
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
]
_CandidateTransitionBatches = Tuple[_TransitionBatch, _TransitionBatch]


class SyntheticPolicyImprovementSequenceSmokeError(ValueError):
    """Raised when the bounded sequence contract is violated."""


@dataclass(frozen=True)
class SyntheticPolicyImprovementStepInput:
    """One immutable input for a reviewed one-step closed loop."""

    step_id: str
    decision_probes: _DecisionProbes
    candidate_transition_batches: _CandidateTransitionBatches
    learning_rate: float
    discount_factor: float


@dataclass(frozen=True)
class SyntheticPolicyImprovementSequenceResult:
    """Immutable ordered diagnostics from a bounded sequence."""

    sequence_version: str
    step_count: int
    max_steps: int
    initial_model: SyntheticLinearActionValueModel
    final_model: SyntheticLinearActionValueModel
    step_ids: Tuple[str, ...]
    step_results: Tuple[SyntheticOneStepPolicyImprovementResult, ...]
    selected_actions: Tuple[int, ...]
    after_actions: Tuple[int, ...]
    global_candidate_transition_record_ids: Tuple[str, ...]
    sequence_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def run_synthetic_policy_improvement_sequence_smoke(
    initial_model: SyntheticLinearActionValueModel,
    steps: Tuple[SyntheticPolicyImprovementStepInput, ...],
) -> SyntheticPolicyImprovementSequenceResult:
    """Run one through four reviewed closed-loop steps in input order."""

    if type(steps) is not tuple:
        raise SyntheticPolicyImprovementSequenceSmokeError(
            "steps must be an exact tuple"
        )
    if not 1 <= len(steps) <= MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS:
        raise SyntheticPolicyImprovementSequenceSmokeError(
            "steps must contain from 1 through 4 exact step inputs"
        )

    step_ids = []
    seen_step_ids = set()
    global_record_ids = []
    seen_record_ids = set()
    current_model = initial_model
    step_results = []
    for step_index, step in enumerate(steps, start=1):
        if type(step) is not SyntheticPolicyImprovementStepInput:
            raise SyntheticPolicyImprovementSequenceSmokeError(
                f"steps[{step_index - 1}] must be an exact SyntheticPolicyImprovementStepInput"
            )
        if type(step.step_id) is not str or not step.step_id.strip():
            raise SyntheticPolicyImprovementSequenceSmokeError(
                f"step {step_index} step_id must be a non-empty string"
            )
        if step.step_id in seen_step_ids:
            raise SyntheticPolicyImprovementSequenceSmokeError(
                "step_ids must be pairwise distinct"
            )
        step_ids.append(step.step_id)
        seen_step_ids.add(step.step_id)
        try:
            batches = _normalize_candidate_batches(
                step.candidate_transition_batches
            )
        except SyntheticOneStepPolicyImprovementSmokeError as exc:
            raise SyntheticPolicyImprovementSequenceSmokeError(
                f"step {step_index} failed: {exc}"
            ) from exc
        step_record_ids = tuple(
            transition.record_id
            for batch in batches
            for transition in batch
        )
        if seen_record_ids.intersection(step_record_ids):
            raise SyntheticPolicyImprovementSequenceSmokeError(
                "candidate transition record_ids must be globally pairwise distinct across all steps"
            )
        global_record_ids.extend(step_record_ids)
        seen_record_ids.update(step_record_ids)
        try:
            result = run_synthetic_one_step_policy_improvement_smoke(
                current_model,
                step.decision_probes,
                batches,
                learning_rate=step.learning_rate,
                discount_factor=step.discount_factor,
            )
        except SyntheticOneStepPolicyImprovementSmokeError as exc:
            raise SyntheticPolicyImprovementSequenceSmokeError(
                f"step {step_index} failed: {exc}"
            ) from exc
        step_results.append(result)
        current_model = result.training_result.final_model

    first_result = step_results[0]
    return SyntheticPolicyImprovementSequenceResult(
        sequence_version=SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION,
        step_count=len(step_results),
        max_steps=MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS,
        initial_model=first_result.initial_model,
        final_model=current_model,
        step_ids=tuple(step_ids),
        step_results=tuple(step_results),
        selected_actions=tuple(
            result.selected_action_index for result in step_results
        ),
        after_actions=tuple(
            result.after_selected_action_index for result in step_results
        ),
        global_candidate_transition_record_ids=tuple(global_record_ids),
        sequence_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION",
    "MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS",
    "SyntheticPolicyImprovementStepInput",
    "SyntheticPolicyImprovementSequenceSmokeError",
    "SyntheticPolicyImprovementSequenceResult",
    "run_synthetic_policy_improvement_sequence_smoke",
]
