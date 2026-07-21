from __future__ import annotations

import hashlib
import inspect
import json
from pathlib import Path
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.data.github_majsoul_sample_smoke import (
    GITHUB_SAMPLE_SMOKE_VERSION,
    MAX_SAMPLE_RECORDS,
    GitHubMahjongSoulSampleSmokeError,
    GitHubSampleSpec,
    build_github_sample_smoke_report,
    inspect_github_sample_payload,
    inspect_local_github_sample,
)
import mjlabai.data.github_majsoul_sample_smoke as smoke_module


ANALYSIS_STUB = """[['1m', '2m']]
东 1 局 0 本场
玩家手牌：
SyntheticA deal tile b'1m'
SyntheticB discard tile b'2m'
""".encode("utf-8")


def _spec(
    payload: bytes = ANALYSIS_STUB,
    *,
    path: str = "example/project-authored-structure-stub.txt",
    record_count: int = 1,
) -> GitHubSampleSpec:
    return GitHubSampleSpec(
        repository="example/project-authored-stub",
        commit="a" * 40,
        path=path,
        expected_sha256=hashlib.sha256(payload).hexdigest(),
        expected_bytes=len(payload),
        replay_record_count=record_count,
    )


class GitHubMahjongSoulSampleSmokeTest(unittest.TestCase):
    def test_analysis_transcript_returns_content_free_summary(self) -> None:
        result = inspect_github_sample_payload(_spec(), ANALYSIS_STUB)

        self.assertEqual(result.smoke_version, GITHUB_SAMPLE_SMOKE_VERSION)
        self.assertEqual(result.content_kind, "majsoul_analysis_transcript")
        self.assertEqual(result.action_marker_count, 2)
        self.assertTrue(result.potential_player_identifiers)
        self.assertFalse(result.structurally_training_ready)
        self.assertEqual(result.rights_status, "unverified")
        self.assertFalse(result.training_use_approved)
        self.assertFalse(result.platform_accessed)

        encoded = json.dumps(result.to_dict(), sort_keys=True)
        self.assertNotIn("SyntheticA", encoded)
        self.assertNotIn("SyntheticB", encoded)
        self.assertNotIn("玩家手牌", encoded)

    def test_local_path_reader_verifies_hash_and_size(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(ANALYSIS_STUB)

            result = inspect_local_github_sample(_spec(), path)

        self.assertEqual(result.byte_count, len(ANALYSIS_STUB))
        self.assertEqual(result.sha256, hashlib.sha256(ANALYSIS_STUB).hexdigest())

    def test_hash_and_size_mismatch_are_rejected(self) -> None:
        bad_hash = GitHubSampleSpec(
            repository="example/project-authored-stub",
            commit="b" * 40,
            path="example/stub.txt",
            expected_sha256="0" * 64,
            expected_bytes=len(ANALYSIS_STUB),
        )
        with self.assertRaisesRegex(
            GitHubMahjongSoulSampleSmokeError, "SHA-256 mismatch"
        ):
            inspect_github_sample_payload(bad_hash, ANALYSIS_STUB)

        with self.assertRaisesRegex(
            GitHubMahjongSoulSampleSmokeError, "byte count mismatch"
        ):
            inspect_github_sample_payload(_spec(), ANALYSIS_STUB + b"x")

    def test_source_contract_rejects_mutable_or_unsafe_identity(self) -> None:
        cases = {
            "mutable commit": {"commit": "main"},
            "absolute path": {"path": "/tmp/sample.txt"},
            "parent path": {"path": "../sample.txt"},
            "unverified rights only": {"rights_status": "approved"},
        }
        base = {
            "repository": "example/project-authored-stub",
            "commit": "c" * 40,
            "path": "example/stub.txt",
            "expected_sha256": hashlib.sha256(ANALYSIS_STUB).hexdigest(),
            "expected_bytes": len(ANALYSIS_STUB),
        }
        for name, override in cases.items():
            with self.subTest(name=name):
                values = dict(base)
                values.update(override)
                with self.assertRaises(GitHubMahjongSoulSampleSmokeError):
                    GitHubSampleSpec(**values)

    def test_mjai_jsonl_is_structurally_ready_but_not_training_approved(self) -> None:
        payload = (
            '\n'.join(
                json.dumps(event)
                for event in (
                    {"type": "start_game"},
                    {"type": "start_kyoku"},
                    {"type": "dahai", "actor": 0, "pai": "1m"},
                    {"type": "end_kyoku"},
                    {"type": "end_game"},
                )
            )
            + "\n"
        ).encode("utf-8")

        result = inspect_github_sample_payload(_spec(payload), payload)

        self.assertEqual(result.content_kind, "mjai_jsonl")
        self.assertTrue(result.structurally_training_ready)
        self.assertFalse(result.training_use_approved)

    def test_empty_mjai_lifecycle_is_not_structurally_ready(self) -> None:
        payload = (
            '\n'.join(
                json.dumps(event)
                for event in (
                    {"type": "start_game"},
                    {"type": "start_kyoku"},
                    {"type": "end_kyoku"},
                    {"type": "end_game"},
                )
            )
            + "\n"
        ).encode("utf-8")

        result = inspect_github_sample_payload(_spec(payload), payload)

        self.assertEqual(result.content_kind, "unrecognized_text")
        self.assertFalse(result.structurally_training_ready)

    def test_report_enforces_record_cap_and_no_duplicate_source(self) -> None:
        one = inspect_github_sample_payload(_spec(), ANALYSIS_STUB)
        report = build_github_sample_smoke_report([one])

        self.assertEqual(report.sample_file_count, 1)
        self.assertEqual(report.replay_record_count, 1)
        self.assertEqual(report.structurally_training_ready_count, 0)
        self.assertTrue(report.any_potential_player_identifiers)
        self.assertTrue(report.all_hashes_verified)
        self.assertFalse(report.rights_verified)
        self.assertFalse(report.training_use_approved)
        self.assertFalse(report.platform_accessed)

        with self.assertRaisesRegex(
            GitHubMahjongSoulSampleSmokeError, "duplicate GitHub source_key"
        ):
            build_github_sample_smoke_report([one, one])

        payload_b = ANALYSIS_STUB + b"\n"
        too_many = inspect_github_sample_payload(
            _spec(
                payload_b,
                path="example/second-stub.txt",
                record_count=MAX_SAMPLE_RECORDS,
            ),
            payload_b,
        )
        with self.assertRaisesRegex(
            GitHubMahjongSoulSampleSmokeError, "exceeds 100"
        ):
            build_github_sample_smoke_report([one, too_many])

    def test_module_has_no_network_or_process_execution_path(self) -> None:
        source = inspect.getsource(smoke_module)
        for forbidden in (
            "import requests",
            "import urllib",
            "import socket",
            "import subprocess",
            "http://",
            "https://",
            "websocket",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, source.lower())


if __name__ == "__main__":
    unittest.main()
