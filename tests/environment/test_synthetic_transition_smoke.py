from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, asdict, fields, replace
import inspect
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.environment.synthetic_transition_smoke as transition_module  # noqa: E402
from mjlabai.environment import (  # noqa: E402
    SYNTHETIC_ENVIRONMENT_ID,
    SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION,
    SYNTHETIC_FOUR_PLAYER_RULESET_ID,
    SyntheticEnvironmentAction,
    SyntheticEnvironmentState,
    SyntheticEnvironmentTransitionResult,
    SyntheticEnvironmentTransitionSmokeError,
    apply_synthetic_environment_transition_smoke,
)


def _action(
    index: int,
    *,
    actor: int = 0,
    tile: str | None = None,
    tsumogiri: bool | None = None,
) -> SyntheticEnvironmentAction:
    return SyntheticEnvironmentAction(
        action_id=f"synthetic-legal-action:{index}",
        actor=actor,
        action_type="dahai",
        tile=tile if tile is not None else ("5pr" if index == 0 else "1s"),
        tsumogiri=tsumogiri if tsumogiri is not None else index == 1,
    )


def _state(*, acting_seat: int = 0) -> SyntheticEnvironmentState:
    return SyntheticEnvironmentState(
        environment_id=SYNTHETIC_ENVIRONMENT_ID,
        environment_version=SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION,
        ruleset_id=SYNTHETIC_FOUR_PLAYER_RULESET_ID,
        episode_id="synthetic-environment-episode:1",
        step_index=0,
        acting_seat=acting_seat,
        legal_actions=(
            _action(0, actor=acting_seat),
            _action(1, actor=acting_seat),
        ),
        terminal=False,
        project_authored=True,
        synthetic=True,
        local_only=True,
        uses_real_data=False,
        uses_external_log=False,
        uses_platform_data=False,
    )


