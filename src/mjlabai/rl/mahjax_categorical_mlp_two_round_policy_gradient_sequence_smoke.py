"""Two sequential shared-policy all-project MahJax raw-outcome updates.

Exact local seeds one and three run in order. Each terminal all-project round
drives one actor-indexed update, and round-one arrays feed round two directly.
This is not production self-play, evaluation, improvement, or strength evidence.
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
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE,
    _apply_actor_indexed_raw_outcome_update,
    _collect_all_project_round,
    _load_pinned_runtime,
    _seat_decision_counts,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MahJaxCategoricalMlpImitationResult,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS = (1, 3)
MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE = (
    MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE
)

_FRESH_SEED3_INITIAL_OBJECTIVE = -0.0553399548
_EXPECTED_TRANSITION_COUNTS = (77, 84)
_EXPECTED_SEAT_COUNTS = ((21, 22, 17, 17), (23, 22, 19, 20))
_EXPECTED_CUMULATIVE_REWARDS = (
    (-20.0, 70.0, -20.0, -30.0),
    (-10.0, -10.0, 20.0, -10.0),
)
_EXPECTED_FINAL_REWARDS = (
    (-20.0, 80.0, -20.0, -20.0),
    (-10.0, -10.0, 30.0, -10.0),
)
_EXPECTED_FINAL_SCORES = ((230, 320, 230, 220), (240, 240, 270, 240))
_EXPECTED_ACTION_PREFIXES = (
    (28, 27, 28, 28, 29, 33, 27, 31, 27, 0, 31, 32),
    (29, 28, 29, 27, 71, 84, 27, 31, 8, 71, 30, 33),
)
_EXPECTED_INITIAL_OBJECTIVES = (0.0936663598, -0.0553588867)
_EXPECTED_POST_OBJECTIVES = (0.0930117071, -0.0554395691)
_EXPECTED_STEP_DELTAS = (
    (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356),
    (0.0002636357, 0.0000601950, 0.0008506179, 0.0000944084),
)
_EXPECTED_FINAL_DELTAS = (
    0.0010158311,
    0.0001864599,
    0.0025688238,
    0.0002769242,
)
_EVIDENCE_GRADE = (
    "P8 local two-round sequential shared all-project-seat raw-outcome training "
    "smoke evidence only"
)
_WARNINGS = (
    "two-round sequential shared all-project-seat training smoke only",
    "exact ordered seeds 1 then 3 and exactly two 0.01 updates",
    "all four seats share one reviewed categorical MLP in both rounds",
    "round-1 updated arrays feed round 2 directly without reinitialization",
    "each round uses separate deterministic environment and action RNG streams",
    "every sampled action is checked against its environment legal mask",
    "each action uses only its acting seat cumulative raw reward divided by 100",
    "no baseline, critic, discount, bootstrapping, entropy, replay or shaping",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "no third round, production self-play, evaluation, league or promotion",
    "no real Tenhou, real haifu, external log or platform data",
    "not improvement, policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(RuntimeError):
    """Raised when the exact two-round sequence contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult:
    """Immutable diagnostics from two directly chained shared updates."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    seeds: Tuple[int, ...]
    round_count: int
    update_count: int
    learning_rate: float
    training_result: MahJaxCategoricalMlpImitationResult
    transition_counts: Tuple[int, ...]
    seat_decision_counts: Tuple[Tuple[int, ...], ...]
    actor_traces: Tuple[Tuple[int, ...], ...]
    action_traces: Tuple[Tuple[int, ...], ...]
    legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    final_raw_rewards: Tuple[Tuple[float, ...], ...]
    final_scores: Tuple[Tuple[int, ...], ...]
    seat_return_scales: Tuple[Tuple[float, ...], ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_update_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    fresh_seed3_initial_objective: float
    carried_seed3_initial_objective: float
    final_parameter_delta_l2: Tuple[float, ...]
    post_round2_transition_count: int
    post_round2_actor_trace: Tuple[int, ...]
    post_round2_action_trace: Tuple[int, ...]
    post_round2_legal_action_trace: Tuple[Tuple[int, ...], ...]
    post_round2_cumulative_raw_rewards: Tuple[float, ...]
    post_round2_final_raw_rewards: Tuple[float, ...]
    post_round2_final_scores: Tuple[int, ...]
    parameter_continuity_proven: bool
    all_actions_legal: bool
    all_rounds_terminated: bool
    post_round2_replay_identical: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke(
) -> MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult:
    """Apply exactly two actor-indexed updates with direct parameter carry."""

    try:
        jax, jnp, parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "reviewed categorical MLP in-memory training failed"
        ) from exc
    try:
        _, _, mahjax = _load_pinned_runtime()
    except Exception as exc:
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "pinned MahJax/JAX two-round runtime is unavailable"
        ) from exc
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    initial_parameters = parameters
    trajectories = []
    updates = []
    for seed in MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS:
        try:
            trajectory = _collect_all_project_round(
                seed,
                parameters,
                jax,
                jnp,
                mahjax,
            )
            update = _apply_actor_indexed_raw_outcome_update(
                parameters,
                trajectory,
                jax,
                jnp,
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
                f"all-project sequence round seed {seed} failed"
            ) from exc
        trajectories.append(trajectory)
        updates.append(update)
        parameters = update.parameters

    transition_counts = tuple(len(item.action_trace) for item in trajectories)
    seat_counts = tuple(
        _seat_decision_counts(item.actor_trace) for item in trajectories
    )
    cumulative_rewards = tuple(item.cumulative_rewards for item in trajectories)
    final_rewards = tuple(item.final_rewards for item in trajectories)
    final_scores = tuple(item.final_scores for item in trajectories)
    initial_objectives = tuple(item.initial_objective for item in updates)
    post_objectives = tuple(item.post_update_objective for item in updates)
    step_deltas = tuple(item.parameter_delta_l2 for item in updates)
    if (
        transition_counts != _EXPECTED_TRANSITION_COUNTS
        or seat_counts != _EXPECTED_SEAT_COUNTS
        or cumulative_rewards != _EXPECTED_CUMULATIVE_REWARDS
        or final_rewards != _EXPECTED_FINAL_REWARDS
        or final_scores != _EXPECTED_FINAL_SCORES
        or any(
            trajectory.action_trace[:12] != expected
            for trajectory, expected in zip(
                trajectories,
                _EXPECTED_ACTION_PREFIXES,
            )
        )
        or any(
            not _close(actual, expected)
            for actual, expected in zip(
                initial_objectives,
                _EXPECTED_INITIAL_OBJECTIVES,
            )
        )
        or any(
            not _close(actual, expected)
            for actual, expected in zip(
                post_objectives,
                _EXPECTED_POST_OBJECTIVES,
            )
        )
        or any(
            not _close(actual, expected)
            for actual_row, expected_row in zip(step_deltas, _EXPECTED_STEP_DELTAS)
            for actual, expected in zip(actual_row, expected_row)
        )
        or any(post >= initial for initial, post in zip(initial_objectives, post_objectives))
    ):
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "two-round diagnostics differ from the reviewed probe"
        )

    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if any(
        not _close(actual, expected) or actual <= 0.0
        for actual, expected in zip(final_deltas, _EXPECTED_FINAL_DELTAS)
    ):
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "two-round final parameter deltas differ from the reviewed probe"
        )

    carried_seed3_initial_objective = initial_objectives[1]
    parameter_continuity_proven = (
        abs(carried_seed3_initial_objective - _FRESH_SEED3_INITIAL_OBJECTIVE)
        > 1e-6
        and all(value > 0.0 for value in step_deltas[0])
        and all(value > 0.0 for value in final_deltas)
    )
    if not parameter_continuity_proven:
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "round-2 direct parameter continuity was not demonstrated"
        )

    try:
        post_round2 = _collect_all_project_round(
            MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS[1],
            parameters,
            jax,
            jnp,
            mahjax,
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "post-update round-2 replay failed"
        ) from exc
    round2 = trajectories[1]
    post_round2_identical = (
        post_round2.actor_trace == round2.actor_trace
        and post_round2.action_trace == round2.action_trace
        and post_round2.legal_action_trace == round2.legal_action_trace
        and post_round2.cumulative_rewards == round2.cumulative_rewards
        and post_round2.final_rewards == round2.final_rewards
        and post_round2.final_scores == round2.final_scores
    )
    if not post_round2_identical:
        raise MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError(
            "post-update round-2 replay differs from the reviewed probe"
        )

    return MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        seeds=MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS,
        round_count=2,
        update_count=2,
        learning_rate=(
            MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE
        ),
        training_result=training_result,
        transition_counts=transition_counts,
        seat_decision_counts=seat_counts,
        actor_traces=tuple(item.actor_trace for item in trajectories),
        action_traces=tuple(item.action_trace for item in trajectories),
        legal_action_traces=tuple(item.legal_action_trace for item in trajectories),
        cumulative_raw_rewards=cumulative_rewards,
        final_raw_rewards=final_rewards,
        final_scores=final_scores,
        seat_return_scales=tuple(item.seat_return_scales for item in updates),
        initial_objectives=initial_objectives,
        post_update_objectives=post_objectives,
        per_update_parameter_delta_l2=step_deltas,
        fresh_seed3_initial_objective=_FRESH_SEED3_INITIAL_OBJECTIVE,
        carried_seed3_initial_objective=carried_seed3_initial_objective,
        final_parameter_delta_l2=final_deltas,
        post_round2_transition_count=len(post_round2.action_trace),
        post_round2_actor_trace=post_round2.actor_trace,
        post_round2_action_trace=post_round2.action_trace,
        post_round2_legal_action_trace=post_round2.legal_action_trace,
        post_round2_cumulative_raw_rewards=post_round2.cumulative_rewards,
        post_round2_final_raw_rewards=post_round2.final_rewards,
        post_round2_final_scores=post_round2.final_scores,
        parameter_continuity_proven=parameter_continuity_proven,
        all_actions_legal=True,
        all_rounds_terminated=True,
        post_round2_replay_identical=post_round2_identical,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_TWO_ROUND_POLICY_GRADIENT_SEQUENCE_LEARNING_RATE",
    "MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceSmokeError",
    "MahJaxCategoricalMlpTwoRoundPolicyGradientSequenceResult",
    "run_mahjax_categorical_mlp_two_round_policy_gradient_sequence_smoke",
]
