"""Categorical-feature MLP imitation training with all-project outcomes.

Bundled MahJax rule-policy decisions from disjoint local seeds train one small
project-owned MLP entirely in memory. The trained policy then drives all four
seats greedily through fixed local rounds to verify nonzero raw-outcome signal.
This is not an RL update, production self-play, or model-strength evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping, Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)


MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION = (
    "p7_p8_mahjax_categorical_mlp_imitation_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT = 882
MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS = tuple(range(8))
MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS = tuple(range(8, 12))
MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS = tuple(range(16))
MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS = 48

_ACTION_COUNT = 87
_HIDDEN_UNIT_COUNT = 64
_RECENT_ACTION_COUNT = 8
_MODEL_SEED = 123
_LEARNING_RATE = 0.003
_ADAM_BETA1 = 0.9
_ADAM_BETA2 = 0.999
_ADAM_EPSILON = 1e-8
_TRANSITION_CAP = 256
_PARAMETER_COUNT = (
    MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT * _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT
    + _HIDDEN_UNIT_COUNT * _ACTION_COUNT
    + _ACTION_COUNT
)
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
_EVIDENCE_GRADE = (
    "P7/P8 local categorical-MLP imitation and all-project outcome smoke evidence only"
)
_WARNINGS = (
    "local categorical-feature MLP imitation training smoke only",
    "train seeds 0 through 7 and evaluation seeds 8 through 11 are disjoint",
    "teacher decisions come only from the pinned bundled MahJax rule policy",
    "exact 882 current-player observation features with no opponent hidden hand",
    "exact 64-hidden ReLU MLP and 48 full-batch Adam epochs",
    "all labels and all-project actions are checked against environment legality",
    "all-project seeds 0 through 15 use one frozen greedy shared policy",
    "all-project rounds are outcome-signal diagnostics with no RL update",
    "no saved dataset, parameters, model weights, checkpoint or artifact",
    "no real Tenhou, real haifu, external log or platform data",
    "not production self-play, evaluation, league or candidate promotion",
    "not improvement, policy-quality, model-strength, stable-dan or LuckyJ evidence",
)


class MahJaxCategoricalMlpImitationSmokeError(RuntimeError):
    """Raised when the exact categorical MLP training contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpImitationResult:
    """Immutable diagnostics from local training and outcome rounds."""

    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    train_seeds: Tuple[int, ...]
    eval_seeds: Tuple[int, ...]
    selfplay_seeds: Tuple[int, ...]
    recent_action_count: int
    feature_count: int
    hidden_unit_count: int
    action_count: int
    parameter_count: int
    model_seed: int
    epoch_count: int
    learning_rate: float
    adam_beta1: float
    adam_beta2: float
    adam_epsilon: float
    train_example_count: int
    eval_example_count: int
    initial_train_loss: float
    final_train_loss: float
    initial_eval_loss: float
    final_eval_loss: float
    initial_train_accuracy: float
    final_train_accuracy: float
    initial_eval_accuracy: float
    final_eval_accuracy: float
    pre_update_loss_history: Tuple[float, ...]
    parameter_delta_l2: float
    selfplay_round_count: int
    selfplay_transition_counts: Tuple[int, ...]
    selfplay_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    selfplay_final_raw_rewards: Tuple[Tuple[float, ...], ...]
    selfplay_final_scores: Tuple[Tuple[int, ...], ...]
    selfplay_nonzero_outcome_seeds: Tuple[int, ...]
    selfplay_all_actions_legal: bool
    selfplay_all_rounds_terminated: bool
    training_applied: bool
    train_eval_sources_separate: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _load_pinned_runtime():
    try:
        import jax
        import jax.numpy as jnp
        import mahjax
        from mahjax.red_mahjong.players import rule_based_player
    except Exception as exc:
        raise MahJaxCategoricalMlpImitationSmokeError(
            "pinned MahJax/JAX categorical-MLP runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax, rule_based_player


def _one_hot(index: int, size: int, jnp, field_name: str):
    if index < 0 or index >= size:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"{field_name} index must be from 0 through {size - 1}"
        )
    return jnp.zeros((size,), dtype=jnp.float32).at[index].set(1.0)


