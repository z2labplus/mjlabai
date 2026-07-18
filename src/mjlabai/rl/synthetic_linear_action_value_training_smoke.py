"""Fixed P8 synthetic/local linear action-value model training smoke.

This module performs deterministic temporal-difference parameter updates for
one two-feature, two-action linear model. It is not an environment, replay
buffer, self-play system, tensor framework, checkpointing system, or
production training/evaluation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Real
from typing import Optional, Tuple

from mjlabai.rl.synthetic_policy_update_smoke import (
    SYNTHETIC_LOCAL_SOURCE_KIND,
)


SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION = (
    "p8_synthetic_linear_action_value_training_smoke_v0.1"
)
LINEAR_ACTION_VALUE_FEATURE_COUNT = 2
LINEAR_ACTION_VALUE_ACTION_COUNT = 2
MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS = 8

_EVIDENCE_GRADE = (
    "P8 exact synthetic/local linear action-value model training smoke "
    "evidence only"
)
_WARNINGS = (
    "synthetic/local linear action-value model training smoke only",
    "fixed two features, two actions, four transitions and at most eight epochs",
    "deterministic ordered temporal-difference updates only",
    "no environment, replay buffer, self-play or model-generated data",
    "no external dependency, tensor framework, optimizer or checkpoint",
    "not production training or evaluation",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)

_FeatureVector = Tuple[float, float]
_WeightMatrix = Tuple[Tuple[float, float], Tuple[float, float]]


class SyntheticLinearActionValueTrainingSmokeError(ValueError):
    """Raised when the fixed synthetic linear-training contract is violated."""


@dataclass(frozen=True)
class SyntheticLinearQTransition:
    """One immutable project-authored synthetic/local Q-learning transition."""

    record_id: str
    source_kind: str
    state_features: _FeatureVector
    action_index: int
    reward: float
    next_state_features: Optional[_FeatureVector]
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
class SyntheticLinearActionValueModel:
    """One immutable fixed two-feature, two-action linear Q model."""

    weights: _WeightMatrix
    biases: Tuple[float, float]


@dataclass(frozen=True)
class SyntheticLinearActionValueTrainingResult:
    """Immutable diagnostics from one bounded deterministic training run."""

    training_version: str
    feature_count: int
    action_count: int
    epoch_count: int
    max_epochs: int
    transition_count: int
    update_count: int
    initial_model: SyntheticLinearActionValueModel
    final_model: SyntheticLinearActionValueModel
    epoch_mean_squared_td_errors: Tuple[float, ...]
    record_ids: Tuple[str, str, str, str]
    training_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _finite_float(value: object, field_name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{field_name} must be a finite real number"
        )
    try:
        normalized = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{field_name} must be representable as a finite float"
        ) from exc
    if not math.isfinite(normalized):
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{field_name} must be a finite real number"
        )
    return normalized


def _finite_computation(value: float, operation: str) -> float:
    if not math.isfinite(value):
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{operation} produced a non-finite value"
        )
    return value


def _normalize_features(value: object, field_name: str) -> _FeatureVector:
    if type(value) is not tuple or len(value) != LINEAR_ACTION_VALUE_FEATURE_COUNT:
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{field_name} must be an exact two-value tuple"
        )
    return (
        _finite_float(value[0], f"{field_name}[0]"),
        _finite_float(value[1], f"{field_name}[1]"),
    )


def _normalize_model(value: object) -> SyntheticLinearActionValueModel:
    if type(value) is not SyntheticLinearActionValueModel:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "initial_model must be an exact SyntheticLinearActionValueModel"
        )
    if type(value.weights) is not tuple or len(value.weights) != 2:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "initial_model.weights must be an exact two-row tuple"
        )
    row_zero = _normalize_features(value.weights[0], "initial_model.weights[0]")
    row_one = _normalize_features(value.weights[1], "initial_model.weights[1]")
    if type(value.biases) is not tuple or len(value.biases) != 2:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "initial_model.biases must be an exact two-value tuple"
        )
    return SyntheticLinearActionValueModel(
        weights=(row_zero, row_one),
        biases=(
            _finite_float(value.biases[0], "initial_model.biases[0]"),
            _finite_float(value.biases[1], "initial_model.biases[1]"),
        ),
    )


def _normalize_transition(
    value: object,
    transition_index: int,
) -> SyntheticLinearQTransition:
    prefix = f"transitions[{transition_index}]"
    if type(value) is not SyntheticLinearQTransition:
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{prefix} must be an exact SyntheticLinearQTransition"
        )
    if type(value.record_id) is not str or not value.record_id.strip():
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{prefix}.record_id must be a non-empty string"
        )
    if value.source_kind != SYNTHETIC_LOCAL_SOURCE_KIND:
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{prefix}.source_kind must be {SYNTHETIC_LOCAL_SOURCE_KIND!r}"
        )
    if type(value.action_index) is not int or value.action_index not in (0, 1):
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{prefix}.action_index must be exact int 0 or 1"
        )
    if type(value.terminal) is not bool:
        raise SyntheticLinearActionValueTrainingSmokeError(
            f"{prefix}.terminal must be bool"
        )

    state_features = _normalize_features(
        value.state_features,
        f"{prefix}.state_features",
    )
    reward = _finite_float(value.reward, f"{prefix}.reward")
    if value.terminal:
        if value.next_state_features is not None:
            raise SyntheticLinearActionValueTrainingSmokeError(
                f"{prefix}.next_state_features must be None when terminal"
            )
        next_state_features = None
    else:
        next_state_features = _normalize_features(
            value.next_state_features,
            f"{prefix}.next_state_features",
        )

    required_flags = {
        "project_authored": True,
        "synthetic": True,
        "local_only": True,
        "uses_real_data": False,
        "uses_external_log": False,
        "uses_platform_data": False,
        "uses_model_output": False,
        "uses_self_play": False,
    }
    for field_name, expected in required_flags.items():
        actual = getattr(value, field_name)
        if type(actual) is not bool or actual is not expected:
            raise SyntheticLinearActionValueTrainingSmokeError(
                f"{prefix}.{field_name} must be {expected}"
            )

    return SyntheticLinearQTransition(
        record_id=value.record_id,
        source_kind=value.source_kind,
        state_features=state_features,
        action_index=value.action_index,
        reward=reward,
        next_state_features=next_state_features,
        terminal=value.terminal,
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
        uses_model_output=False,
        uses_self_play=False,
    )


def _action_value(
    weights: list[list[float]],
    biases: list[float],
    features: _FeatureVector,
    action_index: int,
) -> float:
    return _finite_computation(
        biases[action_index]
        + weights[action_index][0] * features[0]
        + weights[action_index][1] * features[1],
        "action-value calculation",
    )


def train_synthetic_linear_action_value_model_smoke(
    initial_model: SyntheticLinearActionValueModel,
    transitions: Tuple[
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
    ],
    *,
    learning_rate: float,
    discount_factor: float,
    epoch_count: int,
) -> SyntheticLinearActionValueTrainingResult:
    """Train one fixed linear Q model on four synthetic/local transitions."""

    normalized_model = _normalize_model(initial_model)
    if type(transitions) is not tuple or len(transitions) != 4:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "transitions must be an exact four-transition tuple"
        )
    normalized_transitions = tuple(
        _normalize_transition(transition, index)
        for index, transition in enumerate(transitions)
    )
    record_ids = tuple(transition.record_id for transition in normalized_transitions)
    if len(set(record_ids)) != 4:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "transition record_ids must be pairwise distinct"
        )

    normalized_learning_rate = _finite_float(learning_rate, "learning_rate")
    if not 0.0 < normalized_learning_rate <= 1.0:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "learning_rate must satisfy 0 < learning_rate <= 1"
        )
    normalized_discount_factor = _finite_float(
        discount_factor,
        "discount_factor",
    )
    if not 0.0 <= normalized_discount_factor <= 1.0:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "discount_factor must satisfy 0 <= discount_factor <= 1"
        )
    if type(epoch_count) is not int or not 1 <= epoch_count <= 8:
        raise SyntheticLinearActionValueTrainingSmokeError(
            "epoch_count must be exact int from 1 through 8"
        )

    weights = [list(row) for row in normalized_model.weights]
    biases = list(normalized_model.biases)
    epoch_losses = []
    for _ in range(epoch_count):
        squared_error_sum = 0.0
        for transition in normalized_transitions:
            action_index = transition.action_index
            prediction = _action_value(
                weights,
                biases,
                transition.state_features,
                action_index,
            )
            if transition.terminal:
                target = transition.reward
            else:
                next_features = transition.next_state_features
                if next_features is None:
                    raise AssertionError("validated non-terminal transition is missing next state")
                target = _finite_computation(
                    transition.reward
                    + normalized_discount_factor
                    * max(
                        _action_value(weights, biases, next_features, 0),
                        _action_value(weights, biases, next_features, 1),
                    ),
                    "target calculation",
                )
            td_error = _finite_computation(
                target - prediction,
                "TD-error calculation",
            )
            for feature_index in range(LINEAR_ACTION_VALUE_FEATURE_COUNT):
                weights[action_index][feature_index] = _finite_computation(
                    weights[action_index][feature_index]
                    + normalized_learning_rate
                    * td_error
                    * transition.state_features[feature_index],
                    "weight update",
                )
            biases[action_index] = _finite_computation(
                biases[action_index] + normalized_learning_rate * td_error,
                "bias update",
            )
            squared_error_sum = _finite_computation(
                squared_error_sum + td_error * td_error,
                "squared TD-error accumulation",
            )
        epoch_losses.append(
            _finite_computation(
                squared_error_sum / len(normalized_transitions),
                "epoch mean-squared TD-error calculation",
            )
        )

    final_model = SyntheticLinearActionValueModel(
        weights=(tuple(weights[0]), tuple(weights[1])),
        biases=tuple(biases),
    )
    return SyntheticLinearActionValueTrainingResult(
        training_version=SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION,
        feature_count=LINEAR_ACTION_VALUE_FEATURE_COUNT,
        action_count=LINEAR_ACTION_VALUE_ACTION_COUNT,
        epoch_count=epoch_count,
        max_epochs=MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS,
        transition_count=4,
        update_count=4 * epoch_count,
        initial_model=normalized_model,
        final_model=final_model,
        epoch_mean_squared_td_errors=tuple(epoch_losses),
        record_ids=record_ids,
        training_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION",
    "LINEAR_ACTION_VALUE_FEATURE_COUNT",
    "LINEAR_ACTION_VALUE_ACTION_COUNT",
    "MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS",
    "SyntheticLinearActionValueTrainingSmokeError",
    "SyntheticLinearQTransition",
    "SyntheticLinearActionValueModel",
    "SyntheticLinearActionValueTrainingResult",
    "train_synthetic_linear_action_value_model_smoke",
]
