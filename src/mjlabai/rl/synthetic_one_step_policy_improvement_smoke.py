"""One-step P8 synthetic/local policy-improvement closed-loop smoke.

This module links one reviewed greedy decision to one selected synthetic/local
training batch and one reviewed after-decision. It is not a general
environment, episode loop, replay buffer, self-play system, or production
training/evaluation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.rl.synthetic_linear_action_value_training_smoke import (
    SyntheticLinearActionValueModel,
    SyntheticLinearActionValueTrainingResult,
    SyntheticLinearActionValueTrainingSmokeError,
    SyntheticLinearQTransition,
    _normalize_transition,
    train_synthetic_linear_action_value_model_smoke,
)
from mjlabai.rl.synthetic_linear_greedy_decision_smoke import (
    SyntheticLinearDecisionProbe,
    SyntheticLinearGreedyDecisionDiagnosticResult,
    SyntheticLinearGreedyDecisionSmokeError,
    run_synthetic_linear_greedy_decision_diagnostic,
)


SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION = (
    "p8_synthetic_one_step_policy_improvement_smoke_v0.1"
)

_EVIDENCE_GRADE = (
    "P8 exact one-step synthetic/local policy-improvement closed-loop smoke "
    "evidence only"
)
_WARNINGS = (
    "one-step synthetic/local policy-improvement closed-loop smoke only",
    "one before decision, one selected four-transition batch, one training epoch and one after decision",
    "unselected candidate batch is not trained",
    "no general environment, episode, replay buffer or self-play",
    "no model loading, persistence, checkpoint or external dependency",
    "not production training, inference or evaluation",
    "action change is not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)

_TransitionBatch = Tuple[
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
]
_DecisionProbes = Tuple[
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
]


class SyntheticOneStepPolicyImprovementSmokeError(ValueError):
    """Raised when the one-step closed-loop contract is violated."""


@dataclass(frozen=True)
class SyntheticOneStepPolicyImprovementResult:
    """Immutable diagnostics from one decision-training-decision loop."""

    smoke_version: str
    initial_model: SyntheticLinearActionValueModel
    before_diagnostic: SyntheticLinearGreedyDecisionDiagnosticResult
    selected_action_index: int
    selected_transition_record_ids: Tuple[str, str, str, str]
    training_result: SyntheticLinearActionValueTrainingResult
    after_diagnostic: SyntheticLinearGreedyDecisionDiagnosticResult
    after_selected_action_index: int
    controlled_action_changed: bool
    closed_loop_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _normalize_candidate_batches(
    value: object,
) -> Tuple[_TransitionBatch, _TransitionBatch]:
    if type(value) is not tuple or len(value) != 2:
        raise SyntheticOneStepPolicyImprovementSmokeError(
            "candidate_transition_batches must be an exact two-batch tuple"
        )

    normalized_batches = []
    global_record_ids = []
    for batch_index, batch in enumerate(value):
        if type(batch) is not tuple or len(batch) != 4:
            raise SyntheticOneStepPolicyImprovementSmokeError(
                f"candidate_transition_batches[{batch_index}] must be an exact four-transition tuple"
            )
        normalized_batch = []
        for transition_index, transition in enumerate(batch):
            try:
                normalized_transition = _normalize_transition(
                    transition,
                    transition_index,
                )
            except SyntheticLinearActionValueTrainingSmokeError as exc:
                raise SyntheticOneStepPolicyImprovementSmokeError(
                    f"candidate batch {batch_index} transition {transition_index + 1} validation failed: {exc}"
                ) from exc
            normalized_batch.append(normalized_transition)
            global_record_ids.append(normalized_transition.record_id)
        if normalized_batch[0].action_index != batch_index:
            raise SyntheticOneStepPolicyImprovementSmokeError(
                f"candidate batch {batch_index} first transition action_index must be {batch_index}"
            )
        normalized_batches.append(tuple(normalized_batch))

    if len(set(global_record_ids)) != 8:
        raise SyntheticOneStepPolicyImprovementSmokeError(
            "candidate transition record_ids must be pairwise distinct across both batches"
        )
    return tuple(normalized_batches)


def run_synthetic_one_step_policy_improvement_smoke(
    initial_model: SyntheticLinearActionValueModel,
    decision_probes: _DecisionProbes,
    candidate_transition_batches: Tuple[_TransitionBatch, _TransitionBatch],
    *,
    learning_rate: float,
    discount_factor: float,
) -> SyntheticOneStepPolicyImprovementResult:
    """Run one fixed before-decision, selected training, after-decision loop."""

    normalized_batches = _normalize_candidate_batches(candidate_transition_batches)
    try:
        before_diagnostic = run_synthetic_linear_greedy_decision_diagnostic(
            initial_model,
            decision_probes,
        )
    except SyntheticLinearGreedyDecisionSmokeError as exc:
        raise SyntheticOneStepPolicyImprovementSmokeError(
            f"before decision failed: {exc}"
        ) from exc

    selected_action_index = before_diagnostic.decisions[0].selected_action_index
    selected_batch = normalized_batches[selected_action_index]
    try:
        training_result = train_synthetic_linear_action_value_model_smoke(
            before_diagnostic.model,
            selected_batch,
            learning_rate=learning_rate,
            discount_factor=discount_factor,
            epoch_count=1,
        )
    except SyntheticLinearActionValueTrainingSmokeError as exc:
        raise SyntheticOneStepPolicyImprovementSmokeError(
            f"selected batch training failed: {exc}"
        ) from exc

    try:
        after_diagnostic = run_synthetic_linear_greedy_decision_diagnostic(
            training_result.final_model,
            decision_probes,
        )
    except SyntheticLinearGreedyDecisionSmokeError as exc:
        raise SyntheticOneStepPolicyImprovementSmokeError(
            f"after decision failed: {exc}"
        ) from exc

    after_selected_action_index = (
        after_diagnostic.decisions[0].selected_action_index
    )
    return SyntheticOneStepPolicyImprovementResult(
        smoke_version=SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION,
        initial_model=before_diagnostic.model,
        before_diagnostic=before_diagnostic,
        selected_action_index=selected_action_index,
        selected_transition_record_ids=training_result.record_ids,
        training_result=training_result,
        after_diagnostic=after_diagnostic,
        after_selected_action_index=after_selected_action_index,
        controlled_action_changed=(
            selected_action_index != after_selected_action_index
        ),
        closed_loop_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION",
    "SyntheticOneStepPolicyImprovementSmokeError",
    "SyntheticOneStepPolicyImprovementResult",
    "run_synthetic_one_step_policy_improvement_smoke",
]
