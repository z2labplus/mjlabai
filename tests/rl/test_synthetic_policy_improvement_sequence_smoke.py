from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, asdict, fields, replace
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.synthetic_policy_improvement_sequence_smoke as sequence_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS,
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION,
    SyntheticLinearActionValueModel,
    SyntheticLinearDecisionProbe,
    SyntheticLinearQTransition,
    SyntheticPolicyImprovementSequenceResult,
    SyntheticPolicyImprovementSequenceSmokeError,
    SyntheticPolicyImprovementStepInput,
    run_synthetic_one_step_policy_improvement_smoke,
    run_synthetic_policy_improvement_sequence_smoke,
)


def _model(selected_action: int = 0) -> SyntheticLinearActionValueModel:
    biases = (0.2, 0.0) if selected_action == 0 else (0.0, 0.2)
    return SyntheticLinearActionValueModel(
        weights=((0.0, 0.0), (0.0, 0.0)),
        biases=biases,
    )


def _probe(index: int, features: tuple[float, float]) -> SyntheticLinearDecisionProbe:
    return SyntheticLinearDecisionProbe(
        probe_id=f"sequence-probe:{index}",
        source_kind=SYNTHETIC_LOCAL_SOURCE_KIND,
        features=features,
        legal_action_indices=(0, 1),
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
        uses_model_output=False,
        uses_self_play=False,
    )


def _probes() -> tuple[
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
]:
    return (
        _probe(1, (1.0, 0.0)),
        _probe(2, (0.0, 1.0)),
        _probe(3, (0.0, 0.0)),
    )


def _transition(
    step_index: int,
    batch_index: int,
    record_index: int,
    *,
    action_index: int,
    state_features: tuple[float, float],
    reward: float,
) -> SyntheticLinearQTransition:
    return SyntheticLinearQTransition(
        record_id=f"sequence-step{step_index}-batch{batch_index}:{record_index}",
        source_kind=SYNTHETIC_LOCAL_SOURCE_KIND,
        state_features=state_features,
        action_index=action_index,
        reward=reward,
        next_state_features=None,
        terminal=True,
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
        uses_model_output=False,
        uses_self_play=False,
    )


def _batches(step_index: int) -> tuple[
    tuple[
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
    ],
    tuple[
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
    ],
]:
    return (
        (
            _transition(step_index, 0, 1, action_index=0, state_features=(1.0, 0.0), reward=-1.0),
            _transition(step_index, 0, 2, action_index=1, state_features=(1.0, 0.0), reward=2.0),
            _transition(step_index, 0, 3, action_index=0, state_features=(0.0, 0.0), reward=0.0),
            _transition(step_index, 0, 4, action_index=1, state_features=(0.0, 0.0), reward=0.0),
        ),
        (
            _transition(step_index, 1, 1, action_index=1, state_features=(1.0, 0.0), reward=-1.0),
            _transition(step_index, 1, 2, action_index=0, state_features=(1.0, 0.0), reward=2.0),
            _transition(step_index, 1, 3, action_index=1, state_features=(0.0, 0.0), reward=0.0),
            _transition(step_index, 1, 4, action_index=0, state_features=(0.0, 0.0), reward=0.0),
        ),
    )


def _step(step_index: int) -> SyntheticPolicyImprovementStepInput:
    return SyntheticPolicyImprovementStepInput(
        step_id=f"sequence-step:{step_index}",
        decision_probes=_probes(),
        candidate_transition_batches=_batches(step_index),
        learning_rate=0.5,
        discount_factor=0.5,
    )


def _run(step_count: int = 2) -> SyntheticPolicyImprovementSequenceResult:
    return run_synthetic_policy_improvement_sequence_smoke(
        _model(),
        tuple(_step(index) for index in range(1, step_count + 1)),
    )


