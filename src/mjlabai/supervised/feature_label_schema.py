"""Minimal P7 synthetic/local feature-label smoke validation helpers.

This module validates only project-authored synthetic/local supervised smoke
fixture mappings. It does not read files, parse logs, ingest data, extract
features, generate labels, construct supervised datasets, call models, or
train.
"""

from __future__ import annotations

import json
from typing import Any, Mapping


FEATURE_LABEL_SMOKE_SCHEMA_VERSION = "p7_feature_label_smoke_v0.1"
SYNTHETIC_LOCAL_SOURCE_TYPE = "project_authored_synthetic_local_supervised_smoke"

ALLOWED_FEATURE_FAMILIES = frozenset(
    {
        "round_context",
        "seat_turn_context",
        "visible_hand_tile_counts",
        "visible_discard_pond",
        "visible_calls_melds",
        "visible_dora_indicators",
        "score_placement_context",
        "legal_action_mask_candidate",
        "previous_action_context",
        "synthetic_provenance_indicators",
    }
)

ALLOWED_LABEL_FAMILIES = frozenset(
    {
        "action_imitation_label",
        "discard_choice_label",
        "call_no_call_label",
        "riichi_no_riichi_label",
        "legal_action_target_label",
        "synthetic_smoke_label",
        "future_value_reward_target",
        "future_ranking_placement_target",
        "generated_pseudo_label",
        "human_authored_annotation_label",
    }
)

