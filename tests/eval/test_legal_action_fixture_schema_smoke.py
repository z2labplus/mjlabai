import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = REPO_ROOT / "tests/fixtures/eval/legal_action_metric_smoke.json"
EXPECTED_OUTCOMES = {
    "legal",
    "invalid",
    "missing_action",
    "parse_failure",
    "skipped_no_legal_actions",
}


class LegalActionFixtureSchemaSmokeTest(unittest.TestCase):
    """Schema smoke test only.

    `expected_future_outcome` values are fixture labels for future evaluator
    tasks. This test does not calculate legal_action_rate, invalid_action_rate,
    or canonical equality, and it reads no Tenhou, external log, or platform
    data.
    """

    def test_synthetic_legal_action_fixture_shape(self) -> None:
        self.assertTrue(FIXTURE_PATH.exists())

        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.assertIsInstance(fixture, dict)
        self.assertTrue(fixture.get("fixture_id"))
        self.assertEqual(fixture.get("schema_version"), "legal_action_fixture_v0.1")
        self._assert_synthetic_source_note(fixture.get("source_note"))

        records = fixture.get("records")
        self.assertIsInstance(records, list)
        self.assertGreater(len(records), 0)

        outcomes = set()
        for record in records:
            self._assert_record_shape(record)
            outcomes.add(record["expected_future_outcome"])

        self.assertTrue(EXPECTED_OUTCOMES.issubset(outcomes))

    def _assert_record_shape(self, record: object) -> None:
        self.assertIsInstance(record, dict)
        required_keys = {
            "decision_id",
            "actor",
            "ruleset",
            "room",
            "matching_mode",
            "expected_future_outcome",
            "proposed_action",
            "legal_actions",
            "source_note",
        }
        self.assertTrue(required_keys.issubset(record.keys()))
        self.assertTrue(record["decision_id"])
        self.assertEqual(type(record["actor"]), int)
        self.assertIn(record["actor"], {0, 1, 2, 3})
        self.assertEqual(record["matching_mode"], "strict")
        self.assertIn(record["expected_future_outcome"], EXPECTED_OUTCOMES)
        self._assert_synthetic_source_note(record["source_note"])

        proposed_action = record["proposed_action"]
        if proposed_action is not None:
            self._assert_canonical_dahai_action(proposed_action)

        legal_actions = record["legal_actions"]
        self.assertIsInstance(legal_actions, list)
        for action in legal_actions:
            self._assert_canonical_dahai_action(action)

        if record["expected_future_outcome"] == "missing_action":
            self.assertIsNone(proposed_action)
            self.assertGreater(len(legal_actions), 0)
        if record["expected_future_outcome"] == "parse_failure":
            self.assertIsNotNone(proposed_action)
            self.assertGreater(len(legal_actions), 0)
            self.assertEqual(proposed_action["schema_version"], "canonical_action_v0.1")
            self.assertEqual(proposed_action["action_type"], "dahai")
            self.assertIsNone(proposed_action["tsumogiri"])
        if record["expected_future_outcome"] == "skipped_no_legal_actions":
            self.assertEqual(legal_actions, [])

    def _assert_canonical_dahai_action(self, action: object) -> None:
        self.assertIsInstance(action, dict)
        self.assertEqual(action.get("schema_version"), "canonical_action_v0.1")
        self.assertEqual(type(action.get("actor")), int)
        self.assertIn(action.get("actor"), {0, 1, 2, 3})
        self.assertEqual(action.get("action_type"), "dahai")
        self.assertIsInstance(action.get("tile"), str)
        self.assertTrue(action["tile"])
        self.assertIn(action.get("tsumogiri"), {True, False, None})

        raw_action = action.get("raw_action")
        self.assertIsInstance(raw_action, dict)
        self.assertEqual(raw_action.get("type"), "dahai")
        self.assertEqual(raw_action.get("actor"), action.get("actor"))
        self.assertIsInstance(raw_action.get("pai"), str)
        self.assertIn(raw_action.get("tsumogiri"), {True, False, None})

    def _assert_synthetic_source_note(self, source_note: object) -> None:
        self.assertIsInstance(source_note, str)
        note = source_note.lower()
        self.assertIn("synthetic", note)
        self.assertIn("not tenhou", note)
        self.assertIn("not model strength", note)


if __name__ == "__main__":
    unittest.main()
