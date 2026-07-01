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

from mjlabai.supervised.feature_label_schema import (
    FEATURE_LABEL_SMOKE_SCHEMA_VERSION,
    SYNTHETIC_LOCAL_SOURCE_TYPE,
)
from mjlabai.supervised.synthetic_parser_reader_smoke import (
    FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS,
)
from mjlabai.supervised.synthetic_parser_reader_smoke_extension import (
    SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_RECORD_TYPE,
    SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_VERSION,
    SyntheticParserReaderSmokeExtensionError,
    build_synthetic_parser_reader_smoke_extension_manifest,
    collect_synthetic_parser_reader_smoke_extension_errors,
)


def _synthetic_record(
    fixture_id: str = "synthetic-parser-reader-extension-unit-v0.1",
    feature_families: list[str] | None = None,
    label_families: list[str] | None = None,
) -> dict[str, object]:
    return {
        "fixture_id": fixture_id,
        "schema_version": FEATURE_LABEL_SMOKE_SCHEMA_VERSION,
        "provenance": {
            "source_type": SYNTHETIC_LOCAL_SOURCE_TYPE,
            "project_authored": True,
            "synthetic": True,
            "local_only": True,
            "real_data": False,
            "training_use_approved": False,
            "source_approval": "not_approved",
            "model_output": False,
            "self_play": False,
            "league_output": False,
            "human_label_real_play": False,
            "generated_label_from_unapproved_pipeline": False,
        },
        "feature_families": feature_families
        or [
            "round_context",
            "seat_turn_context",
            "visible_hand_tile_counts",
            "synthetic_provenance_indicators",
        ],
        "label_families": label_families
        or [
            "action_imitation_label",
            "discard_choice_label",
            "synthetic_smoke_label",
        ],
        "public_information_fields": {
            "public_information_only": True,
            "decision_time_only": True,
            "round_context": {"round_wind": "E", "honba": 0},
            "seat_turn_context": {"actor": 0, "dealer": 0, "turn_index": 0},
            "visible_hand_tile_counts": {
                "actor": 0,
                "tile_count_stub": {"1m": 1},
            },
        },
        "forbidden_information_absent": {
            "hidden_information_absent": True,
            "future_information_absent": True,
        },
        "evidence_warnings": [
            "project-authored synthetic/local only",
            "not Tenhou data",
            "not real haifu",
            "not external log",
            "not platform data",
            "not model output",
            "not training data",
            "not model strength evidence",
            "not LuckyJ 10.68 comparison",
            "not candidate promotion evidence",
        ],
        "non_evidence": {
            "model_strength": False,
            "tenhou_ranked": False,
            "stable_dan_ranked_game": False,
            "luckyj_10_68_comparison": False,
            "candidate_promotion": False,
            "training_data_approval": False,
            "source_approval": False,
        },
    }


