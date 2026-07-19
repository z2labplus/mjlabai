"""Gate four-pass protocol claims using reviewed immutable summaries only."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple


MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_PROTOCOL_ROBUSTNESS_GATE_VERSION = (
    "p8_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate_v0.1"
)

_REFERENCE_PROTOCOL_ID = "reference_ordered_0_31_four_pass"
_ALTERNATE_PROTOCOL_ID = "alternate_ordered_116_147_four_pass"
_PRIMARY_WINDOW_ID = "fixed_primary_seeds_52_83"
_REPLICATION_WINDOW_ID = "fixed_replication_seeds_84_115"
_REFERENCE_WINDOW_RAW_REWARD_DELTAS = (15.0, 121.0)
_ALTERNATE_WINDOW_RAW_REWARD_DELTAS = (0.0, 0.0)
_EVIDENCE_GRADE = (
    "P8 local reviewed-summary two-training-protocol robustness gating evidence only"
)
_WARNINGS = (
    "reviewed immutable summary values only",
    "no MahJax, JAX, environment, training or evaluation execution",
    "zero raw-reward delta is not a positive improvement",
    "reference fixed-window improvements do not reproduce under the alternate protocol",
    "two protocols do not establish robustness or generalization",
    "no protocol, model, pass or checkpoint is selected",
    "no threshold, winner score, ranking or candidate promotion",
    "not policy-quality, model-strength, stable-dan or promotion evidence",
    "not Tenhou or LuckyJ 10.68 comparison",
)


@dataclass(frozen=True)
class MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult:
    gate_version: str
    protocol_ids: Tuple[str, str]
    evaluation_window_ids: Tuple[str, str]
    reference_window_raw_reward_deltas: Tuple[float, float]
    alternate_window_raw_reward_deltas: Tuple[float, float]
    reference_window_positive_improvements: Tuple[bool, bool]
    alternate_window_positive_improvements: Tuple[bool, bool]
    per_window_improvement_reproduced: Tuple[bool, bool]
    protocols_agree_on_all_windows: bool
    improvement_reproduced_across_protocols: bool
    robustness_established: bool
    selection_permitted: bool
    selected_training_protocol_id: Optional[str]
    selected_model_id: Optional[str]
    selected_pass_index: Optional[int]
    selected_checkpoint_id: Optional[str]
    training_call_count: int
    evaluation_call_count: int
    evidence_grade: str
    warnings: Tuple[str, ...]


def build_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate(
) -> MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult:
    """Build the no-selection gate without executing either reviewed protocol."""

    reference_positive = tuple(
        value > 0.0 for value in _REFERENCE_WINDOW_RAW_REWARD_DELTAS
    )
    alternate_positive = tuple(
        value > 0.0 for value in _ALTERNATE_WINDOW_RAW_REWARD_DELTAS
    )
    reproduced = tuple(
        reference and alternate
        for reference, alternate in zip(reference_positive, alternate_positive)
    )
    protocols_agree = reference_positive == alternate_positive
    improvement_reproduced = all(reproduced)

    return MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult(
        gate_version=(
            MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_PROTOCOL_ROBUSTNESS_GATE_VERSION
        ),
        protocol_ids=(_REFERENCE_PROTOCOL_ID, _ALTERNATE_PROTOCOL_ID),
        evaluation_window_ids=(_PRIMARY_WINDOW_ID, _REPLICATION_WINDOW_ID),
        reference_window_raw_reward_deltas=_REFERENCE_WINDOW_RAW_REWARD_DELTAS,
        alternate_window_raw_reward_deltas=_ALTERNATE_WINDOW_RAW_REWARD_DELTAS,
        reference_window_positive_improvements=reference_positive,
        alternate_window_positive_improvements=alternate_positive,
        per_window_improvement_reproduced=reproduced,
        protocols_agree_on_all_windows=protocols_agree,
        improvement_reproduced_across_protocols=improvement_reproduced,
        robustness_established=False,
        selection_permitted=False,
        selected_training_protocol_id=None,
        selected_model_id=None,
        selected_pass_index=None,
        selected_checkpoint_id=None,
        training_call_count=0,
        evaluation_call_count=0,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FOUR_PASS_TRAINING_PROTOCOL_ROBUSTNESS_GATE_VERSION",
    "MahJaxCategoricalMlpFourPassTrainingProtocolRobustnessGateResult",
    "build_mahjax_categorical_mlp_four_pass_training_protocol_robustness_gate",
]
