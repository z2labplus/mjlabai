"""First environment-backed MahJax rule-policy imitation training smoke.

Two pinned local rounds provide separate in-memory train/evaluation decisions.
The project-owned 630-by-87 linear policy receives exactly sixteen deterministic
full-batch masked-cross-entropy gradient updates. No sample, parameter, or
checkpoint is persisted and the result is not model-strength evidence.
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
    encode_mahjax_public_observation,
)


MAHJAX_IMITATION_TRAINING_SMOKE_VERSION = (
    "p7_p8_mahjax_rule_policy_imitation_training_smoke_v0.1"
)
MAHJAX_IMITATION_TRAIN_SEED = 0
MAHJAX_IMITATION_EVAL_SEED = 1
MAHJAX_IMITATION_MODEL_SEED = 123
MAHJAX_IMITATION_TRAINING_EPOCHS = 16
MAHJAX_IMITATION_LEARNING_RATE = 0.1

_TRANSITION_CAP = 256
_PARAMETER_COUNT = (
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT * MAHJAX_LINEAR_POLICY_ACTION_COUNT
    + MAHJAX_LINEAR_POLICY_ACTION_COUNT
)
_EVIDENCE_GRADE = (
    "P7/P8 local synthetic rule-policy imitation training smoke evidence only"
)
_WARNINGS = (
    "first environment-backed project parameter training smoke only",
    "two pinned local MahJax bundled-rule-policy rounds only",
    "seed 0 train and seed 1 evaluation decisions remain separate in memory",
    "exact 630 public features, 87 legal-masked actions and 54,897 parameters",
    "sixteen deterministic full-batch gradient updates only",
    "no persisted dataset, model weights, checkpoint or artifact",
    "no hidden opponent hand or private environment-state feature",
    "no reward objective, reinforcement-learning update or self-play learning",
    "no real Tenhou, real haifu, external log or platform data",
    "not production training, evaluation, league or candidate promotion",
    "not policy-quality or model-strength evidence",
    "not stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxImitationTrainingSmokeError(RuntimeError):
    """Raised when the exact local imitation-training contract fails."""


@dataclass(frozen=True)
class MahJaxImitationTrainingResult:
    """Immutable diagnostics from the exact bounded training smoke."""

    training_version: str
    package_version: str
    environment_id: str
    environment_version: str
    teacher_policy_id: str
    model_id: str
    train_seed: int
    eval_seed: int
    model_seed: int
    train_example_count: int
    eval_example_count: int
    feature_count: int
    action_count: int
    parameter_count: int
    epoch_count: int
    learning_rate: float
    initial_train_loss: float
    final_train_loss: float
    initial_eval_loss: float
    final_eval_loss: float
    initial_train_accuracy: float
    final_train_accuracy: float
    initial_eval_accuracy: float
    final_eval_accuracy: float
    pre_update_loss_history: Tuple[float, ...]
    weight_delta_l2: float
    bias_delta_l2: float
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
        raise MahJaxImitationTrainingSmokeError(
            "pinned MahJax/JAX imitation-training runtime is unavailable"
        ) from exc
    return jax, jnp, mahjax, rule_based_player


def _collect_decisions(seed, jax, jnp, mahjax, rule_based_player):
    try:
        root_key = jax.random.PRNGKey(seed)
        init_key, policy_key = jax.random.split(root_key)
        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        state = environment.init(init_key)
    except Exception as exc:
        raise MahJaxImitationTrainingSmokeError(
            f"failed to initialize decision source seed {seed}"
        ) from exc

    if (
        environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != MAHJAX_LINEAR_POLICY_ACTION_COUNT
    ):
        raise MahJaxImitationTrainingSmokeError(
            "MahJax decision source identity differs from the pinned contract"
        )

    features = []
    legal_masks = []
    labels = []
    step_fn = jax.jit(environment.step)
    teacher_fn = jax.jit(rule_based_player)
    for transition_index in range(_TRANSITION_CAP):
        if bool(state.terminated) or bool(state.truncated):
            raise MahJaxImitationTrainingSmokeError(
                "decision collection attempted a finished state"
            )
        if int(state.step_count) != transition_index:
            raise MahJaxImitationTrainingSmokeError(
                "decision collection step_count must be monotonic"
            )
        encoded = encode_mahjax_public_observation(environment.observe(state))
        feature_array = jnp.asarray(encoded, dtype=jnp.float32)
        if tuple(feature_array.shape) != (
            MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        ):
            raise MahJaxImitationTrainingSmokeError(
                "encoded decision must contain exactly 630 features"
            )
        mask = state.legal_action_mask
        if str(mask.dtype) != "bool" or tuple(mask.shape) != (
            MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        ):
            raise MahJaxImitationTrainingSmokeError(
                "decision legal mask must be an exact bool 87-vector"
            )
        try:
            policy_key, action_key = jax.random.split(policy_key)
            label = int(teacher_fn(state, action_key))
        except Exception as exc:
            raise MahJaxImitationTrainingSmokeError(
                f"teacher policy failed at seed {seed} transition {transition_index}"
            ) from exc
        if label < 0 or label >= MAHJAX_LINEAR_POLICY_ACTION_COUNT or not bool(
            mask[label]
        ):
            raise MahJaxImitationTrainingSmokeError(
                f"teacher label is illegal at seed {seed} transition {transition_index}"
            )
        features.append(feature_array)
        legal_masks.append(mask)
        labels.append(label)
        try:
            state = jax.block_until_ready(step_fn(state, jnp.int32(label)))
        except Exception as exc:
            raise MahJaxImitationTrainingSmokeError(
                f"decision source step failed at seed {seed} transition {transition_index}"
            ) from exc
        if bool(state.terminated) or bool(state.truncated):
            break
    else:
        raise MahJaxImitationTrainingSmokeError(
            f"decision source seed {seed} exceeded the {_TRANSITION_CAP}-transition cap"
        )

    if not bool(state.terminated) or bool(state.truncated):
        raise MahJaxImitationTrainingSmokeError(
            f"decision source seed {seed} must terminate without truncation"
        )
    return (
        jnp.stack(features),
        jnp.stack(legal_masks),
        jnp.asarray(labels, dtype=jnp.int32),
    )


def _train_mahjax_rule_policy_imitation_parameters():
    """Return initial/trained arrays and diagnostics for in-process smoke use."""

    jax, jnp, mahjax, rule_based_player = _load_pinned_runtime()
    if mahjax.__version__ != _MAHJAX_PACKAGE_VERSION:
        raise MahJaxImitationTrainingSmokeError(
            f"mahjax version must be {_MAHJAX_PACKAGE_VERSION!r}"
        )

    train_features, train_masks, train_labels = _collect_decisions(
        MAHJAX_IMITATION_TRAIN_SEED,
        jax,
        jnp,
        mahjax,
        rule_based_player,
    )
    eval_features, eval_masks, eval_labels = _collect_decisions(
        MAHJAX_IMITATION_EVAL_SEED,
        jax,
        jnp,
        mahjax,
        rule_based_player,
    )
    if int(train_labels.shape[0]) != 54 or int(eval_labels.shape[0]) != 64:
        raise MahJaxImitationTrainingSmokeError(
            "pinned train/evaluation rounds must contain exactly 54/64 examples"
        )

    try:
        model_key = jax.random.PRNGKey(MAHJAX_IMITATION_MODEL_SEED)
        initial_weights = jax.random.normal(
            model_key,
            (
                MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
                MAHJAX_LINEAR_POLICY_ACTION_COUNT,
            ),
            dtype=jnp.float32,
        ) * 0.01
        initial_biases = jnp.zeros(
            (MAHJAX_LINEAR_POLICY_ACTION_COUNT,),
            dtype=jnp.float32,
        )
    except Exception as exc:
        raise MahJaxImitationTrainingSmokeError(
            "failed to initialize project imitation model parameters"
        ) from exc

    def masked_loss(weights, biases, batch_features, batch_masks, batch_labels):
        logits = batch_features @ weights + biases
        masked_logits = jnp.where(batch_masks, logits, -1e9)
        log_probabilities = jax.nn.log_softmax(masked_logits, axis=1)
        return -jnp.mean(
            log_probabilities[
                jnp.arange(batch_labels.shape[0]),
                batch_labels,
            ]
        )

    def exact_accuracy(weights, biases, batch_features, batch_masks, batch_labels):
        logits = batch_features @ weights + biases
        predictions = jnp.argmax(
            jnp.where(batch_masks, logits, -jnp.inf),
            axis=1,
        )
        return jnp.mean(predictions == batch_labels)

    loss_and_gradient = jax.value_and_grad(masked_loss, argnums=(0, 1))

    @jax.jit
    def train_step(weights, biases):
        loss, gradients = loss_and_gradient(
            weights,
            biases,
            train_features,
            train_masks,
            train_labels,
        )
        return (
            weights - MAHJAX_IMITATION_LEARNING_RATE * gradients[0],
            biases - MAHJAX_IMITATION_LEARNING_RATE * gradients[1],
            loss,
        )

    weights = initial_weights
    biases = initial_biases
    initial_train_loss = float(
        masked_loss(weights, biases, train_features, train_masks, train_labels)
    )
    initial_eval_loss = float(
        masked_loss(weights, biases, eval_features, eval_masks, eval_labels)
    )
    initial_train_accuracy = float(
        exact_accuracy(weights, biases, train_features, train_masks, train_labels)
    )
    initial_eval_accuracy = float(
        exact_accuracy(weights, biases, eval_features, eval_masks, eval_labels)
    )
    loss_history = []
    for _ in range(MAHJAX_IMITATION_TRAINING_EPOCHS):
        weights, biases, pre_update_loss = train_step(weights, biases)
        loss_history.append(float(pre_update_loss))

    final_train_loss = float(
        masked_loss(weights, biases, train_features, train_masks, train_labels)
    )
    final_eval_loss = float(
        masked_loss(weights, biases, eval_features, eval_masks, eval_labels)
    )
    final_train_accuracy = float(
        exact_accuracy(weights, biases, train_features, train_masks, train_labels)
    )
    final_eval_accuracy = float(
        exact_accuracy(weights, biases, eval_features, eval_masks, eval_labels)
    )
    weight_delta_l2 = float(jnp.linalg.norm(weights - initial_weights))
    bias_delta_l2 = float(jnp.linalg.norm(biases - initial_biases))

    diagnostics = (
        initial_train_loss,
        final_train_loss,
        initial_eval_loss,
        final_eval_loss,
        initial_train_accuracy,
        final_train_accuracy,
        initial_eval_accuracy,
        final_eval_accuracy,
        weight_delta_l2,
        bias_delta_l2,
    ) + tuple(loss_history)
    if not all(math.isfinite(value) for value in diagnostics):
        raise MahJaxImitationTrainingSmokeError(
            "all imitation-training diagnostics must be finite"
        )
    if not all(
        loss_history[index + 1] < loss_history[index]
        for index in range(len(loss_history) - 1)
    ):
        raise MahJaxImitationTrainingSmokeError(
            "pre-update training loss history must be strictly decreasing"
        )
    if not (
        final_train_loss < initial_train_loss
        and final_eval_loss < initial_eval_loss
        and final_train_accuracy >= initial_train_accuracy
        and final_eval_accuracy >= initial_eval_accuracy
        and weight_delta_l2 > 0.0
        and bias_delta_l2 > 0.0
    ):
        raise MahJaxImitationTrainingSmokeError(
            "training must improve approved loss/accuracy diagnostics and change parameters"
        )

    result = MahJaxImitationTrainingResult(
        training_version=MAHJAX_IMITATION_TRAINING_SMOKE_VERSION,
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        teacher_policy_id="mahjax.red_mahjong.players.rule_based_player@0.1.2",
        model_id="project_linear_630x87_imitation_seed_123",
        train_seed=MAHJAX_IMITATION_TRAIN_SEED,
        eval_seed=MAHJAX_IMITATION_EVAL_SEED,
        model_seed=MAHJAX_IMITATION_MODEL_SEED,
        train_example_count=int(train_labels.shape[0]),
        eval_example_count=int(eval_labels.shape[0]),
        feature_count=MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
        action_count=MAHJAX_LINEAR_POLICY_ACTION_COUNT,
        parameter_count=_PARAMETER_COUNT,
        epoch_count=MAHJAX_IMITATION_TRAINING_EPOCHS,
        learning_rate=MAHJAX_IMITATION_LEARNING_RATE,
        initial_train_loss=initial_train_loss,
        final_train_loss=final_train_loss,
        initial_eval_loss=initial_eval_loss,
        final_eval_loss=final_eval_loss,
        initial_train_accuracy=initial_train_accuracy,
        final_train_accuracy=final_train_accuracy,
        initial_eval_accuracy=initial_eval_accuracy,
        final_eval_accuracy=final_eval_accuracy,
        pre_update_loss_history=tuple(loss_history),
        weight_delta_l2=weight_delta_l2,
        bias_delta_l2=bias_delta_l2,
        training_applied=True,
        train_eval_sources_separate=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )
    return initial_weights, initial_biases, weights, biases, result


def run_mahjax_rule_policy_imitation_training_smoke(
) -> MahJaxImitationTrainingResult:
    """Collect two local rounds and apply sixteen full-batch gradient steps."""

    _, _, _, _, result = _train_mahjax_rule_policy_imitation_parameters()
    return result


__all__ = [
    "MAHJAX_IMITATION_TRAINING_SMOKE_VERSION",
    "MAHJAX_IMITATION_TRAIN_SEED",
    "MAHJAX_IMITATION_EVAL_SEED",
    "MAHJAX_IMITATION_MODEL_SEED",
    "MAHJAX_IMITATION_TRAINING_EPOCHS",
    "MAHJAX_IMITATION_LEARNING_RATE",
    "MahJaxImitationTrainingSmokeError",
    "MahJaxImitationTrainingResult",
    "run_mahjax_rule_policy_imitation_training_smoke",
]
