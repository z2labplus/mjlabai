from __future__ import annotations

import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.adapters.akochan_wrapper import (  # noqa: E402
    AKOCHAN_COMMIT,
    AKOCHAN_REPO,
    AkochanOutputParseError,
    AkochanWrapper,
)


FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "akochan"
FAKE_SYSTEM_EXE = FIXTURE_DIR / "fake_system_exe.py"
LEGAL_ACTION_JSON = FIXTURE_DIR / "legal_action_minimal.json"
MJAI_LOG_SAMPLE = FIXTURE_DIR / "mjai_log_minimal.jsonl"
MJAI_LOG_JSON_LINES_SAMPLE = FIXTURE_DIR / "mjai_log_json_lines.jsonl"
MJAI_LOG_CONCATENATED_SAMPLE = FIXTURE_DIR / "mjai_log_concatenated.jsonl"
MJAI_LOG_PRETTY_STREAM_SAMPLE = FIXTURE_DIR / "mjai_log_pretty_stream.jsonl"
MJAI_LOG_INVALID_MIXED_SAMPLE = FIXTURE_DIR / "mjai_log_invalid_mixed.jsonl"
FAKE_RUNTIME_FILE = FIXTURE_DIR / "fake_setup_mjai.json"


class AkochanWrapperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mode = FAKE_SYSTEM_EXE.stat().st_mode
        FAKE_SYSTEM_EXE.chmod(mode | stat.S_IXUSR)

    def make_wrapper(
        self, *, working_dir: str | os.PathLike[str] | None = None
    ) -> AkochanWrapper:
        return AkochanWrapper(
            system_exe=FAKE_SYSTEM_EXE,
            build_environment="test-fake-executable",
            timeout_seconds=5,
            working_dir=working_dir,
        )

    def test_run_legal_action_with_fake_executable(self) -> None:
        payload = json.loads(LEGAL_ACTION_JSON.read_text(encoding="utf-8"))
        result = self.make_wrapper().run_legal_action(payload)

        self.assertIsInstance(result.parsed_json, list)
        self.assertEqual(result.parsed_records, [result.parsed_json])
        self.assertEqual(result.parse_warnings, ["stdout had surrounding whitespace"])
        self.assertEqual(len(result.normalized_actions), 2)
        self.assertEqual(
            result.normalized_actions[0],
            {
                "source": "akochan",
                "action_type": "dahai",
                "actor": 0,
                "tile": "1s",
                "tsumogiri": True,
                "raw": {
                    "actor": 0,
                    "pai": "1s",
                    "tsumogiri": True,
                    "type": "dahai",
                },
            },
        )

        audit = result.audit_log
        self.assertEqual(audit.tool_name, "akochan_legal_action")
        self.assertEqual(audit.external_repo, AKOCHAN_REPO)
        self.assertEqual(audit.external_commit, AKOCHAN_COMMIT)
        self.assertEqual(audit.build_environment, "test-fake-executable")
        self.assertEqual(audit.working_dir, str(FIXTURE_DIR))
        self.assertEqual(audit.exit_code, 0)
        self.assertFalse(audit.training_related)
        self.assertFalse(audit.self_play_related)
        self.assertFalse(audit.tenhou_related)
        self.assertIn("legal_action", audit.command)
        self.assertEqual(len(audit.input_hash), 64)
        self.assertEqual(len(audit.output_hash), 64)
        self.assertIn("private/internal audit", audit.license_note)
        self.assertIn("third-party source or binary", audit.reproducibility_note)

    def test_run_mjai_log_with_fake_executable(self) -> None:
        result = self.make_wrapper().run_mjai_log(MJAI_LOG_SAMPLE, actor=0, mode=2)

        self.assertEqual(result.normalized_actions, [])
        self.assertEqual(result.parse_warnings, ["stdout had surrounding whitespace"])
        self.assertEqual(result.parsed_json["type"], "start_game")
        self.assertEqual(result.parsed_records, [result.parsed_json])
        self.assertEqual(result.parsed_json["actor"], 0)
        self.assertEqual(result.parsed_json["mode"], 2)
        self.assertEqual(result.parsed_json["cwd"], str(FIXTURE_DIR))
        self.assertEqual(result.audit_log.tool_name, "akochan_mjai_log")
        self.assertEqual(result.audit_log.working_dir, str(FIXTURE_DIR))
        self.assertIn("mjai_log", result.audit_log.command)
        self.assertFalse(result.audit_log.training_related)
        self.assertFalse(result.audit_log.self_play_related)
        self.assertFalse(result.audit_log.tenhou_related)

    def test_run_mjai_log_parses_json_lines(self) -> None:
        result = self.make_wrapper().run_mjai_log(
            MJAI_LOG_JSON_LINES_SAMPLE, actor=0, mode=2
        )

        self.assertIsInstance(result.parsed_json, list)
        self.assertEqual(len(result.parsed_records), 2)
        self.assertEqual(result.parsed_records[0]["type"], "start_game")
        self.assertEqual(result.parsed_records[1]["type"], "end_kyoku")
        self.assertIn("JSON stream parser used", result.parse_warnings)
        self.assertIn("multiple JSON records parsed", result.parse_warnings)
        self.assertIn("stdout had surrounding whitespace", result.parse_warnings)

    def test_run_mjai_log_parses_concatenated_json_objects(self) -> None:
        result = self.make_wrapper().run_mjai_log(
            MJAI_LOG_CONCATENATED_SAMPLE, actor=0, mode=2
        )

        self.assertEqual(len(result.parsed_records), 2)
        self.assertEqual(result.parsed_json, result.parsed_records)
        self.assertEqual(result.parsed_records[0]["type"], "start_game")
        self.assertEqual(result.parsed_records[1]["type"], "end_kyoku")
        self.assertIn("JSON stream parser used", result.parse_warnings)
        self.assertIn("multiple JSON records parsed", result.parse_warnings)

    def test_run_mjai_log_parses_pretty_printed_json_record_sequence(self) -> None:
        result = self.make_wrapper().run_mjai_log(
            MJAI_LOG_PRETTY_STREAM_SAMPLE, actor=0, mode=2
        )

        self.assertEqual(len(result.parsed_records), 2)
        self.assertEqual(result.parsed_json, result.parsed_records)
        self.assertEqual(result.parsed_records[0]["type"], "start_game")
        self.assertEqual(result.parsed_records[1]["type"], "end_kyoku")
        self.assertIn("JSON stream parser used", result.parse_warnings)
        self.assertIn("multiple JSON records parsed", result.parse_warnings)

    def test_invalid_mixed_stdout_raises_with_bounded_diagnostics(self) -> None:
        with self.assertRaises(AkochanOutputParseError) as raised:
            self.make_wrapper().run_mjai_log(
                MJAI_LOG_INVALID_MIXED_SAMPLE, actor=0, mode=2
            )

        message = str(raised.exception)
        self.assertIn("stdout was not parseable as single JSON or strict JSON stream", message)
        self.assertIn("parsed_record_count=1", message)
        self.assertIn("failure_position=", message)
        self.assertIn("stdout_sha256=", message)
        self.assertIn("stdout_summary=", message)
        self.assertLess(len(message), 2600)
        self.assertEqual(raised.exception.audit_log.tool_name, "akochan_mjai_log")
        self.assertFalse(raised.exception.audit_log.training_related)
        self.assertFalse(raised.exception.audit_log.self_play_related)
        self.assertFalse(raised.exception.audit_log.tenhou_related)

    def test_default_working_dir_is_system_exe_directory(self) -> None:
        wrapper = self.make_wrapper()

        self.assertEqual(wrapper.working_dir, str(FIXTURE_DIR))

    def test_explicit_working_dir_is_used_for_subprocess(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            (temp_path / FAKE_RUNTIME_FILE.name).write_text(
                FAKE_RUNTIME_FILE.read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            result = self.make_wrapper(working_dir=temp_path).run_mjai_log(
                MJAI_LOG_SAMPLE, actor=0, mode=2
            )

        self.assertEqual(result.parsed_json["cwd"], str(temp_path.resolve()))
        self.assertEqual(result.audit_log.working_dir, str(temp_path.resolve()))

    def test_working_dir_can_come_from_environment(self) -> None:
        old_value = os.environ.get("AKOCHAN_WORKING_DIR")
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            (temp_path / FAKE_RUNTIME_FILE.name).write_text(
                FAKE_RUNTIME_FILE.read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            os.environ["AKOCHAN_WORKING_DIR"] = str(temp_path)
            try:
                result = self.make_wrapper().run_mjai_log(
                    MJAI_LOG_SAMPLE, actor=0, mode=2
                )
            finally:
                if old_value is None:
                    os.environ.pop("AKOCHAN_WORKING_DIR", None)
                else:
                    os.environ["AKOCHAN_WORKING_DIR"] = old_value

        self.assertEqual(result.parsed_json["cwd"], str(temp_path.resolve()))
        self.assertEqual(result.audit_log.working_dir, str(temp_path.resolve()))

    def test_missing_working_dir_raises_clear_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_dir = Path(temp_dir) / "missing"

        with self.assertRaises(ValueError) as raised:
            self.make_wrapper(working_dir=missing_dir)

        self.assertIn("working directory must exist", str(raised.exception))

    def test_system_exe_can_come_from_environment(self) -> None:
        old_value = os.environ.get("AKOCHAN_SYSTEM_EXE")
        os.environ["AKOCHAN_SYSTEM_EXE"] = str(FAKE_SYSTEM_EXE)
        try:
            wrapper = AkochanWrapper(build_environment="test-fake-executable")
            self.assertEqual(wrapper.system_exe, str(FAKE_SYSTEM_EXE.resolve()))
            self.assertEqual(wrapper.working_dir, str(FIXTURE_DIR))
        finally:
            if old_value is None:
                os.environ.pop("AKOCHAN_SYSTEM_EXE", None)
            else:
                os.environ["AKOCHAN_SYSTEM_EXE"] = old_value

    def test_non_json_stdout_raises_clear_error(self) -> None:
        with self.assertRaises(AkochanOutputParseError) as raised:
            self.make_wrapper().run_legal_action({"force_invalid_stdout": True})

        self.assertIn("not parseable as single JSON or strict JSON stream", str(raised.exception))
        self.assertIn("stdout_sha256=", str(raised.exception))
        self.assertIn("stdout_summary=", str(raised.exception))
        self.assertEqual(raised.exception.audit_log.tool_name, "akochan_legal_action")
        self.assertFalse(raised.exception.audit_log.training_related)
        self.assertFalse(raised.exception.audit_log.self_play_related)
        self.assertFalse(raised.exception.audit_log.tenhou_related)


if __name__ == "__main__":
    unittest.main()
