"""Five shared-policy MahJax updates plus a fixed independent diagnostic.

The reviewed categorical MLP receives one actor-indexed raw-outcome update
after each of five deterministic all-project-seat rounds. Initial and trained
parameters are then evaluated without updates on disjoint fixed seeds: project
seat zero acts greedily and three bundled rule seats remain fixed. The observed
regression is failure evidence, not improvement or model-strength evidence.
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
    _four_floats,
    _legal_actions,
    _load_pinned_runtime,
    _seat_decision_counts,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    MahJaxCategoricalMlpImitationResult,
    _encode_observation_array,
    _mlp_logits,
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_five_round_training_evaluation_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS = (1, 3, 5, 7, 11)
MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS = tuple(range(20, 36))
MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE = (
    MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE
)

_ACTION_COUNT = 87
_PROJECT_SEAT = 0
_TRANSITION_CAP = 256
_EXPECTED_TRAINING_TRANSITION_COUNTS = (77, 84, 83, 81, 84)
_EXPECTED_TRAINING_SEAT_COUNTS = (
    (21, 22, 17, 17),
    (23, 22, 19, 20),
    (18, 23, 21, 21),
    (18, 21, 23, 19),
    (22, 23, 19, 20),
)
_EXPECTED_TRAINING_CUMULATIVE_REWARDS = (
    (-20.0, 70.0, -20.0, -30.0),
    (-10.0, -10.0, 20.0, -10.0),
    (20.0, -10.0, -10.0, -10.0),
    (0.0, 0.0, -120.0, 120.0),
    (-10.0, 20.0, -10.0, -10.0),
)
_EXPECTED_TRAINING_FINAL_REWARDS = (
    (-20.0, 80.0, -20.0, -20.0),
    (-10.0, -10.0, 30.0, -10.0),
    (30.0, -10.0, -10.0, -10.0),
    (0.0, 0.0, -120.0, 130.0),
    (-10.0, 30.0, -10.0, -10.0),
)
_EXPECTED_TRAINING_FINAL_SCORES = (
    (230, 320, 230, 220),
    (240, 240, 270, 240),
    (270, 240, 240, 240),
    (250, 250, 130, 370),
    (240, 270, 240, 240),
)
_EXPECTED_TRAINING_ACTION_PREFIXES = (
    (28, 27, 28, 28, 29, 33, 27, 31, 27, 0, 31, 32),
    (29, 28, 29, 27, 71, 84, 27, 31, 8, 71, 30, 33),
    (29, 27, 28, 8, 30, 29, 8, 71, 1, 84, 84, 31),
    (28, 27, 30, 31, 27, 29, 32, 71, 18, 1, 0, 16),
    (31, 27, 30, 28, 33, 28, 29, 30, 8, 7, 27, 31),
)
_EXPECTED_INITIAL_OBJECTIVES = (
    0.0936663598,
    -0.0553588867,
    -0.0609763190,
    -0.0202308446,
    -0.0131035689,
)
_EXPECTED_POST_OBJECTIVES = (
    0.0930117071,
    -0.0554395691,
    -0.0609965809,
    -0.0218939111,
    -0.0133588845,
)
_EXPECTED_PER_UPDATE_DELTAS = (
    (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356),
    (0.0002636357, 0.0000601950, 0.0008506179, 0.0000944084),
    (0.0002007297, 0.0000233677, 0.0003997849, 0.0000430078),
    (0.0016294104, 0.0002862717, 0.0037121067, 0.0003829675),
    (0.0004151060, 0.0001173344, 0.0015263907, 0.0001777170),
)
_EXPECTED_FINAL_DELTAS = (
    0.0021020556,
    0.0004550584,
    0.0053585209,
    0.0005585462,
)
_EXPECTED_EVALUATION_TRANSITIONS_BEFORE = (
    82, 73, 79, 51, 86, 86, 53, 64, 86, 31, 61, 63, 58, 48, 62, 91,
)
_EXPECTED_EVALUATION_TRANSITIONS_AFTER = (
    82, 73, 79, 51, 86, 86, 53, 64, 86, 31, 61, 63, 62, 48, 62, 91,
)
_EXPECTED_PROJECT_REWARDS_BEFORE = (
    0.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
    -15.0, 0.0, -180.0, 0.0, 74.0, 0.0, -40.0, 0.0,
)
_EXPECTED_PROJECT_REWARDS_AFTER = (
    0.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
    -15.0, 0.0, -180.0, 0.0, -60.0, 0.0, -40.0, 0.0,
)
_EXPECTED_EVALUATION_SCORES_BEFORE = (
    (250, 250, 302, 198), (211, 211, 367, 211),
    (240, 240, 270, 240), (250, 250, 198, 302),
    (235, 255, 235, 255), (235, 255, 255, 235),
    (250, 202, 250, 298), (170, 240, 250, 340),
    (235, 255, 255, 235), (250, 224, 276, 250),
    (70, 430, 250, 250), (250, 250, 276, 224),
    (324, 186, 240, 250), (250, 211, 289, 250),
    (210, 210, 370, 210), (250, 322, 240, 188),
)
_EXPECTED_EVALUATION_SCORES_AFTER = (
    (250, 250, 302, 198), (211, 211, 367, 211),
    (240, 240, 270, 240), (250, 250, 198, 302),
    (235, 255, 235, 255), (235, 255, 255, 235),
    (250, 202, 250, 298), (170, 240, 250, 340),
    (235, 255, 255, 235), (250, 224, 276, 250),
    (70, 430, 250, 250), (250, 250, 276, 224),
    (190, 190, 430, 190), (250, 211, 289, 250),
    (210, 210, 370, 210), (250, 322, 240, 188),
)
_EXPECTED_PROJECT_TRACES_BEFORE = (
    (29, 29, 71, 32, 84, 33, 71, 71, 71, 0, 71, 84, 17, 84, 71, 18, 71, 84, 9),
    (32, 33, 8, 9, 18, 71, 0, 71, 17, 71, 84, 71, 71, 71, 71, 71),
    (29, 27, 30, 29, 31, 32, 71, 18, 84, 71, 71, 71, 71, 71, 84, 17, 71, 84, 71, 71),
    (29, 29, 27, 32, 9, 71, 71, 71),
    (29, 30, 32, 84, 31, 31, 0, 8, 8, 71, 84, 71, 71, 71, 84, 84, 71, 71, 71, 84, 1, 71),
    (29, 27, 27, 33, 32, 0, 18, 84, 19, 71, 84, 71, 71, 84, 71, 10, 84, 71, 71, 71, 84, 71, 84, 71),
    (29, 31, 26, 84, 71, 71, 71, 71, 71, 71, 71),
    (30, 31, 8, 84, 71, 84, 26, 29, 0, 18, 71, 26, 71, 84, 71, 10),
    (30, 33, 71, 71, 84, 71, 71, 84, 8, 17, 71, 71, 84, 71, 71, 71, 71, 84, 71, 84, 71, 71),
    (28, 8, 31, 71, 84, 9, 84, 32),
    (28, 29, 30, 84, 32, 18, 71, 0, 71, 18, 71, 71, 71, 84, 71),
    (31, 33, 71, 71, 8, 71, 71, 71, 71, 71, 84, 0, 31, 84, 27),
    (27, 8, 84, 9, 18, 31, 71, 84, 17, 71, 71, 72, 7, 71, 71, 74),
    (30, 33, 28, 71, 8, 84, 71, 17, 71, 84, 71, 71),
    (31, 8, 84, 71, 17, 17, 71, 84, 71, 84, 71, 71, 84, 71, 71),
    (33, 9, 84, 17, 71, 71, 84, 71, 71, 71, 71, 71, 84, 71, 71, 71, 71, 71, 71, 71),
)
_EXPECTED_PROJECT_TRACES_AFTER = (
    *_EXPECTED_PROJECT_TRACES_BEFORE[:12],
    (27, 8, 84, 9, 18, 31, 71, 84, 17, 0, 71, 0, 84, 71, 26, 71),
    *_EXPECTED_PROJECT_TRACES_BEFORE[13:],
)
_EVIDENCE_GRADE = (
    "P8 local five-round shared-policy training and fixed mixed-policy failure "
    "diagnostic evidence only"
)
_WARNINGS = (
    "five-round bounded shared all-project-seat training diagnostic only",
    "fixed disjoint mixed-policy evaluation performs no gradient update",
    "evaluation regression observed: project raw sum -320 to -454",
    "only evaluation seed 32 changes and project raw reward falls 74 to -60",
    "objective decreases during training are not policy-improvement evidence",
    "no baseline, critic, discount, GAE, entropy, replay or reward shaping",
    "no persistence, checkpoint, model artifact, external or real data",
    "no production self-play, evaluation, league or candidate promotion",
    "not improvement, policy-quality or model-strength evidence",
    "not Tenhou, stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(RuntimeError):
    """Raised when the bounded training/evaluation contract fails."""


@dataclass(frozen=True)
class _MixedPolicyEvaluationRound:
    transition_count: int
    project_action_trace: Tuple[int, ...]
    project_cumulative_raw_reward: float
    final_scores: Tuple[int, ...]


@dataclass(frozen=True)
class MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult:
    """Immutable diagnostics from five updates and fixed evaluation."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    training_seeds: Tuple[int, ...]
    evaluation_seeds: Tuple[int, ...]
    round_count: int
    update_count: int
    evaluation_update_count: int
    learning_rate: float
    training_result: MahJaxCategoricalMlpImitationResult
    training_transition_counts: Tuple[int, ...]
    training_seat_decision_counts: Tuple[Tuple[int, ...], ...]
    training_actor_traces: Tuple[Tuple[int, ...], ...]
    training_action_traces: Tuple[Tuple[int, ...], ...]
    training_legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    training_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    training_final_raw_rewards: Tuple[Tuple[float, ...], ...]
    training_final_scores: Tuple[Tuple[int, ...], ...]
    training_initial_objectives: Tuple[float, ...]
    training_post_update_objectives: Tuple[float, ...]
    per_update_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    final_parameter_delta_l2: Tuple[float, ...]
    evaluation_transition_counts_before: Tuple[int, ...]
    evaluation_transition_counts_after: Tuple[int, ...]
    evaluation_project_action_traces_before: Tuple[Tuple[int, ...], ...]
    evaluation_project_action_traces_after: Tuple[Tuple[int, ...], ...]
    evaluation_project_raw_rewards_before: Tuple[float, ...]
    evaluation_project_raw_rewards_after: Tuple[float, ...]
    evaluation_final_scores_before: Tuple[Tuple[int, ...], ...]
    evaluation_final_scores_after: Tuple[Tuple[int, ...], ...]
    changed_evaluation_seeds: Tuple[int, ...]
    before_project_raw_sum: float
    after_project_raw_sum: float
    before_positive_round_count: int
    after_positive_round_count: int
    before_negative_round_count: int
    after_negative_round_count: int
    training_evaluation_seeds_disjoint: bool
    parameter_continuity_proven: bool
    all_training_actions_legal: bool
    all_evaluation_actions_legal: bool
    all_rounds_terminated: bool
    evaluation_regression_observed: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _collect_mixed_policy_evaluation_round(
    seed,
    parameters,
    environment,
    step_fn,
    rule_policy_fn,
    jax,
    jnp,
):
    init_key, rule_key = jax.random.split(jax.random.PRNGKey(seed))
    try:
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            f"failed to initialize fixed evaluation seed {seed}"
        ) from exc
    if bool(state.terminated) or bool(state.truncated):
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "fixed evaluation initial state must be active"
        )

    project_actions = []
    cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                "fixed evaluation attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                "fixed evaluation step_count must be monotonic"
            )
        actor = int(state.current_player)
        legal_actions = _legal_actions(state.legal_action_mask)
        try:
            if actor == _PROJECT_SEAT:
                features = _encode_observation_array(
                    environment.observe(state),
                    jnp,
                )
                logits = _mlp_logits(parameters, features, jax)
                if tuple(logits.shape) != (_ACTION_COUNT,) or not bool(
                    jnp.all(jnp.isfinite(logits))
                ):
                    raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                        "fixed evaluation project policy must produce 87 finite logits"
                    )
                action = int(
                    jnp.argmax(
                        jnp.where(state.legal_action_mask, logits, -jnp.inf)
                    )
                )
                project_actions.append(action)
            else:
                rule_key, action_key = jax.random.split(rule_key)
                action = int(rule_policy_fn(state, action_key))
        except MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError:
            raise
        except Exception as exc:
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                f"fixed evaluation policy failed at seed {seed} step {transition_index}"
            ) from exc
        if action not in legal_actions:
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                f"fixed evaluation selected illegal action {action} at seed {seed} "
                f"step {transition_index}"
            )
        try:
            state = jax.block_until_ready(step_fn(state, jnp.int32(action)))
        except Exception as exc:
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                f"fixed evaluation step failed at seed {seed} step {transition_index}"
            ) from exc
        raw_rewards = _four_floats(state.rewards, "state.rewards")
        cumulative_rewards = tuple(
            cumulative_rewards[index] + raw_rewards[index]
            for index in range(4)
        )
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            f"fixed evaluation exceeded {_TRANSITION_CAP} transitions"
        )

    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "fixed evaluation must terminate without truncation"
        )
    final_scores = tuple(int(value) for value in state.round_state.score)
    if len(final_scores) != 4 or not project_actions:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "fixed evaluation must expose four scores and project decisions"
        )
    return _MixedPolicyEvaluationRound(
        transition_count=transition_index + 1,
        project_action_trace=tuple(project_actions),
        project_cumulative_raw_reward=cumulative_rewards[_PROJECT_SEAT],
        final_scores=final_scores,
    )


