import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = REPO_ROOT / "tests/fixtures/eval/tiny_benchmark_harness_smoke.json"

REQUIRED_TOP_LEVEL_KEYS = {
    "schema_version",
    "fixture_id",
    "evaluation_stage",
    "fixture_type",
    "source_note",
    "warnings",
    "intended_safety_flags",
    "diagnostic_metric_names",
    "legal_action_diagnostics",
    "latency_diagnostics",
    "fixed_position_decision_diagnostics",
}
REQUIRED_NOTE_TERMS = (
    "synthetic",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not model strength",
    "not luckyj",
)
REQUIRED_SOURCE_TERMS = REQUIRED_NOTE_TERMS + (
    "not platform data",
    "not model output",
    "not candidate promotion",
    "not full action-space",
)
REQUIRED_SAFETY_FLAGS = {
    "training_related",
    "self_play_related",
    "league_related",
    "tenhou_related",
    "platform_automation_related",
    "uses_real_platform_data",
    "uses_external_log",
    "uses_third_party_artifact",
}
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
REQUIRED_LEGAL_ACTION_METRICS = {
    "legal_action_rate",
    "invalid_action_rate",
    "missing_action_rate",
    "parse_failure_rate",
    "evaluated_decision_count",
    "skipped_count",
}
REQUIRED_LATENCY_METRICS = {
    "latency_ms_mean",
    "latency_ms_p50",
    "latency_ms_p95",
    "latency_ms_max",
}
BANNED_LATENCY_FIELDS = {
    "measured_latency_ms",
    "actual_latency_ms",
    "benchmark_result",
    "real_tenhou_latency",
    "gpu_throughput",
    "training_throughput",
    "self_play_throughput",
    "league_throughput",
}


