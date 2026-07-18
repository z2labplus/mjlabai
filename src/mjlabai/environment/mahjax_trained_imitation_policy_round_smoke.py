"""Held-out MahJax round before and after the reviewed imitation training.

The same seed-2 local environment is driven once by initial parameters and
once by the trained in-memory parameters. Every score vector is masked by the
environment-owned legal actions. Parameters and trajectories are never saved,
and changed behavior is not policy-quality or model-strength evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.environment.mahjax_linear_policy_round_smoke import (
    MAHJAX_LINEAR_POLICY_ACTION_COUNT,
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
    encode_mahjax_public_observation,
)
from mjlabai.supervised.mahjax_rule_policy_imitation_training_smoke import (
    MahJaxImitationTrainingResult,
    _train_mahjax_rule_policy_imitation_parameters,
)


MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION = (
    "p7_p8_mahjax_trained_imitation_policy_round_smoke_v0.1"
)
MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED = 2

_TRANSITION_CAP = 256
_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = (
    "P7/P8 local trained-imitation-policy held-out environment smoke evidence only"
)
_WARNINGS = (
    "reviewed in-memory imitation parameters on one held-out MahJax seed only",
    "seed 2 is distinct from seed 0 training and seed 1 label evaluation",
    "initial and trained policies receive identical local environment seeds",
    "environment legal mask remains authoritative before every action",
    "changed action trajectory is behavior smoke only, not improvement evidence",
    "no persisted data, parameters, model weights, checkpoint or artifact",
    "no hidden opponent hand or private environment-state feature",
    "no reward objective, reinforcement-learning update or self-play learning",
    "no real Tenhou, real haifu, external log or platform data",
    "not production training, evaluation, league or candidate promotion",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxTrainedImitationPolicyRoundSmokeError(RuntimeError):
    """Raised when the held-out trained-policy round contract fails."""


@dataclass(frozen=True)
class _ParameterRoundDiagnostics:
    actions: Tuple[int, ...]
    legal_actions: Tuple[Tuple[int, ...], ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    terminated: bool
    truncated: bool


@dataclass(frozen=True)
class MahJaxTrainedImitationPolicyRoundResult:
    """Immutable initial/trained held-out-round diagnostics."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    initial_model_id: str
    trained_model_id: str
    rollout_seed: int
    feature_count: int
    action_count: int
    parameter_count: int
    transition_cap: int
    training_result: MahJaxImitationTrainingResult
    initial_transition_count: int
    trained_transition_count: int
    initial_actions: Tuple[int, ...]
    trained_actions: Tuple[int, ...]
    initial_legal_actions: Tuple[Tuple[int, ...], ...]
    trained_legal_actions: Tuple[Tuple[int, ...], ...]
    initial_final_rewards: Tuple[float, ...]
    trained_final_rewards: Tuple[float, ...]
    initial_cumulative_rewards: Tuple[float, ...]
    trained_cumulative_rewards: Tuple[float, ...]
    initial_final_scores: Tuple[int, ...]
    trained_final_scores: Tuple[int, ...]
    initial_terminated: bool
    trained_terminated: bool
    initial_truncated: bool
    trained_truncated: bool
    trajectory_changed: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _load_pinned_runtime():
    try:
        import jax
        import jax.numpy as jnp
        import mahjax
    except Exception as exc:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "pinned MahJax/JAX held-out policy runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def _legal_actions(mask: object) -> Tuple[int, ...]:
    if str(getattr(mask, "dtype", "")) != "bool":
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        values = tuple(bool(value) for value in mask)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(values) != MAHJAX_LINEAR_POLICY_ACTION_COUNT:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "state.legal_action_mask must contain exactly 87 actions"
        )
    actions = tuple(index for index, is_legal in enumerate(values) if is_legal)
    if not actions:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def _run_parameter_round(seed, weights, biases, jax, jnp, mahjax):
    try:
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(jax.random.PRNGKey(seed))
    except Exception as exc:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "failed to initialize held-out MahJax environment"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != MAHJAX_LINEAR_POLICY_ACTION_COUNT
    ):
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "held-out MahJax environment differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "held-out MahJax initial state must be active"
        )

    actions = []
    legal_history = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    score_fn = jax.jit(lambda features: features @ weights + biases)
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxTrainedImitationPolicyRoundSmokeError(
                "held-out rollout attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxTrainedImitationPolicyRoundSmokeError(
                "held-out rollout step_count must be monotonic"
            )
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            features = jnp.asarray(
                encode_mahjax_public_observation(environment.observe(state)),
                dtype=jnp.float32,
            )
            scores = jax.block_until_ready(score_fn(features))
        except Exception as exc:
            raise MahJaxTrainedImitationPolicyRoundSmokeError(
                f"policy scoring failed at transition {transition_index}"
            ) from exc
        if tuple(scores.shape) != (MAHJAX_LINEAR_POLICY_ACTION_COUNT,) or not bool(
            jnp.all(jnp.isfinite(scores))
        ):
            raise MahJaxTrainedImitationPolicyRoundSmokeError(
                "policy must produce exactly 87 finite action scores"
            )
        selected_action = int(
            jnp.argmax(jnp.where(state.legal_action_mask, scores, -jnp.inf))
        )
        if selected_action not in legal_actions:
            raise MahJaxTrainedImitationPolicyRoundSmokeError(
                f"masked policy selected illegal action {selected_action}"
            )
        actions.append(selected_action)
        legal_history.append(legal_actions)
        try:
            state = jax.block_until_ready(
                step_fn(state, jnp.int32(selected_action))
            )
        except Exception as exc:
            raise MahJaxTrainedImitationPolicyRoundSmokeError(
                f"held-out environment step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            f"held-out rollout exceeded the {_TRANSITION_CAP}-transition cap"
        )

    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "held-out rollout must terminate without truncation"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "failed to read global seat-ordered scores"
        ) from exc
    if len(final_scores) != 4:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "global seat-ordered scores must contain four values"
        )
    return _ParameterRoundDiagnostics(
        actions=tuple(actions),
        legal_actions=tuple(legal_history),
        final_rewards=_four_floats(state.rewards, "state.rewards"),
        cumulative_rewards=cumulative_rewards,
        final_scores=final_scores,
        terminated=True,
        truncated=False,
    )


