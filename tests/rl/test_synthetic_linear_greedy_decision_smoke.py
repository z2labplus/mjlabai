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

import mjlabai.rl.synthetic_linear_greedy_decision_smoke as decision_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION,
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SyntheticLinearActionValueModel,
    SyntheticLinearDecision,
    SyntheticLinearDecisionProbe,
    SyntheticLinearGreedyDecisionDiagnosticResult,
    SyntheticLinearGreedyDecisionSmokeError,
    SyntheticLinearQTransition,
    train_synthetic_linear_action_value_model_smoke,
    run_synthetic_linear_greedy_decision_diagnostic,
)


def _model(**overrides: object) -> SyntheticLinearActionValueModel:
    values: dict[str, object] = {
        "weights": ((1.0, 2.0), (-1.0, 0.5)),
        "biases": (0.5, -0.25),
    }
    values.update(overrides)
    return SyntheticLinearActionValueModel(**values)  # type: ignore[arg-type]


def _probe(index: int, **overrides: object) -> SyntheticLinearDecisionProbe:
    values: dict[str, object] = {
        "probe_id": f"decision:{index}",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "features": (1.0, 0.0),
        "legal_action_indices": (0, 1),
        "project_authored": True,
        "synthetic": True,
        "local_only": True,
        "uses_real_data": False,
        "uses_external_log": False,
        "uses_platform_data": False,
        "uses_model_output": False,
        "uses_self_play": False,
    }
    values.update(overrides)
    return SyntheticLinearDecisionProbe(**values)  # type: ignore[arg-type]


def _probes() -> tuple[
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
    SyntheticLinearDecisionProbe,
]:
    return (
        _probe(1, features=(1.0, 0.0)),
        _probe(2, features=(0.0, -2.0)),
        _probe(3, features=(-0.375, 0.0)),
    )


def _training_transition(
    index: int,
    **overrides: object,
) -> SyntheticLinearQTransition:
    values: dict[str, object] = {
        "record_id": f"decision-training:{index}",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "state_features": (1.0, 0.0),
        "action_index": 0,
        "reward": 1.0,
        "next_state_features": None,
        "terminal": True,
        "project_authored": True,
        "synthetic": True,
        "local_only": True,
        "uses_real_data": False,
        "uses_external_log": False,
        "uses_platform_data": False,
        "uses_model_output": False,
        "uses_self_play": False,
    }
    values.update(overrides)
    return SyntheticLinearQTransition(**values)  # type: ignore[arg-type]


