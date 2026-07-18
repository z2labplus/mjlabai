"""Project-owned masked linear-policy round over public MahJax observations.

The module encodes only the decision-time public observation and runs one
randomly initialized, immutable linear 87-action policy through one local
round. It does not train parameters, read data, persist artifacts, or provide
model-strength evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)


MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION = (
    "p4_p8_mahjax_linear_policy_round_smoke_v0.1"
)
MAHJAX_LINEAR_POLICY_TRANSITION_CAP = 256
MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT = 630
MAHJAX_LINEAR_POLICY_ACTION_COUNT = 87

_EXPECTED_OBSERVATION_SHAPES = {
    "hand": (14,),
    "last_draw": (),
    "action_history": (3, 200),
    "shanten_count": (),
    "furiten": (),
    "scores": (4,),
    "round": (),
    "honba": (),
    "kyotaku": (),
    "prevalent_wind": (),
    "seat_wind": (),
    "dora_indicators": (4,),
}
_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = (
    "P4/P8 project-owned untrained model-output-to-environment smoke evidence only"
)
_WARNINGS = (
    "project-owned random-initialized linear-policy local round only",
    "exact 630 public observation features and 87 action scores",
    "current-player-relative public scores are input features only",
    "environment legal mask is authoritative for action selection",
    "parameters are untrained, immutable and not checkpointed",
    "no hidden opponent hand or private environment-state feature",
    "no labels, dataset, loss, gradient, optimizer or training",
    "no real Tenhou, real haifu, external log or platform data",
    "not production self-play, league or evaluation",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
    "not candidate-promotion evidence",
)


class MahJaxLinearPolicyRoundSmokeError(RuntimeError):
    """Raised when the public-observation linear-policy contract fails."""


@dataclass(frozen=True)
class MahJaxLinearPolicyStep:
    """Immutable model-output and environment-legality diagnostic."""

    pre_step_index: int
    acting_player: int
    legal_actions: Tuple[int, ...]
    selected_action: int
    selected_action_score: float


@dataclass(frozen=True)
class MahJaxLinearPolicyRoundResult:
    """Immutable diagnostics from one untrained linear-policy round."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    model_id: str
    seed: int
    feature_count: int
    action_count: int
    parameter_count: int
    transition_cap: int
    transition_count: int
    initial_player: int
    final_player: int
    final_step_count: int
    trace: Tuple[MahJaxLinearPolicyStep, ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    final_scores: Tuple[int, ...]
    terminated: bool
    truncated: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _load_pinned_runtime():
    try:
        import jax
        import jax.numpy as jnp
        import mahjax
    except Exception as exc:
        raise MahJaxLinearPolicyRoundSmokeError(
            "pinned MahJax/JAX linear-policy runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax


def _encode_observation_array(observation: object, jnp):
    if type(observation) is not dict:
        raise MahJaxLinearPolicyRoundSmokeError(
            "MahJax public observation must be an exact dict"
        )
    if set(observation) != set(_EXPECTED_OBSERVATION_SHAPES):
        raise MahJaxLinearPolicyRoundSmokeError(
            "MahJax public observation keys differ from the pinned contract"
        )
    actual_shapes = {
        key: tuple(getattr(observation[key], "shape", ()))
        for key in _EXPECTED_OBSERVATION_SHAPES
    }
    if actual_shapes != _EXPECTED_OBSERVATION_SHAPES:
        raise MahJaxLinearPolicyRoundSmokeError(
            "MahJax public observation shapes differ from the pinned contract"
        )

    parts = (
        jnp.asarray(observation["hand"], dtype=jnp.float32) / 36.0,
        jnp.asarray([observation["last_draw"]], dtype=jnp.float32) / 36.0,
        jnp.ravel(jnp.asarray(observation["action_history"], dtype=jnp.float32))
        / 86.0,
        jnp.asarray([observation["shanten_count"]], dtype=jnp.float32) / 6.0,
        jnp.asarray([observation["furiten"]], dtype=jnp.float32),
        jnp.asarray(observation["scores"], dtype=jnp.float32) / 1000.0,
        jnp.asarray([observation["round"]], dtype=jnp.float32) / 12.0,
        jnp.asarray([observation["honba"]], dtype=jnp.float32) / 10.0,
        jnp.asarray([observation["kyotaku"]], dtype=jnp.float32) / 10.0,
        jnp.asarray([observation["prevalent_wind"]], dtype=jnp.float32) / 3.0,
        jnp.asarray([observation["seat_wind"]], dtype=jnp.float32) / 3.0,
        jnp.asarray(observation["dora_indicators"], dtype=jnp.float32) / 36.0,
    )
    features = jnp.concatenate(parts)
    if tuple(features.shape) != (MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,):
        raise MahJaxLinearPolicyRoundSmokeError(
            "encoded public observation must contain exactly 630 features"
        )
    if not bool(jnp.all(jnp.isfinite(features))):
        raise MahJaxLinearPolicyRoundSmokeError(
            "encoded public observation features must all be finite"
        )
    return features


def encode_mahjax_public_observation(
    observation: Mapping[str, object],
) -> Tuple[float, ...]:
    """Return one immutable 630-feature decision-time public observation."""

    _, jnp, _ = _load_pinned_runtime()
    features = _encode_observation_array(observation, jnp)
    return tuple(float(value) for value in features)


def _legal_actions(value: object) -> Tuple[int, ...]:
    if str(getattr(value, "dtype", "")) != "bool":
        raise MahJaxLinearPolicyRoundSmokeError(
            "state.legal_action_mask must have bool dtype"
        )
    try:
        mask = tuple(bool(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxLinearPolicyRoundSmokeError(
            "state.legal_action_mask must be an iterable boolean mask"
        ) from exc
    if len(mask) != MAHJAX_LINEAR_POLICY_ACTION_COUNT:
        raise MahJaxLinearPolicyRoundSmokeError(
            "state.legal_action_mask must contain exactly 87 actions"
        )
    actions = tuple(index for index, is_legal in enumerate(mask) if is_legal)
    if not actions:
        raise MahJaxLinearPolicyRoundSmokeError(
            "nonterminal state must expose at least one legal action"
        )
    return actions


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxLinearPolicyRoundSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxLinearPolicyRoundSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def run_mahjax_linear_policy_round_smoke(
    seed: int = 0,
) -> MahJaxLinearPolicyRoundResult:
    """Run one project-owned random linear policy through a local MahJax round."""

    if type(seed) is not int or seed < 0 or seed > 0xFFFFFFFF:
        raise MahJaxLinearPolicyRoundSmokeError(
            "seed must be an exact int from 0 through 4294967295"
        )

    jax, jnp, mahjax = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxLinearPolicyRoundSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )
    try:
        root_key = jax.random.PRNGKey(seed)
        init_key, model_key = jax.random.split(root_key)
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
        weights = jax.random.normal(
            model_key,
            (
                MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
                MAHJAX_LINEAR_POLICY_ACTION_COUNT,
            ),
            dtype=jnp.float32,
        ) * 0.01
        biases = jnp.zeros((MAHJAX_LINEAR_POLICY_ACTION_COUNT,), dtype=jnp.float32)
    except Exception as exc:
        raise MahJaxLinearPolicyRoundSmokeError(
            "failed to initialize MahJax and the project-owned linear policy"
        ) from exc

    if environment.id != _MAHJAX_ENVIRONMENT_ID:
        raise MahJaxLinearPolicyRoundSmokeError("unexpected MahJax environment id")
    if environment.version != _MAHJAX_ENVIRONMENT_VERSION:
        raise MahJaxLinearPolicyRoundSmokeError(
            "unexpected MahJax environment version"
        )
    if environment.num_players != 4 or environment.num_actions != 87:
        raise MahJaxLinearPolicyRoundSmokeError(
            "MahJax environment must expose four players and 87 actions"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxLinearPolicyRoundSmokeError(
            "initial MahJax state must be nonterminal and nontruncated"
        )

    initial_player = int(state.current_player)
    trace = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    score_fn = jax.jit(lambda features: features @ weights + biases)

    for transition_index in range(MAHJAX_LINEAR_POLICY_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxLinearPolicyRoundSmokeError(
                "rollout attempted a model decision from a finished state"
            )
        pre_step_index = int(state.step_count)
        if pre_step_index != transition_index:
            raise MahJaxLinearPolicyRoundSmokeError(
                "MahJax step_count must match the deterministic transition index"
            )
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            observation = environment.observe(state)
            features = _encode_observation_array(observation, jnp)
            scores = jax.block_until_ready(score_fn(features))
        except MahJaxLinearPolicyRoundSmokeError:
            raise
        except Exception as exc:
            raise MahJaxLinearPolicyRoundSmokeError(
                f"linear policy scoring failed at transition {transition_index}"
            ) from exc
        if tuple(scores.shape) != (MAHJAX_LINEAR_POLICY_ACTION_COUNT,):
            raise MahJaxLinearPolicyRoundSmokeError(
                "linear policy must return exactly 87 action scores"
            )
        if not bool(jnp.all(jnp.isfinite(scores))):
            raise MahJaxLinearPolicyRoundSmokeError(
                "linear policy action scores must all be finite"
            )
        masked_scores = jnp.where(state.legal_action_mask, scores, -jnp.inf)
        selected_action = int(jnp.argmax(masked_scores))
        if selected_action not in legal_actions:
            raise MahJaxLinearPolicyRoundSmokeError(
                f"masked linear policy selected illegal action {selected_action}"
            )
        trace.append(
            MahJaxLinearPolicyStep(
                pre_step_index=pre_step_index,
                acting_player=int(state.current_player),
                legal_actions=legal_actions,
                selected_action=selected_action,
                selected_action_score=float(scores[selected_action]),
            )
        )
        try:
            state = step_fn(state, jnp.int32(selected_action))
            state = jax.block_until_ready(state)
        except Exception as exc:
            raise MahJaxLinearPolicyRoundSmokeError(
                f"failed to execute MahJax transition {transition_index}"
            ) from exc
        if int(state.step_count) != pre_step_index + 1:
            raise MahJaxLinearPolicyRoundSmokeError(
                "MahJax transition must increment step_count exactly once"
            )
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxLinearPolicyRoundSmokeError(
            "MahJax linear-policy round exceeded the "
            f"{MAHJAX_LINEAR_POLICY_TRANSITION_CAP}-transition cap"
        )

    terminated = bool(state.terminated)
    truncated = bool(state.truncated)
    if seed == 0 and (not terminated or truncated):
        raise MahJaxLinearPolicyRoundSmokeError(
            "seed 0 must terminate without truncation before the transition cap"
        )
    try:
        final_scores = tuple(int(value) for value in state.round_state.score)
    except Exception as exc:
        raise MahJaxLinearPolicyRoundSmokeError(
            "failed to read final global seat-ordered MahJax scores"
        ) from exc
    if len(final_scores) != 4:
        raise MahJaxLinearPolicyRoundSmokeError(
            "final global seat-ordered scores must contain exactly four values"
        )

    return MahJaxLinearPolicyRoundResult(
        smoke_version=MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        model_id="project_random_linear_630x87_jax_normal_scale_0.01",
        seed=seed,
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        transition_cap=MAHJAX_LINEAR_POLICY_TRANSITION_CAP,
        transition_count=len(trace),
        initial_player=initial_player,
        final_player=int(state.current_player),
        final_step_count=int(state.step_count),
        trace=tuple(trace),
        final_rewards=_four_floats(state.rewards, "state.rewards"),
        cumulative_rewards=cumulative_rewards,
        final_scores=final_scores,
        terminated=terminated,
        truncated=truncated,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION",
    "MAHJAX_LINEAR_POLICY_TRANSITION_CAP",
    "MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT",
    "MAHJAX_LINEAR_POLICY_ACTION_COUNT",
    "MahJaxLinearPolicyRoundSmokeError",
    "MahJaxLinearPolicyStep",
    "MahJaxLinearPolicyRoundResult",
    "encode_mahjax_public_observation",
    "run_mahjax_linear_policy_round_smoke",
]
