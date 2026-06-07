import json
import unittest
from pathlib import Path
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.data.replay_schema import (
    PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY,
    REPLAY_SCHEMA_VERSION,
    assert_valid_replay_fixture,
    is_project_authored_synthetic_fixture,
)


FIXTURE_PATH = REPO_ROOT / "tests/fixtures/data/synthetic_replay_smoke.json"

REQUIRED_TOP_LEVEL_KEYS = {
    "schema_version",
    "fixture_id",
    "source_id",
    "source_category",
    "source_note",
    "warnings",
    "source_provenance",
    "records",
    "evidence_refs",
    "risk_refs",
}
REQUIRED_NOTE_TERMS = (
    "synthetic",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not platform data",
    "not model output",
    "not training",
    "not model strength",
    "not luckyj",
)
REQUIRED_FALSE_PROVENANCE_FLAGS = {
    "uses_real_tenhou",
    "uses_real_haifu",
    "uses_external_log",
    "uses_platform_data",
    "uses_model_output",
    "training_use",
    "strength_evidence",
    "luckyj_comparison",
}
FORBIDDEN_KEYS = {
    "account_id",
    "session_id",
    "cookie",
    "token",
    "private_log",
    "model_output",
    "training_label",
    "supervised_label",
    "label",
    "labels",
}


class SyntheticReplayFixtureSchemaTest(unittest.TestCase):
    def test_project_synthetic_replay_fixture_shape(self) -> None:
        self.assertTrue(FIXTURE_PATH.exists())
        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

        self.assertIsInstance(fixture, dict)
        self.assertTrue(REQUIRED_TOP_LEVEL_KEYS.issubset(fixture.keys()))
        self.assertEqual(fixture["schema_version"], REPLAY_SCHEMA_VERSION)
        self.assertEqual(
            fixture["source_category"],
            PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY,
        )
        self.assertTrue(fixture["fixture_id"])
        self.assertTrue(fixture["source_id"])
        self._assert_note_terms(fixture["source_note"])
        self._assert_warnings(fixture["warnings"])
        self._assert_source_provenance(fixture["source_provenance"])
        self._assert_records(fixture["records"], fixture["source_id"])
        self._assert_refs(fixture["evidence_refs"], "evidence_refs")
        self._assert_refs(fixture["risk_refs"], "risk_refs")
        self._assert_no_forbidden_keys(fixture)
        self.assertTrue(is_project_authored_synthetic_fixture(fixture))
        assert_valid_replay_fixture(fixture)
        json.dumps(fixture, sort_keys=True)

    def _assert_note_terms(self, text: object) -> None:
        self.assertIsInstance(text, str)
        lowered = text.lower()
        for term in REQUIRED_NOTE_TERMS:
            self.assertIn(term, lowered)
        self.assertIn("not candidate promotion", lowered)

    def _assert_warnings(self, warnings: object) -> None:
        self.assertIsInstance(warnings, list)
        warning_text = " ".join(str(warning) for warning in warnings).lower()
        for term in REQUIRED_NOTE_TERMS:
            self.assertIn(term, warning_text)
        self.assertIn("not candidate promotion", warning_text)

    def _assert_source_provenance(self, provenance: object) -> None:
        self.assertIsInstance(provenance, dict)
        self.assertIs(provenance["project_authored"], True)
        self.assertIs(provenance["synthetic_local"], True)
        self.assertEqual(provenance["rights_status"], "project_authored")
        self.assertEqual(
            provenance["may_enter_git"],
            "yes_small_project_authored_only",
        )
        for flag in REQUIRED_FALSE_PROVENANCE_FLAGS:
            self.assertIn(flag, provenance)
            self.assertIs(provenance[flag], False, flag)

    def _assert_records(self, records: object, source_id: object) -> None:
        self.assertIsInstance(records, list)
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertIsInstance(record, dict)
        self.assertEqual(record["schema_version"], REPLAY_SCHEMA_VERSION)
        self.assertEqual(record["source_id"], source_id)
        self.assertTrue(record["replay_id"])
        self.assertTrue(record["source_record_id"])
        self.assertTrue(record["transform_version"])
        self.assertIsInstance(record["game_context"], dict)
        self.assertEqual(record["game_context"]["room_context"], "synthetic_local")
        self.assertIsInstance(record["participants"], list)
        self.assertEqual(len(record["participants"]), 4)
        self.assertIsInstance(record["event_sequence"], list)
        self.assertGreaterEqual(len(record["event_sequence"]), 1)
        self.assertIsInstance(record["decision_state_boundary"], dict)
        self.assertIn("not implemented", record["decision_state_boundary"].values())
        self.assertIsInstance(record["terminal_result"], dict)
        self.assertIn("Synthetic", record["terminal_result"]["result_note"])
        self.assertIsInstance(record["validation_metadata"], dict)

    def _assert_refs(self, refs: object, label: str) -> None:
        self.assertIsInstance(refs, list)
        self.assertGreater(len(refs), 0, label)
        for ref in refs:
            self.assertIsInstance(ref, str)
            self.assertTrue(ref.strip(), label)

    def _assert_no_forbidden_keys(self, value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                self.assertNotIn(str(key).lower(), FORBIDDEN_KEYS)
                self._assert_no_forbidden_keys(child)
        elif isinstance(value, list):
            for child in value:
                self._assert_no_forbidden_keys(child)


if __name__ == "__main__":
    unittest.main()
