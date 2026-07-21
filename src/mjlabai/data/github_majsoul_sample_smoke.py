"""Bounded local inspection for explicitly GitHub-published Mahjong Soul samples.

The helpers in this module never access the network. Callers must provide an
immutable GitHub source description and either bytes already fetched from
GitHub or a local temporary path. The output is metadata-only: it never returns
raw replay content or player identifiers and never approves training use.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Mapping, Sequence


MAX_SAMPLE_RECORDS = 100
MAX_SAMPLE_BYTES = 5 * 1024 * 1024
GITHUB_SAMPLE_SMOKE_VERSION = "github_majsoul_sample_smoke_v0.1"

_HEX_40 = re.compile(r"^[0-9a-f]{40}$")
_HEX_64 = re.compile(r"^[0-9a-f]{64}$")
_REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
_PLAYER_ACTION_LINE = re.compile(
    r"(?m)^\S.*\s(?:deal|discard) tile b['\"][0-9][mpsz]['\"]"
)
_ANALYSIS_MARKERS = ("玩家手牌", " deal tile b'", " discard tile b'")
_MJAI_DECISION_TYPES = frozenset(
    {"dahai", "chi", "pon", "ankan", "kakan", "daiminkan", "reach", "hora"}
)


class GitHubMahjongSoulSampleSmokeError(ValueError):
    """Raised when a bounded GitHub sample inspection contract is violated."""


@dataclass(frozen=True)
class GitHubSampleSpec:
    """Immutable provenance and integrity expectation for one GitHub file."""

    repository: str
    commit: str
    path: str
    expected_sha256: str
    expected_bytes: int
    replay_record_count: int = 1
    rights_status: str = "unverified"

    def __post_init__(self) -> None:
        errors = []
        if not _REPOSITORY.fullmatch(self.repository):
            errors.append("repository must be an owner/name GitHub repository")
        if not _HEX_40.fullmatch(self.commit):
            errors.append("commit must be a lowercase 40-character Git SHA")
        path = Path(self.path)
        if not self.path or path.is_absolute() or ".." in path.parts:
            errors.append("path must be a non-empty repository-relative path")
        if not _HEX_64.fullmatch(self.expected_sha256):
            errors.append("expected_sha256 must be a lowercase SHA-256 digest")
        if not isinstance(self.expected_bytes, int) or not (
            1 <= self.expected_bytes <= MAX_SAMPLE_BYTES
        ):
            errors.append(
                f"expected_bytes must be between 1 and {MAX_SAMPLE_BYTES}"
            )
        if not isinstance(self.replay_record_count, int) or not (
            1 <= self.replay_record_count <= MAX_SAMPLE_RECORDS
        ):
            errors.append(
                f"replay_record_count must be between 1 and {MAX_SAMPLE_RECORDS}"
            )
        if self.rights_status != "unverified":
            errors.append("rights_status must remain 'unverified' for this smoke")
        if errors:
            raise GitHubMahjongSoulSampleSmokeError("; ".join(errors))

    @property
    def source_key(self) -> str:
        return f"{self.repository}@{self.commit}:{self.path}"


@dataclass(frozen=True)
class GitHubSampleInspection:
    """Content-free inspection result for one locally available sample."""

    smoke_version: str
    source_key: str
    byte_count: int
    sha256: str
    content_kind: str
    replay_record_count: int
    utf8_decodable: bool
    action_marker_count: int
    potential_player_identifiers: bool
    structurally_training_ready: bool
    rights_status: str
    training_use_approved: bool
    platform_accessed: bool
    warnings: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return json.loads(json.dumps(asdict(self), sort_keys=True))


@dataclass(frozen=True)
class GitHubSampleSmokeReport:
    """Aggregate metadata-only report for the bounded sample set."""

    smoke_version: str
    sample_file_count: int
    replay_record_count: int
    content_kinds: tuple[str, ...]
    structurally_training_ready_count: int
    any_potential_player_identifiers: bool
    all_hashes_verified: bool
    rights_verified: bool
    training_use_approved: bool
    platform_accessed: bool
    warnings: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return json.loads(json.dumps(asdict(self), sort_keys=True))


def inspect_github_sample_payload(
    spec: GitHubSampleSpec,
    payload: bytes,
) -> GitHubSampleInspection:
    """Inspect bytes already obtained from the immutable GitHub source."""

    if not isinstance(payload, bytes):
        raise GitHubMahjongSoulSampleSmokeError("payload must be bytes")
    if not payload:
        raise GitHubMahjongSoulSampleSmokeError("payload must not be empty")
    if len(payload) > MAX_SAMPLE_BYTES:
        raise GitHubMahjongSoulSampleSmokeError(
            f"payload exceeds {MAX_SAMPLE_BYTES} bytes"
        )

    digest = hashlib.sha256(payload).hexdigest()
    if len(payload) != spec.expected_bytes:
        raise GitHubMahjongSoulSampleSmokeError(
            f"byte count mismatch for {spec.source_key}"
        )
    if digest != spec.expected_sha256:
        raise GitHubMahjongSoulSampleSmokeError(
            f"SHA-256 mismatch for {spec.source_key}"
        )

    try:
        text = payload.decode("utf-8")
        utf8_decodable = True
    except UnicodeDecodeError:
        text = ""
        utf8_decodable = False

    content_kind = _classify_content(text, utf8_decodable)
    action_marker_count = (
        text.count(" deal tile b'") + text.count(" discard tile b'")
        if utf8_decodable
        else 0
    )
    potential_player_identifiers = bool(
        utf8_decodable and _PLAYER_ACTION_LINE.search(text)
    )
    structurally_training_ready = content_kind == "mjai_jsonl"

    return GitHubSampleInspection(
        smoke_version=GITHUB_SAMPLE_SMOKE_VERSION,
        source_key=spec.source_key,
        byte_count=len(payload),
        sha256=digest,
        content_kind=content_kind,
        replay_record_count=spec.replay_record_count,
        utf8_decodable=utf8_decodable,
        action_marker_count=action_marker_count,
        potential_player_identifiers=potential_player_identifiers,
        structurally_training_ready=structurally_training_ready,
        rights_status=spec.rights_status,
        training_use_approved=False,
        platform_accessed=False,
        warnings=(
            "GitHub visibility is not a license",
            "local read-only feasibility evidence only",
            "not approved training data",
            "not model strength evidence",
        ),
    )


def inspect_local_github_sample(
    spec: GitHubSampleSpec,
    local_path: Path,
) -> GitHubSampleInspection:
    """Read one local temporary file and inspect it without network access."""

    path = Path(local_path)
    if not path.is_file():
        raise GitHubMahjongSoulSampleSmokeError("local_path must be an existing file")
    return inspect_github_sample_payload(spec, path.read_bytes())


def build_github_sample_smoke_report(
    inspections: Sequence[GitHubSampleInspection],
) -> GitHubSampleSmokeReport:
    """Build an aggregate report while enforcing the <=100-record boundary."""

    if not inspections:
        raise GitHubMahjongSoulSampleSmokeError("inspections must not be empty")
    if not isinstance(inspections, Sequence):
        raise GitHubMahjongSoulSampleSmokeError("inspections must be a sequence")
    if any(not isinstance(item, GitHubSampleInspection) for item in inspections):
        raise GitHubMahjongSoulSampleSmokeError(
            "every inspection must be a GitHubSampleInspection"
        )

    source_keys = [item.source_key for item in inspections]
    if len(set(source_keys)) != len(source_keys):
        raise GitHubMahjongSoulSampleSmokeError("duplicate GitHub source_key")
    replay_record_count = sum(item.replay_record_count for item in inspections)
    if replay_record_count > MAX_SAMPLE_RECORDS:
        raise GitHubMahjongSoulSampleSmokeError(
            f"replay_record_count exceeds {MAX_SAMPLE_RECORDS}"
        )

    return GitHubSampleSmokeReport(
        smoke_version=GITHUB_SAMPLE_SMOKE_VERSION,
        sample_file_count=len(inspections),
        replay_record_count=replay_record_count,
        content_kinds=tuple(sorted({item.content_kind for item in inspections})),
        structurally_training_ready_count=sum(
            item.structurally_training_ready for item in inspections
        ),
        any_potential_player_identifiers=any(
            item.potential_player_identifiers for item in inspections
        ),
        all_hashes_verified=True,
        rights_verified=False,
        training_use_approved=False,
        platform_accessed=False,
        warnings=(
            "bounded GitHub sample inspection only",
            "source rights remain unverified",
            "no platform access was performed",
            "not training or strength evidence",
        ),
    )


def _classify_content(text: str, utf8_decodable: bool) -> str:
    if not utf8_decodable:
        return "unrecognized_binary"
    if _looks_like_mjai_jsonl(text):
        return "mjai_jsonl"
    if all(marker in text for marker in _ANALYSIS_MARKERS):
        return "majsoul_analysis_transcript"
    try:
        json.loads(text)
    except json.JSONDecodeError:
        return "unrecognized_text"
    return "generic_json"


def _looks_like_mjai_jsonl(text: str) -> bool:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return False
    events = []
    try:
        for line in lines:
            event = json.loads(line)
            if not isinstance(event, Mapping) or not isinstance(event.get("type"), str):
                return False
            events.append(event["type"])
    except json.JSONDecodeError:
        return False
    event_types = set(events)
    required_lifecycle = {"start_game", "start_kyoku", "end_kyoku", "end_game"}
    return required_lifecycle.issubset(event_types) and bool(
        event_types.intersection(_MJAI_DECISION_TYPES)
    )


__all__ = [
    "GITHUB_SAMPLE_SMOKE_VERSION",
    "MAX_SAMPLE_BYTES",
    "MAX_SAMPLE_RECORDS",
    "GitHubMahjongSoulSampleSmokeError",
    "GitHubSampleInspection",
    "GitHubSampleSmokeReport",
    "GitHubSampleSpec",
    "build_github_sample_smoke_report",
    "inspect_github_sample_payload",
    "inspect_local_github_sample",
]
