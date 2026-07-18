"""Fixed two-round sequential MahJax raw-outcome training smoke.

The reviewed one-round on-policy collector/update runs for exact seeds 1 then 5
with direct in-memory parameter carry. Fixed bundled rule opponents do not
learn. The result contains diagnostics only and is not strength evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.environment.mahjax_linear_policy_round_smoke import (
    MAHJAX_LINEAR_POLICY_ACTION_COUNT,
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
)
from mjlabai.rl.mahjax_one_round_policy_gradient_smoke import (
    MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE,
    _apply_one_raw_outcome_update,
    _collect_on_policy_round,
    _load_pinned_runtime,
)
from mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke import (
    MahJaxImitationTrainingResult,
    _train_mahjax_rule_policy_imitation_parameters,
)


MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION = (
    "p8_mahjax_two_round_policy_gradient_sequence_smoke_v0.1"
)
MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS = (1, 5)
MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE = 0.1

_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = (
    "P8 local two-round sequential raw-outcome training smoke evidence only"
)
_WARNINGS = (
    "exact two-round sequential on-policy raw-outcome training smoke only",
    "round seeds are fixed in order as 1 then 5",
    "each round has independent environment, rule and project RNG streams",
    "each project trajectory is sampled from legal-masked categorical logits",
    "updated parameters carry directly from round 1 into round 5",
    "exactly two rounds and exactly two gradient updates",
    "returns are only cumulative raw seat-0 rewards divided by 100",
    "no replay, baseline, critic, discount, bootstrapping or reward shaping",
    "fixed bundled rule opponents do not learn",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "no self-play learning, evaluation, league or candidate promotion",
    "not improvement, policy-quality, model-strength, stable-dan or LuckyJ evidence",
)


class MahJaxTwoRoundPolicyGradientSequenceSmokeError(RuntimeError):
    """Raised when the exact two-round sequential contract fails."""


@dataclass(frozen=True)
class MahJaxTwoRoundPolicyGradientSequenceResult:
    """Immutable diagnostics from two sequential raw-outcome updates."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    seeds: Tuple[int, ...]
    learning_rate: float
    round_count: int
    update_count: int
    feature_count: int
    action_count: int
    parameter_count: int
    training_result: MahJaxImitationTrainingResult
    transition_counts: Tuple[int, ...]
    project_decision_counts: Tuple[int, ...]
    project_actions_by_round: Tuple[Tuple[int, ...], ...]
    action_traces: Tuple[Tuple[int, ...], ...]
    legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    cumulative_rewards_by_round: Tuple[Tuple[float, ...], ...]
    final_rewards_by_round: Tuple[Tuple[float, ...], ...]
    final_scores_by_round: Tuple[Tuple[int, ...], ...]
    return_scales: Tuple[float, ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    step_weight_delta_l2: Tuple[float, ...]
    step_bias_delta_l2: Tuple[float, ...]
    final_weight_delta_l2: float
    final_bias_delta_l2: float
    parameter_continuity_verified: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def run_mahjax_two_round_policy_gradient_sequence_smoke(
) -> MahJaxTwoRoundPolicyGradientSequenceResult:
    """Apply exactly two sequential on-policy raw-outcome updates in memory."""

    try:
        _, _, weights, biases, training_result = (
            _train_mahjax_rule_policy_imitation_parameters()
        )
    except Exception as exc:
        raise MahJaxTwoRoundPolicyGradientSequenceSmokeError(
            "reviewed in-memory imitation training failed"
        ) from exc
    initial_weights = weights
    initial_biases = biases
    jax, jnp, mahjax, rule_policy = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxTwoRoundPolicyGradientSequenceSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    transition_counts = []
    decision_counts = []
    project_actions_by_round = []
    action_traces = []
    legal_traces = []
    cumulative_rewards = []
    final_rewards = []
    final_scores = []
    return_scales = []
    initial_objectives = []
    post_objectives = []
    weight_deltas = []
    bias_deltas = []
    for seed in MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS:
        trajectory = _collect_on_policy_round(
            seed,
            weights,
            biases,
            jax,
            jnp,
            mahjax,
            rule_policy,
        )
        update = _apply_one_raw_outcome_update(
            weights,
            biases,
            trajectory,
            jax,
            jnp,
        )
        weights, biases = update.weights, update.biases
        transition_counts.append(len(trajectory.action_trace))
        decision_counts.append(int(trajectory.project_actions.shape[0]))
        project_actions_by_round.append(
            tuple(int(value) for value in trajectory.project_actions.tolist())
        )
        action_traces.append(trajectory.action_trace)
        legal_traces.append(trajectory.legal_action_trace)
        cumulative_rewards.append(trajectory.cumulative_rewards)
        final_rewards.append(trajectory.final_rewards)
        final_scores.append(trajectory.final_scores)
        return_scales.append(update.return_scale)
        initial_objectives.append(update.initial_objective)
        post_objectives.append(update.post_update_objective)
        weight_deltas.append(update.weight_delta_l2)
        bias_deltas.append(update.bias_delta_l2)

    final_weight_delta_l2 = float(jnp.linalg.norm(weights - initial_weights))
    final_bias_delta_l2 = float(jnp.linalg.norm(biases - initial_biases))
    diagnostics = (
        *return_scales,
        *initial_objectives,
        *post_objectives,
        *weight_deltas,
        *bias_deltas,
        final_weight_delta_l2,
        final_bias_delta_l2,
    )
    if not all(math.isfinite(value) for value in diagnostics):
        raise MahJaxTwoRoundPolicyGradientSequenceSmokeError(
            "two-round training diagnostics must all be finite"
        )
    if (
        tuple(transition_counts) != (37, 32)
        or tuple(decision_counts) != (8, 7)
        or tuple(project_actions_by_round)
        != (
            (20, 84, 16, 30, 27, 26, 3, 13),
            (12, 6, 31, 84, 13, 32, 33),
        )
        or tuple(cumulative_rewards)
        != ((-39.0, 39.0, 0.0, 0.0), (-40.0, -40.0, -40.0, 120.0))
        or tuple(final_rewards)
        != ((-39.0, 39.0, 0.0, 0.0), (-40.0, -40.0, -40.0, 130.0))
        or tuple(final_scores)
        != ((211, 289, 250, 250), (210, 210, 210, 370))
        or any(
            abs(actual - expected) > 1e-5
            for actual, expected in zip(
                (
                    *return_scales,
                    *initial_objectives,
                    *post_objectives,
                    *weight_deltas,
                    *bias_deltas,
                ),
                (
                    -0.39,
                    -0.4,
                    -0.86367577,
                    -0.85308564,
                    -0.88331068,
                    -0.87257367,
                    0.04220101,
                    0.04183802,
                    0.01279154,
                    0.01353321,
                ),
            )
        )
        or final_weight_delta_l2 <= 0.0
        or final_bias_delta_l2 <= 0.0
    ):
        raise MahJaxTwoRoundPolicyGradientSequenceSmokeError(
            "two-round diagnostics differ from the reviewed probe"
        )

    return MahJaxTwoRoundPolicyGradientSequenceResult(
        smoke_version=MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seeds=MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS,
        learning_rate=MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE,
        round_count=2,
        update_count=2,
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        training_result=training_result,
        transition_counts=tuple(transition_counts),
        project_decision_counts=tuple(decision_counts),
        project_actions_by_round=tuple(project_actions_by_round),
        action_traces=tuple(action_traces),
        legal_action_traces=tuple(legal_traces),
        cumulative_rewards_by_round=tuple(cumulative_rewards),
        final_rewards_by_round=tuple(final_rewards),
        final_scores_by_round=tuple(final_scores),
        return_scales=tuple(return_scales),
        initial_objectives=tuple(initial_objectives),
        post_update_objectives=tuple(post_objectives),
        step_weight_delta_l2=tuple(weight_deltas),
        step_bias_delta_l2=tuple(bias_deltas),
        final_weight_delta_l2=final_weight_delta_l2,
        final_bias_delta_l2=final_bias_delta_l2,
        parameter_continuity_verified=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION",
    "MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS",
    "MAHJAX_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE",
    "MahJaxTwoRoundPolicyGradientSequenceSmokeError",
    "MahJaxTwoRoundPolicyGradientSequenceResult",
    "run_mahjax_two_round_policy_gradient_sequence_smoke",
]