def run_mahjax_trained_imitation_policy_round_smoke(
) -> MahJaxTrainedImitationPolicyRoundResult:
    """Train in memory, then compare initial/trained policies on seed 2."""

    try:
        (
            initial_weights,
            initial_biases,
            trained_weights,
            trained_biases,
            training_result,
        ) = _train_mahjax_rule_policy_imitation_parameters()
    except Exception as exc:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "reviewed in-memory imitation training failed"
        ) from exc
    jax, jnp, mahjax = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )
    initial = _run_parameter_round(
        MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED,
        initial_weights,
        initial_biases,
        jax,
        jnp,
        mahjax,
    )
    trained = _run_parameter_round(
        MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED,
        trained_weights,
        trained_biases,
        jax,
        jnp,
        mahjax,
    )
    trajectory_changed = initial.actions != trained.actions
    if (
        len(initial.actions) != 88
        or len(trained.actions) != 94
        or initial.actions[0] != 12
        or trained.actions[0] != 71
        or not trajectory_changed
        or initial.final_scores != (250, 250, 250, 250)
        or trained.final_scores != (250, 250, 250, 250)
    ):
        raise MahJaxTrainedImitationPolicyRoundSmokeError(
            "held-out seed-2 acceptance diagnostics differ from the reviewed probe"
        )

    return MahJaxTrainedImitationPolicyRoundResult(
        smoke_version=MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        initial_model_id="project_linear_630x87_initial_seed_123",
        trained_model_id="project_linear_630x87_imitation_seed_123_epoch_16",
        rollout_seed=MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED,
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        transition_cap=_TRANSITION_CAP,
        training_result=training_result,
        initial_transition_count=len(initial.actions),
        trained_transition_count=len(trained.actions),
        initial_actions=initial.actions,
        trained_actions=trained.actions,
        initial_legal_actions=initial.legal_actions,
        trained_legal_actions=trained.legal_actions,
        initial_final_rewards=initial.final_rewards,
        trained_final_rewards=trained.final_rewards,
        initial_cumulative_rewards=initial.cumulative_rewards,
        trained_cumulative_rewards=trained.cumulative_rewards,
        initial_final_scores=initial.final_scores,
        trained_final_scores=trained.final_scores,
        initial_terminated=initial.terminated,
        trained_terminated=trained.terminated,
        initial_truncated=initial.truncated,
        trained_truncated=trained.truncated,
        trajectory_changed=trajectory_changed,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION",
    "MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED",
    "MahJaxTrainedImitationPolicyRoundSmokeError",
    "MahJaxTrainedImitationPolicyRoundResult",
    "run_mahjax_trained_imitation_policy_round_smoke",
]