class SyntheticPolicyImprovementSequenceSmokeTests(unittest.TestCase):
    def test_one_step_matches_reviewed_one_step_output(self) -> None:
        step = _step(1)
        expected = run_synthetic_one_step_policy_improvement_smoke(
            _model(),
            step.decision_probes,
            step.candidate_transition_batches,
            learning_rate=step.learning_rate,
            discount_factor=step.discount_factor,
        )
        result = run_synthetic_policy_improvement_sequence_smoke(_model(), (step,))

        self.assertEqual(result.step_results, (expected,))
        self.assertEqual(result.initial_model, expected.initial_model)
        self.assertEqual(result.final_model, expected.training_result.final_model)
        self.assertEqual(result.selected_actions, (0,))
        self.assertEqual(result.after_actions, (1,))

    def test_two_steps_carry_model_and_actions_in_order(self) -> None:
        result = _run(2)

        self.assertEqual(result.selected_actions, (0, 1))
        self.assertEqual(result.after_actions, (1, 0))
        self.assertEqual(
            result.step_results[1].initial_model,
            result.step_results[0].training_result.final_model,
        )
        self.assertEqual(
            result.final_model,
            result.step_results[1].training_result.final_model,
        )

    def test_hard_step_limits_and_exact_outer_tuple(self) -> None:
        class TupleSubclass(tuple):
            pass

        for invalid in ((), tuple(_step(i) for i in range(1, 6))):
            with self.assertRaisesRegex(
                SyntheticPolicyImprovementSequenceSmokeError,
                "1 through 4",
            ):
                run_synthetic_policy_improvement_sequence_smoke(_model(), invalid)
        for invalid in ([_step(1)], TupleSubclass((_step(1),))):
            with self.assertRaisesRegex(
                SyntheticPolicyImprovementSequenceSmokeError,
                "exact tuple",
            ):
                run_synthetic_policy_improvement_sequence_smoke(  # type: ignore[arg-type]
                    _model(), invalid
                )

        result = _run(4)
        self.assertEqual(result.step_count, 4)
        self.assertEqual(result.max_steps, 4)
        self.assertEqual(result.selected_actions, (0, 1, 0, 1))

    def test_requires_exact_frozen_steps_and_distinct_nonempty_ids(self) -> None:
        class StepSubclass(SyntheticPolicyImprovementStepInput):
            pass

        step = _step(1)
        subclass = StepSubclass(**asdict(step))
        with self.assertRaisesRegex(
            SyntheticPolicyImprovementSequenceSmokeError,
            "exact SyntheticPolicyImprovementStepInput",
        ):
            run_synthetic_policy_improvement_sequence_smoke(_model(), (subclass,))
        for invalid_id in ("", "   ", 1):
            with self.assertRaisesRegex(
                SyntheticPolicyImprovementSequenceSmokeError,
                "non-empty string",
            ):
                run_synthetic_policy_improvement_sequence_smoke(
                    _model(),
                    (replace(step, step_id=invalid_id),),  # type: ignore[arg-type]
                )
        with self.assertRaisesRegex(
            SyntheticPolicyImprovementSequenceSmokeError,
            "pairwise distinct",
        ):
            run_synthetic_policy_improvement_sequence_smoke(
                _model(),
                (step, replace(_step(2), step_id=step.step_id)),
            )
        with self.assertRaises(FrozenInstanceError):
            step.step_id = "changed"  # type: ignore[misc]

    def test_rejects_global_candidate_transition_id_reuse(self) -> None:
        first = _step(1)
        second = _step(2)
        batches = second.candidate_transition_batches
        duplicate = replace(
            batches[1][3],
            record_id=first.candidate_transition_batches[0][0].record_id,
        )
        second = replace(
            second,
            candidate_transition_batches=(
                batches[0],
                batches[1][:3] + (duplicate,),
            ),
        )

        with self.assertRaisesRegex(
            SyntheticPolicyImprovementSequenceSmokeError,
            "globally pairwise distinct",
        ):
            run_synthetic_policy_improvement_sequence_smoke(
                _model(), (first, second)
            )

    def test_calls_reviewed_helper_once_per_step_with_model_continuity(self) -> None:
        real_helper = sequence_module.run_synthetic_one_step_policy_improvement_smoke
        with patch.object(
            sequence_module,
            "run_synthetic_one_step_policy_improvement_smoke",
            wraps=real_helper,
        ) as helper:
            result = _run(3)

        self.assertEqual(helper.call_count, 3)
        self.assertEqual(helper.call_args_list[0].args[0], result.initial_model)
        self.assertEqual(
            helper.call_args_list[1].args[0],
            result.step_results[0].training_result.final_model,
        )
        self.assertEqual(
            helper.call_args_list[2].args[0],
            result.step_results[1].training_result.final_model,
        )

    def test_wraps_candidate_and_one_step_errors_with_index_and_cause(self) -> None:
        malformed = replace(
            _step(1),
            candidate_transition_batches=(_batches(1)[0],),  # type: ignore[arg-type]
        )
        with self.assertRaisesRegex(
            SyntheticPolicyImprovementSequenceSmokeError,
            "step 1 failed",
        ) as candidate_context:
            run_synthetic_policy_improvement_sequence_smoke(_model(), (malformed,))
        self.assertIsNotNone(candidate_context.exception.__cause__)

        invalid_second = replace(_step(2), learning_rate=0.0)
        with self.assertRaisesRegex(
            SyntheticPolicyImprovementSequenceSmokeError,
            "step 2 failed",
        ) as helper_context:
            run_synthetic_policy_improvement_sequence_smoke(
                _model(), (_step(1), invalid_second)
            )
        self.assertIsNotNone(helper_context.exception.__cause__)

    def test_is_deterministic_immutable_and_does_not_mutate_inputs(self) -> None:
        model = _model()
        steps = (_step(1), _step(2))
        before_model = asdict(model)
        before_steps = tuple(asdict(step) for step in steps)

        first = run_synthetic_policy_improvement_sequence_smoke(model, steps)
        second = run_synthetic_policy_improvement_sequence_smoke(model, steps)

        self.assertEqual(first, second)
        self.assertEqual(asdict(model), before_model)
        self.assertEqual(tuple(asdict(step) for step in steps), before_steps)
        with self.assertRaises(FrozenInstanceError):
            first.step_count = 3  # type: ignore[misc]

    def test_result_has_exact_fields_ids_grade_and_warnings(self) -> None:
        result = _run(2)

        self.assertEqual(
            {field.name for field in fields(result)},
            {
                "sequence_version",
                "step_count",
                "max_steps",
                "initial_model",
                "final_model",
                "step_ids",
                "step_results",
                "selected_actions",
                "after_actions",
                "global_candidate_transition_record_ids",
                "sequence_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.sequence_version,
            SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION,
        )
        self.assertEqual(result.max_steps, MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS)
        self.assertEqual(result.step_ids, ("sequence-step:1", "sequence-step:2"))
        self.assertEqual(len(result.global_candidate_transition_record_ids), 16)
        self.assertEqual(len(set(result.global_candidate_transition_record_ids)), 16)
        self.assertTrue(result.sequence_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        self.assertEqual(
            result.evidence_grade,
            "P8 exact bounded synthetic/local policy-improvement sequence smoke evidence only",
        )
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "bounded synthetic/local policy-improvement sequence smoke only",
            "maximum four steps",
            "one reviewed closed-loop call per step",
            "no general environment, episode, replay buffer or self-play",
            "no model loading, persistence, checkpoint or external dependency",
            "not production training, inference or evaluation",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_surface_reuses_one_step_without_copied_logic(self) -> None:
        self.assertIs(
            run_synthetic_policy_improvement_sequence_smoke,
            sequence_module.run_synthetic_policy_improvement_sequence_smoke,
        )
        self.assertEqual(
            set(sequence_module.__all__),
            {
                "SYNTHETIC_POLICY_IMPROVEMENT_SEQUENCE_SMOKE_VERSION",
                "MAX_SYNTHETIC_POLICY_IMPROVEMENT_STEPS",
                "SyntheticPolicyImprovementStepInput",
                "SyntheticPolicyImprovementSequenceSmokeError",
                "SyntheticPolicyImprovementSequenceResult",
                "run_synthetic_policy_improvement_sequence_smoke",
            },
        )
        source = inspect.getsource(sequence_module)
        self.assertEqual(source.count("run_synthetic_one_step_policy_improvement_smoke("), 1)
        syntax_tree = ast.parse(source)
        self.assertEqual(
            sum(isinstance(node, ast.For) for node in ast.walk(syntax_tree)),
            1,
        )
        for forbidden in (
            "target - prediction",
            "weights[action_index]",
            "action_one_value > action_zero_value",
            "while ",
            "random.",
        ):
            self.assertNotIn(forbidden, source)
        public_text = " ".join(sequence_module.__all__).lower()
        for forbidden in (
            "path",
            "file",
            "loader",
            "persistence",
            "environment",
            "replay",
            "self_play",
            "checkpoint",
            "evaluation",
        ):
            self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