def _validated_observation(observation: object):
    if type(observation) is not dict:
        raise MahJaxCategoricalMlpImitationSmokeError(
            "MahJax categorical observation must be an exact dict"
        )
    if set(observation) != set(_EXPECTED_OBSERVATION_SHAPES):
        raise MahJaxCategoricalMlpImitationSmokeError(
            "MahJax categorical observation keys differ from the pinned contract"
        )
    actual_shapes = {
        key: tuple(getattr(observation[key], "shape", ()))
        for key in _EXPECTED_OBSERVATION_SHAPES
    }
    if actual_shapes != _EXPECTED_OBSERVATION_SHAPES:
        raise MahJaxCategoricalMlpImitationSmokeError(
            "MahJax categorical observation shapes differ from the pinned contract"
        )
    return observation


def _encode_observation_array(observation: object, jnp):
    observation = _validated_observation(observation)

    hand_counts = jnp.zeros((37,), dtype=jnp.float32)
    for raw_tile in observation["hand"].tolist():
        tile = int(raw_tile)
        if tile == -1:
            continue
        if tile < 0 or tile >= 37:
            raise MahJaxCategoricalMlpImitationSmokeError(
                "hand tile must be -1 or an exact 0-through-36 tile id"
            )
        hand_counts = hand_counts.at[tile].add(0.25)

    raw_last_draw = int(observation["last_draw"])
    if raw_last_draw < -1 or raw_last_draw >= 37:
        raise MahJaxCategoricalMlpImitationSmokeError(
            "last_draw must be -1 or an exact 0-through-36 tile id"
        )
    last_draw = _one_hot(
        raw_last_draw if raw_last_draw >= 0 else 37,
        38,
        jnp,
        "last_draw",
    )

    history = observation["action_history"]
    history_actions = tuple(int(value) for value in history[1].tolist())
    valid_columns = tuple(
        index for index, action in enumerate(history_actions) if action >= 0
    )[-_RECENT_ACTION_COUNT:]
    recent_history = jnp.zeros(
        (_RECENT_ACTION_COUNT, 92),
        dtype=jnp.float32,
    )
    output_row = _RECENT_ACTION_COUNT - len(valid_columns)
    for column in valid_columns:
        actor = int(history[0, column])
        action = int(history[1, column])
        tsumogiri = int(history[2, column])
        if actor < 0 or actor >= 4 or action < 0 or action >= _ACTION_COUNT:
            raise MahJaxCategoricalMlpImitationSmokeError(
                "valid action history must contain exact actor/action ids"
            )
        recent_history = recent_history.at[output_row, actor].set(1.0)
        recent_history = recent_history.at[output_row, 4 + action].set(1.0)
        recent_history = recent_history.at[output_row, 91].set(
            float(tsumogiri > 0)
        )
        output_row += 1

    shanten_bucket = max(0, min(6, int(observation["shanten_count"]) + 1))
    shanten = _one_hot(shanten_bucket, 7, jnp, "shanten_count")
    furiten = jnp.asarray([observation["furiten"]], dtype=jnp.float32)
    scores = jnp.asarray(observation["scores"], dtype=jnp.float32) / 1000.0
    round_index = int(observation["round"])
    round_feature = _one_hot(round_index, 12, jnp, "round")
    counters = jnp.asarray(
        [observation["honba"], observation["kyotaku"]],
        dtype=jnp.float32,
    ) / 10.0
    prevalent_wind = _one_hot(
        int(observation["prevalent_wind"]),
        4,
        jnp,
        "prevalent_wind",
    )
    seat_wind = _one_hot(
        int(observation["seat_wind"]),
        4,
        jnp,
        "seat_wind",
    )

    dora_counts = jnp.zeros((37,), dtype=jnp.float32)
    for raw_tile in observation["dora_indicators"].tolist():
        tile = int(raw_tile)
        if tile == -1:
            continue
        if tile < 0 or tile >= 37:
            raise MahJaxCategoricalMlpImitationSmokeError(
                "dora indicator must be -1 or an exact 0-through-36 tile id"
            )
        dora_counts = dora_counts.at[tile].add(0.25)

    features = jnp.concatenate(
        (
            hand_counts,
            last_draw,
            recent_history.ravel(),
            shanten,
            furiten,
            scores,
            round_feature,
            counters,
            prevalent_wind,
            seat_wind,
            dora_counts,
        )
    )
    if tuple(features.shape) != (MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,):
        raise MahJaxCategoricalMlpImitationSmokeError(
            "categorical observation must contain exactly 882 features"
        )
    if not bool(jnp.all(jnp.isfinite(features))):
        raise MahJaxCategoricalMlpImitationSmokeError(
            "categorical observation features must all be finite"
        )
    return features