class SyntheticEnvironmentTransitionSmokeTests(unittest.TestCase):
    def test_applies_first_legal_action(self) -> None:
        state = _state()
        result = apply_synthetic_environment_transition_smoke(
            state,
            replace(state.legal_actions[0], action_id="proposal:first"),
        )

        self.assertEqual(result.legal_action_index, 0)
        self.assertEqual(result.applied_action, state.legal_actions[0])
        self.assertEqual(result.proposed_action.action_id, "proposal:first")
        self.assertTrue(result.transition_applied)

    def test_applies_second_legal_action(self) -> None:
        state = _state(acting_seat=3)
        result = apply_synthetic_environment_transition_smoke(
            state,
            replace(state.legal_actions[1], action_id="proposal:second"),
        )

        self.assertEqual(result.legal_action_index, 1)
        self.assertEqual(result.applied_action, state.legal_actions[1])
        self.assertEqual(result.post_state.acting_seat, 0)

    def test_rejects_non_legal_strict_action(self) -> None:
        state = _state()
        illegal = replace(state.legal_actions[0], tile="9m")

        with self.assertRaisesRegex(
            SyntheticEnvironmentTransitionSmokeError,
            "strictly match exactly one",
        ):
            apply_synthetic_environment_transition_smoke(state, illegal)

    def test_validates_exact_state_version_ruleset_and_provenance(self) -> None:
        state = _state()
        invalid_states = (
            replace(state, environment_id="other"),
            replace(state, environment_version="other"),
            replace(state, ruleset_id="other"),
            replace(state, episode_id=""),
            replace(state, acting_seat=4),
            replace(state, project_authored=False),
            replace(state, synthetic=False),
            replace(state, local_only=False),
            replace(state, uses_real_data=True),
            replace(state, uses_external_log=True),
            replace(state, uses_platform_data=True),
        )
        for invalid in invalid_states:
            with self.subTest(state=invalid):
                with self.assertRaises(SyntheticEnvironmentTransitionSmokeError):
                    apply_synthetic_environment_transition_smoke(
                        invalid, state.legal_actions[0]
                    )

    def test_requires_exact_two_legal_actions_bound_to_seat_and_unique(self) -> None:
        class TupleSubclass(tuple):
            pass

        class ActionSubclass(SyntheticEnvironmentAction):
            pass

        state = _state()
        invalid_legal_sets = (
            list(state.legal_actions),
            (state.legal_actions[0],),
            state.legal_actions + (state.legal_actions[0],),
            TupleSubclass(state.legal_actions),
        )
        for legal_actions in invalid_legal_sets:
            with self.assertRaisesRegex(
                SyntheticEnvironmentTransitionSmokeError,
                "exact two-action tuple",
            ):
                apply_synthetic_environment_transition_smoke(
                    replace(state, legal_actions=legal_actions),  # type: ignore[arg-type]
                    state.legal_actions[0],
                )

        subclass = ActionSubclass(**asdict(state.legal_actions[0]))
        wrong_actor = replace(state.legal_actions[1], actor=1)
        duplicate_id = replace(
            state.legal_actions[1],
            action_id=state.legal_actions[0].action_id,
        )
        duplicate_strict = replace(
            state.legal_actions[1],
            tile=state.legal_actions[0].tile,
            tsumogiri=state.legal_actions[0].tsumogiri,
        )
        for legal_actions in (
            (subclass, state.legal_actions[1]),
            (state.legal_actions[0], wrong_actor),
            (state.legal_actions[0], duplicate_id),
            (state.legal_actions[0], duplicate_strict),
        ):
            with self.assertRaises(SyntheticEnvironmentTransitionSmokeError):
                apply_synthetic_environment_transition_smoke(
                    replace(state, legal_actions=legal_actions),
                    state.legal_actions[0],
                )

    def test_strict_matching_ignores_only_action_id(self) -> None:
        state = _state()
        legal = state.legal_actions[0]
        result = apply_synthetic_environment_transition_smoke(
            state,
            replace(legal, action_id="different-audit-id"),
        )
        self.assertEqual(result.legal_action_index, 0)

        strict_variants = (
            replace(legal, actor=1),
            replace(legal, action_type="reach"),
            replace(legal, tile="5p"),
            replace(legal, tsumogiri=not legal.tsumogiri),
        )
        for proposed in strict_variants:
            with self.subTest(proposed=proposed):
                with self.assertRaises(SyntheticEnvironmentTransitionSmokeError):
                    apply_synthetic_environment_transition_smoke(state, proposed)

    def test_preserves_red_indicator_tile_verbatim_without_normalization(self) -> None:
        state = _state()
        result = apply_synthetic_environment_transition_smoke(
            state,
            replace(state.legal_actions[0], action_id="red-proposal"),
        )

        self.assertEqual(result.proposed_action.tile, "5pr")
        self.assertEqual(result.applied_action.tile, "5pr")
        self.assertEqual(result.pre_state.legal_actions[0].tile, "5pr")

    def test_builds_deterministic_monotonic_terminal_post_state(self) -> None:
        state = _state(acting_seat=2)
        result = apply_synthetic_environment_transition_smoke(
            state,
            state.legal_actions[1],
        )

        self.assertEqual(
            result.event_id,
            "synthetic-environment-episode:1:step:0:dahai",
        )
        self.assertEqual(result.post_state.step_index, 1)
        self.assertEqual(result.post_state.acting_seat, 3)
        self.assertEqual(result.post_state.legal_actions, ())
        self.assertTrue(result.post_state.terminal)
        self.assertTrue(result.terminal_reached)
        self.assertEqual(result.post_state.episode_id, state.episode_id)
        self.assertEqual(result.post_state.environment_id, state.environment_id)

    def test_rejects_terminal_reused_and_wrong_index_inputs(self) -> None:
        state = _state()
        invalid_states = (
            replace(state, terminal=True),
            replace(state, step_index=1),
            replace(state, step_index=False),
        )
        for invalid in invalid_states:
            with self.subTest(invalid=invalid):
                with self.assertRaises(SyntheticEnvironmentTransitionSmokeError):
                    apply_synthetic_environment_transition_smoke(
                        invalid, state.legal_actions[0]
                    )

        result = apply_synthetic_environment_transition_smoke(
            state, state.legal_actions[0]
        )
        with self.assertRaises(SyntheticEnvironmentTransitionSmokeError):
            apply_synthetic_environment_transition_smoke(
                result.post_state,
                result.applied_action,
            )

    def test_is_deterministic_frozen_and_does_not_mutate_inputs(self) -> None:
        state = _state()
        proposed = replace(state.legal_actions[0], action_id="proposal")
        before_state = asdict(state)
        before_proposed = asdict(proposed)

        first = apply_synthetic_environment_transition_smoke(state, proposed)
        second = apply_synthetic_environment_transition_smoke(state, proposed)

        self.assertEqual(first, second)
        self.assertEqual(asdict(state), before_state)
        self.assertEqual(asdict(proposed), before_proposed)
        with self.assertRaises(FrozenInstanceError):
            state.step_index = 1  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            proposed.tile = "9s"  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            first.legal_action_index = 1  # type: ignore[misc]

    def test_result_has_exact_fields_flags_grade_and_warnings(self) -> None:
        state = _state()
        result = apply_synthetic_environment_transition_smoke(
            state, state.legal_actions[0]
        )

        self.assertIsInstance(result, SyntheticEnvironmentTransitionResult)
        self.assertEqual(
            {field.name for field in fields(result)},
            {
                "transition_version",
                "pre_state",
                "proposed_action",
                "applied_action",
                "legal_action_index",
                "event_id",
                "post_state",
                "transition_applied",
                "terminal_reached",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            result.transition_version,
            SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION,
        )
        self.assertTrue(result.transition_applied)
        self.assertTrue(result.terminal_reached)
        self.assertTrue(result.safety_guardrails_all_satisfied)
        self.assertEqual(
            result.evidence_grade,
            "P4 exact single-transition synthetic/local environment-contract smoke evidence only",
        )
        warning_text = " ".join(result.warnings).lower()
        for phrase in (
            "exact single-transition synthetic/local environment smoke only",
            "four-seat contract identity and strict dahai matching only",
            "no mahjong hand, tile ownership, rules, scoring, hidden state, rng or multi-step episode",
            "no model, reward, training, self-play or evaluation",
            "no persistence, external dependency or real data",
            "not policy-quality or model-strength evidence",
            "not tenhou, stable-dan or luckyj comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_package_surface_has_no_parser_file_rng_model_or_rl_logic(self) -> None:
        self.assertIs(
            apply_synthetic_environment_transition_smoke,
            transition_module.apply_synthetic_environment_transition_smoke,
        )
        self.assertEqual(
            set(transition_module.__all__),
            {
                "SYNTHETIC_ENVIRONMENT_ID",
                "SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION",
                "SYNTHETIC_FOUR_PLAYER_RULESET_ID",
                "SyntheticEnvironmentAction",
                "SyntheticEnvironmentState",
                "SyntheticEnvironmentTransitionResult",
                "SyntheticEnvironmentTransitionSmokeError",
                "apply_synthetic_environment_transition_smoke",
            },
        )
        source = inspect.getsource(transition_module)
        syntax_tree = ast.parse(source)
        imported_modules = {
            node.module.split(".")[0]
            for node in ast.walk(syntax_tree)
            if isinstance(node, ast.ImportFrom) and node.module
        }
        imported_modules.update(
            alias.name.split(".")[0]
            for node in ast.walk(syntax_tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
        self.assertTrue(imported_modules <= {"__future__", "dataclasses", "typing"})
        for copied_logic in (
            "target - prediction",
            "weights[action_index]",
            "action_one_value > action_zero_value",
            "random.",
            "open(",
            "Path(",
        ):
            self.assertNotIn(copied_logic, source)


if __name__ == "__main__":
    unittest.main()