class SyntheticParserReaderSmokeExtensionTest(unittest.TestCase):
    def test_valid_in_memory_records_return_json_safe_manifest(self) -> None:
        records = [_synthetic_record()]

        manifest = build_synthetic_parser_reader_smoke_extension_manifest(records)

        self.assertEqual(
            manifest["record_type"],
            SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_RECORD_TYPE,
        )
        self.assertEqual(
            manifest["extension_version"],
            SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_VERSION,
        )
        self.assertEqual(manifest["record_count"], 1)
        self.assertEqual(manifest["input_kind"], "in_memory_sequence")
        self.assertEqual(manifest["output_kind"], "json_safe_manifest_summary")
        self.assertTrue(manifest["all_project_authored"])
        self.assertTrue(manifest["all_synthetic"])
        self.assertTrue(manifest["all_local_only"])
        self.assertFalse(manifest["any_real_data"])
        self.assertFalse(manifest["any_model_output"])
        self.assertFalse(manifest["any_training_use_approved"])
        self.assertFalse(manifest["any_self_play"])
        self.assertFalse(manifest["any_league_output"])
        self.assertTrue(manifest["all_public_information_only"])
        self.assertTrue(manifest["all_decision_time_only"])
        self.assertTrue(manifest["all_hidden_information_absent"])
        self.assertTrue(manifest["all_future_information_absent"])
        self.assertEqual(manifest["total_feature_family_count"], 4)
        self.assertEqual(manifest["total_label_family_count"], 3)
        self.assertEqual(manifest["total_evidence_warning_count"], 10)
        self.assertTrue(manifest["non_evidence_guardrails_all_false"])
        self.assertEqual(
            manifest["input_fixture_ids"],
            ["synthetic-parser-reader-extension-unit-v0.1"],
        )
        self.assertEqual(
            manifest["input_schema_versions"],
            [FEATURE_LABEL_SMOKE_SCHEMA_VERSION],
        )
        json.dumps(manifest, sort_keys=True)

    def test_multiple_records_aggregate_manifest_counts(self) -> None:
        records = [
            _synthetic_record(
                fixture_id="synthetic-parser-reader-extension-unit-0001",
                feature_families=["round_context", "seat_turn_context"],
                label_families=["synthetic_smoke_label"],
            ),
            _synthetic_record(
                fixture_id="synthetic-parser-reader-extension-unit-0002",
                feature_families=[
                    "round_context",
                    "visible_hand_tile_counts",
                    "synthetic_provenance_indicators",
                ],
                label_families=[
                    "action_imitation_label",
                    "discard_choice_label",
                ],
            ),
        ]

        manifest = build_synthetic_parser_reader_smoke_extension_manifest(records)

        self.assertEqual(manifest["record_count"], 2)
        self.assertEqual(manifest["total_feature_family_count"], 5)
        self.assertEqual(manifest["total_label_family_count"], 3)
        self.assertEqual(manifest["total_evidence_warning_count"], 20)
        self.assertEqual(
            manifest["input_fixture_ids"],
            [
                "synthetic-parser-reader-extension-unit-0001",
                "synthetic-parser-reader-extension-unit-0002",
            ],
        )

    def test_empty_sequence_is_rejected(self) -> None:
        errors = collect_synthetic_parser_reader_smoke_extension_errors([])

        self.assertEqual(errors, ["records must be a non-empty sequence"])
        with self.assertRaisesRegex(
            SyntheticParserReaderSmokeExtensionError,
            "non-empty sequence",
        ):
            build_synthetic_parser_reader_smoke_extension_manifest([])

    def test_top_level_path_like_and_string_inputs_are_rejected(self) -> None:
        for value in ("tests/fixtures/supervised/synthetic_supervised_smoke.json", Path(".")):
            with self.subTest(value=type(value).__name__):
                with self.assertRaisesRegex(
                    SyntheticParserReaderSmokeExtensionError,
                    "in-memory sequence",
                ):
                    build_synthetic_parser_reader_smoke_extension_manifest(value)  # type: ignore[arg-type]

    def test_record_path_like_entries_are_rejected(self) -> None:
        for value in ("synthetic_supervised_smoke.json", Path(".")):
            with self.subTest(value=type(value).__name__):
                with self.assertRaisesRegex(
                    SyntheticParserReaderSmokeExtensionError,
                    "in-memory mapping",
                ):
                    build_synthetic_parser_reader_smoke_extension_manifest([value])  # type: ignore[list-item]

    def test_real_data_record_is_rejected(self) -> None:
        record = _synthetic_record()
        record["provenance"]["real_data"] = True  # type: ignore[index]

        with self.assertRaisesRegex(
            SyntheticParserReaderSmokeExtensionError,
            r"records\[0\].*real_data",
        ):
            build_synthetic_parser_reader_smoke_extension_manifest([record])

    def test_model_output_record_is_rejected(self) -> None:
        record = _synthetic_record()
        record["provenance"]["model_output"] = True  # type: ignore[index]

        with self.assertRaisesRegex(
            SyntheticParserReaderSmokeExtensionError,
            r"records\[0\].*model_output",
        ):
            build_synthetic_parser_reader_smoke_extension_manifest([record])

    def test_source_approval_claim_is_rejected(self) -> None:
        record = _synthetic_record()
        record["provenance"]["source_approval"] = "approved"  # type: ignore[index]

        with self.assertRaisesRegex(
            SyntheticParserReaderSmokeExtensionError,
            r"records\[0\].*source_approval",
        ):
            build_synthetic_parser_reader_smoke_extension_manifest([record])

    def test_hidden_or_future_information_is_rejected(self) -> None:
        cases = {
            "hidden_information": {
                "opponent_private_hand": ["1m"],
            },
            "future_information": {
                "future_draw": "9s",
            },
        }
        for key, payload in cases.items():
            with self.subTest(key=key):
                record = _synthetic_record()
                record["public_information_fields"][key] = payload  # type: ignore[index]

                with self.assertRaisesRegex(
                    SyntheticParserReaderSmokeExtensionError,
                    rf"records\[0\].*{key}",
                ):
                    build_synthetic_parser_reader_smoke_extension_manifest([record])

    def test_manifest_output_does_not_contain_forbidden_keys(self) -> None:
        manifest = build_synthetic_parser_reader_smoke_extension_manifest(
            [_synthetic_record()]
        )

        found_keys: set[str] = set()
        self._collect_keys(manifest, found_keys)

        self.assertTrue(FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS.isdisjoint(found_keys))

    def test_non_evidence_guardrails_remain_false(self) -> None:
        record = _synthetic_record()
        non_evidence = record["non_evidence"]

        self.assertIsInstance(non_evidence, dict)
        self.assertTrue(all(value is False for value in non_evidence.values()))
        manifest = build_synthetic_parser_reader_smoke_extension_manifest([record])
        self.assertTrue(manifest["non_evidence_guardrails_all_false"])

    def test_non_json_safe_record_is_rejected(self) -> None:
        record = copy.deepcopy(_synthetic_record())
        record["public_information_fields"]["bad_set"] = {"1m"}  # type: ignore[index]

        with self.assertRaisesRegex(
            SyntheticParserReaderSmokeExtensionError,
            "JSON-safe",
        ):
            build_synthetic_parser_reader_smoke_extension_manifest([record])

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