def encode_mahjax_categorical_observation(
    observation: Mapping[str, object],
) -> Tuple[float, ...]:
    """Return one immutable 882-feature current-player observation."""

    _, jnp, _, _ = _load_pinned_runtime()
    features = _encode_observation_array(observation, jnp)
    return tuple(float(value) for value in features)


def _collect_rule_decisions(
    seed,
    environment,
    step_fn,
    teacher_fn,
    jax,
    jnp,
):
    try:
        init_key, policy_key = jax.random.split(jax.random.PRNGKey(seed))
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"failed to initialize categorical decision source seed {seed}"
        ) from exc
    features = []
    masks = []
    labels = []
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxCategoricalMlpImitationSmokeError(
                "categorical decision collection attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxCategoricalMlpImitationSmokeError(
                "categorical decision source step_count must be monotonic"
            )
        feature_array = _encode_observation_array(environment.observe(state), jnp)
        mask = state.legal_action_mask
        if str(mask.dtype) != "bool" or tuple(mask.shape) != (_ACTION_COUNT,):
            raise MahJaxCategoricalMlpImitationSmokeError(
                "categorical decision legal mask must be an exact bool 87-vector"
            )
        try:
            policy_key, action_key = jax.random.split(policy_key)
            label = int(teacher_fn(state, action_key))
        except Exception as exc:
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"teacher failed at seed {seed} transition {transition_index}"
            ) from exc
        if label < 0 or label >= _ACTION_COUNT or not bool(mask[label]):
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"teacher label is illegal at seed {seed} transition {transition_index}"
            )
        features.append(feature_array)
        masks.append(mask)
        labels.append(label)
        try:
            state = jax.block_until_ready(step_fn(state, jnp.int32(label)))
        except Exception as exc:
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"decision source step failed at seed {seed} transition {transition_index}"
            ) from exc
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"decision source seed {seed} exceeded the transition cap"
        )
    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"decision source seed {seed} must terminate without truncation"
        )
    return (
        jnp.stack(features),
        jnp.stack(masks),
        jnp.asarray(labels, dtype=jnp.int32),
    )


def _mlp_logits(parameters, features, jax):
    hidden = jax.nn.relu(features @ parameters[0] + parameters[1])
    return hidden @ parameters[2] + parameters[3]


def _four_floats(value: object, field_name: str) -> Tuple[float, ...]:
    try:
        normalized = tuple(float(item) for item in value)  # type: ignore[union-attr]
    except Exception as exc:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"{field_name} must be an iterable four-vector"
        ) from exc
    if len(normalized) != 4:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"{field_name} must contain exactly four values"
        )
    return normalized


