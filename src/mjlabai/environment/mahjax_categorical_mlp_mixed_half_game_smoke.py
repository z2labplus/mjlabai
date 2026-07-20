"""Read-only categorical-MLP versus rule-policy MahJax half-game smoke."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.environment.mahjax_rule_based_half_game_smoke import (
    MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
    MahJaxRuleBasedHalfGameRoundBoundary,
    _four_ints,
)
from mjlabai.environment.mahjax_rule_based_single_round_smoke import (
    _four_floats,
    _legal_actions,
    _load_pinned_runtime,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
    MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
    _encode_observation_array,
    _mlp_logits,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_SMOKE_VERSION = (
    "p4_p7_p8_mahjax_categorical_mlp_mixed_half_game_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT = 0

_ACTION_COUNT = 87
_PON_ACTION = 75
_PON_RED_ACTION = 76
_EXPECTED_BOUNDARIES = (
    (121, 0, 1, (250, 285, 345, 120)),
    (158, 1, 2, (198, 337, 345, 120)),
    (228, 2, 3, (188, 332, 340, 140)),
    (304, 3, 4, (188, 332, 263, 217)),
    (477, 4, 5, (162, 296, 257, 285)),
    (557, 5, 6, (85, 373, 257, 285)),
    (600, 6, 7, (85, 363, 231, 321)),
    (769, 7, 8, (90, 275, 329, 306)),
)
_EXPECTED_FINAL_SCORES = (40, 265, 379, 316)
_EXPECTED_FINAL_REWARDS = (-20.0, 0.0, 30.0, 0.0)
_EXPECTED_CUMULATIVE_REWARDS = (-200.0, 15.0, 12.0, 123.0)
_EXPECTED_NORMALIZATION = (450, 3, 75, 76)

_PROJECT_POLICY_ID = (
    "mjlabai.categorical_mlp_imitation_greedy@"
    + MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION
)
_RULE_POLICY_ID = "mahjax.red_mahjong.players.rule_based_player@0.1.2"
_EVIDENCE_GRADE = (
    "P4/P7/P8 pinned local read-only categorical-MLP mixed half-game smoke evidence"
)
_WARNINGS = (
    "one pinned local seed-0 categorical-MLP mixed half-game smoke only",
    "project greedy legal-masked policy drives seat 0 without half-game updates",
    "bundled MahJax rule policy drives seats 1 through 3",
    "only raw PON 75 to legal PON_RED 76 normalization is permitted",
    "every raw and applied action plus normalization is recorded",
    "complete transition and round-boundary provenance is retained",
    "no saved parameters, weights, checkpoint, dataset or artifact",
    "no real Tenhou, real haifu, external log or platform data",
    "not production self-play, evaluation, league or candidate promotion",
    "not improvement, policy-quality or model-strength evidence",
    "not stable-dan, LuckyJ 10.68 or P9-P12 evidence",
)


class MahJaxCategoricalMlpMixedHalfGameSmokeError(RuntimeError):
    """Raised when the exact read-only mixed half-game contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpMixedHalfGameStep:
    """One immutable mixed-policy half-game transition."""

    transition_index: int
    round_index: int
    round_step_index: int
    acting_player: int
    policy_id: str
    legal_actions: Tuple[int, ...]
    raw_action: int
    applied_action: int
    red_pon_normalized: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpMixedHalfGameResult:
    """Frozen read-only project/rule half-game diagnostics."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    imitation_smoke_version: str
    project_policy_id: str
    rule_policy_id: str
    feature_count: int
    action_count: int
    project_seat: int
    seed: int
    transition_cap: int
    transition_count: int
    project_decision_count: int
    rule_decision_count: int
    red_pon_normalization_count: int
    round_boundaries: Tuple[MahJaxRuleBasedHalfGameRoundBoundary, ...]
    trace: Tuple[MahJaxCategoricalMlpMixedHalfGameStep, ...]
    final_round_index: int
    final_scores: Tuple[int, ...]
    final_rewards: Tuple[float, ...]
    cumulative_rewards: Tuple[float, ...]
    terminated: bool
    truncated: bool
    half_game_update_count: int
    selected_model_id: None
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _normalize_rule_action(
    raw_action: int,
    legal_actions: Tuple[int, ...],
) -> Tuple[int, bool]:
    if raw_action in legal_actions:
        return raw_action, False
    if (
        raw_action == _PON_ACTION
        and _PON_ACTION not in legal_actions
        and _PON_RED_ACTION in legal_actions
    ):
        return _PON_RED_ACTION, True
    raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
        f"bundled rule policy selected unsupported illegal action {raw_action}"
    )


def run_mahjax_categorical_mlp_mixed_half_game_smoke(
    seed: int = 0,
) -> MahJaxCategoricalMlpMixedHalfGameResult:
    """Run one read-only project-seat-0 versus rule-seat half-game."""

    if type(seed) is not int or seed < 0 or seed > 0xFFFFFFFF:
        raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
            "seed must be an exact int from 0 through 4294967295"
        )

    try:
        jax, jnp, parameters, _ = _train_mahjax_categorical_mlp_parameters()
        _, _, mahjax, rule_based_player = _load_pinned_runtime()
        root_key = jax.random.PRNGKey(seed)
        init_key, rule_key = jax.random.split(root_key)
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="half",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
            "failed to initialize the pinned mixed half-game runtime"
        ) from exc

    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.round_mode != "half"
        or environment.next_round_style != "auto"
        or environment.num_players != 4
        or environment.num_actions != _ACTION_COUNT
    ):
        raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
            "mixed half-game runtime differs from the pinned contract"
        )
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
            "initial mixed half-game state must be active"
        )

    trace = []
    boundaries = []
    round_start_transition_index = 0
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    step_fn = jax.jit(environment.step)
    rule_policy_fn = jax.jit(rule_based_player)
    project_policy_fn = jax.jit(
        lambda features: _mlp_logits(parameters, features, jax)
    )

    for transition_index in range(MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
                "mixed rollout attempted a policy action from a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
                "MahJax step_count must match the global transition index"
            )
        round_index = int(state.round_state.round)
        round_step_index = transition_index - round_start_transition_index
        actor = int(state.current_player)
        legal_actions = _legal_actions(state.legal_action_mask, _ACTION_COUNT)
        try:
            if actor == MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT:
                features = _encode_observation_array(
                    environment.observe(state),
                    jnp,
                )
                logits = jax.block_until_ready(project_policy_fn(features))
                if tuple(logits.shape) != (_ACTION_COUNT,) or not bool(
                    jnp.all(jnp.isfinite(logits))
                ):
                    raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
                        "project policy must produce 87 finite logits"
                    )
                raw_action = int(
                    jnp.argmax(
                        jnp.where(state.legal_action_mask, logits, -jnp.inf)
                    )
                )
                applied_action = raw_action
                normalized = False
                policy_id = _PROJECT_POLICY_ID
            else:
                rule_key, action_key = jax.random.split(rule_key)
                raw_action = int(rule_policy_fn(state, action_key))
                applied_action, normalized = _normalize_rule_action(
                    raw_action,
                    legal_actions,
                )
                policy_id = _RULE_POLICY_ID
        except MahJaxCategoricalMlpMixedHalfGameSmokeError:
            raise
        except Exception as exc:
            raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
                f"mixed policy failed at transition {transition_index}"
            ) from exc
        if applied_action not in legal_actions:
            raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
                f"mixed policy applied illegal action {applied_action}"
            )
        trace.append(
            MahJaxCategoricalMlpMixedHalfGameStep(
                transition_index=transition_index,
                round_index=round_index,
                round_step_index=round_step_index,
                acting_player=actor,
                policy_id=policy_id,
                legal_actions=legal_actions,
                raw_action=raw_action,
                applied_action=applied_action,
                red_pon_normalized=normalized,
            )
        )
        try:
            state = step_fn(state, jnp.int32(applied_action))
            state = jax.block_until_ready(state)
        except Exception as exc:
            raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
                f"mixed half-game step failed at transition {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index] for index in range(4)
        )
        next_round_index = int(state.round_state.round)
        if next_round_index != round_index:
            boundaries.append(
                MahJaxRuleBasedHalfGameRoundBoundary(
                    completed_transition_count=transition_index + 1,
                    previous_round_index=round_index,
                    next_round_index=next_round_index,
                    scores_after_boundary=_four_ints(
                        state.round_state.score,
                        "round-boundary scores",
                    ),
                )
            )
            round_start_transition_index = transition_index + 1
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
            "mixed half-game exceeded the "
            f"{MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP}-transition cap"
        )

    final_scores = _four_ints(state.round_state.score, "final scores")
    final_rewards = _four_floats(state.rewards, "final rewards")
    boundary_values = tuple(
        (
            item.completed_transition_count,
            item.previous_round_index,
            item.next_round_index,
            item.scores_after_boundary,
        )
        for item in boundaries
    )
    normalization_values = tuple(
        (
            item.transition_index,
            item.acting_player,
            item.raw_action,
            item.applied_action,
        )
        for item in trace
        if item.red_pon_normalized
    )
    project_decision_count = sum(
        item.acting_player == MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT
        for item in trace
    )
    if seed == 0 and (
        len(trace) != 825
        or project_decision_count != 200
        or normalization_values != (_EXPECTED_NORMALIZATION,)
        or boundary_values != _EXPECTED_BOUNDARIES
        or not bool(state.terminated)
        or bool(state.truncated)
        or int(state.round_state.round) != 8
        or final_scores != _EXPECTED_FINAL_SCORES
        or final_rewards != _EXPECTED_FINAL_REWARDS
        or cumulative_rewards != _EXPECTED_CUMULATIVE_REWARDS
    ):
        raise MahJaxCategoricalMlpMixedHalfGameSmokeError(
            "seed-0 mixed half-game differs from the approved contract"
        )

    return MahJaxCategoricalMlpMixedHalfGameResult(
        smoke_version=MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        imitation_smoke_version=MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
        project_policy_id=_PROJECT_POLICY_ID,
        rule_policy_id=_RULE_POLICY_ID,
        feature_count=MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
        action_count=_ACTION_COUNT,
        project_seat=MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT,
        seed=seed,
        transition_cap=MAHJAX_RULE_BASED_HALF_GAME_TRANSITION_CAP,
        transition_count=len(trace),
        project_decision_count=project_decision_count,
        rule_decision_count=len(trace) - project_decision_count,
        red_pon_normalization_count=len(normalization_values),
        round_boundaries=tuple(boundaries),
        trace=tuple(trace),
        final_round_index=int(state.round_state.round),
        final_scores=final_scores,
        final_rewards=final_rewards,
        cumulative_rewards=cumulative_rewards,
        terminated=bool(state.terminated),
        truncated=bool(state.truncated),
        half_game_update_count=0,
        selected_model_id=None,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_MIXED_HALF_GAME_PROJECT_SEAT",
    "MahJaxCategoricalMlpMixedHalfGameSmokeError",
    "MahJaxCategoricalMlpMixedHalfGameStep",
    "MahJaxCategoricalMlpMixedHalfGameResult",
    "run_mahjax_categorical_mlp_mixed_half_game_smoke",
]
