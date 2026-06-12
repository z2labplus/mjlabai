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
    validate_feature_label_smoke_mapping,
)


FIXTURE_PATH = REPO_ROOT / "tests/fixtures/supervised/synthetic_supervised_smoke.json"

REQUIRED_TOP_LEVEL_KEYS = {
    "fixture_id",
    "schema_version",
    "provenance",
    "feature_families",
    "label_families",
    "public_information_fields",
    "forbidden_information_absent",
    "evidence_warnings",
    "non_evidence",
}
REQUIRED_WARNING_TERMS = (
    "synthetic",
    "local",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not platform data",
    "not model output",
    "not training",
    "not model strength",
    "not luckyj",
    "not candidate promotion",
)
FALSE_PROVENANCE_FLAGS = (
    "real_data",
    "training_use_approved",
    "model_output",
    "self_play",
    "league_output",
    "human_label_real_play",
    "generated_label_from_unapproved_pipeline",
)
FALSE_NON_EVIDENCE_FLAGS = (
    "model_strength",
    "tenhou_ranked",
    "stable_dan_ranked_game",
    "luckyj_10_68_comparison",
    "candidate_promotion",
    "training_data_approval",
    "source_approval",
)


class SyntheticSupervisedFixtureSchemaTest(unittest.TestCase):
    def test_project_synthetic_supervised_fixture_shape(self) -> None:
        self.assertTrue(FIXTURE_PATH.exists())
        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

        self.assertIsInstance(fixture, dict)
        self.assertTrue(REQUIRED_TOP_LEVEL_KEYS.issubset(fixture))
        self.assertEqual(fixture["schema_version"], FEATURE_LABEL_SMOKE_SCHEMA_VERSION)
        self.assertTrue(fixture["fixture_id"])
        self._assert_provenance(fixture["provenance"])
        self._assert_non_empty_string_list(fixture["feature_families"])
        self._assert_non_empty_string_list(fixture["label_families"])
        self._assert_public_information_fields(fixture["public_information_fields"])
        self._assert_forbidden_information_absent(
            fixture["forbidden_information_absent"]
        )
        self._assert_warnings(fixture["evidence_warnings"])
        self._assert_non_evidence(fixture["non_evidence"])
        normalized = validate_feature_label_smoke_mapping(fixture)
        json.dumps(normalized, sort_keys=True)

    def _assert_provenance(self, provenance: object) -> None:
        self.assertIsInstance(provenance, dict)
        self.assertEqual(provenance["source_type"], SYNTHETIC_LOCAL_SOURCE_TYPE)
        self.assertIs(provenance["project_authored"], True)
        self.assertIs(provenance["synthetic"], True)
        self.assertIs(provenance["local_only"], True)
        self.assertIn("not_approved", provenance["source_approval"])
        for flag in FALSE_PROVENANCE_FLAGS:
            self.assertIn(flag, provenance)
            self.assertIs(provenance[flag], False, flag)

    def _assert_public_information_fields(self, fields: object) -> None:
        self.assertIsInstance(fields, dict)
        self.assertIs(fields["public_information_only"], True)
        self.assertIs(fields["decision_time_only"], True)
        forbidden_keys = {"hidden_information", "future_information"}
        self.assertTrue(forbidden_keys.isdisjoint(fields.keys()))

    def _assert_forbidden_information_absent(self, flags: object) -> None:
        self.assertIsInstance(flags, dict)
        self.assertIs(flags["hidden_information_absent"], True)
        self.assertIs(flags["future_information_absent"], True)

    def _assert_warnings(self, warnings: object) -> None:
        self.assertIsInstance(warnings, list)
        text = " ".join(str(warning) for warning in warnings).lower()
        for term in REQUIRED_WARNING_TERMS:
            self.assertIn(term, text)

    def _assert_non_evidence(self, non_evidence: object) -> None:
        self.assertIsInstance(non_evidence, dict)
        for flag in FALSE_NON_EVIDENCE_FLAGS:
            self.assertIn(flag, non_evidence)
            self.assertIs(non_evidence[flag], False, flag)

    def _assert_non_empty_string_list(self, value: object) -> None:
        self.assertIsInstance(value, list)
        self.assertGreater(len(value), 0)
        for item in value:
            self.assertIsInstance(item, str)
            self.assertTrue(item.strip())


if __name__ == "__main__":
    unittest.main()