def _run_all_project_rounds(
    parameters,
    environment,
    step_fn,
    jax,
    jnp,
):
    transition_counts = []
    cumulative_results = []
    final_results = []
    score_results = []
    for seed in MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS:
        try:
            state = environment.init(jax.random.PRNGKey(seed))
        except Exception as exc:
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"failed to initialize all-project seed {seed}"
            ) from exc
        cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
        for transition_index in range(_TRANSITION_CAP):
            feature_array = _encode_observation_array(
                environment.observe(state),
                jnp,
            )
            mask = state.legal_action_mask
            if str(mask.dtype) != "bool" or tuple(mask.shape) != (_ACTION_COUNT,):
                raise MahJaxCategoricalMlpImitationSmokeError(
                    "all-project legal mask must be an exact bool 87-vector"
                )
            scores = _mlp_logits(parameters, feature_array, jax)
            action = int(jnp.argmax(jnp.where(mask, scores, -jnp.inf)))
            if action < 0 or action >= _ACTION_COUNT or not bool(mask[action]):
                raise MahJaxCategoricalMlpImitationSmokeError(
                    f"all-project action is illegal at seed {seed} transition "
                    f"{transition_index}"
                )
            try:
                state = jax.block_until_ready(step_fn(state, jnp.int32(action)))
            except Exception as exc:
                raise MahJaxCategoricalMlpImitationSmokeError(
                    f"all-project step failed at seed {seed} transition "
                    f"{transition_index}"
                ) from exc
            raw_rewards = _four_floats(state.rewards, "state.rewards")
            cumulative_rewards = tuple(
                cumulative_rewards[index] + raw_rewards[index]
                for index in range(4)
            )
            if bool(state.terminated) or bool(state.truncated):
                break
        else:
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"all-project seed {seed} exceeded the transition cap"
            )
        if not bool(state.terminated) or bool(state.truncated):
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"all-project seed {seed} must terminate without truncation"
            )
        try:
            final_scores = tuple(int(value) for value in state.round_state.score)
        except Exception as exc:
            raise MahJaxCategoricalMlpImitationSmokeError(
                f"failed to read all-project global scores at seed {seed}"
            ) from exc
        if len(final_scores) != 4:
            raise MahJaxCategoricalMlpImitationSmokeError(
                "all-project final scores must contain four seats"
            )
        transition_counts.append(transition_index + 1)
        cumulative_results.append(cumulative_rewards)
        final_results.append(_four_floats(state.rewards, "state.rewards"))
        score_results.append(final_scores)
    return (
        tuple(transition_counts),
        tuple(cumulative_results),
        tuple(final_results),
        tuple(score_results),
    )


