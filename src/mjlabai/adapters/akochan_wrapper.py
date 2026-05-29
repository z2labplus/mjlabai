"""Minimal Akochan wrapper skeleton for fixed F2 smoke samples.

This module shells out only to the two audited non-training commands used by
the F2 skeleton: ``legal_action`` and ``mjai_log``. It does not vendor,
download, build, or store Akochan source or binaries.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
from typing import Any, Mapping, Sequence


AKOCHAN_REPO = "https://github.com/critter-mj/akochan.git"
AKOCHAN_COMMIT = "53188a0b926fbab38177f88c3cd87d554cf412af"
DEFAULT_LICENSE_NOTE = "Akochan custom license; private/internal audit only."
DEFAULT_REPRODUCIBILITY_NOTE = (
    "Akochan is called from an explicit external path; no third-party source "
    "or binary is stored in this repository."
)
_ALLOWED_SUBCOMMANDS = {"legal_action", "mjai_log"}


class AkochanWrapperError(RuntimeError):
    """Base exception for wrapper failures."""


class AkochanOutputParseError(AkochanWrapperError):
    """Raised when Akochan stdout cannot be parsed as JSON."""

    def __init__(self, message: str, *, audit_log: "AkochanAuditLog") -> None:
        super().__init__(message)
        self.audit_log = audit_log


@dataclass(frozen=True)
class AkochanAuditLog:
    """Audit record required for every wrapper subprocess call."""

    tool_name: str
    external_repo: str
    external_commit: str
    build_environment: str
    command: list[str]
    working_dir: str
    input_hash: str
    output_hash: str
    exit_code: int
    stdout_summary: str
    stderr_summary: str
    elapsed_ms: int
    training_related: bool
    self_play_related: bool
    tenhou_related: bool
    license_note: str
    reproducibility_note: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AkochanCommandResult:
    """Wrapper command output with raw and normalized views."""

    raw_stdout: str
    parsed_json: Any
    parsed_records: list[Any]
    normalized_actions: list[dict[str, Any]]
    audit_log: AkochanAuditLog
    parse_warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["audit_log"] = self.audit_log.to_dict()
        return data


class AkochanWrapper:
    """Minimal fixed-command wrapper for an external Akochan executable."""

    def __init__(
        self,
        system_exe: str | os.PathLike[str] | None = None,
        *,
        external_repo: str = AKOCHAN_REPO,
        external_commit: str = AKOCHAN_COMMIT,
        build_environment: str | None = None,
        license_note: str = DEFAULT_LICENSE_NOTE,
        reproducibility_note: str = DEFAULT_REPRODUCIBILITY_NOTE,
        timeout_seconds: float = 30.0,
        stdout_summary_limit: int = 1000,
        stderr_summary_limit: int = 1000,
        working_dir: str | os.PathLike[str] | None = None,
    ) -> None:
        exe = system_exe or os.environ.get("AKOCHAN_SYSTEM_EXE")
        if not exe:
            raise ValueError(
                "Akochan system executable path is required via system_exe "
                "or AKOCHAN_SYSTEM_EXE."
            )
        self.system_exe_path = Path(exe).expanduser().resolve()
        self.system_exe = str(self.system_exe_path)

        working_dir_value = working_dir or os.environ.get("AKOCHAN_WORKING_DIR")
        if working_dir_value:
            working_dir_path = Path(working_dir_value).expanduser().resolve()
        else:
            working_dir_path = self.system_exe_path.parent
        if not working_dir_path.is_dir():
            raise ValueError(
                "Akochan working directory must exist and be a directory: "
                f"{working_dir_path}"
            )
        self.working_dir = str(working_dir_path)

        self.external_repo = external_repo
        self.external_commit = external_commit
        self.build_environment = (
            build_environment
            or os.environ.get("AKOCHAN_BUILD_ENV")
            or "external-path"
        )
        self.license_note = license_note
        self.reproducibility_note = reproducibility_note
        self.timeout_seconds = timeout_seconds
        self.stdout_summary_limit = stdout_summary_limit
        self.stderr_summary_limit = stderr_summary_limit

    def run_legal_action(
        self, input_json: Mapping[str, Any] | Sequence[Any] | str
    ) -> AkochanCommandResult:
        """Run ``system.exe legal_action <json>`` and normalize actions."""

        json_payload = _to_json_string(input_json)
        raw_stdout, audit_log = self._run_subcommand(
            "legal_action",
            [json_payload],
            tool_name="akochan_legal_action",
            input_for_hash=json_payload,
        )
        parsed, records, parse_warnings = self._parse_stdout(raw_stdout, audit_log)
        normalized, warnings = normalize_legal_actions(parsed)
        return AkochanCommandResult(
            raw_stdout=raw_stdout,
            parsed_json=parsed,
            parsed_records=records,
            normalized_actions=normalized,
            audit_log=audit_log,
            parse_warnings=[*parse_warnings, *warnings],
        )

    def run_mjai_log(
        self, log_path: str | os.PathLike[str], actor: int = 0, mode: int = 2
    ) -> AkochanCommandResult:
        """Run ``system.exe mjai_log <log_path> <actor> <mode>``."""

        log_path_str = str(Path(log_path))
        input_for_hash = json.dumps(
            {"log_path": log_path_str, "actor": actor, "mode": mode},
            sort_keys=True,
            separators=(",", ":"),
        )
        raw_stdout, audit_log = self._run_subcommand(
            "mjai_log",
            [log_path_str, str(actor), str(mode)],
            tool_name="akochan_mjai_log",
            input_for_hash=input_for_hash,
        )
        parsed, records, parse_warnings = self._parse_stdout(raw_stdout, audit_log)
        return AkochanCommandResult(
            raw_stdout=raw_stdout,
            parsed_json=parsed,
            parsed_records=records,
            normalized_actions=[],
            audit_log=audit_log,
            parse_warnings=parse_warnings,
        )

    def _run_subcommand(
        self,
        subcommand: str,
        args: list[str],
        *,
        tool_name: str,
        input_for_hash: str,
    ) -> tuple[str, AkochanAuditLog]:
        if subcommand not in _ALLOWED_SUBCOMMANDS:
            raise ValueError(f"Forbidden Akochan subcommand: {subcommand}")

        command = [self.system_exe, subcommand, *args]
        start = time.monotonic()
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=self.timeout_seconds,
            cwd=self.working_dir,
        )
        elapsed_ms = int((time.monotonic() - start) * 1000)

        audit_log = AkochanAuditLog(
            tool_name=tool_name,
            external_repo=self.external_repo,
            external_commit=self.external_commit,
            build_environment=self.build_environment,
            command=command,
            working_dir=self.working_dir,
            input_hash=_sha256_text(input_for_hash),
            output_hash=_sha256_text(completed.stdout),
            exit_code=completed.returncode,
            stdout_summary=_summary(completed.stdout, self.stdout_summary_limit),
            stderr_summary=_summary(completed.stderr, self.stderr_summary_limit),
            elapsed_ms=elapsed_ms,
            training_related=False,
            self_play_related=False,
            tenhou_related=False,
            license_note=self.license_note,
            reproducibility_note=self.reproducibility_note,
        )
        if completed.returncode != 0:
            raise AkochanWrapperError(
                f"Akochan command failed with exit code {completed.returncode}: "
                f"{audit_log.stderr_summary}"
            )
        return completed.stdout, audit_log

    @staticmethod
    def _parse_stdout(
        raw_stdout: str, audit_log: AkochanAuditLog
    ) -> tuple[Any, list[Any], list[str]]:
        return _parse_json_stream(raw_stdout, audit_log)


def _parse_json_stream(
    raw_stdout: str, audit_log: AkochanAuditLog
) -> tuple[Any, list[Any], list[str]]:
    """Parse a single JSON value or a strict stream of JSON values."""

    warnings: list[str] = []
    if raw_stdout != raw_stdout.strip():
        warnings.append("stdout had surrounding whitespace")

    if not raw_stdout.strip():
        raise AkochanOutputParseError(
            _parse_error_message(
                raw_stdout,
                "empty stdout",
                parsed_record_count=0,
                failure_position=0,
            ),
            audit_log=audit_log,
        )

    try:
        parsed = json.loads(raw_stdout)
        return parsed, [parsed], warnings
    except json.JSONDecodeError as single_json_error:
        single_error_summary = f"{single_json_error}"
        single_error_position = single_json_error.pos
        decoder = json.JSONDecoder()
        records: list[Any] = []
        position = 0
        length = len(raw_stdout)

        while True:
            while position < length and raw_stdout[position].isspace():
                position += 1
            if position >= length:
                break
            try:
                record, end = decoder.raw_decode(raw_stdout, position)
            except json.JSONDecodeError as stream_error:
                raise AkochanOutputParseError(
                    _parse_error_message(
                        raw_stdout,
                        f"{stream_error}",
                        parsed_record_count=len(records),
                        failure_position=stream_error.pos,
                    ),
                    audit_log=audit_log,
                ) from stream_error

            if end <= position:
                raise AkochanOutputParseError(
                    _parse_error_message(
                        raw_stdout,
                        "JSON stream parser made no progress",
                        parsed_record_count=len(records),
                        failure_position=position,
                    ),
                    audit_log=audit_log,
                ) from single_json_error

            records.append(record)
            position = end

    if not records:
        raise AkochanOutputParseError(
            _parse_error_message(
                raw_stdout,
                single_error_summary,
                parsed_record_count=0,
                failure_position=single_error_position,
            ),
            audit_log=audit_log,
        )

    warnings.append("JSON stream parser used")
    if len(records) > 1:
        warnings.append("multiple JSON records parsed")

    if len(records) == 1:
        return records[0], records, warnings
    return records, records, warnings


def _parse_error_message(
    raw_stdout: str,
    error_summary: str,
    *,
    parsed_record_count: int,
    failure_position: int,
) -> str:
    return (
        "Akochan stdout was not parseable as single JSON or strict JSON stream: "
        f"{error_summary}; parsed_record_count={parsed_record_count}; "
        f"failure_position={failure_position}; "
        f"stdout_sha256={_sha256_text(raw_stdout)}; "
        f"stdout_summary={_summary(raw_stdout, 2000)!r}"
    )


def normalize_legal_actions(parsed_json: Any) -> tuple[list[dict[str, Any]], list[str]]:
    """Normalize Akochan/mjai-style legal-action output to project schema."""

    warnings: list[str] = []
    if not isinstance(parsed_json, list):
        warnings.append("legal_action output is not a list; raw output preserved only")
        return [], warnings

    normalized: list[dict[str, Any]] = []
    for index, raw_action in enumerate(parsed_json):
        if not isinstance(raw_action, dict):
            warnings.append(f"action[{index}] is not an object; preserved as raw")
            normalized.append(
                {
                    "source": "akochan",
                    "action_type": "unknown",
                    "actor": None,
                    "tile": None,
                    "tsumogiri": None,
                    "raw": raw_action,
                }
            )
            continue

        action_type = raw_action.get("type", "unknown")
        normalized_action: dict[str, Any] = {
            "source": "akochan",
            "action_type": action_type,
            "actor": raw_action.get("actor"),
            "tile": raw_action.get("pai"),
            "tsumogiri": raw_action.get("tsumogiri"),
            "raw": dict(raw_action),
        }
        if action_type != "dahai":
            warnings.append(
                f"action[{index}] type {action_type!r} is not fully normalized"
            )
        normalized.append(normalized_action)

    return normalized, warnings


def _to_json_string(value: Mapping[str, Any] | Sequence[Any] | str) -> str:
    if isinstance(value, str):
        json.loads(value)
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _summary(value: str, limit: int) -> str:
    value = value.strip()
    if len(value) <= limit:
        return value
    return value[:limit] + "...<truncated>"
