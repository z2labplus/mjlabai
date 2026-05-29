from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval import (  # noqa: E402
    LegalActionMetricResult,
    build_synthetic_legal_action_metric_envelope,
    evaluate_synthetic_legal_action_fixture,
)


FIXTURE_ID = "tests/fixtures/eval/legal_action_metric_smoke.json"
FIXTURE_PATH = REPO_ROOT / FIXTURE_ID
REQUIRED_WARNING_WORDS = (
    "synthetic",
    "not Tenhou",
    "not real haifu",
    "not model strength",
    "not LuckyJ",
)


class LegalActionMetricTests(unittest.TestCase):
    def test_project_fixture_counts_rates_and_invariant(self) -> None:
        result = evaluate_synthetic_legal_action_fixture(_load_fixture())

        self.assertIsInstance(result, LegalActionMetricResult)
        self.assertEqual(result.total_record_count, 5)
        self.assertEqual(result.legal_action_count, 1)
        self.assertEqual(result.invalid_action_count, 1)
        self.assertEqual(result.missing_action_count, 1)
        self.assertEqual(result.parse_failure_count, 1)
        self.assertEqual(result.skipped_count, 1)
        self.assertEqual(result.evaluated_decision_count, 4)
        self.assertTrue(result.invariant_holds)
        self.assertAlmostEqual(result.legal_action_rate, 1 / 4)
        self.assertAlmostEqual(result.invalid_action_rate, 1 / 4)
        self.assertAlmostEqual(result.missing_action_rate, 1 / 4)
        self.assertAlmostEqual(result.parse_failure_rate, 1 / 4)

    def test_skipped_no_legal_actions_is_not_in_denominator(self) -> None:
        fixture = _minimal_fixture(
            [
                {
                    "decision_id": "skip-only",
                    "actor": 0,
                    "ruleset": "tenhou_four_player",
                    "room": "phoenix",
                    "matching_mode": "strict",
                    "proposed_action": _dahai(actor=0, tile="1s", tsumogiri=True),
                    "legal_actions": [],
                }
            ]
        )

        result = evaluate_synthetic_legal_action_fixture(fixture)

        self.assertEqual(result.total_record_count, 1)
        self.assertEqual(result.skipped_count, 1)
        self.assertEqual(result.evaluated_decision_count, 0)
        self.assertIsNone(result.legal_action_rate)
        self.assertIsNone(result.invalid_action_rate)
        self.assertIsNone(result.missing_action_rate)
        self.assertIsNone(result.parse_failure_rate)

    def test_parse_failure_is_counted_separately(self) -> None:
        fixture = _minimal_fixture(
            [
                {
                    "decision_id": "parse-failure",
                    "actor": 0,
                    "ruleset": "tenhou_four_player",
                    "room": "phoenix",
                    "matching_mode": "strict",
                    "proposed_action": {
                        "schema_version": "canonical_action_v0.1",
                        "actor": 0,
                        "action_type": "reach",
                        "tile": "1s",
                        "tsumogiri": True,
                    },
                    "legal_actions": [_dahai(actor=0, tile="1s", tsumogiri=True)],
                }
            ]
        )

        result = evaluate_synthetic_legal_action_fixture(fixture)

        self.assertEqual(result.parse_failure_count, 1)
        self.assertEqual(result.evaluated_decision_count, 1)
        self.assertEqual(result.parse_failure_rate, 1.0)
        self.assertEqual(result.invalid_action_count, 0)

    def test_malformed_legal_action_raises(self) -> None:
        fixture = _minimal_fixture(
            [
                {
                    "decision_id": "bad-legal-action",
                    "actor": 0,
                    "ruleset": "tenhou_four_player",
                    "room": "phoenix",
                    "matching_mode": "strict",
                    "proposed_action": _dahai(actor=0, tile="1s", tsumogiri=True),
                    "legal_actions": [
                        {
                            "schema_version": "canonical_action_v0.1",
                            "actor": 0,
                            "action_type": "reach",
                            "tile": "1s",
                            "tsumogiri": True,
                        }
                    ],
                }
            ]
        )

        with self.assertRaises(ValueError):
            evaluate_synthetic_legal_action_fixture(fixture)

    def test_expected_future_outcome_is_not_used_for_computation(self) -> None:
        fixture = _load_fixture()
        expected_result = evaluate_synthetic_legal_action_fixture(fixture)

        tampered_fixture = copy.deepcopy(fixture)
        for record in tampered_fixture["records"]:
            record["expected_future_outcome"] = "legal"
        actual_result = evaluate_synthetic_legal_action_fixture(tampered_fixture)

        self.assertEqual(expected_result.to_dict(), actual_result.to_dict())

    def test_envelope_helper_records_synthetic_metric_result(self) -> None:
        result = evaluate_synthetic_legal_action_fixture(_load_fixture())
        envelope = build_synthetic_legal_action_metric_envelope(
            result,
            dataset_or_fixture_id=FIXTURE_ID,
            code_commit="synthetic-local-test",
            environment="unit-test",
        )

        self.assertEqual(envelope.evaluation_stage, "P5")
        self.assertEqual(envelope.evaluation_type, "legal_action_metric")
        self.assertEqual(
            envelope.model_or_tool_id,
            "synthetic-legal-action-fixture-evaluator",
        )
        self.assertEqual(envelope.dataset_or_fixture_id, FIXTURE_ID)
        self.assertEqual(envelope.sample_size, 4)
        self.assertEqual(envelope.safety.high_risk_flag_names(), ())

        metric_values = {metric.metric_name: metric.value for metric in envelope.metrics}
        self.assertEqual(metric_values["legal_action_count"], 1)
        self.assertEqual(metric_values["invalid_action_count"], 1)
        self.assertEqual(metric_values["missing_action_count"], 1)
        self.assertEqual(metric_values["parse_failure_count"], 1)
        self.assertEqual(metric_values["skipped_count"], 1)
        self.assertAlmostEqual(metric_values["legal_action_rate"], 1 / 4)
        self.assertAlmostEqual(metric_values["invalid_action_rate"], 1 / 4)
        self.assertAlmostEqual(metric_values["missing_action_rate"], 1 / 4)
        self.assertAlmostEqual(metric_values["parse_failure_rate"], 1 / 4)

        warning_text = " ".join(envelope.warnings)
        for expected_word in REQUIRED_WARNING_WORDS:
            self.assertIn(expected_word, warning_text)
        self.assertIn("tests/eval/test_legal_action_metric.py", envelope.evidence_refs)
        self.assertIn(FIXTURE_ID, envelope.evidence_refs)
        json.dumps(envelope.to_dict(), sort_keys=True)


def _load_fixture() -> dict[str, object]:
    with FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
        fixture = json.load(fixture_file)
    return fixture


def _minimal_fixture(records: list[dict[str, object]]) -> dict[str, object]:
    return {
        "fixture_id": "synthetic-legal-action-inline-test",
        "schema_version": "legal_action_fixture_v0.1",
        "source_note": (
            "Synthetic fixture only; not Tenhou data; not a real haifu; "
            "not model strength evidence."
        ),
        "records": records,
    }


def _dahai(*, actor: int, tile: str, tsumogiri: bool) -> dict[str, object]:
    return {
        "schema_version": "canonical_action_v0.1",
        "actor": actor,
        "action_type": "dahai",
        "tile": tile,
        "tsumogiri": tsumogiri,
        "raw_action": {
            "type": "dahai",
            "actor": actor,
            "pai": tile,
            "tsumogiri": tsumogiri,
        },
    }


if __name__ == "__main__":
    unittest.main()
