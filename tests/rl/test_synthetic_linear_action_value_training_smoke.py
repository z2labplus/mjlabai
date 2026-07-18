from __future__ import annotations

from dataclasses import FrozenInstanceError, asdict, replace
import inspect
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.rl.synthetic_linear_action_value_training_smoke as linear_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    LINEAR_ACTION_VALUE_ACTION_COUNT,
    LINEAR_ACTION_VALUE_FEATURE_COUNT,
    MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS,
    SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION,
    SYNTHETIC_LOCAL_SOURCE_KIND,
    SyntheticLinearActionValueModel,
    SyntheticLinearActionValueTrainingResult,
    SyntheticLinearActionValueTrainingSmokeError,
    SyntheticLinearQTransition,
    train_synthetic_linear_action_value_model_smoke,
)


def _model(**overrides: object) -> SyntheticLinearActionValueModel:
    values: dict[str, object] = {
        "weights": ((0.0, 0.0), (0.0, 0.0)),
        "biases": (0.0, 0.0),
    }
    values.update(overrides)
    return SyntheticLinearActionValueModel(**values)  # type: ignore[arg-type]


def _transition(index: int, **overrides: object) -> SyntheticLinearQTransition:
    values: dict[str, object] = {
        "record_id": f"linear:{index}",
        "source_kind": SYNTHETIC_LOCAL_SOURCE_KIND,
        "state_features": (1.0, 0.0),
        "action_index": 0,
        "reward": 1.0,
        "next_state_features": (0.0, 1.0),
        "terminal": False,
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


def _transitions() -> tuple[
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
    SyntheticLinearQTransition,
]:
    return (
        _transition(1),
        _transition(
            2,
            state_features=(0.0, 1.0),
            action_index=1,
            reward=2.0,
            next_state_features=None,
            terminal=True,
        ),
        _transition(
            3,
            state_features=(1.0, 1.0),
            reward=0.0,
            next_state_features=(1.0, 0.0),
        ),
        _transition(
            4,
            state_features=(0.5, -1.0),
            action_index=1,
            reward=-1.0,
            next_state_features=None,
            terminal=True,
        ),
    )


def _train(
    *,
    model: SyntheticLinearActionValueModel | None = None,
    transitions: tuple[
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
        SyntheticLinearQTransition,
    ]
    | None = None,
    epoch_count: int = 1,
) -> SyntheticLinearActionValueTrainingResult:
    return train_synthetic_linear_action_value_model_smoke(
        model or _model(),
        transitions or _transitions(),
        learning_rate=0.1,
        discount_factor=0.5,
        epoch_count=epoch_count,
    )


class SyntheticLinearActionValueTrainingSmokeTests(unittest.TestCase):
    def test_exact_one_epoch_parameters_and_loss(self) -> None:
        result = _train()

        self.assertEqual(
            result.final_model.weights[0],
            (0.09, -0.010000000000000002),
        )
        self.assertEqual(
            result.final_model.weights[1],
            (-0.05, 0.30000000000000004),
        )
        self.assertEqual(result.final_model.biases, (0.09, 0.1))
        self.assertEqual(result.epoch_mean_squared_td_errors, (1.5025,))

    def test_terminal_and_non_terminal_targets_are_distinct(self) -> None:
        model = _model(
            weights=((1.0, 0.0), (0.0, 0.0)),
            biases=(0.0, 0.0),
        )
        transitions = (
            _transition(
                1,
                state_features=(0.0, 0.0),
                reward=0.0,
                next_state_features=(1.0, 0.0),
            ),
            _transition(
                2,
                state_features=(0.0, 0.0),
                reward=0.0,
                next_state_features=None,
                terminal=True,
            ),
            _transition(
                3,
                state_features=(0.0, 0.0),
                action_index=1,
                reward=0.0,
                next_state_features=None,
                terminal=True,
            ),
            _transition(
                4,
                state_features=(0.0, 0.0),
                action_index=1,
                reward=0.0,
                next_state_features=None,
                terminal=True,
            ),
        )

        result = _train(model=model, transitions=transitions)

        self.assertEqual(result.final_model.weights, model.weights)
        self.assertEqual(result.final_model.biases, (0.045, 0.0))
        self.assertEqual(result.epoch_mean_squared_td_errors, (0.063125,))

    def test_exact_two_epoch_carry_forward_is_deterministic(self) -> None:
        result = _train(epoch_count=2)

        self.assertEqual(
            result.final_model.weights,
            (
                (0.1738, -0.028200000000000003),
                (-0.08875, 0.5375000000000001),
            ),
        )
        self.assertEqual(result.final_model.biases, (0.1738, 0.1825))
        self.assertEqual(
            result.epoch_mean_squared_td_errors,
            (1.5025, 1.05853725),
        )

    def test_epoch_bounds_require_exact_int_and_accept_eight(self) -> None:
        for bad_epoch in (0, 9, True, 1.0, "1"):
            with self.subTest(bad_epoch=bad_epoch):
                with self.assertRaises(SyntheticLinearActionValueTrainingSmokeError):
                    _train(epoch_count=bad_epoch)  # type: ignore[arg-type]

        result = _train(epoch_count=8)
        self.assertEqual(result.epoch_count, 8)
        self.assertEqual(result.max_epochs, 8)
        self.assertEqual(result.update_count, 32)
        self.assertEqual(len(result.epoch_mean_squared_td_errors), 8)

        invalid_parameters = (
            {"learning_rate": 0.0},
            {"learning_rate": -0.1},
            {"learning_rate": 1.1},
            {"learning_rate": True},
            {"learning_rate": float("nan")},
            {"discount_factor": -0.1},
            {"discount_factor": 1.1},
            {"discount_factor": False},
            {"discount_factor": float("inf")},
        )
        for overrides in invalid_parameters:
            parameters: dict[str, object] = {
                "learning_rate": 0.1,
                "discount_factor": 0.5,
            }
            parameters.update(overrides)
            with self.subTest(parameters=parameters):
                with self.assertRaises(SyntheticLinearActionValueTrainingSmokeError):
                    train_synthetic_linear_action_value_model_smoke(
                        _model(),
                        _transitions(),
                        epoch_count=1,
                        **parameters,  # type: ignore[arg-type]
                    )

    def test_model_requires_exact_nested_tuple_shapes_and_finite_values(self) -> None:
        class ModelSubclass(SyntheticLinearActionValueModel):
            pass

        class TupleSubclass(tuple):
            pass

        invalid_models = (
            ModelSubclass(((0.0, 0.0), (0.0, 0.0)), (0.0, 0.0)),
            _model(weights=[(0.0, 0.0), (0.0, 0.0)]),
            _model(weights=TupleSubclass(((0.0, 0.0), (0.0, 0.0)))),
            _model(weights=((0.0,), (0.0, 0.0))),
            _model(weights=((False, 0.0), (0.0, 0.0))),
            _model(biases=[0.0, 0.0]),
            _model(biases=(float("inf"), 0.0)),
        )
        for model in invalid_models:
            with self.subTest(model=model):
                with self.assertRaises(SyntheticLinearActionValueTrainingSmokeError):
                    _train(model=model)

        normalized = _train(model=_model(weights=((0, 0), (0, 0)), biases=(0, 0)))
        self.assertIsInstance(normalized.initial_model.weights[0][0], float)

    def test_requires_exact_four_transition_tuple_and_exact_objects(self) -> None:
        transitions = _transitions()

        class TupleSubclass(tuple):
            pass

        invalid_inputs = (
            list(transitions),
            transitions[:3],
            transitions + (_transition(5),),
            TupleSubclass(transitions),
            (asdict(transitions[0]),) + transitions[1:],
        )
        for value in invalid_inputs:
            with self.subTest(value_type=type(value).__name__, length=len(value)):
                with self.assertRaises(SyntheticLinearActionValueTrainingSmokeError):
                    train_synthetic_linear_action_value_model_smoke(  # type: ignore[arg-type]
                        _model(),
                        value,
                        learning_rate=0.1,
                        discount_factor=0.5,
                        epoch_count=1,
                    )

    def test_transition_feature_action_reward_and_terminal_validation(self) -> None:
        invalid_first_records = (
            replace(_transitions()[0], state_features=[1.0, 0.0]),
            replace(_transitions()[0], state_features=(1.0,)),
            replace(_transitions()[0], state_features=(True, 0.0)),
            replace(_transitions()[0], action_index=True),
            replace(_transitions()[0], action_index=2),
            replace(_transitions()[0], reward=float("nan")),
            replace(_transitions()[0], next_state_features=None),
            replace(_transitions()[0], terminal="false"),
            replace(
                _transitions()[1],
                next_state_features=(0.0, 0.0),
            ),
        )
        for record in invalid_first_records:
            with self.subTest(record=record):
                records = (record,) + _transitions()[1:]
                with self.assertRaises(SyntheticLinearActionValueTrainingSmokeError):
                    _train(transitions=records)  # type: ignore[arg-type]

    def test_provenance_source_and_distinct_ids_are_required(self) -> None:
        cases = (
            replace(_transitions()[0], record_id=" "),
            replace(_transitions()[0], source_kind="external"),
            replace(_transitions()[0], project_authored=False),
            replace(_transitions()[0], synthetic=False),
            replace(_transitions()[0], local_only=False),
            replace(_transitions()[0], uses_real_data=True),
            replace(_transitions()[0], uses_external_log=True),
            replace(_transitions()[0], uses_platform_data=True),
            replace(_transitions()[0], uses_model_output=True),
            replace(_transitions()[0], uses_self_play=True),
        )
        for record in cases:
            with self.subTest(record=record):
                with self.assertRaises(SyntheticLinearActionValueTrainingSmokeError):
                    _train(transitions=(record,) + _transitions()[1:])

        duplicate = replace(_transitions()[3], record_id=_transitions()[0].record_id)
        with self.assertRaisesRegex(
            SyntheticLinearActionValueTrainingSmokeError,
            "pairwise distinct",
        ):
            _train(transitions=_transitions()[:3] + (duplicate,))

    def test_selected_action_only_and_ordered_update_count(self) -> None:
        transitions = tuple(
            _transition(
                index,
                state_features=(1.0, 0.0),
                action_index=0,
                reward=1.0 if index == 1 else 0.0,
                next_state_features=None,
                terminal=True,
            )
            for index in range(1, 5)
        )

        result = _train(transitions=transitions)  # type: ignore[arg-type]

        self.assertEqual(result.update_count, 4)
        self.assertEqual(result.final_model.weights[1], (0.0, 0.0))
        self.assertEqual(result.final_model.biases[1], 0.0)
        self.assertEqual(result.record_ids, tuple(f"linear:{i}" for i in range(1, 5)))
        source = inspect.getsource(linear_module)
        self.assertNotIn("shuffle", inspect.getsource(linear_module.train_synthetic_linear_action_value_model_smoke))
        self.assertNotIn("while ", source)

    def test_repeated_output_inputs_and_frozen_results(self) -> None:
        model = _model()
        transitions = _transitions()
        before_model = asdict(model)
        before_transitions = tuple(asdict(record) for record in transitions)

        first = _train(model=model, transitions=transitions, epoch_count=2)
        second = _train(model=model, transitions=transitions, epoch_count=2)

        self.assertEqual(first, second)
        self.assertEqual(asdict(model), before_model)
        self.assertEqual(tuple(asdict(record) for record in transitions), before_transitions)
        with self.assertRaises(FrozenInstanceError):
            first.epoch_count = 3  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            first.final_model.biases = (1.0, 1.0)  # type: ignore[misc]

    def test_result_has_exact_fields_counts_grade_and_warnings(self) -> None:
        result = _train(epoch_count=2)

        self.assertEqual(
            set(asdict(result)),
            {
                "training_version",
                "feature_count",
                "action_count",
                "epoch_count",
                "max_epochs",
                "transition_count",
                "update_count",
                "initial_model",
                "final_model",
                "epoch_mean_squared_td_errors",
                "record_ids",
                "training_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.training_version,
            SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION,
        )
        self.assertEqual(result.feature_count, LINEAR_ACTION_VALUE_FEATURE_COUNT)
        self.assertEqual(result.action_count, LINEAR_ACTION_VALUE_ACTION_COUNT)
        self.assertEqual(result.max_epochs, MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS)
        self.assertEqual(result.transition_count, 4)
        self.assertEqual(result.update_count, 8)
        self.assertTrue(result.training_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        self.assertEqual(
            result.evidence_grade,
            "P8 exact synthetic/local linear action-value model training smoke evidence only",
        )
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "synthetic/local linear action-value model training smoke only",
            "fixed two features, two actions, four transitions and at most eight epochs",
            "deterministic ordered temporal-difference updates only",
            "no environment, replay buffer, self-play or model-generated data",
            "no external dependency, tensor framework, optimizer or checkpoint",
            "not production training or evaluation",
            "not model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_exports_and_public_surface_are_narrow(self) -> None:
        self.assertIs(
            train_synthetic_linear_action_value_model_smoke,
            linear_module.train_synthetic_linear_action_value_model_smoke,
        )
        self.assertEqual(
            set(linear_module.__all__),
            {
                "SYNTHETIC_LINEAR_ACTION_VALUE_TRAINING_SMOKE_VERSION",
                "LINEAR_ACTION_VALUE_FEATURE_COUNT",
                "LINEAR_ACTION_VALUE_ACTION_COUNT",
                "MAX_SYNTHETIC_LINEAR_TRAINING_EPOCHS",
                "SyntheticLinearActionValueTrainingSmokeError",
                "SyntheticLinearQTransition",
                "SyntheticLinearActionValueModel",
                "SyntheticLinearActionValueTrainingResult",
                "train_synthetic_linear_action_value_model_smoke",
            },
        )
        public_text = " ".join(linear_module.__all__).lower()
        for forbidden in (
            "path",
            "file",
            "persistence",
            "environment",
            "replay",
            "self_play",
            "checkpoint",
            "evaluation",
        ):
            self.assertNotIn(forbidden, public_text)

    def test_huge_numeric_conversion_is_normalized_with_cause(self) -> None:
        huge_model = _model(weights=((10**10000, 0.0), (0.0, 0.0)))

        with self.assertRaisesRegex(
            SyntheticLinearActionValueTrainingSmokeError,
            "representable as a finite float",
        ) as context:
            _train(model=huge_model)

        self.assertIsInstance(context.exception.__cause__, OverflowError)


if __name__ == "__main__":
    unittest.main()
