"""Minimal P7 synthetic/local parser-reader smoke extension helpers.

This module accepts only already-loaded project-authored synthetic/local
parser-reader smoke records. It does not read files, ingest data, parse real
logs, extract features, generate labels, build datasets, call models, evaluate
models, or train.
"""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from os import PathLike
from typing import Any

from mjlabai.supervised.synthetic_parser_reader_smoke import (
    FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS,
    collect_synthetic_parser_reader_smoke_errors,
    parse_synthetic_parser_reader_smoke_mapping,
)


SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_RECORD_TYPE = (
    "p7_synthetic_local_parser_reader_smoke_extension_v0.1"
)
SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_VERSION = "v0.1"


class SyntheticParserReaderSmokeExtensionError(ValueError):
    """Raised when a synthetic/local parser-reader smoke extension is invalid."""


def collect_synthetic_parser_reader_smoke_extension_errors(
    records: Sequence[Mapping[str, Any]],
) -> list[str]:
    """Return validation errors for an in-memory synthetic/local record sequence.

    The extension deliberately rejects path-like inputs. It is a tiny
    in-memory manifest builder around the existing parser-reader smoke helper,
    not a file reader, source ingestion interface, feature extractor, label
    generator, dataset builder, model-output path, evaluator, or trainer.
    """

    if isinstance(records, str):
        return ["records must be an in-memory sequence; path strings are not accepted"]
    if isinstance(records, (bytes, bytearray, PathLike)):
        return [
            "records must be an in-memory sequence; path-like inputs are not accepted"
        ]
    if isinstance(records, Mapping):
        return ["records must be a sequence of in-memory mappings, not a mapping"]
    if not isinstance(records, Sequence):
        return ["records must be an in-memory sequence of mappings"]
    if not records:
        return ["records must be a non-empty sequence"]

    errors: list[str] = []
    for index, record in enumerate(records):
        if isinstance(record, str):
            errors.append(
                f"records[{index}] must be an in-memory mapping; "
                "path strings are not accepted"
            )
            continue
        if isinstance(record, (bytes, bytearray, PathLike)):
            errors.append(
                f"records[{index}] must be an in-memory mapping; "
                "path-like inputs are not accepted"
            )
            continue
        if not isinstance(record, Mapping):
            errors.append(f"records[{index}] must be an in-memory mapping")
            continue

        for error in collect_synthetic_parser_reader_smoke_errors(record):
            errors.append(f"records[{index}].{error}")
    return errors


def build_synthetic_parser_reader_smoke_extension_manifest(
    records: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Build a JSON-safe manifest summary for synthetic/local smoke records.

    The manifest aggregates guardrail summaries only. It intentionally excludes
    feature tensors, labels, targets, supervised examples, datasets, splits,
    model input, model output, evaluation results, and model-strength fields.
    """

    errors = collect_synthetic_parser_reader_smoke_extension_errors(records)
    if errors:
        raise SyntheticParserReaderSmokeExtensionError("; ".join(errors))

    summaries = [
        parse_synthetic_parser_reader_smoke_mapping(record) for record in records
    ]
    manifest = {
        "record_type": SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_RECORD_TYPE,
        "extension_version": SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_VERSION,
        "record_count": len(summaries),
        "input_kind": "in_memory_sequence",
        "output_kind": "json_safe_manifest_summary",
        "all_project_authored": all(
            summary["project_authored"] is True for summary in summaries
        ),
        "all_synthetic": all(summary["synthetic"] is True for summary in summaries),
        "all_local_only": all(summary["local_only"] is True for summary in summaries),
        "any_real_data": any(
            summary["uses_real_data"] is True for summary in summaries
        ),
        "any_model_output": any(
            summary["has_model_output"] is True for summary in summaries
        ),
        "any_training_use_approved": any(
            summary["training_use_approved"] is True for summary in summaries
        ),
        "any_self_play": any(
            summary["uses_self_play"] is True for summary in summaries
        ),
        "any_league_output": any(
            summary["uses_league_output"] is True for summary in summaries
        ),
        "all_public_information_only": all(
            summary["public_information_only"] is True for summary in summaries
        ),
        "all_decision_time_only": all(
            summary["decision_time_only"] is True for summary in summaries
        ),
        "all_hidden_information_absent": all(
            summary["hidden_information_absent"] is True for summary in summaries
        ),
        "all_future_information_absent": all(
            summary["future_information_absent"] is True for summary in summaries
        ),
        "total_feature_family_count": sum(
            int(summary["feature_family_count"]) for summary in summaries
        ),
        "total_label_family_count": sum(
            int(summary["label_family_count"]) for summary in summaries
        ),
        "total_evidence_warning_count": sum(
            int(summary["evidence_warning_count"]) for summary in summaries
        ),
        "non_evidence_guardrails_all_false": all(
            summary["non_evidence_guardrails_all_false"] is True
            for summary in summaries
        ),
        "input_fixture_ids": [
            str(summary["input_fixture_id"]) for summary in summaries
        ],
        "input_schema_versions": [
            str(summary["input_schema_version"]) for summary in summaries
        ],
    }
    _assert_no_forbidden_output_keys(manifest)
    return json.loads(json.dumps(manifest, sort_keys=True))


def _assert_no_forbidden_output_keys(value: object) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if str(key) in FORBIDDEN_PARSER_READER_SMOKE_OUTPUT_KEYS:
                raise SyntheticParserReaderSmokeExtensionError(
                    "parser-reader smoke extension manifest contains forbidden "
                    f"key {key!r}"
                )
            _assert_no_forbidden_output_keys(child)
    elif isinstance(value, list):
        for child in value:
            _assert_no_forbidden_output_keys(child)


__all__ = [
    "SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_RECORD_TYPE",
    "SYNTHETIC_PARSER_READER_SMOKE_EXTENSION_VERSION",
    "SyntheticParserReaderSmokeExtensionError",
    "build_synthetic_parser_reader_smoke_extension_manifest",
    "collect_synthetic_parser_reader_smoke_extension_errors",
]
