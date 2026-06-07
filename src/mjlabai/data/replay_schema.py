"""Minimal P6 replay schema helpers for the synthetic smoke fixture.

This module validates only project-authored synthetic/local replay fixture
mappings. It does not parse real logs, read files, ingest data, extract
features, generate labels, call models, or connect to Tenhou.
"""

from __future__ import annotations

import json
from typing import Any, Mapping


REPLAY_SCHEMA_VERSION = "p6_replay_schema_v0.1"
PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY = (
    "project_authored_synthetic_local_fixture"
)

REQUIRED_TOP_LEVEL_KEYS = frozenset(
    {
        "schema_version",
        "fixture_id",
        "source_id",
        "source_category",
        "source_note",
        "warnings",
        "source_provenance",
        "records",
        "evidence_refs",
        "risk_refs",
    }
)
REQUIRED_RECORD_KEYS = frozenset(
    {
        "schema_version",
        "replay_id",
        "source_id",
        "source_record_id",
        "transform_version",
        "game_context",
        "participants",
        "event_sequence",
        "decision_state_boundary",
        "terminal_result",
        "validation_metadata",
    }
)
REQUIRED_PROVENANCE_KEYS = frozenset(
    {
        "project_authored",
        "synthetic_local",
        "rights_status",
        "allowed_use",
        "may_enter_git",
        "uses_real_tenhou",
        "uses_real_haifu",
        "uses_external_log",
        "uses_platform_data",
        "uses_model_output",
        "training_use",
        "strength_evidence",
        "luckyj_comparison",
    }
)
_REQUIRED_NOTE_TERMS = (
    "synthetic",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not platform data",
    "not model output",
    "not training",
    "not model strength",
    "not luckyj",
)
_FALSE_PROVENANCE_FLAGS = (
    "uses_real_tenhou",
    "uses_real_haifu",
    "uses_external_log",
    "uses_platform_data",
    "uses_model_output",
    "training_use",
    "strength_evidence",
    "luckyj_comparison",
)
_FORBIDDEN_KEY_NAMES = frozenset(
    {
        "account_id",
        "session_id",
        "cookie",
        "token",
        "private_log",
        "model_output",
        "training_label",
        "supervised_label",
        "label",
        "labels",
    }
)


def validate_replay_record(record: Mapping[str, Any]) -> list[str]:
    """Return validation errors for one synthetic replay record mapping."""

    errors: list[str] = []
    if not isinstance(record, Mapping):
        return ["record must be a mapping"]

    _require_keys(record, REQUIRED_RECORD_KEYS, "record", errors)
    _validate_schema_version(record.get("schema_version"), "record", errors)
    _validate_non_empty_string(record.get("replay_id"), "record.replay_id", errors)
    _validate_non_empty_string(record.get("source_id"), "record.source_id", errors)
    _validate_non_empty_string(
        record.get("source_record_id"),
        "record.source_record_id",
        errors,
    )
    _validate_non_empty_string(
        record.get("transform_version"),
        "record.transform_version",
        errors,
    )
    _validate_mapping(record.get("game_context"), "record.game_context", errors)
    _validate_non_empty_list(
        record.get("participants"),
        "record.participants",
        errors,
    )
    _validate_non_empty_list(
        record.get("event_sequence"),
        "record.event_sequence",
        errors,
    )
    _validate_mapping(
        record.get("decision_state_boundary"),
        "record.decision_state_boundary",
        errors,
    )
    _validate_mapping(record.get("terminal_result"), "record.terminal_result", errors)
    _validate_mapping(
        record.get("validation_metadata"),
        "record.validation_metadata",
        errors,
    )
    _validate_forbidden_keys(record, "record", errors)
    _validate_json_safe(record, "record", errors)
    return errors


def validate_replay_fixture(fixture: Mapping[str, Any]) -> list[str]:
    """Return validation errors for the project-authored synthetic fixture."""

    errors: list[str] = []
    if not isinstance(fixture, Mapping):
        return ["fixture must be a mapping"]

    _require_keys(fixture, REQUIRED_TOP_LEVEL_KEYS, "fixture", errors)
    _validate_schema_version(fixture.get("schema_version"), "fixture", errors)
    _validate_non_empty_string(fixture.get("fixture_id"), "fixture_id", errors)
    _validate_non_empty_string(fixture.get("source_id"), "source_id", errors)
    if fixture.get("source_category") != PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY:
        errors.append(
            "source_category must be "
            f"{PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY!r}"
        )

    source_note = fixture.get("source_note")
    _validate_non_empty_string(source_note, "source_note", errors)
    if isinstance(source_note, str):
        _require_terms(source_note, _REQUIRED_NOTE_TERMS, "source_note", errors)

    warnings = fixture.get("warnings")
    _validate_non_empty_list(warnings, "warnings", errors)
    if isinstance(warnings, list):
        warning_text = " ".join(str(warning) for warning in warnings)
        _require_terms(warning_text, _REQUIRED_NOTE_TERMS, "warnings", errors)

    _validate_source_provenance(
        fixture.get("source_provenance"),
        fixture.get("source_id"),
        errors,
    )
    _validate_non_empty_string_list(
        fixture.get("evidence_refs"),
        "evidence_refs",
        errors,
    )
    _validate_non_empty_string_list(fixture.get("risk_refs"), "risk_refs", errors)

    records = fixture.get("records")
    _validate_non_empty_list(records, "records", errors)
    if isinstance(records, list):
        for index, record in enumerate(records):
            for error in validate_replay_record(record):
                errors.append(f"records[{index}].{error}")
            if isinstance(record, Mapping) and record.get("source_id") != fixture.get(
                "source_id"
            ):
                errors.append(
                    f"records[{index}].source_id must match fixture source_id"
                )

    _validate_forbidden_keys(fixture, "fixture", errors)
    _validate_json_safe(fixture, "fixture", errors)
    return errors


