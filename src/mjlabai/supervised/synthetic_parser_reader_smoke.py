"""Minimal P7 synthetic/local parser-reader smoke helpers.

This module accepts only already-loaded project-authored synthetic/local
feature-label smoke mappings. It does not read files, ingest data, parse real
logs, extract features, generate labels, build datasets, call models, or train.
"""

from __future__ import annotations

import json
from os import PathLike
from typing import Any, Mapping

from mjlabai.supervised.feature_label_schema import (
    collect_feature_label_smoke_errors,
    validate_feature_label_smoke_mapping,
)


SYNTHETIC_PARSER_READER_SMOKE_RECORD_TYPE = (
    "p7_synthetic_local_parser_reader_smoke_v0.1"
)
SYNTHETIC_PARSER_READER_SMOKE_VERSION = "v0.1"

FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS = frozenset(
    {
        "feature_tensor",
        "features",
        "labels",
        "targets",
        "supervised_examples",
        "splits",
        "dataset",
        "training_data",
        "model_input",
        "model_output",
        "evaluation_result",
        "model_strength",
    }
)


class SyntheticParserReaderSmokeError(ValueError):
    """Raised when a synthetic/local parser-reader smoke mapping is invalid."""


def collect_synthetic_parser_reader_smoke_errors(
    mapping: Mapping[str, Any],
) -> list[str]:
    """Return validation errors for an in-memory synthetic/local smoke mapping.

    The function deliberately rejects path-like inputs. The parser-reader smoke
    boundary is a tiny in-memory handoff check, not a file reader, parser, data
    ingestion interface, feature extractor, label generator, or dataset builder.
    """

    if isinstance(mapping, str):
        return ["mapping must be an in-memory mapping; path strings are not accepted"]
    if isinstance(mapping, (bytes, bytearray, PathLike)):
        return ["mapping must be an in-memory mapping; path-like inputs are not accepted"]
    if not isinstance(mapping, Mapping):
        return ["mapping must be an in-memory mapping"]

    errors = collect_feature_label_smoke_errors(mapping)
    if errors:
        return [f"feature-label smoke validation failed: {error}" for error in errors]
    return []


def parse_synthetic_parser_reader_smoke_mapping(
    mapping: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a JSON-safe parser-reader smoke summary for a valid mapping.

    The output is a guardrail summary only. It intentionally excludes feature
    tensors, labels, targets, supervised examples, datasets, splits, model input,
    model output, evaluation results, and model-strength fields.
    """

    errors = collect_synthetic_parser_reader_smoke_errors(mapping)
    if errors:
        raise SyntheticParserReaderSmokeError("; ".join(errors))

    normalized = validate_feature_label_smoke_mapping(mapping)
    provenance = normalized["provenance"]
    public_fields = normalized["public_information_fields"]
    absent_flags = normalized["forbidden_information_absent"]
    non_evidence = normalized["non_evidence"]

    summary = {
        "record_type": SYNTHETIC_PARSER_READER_SMOKE_RECORD_TYPE,
        "parser_reader_smoke_version": SYNTHETIC_PARSER_READER_SMOKE_VERSION,
        "input_fixture_id": normalized["fixture_id"],
        "input_schema_version": normalized["schema_version"],
        "reader_input_kind": "in_memory_mapping",
        "parser_output_kind": "json_safe_guardrail_summary",
        "source_type": provenance["source_type"],
        "project_authored": provenance["project_authored"],
        "synthetic": provenance["synthetic"],
        "local_only": provenance["local_only"],
        "uses_real_data": provenance["real_data"],
        "training_use_approved": provenance["training_use_approved"],
        "source_approval_status": provenance["source_approval"],
        "has_model_output": provenance["model_output"],
        "uses_self_play": provenance["self_play"],
        "uses_league_output": provenance["league_output"],
        "public_information_only": public_fields["public_information_only"],
        "decision_time_only": public_fields["decision_time_only"],
        "hidden_information_absent": absent_flags["hidden_information_absent"],
        "future_information_absent": absent_flags["future_information_absent"],
        "feature_family_count": len(normalized["feature_families"]),
        "label_family_count": len(normalized["label_families"]),
        "evidence_warning_count": len(normalized["evidence_warnings"]),
        "non_evidence_guardrail_count": len(non_evidence),
        "non_evidence_guardrails_all_false": all(
            value is False for value in non_evidence.values()
        ),
    }
    _assert_no_forbidden_output_keys(summary)
    return json.loads(json.dumps(summary, sort_keys=True))


def _assert_no_forbidden_output_keys(value: object) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if str(key) in FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS:
                raise SyntheticParserReaderSmokeError(
                    f"parser-reader smoke summary contains forbidden key {key!r}"
                )
            _assert_no_forbidden_output_keys(child)
    elif isinstance(value, list):
        for child in value:
            _assert_no_forbidden_output_keys(child)


__all__ = [
    "FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS",
    "SYNTHETIC_PARSER_READER_SMOKE_RECORD_TYPE",
    "SYNTHETIC_PARSER_READER_SMOKE_VERSION",
    "SyntheticParserReaderSmokeError",
    "collect_synthetic_parser_reader_smoke_errors",
    "parse_synthetic_parser_reader_smoke_mapping",
]