def run_mahjax_categorical_mlp_five_round_training_evaluation_smoke(
) -> MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult:
    """Run five reviewed updates and a disjoint no-update diagnostic."""

    try:
        jax, jnp, parameters, training_result = (
            _train_mahjax_categorical_mlp_parameters()
        )
    except Exception as exc:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "reviewed categorical MLP in-memory training failed"
        ) from exc
    try:
        _, _, mahjax = _load_pinned_runtime()
        from mahjax.red_mahjong.players import rule_based_player
    except Exception as exc:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "pinned MahJax/JAX fixed evaluation runtime is unavailable"
        ) from exc
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    initial_parameters = parameters
    trajectories = []
    updates = []
    for seed in MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS:
        try:
            trajectory = _collect_all_project_round(
                seed, parameters, jax, jnp, mahjax
            )
            update = _apply_actor_indexed_raw_outcome_update(
                parameters, trajectory, jax, jnp
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                f"all-project training round seed {seed} failed"
            ) from exc
        trajectories.append(trajectory)
        updates.append(update)
        parameters = update.parameters

    training_transition_counts = tuple(
        len(item.action_trace) for item in trajectories
    )
    training_seat_counts = tuple(
        _seat_decision_counts(item.actor_trace) for item in trajectories
    )
    training_cumulative_rewards = tuple(
        item.cumulative_rewards for item in trajectories
    )
    training_final_rewards = tuple(item.final_rewards for item in trajectories)
    training_final_scores = tuple(item.final_scores for item in trajectories)
    initial_objectives = tuple(item.initial_objective for item in updates)
    post_objectives = tuple(item.post_update_objective for item in updates)
    per_update_deltas = tuple(item.parameter_delta_l2 for item in updates)
    if (
        training_transition_counts != _EXPECTED_TRAINING_TRANSITION_COUNTS
        or training_seat_counts != _EXPECTED_TRAINING_SEAT_COUNTS
        or training_cumulative_rewards != _EXPECTED_TRAINING_CUMULATIVE_REWARDS
        or training_final_rewards != _EXPECTED_TRAINING_FINAL_REWARDS
        or training_final_scores != _EXPECTED_TRAINING_FINAL_SCORES
        or any(
            trajectory.action_trace[:12] != expected
            for trajectory, expected in zip(
                trajectories, _EXPECTED_TRAINING_ACTION_PREFIXES
            )
        )
        or any(
            not _close(actual, expected)
            for actual, expected in zip(
                initial_objectives, _EXPECTED_INITIAL_OBJECTIVES
            )
        )
        or any(
            not _close(actual, expected)
            for actual, expected in zip(post_objectives, _EXPECTED_POST_OBJECTIVES)
        )
        or any(
            not _close(actual, expected)
            for actual_row, expected_row in zip(
                per_update_deltas, _EXPECTED_PER_UPDATE_DELTAS
            )
            for actual, expected in zip(actual_row, expected_row)
        )
        or any(
            post >= initial
            for initial, post in zip(initial_objectives, post_objectives)
        )
    ):
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "five-round training diagnostics differ from the reviewed probe"
        )

    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if any(
        not _close(actual, expected) or actual <= 0.0
        for actual, expected in zip(final_deltas, _EXPECTED_FINAL_DELTAS)
    ):
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "five-round final parameter deltas differ from the reviewed probe"
        )

    try:
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        step_fn = jax.jit(environment.step)
        rule_policy_fn = jax.jit(rule_based_player)
    except Exception as exc:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "failed to initialize fixed mixed-policy evaluation"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != _ACTION_COUNT
    ):
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "fixed evaluation environment differs from the pinned contract"
        )

    before_rounds = []
    after_rounds = []
    for seed in MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS:
        try:
            before = _collect_mixed_policy_evaluation_round(
                seed,
                initial_parameters,
                environment,
                step_fn,
                rule_policy_fn,
                jax,
                jnp,
            )
            after = _collect_mixed_policy_evaluation_round(
                seed,
                parameters,
                environment,
                step_fn,
                rule_policy_fn,
                jax,
                jnp,
            )
        except Exception as exc:
            raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
                f"fixed mixed-policy evaluation seed {seed} failed"
            ) from exc
        before_rounds.append(before)
        after_rounds.append(after)

    before_transitions = tuple(item.transition_count for item in before_rounds)
    after_transitions = tuple(item.transition_count for item in after_rounds)
    before_traces = tuple(item.project_action_trace for item in before_rounds)
    after_traces = tuple(item.project_action_trace for item in after_rounds)
    before_rewards = tuple(
        item.project_cumulative_raw_reward for item in before_rounds
    )
    after_rewards = tuple(
        item.project_cumulative_raw_reward for item in after_rounds
    )
    before_scores = tuple(item.final_scores for item in before_rounds)
    after_scores = tuple(item.final_scores for item in after_rounds)
    changed_seeds = tuple(
        seed
        for seed, before, after in zip(
            MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS,
            before_rounds,
            after_rounds,
        )
        if before != after
    )
    if (
        before_transitions != _EXPECTED_EVALUATION_TRANSITIONS_BEFORE
        or after_transitions != _EXPECTED_EVALUATION_TRANSITIONS_AFTER
        or before_traces != _EXPECTED_PROJECT_TRACES_BEFORE
        or after_traces != _EXPECTED_PROJECT_TRACES_AFTER
        or before_rewards != _EXPECTED_PROJECT_REWARDS_BEFORE
        or after_rewards != _EXPECTED_PROJECT_REWARDS_AFTER
        or before_scores != _EXPECTED_EVALUATION_SCORES_BEFORE
        or after_scores != _EXPECTED_EVALUATION_SCORES_AFTER
        or changed_seeds != (32,)
    ):
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "fixed evaluation diagnostics differ from the reviewed probe"
        )

    before_sum = sum(before_rewards)
    after_sum = sum(after_rewards)
    before_positive = sum(value > 0.0 for value in before_rewards)
    after_positive = sum(value > 0.0 for value in after_rewards)
    before_negative = sum(value < 0.0 for value in before_rewards)
    after_negative = sum(value < 0.0 for value in after_rewards)
    regression_observed = (
        before_sum == -320.0
        and after_sum == -454.0
        and before_positive == 1
        and after_positive == 0
        and before_negative == 8
        and after_negative == 9
        and before_rewards[12] == 74.0
        and after_rewards[12] == -60.0
    )
    if not regression_observed:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "fixed evaluation regression differs from the reviewed probe"
        )

    disjoint = not set(MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS).intersection(
        MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS
    )
    continuity = all(value > 0.0 for value in final_deltas)
    if not disjoint or not continuity:
        raise MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError(
            "training/evaluation separation or parameter continuity failed"
        )

    return MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        training_seeds=MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS,
        evaluation_seeds=MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS,
        round_count=5,
        update_count=5,
        evaluation_update_count=0,
        learning_rate=MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE,
        training_result=training_result,
        training_transition_counts=training_transition_counts,
        training_seat_decision_counts=training_seat_counts,
        training_actor_traces=tuple(item.actor_trace for item in trajectories),
        training_action_traces=tuple(item.action_trace for item in trajectories),
        training_legal_action_traces=tuple(
            item.legal_action_trace for item in trajectories
        ),
        training_cumulative_raw_rewards=training_cumulative_rewards,
        training_final_raw_rewards=training_final_rewards,
        training_final_scores=training_final_scores,
        training_initial_objectives=initial_objectives,
        training_post_update_objectives=post_objectives,
        per_update_parameter_delta_l2=per_update_deltas,
        final_parameter_delta_l2=final_deltas,
        evaluation_transition_counts_before=before_transitions,
        evaluation_transition_counts_after=after_transitions,
        evaluation_project_action_traces_before=before_traces,
        evaluation_project_action_traces_after=after_traces,
        evaluation_project_raw_rewards_before=before_rewards,
        evaluation_project_raw_rewards_after=after_rewards,
        evaluation_final_scores_before=before_scores,
        evaluation_final_scores_after=after_scores,
        changed_evaluation_seeds=changed_seeds,
        before_project_raw_sum=before_sum,
        after_project_raw_sum=after_sum,
        before_positive_round_count=before_positive,
        after_positive_round_count=after_positive,
        before_negative_round_count=before_negative,
        after_negative_round_count=after_negative,
        training_evaluation_seeds_disjoint=disjoint,
        parameter_continuity_proven=continuity,
        all_training_actions_legal=True,
        all_evaluation_actions_legal=True,
        all_rounds_terminated=True,
        evaluation_regression_observed=regression_observed,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE",
    "MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError",
    "MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult",
    "run_mahjax_categorical_mlp_five_round_training_evaluation_smoke",
]
