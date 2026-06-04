"""P5 synthetic/local tiny benchmark harness for the project smoke fixture."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Mapping

from mjlabai.eval.offline_result import (
    OfflineEvaluationMetricValue,
    OfflineEvaluationResultEnvelope,
    OfflineEvaluationSafetyFlags,
    OfflineReproducibilityMetadata,
)


TINY_BENCHMARK_FIXTURE_SCHEMA_VERSION = "tiny_benchmark_harness_fixture_v0.1"
TINY_BENCHMARK_FIXTURE_TYPE = "tiny_benchmark_harness_schema_smoke"
CANONICAL_ACTION_SCHEMA_VERSION = "canonical_action_v0.1"
PROJECT_TINY_BENCHMARK_FIXTURE_ID = (
    "tests/fixtures/eval/tiny_benchmark_harness_smoke.json"
)
PROJECT_TINY_BENCHMARK_FIXTURE_PATH = (
    Path(__file__).resolve().parents[3] / PROJECT_TINY_BENCHMARK_FIXTURE_ID
)
TINY_BENCHMARK_HARNESS_SOURCE_NOTE = (
    "P5 synthetic/local tiny benchmark harness for the project-authored smoke "
    "fixture only; not model strength evidence, Tenhou evidence, stable-dan "
    "evidence or LuckyJ comparison."
)
TINY_BENCHMARK_HARNESS_WARNINGS = (
    "synthetic/local only",
    "not Tenhou data",
    "not real haifu",
    "not external log",
    "not platform data",
    "not model output",
    "not model strength evidence",
    "not LuckyJ 10.68 comparison",
    "not candidate promotion evidence",
    "not full action-space coverage",
)

_REQUIRED_DIAGNOSTIC_METRICS = {
    "legal_action_rate",
    "invalid_action_rate",
    "missing_action_rate",
    "parse_failure_rate",
    "evaluated_decision_count",
    "skipped_count",
    "latency_ms_mean",
    "latency_ms_p50",
    "latency_ms_p95",
    "latency_ms_max",
    "fixed_position_decision_count",
    "fixed_position_exact_match_rate",
}
_REQUIRED_LEGAL_ACTION_METRICS = {
    "legal_action_rate",
    "invalid_action_rate",
    "missing_action_rate",
    "parse_failure_rate",
    "evaluated_decision_count",
    "skipped_count",
}
_REQUIRED_LATENCY_METRICS = {
    "latency_ms_mean",
    "latency_ms_p50",
    "latency_ms_p95",
    "latency_ms_max",
}
_BANNED_LATENCY_FIELDS = {
    "measured_latency_ms",
    "actual_latency_ms",
    "benchmark_result",
    "real_tenhou_latency",
    "gpu_throughput",
    "training_throughput",
    "self_play_throughput",
    "league_throughput",
}
_REQUIRED_SAFETY_FLAGS = {
    "training_related",
    "self_play_related",
    "league_related",
    "tenhou_related",
    "platform_automation_related",
    "uses_real_platform_data",
    "uses_external_log",
    "uses_third_party_artifact",
}
_SOURCE_NOTE_TERMS = (
    "synthetic",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not platform data",
    "not model output",
    "not model strength",
    "not luckyj",
)
_WARNING_TERMS = (
    "synthetic",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not model strength",
    "not luckyj",
    "not candidate promotion",
    "not full action-space",
)
_RECORD_NOTE_TERMS = (
    "synthetic",
    "not tenhou",
    "not real haifu",
    "not external log",
    "not model strength",
    "not luckyj",
)


@dataclass(frozen=True)
class TinyBenchmarkHarnessResult:
    fixture_id: str
    fixture_schema_version: str
    evaluation_stage: str
    fixture_type: str
    smoke_success: bool
    diagnostic_metric_names: tuple[str, ...]
    legal_action_metric_names: tuple[str, ...]
    latency_metric_names: tuple[str, ...]
    fixed_position_metric_names: tuple[str, ...]
    fixed_position_record_count: int
    warnings: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    source_note: str = TINY_BENCHMARK_HARNESS_SOURCE_NOTE

    def __post_init__(self) -> None:
        _validate_non_empty_string(self.fixture_id, "fixture_id")
        _validate_non_empty_string(
            self.fixture_schema_version,
            "fixture_schema_version",
        )
        if self.fixture_schema_version != TINY_BENCHMARK_FIXTURE_SCHEMA_VERSION:
            raise ValueError(
                "fixture_schema_version must be "
                f"{TINY_BENCHMARK_FIXTURE_SCHEMA_VERSION!r}"
            )
        if self.evaluation_stage != "P5":
            raise ValueError("evaluation_stage must be 'P5'")
        if self.fixture_type != TINY_BENCHMARK_FIXTURE_TYPE:
            raise ValueError(
                f"fixture_type must be {TINY_BENCHMARK_FIXTURE_TYPE!r}"
            )
        if not isinstance(self.smoke_success, bool):
            raise ValueError("smoke_success must be a bool")
        _validate_string_tuple(
            self.diagnostic_metric_names,
            "diagnostic_metric_names",
        )
        _validate_string_tuple(
            self.legal_action_metric_names,
            "legal_action_metric_names",
        )
        _validate_string_tuple(self.latency_metric_names, "latency_metric_names")
        _validate_string_tuple(
            self.fixed_position_metric_names,
            "fixed_position_metric_names",
        )
        _validate_non_negative_int(
            self.fixed_position_record_count,
            "fixed_position_record_count",
        )
        _validate_string_tuple(self.warnings, "warnings")
        _validate_string_tuple(self.evidence_refs, "evidence_refs")
        _validate_non_empty_string(self.source_note, "source_note")

    def to_dict(self) -> dict[str, object]:
        return {
            "fixture_id": self.fixture_id,
            "fixture_schema_version": self.fixture_schema_version,
            "evaluation_stage": self.evaluation_stage,
            "fixture_type": self.fixture_type,
            "smoke_success": self.smoke_success,
            "diagnostic_metric_names": list(self.diagnostic_metric_names),
            "legal_action_metric_names": list(self.legal_action_metric_names),
            "latency_metric_names": list(self.latency_metric_names),
            "fixed_position_metric_names": list(self.fixed_position_metric_names),
            "fixed_position_record_count": self.fixed_position_record_count,
            "warnings": list(self.warnings),
            "evidence_refs": list(self.evidence_refs),
            "source_note": self.source_note,
        }


def load_project_tiny_benchmark_harness_fixture() -> dict[str, object]:
    """Load the single project-authored synthetic tiny benchmark fixture."""

    with PROJECT_TINY_BENCHMARK_FIXTURE_PATH.open(encoding="utf-8") as fixture_file:
        fixture = json.load(fixture_file)
    if not isinstance(fixture, dict):
        raise ValueError("project tiny benchmark fixture must be a JSON object")
    return fixture


def evaluate_tiny_benchmark_harness_fixture(
    fixture: Mapping[str, object],
) -> TinyBenchmarkHarnessResult:
    """Validate and summarize a synthetic/local tiny benchmark fixture mapping.

    This is a schema-safe smoke harness. It does not measure latency, calculate
    legal-action rates, calculate fixed-position exact-match, call models, call
    external tools, read arbitrary paths, or ingest real data.
    """

    if not isinstance(fixture, Mapping):
        raise ValueError("fixture must be a mapping")

    fixture_id = _validate_non_empty_string(fixture.get("fixture_id"), "fixture_id")
    schema_version = _validate_non_empty_string(
        fixture.get("schema_version"),
        "schema_version",
    )
    if schema_version != TINY_BENCHMARK_FIXTURE_SCHEMA_VERSION:
        raise ValueError(
            f"schema_version must be {TINY_BENCHMARK_FIXTURE_SCHEMA_VERSION!r}"
        )
    evaluation_stage = _validate_non_empty_string(
        fixture.get("evaluation_stage"),
        "evaluation_stage",
    )
    if evaluation_stage != "P5":
        raise ValueError("evaluation_stage must be 'P5'")
    fixture_type = _validate_non_empty_string(
        fixture.get("fixture_type"),
        "fixture_type",
    )
    if fixture_type != TINY_BENCHMARK_FIXTURE_TYPE:
        raise ValueError(f"fixture_type must be {TINY_BENCHMARK_FIXTURE_TYPE!r}")
    _validate_guardrail_text(fixture.get("source_note"), "source_note")
    _validate_warnings(fixture.get("warnings"))
    _validate_safety_flags(fixture.get("intended_safety_flags"))

    diagnostic_metric_names = _validate_metric_names(
        fixture.get("diagnostic_metric_names"),
        "diagnostic_metric_names",
        _REQUIRED_DIAGNOSTIC_METRICS,
    )
    legal_action_section = _validate_legal_action_diagnostics(
        fixture.get("legal_action_diagnostics"),
    )
    latency_section = _validate_latency_diagnostics(
        fixture.get("latency_diagnostics"),
    )
    fixed_position_section = _validate_fixed_position_diagnostics(
        fixture.get("fixed_position_decision_diagnostics"),
    )
    evidence_refs = _validate_string_tuple(
        tuple(fixture.get("evidence_refs", ())),
        "evidence_refs",
    )

    return TinyBenchmarkHarnessResult(
        fixture_id=fixture_id,
        fixture_schema_version=schema_version,
        evaluation_stage=evaluation_stage,
        fixture_type=fixture_type,
        smoke_success=True,
        diagnostic_metric_names=diagnostic_metric_names,
        legal_action_metric_names=tuple(legal_action_section["metric_names"]),
        latency_metric_names=tuple(latency_section["metric_names"]),
        fixed_position_metric_names=tuple(
            fixed_position_section["fixed_position_metric_names"]
        ),
        fixed_position_record_count=fixed_position_section[
            "fixed_position_record_count"
        ],
        warnings=TINY_BENCHMARK_HARNESS_WARNINGS,
        evidence_refs=evidence_refs,
    )


def run_project_tiny_benchmark_harness() -> TinyBenchmarkHarnessResult:
    """Run the P5 tiny benchmark harness against the fixed project fixture."""

    return evaluate_tiny_benchmark_harness_fixture(
        load_project_tiny_benchmark_harness_fixture()
    )


def build_tiny_benchmark_harness_envelope(
    result: TinyBenchmarkHarnessResult,
    *,
    evaluation_id: str = "synthetic-tiny-benchmark-harness-smoke-001",
    model_or_tool_id: str = "synthetic-tiny-benchmark-harness",
    dataset_or_fixture_id: str = PROJECT_TINY_BENCHMARK_FIXTURE_ID,
    code_commit: str | None = None,
    environment: str | None = "local-unit-test",
) -> OfflineEvaluationResultEnvelope:
    """Wrap the synthetic tiny benchmark harness smoke result in the envelope."""

    if not isinstance(result, TinyBenchmarkHarnessResult):
        raise TypeError("result must be TinyBenchmarkHarnessResult")
    return OfflineEvaluationResultEnvelope(
        evaluation_id=evaluation_id,
        evaluation_stage="P5",
        evaluation_type="tiny_benchmark_harness",
        model_or_tool_id=model_or_tool_id,
        dataset_or_fixture_id=dataset_or_fixture_id,
        metrics=(
            OfflineEvaluationMetricValue(
                metric_name="wrapper_smoke_success",
                value=result.smoke_success,
                sample_size=result.fixed_position_record_count,
            ),
        ),
        sample_size=result.fixed_position_record_count,
        reproducibility=OfflineReproducibilityMetadata(
            code_commit=code_commit,
            fixture_id=result.fixture_id,
            environment=environment,
        ),
        safety=OfflineEvaluationSafetyFlags(),
        warnings=result.warnings,
        evidence_refs=result.evidence_refs
        + (
            "tests/eval/test_tiny_benchmark_harness.py",
            "docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md",
            "docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md",
        ),
        source_note=TINY_BENCHMARK_HARNESS_SOURCE_NOTE,
    )


def _validate_legal_action_diagnostics(section: object) -> dict[str, object]:
    if not isinstance(section, Mapping):
        raise ValueError("legal_action_diagnostics must be a mapping")
    if section.get("source_kind") != "synthetic_fixture_reference":
        raise ValueError(
            "legal_action_diagnostics.source_kind must be "
            "'synthetic_fixture_reference'"
        )
    if section.get("fixture_path") != "tests/fixtures/eval/legal_action_metric_smoke.json":
        raise ValueError(
            "legal_action_diagnostics.fixture_path must reference the project "
            "synthetic legal-action fixture"
        )
    allowed_scope = _validate_string_tuple(
        tuple(section.get("allowed_scope", ())),
        "legal_action_diagnostics.allowed_scope",
    )
    for expected_scope in (
        "project-authored synthetic/local only",
        "dahai only",
        "strict matching only",
    ):
        if expected_scope not in allowed_scope:
            raise ValueError(
                "legal_action_diagnostics.allowed_scope missing "
                f"{expected_scope!r}"
            )
    metric_names = _validate_metric_names(
        section.get("metric_names"),
        "legal_action_diagnostics.metric_names",
        _REQUIRED_LEGAL_ACTION_METRICS,
    )
    interpretation = _validate_string_tuple(
        tuple(section.get("interpretation", ())),
        "legal_action_diagnostics.interpretation",
    )
    interpretation_text = " ".join(interpretation).lower()
    for term in ("legality diagnostic", "not strength", "not luckyj"):
        if term not in interpretation_text:
            raise ValueError(
                "legal_action_diagnostics.interpretation must include "
                f"{term!r}"
            )
    return {"metric_names": metric_names}


def _validate_latency_diagnostics(section: object) -> dict[str, object]:
    if not isinstance(section, Mapping):
        raise ValueError("latency_diagnostics must be a mapping")
    if _BANNED_LATENCY_FIELDS.intersection(section.keys()):
        raise ValueError("latency_diagnostics must not contain measured results")
    if section.get("source_kind") != "synthetic_latency_plan":
        raise ValueError("latency_diagnostics.source_kind must be a plan")
    _validate_non_empty_string(
        section.get("timing_method"),
        "latency_diagnostics.timing_method",
    )
    _validate_positive_int(section.get("repetitions"), "latency_diagnostics.repetitions")
    _validate_positive_int(section.get("sample_count"), "latency_diagnostics.sample_count")
    if section.get("target_kind") != "synthetic_local_evaluation_path_future_placeholder":
        raise ValueError("latency_diagnostics.target_kind must remain synthetic/local")
    metric_names = _validate_metric_names(
        section.get("metric_names"),
        "latency_diagnostics.metric_names",
        _REQUIRED_LATENCY_METRICS,
    )
    required_repro = set(
        _validate_string_tuple(
            tuple(section.get("required_reproducibility_fields", ())),
            "latency_diagnostics.required_reproducibility_fields",
        )
    )
    if not {
        "environment",
        "command_or_test_path",
        "sample_count",
        "timing_method",
        "repetitions",
    }.issubset(required_repro):
        raise ValueError("latency_diagnostics missing reproducibility fields")
    interpretation = _validate_string_tuple(
        tuple(section.get("interpretation", ())),
        "latency_diagnostics.interpretation",
    )
    interpretation_text = " ".join(interpretation).lower()
    for term in (
        "engineering smoke diagnostic",
        "not model strength",
        "not training throughput",
        "not self-play throughput",
        "not league throughput",
        "not gpu benchmark",
    ):
        if term not in interpretation_text:
            raise ValueError(
                "latency_diagnostics.interpretation must include " f"{term!r}"
            )
    return {"metric_names": metric_names}


def _validate_fixed_position_diagnostics(section: object) -> dict[str, object]:
    if not isinstance(section, Mapping):
        raise ValueError("fixed_position_decision_diagnostics must be a mapping")
    if section.get("source_kind") != "project_authored_synthetic_fixed_position_records":
        raise ValueError("fixed_position source_kind must remain project-authored")
    if section.get("matching_mode") != "strict":
        raise ValueError("fixed_position matching_mode must be strict")
    if section.get("action_scope") != "dahai":
        raise ValueError("fixed_position action_scope must be dahai")
    records = section.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("fixed_position records must be a non-empty list")

    fixed_position_metric_names: set[str] = set()
    for record in records:
        metric_names = _validate_fixed_position_record(record)
        fixed_position_metric_names.update(metric_names)
    if not {
        "fixed_position_decision_count",
        "fixed_position_exact_match_rate",
    }.issubset(fixed_position_metric_names):
        raise ValueError("fixed_position records missing required metric names")
    return {
        "fixed_position_record_count": len(records),
        "fixed_position_metric_names": tuple(sorted(fixed_position_metric_names)),
    }


def _validate_fixed_position_record(record: object) -> tuple[str, ...]:
    if not isinstance(record, Mapping):
        raise ValueError("fixed_position records must be mappings")
    _validate_non_empty_string(record.get("record_id"), "record_id")
    _validate_guardrail_text(
        record.get("source_note"),
        "record.source_note",
        required_terms=_RECORD_NOTE_TERMS,
    )
    _validate_non_empty_string(
        record.get("synthetic_position_id"),
        "synthetic_position_id",
    )
    decision_context = record.get("decision_context")
    if not isinstance(decision_context, Mapping):
        raise ValueError("decision_context must be a mapping")
    if decision_context.get("no_real_haifu") is not True:
        raise ValueError("decision_context.no_real_haifu must be true")
    _validate_actor(decision_context.get("actor"), "decision_context.actor")
    _validate_non_negative_int(
        decision_context.get("turn_index"),
        "decision_context.turn_index",
    )
    _validate_non_empty_string(
        decision_context.get("observation_stub"),
        "decision_context.observation_stub",
    )

    candidate_actions = record.get("candidate_actions")
    if not isinstance(candidate_actions, list) or not candidate_actions:
        raise ValueError("candidate_actions must be a non-empty list")
    for action in candidate_actions:
        _validate_canonical_dahai_action(action, "candidate_actions")
    _validate_canonical_dahai_action(record.get("expected_action"), "expected_action")
    metric_names = _validate_string_tuple(
        tuple(record.get("metric_names", ())),
        "fixed_position.metric_names",
    )
    interpretation = _validate_string_tuple(
        tuple(record.get("interpretation", ())),
        "fixed_position.interpretation",
    )
    interpretation_text = " ".join(interpretation).lower()
    for term in (
        "future diagnostic expectation only",
        "not supervised label",
        "not policy-quality evidence",
        "not strength evidence",
    ):
        if term not in interpretation_text:
            raise ValueError("fixed_position interpretation missing " f"{term!r}")
    return metric_names


def _validate_canonical_dahai_action(action: object, field_name: str) -> None:
    if not isinstance(action, Mapping):
        raise ValueError(f"{field_name} must contain mappings")
    if action.get("schema_version") != CANONICAL_ACTION_SCHEMA_VERSION:
        raise ValueError(
            f"{field_name}.schema_version must be "
            f"{CANONICAL_ACTION_SCHEMA_VERSION!r}"
        )
    _validate_actor(action.get("actor"), f"{field_name}.actor")
    if action.get("action_type") != "dahai":
        raise ValueError(f"{field_name}.action_type must be dahai")
    _validate_non_empty_string(action.get("tile"), f"{field_name}.tile")
    if not isinstance(action.get("tsumogiri"), bool):
        raise ValueError(f"{field_name}.tsumogiri must be bool")


def _validate_safety_flags(flags: object) -> None:
    if not isinstance(flags, Mapping):
        raise ValueError("intended_safety_flags must be a mapping")
    if set(flags.keys()) != _REQUIRED_SAFETY_FLAGS:
        raise ValueError("intended_safety_flags must contain the required keys")
    for name, value in flags.items():
        if value is not False:
            raise ValueError(f"intended_safety_flags.{name} must be false")


def _validate_warnings(warnings: object) -> None:
    if not isinstance(warnings, list):
        raise ValueError("warnings must be a list")
    warning_text = " ".join(str(warning) for warning in warnings).lower()
    for term in _WARNING_TERMS:
        if term not in warning_text:
            raise ValueError(f"warnings must include {term!r}")


def _validate_guardrail_text(
    value: object,
    name: str,
    *,
    required_terms: tuple[str, ...] = _SOURCE_NOTE_TERMS,
) -> str:
    text = _validate_non_empty_string(value, name)
    lowered = text.lower()
    for term in required_terms:
        if term not in lowered:
            raise ValueError(f"{name} must include {term!r}")
    return text


def _validate_metric_names(
    value: object,
    name: str,
    required_metrics: set[str],
) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    metric_names = _validate_string_tuple(tuple(value), name)
    if not required_metrics.issubset(set(metric_names)):
        raise ValueError(f"{name} missing required metric names")
    return metric_names


def _validate_string_tuple(values: tuple[object, ...], name: str) -> tuple[str, ...]:
    strings: list[str] = []
    for value in values:
        strings.append(_validate_non_empty_string(value, name))
    return tuple(strings)


def _validate_non_empty_string(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value


def _validate_actor(value: object, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{name} must be an integer actor")
    if value not in {0, 1, 2, 3}:
        raise ValueError(f"{name} must be one of 0, 1, 2, 3")
    return value


def _validate_non_negative_int(value: object, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be >= 0")
    return value


def _validate_positive_int(value: object, name: str) -> int:
    integer = _validate_non_negative_int(value, name)
    if integer <= 0:
        raise ValueError(f"{name} must be > 0")
    return integer
