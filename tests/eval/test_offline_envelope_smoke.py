from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval import (  # noqa: E402
    OfflineConfidenceInterval,
    OfflineEvaluationMetricValue,
    OfflineEvaluationResultEnvelope,
    OfflineEvaluationSafetyFlags,
    OfflineReproducibilityMetadata,
    aggregate_placement_records,
    bootstrap_stable_dan_ci,
    build_stable_dan_evaluation_report,
    compare_stable_dan_to_threshold,
)


FIXTURE_ID = "tests/fixtures/eval/stable_dan_placements_smoke.json"
FIXTURE_PATH = REPO_ROOT / FIXTURE_ID
ROOM = "phoenix"
RULESET = "tenhou_four_player_phoenix"
N_BOOTSTRAP = 300
CONFIDENCE_LEVEL = 0.95
SEED = 12345


class OfflineEnvelopeSmokeTest(unittest.TestCase):
    def test_synthetic_stable_dan_report_builds_offline_envelope(self) -> None:
        # The fixture is project-authored synthetic data only. It is not Tenhou
        # data, a real haifu/log, model output, league output or strength evidence.
        records = self.load_fixture_records()
        counts = aggregate_placement_records(records, placement_key="placement")
        self.assertEqual(counts.total_games, 100)

        bootstrap = bootstrap_stable_dan_ci(
            **counts.to_stable_dan_kwargs(),
            room=ROOM,
            n_bootstrap=N_BOOTSTRAP,
            confidence_level=CONFIDENCE_LEVEL,
            seed=SEED,
        )
        comparison = compare_stable_dan_to_threshold(bootstrap)
        report = build_stable_dan_evaluation_report(
            bootstrap,
            comparison,
            schema_version="stable_dan_report_smoke_v0.1",
        )

        envelope = OfflineEvaluationResultEnvelope(
            evaluation_id="synthetic-stable-dan-envelope-smoke-001",
            evaluation_stage="P5",
            evaluation_type="stable_dan_report_smoke",
            model_or_tool_id="synthetic-smoke-model",
            dataset_or_fixture_id=FIXTURE_ID,
            room=report.room,
            ruleset=RULESET,
            metrics=(
                OfflineEvaluationMetricValue(
                    metric_name="stable_dan_point_estimate",
                    value=report.point_estimate,
                    sample_size=report.total_games,
                ),
                OfflineEvaluationMetricValue(
                    metric_name="stable_dan_ci_lower",
                    value=report.lower_bound,
                    sample_size=report.total_games,
                ),
                OfflineEvaluationMetricValue(
                    metric_name="stable_dan_ci_upper",
                    value=report.upper_bound,
                    sample_size=report.total_games,
                ),
                OfflineEvaluationMetricValue(
                    metric_name="stable_dan_threshold_outcome",
                    value=report.threshold_outcome,
                    sample_size=report.total_games,
                ),
                OfflineEvaluationMetricValue(
                    metric_name="stable_dan_sample_size_status",
                    value=report.sample_size_assessment.reporting_status,
                    sample_size=report.total_games,
                ),
            ),
            sample_size=report.total_games,
            confidence_interval=OfflineConfidenceInterval(
                lower_bound=report.lower_bound,
                upper_bound=report.upper_bound,
                confidence_level=report.confidence_level,
                method=bootstrap.method,
            ),
            reproducibility=OfflineReproducibilityMetadata(
                code_commit="synthetic-local-smoke",
                fixture_id=FIXTURE_ID,
                seed=SEED,
                environment="local-unit-test",
            ),
            safety=OfflineEvaluationSafetyFlags(),
            warnings=(
                "synthetic only",
                "not strength evidence",
                "not Tenhou result",
            ),
            evidence_refs=(
                "tests/eval/test_offline_envelope_smoke.py",
                FIXTURE_ID,
            ),
        )

        self.assertEqual(envelope.evaluation_stage, "P5")
        self.assertEqual(envelope.evaluation_type, "stable_dan_report_smoke")
        self.assertEqual(envelope.sample_size, 100)
        self.assertEqual(envelope.room, "phoenix")
        self.assertIsNone(envelope.command_status)
        self.assertEqual(envelope.safety.high_risk_flag_names(), ())

        metric_values = {metric.metric_name: metric.value for metric in envelope.metrics}
        self.assertEqual(
            set(metric_values),
            {
                "stable_dan_point_estimate",
                "stable_dan_ci_lower",
                "stable_dan_ci_upper",
                "stable_dan_threshold_outcome",
                "stable_dan_sample_size_status",
            },
        )
        self.assertAlmostEqual(metric_values["stable_dan_point_estimate"], 11.5)
        self.assertLessEqual(
            metric_values["stable_dan_ci_lower"],
            metric_values["stable_dan_ci_upper"],
        )
        self.assertIn(envelope.warnings[0], ("synthetic only",))
        self.assertIn("not strength evidence", envelope.warnings)
        self.assertIn("not Tenhou result", envelope.warnings)

        envelope_dict = envelope.to_dict()
        json.dumps(envelope_dict, sort_keys=True)
        self.assertEqual(envelope_dict["dataset_or_fixture_id"], FIXTURE_ID)
        self.assertFalse(any(envelope_dict["safety"].values()))
        self.assertIn("tests/eval/test_offline_envelope_smoke.py", envelope_dict["evidence_refs"])
        self.assertIn(FIXTURE_ID, envelope_dict["evidence_refs"])

    def load_fixture_records(self) -> list[dict[str, object]]:
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            records = json.load(fixture_file)
        self.assertIsInstance(records, list)
        self.assertEqual(len(records), 100)
        self.assertTrue(
            all(record["game_id"].startswith("synthetic-smoke-") for record in records)
        )
        return records


if __name__ == "__main__":
    unittest.main()
