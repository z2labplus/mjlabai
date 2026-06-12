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
    ALLOWED_FEATURE_FAMILIES,
    ALLOWED_LABEL_FAMILIES,
    FEATURE_LABEL_SMOKE_SCHEMA_VERSION,
    SYNTHETIC_LOCAL_SOURCE_TYPE,
    FeatureLabelSchemaError,
    is_json_safe_mapping,
    validate_feature_label_smoke_mapping,
)


def _valid_mapping() -> dict[str, object]:
    return {
        "fixture_id": "synthetic-supervised-unit-v0.1",
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
        "feature_families": [
            "round_context",
            "seat_turn_context",
            "visible_hand_tile_counts",
            "synthetic_provenance_indicators",
        ],
        "label_families": [
            "action_imitation_label",
            "discard_choice_label",
            "synthetic_smoke_label",
        ],
        "public_information_fields": {
            "public_information_only": True,
            "decision_time_only": True,
            "round_context": {"round_wind": "E", "honba": 0},
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


class FeatureLabelSchemaTest(unittest.TestCase):
    def test_valid_synthetic_mapping_passes_and_is_json_safe(self) -> None:
        mapping = _valid_mapping()

        normalized = validate_feature_label_smoke_mapping(mapping)

        self.assertEqual(normalized["fixture_id"], mapping["fixture_id"])
        self.assertTrue(is_json_safe_mapping(mapping))
        json.dumps(normalized, sort_keys=True)

    def test_candidate_feature_families_are_recognized(self) -> None:
        mapping = _valid_mapping()
        mapping["feature_families"] = sorted(ALLOWED_FEATURE_FAMILIES)

        normalized = validate_feature_label_smoke_mapping(mapping)

        self.assertEqual(
            set(normalized["feature_families"]),
            set(ALLOWED_FEATURE_FAMILIES),
        )

    def test_candidate_label_families_are_recognized(self) -> None:
        mapping = _valid_mapping()
        mapping["label_families"] = sorted(ALLOWED_LABEL_FAMILIES)

        normalized = validate_feature_label_smoke_mapping(mapping)

        self.assertEqual(set(normalized["label_families"]), set(ALLOWED_LABEL_FAMILIES))

    def test_hidden_information_field_is_rejected(self) -> None:
        mapping = _valid_mapping()
        mapping["public_information_fields"]["hidden_information"] = {  # type: ignore[index]
            "opponent_hand": ["1m"]
        }

        with self.assertRaisesRegex(FeatureLabelSchemaError, "hidden_information"):
            validate_feature_label_smoke_mapping(mapping)

    def test_future_information_field_is_rejected(self) -> None:
        mapping = _valid_mapping()
        mapping["public_information_fields"]["future_information"] = {  # type: ignore[index]
            "future_draw": "9s"
        }

        with self.assertRaisesRegex(FeatureLabelSchemaError, "future_information"):
            validate_feature_label_smoke_mapping(mapping)

    def test_training_use_approval_claim_is_rejected(self) -> None:
        mapping = _valid_mapping()
        mapping["provenance"]["training_use_approved"] = True  # type: ignore[index]

        with self.assertRaisesRegex(FeatureLabelSchemaError, "training_use_approved"):
            validate_feature_label_smoke_mapping(mapping)

    def test_source_approval_claim_is_rejected(self) -> None:
        mapping = _valid_mapping()
        mapping["provenance"]["source_approval"] = "approved"  # type: ignore[index]

        with self.assertRaisesRegex(FeatureLabelSchemaError, "source_approval"):
            validate_feature_label_smoke_mapping(mapping)

    def test_real_data_provenance_is_rejected(self) -> None:
        mapping = _valid_mapping()
        mapping["provenance"]["real_data"] = True  # type: ignore[index]

        with self.assertRaisesRegex(FeatureLabelSchemaError, "real_data"):
            validate_feature_label_smoke_mapping(mapping)

    def test_model_output_provenance_is_rejected(self) -> None:
        mapping = _valid_mapping()
        mapping["provenance"]["model_output"] = True  # type: ignore[index]

        with self.assertRaisesRegex(FeatureLabelSchemaError, "model_output"):
            validate_feature_label_smoke_mapping(mapping)

    def test_self_play_and_league_provenance_are_rejected(self) -> None:
        for key in ("self_play", "league_output"):
            with self.subTest(key=key):
                mapping = _valid_mapping()
                mapping["provenance"][key] = True  # type: ignore[index]

                with self.assertRaisesRegex(FeatureLabelSchemaError, key):
                    validate_feature_label_smoke_mapping(mapping)

    def test_non_json_safe_value_is_rejected(self) -> None:
        mapping = copy.deepcopy(_valid_mapping())
        mapping["public_information_fields"]["bad_set"] = {"1m"}  # type: ignore[index]

        with self.assertRaisesRegex(FeatureLabelSchemaError, "JSON-safe"):
            validate_feature_label_smoke_mapping(mapping)


if __name__ == "__main__":
    unittest.main()
