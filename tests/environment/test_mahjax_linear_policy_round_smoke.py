from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, fields
import inspect
import math
from pathlib import Path
import sys
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import jax  # noqa: E402
import mahjax  # noqa: E402
import mjlabai.environment.mahjax_linear_policy_round_smoke as smoke_module  # noqa: E402
from mjlabai.environment import (  # noqa: E402
    MAHJAX_LINEAR_POLICY_ACTION_COUNT,
    MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION,
    MAHJAX_LINEAR_POLICY_TRANSITION_CAP,
    MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT,
    MahJaxLinearPolicyRoundResult,
    MahJaxLinearPolicyRoundSmokeError,
    MahJaxLinearPolicyStep,
    encode_mahjax_public_observation,
    run_mahjax_linear_policy_round_smoke,
)


class MahJaxLinearPolicyRoundSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root_key = jax.random.PRNGKey(0)
        init_key, _ = jax.random.split(root_key)
        environment = mahjax.make(
            "red_mahjong",
            round_mode="single",
            observe_type="dict",
            next_round_style="auto",
        )
        cls.observation = environment.observe(environment.init(init_key))
        cls.features = encode_mahjax_public_observation(cls.observation)
        cls.result = run_mahjax_linear_policy_round_smoke(0)

    def test_exact_public_surface_and_frozen_objects(self) -> None:
        self.assertEqual(
            set(smoke_module.__all__),
            {
                "MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION",
                "MAHJAX_LINEAR_POLICY_TRANSITION_CAP",
                "MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT",
                "MAHJAX_LINEAR_POLICY_ACTION_COUNT",
                "MahJaxLinearPolicyRoundSmokeError",
                "MahJaxLinearPolicyStep",
                "MahJaxLinearPolicyRoundResult",
                "encode_mahjax_public_observation",
                "run_mahjax_linear_policy_round_smoke",
            },
        )
        self.assertEqual(MAHJAX_LINEAR_POLICY_TRANSITION_CAP, 256)
        self.assertEqual(MAHJAX_PUBLIC_OBSERVATION_FEATURE_COUNT, 630)
        self.assertEqual(MAHJAX_LINEAR_POLICY_ACTION_COUNT, 87)
        self.assertEqual(
            self.result.smoke_version,
            MAHJAX_LINEAR_POLICY_ROUND_SMOKE_VERSION,
        )
        self.assertIsInstance(self.result, MahJaxLinearPolicyRoundResult)
        self.assertIsInstance(self.result.trace[0], MahJaxLinearPolicyStep)
        self.assertEqual(
            {field.name for field in fields(self.result.trace[0])},
            {
                "pre_step_index",
                "acting_player",
                "legal_actions",
                "selected_action",
                "selected_action_score",
            },
        )
        with self.assertRaises(FrozenInstanceError):
            self.result.seed = 1  # type: ignore[misc]

    def test_encoder_returns_exact_finite_immutable_public_features(self) -> None:
        self.assertIs(type(self.features), tuple)
        self.assertEqual(len(self.features), 630)
        self.assertTrue(all(type(value) is float for value in self.features))
        self.assertTrue(all(math.isfinite(value) for value in self.features))
        self.assertAlmostEqual(
            self.features[0],
            float(self.observation["hand"][0]) / 36.0,
            places=7,
        )
        self.assertAlmostEqual(
            self.features[14],
            float(self.observation["last_draw"]) / 36.0,
            places=7,
        )

    def test_encoder_rejects_key_shape_and_nonfinite_drift(self) -> None:
        missing = dict(self.observation)
        missing.pop("hand")
        with self.assertRaisesRegex(
            MahJaxLinearPolicyRoundSmokeError,
            "keys differ",
        ):
            encode_mahjax_public_observation(missing)

        wrong_shape = dict(self.observation)
        wrong_shape["hand"] = self.observation["hand"][:13]
        with self.assertRaisesRegex(
            MahJaxLinearPolicyRoundSmokeError,
            "shapes differ",
        ):
            encode_mahjax_public_observation(wrong_shape)

        nonfinite = dict(self.observation)
        nonfinite["last_draw"] = float("nan")
        with self.assertRaisesRegex(
            MahJaxLinearPolicyRoundSmokeError,
            "must all be finite",
        ):
            encode_mahjax_public_observation(nonfinite)

    def test_pins_runtime_environment_and_project_model_identity(self) -> None:
        self.assertEqual(self.result.package_version, "0.1.2")
        self.assertEqual(self.result.environment_id, "red_mahjong")
        self.assertEqual(self.result.environment_version, "beta")
        self.assertEqual(
            self.result.model_id,
            "project_random_linear_630x87_jax_normal_scale_0.01",
        )
        self.assertEqual(self.result.feature_count, 630)
        self.assertEqual(self.result.action_count, 87)
        self.assertEqual(self.result.parameter_count, 54_897)

    def test_seed_zero_exact_terminal_result(self) -> None:
        self.assertEqual(self.result.transition_count, 91)
        self.assertEqual(self.result.final_step_count, 91)
        self.assertTrue(self.result.terminated)
        self.assertFalse(self.result.truncated)
        self.assertEqual(self.result.final_rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(self.result.cumulative_rewards, (0.0, 0.0, 0.0, 0.0))
        self.assertEqual(self.result.final_scores, (250, 250, 250, 250))

    def test_trace_is_complete_and_every_masked_model_action_is_legal(self) -> None:
        self.assertEqual(len(self.result.trace), self.result.transition_count)
        self.assertEqual(
            tuple(step.pre_step_index for step in self.result.trace),
            tuple(range(self.result.transition_count)),
        )
        for step in self.result.trace:
            self.assertIn(step.acting_player, range(4))
            self.assertTrue(step.legal_actions)
            self.assertEqual(step.legal_actions, tuple(sorted(step.legal_actions)))
            self.assertIn(step.selected_action, step.legal_actions)
            self.assertTrue(math.isfinite(step.selected_action_score))

    def test_is_deterministic_and_pins_first_and_final_actions(self) -> None:
        self.assertEqual(self.result, run_mahjax_linear_policy_round_smoke(0))
        self.assertEqual(self.result.trace[0].selected_action, 10)
        self.assertEqual(self.result.trace[-1].selected_action, 7)

    def test_rejects_invalid_seed_before_runtime_use(self) -> None:
        for invalid_seed in (True, -1, 2**32, 0.0, "0", None):
            with self.subTest(seed=invalid_seed):
                with mock.patch.object(
                    smoke_module,
                    "_load_pinned_runtime",
                    side_effect=AssertionError("runtime must not load"),
                ):
                    with self.assertRaisesRegex(
                        MahJaxLinearPolicyRoundSmokeError,
                        "seed must be an exact int",
                    ):
                        run_mahjax_linear_policy_round_smoke(  # type: ignore[arg-type]
                            invalid_seed
                        )

    def test_cap_exhaustion_is_explicit(self) -> None:
        with mock.patch.object(
            smoke_module,
            "MAHJAX_LINEAR_POLICY_TRANSITION_CAP",
            1,
        ):
            with self.assertRaisesRegex(
                MahJaxLinearPolicyRoundSmokeError,
                "exceeded the 1-transition cap",
            ):
                run_mahjax_linear_policy_round_smoke(0)

    def test_evidence_grade_and_warnings_prevent_overclaim(self) -> None:
        self.assertTrue(self.result.safety_guardrails_all_satisfied)
        self.assertEqual(
            self.result.evidence_grade,
            "P4/P8 project-owned untrained model-output-to-environment smoke evidence only",
        )
        warning_text = " ".join(self.result.warnings).lower()
        for phrase in (
            "random-initialized linear-policy local round only",
            "630 public observation features and 87 action scores",
            "environment legal mask is authoritative",
            "parameters are untrained",
            "no hidden opponent hand or private environment-state feature",
            "no labels, dataset, loss, gradient, optimizer or training",
            "no real tenhou, real haifu, external log or platform data",
            "not production self-play, league or evaluation",
            "not policy-quality or model-strength evidence",
            "not stable-dan or luckyj 10.68 comparison",
        ):
            self.assertIn(phrase, warning_text)

    def test_source_has_two_jits_one_loop_and_public_observation_only(self) -> None:
        source = inspect.getsource(smoke_module)
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
        self.assertEqual(len(jit_calls), 2)
        self.assertIn("observation = environment.observe(state)", source)
        self.assertIn("state.round_state.score", source)
        for forbidden in (
            "state.players.hand",
            "opponent_private",
            "Path(",
            "open(",
            "requests",
            "subprocess",
            "gradient(",
            "optimizer(",
            "checkpoint(",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