REQUIRED_TOP_LEVEL_KEYS = frozenset(
    {
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
)

REQUIRED_PROVENANCE_KEYS = frozenset(
    {
        "source_type",
        "project_authored",
        "synthetic",
        "local_only",
        "real_data",
        "training_use_approved",
        "source_approval",
        "model_output",
        "self_play",
        "league_output",
        "human_label_real_play",
        "generated_label_from_unapproved_pipeline",
    }
)

REQUIRED_ABSENT_INFORMATION_FLAGS = frozenset(
    {
        "hidden_information_absent",
        "future_information_absent",
    }
)

REQUIRED_NON_EVIDENCE_FLAGS = frozenset(
    {
        "model_strength",
        "tenhou_ranked",
        "stable_dan_ranked_game",
        "luckyj_10_68_comparison",
        "candidate_promotion",
        "training_data_approval",
        "source_approval",
    }
)

_REQUIRED_WARNING_TERMS = (
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

_FALSE_PROVENANCE_FLAGS = (
    "real_data",
    "training_use_approved",
    "model_output",
    "self_play",
    "league_output",
    "human_label_real_play",
    "generated_label_from_unapproved_pipeline",
)

_FORBIDDEN_KEY_NAMES = frozenset(
    {
        "hidden_information",
        "future_information",
        "opponent_hidden_hand",
        "opponent_private_hand",
        "wall_order",
        "future_draw",
        "future_discards",
        "future_calls",
        "future_result",
        "account_id",
        "session_id",
        "cookie",
        "token",
        "private_log",
    }
)

_APPROVAL_CLAIMS = frozenset(
    {
        "approved",
        "true",
        "yes",
        "source_approved",
        "training_approved",
        "approved_for_training",
        "approved_for_ingestion",
    }
)


class FeatureLabelSchemaError(ValueError):
    """Raised when a synthetic feature-label smoke mapping is invalid."""


def validate_feature_label_smoke_mapping(
    mapping: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a JSON-safe normalized dict if a smoke mapping is valid.

    The validator is intentionally narrow: it checks synthetic/local fixture
    shape and guardrails only. It never reads from disk and never derives
    features or labels.
    """

    errors = collect_feature_label_smoke_errors(mapping)
    if errors:
        raise FeatureLabelSchemaError("; ".join(errors))
    return json.loads(json.dumps(mapping, sort_keys=True))


def collect_feature_label_smoke_errors(mapping: Mapping[str, Any]) -> list[str]:
    """Return validation errors for a synthetic feature-label smoke mapping."""

    errors: list[str] = []
    if not isinstance(mapping, Mapping):
        return ["mapping must be a mapping"]

    _require_keys(mapping, REQUIRED_TOP_LEVEL_KEYS, "mapping", errors)
    _validate_non_empty_string(mapping.get("fixture_id"), "fixture_id", errors)
    if mapping.get("schema_version") != FEATURE_LABEL_SMOKE_SCHEMA_VERSION:
        errors.append(
            "schema_version must be "
            f"{FEATURE_LABEL_SMOKE_SCHEMA_VERSION!r}"
        )

    _validate_provenance(mapping.get("provenance"), errors)
    _validate_family_list(
        mapping.get("feature_families"),
        ALLOWED_FEATURE_FAMILIES,
        "feature_families",
        errors,
    )
    _validate_family_list(
        mapping.get("label_families"),
        ALLOWED_LABEL_FAMILIES,
        "label_families",
        errors,
    )
    _validate_public_information_fields(
        mapping.get("public_information_fields"),
        errors,
    )
    _validate_absent_information_flags(
        mapping.get("forbidden_information_absent"),
        errors,
    )
    _validate_evidence_warnings(mapping.get("evidence_warnings"), errors)
    _validate_non_evidence(mapping.get("non_evidence"), errors)
    _validate_forbidden_keys(mapping, "mapping", errors)
    _validate_json_safe(mapping, "mapping", errors)
    return errors


def is_json_safe_mapping(mapping: Mapping[str, Any]) -> bool:
    """Return whether a mapping can be encoded as JSON."""

    try:
        json.dumps(mapping, sort_keys=True)
    except (TypeError, ValueError):
        return False
    return True


def _validate_provenance(value: object, errors: list[str]) -> None:
    _validate_mapping(value, "provenance", errors)
    if not isinstance(value, Mapping):
        return

    _require_keys(value, REQUIRED_PROVENANCE_KEYS, "provenance", errors)
    if value.get("source_type") != SYNTHETIC_LOCAL_SOURCE_TYPE:
        errors.append(f"provenance.source_type must be {SYNTHETIC_LOCAL_SOURCE_TYPE!r}")
    for flag in ("project_authored", "synthetic", "local_only"):
        if value.get(flag) is not True:
            errors.append(f"provenance.{flag} must be true")
    for flag in _FALSE_PROVENANCE_FLAGS:
        if value.get(flag) is not False:
            errors.append(f"provenance.{flag} must be false")
    if _is_approval_claim(value.get("source_approval")):
        errors.append("provenance.source_approval must not claim approval")


def _validate_family_list(
    value: object,
    allowed: frozenset[str],
    label: str,
    errors: list[str],
) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{label} must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{label}[{index}] must be a non-empty string")
        elif item not in allowed:
            errors.append(f"{label}[{index}] has unknown family {item!r}")


def _validate_public_information_fields(value: object, errors: list[str]) -> None:
    _validate_mapping(value, "public_information_fields", errors)
    if not isinstance(value, Mapping):
        return
    if value.get("public_information_only") is not True:
        errors.append("public_information_fields.public_information_only must be true")
    if value.get("decision_time_only") is not True:
        errors.append("public_information_fields.decision_time_only must be true")


def _validate_absent_information_flags(value: object, errors: list[str]) -> None:
    _validate_mapping(value, "forbidden_information_absent", errors)
    if not isinstance(value, Mapping):
        return
    _require_keys(
        value,
        REQUIRED_ABSENT_INFORMATION_FLAGS,
        "forbidden_information_absent",
        errors,
    )
    for flag in REQUIRED_ABSENT_INFORMATION_FLAGS:
        if value.get(flag) is not True:
            errors.append(f"forbidden_information_absent.{flag} must be true")


def _validate_evidence_warnings(value: object, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append("evidence_warnings must be a non-empty list")
        return
    text = " ".join(str(item) for item in value).lower()
    for term in _REQUIRED_WARNING_TERMS:
        if term not in text:
            errors.append(f"evidence_warnings must mention {term!r}")


def _validate_non_evidence(value: object, errors: list[str]) -> None:
    _validate_mapping(value, "non_evidence", errors)
    if not isinstance(value, Mapping):
        return
    _require_keys(value, REQUIRED_NON_EVIDENCE_FLAGS, "non_evidence", errors)
    for flag in REQUIRED_NON_EVIDENCE_FLAGS:
        if value.get(flag) is not False:
            errors.append(f"non_evidence.{flag} must be false")


def _require_keys(
    mapping: Mapping[str, Any],
    required_keys: frozenset[str],
    label: str,
    errors: list[str],
) -> None:
    missing = sorted(required_keys - set(mapping.keys()))
    if missing:
        errors.append(f"{label} missing required keys: {', '.join(missing)}")


def _validate_mapping(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, Mapping):
        errors.append(f"{label} must be a mapping")


def _validate_non_empty_string(
    value: object,
    label: str,
    errors: list[str],
) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string")


def _validate_forbidden_keys(
    value: object,
    path: str,
    errors: list[str],
) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            key_text = str(key)
            if key_text.lower() in _FORBIDDEN_KEY_NAMES:
                errors.append(f"{path}.{key_text} is forbidden")
            _validate_forbidden_keys(child, f"{path}.{key_text}", errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _validate_forbidden_keys(child, f"{path}[{index}]", errors)


def _validate_json_safe(value: object, label: str, errors: list[str]) -> None:
    try:
        json.dumps(value, sort_keys=True)
    except (TypeError, ValueError) as exc:
        errors.append(f"{label} must be JSON-safe: {exc}")


def _is_approval_claim(value: object) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in _APPROVAL_CLAIMS
    return False
