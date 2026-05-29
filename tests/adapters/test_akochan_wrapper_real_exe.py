from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.adapters.akochan_wrapper import AkochanWrapper  # noqa: E402


FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "akochan"
LEGAL_ACTION_JSON = FIXTURE_DIR / "legal_action_minimal.json"


def _real_system_exe() -> str:
    value = os.environ.get("AKOCHAN_SYSTEM_EXE")
    if not value:
        raise unittest.SkipTest("AKOCHAN_SYSTEM_EXE is not set")
    if not Path(value).exists():
        raise unittest.SkipTest(f"AKOCHAN_SYSTEM_EXE does not exist: {value}")
    return value


class AkochanWrapperRealExeTest(unittest.TestCase):
    def make_wrapper(self) -> AkochanWrapper:
        return AkochanWrapper(
            system_exe=_real_system_exe(),
            build_environment=os.environ.get(
                "AKOCHAN_BUILD_ENV", "github-actions-ubuntu-real-exe"
            ),
            timeout_seconds=120,
        )

    def test_real_exe_legal_action_fixed_sample(self) -> None:
        payload = json.loads(LEGAL_ACTION_JSON.read_text(encoding="utf-8"))
        result = self.make_wrapper().run_legal_action(payload)

        self.assertEqual(result.audit_log.exit_code, 0)
        self.assertIsNotNone(result.parsed_json)
        self.assertIsInstance(result.normalized_actions, list)
        self.assertFalse(result.audit_log.training_related)
        self.assertFalse(result.audit_log.self_play_related)
        self.assertFalse(result.audit_log.tenhou_related)

    def test_real_exe_mjai_log_fixed_sample(self) -> None:
        log_path = os.environ.get("AKOCHAN_MJAI_LOG_SAMPLE")
        if not log_path:
            self.skipTest("AKOCHAN_MJAI_LOG_SAMPLE is not set")
        if not Path(log_path).exists():
            self.skipTest(f"AKOCHAN_MJAI_LOG_SAMPLE does not exist: {log_path}")

        result = self.make_wrapper().run_mjai_log(log_path, actor=0, mode=2)

        self.assertEqual(result.audit_log.exit_code, 0)
        self.assertIsNotNone(result.parsed_json)
        self.assertFalse(result.audit_log.training_related)
        self.assertFalse(result.audit_log.self_play_related)
        self.assertFalse(result.audit_log.tenhou_related)


if __name__ == "__main__":
    unittest.main()
