import copy
import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.data.replay_schema import (
    PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY,
    REPLAY_SCHEMA_VERSION,
    assert_valid_replay_fixture,
    is_project_authored_synthetic_fixture,
    validate_replay_fixture,
    validate_replay_record,
)


def _minimal_record() -> dict[str, object]:
    return {
        "schema_version": REPLAY_SCHEMA_VERSION,
        "replay_id": "synthetic-replay-unit-0001",
        "source_id": "project_authored_synthetic_unit",
        "source_record_id": "synthetic-source-record-unit-0001",
        "transform_version": "synthetic_transform_v0.1",
        "game_context": {
            "ruleset": "synthetic_riichi_four_player",
            "room_context": "synthetic_local",
        },
        "participants": [
            {"seat": 0, "synthetic_player_id": "synthetic-seat-0"},
            {"seat": 1, "synthetic_player_id": "synthetic-seat-1"},
            {"seat": 2, "synthetic_player_id": "synthetic-seat-2"},
            {"seat": 3, "synthetic_player_id": "synthetic-seat-3"},
        ],
        "event_sequence": [
            {
                "event_index": 0,
                "event_type": "synthetic_start",
                "event_payload_boundary": "synthetic marker only",
            }
        ],
        "decision_state_boundary": {
            "observation_scope": "synthetic visible-state stub only",
            "hidden_information_policy": "hidden information is not represented",
            "feature_extraction_status": "not implemented",
            "future_target_status": "not implemented",
        },
        "terminal_result": {
            "result_note": "Synthetic terminal result only; not strength evidence."
        },
        "validation_metadata": {
            "validation_status": "synthetic_schema_smoke_expected_valid"
        },
    }


def _minimal_fixture() -> dict[str, object]:
    return {
        "schema_version": REPLAY_SCHEMA_VERSION,
        "fixture_id": "synthetic_replay_unit_v0.1",
        "source_id": "project_authored_synthetic_unit",
        "source_category": PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY,
        "source_note": (
            "Project-authored synthetic/local replay smoke fixture only; "
            "not Tenhou data; not real haifu; not external log; not platform "
            "data; not model output; not training data; not model strength "
            "evidence; not LuckyJ 10.68 comparison."
        ),
        "warnings": [
            "synthetic/local only",
            "not Tenhou data",
            "not real haifu",
            "not external log",
            "not platform data",
            "not model output",
            "not training data",
            "not model strength evidence",
            "not LuckyJ 10.68 comparison",
        ],
        "source_provenance": {
            "source_id": "project_authored_synthetic_unit",
            "project_authored": True,
            "synthetic_local": True,
            "rights_status": "project_authored",
            "allowed_use": "P6 replay schema smoke validation only",
            "may_enter_git": "yes_small_project_authored_only",
            "uses_real_tenhou": False,
            "uses_real_haifu": False,
            "uses_external_log": False,
            "uses_platform_data": False,
            "uses_model_output": False,
            "training_use": False,
            "strength_evidence": False,
            "luckyj_comparison": False,
        },
        "records": [_minimal_record()],
        "evidence_refs": ["docs/09_governance/09_EVIDENCE_LOG.md"],
        "risk_refs": ["docs/09_governance/09_RISK_REGISTER.md"],
    }


class ReplaySchemaTest(unittest.TestCase):
    def test_valid_fixture_has_no_errors_and_is_json_safe(self) -> None:
        fixture = _minimal_fixture()

        self.assertEqual(validate_replay_fixture(fixture), [])
        assert_valid_replay_fixture(fixture)
        json.dumps(fixture, sort_keys=True)

    def test_valid_record_has_no_errors(self) -> None:
        self.assertEqual(validate_replay_record(_minimal_record()), [])

    def test_project_authored_synthetic_guard(self) -> None:
        fixture = _minimal_fixture()
        self.assertTrue(is_project_authored_synthetic_fixture(fixture))

        fixture["source_provenance"]["uses_real_tenhou"] = True  # type: ignore[index]
        self.assertFalse(is_project_authored_synthetic_fixture(fixture))
        self.assertIn(
            "source_provenance.uses_real_tenhou must be false",
            validate_replay_fixture(fixture),
        )

    def test_missing_required_field_raises(self) -> None:
        fixture = _minimal_fixture()
        del fixture["records"]

        with self.assertRaisesRegex(ValueError, "missing required keys"):
            assert_valid_replay_fixture(fixture)

    def test_rejects_private_or_model_output_keys(self) -> None:
        fixture = _minimal_fixture()
        record = fixture["records"][0]  # type: ignore[index]
        record["participants"][0]["account_id"] = "real-account"  # type: ignore[index]
        record["model_output"] = {"action": "synthetic"}  # type: ignore[index]

        errors = validate_replay_fixture(fixture)
        self.assertTrue(any("account_id is forbidden" in error for error in errors))
        self.assertTrue(any("model_output is forbidden" in error for error in errors))

    def test_rejects_non_json_safe_record(self) -> None:
        record = _minimal_record()
        record["event_sequence"] = [{"bad": {"set-is-not-json-safe"}}]

        errors = validate_replay_record(record)
        self.assertTrue(any("JSON-safe" in error for error in errors))

    def test_fixture_source_id_must_match_record_source_id(self) -> None:
        fixture = copy.deepcopy(_minimal_fixture())
        fixture["records"][0]["source_id"] = "other-source"  # type: ignore[index]

        errors = validate_replay_fixture(fixture)
        self.assertIn("records[0].source_id must match fixture source_id", errors)


if __name__ == "__main__":
    unittest.main()
