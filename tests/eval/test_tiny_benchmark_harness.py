from __future__ import annotations

import copy
import inspect
import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval import (  # noqa: E402
    PROJECT_TINY_BENCHMARK_FIXTURE_ID,
    TinyBenchmarkHarnessResult,
    build_tiny_benchmark_harness_envelope,
    evaluate_tiny_benchmark_harness_fixture,
    load_project_tiny_benchmark_harness_fixture,
    run_project_tiny_benchmark_harness,
)


REQUIRED_WARNING_WORDS = (
    "synthetic",
    "not Tenhou",
    "not real haifu",
    "not external log",
    "not model strength",
    "not LuckyJ",
    "not candidate promotion",
    "not full action-space",
)
REQUIRED_DIAGNOSTIC_METRICS = {
    "legal_action_rate",
    "invalid_action_rate",
    "missing_action_rate",
    "parse_failure_rate",
    "evaluated_decision_count",
    "skipped_count",
    "latency_ms_mean",
    "latency_ms_p50",
    "latency_ms_p95",
    "latency_ms_max",
    "fixed_position_decision_count",
    "fixed_position_exact_match_rate",
}


class TinyBenchmarkHarnessTests(unittest.TestCase):
    def test_project_harness_loads_fixed_fixture(self) -> None:
        fixture = load_project_tiny_benchmark_harness_fixture()

        self.assertEqual(
            fixture["fixture_id"],
            "tiny_benchmark_harness_smoke_v0.1",
        )
        self.assertEqual(
            fixture["schema_version"],
            "tiny_benchmark_harness_fixture_v0.1",
        )
        self.assertEqual(PROJECT_TINY_BENCHMARK_FIXTURE_ID, fixture["evidence_refs"][0])

    def test_project_harness_result_is_deterministic(self) -> None:
        first_result = run_project_tiny_benchmark_harness()
        second_result = run_project_tiny_benchmark_harness()

        self.assertIsInstance(first_result, TinyBenchmarkHarnessResult)
        self.assertEqual(first_result.to_dict(), second_result.to_dict())
        self.assertEqual(first_result.evaluation_stage, "P5")
        self.assertEqual(
            first_result.fixture_type,
            "tiny_benchmark_harness_schema_smoke",
        )
        self.assertTrue(first_result.smoke_success)
        self.assertEqual(first_result.fixed_position_record_count, 1)
        self.assertTrue(
            REQUIRED_DIAGNOSTIC_METRICS.issubset(
                set(first_result.diagnostic_metric_names),
            )
        )
        warning_text = " ".join(first_result.warnings)
        for expected_word in REQUIRED_WARNING_WORDS:
            self.assertIn(expected_word, warning_text)
        json.dumps(first_result.to_dict(), sort_keys=True)

    def test_run_project_harness_does_not_accept_arbitrary_paths(self) -> None:
        signature = inspect.signature(run_project_tiny_benchmark_harness)

        self.assertEqual(tuple(signature.parameters), ())

    def test_envelope_records_synthetic_harness_smoke_result(self) -> None:
        result = run_project_tiny_benchmark_harness()
        envelope = build_tiny_benchmark_harness_envelope(
            result,
            code_commit="synthetic-local-test",
            environment="unit-test",
        )

        self.assertEqual(envelope.evaluation_stage, "P5")
        self.assertEqual(envelope.evaluation_type, "tiny_benchmark_harness")
        self.assertEqual(
            envelope.model_or_tool_id,
            "synthetic-tiny-benchmark-harness",
        )
        self.assertEqual(envelope.dataset_or_fixture_id, PROJECT_TINY_BENCHMARK_FIXTURE_ID)
        self.assertEqual(envelope.sample_size, 1)
        self.assertIsNone(envelope.latency_ms)
        self.assertEqual(envelope.safety.high_risk_flag_names(), ())

        metric_values = {metric.metric_name: metric.value for metric in envelope.metrics}
        self.assertEqual(metric_values, {"wrapper_smoke_success": True})
        warning_text = " ".join(envelope.warnings)
        for expected_word in REQUIRED_WARNING_WORDS:
            self.assertIn(expected_word, warning_text)
        self.assertIn("tests/eval/test_tiny_benchmark_harness.py", envelope.evidence_refs)
        self.assertIn(PROJECT_TINY_BENCHMARK_FIXTURE_ID, envelope.evidence_refs)
        json.dumps(envelope.to_dict(), sort_keys=True)

    def test_true_safety_flag_is_rejected(self) -> None:
        fixture = copy.deepcopy(load_project_tiny_benchmark_harness_fixture())
        fixture["intended_safety_flags"]["tenhou_related"] = True

        with self.assertRaises(ValueError):
            evaluate_tiny_benchmark_harness_fixture(fixture)

    def test_measured_latency_field_is_rejected(self) -> None:
        fixture = copy.deepcopy(load_project_tiny_benchmark_harness_fixture())
        fixture["latency_diagnostics"]["measured_latency_ms"] = 1.0

        with self.assertRaises(ValueError):
            evaluate_tiny_benchmark_harness_fixture(fixture)


if __name__ == "__main__":
    unittest.main()
