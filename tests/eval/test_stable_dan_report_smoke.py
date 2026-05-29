from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval.placement_counts import aggregate_placement_records  # noqa: E402
from mjlabai.eval.stable_dan import (  # noqa: E402
    bootstrap_stable_dan_ci,
    build_stable_dan_evaluation_report,
    calculate_stable_dan,
    compare_stable_dan_to_threshold,
)


FIXTURE_PATH = (
    REPO_ROOT / "tests" / "fixtures" / "eval" / "stable_dan_placements_smoke.json"
)
ROOM = "phoenix"
N_BOOTSTRAP = 300
CONFIDENCE_LEVEL = 0.95
SEED = 12345


class StableDanReportSmokeTest(unittest.TestCase):
    def test_synthetic_placements_build_stable_dan_report(self) -> None:
        # This fixture is project-authored synthetic data only. It is not a
        # Tenhou result, external haifu/log, league result, model result,
        # training result, self-play result or strength claim.
        records = self.load_fixture_records()
        self.assertTrue(
            all(record["game_id"].startswith("synthetic-smoke-") for record in records)
        )

        counts = aggregate_placement_records(records, placement_key="placement")
        self.assertEqual(counts.first_count, 30)
        self.assertEqual(counts.second_count, 30)
        self.assertEqual(counts.third_count, 20)
        self.assertEqual(counts.fourth_count, 20)
        self.assertEqual(counts.total_games, 100)

        point_estimate = calculate_stable_dan(
            **counts.to_stable_dan_kwargs(),
            room=ROOM,
        )
        self.assertAlmostEqual(point_estimate.stable_dan, 11.5)

        bootstrap_result = bootstrap_stable_dan_ci(
            **counts.to_stable_dan_kwargs(),
            room=ROOM,
            n_bootstrap=N_BOOTSTRAP,
            confidence_level=CONFIDENCE_LEVEL,
            seed=SEED,
        )
        self.assertLessEqual(bootstrap_result.lower_bound, bootstrap_result.upper_bound)
        self.assertEqual(
            bootstrap_result.successful_resamples
            + bootstrap_result.undefined_resamples,
            N_BOOTSTRAP,
        )
        self.assertGreaterEqual(bootstrap_result.undefined_rate, 0)
        self.assertLessEqual(bootstrap_result.undefined_rate, 1)

        comparison = compare_stable_dan_to_threshold(bootstrap_result)
        self.assertIsInstance(comparison.outcome, str)
        self.assertTrue(comparison.outcome)

        report = build_stable_dan_evaluation_report(
            bootstrap_result,
            comparison,
            schema_version="stable_dan_report_smoke_v0.1",
        )
        self.assertEqual(report.total_games, 100)
        self.assertEqual(report.first_count, 30)
        self.assertEqual(report.second_count, 30)
        self.assertEqual(report.third_count, 20)
        self.assertEqual(report.fourth_count, 20)
        self.assertAlmostEqual(report.point_estimate, 11.5)
        self.assertTrue(report.can_report_stable_dan)
        self.assertFalse(report.can_enter_threshold_review)
        self.assertEqual(
            report.sample_size_assessment.reporting_status,
            "reportable_estimate",
        )
        self.assertIn("not model strength evidence by itself", report.notes)
        self.assertIn("not a Tenhou ranked result", report.notes)

        report_dict = report.to_dict()
        json.dumps(report_dict, sort_keys=True)
        self.assertEqual(report_dict["schema_version"], "stable_dan_report_smoke_v0.1")
        self.assertEqual(report_dict["total_games"], 100)
        self.assertFalse(report_dict["can_enter_threshold_review"])

    def load_fixture_records(self) -> list[dict[str, object]]:
        with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
            records = json.load(fixture_file)
        self.assertIsInstance(records, list)
        self.assertEqual(len(records), 100)
        return records


if __name__ == "__main__":
    unittest.main()
