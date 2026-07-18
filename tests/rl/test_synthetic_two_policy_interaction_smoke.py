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

import mjlabai.rl.synthetic_two_policy_interaction_smoke as interaction_module  # noqa: E402
from mjlabai.rl import (  # noqa: E402
    MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS,
    SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION,
    SyntheticTwoPolicyInteractionResult,
    SyntheticTwoPolicyInteractionSmokeError,
    SyntheticTwoPolicyInteractionTurnInput,
    SyntheticTwoPolicyInteractionTurnResult,
    SyntheticTwoPolicyParticipantInput,
    run_synthetic_two_policy_interaction_smoke,
)
from tests.rl.test_synthetic_policy_improvement_sequence_smoke import (  # noqa: E402
    _batches,
    _model,
    _probes,
)


def _participants() -> tuple[
    SyntheticTwoPolicyParticipantInput,
    SyntheticTwoPolicyParticipantInput,
]:
    return (
        SyntheticTwoPolicyParticipantInput(
            policy_id="policy-a",
            initial_model=_model(0),
        ),
        SyntheticTwoPolicyParticipantInput(
            policy_id="policy-b",
            initial_model=_model(1),
        ),
    )


def _turn(turn_index: int) -> SyntheticTwoPolicyInteractionTurnInput:
    return SyntheticTwoPolicyInteractionTurnInput(
        turn_id=f"interaction-turn:{turn_index}",
        actor_policy_id="policy-a" if turn_index % 2 == 1 else "policy-b",
        decision_probes=_probes(),
        candidate_transition_batches=_batches(turn_index),
        learning_rate=0.5,
        discount_factor=0.5,
    )


def _run(turn_count: int = 2) -> SyntheticTwoPolicyInteractionResult:
    return run_synthetic_two_policy_interaction_smoke(
        _participants(),
        tuple(_turn(index) for index in range(1, turn_count + 1)),
    )


