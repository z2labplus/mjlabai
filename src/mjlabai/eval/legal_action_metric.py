"""Synthetic-only legal-action metric evaluator for P5 smoke fixtures."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from mjlabai.eval.offline_result import (
    OfflineEvaluationMetricValue,
    OfflineEvaluationResultEnvelope,
    OfflineEvaluationSafetyFlags,
    OfflineReproducibilityMetadata,
)


LEGAL_ACTION_METRIC_SOURCE_NOTE = (
    "P5 synthetic-only legal-action metric evaluator for project-authored "
    "fixtures; not model strength evidence and not a LuckyJ comparison."
)
LEGAL_ACTION_FIXTURE_SCHEMA_VERSION = "legal_action_fixture_v0.1"
CANONICAL_ACTION_SCHEMA_VERSION = "canonical_action_v0.1"
SYNTHETIC_LEGAL_ACTION_WARNINGS = (
    "synthetic only",
    "not Tenhou data",
    "not real haifu",
    "not model strength evidence",
    "not LuckyJ 10.68 comparison",
)


@dataclass(frozen=True)
class LegalActionMetricResult:
    fixture_id: str
    fixture_schema_version: str
    total_record_count: int
    evaluated_decision_count: int
    legal_action_count: int
    invalid_action_count: int
    missing_action_count: int
    parse_failure_count: int
    skipped_count: int
    legal_action_rate: float | None
    invalid_action_rate: float | None
    missing_action_rate: float | None
    parse_failure_rate: float | None
    source_note: str = LEGAL_ACTION_METRIC_SOURCE_NOTE

    def __post_init__(self) -> None:
        _validate_non_empty_string(self.fixture_id, "fixture_id")
        _validate_non_empty_string(
            self.fixture_schema_version,
            "fixture_schema_version",
        )
        for name in (
            "total_record_count",
            "evaluated_decision_count",
            "legal_action_count",
            "invalid_action_count",
            "missing_action_count",
            "parse_failure_count",
            "skipped_count",
        ):
            _validate_non_negative_int(getattr(self, name), name)
        expected = (
            self.legal_action_count
            + self.invalid_action_count
            + self.missing_action_count
            + self.parse_failure_count
        )
        if self.evaluated_decision_count != expected:
            raise ValueError(
                "evaluated_decision_count must equal legal_action_count + "
                "invalid_action_count + missing_action_count + "
                "parse_failure_count"
            )
        if self.total_record_count != self.evaluated_decision_count + self.skipped_count:
            raise ValueError(
                "total_record_count must equal evaluated_decision_count + skipped_count"
            )
        for name in (
            "legal_action_rate",
            "invalid_action_rate",
            "missing_action_rate",
            "parse_failure_rate",
        ):
            _validate_rate_or_none(getattr(self, name), name)
        if self.evaluated_decision_count == 0:
            if any(
                getattr(self, name) is not None
                for name in (
                    "legal_action_rate",
                    "invalid_action_rate",
                    "missing_action_rate",
                    "parse_failure_rate",
                )
            ):
                raise ValueError("rates must be None when evaluated_decision_count is 0")
        _validate_non_empty_string(self.source_note, "source_note")

    @property
    def invariant_holds(self) -> bool:
        return self.evaluated_decision_count == (
            self.legal_action_count
            + self.invalid_action_count
            + self.missing_action_count
            + self.parse_failure_count
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "fixture_id": self.fixture_id,
            "fixture_schema_version": self.fixture_schema_version,
            "total_record_count": self.total_record_count,
            "evaluated_decision_count": self.evaluated_decision_count,
            "legal_action_count": self.legal_action_count,
            "invalid_action_count": self.invalid_action_count,
            "missing_action_count": self.missing_action_count,
            "parse_failure_count": self.parse_failure_count,
            "skipped_count": self.skipped_count,
            "legal_action_rate": self.legal_action_rate,
            "invalid_action_rate": self.invalid_action_rate,
            "missing_action_rate": self.missing_action_rate,
            "parse_failure_rate": self.parse_failure_rate,
            "source_note": self.source_note,
        }


@dataclass(frozen=True)
class _StrictDahaiAction:
    actor: int
    action_type: str
    tile: str
    tsumogiri: bool


def evaluate_synthetic_legal_action_fixture(
    fixture: Mapping[str, object],
) -> LegalActionMetricResult:
    """Evaluate the project-authored synthetic legal-action fixture.

    This evaluator intentionally supports only strict `dahai` records in an
    in-memory fixture mapping. It does not read files, call external tools,
    canonicalize arbitrary action formats, or evaluate real model output.
    """

    if not isinstance(fixture, Mapping):
        raise ValueError("fixture must be a mapping")
    fixture_id = _validate_non_empty_string(fixture.get("fixture_id"), "fixture_id")
    fixture_schema_version = _validate_non_empty_string(
        fixture.get("schema_version"),
        "schema_version",
    )
    if fixture_schema_version != LEGAL_ACTION_FIXTURE_SCHEMA_VERSION:
        raise ValueError(
            f"schema_version must be {LEGAL_ACTION_FIXTURE_SCHEMA_VERSION!r}"
        )
    records = fixture.get("records")
    if not isinstance(records, list):
        raise ValueError("records must be a list")

    legal_action_count = 0
    invalid_action_count = 0
    missing_action_count = 0
    parse_failure_count = 0
    skipped_count = 0

    for record in records:
        if not isinstance(record, Mapping):
            raise ValueError("each record must be a mapping")
        _validate_record_boundary(record)
        legal_actions = record.get("legal_actions")
        if legal_actions is None or legal_actions == []:
            skipped_count += 1
            continue
        if not isinstance(legal_actions, list):
            raise ValueError("legal_actions must be a list when present")
        parsed_legal_actions = tuple(
            _parse_strict_dahai_action(action, "legal_actions")
            for action in legal_actions
        )

        proposed_action = record.get("proposed_action")
        if proposed_action is None:
            missing_action_count += 1
            continue

        try:
            parsed_proposed_action = _parse_strict_dahai_action(
                proposed_action,
                "proposed_action",
            )
        except ValueError:
            parse_failure_count += 1
            continue

        if any(
            _strict_dahai_actions_equal(parsed_proposed_action, legal_action)
            for legal_action in parsed_legal_actions
        ):
            legal_action_count += 1
        else:
            invalid_action_count += 1

    evaluated_decision_count = (
        legal_action_count
        + invalid_action_count
        + missing_action_count
        + parse_failure_count
    )
    rates = _make_rates(
        evaluated_decision_count=evaluated_decision_count,
        legal_action_count=legal_action_count,
        invalid_action_count=invalid_action_count,
        missing_action_count=missing_action_count,
        parse_failure_count=parse_failure_count,
    )
    return LegalActionMetricResult(
        fixture_id=fixture_id,
        fixture_schema_version=fixture_schema_version,
        total_record_count=len(records),
        evaluated_decision_count=evaluated_decision_count,
        legal_action_count=legal_action_count,
        invalid_action_count=invalid_action_count,
        missing_action_count=missing_action_count,
        parse_failure_count=parse_failure_count,
        skipped_count=skipped_count,
        legal_action_rate=rates["legal_action_rate"],
        invalid_action_rate=rates["invalid_action_rate"],
        missing_action_rate=rates["missing_action_rate"],
        parse_failure_rate=rates["parse_failure_rate"],
    )


def build_synthetic_legal_action_metric_envelope(
    result: LegalActionMetricResult,
    *,
    evaluation_id: str = "synthetic-legal-action-metric-smoke-001",
    model_or_tool_id: str = "synthetic-legal-action-fixture-evaluator",
    dataset_or_fixture_id: str = "tests/fixtures/eval/legal_action_metric_smoke.json",
    room: str | None = "phoenix",
    ruleset: str | None = "tenhou_four_player",
    code_commit: str | None = None,
    environment: str | None = "local-unit-test",
    evidence_refs: tuple[str, ...] = (
        "tests/eval/test_legal_action_metric.py",
        "tests/fixtures/eval/legal_action_metric_smoke.json",
        "docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md",
    ),
    warnings: tuple[str, ...] = SYNTHETIC_LEGAL_ACTION_WARNINGS,
) -> OfflineEvaluationResultEnvelope:
    """Wrap a synthetic legal-action metric result in the P5 envelope schema."""

    if not isinstance(result, LegalActionMetricResult):
        raise TypeError("result must be LegalActionMetricResult")
    return OfflineEvaluationResultEnvelope(
        evaluation_id=evaluation_id,
        evaluation_stage="P5",
        evaluation_type="legal_action_metric",
        model_or_tool_id=model_or_tool_id,
        dataset_or_fixture_id=dataset_or_fixture_id,
        room=room,
        ruleset=ruleset,
        metrics=_make_metric_values(result),
        sample_size=result.evaluated_decision_count,
        reproducibility=OfflineReproducibilityMetadata(
            code_commit=code_commit,
            fixture_id=result.fixture_id,
            environment=environment,
        ),
        safety=OfflineEvaluationSafetyFlags(),
        warnings=warnings,
        evidence_refs=evidence_refs,
        source_note=LEGAL_ACTION_METRIC_SOURCE_NOTE,
    )


def _make_metric_values(
    result: LegalActionMetricResult,
) -> tuple[OfflineEvaluationMetricValue, ...]:
    sample_size = result.evaluated_decision_count
    return (
        OfflineEvaluationMetricValue(
            metric_name="evaluated_decision_count",
            value=result.evaluated_decision_count,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="legal_action_count",
            value=result.legal_action_count,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="invalid_action_count",
            value=result.invalid_action_count,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="missing_action_count",
            value=result.missing_action_count,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="parse_failure_count",
            value=result.parse_failure_count,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="skipped_count",
            value=result.skipped_count,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="legal_action_rate",
            value=result.legal_action_rate,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="invalid_action_rate",
            value=result.invalid_action_rate,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="missing_action_rate",
            value=result.missing_action_rate,
            sample_size=sample_size,
        ),
        OfflineEvaluationMetricValue(
            metric_name="parse_failure_rate",
            value=result.parse_failure_rate,
            sample_size=sample_size,
        ),
    )


def _validate_record_boundary(record: Mapping[str, object]) -> None:
    _validate_non_empty_string(record.get("decision_id"), "decision_id")
    _validate_actor(record.get("actor"), "actor")
    _validate_non_empty_string(record.get("ruleset"), "ruleset")
    _validate_non_empty_string(record.get("room"), "room")
    matching_mode = _validate_non_empty_string(
        record.get("matching_mode"),
        "matching_mode",
    )
    if matching_mode != "strict":
        raise ValueError("only strict matching_mode is supported")


def _parse_strict_dahai_action(
    action: object,
    field_name: str,
) -> _StrictDahaiAction:
    if not isinstance(action, Mapping):
        raise ValueError(f"{field_name} must contain canonical action mappings")
    schema_version = _validate_non_empty_string(
        action.get("schema_version"),
        f"{field_name}.schema_version",
    )
    if schema_version != CANONICAL_ACTION_SCHEMA_VERSION:
        raise ValueError(
            f"{field_name}.schema_version must be "
            f"{CANONICAL_ACTION_SCHEMA_VERSION!r}"
        )
    action_type = _validate_non_empty_string(
        action.get("action_type"),
        f"{field_name}.action_type",
    )
    if action_type != "dahai":
        raise ValueError("only dahai actions are supported")
    actor = _validate_actor(action.get("actor"), f"{field_name}.actor")
    tile = _validate_non_empty_string(action.get("tile"), f"{field_name}.tile")
    tsumogiri = action.get("tsumogiri")
    if not isinstance(tsumogiri, bool):
        raise ValueError(
            f"{field_name}.tsumogiri must be a bool for current strict dahai scope"
        )
    return _StrictDahaiAction(
        actor=actor,
        action_type=action_type,
        tile=tile,
        tsumogiri=tsumogiri,
    )


def _strict_dahai_actions_equal(
    proposed_action: _StrictDahaiAction,
    legal_action: _StrictDahaiAction,
) -> bool:
    return proposed_action == legal_action


def _make_rates(
    *,
    evaluated_decision_count: int,
    legal_action_count: int,
    invalid_action_count: int,
    missing_action_count: int,
    parse_failure_count: int,
) -> dict[str, float | None]:
    if evaluated_decision_count == 0:
        return {
            "legal_action_rate": None,
            "invalid_action_rate": None,
            "missing_action_rate": None,
            "parse_failure_rate": None,
        }
    denominator = float(evaluated_decision_count)
    return {
        "legal_action_rate": legal_action_count / denominator,
        "invalid_action_rate": invalid_action_count / denominator,
        "missing_action_rate": missing_action_count / denominator,
        "parse_failure_rate": parse_failure_count / denominator,
    }


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


def _validate_rate_or_none(value: object, name: str) -> None:
    if value is None:
        return
    if not isinstance(value, float):
        raise ValueError(f"{name} must be a float or None")
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be in [0, 1]")
