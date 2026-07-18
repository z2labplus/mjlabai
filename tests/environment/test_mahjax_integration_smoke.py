from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import mjlabai.environment.mahjax_integration_smoke as integration_module  # noqa: E402
from mjlabai.environment import (  # noqa: E402
    MAHJAX_ENVIRONMENT_ID,
    MAHJAX_ENVIRONMENT_VERSION,
    MAHJAX_INTEGRATION_SMOKE_VERSION,
    MAHJAX_PACKAGE_VERSION,
    MahJaxIntegrationSmokeError,
    MahJaxIntegrationSmokeResult,
    run_mahjax_integration_smoke,
)


class MahJaxIntegrationSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_mahjax_integration_smoke()

    def test_pinned_package_and_environment_identity(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.package_version, MAHJAX_PACKAGE_VERSION)
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_id, MAHJAX_ENVIRONMENT_ID)
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(
            self.result.environment_version,
            MAHJAX_ENVIRONMENT_VERSION,
        )

    def test_exposes_four_players_and_pinned_action_space(self) -> None:
        self.assertEqual(self.result.num_players, 4)
        self.assertEqual(self.result.num_actions, 87)

    def test_uses_environment_owned_nonempty_legal_mask(self) -> None:
        self.assertEqual(self.result.initial_legal_action_count, 12)
        self.assertEqual(self.result.selected_action, 2)
        self.assertEqual(self.result.next_legal_action_count, 13)

    def test_observation_matches_pinned_public_dict_surface(self) -> None:
        self.assertEqual(
            set(self.result.observation_keys),
            {
                "action_history",
                "dora_indicators",
                "furiten",
                "hand",
                "honba",
                "kyotaku",
                "last_draw",
                "prevalent_wind",
                "round",
                "scores",
                "seat_wind",
                "shanten_count",
            },
        )

    def test_executes_one_legal_state_transition(self) -> None:
        self.assertEqual(self.result.initial_step_count, 0)
        self.assertEqual(self.result.next_step_count, 1)
        self.assertEqual(self.result.initial_player, 2)
        self.assertEqual(self.result.next_player, 3)
        self.assertEqual(self.result.rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertFalse(self.result.terminated)
        self.assertFalse(self.result.truncated)

    def test_is_deterministic_for_the_same_seed(self) -> None:
        self.assertEqual(self.result, run_mahjax_integration_smoke(seed=0))

    def test_rejects_invalid_seed_before_runtime_use(self) -> None:
        for invalid_seed in (True, -1, 2**32, 0.0, "0", None):
            with self.subTest(seed=invalid_seed):
                with self.assertRaisesRegex(
                    MahJaxIntegrationSmokeError,
                    "seed must be an exact int",
                ):
                    run_mahjax_integration_smoke(invalid_seed)  # type: ignore[arg-type]

    def test_result_is_frozen_and_has_exact_fields(self) -> None:
        self.assertIsInstance(self.result, MahJaxIntegrationSmokeResult)
        self.assertEqual(
            {field.name for field in fields(self.result)},
            {
                "integration_version",
                "package_version",
                "environment_id",
                "environment_version",
                "num_players",
                "num_actions",
                "seed",
                "initial_player",
                "initial_step_count",
                "initial_legal_action_count",
                "selected_action",
                "observation_keys",
                "next_player",
                "next_step_count",
                "next_legal_action_count",
                "rewards",
                "terminated",
                "truncated",
                "safety_guardrails_all_satisfied",
                "evidence_grade",
                "warnings",
            },
        )
        self.assertEqual(
            self.result.integration_version,
            MAHJAX_INTEGRATION_SMOKE_VERSION,
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P4 pinned third-party local riichi environment integration smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "pinned mahjax v0.1.2 local cpu integration smoke only",
            "one environment-owned legal action and one state transition only",
            "not full tenhou-rule conformance or complete gameplay evidence",
            "no real tenhou, real haifu, external log or platform data",
            "no model output, training, self-play, league or production evaluation",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
            "not candidate-promotion evidence",
        ):
            self.assertIn(phrase, warning_text)

    def test_surface_has_no_path_network_model_or_training_behavior(self) -> None:
        self.assertIs(
            run_mahjax_integration_smoke,
            integration_module.run_mahjax_integration_smoke,
        )
        self.assertEqual(
            set(integration_module.__all__),
            {
                "MAHJAX_ENVIRONMENT_ID",
                "MAHJAX_ENVIRONMENT_VERSION",
                "MAHJAX_INTEGRATION_SMOKE_VERSION",
                "MAHJAX_PACKAGE_VERSION",
                "MahJaxIntegrationSmokeError",
                "MahJaxIntegrationSmokeResult",
                "run_mahjax_integration_smoke",
            },
        )
        source = inspect.getsource(integration_module)
        tree = ast.parse(source)
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
            <= {"__future__", "dataclasses", "jax", "mahjax", "typing"}
        )
        for forbidden in (
            "Path(",
            "open(",
            "requests",
            "socket",
            "subprocess",
            "tenhou",
            "training_step",
            "optimizer",
        ):
            self.assertNotIn(forbidden, source)

    def test_pyproject_pins_exact_runtime(self) -> None:
        pyproject = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('"mahjax==0.1.2"', pyproject)
        self.assertIn('"jax==0.4.30"', pyproject)
        self.assertIn('"jaxlib==0.4.30"', pyproject)


if __name__ == "__main__":
    unittest.main()
