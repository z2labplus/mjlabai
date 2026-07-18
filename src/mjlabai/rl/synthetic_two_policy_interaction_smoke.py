"""Bounded P8 synthetic/local two-policy interaction smoke.

This module alternates exactly two independent policy models across two or
four project-authored turns. It is not an environment, game episode, replay
buffer, production self-play system, or production training/evaluation path.
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


SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION = (
    "p8_synthetic_two_policy_interaction_smoke_v0.1"
)
MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS = 4

_EVIDENCE_GRADE = (
    "P8 exact bounded synthetic/local two-policy alternating interaction "
    "smoke evidence only"
)
_WARNINGS = (
    "bounded two-policy synthetic/local interaction smoke only",
    "exactly two participants and two or four alternating turns",
    "one reviewed closed-loop call per turn",
    "no general environment, game episode, outcome generation, replay or production self-play",
    "no model loading, persistence, checkpoint or external dependency",
    "not production training, inference or evaluation",
    "interaction action changes are not policy-quality or model-strength evidence",
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


class SyntheticTwoPolicyInteractionSmokeError(ValueError):
    """Raised when the bounded two-policy interaction contract is violated."""


@dataclass(frozen=True)
class SyntheticTwoPolicyParticipantInput:
    """One immutable synthetic/local policy participant."""

    policy_id: str
    initial_model: SyntheticLinearActionValueModel


@dataclass(frozen=True)
class SyntheticTwoPolicyInteractionTurnInput:
    """One immutable authored turn for the alternating interaction."""

    turn_id: str
    actor_policy_id: str
    decision_probes: _DecisionProbes
    candidate_transition_batches: _CandidateTransitionBatches
    learning_rate: float
    discount_factor: float


@dataclass(frozen=True)
class SyntheticTwoPolicyInteractionTurnResult:
    """Immutable diagnostics for one actor turn."""

    turn_index: int
    turn_id: str
    actor_policy_id: str
    non_actor_policy_id: str
    actor_initial_model: SyntheticLinearActionValueModel
    actor_final_model: SyntheticLinearActionValueModel
    non_actor_model_before: SyntheticLinearActionValueModel
    non_actor_model_after: SyntheticLinearActionValueModel
    one_step_result: SyntheticOneStepPolicyImprovementResult
    non_actor_model_unchanged: bool


@dataclass(frozen=True)
class SyntheticTwoPolicyInteractionResult:
    """Immutable ordered diagnostics for the exact two-policy interaction."""

    interaction_version: str
    participant_count: int
    turn_count: int
    max_turns: int
    policy_ids: Tuple[str, str]
    initial_models: Tuple[
        SyntheticLinearActionValueModel,
        SyntheticLinearActionValueModel,
    ]
    final_models: Tuple[
        SyntheticLinearActionValueModel,
        SyntheticLinearActionValueModel,
    ]
    turn_ids: Tuple[str, ...]
    turn_results: Tuple[SyntheticTwoPolicyInteractionTurnResult, ...]
    selected_actions: Tuple[int, ...]
    after_actions: Tuple[int, ...]
    global_candidate_transition_record_ids: Tuple[str, ...]
    interaction_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _validate_participant(
    participant: object,
    participant_index: int,
) -> SyntheticTwoPolicyParticipantInput:
    if type(participant) is not SyntheticTwoPolicyParticipantInput:
        raise SyntheticTwoPolicyInteractionSmokeError(
            f"participants[{participant_index}] must be an exact SyntheticTwoPolicyParticipantInput"
        )
    if type(participant.policy_id) is not str or not participant.policy_id.strip():
        raise SyntheticTwoPolicyInteractionSmokeError(
            f"participant {participant_index + 1} policy_id must be a non-empty string"
        )
    return participant


def run_synthetic_two_policy_interaction_smoke(
    participants: Tuple[
        SyntheticTwoPolicyParticipantInput,
        SyntheticTwoPolicyParticipantInput,
    ],
    turns: Tuple[SyntheticTwoPolicyInteractionTurnInput, ...],
) -> SyntheticTwoPolicyInteractionResult:
    """Run exactly two or four alternating reviewed policy-improvement turns."""

    if type(participants) is not tuple or len(participants) != 2:
        raise SyntheticTwoPolicyInteractionSmokeError(
            "participants must be an exact two-participant tuple"
        )
    participant_zero = _validate_participant(participants[0], 0)
    participant_one = _validate_participant(participants[1], 1)
    policy_ids = (participant_zero.policy_id, participant_one.policy_id)
    if policy_ids[0] == policy_ids[1]:
        raise SyntheticTwoPolicyInteractionSmokeError(
            "participant policy_ids must be distinct"
        )
    if type(turns) is not tuple:
        raise SyntheticTwoPolicyInteractionSmokeError(
            "turns must be an exact tuple"
        )
    if len(turns) not in (2, MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS):
        raise SyntheticTwoPolicyInteractionSmokeError(
            "turns must contain exactly 2 or exactly 4 turn inputs"
        )

    current_model_zero = participant_zero.initial_model
    current_model_one = participant_one.initial_model
    normalized_initial_model_zero = None
    normalized_initial_model_one = None
    turn_ids = []
    seen_turn_ids = set()
    global_record_ids = []
    seen_record_ids = set()
    turn_results = []
    for turn_index, turn in enumerate(turns, start=1):
        if type(turn) is not SyntheticTwoPolicyInteractionTurnInput:
            raise SyntheticTwoPolicyInteractionSmokeError(
                f"turns[{turn_index - 1}] must be an exact SyntheticTwoPolicyInteractionTurnInput"
            )
        if type(turn.turn_id) is not str or not turn.turn_id.strip():
            raise SyntheticTwoPolicyInteractionSmokeError(
                f"turn {turn_index} turn_id must be a non-empty string"
            )
        if turn.turn_id in seen_turn_ids:
            raise SyntheticTwoPolicyInteractionSmokeError(
                "turn_ids must be pairwise distinct"
            )
        actor_index = (turn_index - 1) % 2
        expected_actor_id = policy_ids[actor_index]
        if type(turn.actor_policy_id) is not str or turn.actor_policy_id != expected_actor_id:
            raise SyntheticTwoPolicyInteractionSmokeError(
                f"turn {turn_index} actor_policy_id must be {expected_actor_id!r}"
            )
        turn_ids.append(turn.turn_id)
        seen_turn_ids.add(turn.turn_id)
        try:
            batches = _normalize_candidate_batches(
                turn.candidate_transition_batches
            )
        except SyntheticOneStepPolicyImprovementSmokeError as exc:
            raise SyntheticTwoPolicyInteractionSmokeError(
                f"turn {turn_index} failed: {exc}"
            ) from exc
        turn_record_ids = tuple(
            transition.record_id
            for batch in batches
            for transition in batch
        )
        if seen_record_ids.intersection(turn_record_ids):
            raise SyntheticTwoPolicyInteractionSmokeError(
                "candidate transition record_ids must be globally pairwise distinct across all turns"
            )
        global_record_ids.extend(turn_record_ids)
        seen_record_ids.update(turn_record_ids)

        if actor_index == 0:
            actor_model = current_model_zero
            non_actor_model = current_model_one
            non_actor_policy_id = policy_ids[1]
        else:
            actor_model = current_model_one
            non_actor_model = current_model_zero
            non_actor_policy_id = policy_ids[0]
        try:
            one_step_result = run_synthetic_one_step_policy_improvement_smoke(
                actor_model,
                turn.decision_probes,
                batches,
                learning_rate=turn.learning_rate,
                discount_factor=turn.discount_factor,
            )
        except SyntheticOneStepPolicyImprovementSmokeError as exc:
            raise SyntheticTwoPolicyInteractionSmokeError(
                f"turn {turn_index} failed: {exc}"
            ) from exc

        actor_final_model = one_step_result.training_result.final_model
        if actor_index == 0:
            if normalized_initial_model_zero is None:
                normalized_initial_model_zero = one_step_result.initial_model
            current_model_zero = actor_final_model
            non_actor_model_after = current_model_one
        else:
            if normalized_initial_model_one is None:
                normalized_initial_model_one = one_step_result.initial_model
            current_model_one = actor_final_model
            non_actor_model_after = current_model_zero
        turn_results.append(
            SyntheticTwoPolicyInteractionTurnResult(
                turn_index=turn_index,
                turn_id=turn.turn_id,
                actor_policy_id=expected_actor_id,
                non_actor_policy_id=non_actor_policy_id,
                actor_initial_model=one_step_result.initial_model,
                actor_final_model=actor_final_model,
                non_actor_model_before=non_actor_model,
                non_actor_model_after=non_actor_model_after,
                one_step_result=one_step_result,
                non_actor_model_unchanged=(
                    non_actor_model == non_actor_model_after
                ),
            )
        )

    if normalized_initial_model_zero is None or normalized_initial_model_one is None:
        raise AssertionError("validated alternating turns must exercise both policies")
    return SyntheticTwoPolicyInteractionResult(
        interaction_version=SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION,
        participant_count=2,
        turn_count=len(turn_results),
        max_turns=MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS,
        policy_ids=policy_ids,
        initial_models=(
            normalized_initial_model_zero,
            normalized_initial_model_one,
        ),
        final_models=(current_model_zero, current_model_one),
        turn_ids=tuple(turn_ids),
        turn_results=tuple(turn_results),
        selected_actions=tuple(
            result.one_step_result.selected_action_index
            for result in turn_results
        ),
        after_actions=tuple(
            result.one_step_result.after_selected_action_index
            for result in turn_results
        ),
        global_candidate_transition_record_ids=tuple(global_record_ids),
        interaction_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION",
    "MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS",
    "SyntheticTwoPolicyParticipantInput",
    "SyntheticTwoPolicyInteractionTurnInput",
    "SyntheticTwoPolicyInteractionTurnResult",
    "SyntheticTwoPolicyInteractionSmokeError",
    "SyntheticTwoPolicyInteractionResult",
    "run_synthetic_two_policy_interaction_smoke",
]
