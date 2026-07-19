"""Compare outcome-selected and contiguous MahJax training seed protocols.

This bounded diagnostic starts two branches from identical reviewed imitation
parameters, attempts five reviewed raw-return updates per branch, and evaluates
both without updates on the same fixed seeds. It selects no seed protocol.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
from typing import Optional, Tuple

from mjlabai.environment.mahjax_integration_smoke import (
    MAHJAX_ENVIRONMENT_ID as _MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION as _MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_PACKAGE_VERSION as _MAHJAX_PACKAGE_VERSION,
)
from mjlabai.rl.mahjax_categorical_mlp_all_project_policy_gradient_smoke import (
    _apply_actor_indexed_raw_outcome_update,
    _collect_all_project_round,
    _load_pinned_runtime,
)
from mjlabai.rl.mahjax_categorical_mlp_learning_rate_comparison_smoke import (
    MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS,
    _evaluate_parameters,
)
from mjlabai.supervised.mahjax_categorical_mlp_imitation_training_smoke import (
    _train_mahjax_categorical_mlp_parameters,
)


MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_PROTOCOL_COMPARISON_SMOKE_VERSION = (
    "p8_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke_v0.1"
)
MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS = (1, 3, 5, 7, 11)
MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS = (0, 1, 2, 3, 4)
MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS = (
    MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS
)

_OUTCOME_SELECTED_PROTOCOL_ID = "outcome_selected_1_3_5_7_11"
_CONTIGUOUS_PROTOCOL_ID = "contiguous_0_through_4"
_EXPECTED_TRAINING_ROWS = {
    _OUTCOME_SELECTED_PROTOCOL_ID: (
        (1, 77, (-20.0, 70.0, -20.0, -30.0), (230, 320, 230, 220), "9d9bc93cc2e85086797fde119070da58159ba3541d234fbcf3e833d7ac1122cf", "195406fbd7736f7e6b639721c25063ad044e10f866bc65e4472ac4a33082fac3", 0.0936663598, 0.0930117071, (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356)),
        (3, 84, (-10.0, -10.0, 20.0, -10.0), (240, 240, 270, 240), "8e0216f01b24fa50991f1c028807d1fb265da714e5bc97ecb35b08ffb4a73a19", "0ce709006cfa73f6b7d0c83efea8b9ae35bd90ac51e5395bf66ff317910293af", -0.0553588867, -0.0554395691, (0.0002636357, 0.0000601950, 0.0008506179, 0.0000944084)),
        (5, 83, (20.0, -10.0, -10.0, -10.0), (270, 240, 240, 240), "6e9bfaa0785a543f23597d5747309ec49c68d190f16c7b104bb815fa63c0a9f0", "7b6ae19ce96ca946a22434ec8e24a43e50169803e7d4d8f8a8d7fd6741da0528", -0.0609763190, -0.0609965809, (0.0002007297, 0.0000233677, 0.0003997849, 0.0000430078)),
        (7, 81, (0.0, 0.0, -120.0, 120.0), (250, 250, 130, 370), "9f0dc1b42804ad209983a546f4d0a4a3acbd3adb3c4609c81286af54c8572c03", "fbed420400008f45b24a17533a8f0066f35952fc00efbaec9c9bd77c0f6b8462", -0.0202308446, -0.0218939111, (0.0016294104, 0.0002862717, 0.0037121067, 0.0003829675)),
        (11, 84, (-10.0, 20.0, -10.0, -10.0), (240, 270, 240, 240), "7d0f0960b0864162ab54d7d5d0402843ab977c064ecdf78d5ae90e2e0409c6ad", "8c00f6c294a985134dc40505fb2803c50299dd6e7ac803d4b35d770dd618a005", -0.0131035689, -0.0133588845, (0.0004151060, 0.0001173344, 0.0015263907, 0.0001777170)),
    ),
    _CONTIGUOUS_PROTOCOL_ID: (
        (0, 92, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "3915fd25d6b10919794ca0e7ff0052b53923c18a8398098ac31dd8961e5337ad", "37ddd6e0e0fe7f4c3dced43ed3355a2c6c77710a6ba68a44ec6a36613334cb28", 0.0, 0.0, (0.0, 0.0, 0.0, 0.0)),
        (1, 77, (-20.0, 70.0, -20.0, -30.0), (230, 320, 230, 220), "9d9bc93cc2e85086797fde119070da58159ba3541d234fbcf3e833d7ac1122cf", "195406fbd7736f7e6b639721c25063ad044e10f866bc65e4472ac4a33082fac3", 0.0936663598, 0.0930117071, (0.0009705852, 0.0001615889, 0.0023494314, 0.0002528356)),
        (2, 90, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "11e4029e2fd4841f40ceb22700a346a2b6357c97b068c6a7397c366aad15c961", "38f513127cf1b4192682ca7b7a7b1255704d0e28d692607cd42edabdab1915e4", 0.0, 0.0, (0.0, 0.0, 0.0, 0.0)),
        (3, 84, (-10.0, -10.0, 20.0, -10.0), (240, 240, 270, 240), "8e0216f01b24fa50991f1c028807d1fb265da714e5bc97ecb35b08ffb4a73a19", "0ce709006cfa73f6b7d0c83efea8b9ae35bd90ac51e5395bf66ff317910293af", -0.0553588867, -0.0554395691, (0.0002636357, 0.0000601950, 0.0008506179, 0.0000944084)),
        (4, 84, (0.0, 0.0, 0.0, 0.0), (250, 250, 250, 250), "a5b5ddea976ade42e831951e55feddcbf54273a4ee395ad273f728162a6e44b9", "78dc2869b7b23922cbfaf0e3e79e0e4da4cc23afc468795fa79a936e01804cdd", 0.0, 0.0, (0.0, 0.0, 0.0, 0.0)),
    ),
}
_EXPECTED_FINAL_DELTAS = {
    _OUTCOME_SELECTED_PROTOCOL_ID: (
        0.0021020556,
        0.0004550584,
        0.0053585209,
        0.0005585462,
    ),
    _CONTIGUOUS_PROTOCOL_ID: (
        0.0010158311,
        0.0001864599,
        0.0025688238,
        0.0002769242,
    ),
}
_EXPECTED_INITIAL_AND_CONTIGUOUS_REWARDS = (
    0.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
    -15.0, 0.0, -180.0, 0.0, 74.0, 0.0, -40.0, 0.0,
    -15.0, 0.0, -20.0, 0.0, 0.0, -39.0, -15.0, 0.0,
    -15.0, 0.0, 0.0, -10.0, -15.0, -52.0, 0.0, 0.0,
)
_EXPECTED_SELECTED_REWARDS = (
    0.0, -39.0, -10.0, 0.0, -15.0, -15.0, 0.0, -80.0,
    -15.0, 0.0, -180.0, 0.0, -60.0, 0.0, -40.0, 0.0,
    -15.0, 0.0, -20.0, 0.0, 0.0, -39.0, -15.0, -15.0,
    -15.0, 0.0, 0.0, -10.0, -15.0, -52.0, 0.0, 0.0,
)
_EVIDENCE_GRADE = (
    "P8 local training-seed outcome-selection-bias comparison evidence only"
)
_WARNINGS = (
    "exact outcome-selected versus contiguous training-seed diagnostic only",
    "both branches start from identical reviewed imitation parameters",
    "all five predeclared records remain in each protocol without filtering",
    "zero-return seeds 0, 2 and 4 are retained as exact no-op update attempts",
    "fixed evaluation seeds 20 through 51 perform zero updates",
    "contiguous behavior identity is not protocol superiority or selection",
    "no third protocol, seed search, replacement sampling or adaptive choice",
    "no persistence, checkpoint, artifact, external or real data",
    "not improvement, policy-quality, model-strength or promotion evidence",
    "not Tenhou, stable-dan or LuckyJ 10.68 comparison",
)


class MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(RuntimeError):
    """Raised when the exact training-seed comparison contract fails."""


@dataclass(frozen=True)
class MahJaxCategoricalMlpTrainingSeedProtocolBranchResult:
    protocol_id: str
    training_seeds: Tuple[int, ...]
    update_attempt_count: int
    nonzero_update_count: int
    zero_return_noop_seeds: Tuple[int, ...]
    training_transition_counts: Tuple[int, ...]
    training_actor_traces: Tuple[Tuple[int, ...], ...]
    training_action_traces: Tuple[Tuple[int, ...], ...]
    training_legal_action_traces: Tuple[Tuple[Tuple[int, ...], ...], ...]
    training_cumulative_raw_rewards: Tuple[Tuple[float, ...], ...]
    training_final_scores: Tuple[Tuple[int, ...], ...]
    training_action_trace_sha256: Tuple[str, ...]
    training_actor_trace_sha256: Tuple[str, ...]
    initial_objectives: Tuple[float, ...]
    post_update_objectives: Tuple[float, ...]
    per_attempt_parameter_delta_l2: Tuple[Tuple[float, ...], ...]
    final_parameter_delta_l2: Tuple[float, ...]
    evaluation_transition_counts: Tuple[int, ...]
    evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    evaluation_project_raw_rewards: Tuple[float, ...]
    evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    project_raw_sum: float
    positive_round_count: int
    negative_round_count: int
    changed_from_initial_evaluation_seeds: Tuple[int, ...]
    all_actions_legal: bool
    all_rounds_terminated: bool


@dataclass(frozen=True)
class MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult:
    smoke_version: str
    package_version: str
    environment_id: str
    environment_version: str
    evaluation_seeds: Tuple[int, ...]
    initial_evaluation_transition_counts: Tuple[int, ...]
    initial_evaluation_project_action_traces: Tuple[Tuple[int, ...], ...]
    initial_evaluation_project_raw_rewards: Tuple[float, ...]
    initial_evaluation_final_scores: Tuple[Tuple[int, ...], ...]
    initial_project_raw_sum: float
    branches: Tuple[MahJaxCategoricalMlpTrainingSeedProtocolBranchResult, ...]
    branch_initial_parameters_identical: bool
    branch_final_parameters_distinct: bool
    evaluation_update_count: int
    selected_protocol_id: Optional[str]
    selection_bias_effect_observed: bool
    safety_guardrails_all_satisfied: bool
    evidence_grade: str
    warnings: Tuple[str, ...]


def _trace_sha256(trace: Tuple[int, ...]) -> str:
    return hashlib.sha256(",".join(map(str, trace)).encode("ascii")).hexdigest()


def _close(actual: float, expected: float, tolerance: float = 1e-5) -> bool:
    return math.isfinite(actual) and abs(actual - expected) <= tolerance


def _run_protocol_branch(
    protocol_id,
    seeds,
    initial_parameters,
    initial_evaluation,
    environment,
    step_fn,
    rule_policy_fn,
    jax,
    jnp,
    mahjax,
):
    parameters = tuple(initial_parameters)
    trajectories = []
    updates = []
    noop_seeds = []
    for seed in seeds:
        trajectory = _collect_all_project_round(seed, parameters, jax, jnp, mahjax)
        before = tuple(parameters)
        update = _apply_actor_indexed_raw_outcome_update(
            parameters,
            trajectory,
            jax,
            jnp,
        )
        is_zero_return = all(value == 0.0 for value in trajectory.cumulative_rewards)
        unchanged = all(
            bool(jnp.array_equal(left, right))
            for left, right in zip(before, update.parameters)
        )
        if is_zero_return:
            noop_seeds.append(seed)
            if not unchanged or any(value != 0.0 for value in update.parameter_delta_l2):
                raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
                    f"protocol {protocol_id} zero-return seed {seed} was not a no-op"
                )
        trajectories.append(trajectory)
        updates.append(update)
        parameters = update.parameters

    observed_rows = tuple(
        (
            seed,
            len(trajectory.action_trace),
            trajectory.cumulative_rewards,
            trajectory.final_scores,
            _trace_sha256(trajectory.action_trace),
            _trace_sha256(trajectory.actor_trace),
            update.initial_objective,
            update.post_update_objective,
            update.parameter_delta_l2,
        )
        for seed, trajectory, update in zip(seeds, trajectories, updates)
    )
    expected_rows = _EXPECTED_TRAINING_ROWS[protocol_id]
    rows_match = all(
        observed[:6] == expected[:6]
        and _close(observed[6], expected[6])
        and _close(observed[7], expected[7])
        and all(_close(a, b) for a, b in zip(observed[8], expected[8]))
        for observed, expected in zip(observed_rows, expected_rows)
    )
    final_deltas = tuple(
        float(jnp.linalg.norm(final - initial))
        for initial, final in zip(initial_parameters, parameters)
    )
    if not rows_match or not all(
        _close(actual, expected)
        for actual, expected in zip(final_deltas, _EXPECTED_FINAL_DELTAS[protocol_id])
    ):
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            f"protocol {protocol_id} training differs from the approved probe"
        )

    evaluation = _evaluate_parameters(
        parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
    )
    evaluation_rewards = tuple(item.project_cumulative_raw_reward for item in evaluation)
    changed_seeds = tuple(
        seed
        for seed, before, after in zip(
            MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS,
            initial_evaluation,
            evaluation,
        )
        if before != after
    )
    expected_rewards = (
        _EXPECTED_SELECTED_REWARDS
        if protocol_id == _OUTCOME_SELECTED_PROTOCOL_ID
        else _EXPECTED_INITIAL_AND_CONTIGUOUS_REWARDS
    )
    expected_changed = (
        (32, 39, 43, 44, 50)
        if protocol_id == _OUTCOME_SELECTED_PROTOCOL_ID
        else ()
    )
    if evaluation_rewards != expected_rewards or changed_seeds != expected_changed:
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            f"protocol {protocol_id} fixed evaluation differs from the approved probe"
        )

    return parameters, MahJaxCategoricalMlpTrainingSeedProtocolBranchResult(
        protocol_id=protocol_id,
        training_seeds=seeds,
        update_attempt_count=len(updates),
        nonzero_update_count=len(updates) - len(noop_seeds),
        zero_return_noop_seeds=tuple(noop_seeds),
        training_transition_counts=tuple(len(item.action_trace) for item in trajectories),
        training_actor_traces=tuple(item.actor_trace for item in trajectories),
        training_action_traces=tuple(item.action_trace for item in trajectories),
        training_legal_action_traces=tuple(item.legal_action_trace for item in trajectories),
        training_cumulative_raw_rewards=tuple(item.cumulative_rewards for item in trajectories),
        training_final_scores=tuple(item.final_scores for item in trajectories),
        training_action_trace_sha256=tuple(_trace_sha256(item.action_trace) for item in trajectories),
        training_actor_trace_sha256=tuple(_trace_sha256(item.actor_trace) for item in trajectories),
        initial_objectives=tuple(item.initial_objective for item in updates),
        post_update_objectives=tuple(item.post_update_objective for item in updates),
        per_attempt_parameter_delta_l2=tuple(item.parameter_delta_l2 for item in updates),
        final_parameter_delta_l2=final_deltas,
        evaluation_transition_counts=tuple(item.transition_count for item in evaluation),
        evaluation_project_action_traces=tuple(item.project_action_trace for item in evaluation),
        evaluation_project_raw_rewards=evaluation_rewards,
        evaluation_final_scores=tuple(item.final_scores for item in evaluation),
        project_raw_sum=sum(evaluation_rewards),
        positive_round_count=sum(value > 0.0 for value in evaluation_rewards),
        negative_round_count=sum(value < 0.0 for value in evaluation_rewards),
        changed_from_initial_evaluation_seeds=changed_seeds,
        all_actions_legal=True,
        all_rounds_terminated=True,
    )


def run_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke(
) -> MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult:
    """Run the exact selected-versus-contiguous seed protocol comparison."""

    try:
        jax, jnp, initial_parameters, _ = _train_mahjax_categorical_mlp_parameters()
    except Exception as exc:
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            "reviewed categorical MLP in-memory training failed"
        ) from exc
    try:
        _, _, mahjax = _load_pinned_runtime()
        from mahjax.red_mahjong.players import rule_based_player

        environment = mahjax.make(
            _MAHJAX_ENVIRONMENT_ID,
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        step_fn = jax.jit(environment.step)
        rule_policy_fn = jax.jit(rule_based_player)
    except Exception as exc:
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            "pinned MahJax/JAX seed-protocol runtime is unavailable"
        ) from exc
    if (
        mahjax.__version__ != _MAHJAX_PACKAGE_VERSION
        or environment.id != _MAHJAX_ENVIRONMENT_ID
        or environment.version != _MAHJAX_ENVIRONMENT_VERSION
        or environment.num_players != 4
        or environment.num_actions != 87
    ):
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            "seed-protocol runtime differs from the pinned contract"
        )

    initial_evaluation = _evaluate_parameters(
        initial_parameters,
        environment,
        step_fn,
        rule_policy_fn,
        jax,
        jnp,
    )
    initial_rewards = tuple(
        item.project_cumulative_raw_reward for item in initial_evaluation
    )
    if (
        initial_rewards != _EXPECTED_INITIAL_AND_CONTIGUOUS_REWARDS
        or sum(initial_rewards) != -501.0
    ):
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            "initial fixed evaluation differs from the approved probe"
        )

    branch_inputs = (
        (
            _OUTCOME_SELECTED_PROTOCOL_ID,
            MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS,
        ),
        (
            _CONTIGUOUS_PROTOCOL_ID,
            MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS,
        ),
    )
    branch_initials = tuple(tuple(initial_parameters) for _ in branch_inputs)
    initial_identical = all(
        all(bool(jnp.array_equal(a, b)) for a, b in zip(initial_parameters, branch))
        for branch in branch_initials
    )
    final_parameters = []
    branch_results = []
    for (protocol_id, seeds), branch_initial in zip(branch_inputs, branch_initials):
        try:
            parameters, branch_result = _run_protocol_branch(
                protocol_id,
                seeds,
                branch_initial,
                initial_evaluation,
                environment,
                step_fn,
                rule_policy_fn,
                jax,
                jnp,
                mahjax,
            )
        except Exception as exc:
            if isinstance(
                exc,
                MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError,
            ):
                raise
            raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
                f"protocol {protocol_id} branch failed"
            ) from exc
        final_parameters.append(parameters)
        branch_results.append(branch_result)

    final_distinct = any(
        not bool(jnp.array_equal(left, right))
        for left, right in zip(final_parameters[0], final_parameters[1])
    )
    observed_sums = tuple(item.project_raw_sum for item in branch_results)
    if (
        not initial_identical
        or not final_distinct
        or observed_sums != (-650.0, -501.0)
        or branch_results[0].positive_round_count != 0
        or branch_results[0].negative_round_count != 18
        or branch_results[1].positive_round_count != 1
        or branch_results[1].negative_round_count != 16
    ):
        raise MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError(
            "training-seed protocol comparison invariants were not demonstrated"
        )

    return MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult(
        smoke_version=(
            MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_PROTOCOL_COMPARISON_SMOKE_VERSION
        ),
        package_version=_MAHJAX_PACKAGE_VERSION,
        environment_id=_MAHJAX_ENVIRONMENT_ID,
        environment_version=_MAHJAX_ENVIRONMENT_VERSION,
        evaluation_seeds=(
            MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS
        ),
        initial_evaluation_transition_counts=tuple(
            item.transition_count for item in initial_evaluation
        ),
        initial_evaluation_project_action_traces=tuple(
            item.project_action_trace for item in initial_evaluation
        ),
        initial_evaluation_project_raw_rewards=initial_rewards,
        initial_evaluation_final_scores=tuple(
            item.final_scores for item in initial_evaluation
        ),
        initial_project_raw_sum=sum(initial_rewards),
        branches=tuple(branch_results),
        branch_initial_parameters_identical=initial_identical,
        branch_final_parameters_distinct=final_distinct,
        evaluation_update_count=0,
        selected_protocol_id=None,
        selection_bias_effect_observed=True,
        safety_guardrails_all_satisfied=True,
        evidence_grade=_EVIDENCE_GRADE,
        warnings=_WARNINGS,
    )


__all__ = [
    "MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_PROTOCOL_COMPARISON_SMOKE_VERSION",
    "MAHJAX_CATEGORICAL_MLP_OUTCOME_SELECTED_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_CONTIGUOUS_TRAINING_SEEDS",
    "MAHJAX_CATEGORICAL_MLP_TRAINING_SEED_COMPARISON_EVALUATION_SEEDS",
    "MahJaxCategoricalMlpTrainingSeedProtocolComparisonSmokeError",
    "MahJaxCategoricalMlpTrainingSeedProtocolBranchResult",
    "MahJaxCategoricalMlpTrainingSeedProtocolComparisonResult",
    "run_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke",
]