class SyntheticLinearGreedyDecisionSmokeTests(unittest.TestCase):
    def test_exact_action_values_and_decisions_for_three_probes(self) -> None:
        result = run_synthetic_linear_greedy_decision_diagnostic(
            _model(),
            _probes(),
        )

        self.assertEqual(
            tuple(decision.action_values for decision in result.decisions),
            ((1.5, -1.25), (-3.5, -1.25), (0.125, 0.125)),
        )
        self.assertEqual(
            tuple(decision.selected_action_index for decision in result.decisions),
            (0, 1, 0),
        )
        self.assertEqual(
            tuple(decision.tie_detected for decision in result.decisions),
            (False, False, True),
        )

    def test_exact_tie_uses_lower_action_index(self) -> None:
        tie_model = _model(
            weights=((1.0, 1.0), (1.0, 1.0)),
            biases=(0.0, 0.0),
        )

        result = run_synthetic_linear_greedy_decision_diagnostic(
            tie_model,
            _probes(),
        )

        for decision in result.decisions:
            self.assertTrue(decision.tie_detected)
            self.assertEqual(decision.selected_action_index, 0)

    def test_integrates_with_reviewed_trainer_final_model(self) -> None:
        transitions = tuple(
            _training_transition(
                index,
                action_index=0 if index % 2 else 1,
                reward=float(index),
            )
            for index in range(1, 5)
        )
        trained = train_synthetic_linear_action_value_model_smoke(
            SyntheticLinearActionValueModel(
                weights=((0.0, 0.0), (0.0, 0.0)),
                biases=(0.0, 0.0),
            ),
            transitions,  # type: ignore[arg-type]
            learning_rate=0.1,
            discount_factor=0.5,
            epoch_count=2,
        )

        result = run_synthetic_linear_greedy_decision_diagnostic(
            trained.final_model,
            _probes(),
        )

        self.assertEqual(result.model, trained.final_model)
        self.assertEqual(result.probe_count, 3)
        self.assertEqual(len(result.decisions), 3)

    def test_requires_exact_three_probe_tuple_and_exact_objects(self) -> None:
        probes = _probes()

        class TupleSubclass(tuple):
            pass

        invalid_inputs = (
            list(probes),
            probes[:2],
            probes + (_probe(4),),
            TupleSubclass(probes),
            (asdict(probes[0]),) + probes[1:],
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__, length=len(value)):
                with self.assertRaises(SyntheticLinearGreedyDecisionSmokeError):
                    run_synthetic_linear_greedy_decision_diagnostic(  # type: ignore[arg-type]
                        _model(),
                        value,
                    )

    def test_feature_and_legal_action_tuple_validation(self) -> None:
        class TupleSubclass(tuple):
            pass

        invalid_first_probes = (
            replace(_probes()[0], features=[1.0, 0.0]),
            replace(_probes()[0], features=(1.0,)),
            replace(_probes()[0], features=(True, 0.0)),
            replace(_probes()[0], legal_action_indices=[0, 1]),
            replace(_probes()[0], legal_action_indices=TupleSubclass((0, 1))),
            replace(_probes()[0], legal_action_indices=(False, True)),
            replace(_probes()[0], legal_action_indices=(1, 0)),
        )
        for probe in invalid_first_probes:
            with self.subTest(probe=probe):
                with self.assertRaises(SyntheticLinearGreedyDecisionSmokeError):
                    run_synthetic_linear_greedy_decision_diagnostic(
                        _model(),
                        (probe,) + _probes()[1:],
                    )

    def test_provenance_source_and_distinct_ids_are_required(self) -> None:
        cases = (
            replace(_probes()[0], probe_id=" "),
            replace(_probes()[0], source_kind="external"),
            replace(_probes()[0], project_authored=False),
            replace(_probes()[0], synthetic=False),
            replace(_probes()[0], local_only=False),
            replace(_probes()[0], uses_real_data=True),
            replace(_probes()[0], uses_external_log=True),
            replace(_probes()[0], uses_platform_data=True),
            replace(_probes()[0], uses_model_output=True),
            replace(_probes()[0], uses_self_play=True),
        )
        for probe in cases:
            with self.subTest(probe=probe):
                with self.assertRaises(SyntheticLinearGreedyDecisionSmokeError):
                    run_synthetic_linear_greedy_decision_diagnostic(
                        _model(),
                        (probe,) + _probes()[1:],
                    )

        duplicate = replace(_probes()[2], probe_id=_probes()[0].probe_id)
        with self.assertRaisesRegex(
            SyntheticLinearGreedyDecisionSmokeError,
            "pairwise distinct",
        ):
            run_synthetic_linear_greedy_decision_diagnostic(
                _model(),
                _probes()[:2] + (duplicate,),
            )

    def test_reuses_reviewed_helpers_without_formula_copy(self) -> None:
        with (
            patch.object(
                decision_module,
                "_normalize_model",
                wraps=decision_module._normalize_model,
            ) as model_helper,
            patch.object(
                decision_module,
                "_normalize_features",
                wraps=decision_module._normalize_features,
            ) as feature_helper,
            patch.object(
                decision_module,
                "_action_value",
                wraps=decision_module._action_value,
            ) as action_value_helper,
        ):
            run_synthetic_linear_greedy_decision_diagnostic(_model(), _probes())

        self.assertEqual(model_helper.call_count, 1)
        self.assertEqual(feature_helper.call_count, 3)
        self.assertEqual(action_value_helper.call_count, 6)
        source = inspect.getsource(decision_module)
        self.assertNotIn("weights[action_index][0] *", source)
        self.assertNotIn("weights[action_index][1] *", source)

    def test_repeated_output_inputs_and_frozen_results(self) -> None:
        model = _model()
        probes = _probes()
        before_model = asdict(model)
        before_probes = tuple(asdict(probe) for probe in probes)

        first = run_synthetic_linear_greedy_decision_diagnostic(model, probes)
        second = run_synthetic_linear_greedy_decision_diagnostic(model, probes)

        self.assertEqual(first, second)
        self.assertEqual(asdict(model), before_model)
        self.assertEqual(tuple(asdict(probe) for probe in probes), before_probes)
        with self.assertRaises(FrozenInstanceError):
            first.probe_count = 4  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            first.decisions[0].selected_action_index = 1  # type: ignore[misc]

    def test_result_has_exact_fields_counts_grade_and_warnings(self) -> None:
        result = run_synthetic_linear_greedy_decision_diagnostic(
            _model(),
            _probes(),
        )

        self.assertIsInstance(result, SyntheticLinearGreedyDecisionDiagnosticResult)
        self.assertTrue(all(isinstance(item, SyntheticLinearDecision) for item in result.decisions))
        self.assertEqual(
            set(asdict(result)),
            {
                "diagnostic_version",
                "model",
                "probe_count",
                "decisions",
                "probe_ids",
                "inference_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            set(asdict(result.decisions[0])),
            {
                "probe_id",
                "features",
                "legal_action_indices",
                "action_values",
                "selected_action_index",
                "tie_detected",
            },
        )
        self.assertEqual(
            result.diagnostic_version,
            SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION,
        )
        self.assertEqual(result.probe_count, 3)
        self.assertEqual(result.probe_ids, ("decision:1", "decision:2", "decision:3"))
        self.assertTrue(result.inference_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        self.assertEqual(
            result.evidence_grade,
            "P8 exact synthetic/local linear-model inference and greedy-decision diagnostic evidence only",
        )
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local linear-model inference and greedy-decision diagnostic only",
            "fixed two features, two actions and three probes",
            "deterministic lower-action-index tie break",
            "no environment, gameplay, replay buffer or self-play",
            "no model loading, external dependency, persistence or checkpoint",
            "not production inference or evaluation",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_exports_and_public_surface_are_narrow(self) -> None:
        self.assertIs(
            run_synthetic_linear_greedy_decision_diagnostic,
            decision_module.run_synthetic_linear_greedy_decision_diagnostic,
        )
        self.assertEqual(
            set(decision_module.__all__),
            {
                "SYNTHETIC_LINEAR_GREEDY_DECISION_SMOKE_VERSION",
                "SyntheticLinearGreedyDecisionSmokeError",
                "SyntheticLinearDecisionProbe",
                "SyntheticLinearDecision",
                "SyntheticLinearGreedyDecisionDiagnosticResult",
                "run_synthetic_linear_greedy_decision_diagnostic",
            },
        )
        public_text = " ".join(decision_module.__all__).lower()
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

    def test_invalid_and_huge_numeric_errors_are_wrapped_with_cause(self) -> None:
        huge_model = _model(weights=((10**10000, 0.0), (0.0, 0.0)))
        with self.assertRaisesRegex(
            SyntheticLinearGreedyDecisionSmokeError,
            "model validation failed",
        ) as model_context:
            run_synthetic_linear_greedy_decision_diagnostic(huge_model, _probes())
        self.assertIsNotNone(model_context.exception.__cause__)
        self.assertIsInstance(
            model_context.exception.__cause__.__cause__,
            OverflowError,
        )

        huge_probe = replace(_probes()[0], features=(10**10000, 0.0))
        with self.assertRaisesRegex(
            SyntheticLinearGreedyDecisionSmokeError,
            "probe 1 feature validation failed",
        ) as probe_context:
            run_synthetic_linear_greedy_decision_diagnostic(
                _model(),
                (huge_probe,) + _probes()[1:],
            )
        self.assertIsNotNone(probe_context.exception.__cause__)
        self.assertIsInstance(
            probe_context.exception.__cause__.__cause__,
            OverflowError,
        )


if __name__ == "__main__":
    unittest.main()
