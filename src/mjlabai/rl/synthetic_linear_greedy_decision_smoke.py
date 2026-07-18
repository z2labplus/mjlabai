"""Fixed P8 synthetic/local linear-model greedy-decision diagnostic.

This module computes two action values and one deterministic greedy decision
for exactly three project-authored synthetic/local probes. It is not an
environment, gameplay loop, self-play system, model loader, or production
inference/evaluation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.rl.synthetic_linear_action_value_training_smoke import (
    SyntheticLinearActionValueModel,
    SyntheticLinearActionValueTrainingSmokeError,
    _action_value,
    _normalize_features,
    _normalize_model,
)
from mjlabai.rl.synthetic_policy_update_smoke import (
    SYNTHETIC_LOCAL_SOURCE_KIND,
)


SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION = (
    "p8_synthetic_linear_greedy_decision_smoke_v0.1"
)

_EVIDENCE_GRADE = (
    "P8 exact synthetic/local linear-model inference and greedy-decision "
    "diagnostic evidence only"
)
_WARNINGS = (
    "synthetic/local linear-model inference and greedy-decision diagnostic only",
    "fixed two features, two actions and three probes",
    "deterministic lower-action-index tie break",
    "no environment, gameplay, replay buffer or self-play",
    "no model loading, external dependency, persistence or checkpoint",
    "not production inference or evaluation",
    "not model-strength evidence",
    "not stable-dan or LuckyJ comparison",
    "not candidate-promotion evidence",
)

_FeatureVector = Tuple[float, float]
_ActionIndices = Tuple[int, int]


class SyntheticLinearGreedyDecisionSmokeError(ValueError):
    """Raised when the fixed synthetic decision contract is violated."""


@dataclass(frozen=True)
class SyntheticLinearDecisionProbe:
    """One immutable project-authored synthetic/local decision probe."""

    probe_id: str
    source_kind: str
    features: _FeatureVector
    legal_action_indices: _ActionIndices
    project_authored: bool
    synthetic: bool
    local_only: bool
    uses_real_data: bool
    uses_external_log: bool
    uses_platform_data: bool
    uses_model_output: bool
    uses_self_play: bool


@dataclass(frozen=True)
class SyntheticLinearDecision:
    """One immutable pair of action values and deterministic decision."""

    probe_id: str
    features: _FeatureVector
    legal_action_indices: _ActionIndices
    action_values: Tuple[float, float]
    selected_action_index: int
    tie_detected: bool


@dataclass(frozen=True)
class SyntheticLinearGreedyDecisionDiagnosticResult:
    """Immutable diagnostics for exactly three fixed decisions."""

    diagnostic_version: str
    model: SyntheticLinearActionValueModel
    probe_count: int
    decisions: Tuple[
        SyntheticLinearDecision,
        SyntheticLinearDecision,
        SyntheticLinearDecision,
    ]
    probe_ids: Tuple[str, str, str]
    inference_applied: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _normalize_probe(
    value: object,
    probe_index: int,
) -> SyntheticLinearDecisionProbe:
    prefix = f"probes[{probe_index}]"
    if type(value) is not SyntheticLinearDecisionProbe:
        raise SyntheticLinearGreedyDecisionSmokeError(
            f"{prefix} must be an exact SyntheticLinearDecisionProbe"
        )
    if type(value.probe_id) is not str or not value.probe_id.strip():
        raise SyntheticLinearGreedyDecisionSmokeError(
            f"{prefix}.probe_id must be a non-empty string"
        )
    if value.source_kind != SYNTHETIC_LOCAL_SOURCE_KIND:
        raise SyntheticLinearGreedyDecisionSmokeError(
            f"{prefix}.source_kind must be {SYNTHETIC_LOCAL_SOURCE_KIND!r}"
        )
    try:
        features = _normalize_features(value.features, f"{prefix}.features")
    except SyntheticLinearActionValueTrainingSmokeError as exc:
        raise SyntheticLinearGreedyDecisionSmokeError(
            f"probe {probe_index + 1} feature validation failed: {exc}"
        ) from exc
    if (
        type(value.legal_action_indices) is not tuple
        or len(value.legal_action_indices) != 2
        or type(value.legal_action_indices[0]) is not int
        or type(value.legal_action_indices[1]) is not int
        or value.legal_action_indices != (0, 1)
    ):
        raise SyntheticLinearGreedyDecisionSmokeError(
            f"{prefix}.legal_action_indices must be exact tuple (0, 1)"
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
            raise SyntheticLinearGreedyDecisionSmokeError(
                f"{prefix}.{field_name} must be {expected}"
            )

    return SyntheticLinearDecisionProbe(
        probe_id=value.probe_id,
        source_kind=value.source_kind,
        features=features,
        legal_action_indices=(0, 1),
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
        uses_model_output=False,
        uses_self_play=False,
    )


def run_synthetic_linear_greedy_decision_diagnostic(
    model: SyntheticLinearActionValueModel,
    probes: Tuple[
        SyntheticLinearDecisionProbe,
        SyntheticLinearDecisionProbe,
        SyntheticLinearDecisionProbe,
    ],
) -> SyntheticLinearGreedyDecisionDiagnosticResult:
    """Compute fixed action values and deterministic decisions for three probes."""

    try:
        normalized_model = _normalize_model(model)
    except SyntheticLinearActionValueTrainingSmokeError as exc:
        raise SyntheticLinearGreedyDecisionSmokeError(
            f"model validation failed: {exc}"
        ) from exc
    if type(probes) is not tuple or len(probes) != 3:
        raise SyntheticLinearGreedyDecisionSmokeError(
            "probes must be an exact three-probe tuple"
        )
    normalized_probes = tuple(
        _normalize_probe(probe, index) for index, probe in enumerate(probes)
    )
    probe_ids = tuple(probe.probe_id for probe in normalized_probes)
    if len(set(probe_ids)) != 3:
        raise SyntheticLinearGreedyDecisionSmokeError(
            "probe_ids must be pairwise distinct"
        )

    weights = [list(row) for row in normalized_model.weights]
    biases = list(normalized_model.biases)
    decisions = []
    for probe_index, probe in enumerate(normalized_probes, start=1):
        try:
            action_zero_value = _action_value(
                weights,
                biases,
                probe.features,
                0,
            )
            action_one_value = _action_value(
                weights,
                biases,
                probe.features,
                1,
            )
        except SyntheticLinearActionValueTrainingSmokeError as exc:
            raise SyntheticLinearGreedyDecisionSmokeError(
                f"probe {probe_index} action-value calculation failed: {exc}"
            ) from exc
        tie_detected = action_zero_value == action_one_value
        selected_action_index = 1 if action_one_value > action_zero_value else 0
        decisions.append(
            SyntheticLinearDecision(
                probe_id=probe.probe_id,
                features=probe.features,
                legal_action_indices=(0, 1),
                action_values=(action_zero_value, action_one_value),
                selected_action_index=selected_action_index,
                tie_detected=tie_detected,
            )
        )

    return SyntheticLinearGreedyDecisionDiagnosticResult(
        diagnostic_version=SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION,
        model=normalized_model,
        probe_count=3,
        decisions=tuple(decisions),
        probe_ids=probe_ids,
        inference_applied=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION",
    "SyntheticLinearGreedyDecisionSmokeError",
    "SyntheticLinearDecisionProbe",
    "SyntheticLinearDecision",
    "SyntheticLinearGreedyDecisionDiagnosticResult",
    "run_synthetic_linear_greedy_decision_diagnostic",
]
