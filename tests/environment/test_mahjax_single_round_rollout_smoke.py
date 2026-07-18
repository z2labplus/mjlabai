from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.environment.mahjax_single_round_rollout_smoke as rollout_module  # noqa: E402
from mjlabai.environment import (  # noqa: E402
    MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION,
    MAHJAX_SINGLE_ROUND_TRANSITION_CAP,
    MahJaxSingleRoundRolloutResult,
    MahJaxSingleRoundRolloutSmokeError,
    MahJaxSingleRoundStep,
    run_mahjax_single_round_rollout_smoke,
)


class MahJaxSingleRoundRolloutSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_single_round_rollout_smoke(seed=0)

    def test_exact_public_surface_and_frozen_objects(self) -> None:
        self.assertEqual(
            set(rollout_module.__all__),
            {
                "MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION",
                "MAHJAX_SINGLE_ROUND_TRANSITION_CAP",
                "MahJaxSingleRoundRolloutSmokeError",
                "MahJaxSingleRoundStep",
                "MahJaxSingleRoundRolloutResult",
                "run_mahjax_single_round_rollout_smoke",
            },
        )
        self.assertEqual(MAHJAX_SINGLE_ROUND_TRANSITION_CAP, 256)
        self.assertEqual(
            self.result.rollout_version,
            MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxSingleRoundRolloutResult)
        self.assertIsInstance(self.result.trace[0], MahJaxSingleRoundStep)
        self.assertEqual(
            {field.name for field in fields(self.result.trace[0])},
            {"pre_step_index", "acting_player", "legal_actions", "selected_action"},
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]
        with self.assertRaises(FrozenInstanceError):
            self.result.trace[0].selected_action = 0  # type: ignore[misc]

    def test_pins_package_environment_and_dependency_identity(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        pyproject = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('"mahjax==0.1.2"', pyproject)
        self.assertIn('"jax==0.4.30"', pyproject)
        self.assertIn('"jaxlib==0.4.30"', pyproject)

    def test_seed_zero_exact_terminal_result(self) -> None:
        self.assertEqual(self.result.seed, 0)
        self.assertEqual(self.result.transition_count, 94)
        self.assertEqual(self.result.final_step_count, 94)
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(self.result.final_rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(self.result.cumulative_rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(self.result.final_scores, (250, 250, 250, 250))

    def test_trace_is_complete_monotonic_and_uses_lowest_legal_action(self) -> None:
        self.assertEqual(len(self.result.trace), self.result.transition_count)
        self.assertEqual(
            tuple(step.pre_step_index for step in self.result.trace),
            tuple(range(self.result.transition_count)),
        )
        for step in self.result.trace:
            self.assertIn(step.acting_player, range(4))
            self.assertTrue(step.legal_actions)
            self.assertEqual(step.legal_actions, tuple(sorted(step.legal_actions)))
            self.assertEqual(len(step.legal_actions), len(set(step.legal_actions)))
            self.assertTrue(all(0 <= action < 87 for action in step.legal_actions))
            self.assertEqual(step.selected_action, step.legal_actions[0])

    def test_rollout_finishes_inside_hard_bound(self) -> None:
        self.assertEqual(self.result.transition_cap, 256)
        self.assertLess(self.result.transition_count, self.result.transition_cap)
        self.assertEqual(self.result.final_step_count, self.result.transition_count)
        self.assertIn(self.result.initial_player, range(4))
        self.assertIn(self.result.final_player, range(4))

    def test_rewards_are_raw_unshaped_four_tuples(self) -> None:
        self.assertIs(type(self.result.final_rewards), tuple)
        self.assertIs(type(self.result.cumulative_rewards), tuple)
        self.assertEqual(len(self.result.final_rewards), 4)
        self.assertEqual(len(self.result.cumulative_rewards), 4)
        self.assertTrue(all(type(value) is float for value in self.result.final_rewards))
        self.assertTrue(
            all(type(value) is float for value in self.result.cumulative_rewards)
        )

    def test_is_deterministic_for_equal_seed(self) -> None:
        self.assertEqual(self.result, run_mahjax_single_round_rollout_smoke(seed=0))

    def test_rejects_invalid_seed_before_runtime_use(self) -> None:
        for invalid_seed in (True, -1, 2**32, 0.0, "0", None):
            with self.subTest(seed=invalid_seed):
                with mock.patch.object(
                    rollout_module,
                    "_load_pinned_runtime",
                    side_effect=AssertionError("runtime must not load"),
                ):
                    with self.assertRaisesRegex(
                        MahJaxSingleRoundRolloutSmokeError,
                        "seed must be an exact int",
                    ):
                        run_mahjax_single_round_rollout_smoke(  # type: ignore[arg-type]
                            invalid_seed
                        )

    def test_cap_exhaustion_is_an_explicit_error(self) -> None:
        with mock.patch.object(
            rollout_module,
            "MAHJAX_SINGLE_ROUND_TRANSITION_CAP",
            1,
        ):
            with self.assertRaisesRegex(
                MahJaxSingleRoundRolloutSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_single_round_rollout_smoke(seed=0)

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P4 pinned local single-round environment rollout smoke evidence",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "local cpu single-round rollout smoke only",
            "lowest-legal-action diagnostic policy only",
            "not full tenhou-rule conformance",
            "no real tenhou, real haifu, external log or platform data",
            "no model output, learning, training, production self-play or league",
            "raw environment rewards are recorded without shaping",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_is_one_bounded_loop_and_one_jitted_step(self) -> None:
        source = inspect.getsource(rollout_module)
        tree = ast.parse(source)
        self.assertEqual(sum(isinstance(node, ast.For) for node in ast.walk(tree)), 1)
        self.assertEqual(sum(isinstance(node, ast.While) for node in ast.walk(tree)), 0)
        jit_calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "jax"
            and node.func.attr == "jit"
        ]
        self.assertEqual(len(jit_calls), 1)
        imported_modules = {
            node.module.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        }
        imported_modules.update(
            alias.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
        self.assertTrue(
            imported_modules
            <= {"__future__", "dataclasses", "jax", "mahjax", "mjlabai", "typing"}
        )
        for forbidden in (
            "Path(",
            "open(",
            "requests",
            "socket",
            "subprocess",
            "optimizer",
            "checkpoint",
            "policy_callback",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