def assert_valid_replay_fixture(fixture: Mapping[str, Any]) -> None:
    """Raise ValueError unless the fixture passes synthetic replay validation."""

    errors = validate_replay_fixture(fixture)
    if errors:
        raise ValueError("; ".join(errors))


def is_project_authored_synthetic_fixture(fixture: Mapping[str, Any]) -> bool:
    """Return whether a mapping has the required synthetic/local source guard."""

    if not isinstance(fixture, Mapping):
        return False
    provenance = fixture.get("source_provenance")
    if not isinstance(provenance, Mapping):
        return False
    if fixture.get("source_category") != PROJECT_AUTHORED_SYNTHETIC_SOURCE_CATEGORY:
        return False
    if provenance.get("project_authored") is not True:
        return False
    if provenance.get("synthetic_local") is not True:
        return False
    return all(provenance.get(flag) is False for flag in _FALSE_PROVENANCE_FLAGS)


def _require_keys(
    mapping: Mapping[str, Any],
    required_keys: frozenset[str],
    label: str,
    errors: list[str],
) -> None:
    missing = sorted(required_keys - set(mapping.keys()))
    if missing:
        errors.append(f"{label} missing required keys: {', '.join(missing)}")


def _validate_schema_version(value: object, label: str, errors: list[str]) -> None:
    if value != REPLAY_SCHEMA_VERSION:
        errors.append(f"{label}.schema_version must be {REPLAY_SCHEMA_VERSION!r}")


def _validate_non_empty_string(
    value: object,
    label: str,
    errors: list[str],
) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string")


def _validate_mapping(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, Mapping):
        errors.append(f"{label} must be a mapping")


def _validate_non_empty_list(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{label} must be a non-empty list")


def _validate_non_empty_string_list(
    value: object,
    label: str,
    errors: list[str],
) -> None:
    _validate_non_empty_list(value, label, errors)
    if isinstance(value, list):
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                errors.append(f"{label}[{index}] must be a non-empty string")


def _validate_source_provenance(
    provenance: object,
    source_id: object,
    errors: list[str],
) -> None:
    if not isinstance(provenance, Mapping):
        errors.append("source_provenance must be a mapping")
        return
    _require_keys(provenance, REQUIRED_PROVENANCE_KEYS, "source_provenance", errors)
    if provenance.get("project_authored") is not True:
        errors.append("source_provenance.project_authored must be true")
    if provenance.get("synthetic_local") is not True:
        errors.append("source_provenance.synthetic_local must be true")
    if provenance.get("rights_status") != "project_authored":
        errors.append("source_provenance.rights_status must be 'project_authored'")
    if provenance.get("source_id") is not None and provenance.get("source_id") != source_id:
        errors.append("source_provenance.source_id must match fixture source_id")
    for flag in _FALSE_PROVENANCE_FLAGS:
        if provenance.get(flag) is not False:
            errors.append(f"source_provenance.{flag} must be false")


def _require_terms(
    text: str,
    required_terms: tuple[str, ...],
    label: str,
    errors: list[str],
) -> None:
    lowered = text.lower()
    for term in required_terms:
        if term not in lowered:
            errors.append(f"{label} must include {term!r}")


def _validate_forbidden_keys(
    value: object,
    path: str,
    errors: list[str],
) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            key_text = str(key).lower()
            if key_text in _FORBIDDEN_KEY_NAMES:
                errors.append(f"{path}.{key} is forbidden in synthetic replay fixture")
            _validate_forbidden_keys(child, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _validate_forbidden_keys(child, f"{path}[{index}]", errors)


def _validate_json_safe(value: object, label: str, errors: list[str]) -> None:
    try:
        json.dumps(value, sort_keys=True)
    except (TypeError, ValueError) as exc:
        errors.append(f"{label} must be JSON-safe: {exc}")
