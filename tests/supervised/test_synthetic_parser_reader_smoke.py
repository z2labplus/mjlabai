import copy
import json
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.supervised.synthetic_parser_reader_smoke import (
    FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS,
    SYNTHETIC_PARSER_READER_SMOKE_RECORD_TYPE,
    SYNTHETIC_PARSER_READER_SMOKE_VERSION,
    SyntheticParserReaderSmokeError,
    collect_synthetic_parser_reader_smoke_errors,
    parse_synthetic_parser_reader_smoke_mapping,
)


FIXTURE_PATH = REPO_ROOT / "tests/fixtures/supervised/synthetic_supervised_smoke.json"


def _fixture_mapping() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


class SyntheticParserReaderSmokeTest(unittest.TestCase):
    def test_existing_synthetic_fixture_returns_json_safe_summary(self) -> None:
        mapping = _fixture_mapping()

        summary = parse_synthetic_parser_reader_smoke_mapping(mapping)

        self.assertEqual(
            summary["record_type"],
            SYNTHETIC_PARSER_READER_SMOKE_RECORD_TYPE,
        )
        self.assertEqual(
            summary["parser_reader_smoke_version"],
            SYNTHETIC_PARSER_READER_SMOKE_VERSION,
        )
        self.assertEqual(summary["reader_input_kind"], "in_memory_mapping")
        self.assertEqual(summary["parser_output_kind"], "json_safe_guardrail_summary")
        self.assertEqual(summary["input_fixture_id"], mapping["fixture_id"])
        self.assertTrue(summary["project_authored"])
        self.assertTrue(summary["synthetic"])
        self.assertTrue(summary["local_only"])
        self.assertFalse(summary["uses_real_data"])
        self.assertFalse(summary["training_use_approved"])
        self.assertFalse(summary["has_model_output"])
        self.assertFalse(summary["uses_self_play"])
        self.assertFalse(summary["uses_league_output"])
        self.assertTrue(summary["public_information_only"])
        self.assertTrue(summary["decision_time_only"])
        self.assertTrue(summary["hidden_information_absent"])
        self.assertTrue(summary["future_information_absent"])
        self.assertGreater(summary["feature_family_count"], 0)
        self.assertGreater(summary["label_family_count"], 0)
        self.assertGreater(summary["evidence_warning_count"], 0)
        self.assertTrue(summary["non_evidence_guardrails_all_false"])
        json.dumps(summary, sort_keys=True)

    def test_collect_errors_for_valid_mapping_is_empty(self) -> None:
        self.assertEqual(collect_synthetic_parser_reader_smoke_errors(_fixture_mapping()), [])

    def test_real_data_is_rejected(self) -> None:
        mapping = _fixture_mapping()
        mapping["provenance"]["real_data"] = True  # type: ignore[index]

        with self.assertRaisesRegex(SyntheticParserReaderSmokeError, "real_data"):
            parse_synthetic_parser_reader_smoke_mapping(mapping)

    def test_model_output_is_rejected(self) -> None:
        mapping = _fixture_mapping()
        mapping["provenance"]["model_output"] = True  # type: ignore[index]

        with self.assertRaisesRegex(SyntheticParserReaderSmokeError, "model_output"):
            parse_synthetic_parser_reader_smoke_mapping(mapping)

    def test_source_approval_claim_is_rejected(self) -> None:
        mapping = _fixture_mapping()
        mapping["provenance"]["source_approval"] = "approved"  # type: ignore[index]

        with self.assertRaisesRegex(SyntheticParserReaderSmokeError, "source_approval"):
            parse_synthetic_parser_reader_smoke_mapping(mapping)

    def test_hidden_information_is_rejected(self) -> None:
        mapping = _fixture_mapping()
        mapping["public_information_fields"]["hidden_information"] = {  # type: ignore[index]
            "opponent_private_hand": ["1m"]
        }

        with self.assertRaisesRegex(SyntheticParserReaderSmokeError, "hidden_information"):
            parse_synthetic_parser_reader_smoke_mapping(mapping)

    def test_future_information_is_rejected(self) -> None:
        mapping = _fixture_mapping()
        mapping["public_information_fields"]["future_information"] = {  # type: ignore[index]
            "future_draw": "9s"
        }

        with self.assertRaisesRegex(SyntheticParserReaderSmokeError, "future_information"):
            parse_synthetic_parser_reader_smoke_mapping(mapping)

    def test_path_like_and_string_inputs_are_rejected(self) -> None:
        for value in (str(FIXTURE_PATH), FIXTURE_PATH):
            with self.subTest(value=type(value).__name__):
                with self.assertRaisesRegex(
                    SyntheticParserReaderSmokeError,
                    "in-memory mapping",
                ):
                    parse_synthetic_parser_reader_smoke_mapping(value)  # type: ignore[arg-type]

    def test_output_does_not_contain_forbidden_dataset_or_model_keys(self) -> None:
        summary = parse_synthetic_parser_reader_smoke_mapping(_fixture_mapping())

        found_keys = set()
        self._collect_keys(summary, found_keys)

        self.assertTrue(FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS.isdisjoint(found_keys))

    def test_non_evidence_flags_remain_false(self) -> None:
        mapping = _fixture_mapping()
        non_evidence = mapping["non_evidence"]

        self.assertIsInstance(non_evidence, dict)
        self.assertTrue(non_evidence)
        self.assertTrue(all(value is False for value in non_evidence.values()))
        summary = parse_synthetic_parser_reader_smoke_mapping(mapping)
        self.assertTrue(summary["non_evidence_guardrails_all_false"])

    def test_non_json_safe_mapping_is_rejected(self) -> None:
        mapping = copy.deepcopy(_fixture_mapping())
        mapping["public_information_fields"]["bad_set"] = {"1m"}  # type: ignore[index]

        with self.assertRaisesRegex(SyntheticParserReaderSmokeError, "JSON-safe"):
            parse_synthetic_parser_reader_smoke_mapping(mapping)

    def _collect_keys(self, value: object, found_keys: set[str]) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                found_keys.add(str(key))
                self._collect_keys(child, found_keys)
        elif isinstance(value, list):
            for child in value:
                self._collect_keys(child, found_keys)


if __name__ == "__main__":
    unittest.main()
