from __future__ import annotations

from dataclasses import FrozenInstanceError, asdict, replace
import inspect
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.synthetic_one_step_policy_improvement_smoke as loop_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION,
    SyntheticLinearActionValueModel,
    SyntheticLinearDecisionProbe,
    SyntheticLinearGreedyDecisionSmokeError,
    SyntheticLinearQTransition,
    SyntheticOneStepPolicyImprovementResult,
    SyntheticOneStepPolicyImprovementSmokeError,
    run_synthetic_one_step_policy_improvement_smoke,
)


def _model(selected_action: int = 0) -> SyntheticLinearActionValueModel:
    biases = (0.2, 0.0) if selected_action == 0 else (0.0, 0.2)
    return SyntheticLinearActionValueModel(
        weights=((0.0, 0.0), (0.0, 0.0)),
        biases=biases,
    )


def _probe(index: int, features: tuple[float, float]) -> SyntheticLinearDecisionProbe:
    return SyntheticLinearDecisionProbe(
        probe_id=f"loop-probe:{index}",
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
    batch_index: int,
    record_index: int,
    *,
    action_index: int,
    state_features: tuple[float, float],
    reward: float,
) -> SyntheticLinearQTransition:
    return SyntheticLinearQTransition(
        record_id=f"loop-batch{batch_index}:{record_index}",
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


def _batches() -> tuple[
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
    batch_zero = (
        _transition(0, 1, action_index=0, state_features=(1.0, 0.0), reward=-1.0),
        _transition(0, 2, action_index=1, state_features=(1.0, 0.0), reward=2.0),
        _transition(0, 3, action_index=0, state_features=(0.0, 0.0), reward=0.0),
        _transition(0, 4, action_index=1, state_features=(0.0, 0.0), reward=0.0),
    )
    batch_one = (
        _transition(1, 1, action_index=1, state_features=(1.0, 0.0), reward=-1.0),
        _transition(1, 2, action_index=0, state_features=(1.0, 0.0), reward=2.0),
        _transition(1, 3, action_index=1, state_features=(0.0, 0.0), reward=0.0),
        _transition(1, 4, action_index=0, state_features=(0.0, 0.0), reward=0.0),
    )
    return (batch_zero, batch_one)


def _run(selected_action: int = 0) -> SyntheticOneStepPolicyImprovementResult:
    return run_synthetic_one_step_policy_improvement_smoke(
        _model(selected_action),
        _probes(),
        _batches(),
        learning_rate=0.5,
        discount_factor=0.5,
    )


class SyntheticOneStepPolicyImprovementSmokeTests(unittest.TestCase):
    def test_action_zero_selects_only_batch_zero_and_changes_to_one(self) -> None:
        result = _run(0)

        self.assertEqual(result.selected_action_index, 0)
        self.assertEqual(result.after_selected_action_index, 1)
        self.assertTrue(result.controlled_action_changed)
        self.assertEqual(
            result.selected_transition_record_ids,
            tuple(record.record_id for record in _batches()[0]),
        )
        self.assertEqual(result.training_result.epoch_count, 1)
        self.assertEqual(result.training_result.update_count, 4)
        self.assertEqual(
            result.after_diagnostic.model,
            result.training_result.final_model,
        )

    def test_action_one_selects_only_batch_one_and_changes_to_zero(self) -> None:
        result = _run(1)

        self.assertEqual(result.selected_action_index, 1)
        self.assertEqual(result.after_selected_action_index, 0)
        self.assertTrue(result.controlled_action_changed)
        self.assertEqual(
            result.selected_transition_record_ids,
            tuple(record.record_id for record in _batches()[1]),
        )

    def test_calls_decision_train_decision_in_exact_order(self) -> None:
        events: list[str] = []
        real_decision = loop_module.run_synthetic_linear_greedy_decision_diagnostic
        real_training = loop_module.train_synthetic_linear_action_value_model_smoke

        def decision_wrapper(*args: object, **kwargs: object) -> object:
            events.append("decision")
            return real_decision(*args, **kwargs)  # type: ignore[arg-type]

        def training_wrapper(*args: object, **kwargs: object) -> object:
            events.append("training")
            return real_training(*args, **kwargs)  # type: ignore[arg-type]

        with (
            patch.object(
                loop_module,
                "run_synthetic_linear_greedy_decision_diagnostic",
                side_effect=decision_wrapper,
            ) as decision_helper,
            patch.object(
                loop_module,
                "train_synthetic_linear_action_value_model_smoke",
                side_effect=training_wrapper,
            ) as training_helper,
        ):
            result = _run(0)

        self.assertEqual(events, ["decision", "training", "decision"])
        self.assertEqual(decision_helper.call_count, 2)
        self.assertEqual(training_helper.call_count, 1)
        self.assertEqual(
            training_helper.call_args.args[1],
            _batches()[0],
        )
        self.assertEqual(training_helper.call_args.kwargs["epoch_count"], 1)
        self.assertEqual(
            training_helper.call_args.args[0],
            result.before_diagnostic.model,
        )

    def test_requires_exact_two_batches_and_exact_inner_tuples(self) -> None:
        batches = _batches()

        class TupleSubclass(tuple):
            pass

        invalid_inputs = (
            list(batches),
            (batches[0],),
            batches + (batches[0],),
            TupleSubclass(batches),
            (list(batches[0]), batches[1]),
            (batches[0][:3], batches[1]),
            (TupleSubclass(batches[0]), batches[1]),
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(SyntheticOneStepPolicyImprovementSmokeError):
                    run_synthetic_one_step_policy_improvement_smoke(  # type: ignore[arg-type]
                        _model(),
                        _probes(),
                        value,
                        learning_rate=0.5,
                        discount_factor=0.5,
                    )

    def test_requires_first_action_binding_and_eight_distinct_ids(self) -> None:
        batches = _batches()
        bad_first = replace(batches[0][0], action_index=1)
        with self.assertRaisesRegex(
            SyntheticOneStepPolicyImprovementSmokeError,
            "first transition action_index",
        ):
            run_synthetic_one_step_policy_improvement_smoke(
                _model(),
                _probes(),
                ((bad_first,) + batches[0][1:], batches[1]),
                learning_rate=0.5,
                discount_factor=0.5,
            )

        duplicate = replace(batches[1][3], record_id=batches[0][1].record_id)
        with self.assertRaisesRegex(
            SyntheticOneStepPolicyImprovementSmokeError,
            "pairwise distinct",
        ):
            run_synthetic_one_step_policy_improvement_smoke(
                _model(),
                _probes(),
                (batches[0], batches[1][:3] + (duplicate,)),
                learning_rate=0.5,
                discount_factor=0.5,
            )

    def test_helper_errors_are_stage_wrapped_with_chained_causes(self) -> None:
        with self.assertRaisesRegex(
            SyntheticOneStepPolicyImprovementSmokeError,
            "before decision failed",
        ) as before_context:
            run_synthetic_one_step_policy_improvement_smoke(
                SyntheticLinearActionValueModel(
                    weights=((float("inf"), 0.0), (0.0, 0.0)),
                    biases=(0.0, 0.0),
                ),
                _probes(),
                _batches(),
                learning_rate=0.5,
                discount_factor=0.5,
            )
        self.assertIsNotNone(before_context.exception.__cause__)

        with self.assertRaisesRegex(
            SyntheticOneStepPolicyImprovementSmokeError,
            "selected batch training failed",
        ) as training_context:
            run_synthetic_one_step_policy_improvement_smoke(
                _model(),
                _probes(),
                _batches(),
                learning_rate=0.0,
                discount_factor=0.5,
            )
        self.assertIsNotNone(training_context.exception.__cause__)

        real_decision = loop_module.run_synthetic_linear_greedy_decision_diagnostic
        call_count = 0

        def fail_second_decision(*args: object, **kwargs: object) -> object:
            nonlocal call_count
            call_count += 1
            if call_count == 2:
                raise SyntheticLinearGreedyDecisionSmokeError("forced after failure")
            return real_decision(*args, **kwargs)  # type: ignore[arg-type]

        with (
            patch.object(
                loop_module,
                "run_synthetic_linear_greedy_decision_diagnostic",
                side_effect=fail_second_decision,
            ),
            self.assertRaisesRegex(
                SyntheticOneStepPolicyImprovementSmokeError,
                "after decision failed",
            ) as after_context,
        ):
            _run(0)
        self.assertIsNotNone(after_context.exception.__cause__)

    def test_repeated_output_inputs_and_frozen_result(self) -> None:
        model = _model()
        probes = _probes()
        batches = _batches()
        before_model = asdict(model)
        before_probes = tuple(asdict(probe) for probe in probes)
        before_batches = tuple(
            tuple(asdict(record) for record in batch) for batch in batches
        )

        first = run_synthetic_one_step_policy_improvement_smoke(
            model,
            probes,
            batches,
            learning_rate=0.5,
            discount_factor=0.5,
        )
        second = run_synthetic_one_step_policy_improvement_smoke(
            model,
            probes,
            batches,
            learning_rate=0.5,
            discount_factor=0.5,
        )

        self.assertEqual(first, second)
        self.assertEqual(asdict(model), before_model)
        self.assertEqual(tuple(asdict(probe) for probe in probes), before_probes)
        self.assertEqual(
            tuple(tuple(asdict(record) for record in batch) for batch in batches),
            before_batches,
        )
        with self.assertRaises(FrozenInstanceError):
            first.selected_action_index = 1  # type: ignore[misc]

    def test_result_has_exact_fields_ids_counts_grade_and_warnings(self) -> None:
        result = _run(0)

        self.assertIsInstance(result, SyntheticOneStepPolicyImprovementResult)
        self.assertEqual(
            set(asdict(result)),
            {
                "smoke_version",
                "initial_model",
                "before_diagnostic",
                "selected_action_index",
                "selected_transition_record_ids",
                "training_result",
                "after_diagnostic",
                "after_selected_action_index",
                "controlled_action_changed",
                "closed_loop_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.smoke_version,
            SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION,
        )
        self.assertEqual(result.training_result.epoch_count, 1)
        self.assertEqual(result.training_result.update_count, 4)
        self.assertTrue(result.closed_loop_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        self.assertEqual(
            result.evidence_grade,
            "P8 exact one-step synthetic/local policy-improvement closed-loop smoke evidence only",
        )
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "one-step synthetic/local policy-improvement closed-loop smoke only",
            "one before decision, one selected four-transition batch, one training epoch and one after decision",
            "unselected candidate batch is not trained",
            "no general environment, episode, replay buffer or self-play",
            "no model loading, persistence, checkpoint or external dependency",
            "not production training, inference or evaluation",
            "action change is not policy-quality or model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_exports_public_surface_and_no_formula_copy(self) -> None:
        self.assertIs(
            run_synthetic_one_step_policy_improvement_smoke,
            loop_module.run_synthetic_one_step_policy_improvement_smoke,
        )
        self.assertEqual(
            set(loop_module.__all__),
            {
                "SYNTHETIC_ONE_STEP_POLICY_IMPROVEMENT_SMOKE_VERSION",
                "SyntheticOneStepPolicyImprovementSmokeError",
                "SyntheticOneStepPolicyImprovementResult",
                "run_synthetic_one_step_policy_improvement_smoke",
            },
        )
        source = inspect.getsource(loop_module)
        for copied_formula in (
            "target - prediction",
            "weights[action_index]",
            "action_one_value > action_zero_value",
        ):
            self.assertNotIn(copied_formula, source)
        public_text = " ".join(loop_module.__all__).lower()
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

    def test_unselected_batch_is_validated_but_never_trained(self) -> None:
        batches = _batches()
        invalid_unselected = replace(batches[1][2], uses_external_log=True)
        with self.assertRaisesRegex(
            SyntheticOneStepPolicyImprovementSmokeError,
            "candidate batch 1 transition 3 validation failed",
        ):
            run_synthetic_one_step_policy_improvement_smoke(
                _model(0),
                _probes(),
                (batches[0], batches[1][:2] + (invalid_unselected,) + batches[1][3:]),
                learning_rate=0.5,
                discount_factor=0.5,
            )

        with patch.object(
            loop_module,
            "train_synthetic_linear_action_value_model_smoke",
            wraps=loop_module.train_synthetic_linear_action_value_model_smoke,
        ) as trainer:
            _run(0)
        self.assertEqual(trainer.call_count, 1)
        self.assertEqual(trainer.call_args.args[1], batches[0])


if __name__ == "__main__":
    unittest.main()