class TinyBenchmarkHarnessFixtureSchemaSmokeTest(unittest.TestCase):
    """Schema smoke test only.

    This test validates a project-authored synthetic/local fixture shape for a
    future tiny benchmark harness. It does not import or call evaluator code,
    does not measure latency, and does not calculate benchmark metrics or
    fixed-position exact-match results.
    """

    def test_tiny_benchmark_harness_fixture_shape(self) -> None:
        self.assertTrue(FIXTURE_PATH.exists())

        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.assertIsInstance(fixture, dict)
        self.assertTrue(REQUIRED_TOP_LEVEL_KEYS.issubset(fixture.keys()))
        self.assertEqual(
            fixture["schema_version"],
            "tiny_benchmark_harness_fixture_v0.1",
        )
        self.assertTrue(fixture["fixture_id"])
        self.assertEqual(fixture["evaluation_stage"], "P5")
        self.assertEqual(
            fixture["fixture_type"],
            "tiny_benchmark_harness_schema_smoke",
        )
        self._assert_note_terms(fixture["source_note"], REQUIRED_SOURCE_TERMS)
        self._assert_warnings(fixture["warnings"])
        self._assert_safety_flags(fixture["intended_safety_flags"])
        self._assert_metric_names(fixture["diagnostic_metric_names"])
        self._assert_legal_action_diagnostics(fixture["legal_action_diagnostics"])
        self._assert_latency_diagnostics(fixture["latency_diagnostics"])
        self._assert_fixed_position_diagnostics(
            fixture["fixed_position_decision_diagnostics"],
        )

    def _assert_warnings(self, warnings: object) -> None:
        self.assertIsInstance(warnings, list)
        warning_text = " ".join(str(warning) for warning in warnings)
        self._assert_note_terms(warning_text, REQUIRED_NOTE_TERMS)
        self.assertIn("not candidate promotion", warning_text.lower())
        self.assertIn("not full action-space", warning_text.lower())

    def _assert_safety_flags(self, flags: object) -> None:
        self.assertIsInstance(flags, dict)
        self.assertEqual(set(flags.keys()), REQUIRED_SAFETY_FLAGS)
        for name, value in flags.items():
            self.assertIs(value, False, name)

    def _assert_metric_names(self, metric_names: object) -> None:
        self.assertIsInstance(metric_names, list)
        metrics = set(metric_names)
        self.assertTrue(REQUIRED_DIAGNOSTIC_METRICS.issubset(metrics))

    def _assert_legal_action_diagnostics(self, section: object) -> None:
        self.assertIsInstance(section, dict)
        self.assertEqual(section.get("source_kind"), "synthetic_fixture_reference")
        self.assertEqual(
            section.get("fixture_path"),
            "tests/fixtures/eval/legal_action_metric_smoke.json",
        )
        self.assertIn("dahai only", section.get("allowed_scope", ()))
        self.assertIn("strict matching only", section.get("allowed_scope", ()))
        self.assertTrue(
            REQUIRED_LEGAL_ACTION_METRICS.issubset(
                set(section.get("metric_names", ())),
            )
        )
        interpretation = " ".join(section.get("interpretation", ())).lower()
        self.assertIn("legality diagnostic", interpretation)
        self.assertIn("not strength", interpretation)
        self.assertIn("not luckyj", interpretation)

    def _assert_latency_diagnostics(self, section: object) -> None:
        self.assertIsInstance(section, dict)
        self.assertEqual(section.get("source_kind"), "synthetic_latency_plan")
        self.assertEqual(
            section.get("timing_method"),
            "perf_counter_ns_or_equivalent_future_plan",
        )
        self.assertEqual(type(section.get("repetitions")), int)
        self.assertGreater(section["repetitions"], 0)
        self.assertEqual(type(section.get("sample_count")), int)
        self.assertGreater(section["sample_count"], 0)
        self.assertEqual(
            section.get("target_kind"),
            "synthetic_local_evaluation_path_future_placeholder",
        )
        self.assertTrue(BANNED_LATENCY_FIELDS.isdisjoint(section.keys()))
        self.assertTrue(
            REQUIRED_LATENCY_METRICS.issubset(set(section.get("metric_names", ()))),
        )
        required_repro = set(section.get("required_reproducibility_fields", ()))
        self.assertTrue(
            {
                "environment",
                "command_or_test_path",
                "sample_count",
                "timing_method",
                "repetitions",
            }.issubset(required_repro)
        )
        interpretation = " ".join(section.get("interpretation", ())).lower()
        self.assertIn("engineering smoke diagnostic", interpretation)
        self.assertIn("not model strength", interpretation)
        self.assertIn("not training throughput", interpretation)
        self.assertIn("not self-play throughput", interpretation)
        self.assertIn("not league throughput", interpretation)
        self.assertIn("not gpu benchmark", interpretation)

    def _assert_fixed_position_diagnostics(self, section: object) -> None:
        self.assertIsInstance(section, dict)
        self.assertEqual(
            section.get("source_kind"),
            "project_authored_synthetic_fixed_position_records",
        )
        self.assertEqual(section.get("matching_mode"), "strict")
        self.assertEqual(section.get("action_scope"), "dahai")
        records = section.get("records")
        self.assertIsInstance(records, list)
        self.assertGreater(len(records), 0)

        for record in records:
            self._assert_fixed_position_record(record)

    def _assert_fixed_position_record(self, record: object) -> None:
        self.assertIsInstance(record, dict)
        required_keys = {
            "record_id",
            "source_note",
            "synthetic_position_id",
            "decision_context",
            "candidate_actions",
            "expected_action",
            "metric_names",
        }
        self.assertTrue(required_keys.issubset(record.keys()))
        self._assert_note_terms(record["source_note"], REQUIRED_NOTE_TERMS)

        decision_context = record["decision_context"]
        self.assertIsInstance(decision_context, dict)
        self.assertEqual(decision_context.get("round_id"), "synthetic_round_0")
        self.assertEqual(decision_context.get("actor"), 0)
        self.assertEqual(decision_context.get("turn_index"), 0)
        self.assertIn("synthetic", decision_context.get("observation_stub", ""))
        self.assertIs(decision_context.get("no_real_haifu"), True)

        candidate_actions = record["candidate_actions"]
        self.assertIsInstance(candidate_actions, list)
        self.assertGreater(len(candidate_actions), 0)
        for action in candidate_actions:
            self._assert_canonical_dahai_action(action)
        self._assert_canonical_dahai_action(record["expected_action"])

        metric_names = set(record["metric_names"])
        self.assertIn("fixed_position_decision_count", metric_names)
        self.assertIn("fixed_position_exact_match_rate", metric_names)
        interpretation = " ".join(record.get("interpretation", ())).lower()
        self.assertIn("future diagnostic expectation only", interpretation)
        self.assertIn("not supervised label", interpretation)
        self.assertIn("not policy-quality evidence", interpretation)
        self.assertIn("not strength evidence", interpretation)

    def _assert_canonical_dahai_action(self, action: object) -> None:
        self.assertIsInstance(action, dict)
        self.assertEqual(action.get("schema_version"), "canonical_action_v0.1")
        self.assertEqual(type(action.get("actor")), int)
        self.assertIn(action.get("actor"), {0, 1, 2, 3})
        self.assertEqual(action.get("action_type"), "dahai")
        self.assertIsInstance(action.get("tile"), str)
        self.assertTrue(action["tile"])
        self.assertEqual(type(action.get("tsumogiri")), bool)

        raw_action = action.get("raw_action")
        if raw_action is not None:
            self.assertIsInstance(raw_action, dict)
            self.assertEqual(raw_action.get("type"), "dahai")
            self.assertEqual(raw_action.get("actor"), action.get("actor"))
            self.assertIsInstance(raw_action.get("pai"), str)
            self.assertEqual(type(raw_action.get("tsumogiri")), bool)

        metadata = action.get("metadata")
        if metadata is not None:
            self.assertIsInstance(metadata, dict)
            self.assertIs(metadata.get("not_part_of_equality"), True)

    def _assert_note_terms(self, value: object, required_terms: tuple[str, ...]) -> None:
        self.assertIsInstance(value, str)
        text = value.lower()
        for term in required_terms:
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