class SyntheticTwoPolicyInteractionSmokeTests(unittest.TestCase):
    def test_two_turns_update_both_policies_in_ab_order(self) -> None:
        result = _run(2)

        self.assertEqual(result.policy_ids, ("policy-a", "policy-b"))
        self.assertEqual(result.selected_actions, (0, 1))
        self.assertEqual(result.after_actions, (1, 0))
        self.assertEqual(
            result.final_models,
            (
                result.turn_results[0].actor_final_model,
                result.turn_results[1].actor_final_model,
            ),
        )
        self.assertNotEqual(result.final_models[0], result.initial_models[0])
        self.assertNotEqual(result.final_models[1], result.initial_models[1])

    def test_four_turns_preserve_independent_policy_continuity(self) -> None:
        result = _run(4)

        self.assertEqual(result.selected_actions, (0, 1, 1, 0))
        self.assertEqual(result.after_actions, (1, 0, 0, 1))
        self.assertEqual(
            result.turn_results[2].actor_initial_model,
            result.turn_results[0].actor_final_model,
        )
        self.assertEqual(
            result.turn_results[3].actor_initial_model,
            result.turn_results[1].actor_final_model,
        )
        self.assertEqual(result.final_models[0], result.turn_results[2].actor_final_model)
        self.assertEqual(result.final_models[1], result.turn_results[3].actor_final_model)

    def test_requires_exact_two_frozen_participants_and_distinct_ids(self) -> None:
        class TupleSubclass(tuple):
            pass

        class ParticipantSubclass(SyntheticTwoPolicyParticipantInput):
            pass

        participants = _participants()
        turns = (_turn(1), _turn(2))
        for invalid in (
            list(participants),
            (participants[0],),
            participants + (participants[0],),
            TupleSubclass(participants),
        ):
            with self.assertRaisesRegex(
                SyntheticTwoPolicyInteractionSmokeError,
                "exact two-participant tuple",
            ):
                run_synthetic_two_policy_interaction_smoke(  # type: ignore[arg-type]
                    invalid, turns
                )
        subclass = ParticipantSubclass(**asdict(participants[0]))
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "exact SyntheticTwoPolicyParticipantInput",
        ):
            run_synthetic_two_policy_interaction_smoke(
                (subclass, participants[1]), turns
            )
        for invalid_id in ("", "   ", 1):
            with self.assertRaisesRegex(
                SyntheticTwoPolicyInteractionSmokeError,
                "non-empty string",
            ):
                run_synthetic_two_policy_interaction_smoke(
                    (replace(participants[0], policy_id=invalid_id), participants[1]),  # type: ignore[arg-type]
                    turns,
                )
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "must be distinct",
        ):
            run_synthetic_two_policy_interaction_smoke(
                (
                    participants[0],
                    replace(participants[1], policy_id=participants[0].policy_id),
                ),
                turns,
            )
        with self.assertRaises(FrozenInstanceError):
            participants[0].policy_id = "changed"  # type: ignore[misc]

    def test_requires_exact_two_or_four_turns_and_ab_alternation(self) -> None:
        class TupleSubclass(tuple):
            pass

        participants = _participants()
        for invalid in (
            (_turn(1),),
            tuple(_turn(i) for i in range(1, 4)),
            tuple(_turn(i) for i in range(1, 6)),
        ):
            with self.assertRaisesRegex(
                SyntheticTwoPolicyInteractionSmokeError,
                "exactly 2 or exactly 4",
            ):
                run_synthetic_two_policy_interaction_smoke(participants, invalid)
        for invalid in (
            [_turn(1), _turn(2)],
            TupleSubclass((_turn(1), _turn(2))),
        ):
            with self.assertRaisesRegex(
                SyntheticTwoPolicyInteractionSmokeError,
                "exact tuple",
            ):
                run_synthetic_two_policy_interaction_smoke(  # type: ignore[arg-type]
                    participants, invalid
                )
        wrong_actor = replace(_turn(2), actor_policy_id="policy-a")
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "turn 2 actor_policy_id",
        ):
            run_synthetic_two_policy_interaction_smoke(
                participants, (_turn(1), wrong_actor)
            )

    def test_requires_exact_frozen_turns_and_distinct_nonempty_ids(self) -> None:
        class TurnSubclass(SyntheticTwoPolicyInteractionTurnInput):
            pass

        first = _turn(1)
        second = _turn(2)
        subclass = TurnSubclass(**asdict(first))
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "exact SyntheticTwoPolicyInteractionTurnInput",
        ):
            run_synthetic_two_policy_interaction_smoke(
                _participants(), (subclass, second)
            )
        for invalid_id in ("", "   ", 1):
            with self.assertRaisesRegex(
                SyntheticTwoPolicyInteractionSmokeError,
                "non-empty string",
            ):
                run_synthetic_two_policy_interaction_smoke(
                    _participants(),
                    (replace(first, turn_id=invalid_id), second),  # type: ignore[arg-type]
                )
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "pairwise distinct",
        ):
            run_synthetic_two_policy_interaction_smoke(
                _participants(),
                (first, replace(second, turn_id=first.turn_id)),
            )
        with self.assertRaises(FrozenInstanceError):
            first.turn_id = "changed"  # type: ignore[misc]

    def test_rejects_global_candidate_transition_id_reuse(self) -> None:
        first = _turn(1)
        second = _turn(2)
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
            SyntheticTwoPolicyInteractionSmokeError,
            "globally pairwise distinct",
        ):
            run_synthetic_two_policy_interaction_smoke(
                _participants(), (first, second)
            )

    def test_calls_reviewed_helper_once_per_turn_with_actor_continuity(self) -> None:
        real_helper = interaction_module.run_synthetic_one_step_policy_improvement_smoke
        with patch.object(
            interaction_module,
            "run_synthetic_one_step_policy_improvement_smoke",
            wraps=real_helper,
        ) as helper:
            result = _run(4)

        self.assertEqual(helper.call_count, 4)
        self.assertEqual(helper.call_args_list[0].args[0], result.initial_models[0])
        self.assertEqual(helper.call_args_list[1].args[0], result.initial_models[1])
        self.assertEqual(
            helper.call_args_list[2].args[0],
            result.turn_results[0].actor_final_model,
        )
        self.assertEqual(
            helper.call_args_list[3].args[0],
            result.turn_results[1].actor_final_model,
        )

    def test_non_actor_model_is_unchanged_on_every_turn(self) -> None:
        result = _run(4)

        self.assertTrue(
            all(turn.non_actor_model_unchanged for turn in result.turn_results)
        )
        for turn in result.turn_results:
            self.assertEqual(turn.non_actor_model_before, turn.non_actor_model_after)

    def test_wraps_candidate_and_helper_errors_with_turn_index_and_cause(self) -> None:
        malformed = replace(
            _turn(1),
            candidate_transition_batches=(_batches(1)[0],),  # type: ignore[arg-type]
        )
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "turn 1 failed",
        ) as candidate_context:
            run_synthetic_two_policy_interaction_smoke(
                _participants(), (malformed, _turn(2))
            )
        self.assertIsNotNone(candidate_context.exception.__cause__)

        invalid_second = replace(_turn(2), learning_rate=0.0)
        with self.assertRaisesRegex(
            SyntheticTwoPolicyInteractionSmokeError,
            "turn 2 failed",
        ) as helper_context:
            run_synthetic_two_policy_interaction_smoke(
                _participants(), (_turn(1), invalid_second)
            )
        self.assertIsNotNone(helper_context.exception.__cause__)

    def test_is_deterministic_immutable_and_does_not_mutate_inputs(self) -> None:
        participants = _participants()
        turns = (_turn(1), _turn(2), _turn(3), _turn(4))
        before_participants = tuple(asdict(value) for value in participants)
        before_turns = tuple(asdict(value) for value in turns)

        first = run_synthetic_two_policy_interaction_smoke(participants, turns)
        second = run_synthetic_two_policy_interaction_smoke(participants, turns)

        self.assertEqual(first, second)
        self.assertEqual(
            tuple(asdict(value) for value in participants), before_participants
        )
        self.assertEqual(tuple(asdict(value) for value in turns), before_turns)
        with self.assertRaises(FrozenInstanceError):
            first.turn_count = 2  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            first.turn_results[0].turn_id = "changed"  # type: ignore[misc]

    def test_result_and_turn_have_exact_fields_ids_grade_and_warnings(self) -> None:
        result = _run(4)

        self.assertEqual(
            {field.name for field in fields(result)},
            {
                "interaction_version",
                "participant_count",
                "turn_count",
                "max_turns",
                "policy_ids",
                "initial_models",
                "final_models",
                "turn_ids",
                "turn_results",
                "selected_actions",
                "after_actions",
                "global_candidate_transition_record_ids",
                "interaction_applied",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            {field.name for field in fields(result.turn_results[0])},
            {
                "turn_index",
                "turn_id",
                "actor_policy_id",
                "non_actor_policy_id",
                "actor_initial_model",
                "actor_final_model",
                "non_actor_model_before",
                "non_actor_model_after",
                "one_step_result",
                "non_actor_model_unchanged",
            },
        )
        self.assertIsInstance(result, SyntheticTwoPolicyInteractionResult)
        self.assertIsInstance(
            result.turn_results[0], SyntheticTwoPolicyInteractionTurnResult
        )
        self.assertEqual(
            result.interaction_version,
            SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION,
        )
        self.assertEqual(result.participant_count, 2)
        self.assertEqual(result.max_turns, MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS)
        self.assertEqual(len(result.global_candidate_transition_record_ids), 32)
        self.assertEqual(len(set(result.global_candidate_transition_record_ids)), 32)
        self.assertTrue(result.interaction_applied)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        self.assertEqual(
            result.evidence_grade,
            "P8 exact bounded synthetic/local two-policy alternating interaction smoke evidence only",
        )
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "bounded two-policy synthetic/local interaction smoke only",
            "exactly two participants and two or four alternating turns",
            "one reviewed closed-loop call per turn",
            "no general environment, game episode, outcome generation, replay or production self-play",
            "no model loading, persistence, checkpoint or external dependency",
            "not production training, inference or evaluation",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_surface_has_one_turn_loop_and_no_copied_logic(self) -> None:
        self.assertIs(
            run_synthetic_two_policy_interaction_smoke,
            interaction_module.run_synthetic_two_policy_interaction_smoke,
        )
        self.assertEqual(
            set(interaction_module.__all__),
            {
                "SYNTHETIC_TWO_POLICY_INTERACTION_SMOKE_VERSION",
                "MAX_SYNTHETIC_TWO_POLICY_INTERACTION_TURNS",
                "SyntheticTwoPolicyParticipantInput",
                "SyntheticTwoPolicyInteractionTurnInput",
                "SyntheticTwoPolicyInteractionTurnResult",
                "SyntheticTwoPolicyInteractionSmokeError",
                "SyntheticTwoPolicyInteractionResult",
                "run_synthetic_two_policy_interaction_smoke",
            },
        )
        source = inspect.getsource(interaction_module)
        self.assertEqual(source.count("run_synthetic_one_step_policy_improvement_smoke("), 1)
        syntax_tree = ast.parse(source)
        self.assertEqual(
            sum(isinstance(node, ast.For) for node in ast.walk(syntax_tree)),
            1,
        )
        self.assertEqual(
            sum(isinstance(node, ast.While) for node in ast.walk(syntax_tree)),
            0,
        )
        for forbidden in (
            "target - prediction",
            "weights[action_index]",
            "action_one_value > action_zero_value",
            "random.",
        ):
            self.assertNotIn(forbidden, source)
        public_text = " ".join(interaction_module.__all__).lower()
        for forbidden in (
            "path",
            "file",
            "loader",
            "persistence",
            "environment",
            "replay",
            "checkpoint",
            "evaluation",
        ):
            self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