def _train_mahjax_categorical_mlp_parameters():
    jax, jnp, mahjax, rule_policy = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )
    try:
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        step_fn = jax.jit(environment.step)
        teacher_fn = jax.jit(rule_policy)
    except Exception as exc:
        raise MahJaxCategoricalMlpImitationSmokeError(
            "failed to initialize categorical MLP training environment"
        ) from exc
    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != _ACTION_COUNT
    ):
        raise MahJaxCategoricalMlpImitationSmokeError(
            "categorical MLP environment differs from the pinned contract"
        )

    train_parts = tuple(
        _collect_rule_decisions(
            seed,
            environment,
            step_fn,
            teacher_fn,
            jax,
            jnp,
        )
        for seed in MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS
    )
    eval_parts = tuple(
        _collect_rule_decisions(
            seed,
            environment,
            step_fn,
            teacher_fn,
            jax,
            jnp,
        )
        for seed in MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS
    )
    train_features = jnp.concatenate(tuple(part[0] for part in train_parts))
    train_masks = jnp.concatenate(tuple(part[1] for part in train_parts))
    train_labels = jnp.concatenate(tuple(part[2] for part in train_parts))
    eval_features = jnp.concatenate(tuple(part[0] for part in eval_parts))
    eval_masks = jnp.concatenate(tuple(part[1] for part in eval_parts))
    eval_labels = jnp.concatenate(tuple(part[2] for part in eval_parts))
    if int(train_labels.shape[0]) != 482 or int(eval_labels.shape[0]) != 221:
        raise MahJaxCategoricalMlpImitationSmokeError(
            "categorical train/evaluation sources must contain exactly 482/221 examples"
        )

    model_key1, model_key2 = jax.random.split(jax.random.PRNGKey(_MODEL_SEED))
    initial_parameters = (
        jax.random.normal(
            model_key1,
            (MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT, _HIDDEN_UNIT_COUNT),
            dtype=jnp.float32,
        )
        * 0.03,
        jnp.zeros((_HIDDEN_UNIT_COUNT,), dtype=jnp.float32),
        jax.random.normal(
            model_key2,
            (_HIDDEN_UNIT_COUNT, _ACTION_COUNT),
            dtype=jnp.float32,
        )
        * 0.03,
        jnp.zeros((_ACTION_COUNT,), dtype=jnp.float32),
    )

    def masked_loss(parameters, features, masks, labels):
        logits = _mlp_logits(parameters, features, jax)
        log_probabilities = jax.nn.log_softmax(
            jnp.where(masks, logits, -1e9),
            axis=1,
        )
        return -jnp.mean(
            log_probabilities[jnp.arange(labels.shape[0]), labels]
        )

    def exact_accuracy(parameters, features, masks, labels):
        predictions = jnp.argmax(
            jnp.where(masks, _mlp_logits(parameters, features, jax), -1e9),
            axis=1,
        )
        return jnp.mean(predictions == labels)

    parameters = initial_parameters
    first_moment = tuple(jnp.zeros_like(value) for value in parameters)
    second_moment = tuple(jnp.zeros_like(value) for value in parameters)
    loss_and_gradient = jax.jit(
        jax.value_and_grad(
            lambda values: masked_loss(
                values,
                train_features,
                train_masks,
                train_labels,
            )
        )
    )
    initial_train_loss = float(
        masked_loss(parameters, train_features, train_masks, train_labels)
    )
    initial_eval_loss = float(
        masked_loss(parameters, eval_features, eval_masks, eval_labels)
    )
    initial_train_accuracy = float(
        exact_accuracy(parameters, train_features, train_masks, train_labels)
    )
    initial_eval_accuracy = float(
        exact_accuracy(parameters, eval_features, eval_masks, eval_labels)
    )
    pre_update_losses = []
    for epoch_index in range(MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS):
        loss_value, gradients = loss_and_gradient(parameters)
        pre_update_losses.append(float(loss_value))
        first_moment = tuple(
            _ADAM_BETA1 * moment + (1.0 - _ADAM_BETA1) * gradient
            for moment, gradient in zip(first_moment, gradients)
        )
        second_moment = tuple(
            _ADAM_BETA2 * moment + (1.0 - _ADAM_BETA2) * gradient * gradient
            for moment, gradient in zip(second_moment, gradients)
        )
        step_number = epoch_index + 1
        corrected_first = tuple(
            moment / (1.0 - _ADAM_BETA1**step_number)
            for moment in first_moment
        )
        corrected_second = tuple(
            moment / (1.0 - _ADAM_BETA2**step_number)
            for moment in second_moment
        )
        parameters = tuple(
            value
            - _LEARNING_RATE
            * first
            / (jnp.sqrt(second) + _ADAM_EPSILON)
            for value, first, second in zip(
                parameters,
                corrected_first,
                corrected_second,
            )
        )
    parameters = jax.block_until_ready(parameters)

    final_train_loss = float(
        masked_loss(parameters, train_features, train_masks, train_labels)
    )
    final_eval_loss = float(
        masked_loss(parameters, eval_features, eval_masks, eval_labels)
    )
    final_train_accuracy = float(
        exact_accuracy(parameters, train_features, train_masks, train_labels)
    )
    final_eval_accuracy = float(
        exact_accuracy(parameters, eval_features, eval_masks, eval_labels)
    )
    parameter_delta_l2 = math.sqrt(
        sum(
            float(jnp.linalg.norm(value - initial_value)) ** 2
            for value, initial_value in zip(parameters, initial_parameters)
        )
    )

    (
        selfplay_transition_counts,
        selfplay_cumulative_rewards,
        selfplay_final_rewards,
        selfplay_final_scores,
    ) = _run_all_project_rounds(
        parameters,
        environment,
        step_fn,
        jax,
        jnp,
    )
    selfplay_nonzero_seeds = tuple(
        seed
        for seed, rewards in zip(
            MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS,
            selfplay_cumulative_rewards,
        )
        if any(rewards)
    )
    expected_nonzero_rewards = {
        0: (-10.0, -10.0, -10.0, 20.0),
        1: (-10.0, -10.0, 20.0, -10.0),
        3: (-10.0, -10.0, -10.0, 20.0),
        5: (32.0, -32.0, 0.0, 0.0),
        6: (-23.0, 37.0, -7.0, -7.0),
        7: (-10.0, -10.0, -10.0, 20.0),
        10: (0.0, 180.0, 0.0, -180.0),
    }
    if (
        abs(final_train_loss - 0.36734492) > 1e-5
        or abs(final_eval_loss - 1.77358353) > 1e-5
        or abs(final_train_accuracy - 0.93153530) > 1e-5
        or abs(final_eval_accuracy - 0.58371043) > 1e-5
        or selfplay_nonzero_seeds != tuple(expected_nonzero_rewards)
        or any(
            selfplay_cumulative_rewards[seed] != rewards
            for seed, rewards in expected_nonzero_rewards.items()
        )
        or final_train_loss >= initial_train_loss
        or final_eval_loss >= initial_eval_loss
        or parameter_delta_l2 <= 0.0
    ):
        raise MahJaxCategoricalMlpImitationSmokeError(
            "categorical MLP diagnostics differ from the reviewed probe"
        )

    result = MahJaxCategoricalMlpImitationResult(
        smoke_version=MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        train_seeds=MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS,
        eval_seeds=MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS,
        selfplay_seeds=MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS,
        recent_action_count=_RECENT_ACTION_COUNT,
        feature_count=MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT,
        hidden_unit_count=_HIDDEN_UNIT_COUNT,
        action_count=_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        model_seed=_MODEL_SEED,
        epoch_count=MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS,
        learning_rate=_LEARNING_RATE,
        adam_beta1=_ADAM_BETA1,
        adam_beta2=_ADAM_BETA2,
        adam_epsilon=_ADAM_EPSILON,
        train_example_count=int(train_labels.shape[0]),
        eval_example_count=int(eval_labels.shape[0]),
        initial_train_loss=initial_train_loss,
        final_train_loss=final_train_loss,
        initial_eval_loss=initial_eval_loss,
        final_eval_loss=final_eval_loss,
        initial_train_accuracy=initial_train_accuracy,
        final_train_accuracy=final_train_accuracy,
        initial_eval_accuracy=initial_eval_accuracy,
        final_eval_accuracy=final_eval_accuracy,
        pre_update_loss_history=tuple(pre_update_losses),
        parameter_delta_l2=parameter_delta_l2,
        selfplay_round_count=len(MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS),
        selfplay_transition_counts=selfplay_transition_counts,
        selfplay_cumulative_raw_rewards=selfplay_cumulative_rewards,
        selfplay_final_raw_rewards=selfplay_final_rewards,
        selfplay_final_scores=selfplay_final_scores,
        selfplay_nonzero_outcome_seeds=selfplay_nonzero_seeds,
        selfplay_all_actions_legal=True,
        selfplay_all_rounds_terminated=True,
        training_applied=True,
        train_eval_sources_separate=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )
    return jax, jnp, parameters, result


def run_mahjax_categorical_mlp_imitation_training_smoke(
) -> MahJaxCategoricalMlpImitationResult:
    """Train the exact local MLP and return frozen diagnostics only."""

    try:
        _, _, _, result = _train_mahjax_categorical_mlp_parameters()
    except MahJaxCategoricalMlpImitationSmokeError:
        raise
    except Exception as exc:
        raise MahJaxCategoricalMlpImitationSmokeError(
            f"categorical MLP training smoke failed: {exc}"
        ) from exc
    return result


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT",
    "MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS",
    "MahJaxCategoricalMlpImitationSmokeError",
    "MahJaxCategoricalMlpImitationResult",
    "encode_mahjax_categorical_observation",
    "run_mahjax_categorical_mlp_imitation_training_smoke",
]
