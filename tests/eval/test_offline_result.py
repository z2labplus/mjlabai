import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval import (
    EvaluationMetricDefinition,
    OfflineCommandStatus,
    OfflineConfidenceInterval,
    OfflineEvaluationMetricValue,
    OfflineEvaluationResultEnvelope,
    OfflineEvaluationSafetyFlags,
    OfflineReproducibilityMetadata,
    get_metric_definition,
    list_metric_definitions,
)


class OfflineResultTests(unittest.TestCase):
    def test_metric_registry_contains_stable_dan_and_wrapper_metrics(self):
        names = {definition.metric_name for definition in list_metric_definitions()}

        self.assertIn("stable_dan_point_estimate", names)
        self.assertIn("stable_dan_ci_lower", names)
        self.assertIn("stable_dan_ci_upper", names)
        self.assertIn("stable_dan_threshold_outcome", names)
        self.assertIn("stable_dan_sample_size_status", names)
        self.assertIn("legal_action_rate", names)
        self.assertIn("invalid_action_rate", names)
        self.assertIn("evaluated_decision_count", names)
        self.assertIn("legal_action_count", names)
        self.assertIn("invalid_action_count", names)
        self.assertIn("missing_action_count", names)
        self.assertIn("parse_failure_count", names)
        self.assertIn("skipped_count", names)
        self.assertIn("missing_action_rate", names)
        self.assertIn("parse_failure_rate", names)
        self.assertIn("command_exit_code", names)
        self.assertIn("latency_ms", names)
        self.assertIn("parse_success_rate", names)
        self.assertIn("wrapper_smoke_success", names)

    def test_get_metric_definition(self):
        definition = get_metric_definition("stable_dan_point_estimate")

        self.assertIsInstance(definition, EvaluationMetricDefinition)
        self.assertEqual(definition.metric_unit, "dan")
        self.assertTrue(definition.higher_is_better)

    def test_legal_action_metric_registry_directions(self):
        count_definition = get_metric_definition("evaluated_decision_count")
        self.assertEqual(count_definition.metric_unit, "count")
        self.assertIsNone(count_definition.higher_is_better)

        missing_rate_definition = get_metric_definition("missing_action_rate")
        self.assertEqual(missing_rate_definition.metric_unit, "rate")
        self.assertFalse(missing_rate_definition.higher_is_better)

    def test_unknown_metric_definition_raises(self):
        with self.assertRaises(ValueError):
            get_metric_definition("not_a_metric")

    def test_metric_value_to_dict_uses_registry_defaults(self):
        metric = OfflineEvaluationMetricValue(
            metric_name="latency_ms",
            value=12.5,
            sample_size=1,
        )

        self.assertEqual(metric.metric_unit, "ms")
        self.assertFalse(metric.higher_is_better)
        self.assertEqual(metric.to_dict()["value"], 12.5)

    def test_confidence_interval_validation(self):
        interval = OfflineConfidenceInterval(
            lower_bound=1.0,
            upper_bound=2.0,
            confidence_level=0.95,
            method="percentile_bootstrap",
        )

        self.assertEqual(interval.to_dict()["method"], "percentile_bootstrap")

    def test_confidence_interval_lower_above_upper_raises(self):
        with self.assertRaises(ValueError):
            OfflineConfidenceInterval(
                lower_bound=2.0,
                upper_bound=1.0,
                confidence_level=0.95,
                method="percentile_bootstrap",
            )

    def test_confidence_interval_invalid_level_raises(self):
        with self.assertRaises(ValueError):
            OfflineConfidenceInterval(
                lower_bound=1.0,
                upper_bound=2.0,
                confidence_level=1.0,
                method="percentile_bootstrap",
            )

    def test_envelope_to_dict_is_json_serializable(self):
        envelope = _make_envelope()
        envelope_dict = envelope.to_dict()

        self.assertEqual(envelope_dict["schema_version"], "offline_evaluation_result_v0.1")
        self.assertEqual(envelope_dict["evaluation_stage"], "P5")
        self.assertEqual(envelope_dict["metrics"][0]["metric_name"], "stable_dan_point_estimate")
        json.dumps(envelope_dict, sort_keys=True)

    def test_empty_evaluation_id_raises(self):
        with self.assertRaises(ValueError):
            _make_envelope(evaluation_id="")

    def test_empty_metrics_raises(self):
        with self.assertRaises(ValueError):
            _make_envelope(metrics=())

    def test_negative_latency_raises(self):
        with self.assertRaises(ValueError):
            _make_envelope(latency_ms=-0.1)

    def test_negative_sample_size_raises(self):
        with self.assertRaises(ValueError):
            _make_envelope(sample_size=-1)

    def test_command_status_bounded_summary(self):
        status = OfflineCommandStatus(
            command_name="wrapper_smoke",
            exit_code=0,
            success=True,
            stdout_summary="ok",
            stderr_summary=None,
        )

        self.assertTrue(status.to_dict()["success"])

    def test_high_risk_safety_flags_are_recorded_as_warnings(self):
        envelope = _make_envelope(
            safety=OfflineEvaluationSafetyFlags(
                training_related=True,
                tenhou_related=True,
            )
        )

        self.assertTrue(envelope.safety.training_related)
        self.assertIn("high-risk safety flag set: training_related", envelope.warnings)
        self.assertIn("high-risk safety flag set: tenhou_related", envelope.warnings)

    def test_high_risk_flags_do_not_execute_actions(self):
        envelope = _make_envelope(
            safety=OfflineEvaluationSafetyFlags(uses_external_log=True),
            warnings=("schema records risk only",),
        )

        self.assertIn("schema records risk only", envelope.warnings)
        self.assertIn("high-risk safety flag set: uses_external_log", envelope.warnings)


def _make_envelope(**overrides):
    values = {
        "evaluation_id": "synthetic-eval-001",
        "evaluation_stage": "P5",
        "evaluation_type": "stable_dan_report_smoke",
        "model_or_tool_id": "synthetic-smoke-model",
        "dataset_or_fixture_id": "synthetic-stable-dan-smoke-fixture",
        "room": "phoenix",
        "ruleset": "tenhou_four_player_phoenix",
        "metrics": (
            OfflineEvaluationMetricValue(
                metric_name="stable_dan_point_estimate",
                value=11.5,
                sample_size=100,
            ),
            OfflineEvaluationMetricValue(
                metric_name="stable_dan_threshold_outcome",
                value="point_estimate_only",
                sample_size=100,
            ),
        ),
        "sample_size": 100,
        "confidence_interval": OfflineConfidenceInterval(
            lower_bound=8.0,
            upper_bound=14.0,
            confidence_level=0.95,
            method="empirical_multinomial_percentile_bootstrap",
        ),
        "command_status": OfflineCommandStatus(
            command_name="synthetic_smoke_test",
            exit_code=0,
            success=True,
            stdout_summary="1 test passed",
            stderr_summary=None,
        ),
        "latency_ms": 1.5,
        "reproducibility": OfflineReproducibilityMetadata(
            code_commit="local-test",
            fixture_id="tests/fixtures/eval/stable_dan_placements_smoke.json",
            seed=12345,
            environment="unit-test",
        ),
        "safety": OfflineEvaluationSafetyFlags(),
        "warnings": ("synthetic only; not strength evidence",),
        "evidence_refs": ("tests/eval/test_offline_result.py",),
    }
    values.update(overrides)
    return OfflineEvaluationResultEnvelope(**values)


if __name__ == "__main__":
    unittest.main()
