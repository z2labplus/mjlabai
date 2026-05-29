"""Offline evaluation metric registry and result envelope schema."""

from __future__ import annotations

from dataclasses import dataclass
import math
from types import MappingProxyType
from typing import Any, Mapping


OFFLINE_RESULT_SCHEMA_VERSION = "offline_evaluation_result_v0.1"
OFFLINE_RESULT_SOURCE_NOTE = (
    "P5 offline evaluation result envelope schema; records results produced "
    "elsewhere and does not execute training, self-play, league, Tenhou or "
    "platform automation."
)
METRIC_REGISTRY_SOURCE_NOTE = (
    "P5 offline evaluation metric registry; some metrics are placeholders for "
    "future evaluators and are not implemented calculators in this module."
)
COMMAND_SUMMARY_MAX_CHARS = 2000


@dataclass(frozen=True)
class EvaluationMetricDefinition:
    metric_name: str
    display_name: str
    metric_unit: str
    higher_is_better: bool | None
    description: str
    source_note: str = METRIC_REGISTRY_SOURCE_NOTE

    def __post_init__(self) -> None:
        _validate_non_empty_string(self.metric_name, "metric_name")
        _validate_non_empty_string(self.display_name, "display_name")
        _validate_non_empty_string(self.metric_unit, "metric_unit")
        if self.higher_is_better is not None and not isinstance(
            self.higher_is_better,
            bool,
        ):
            raise ValueError("higher_is_better must be bool or None")
        _validate_non_empty_string(self.description, "description")
        _validate_non_empty_string(self.source_note, "source_note")

    def to_dict(self) -> dict[str, object]:
        return {
            "metric_name": self.metric_name,
            "display_name": self.display_name,
            "metric_unit": self.metric_unit,
            "higher_is_better": self.higher_is_better,
            "description": self.description,
            "source_note": self.source_note,
        }


@dataclass(frozen=True)
class OfflineEvaluationMetricValue:
    metric_name: str
    value: int | float | str | bool | None
    metric_unit: str = ""
    higher_is_better: bool | None = None
    sample_size: int | None = None
    source_note: str = OFFLINE_RESULT_SOURCE_NOTE

    def __post_init__(self) -> None:
        metric_name = _validate_non_empty_string(self.metric_name, "metric_name")
        if not _is_supported_metric_value(self.value):
            raise ValueError(
                "value must be int, float, str, bool or None; complex objects "
                "are not supported"
            )
        definition = _METRIC_DEFINITIONS_BY_NAME.get(metric_name)
        if definition is not None:
            if not self.metric_unit:
                object.__setattr__(self, "metric_unit", definition.metric_unit)
            if self.higher_is_better is None:
                object.__setattr__(
                    self,
                    "higher_is_better",
                    definition.higher_is_better,
                )
        _validate_non_empty_string(self.metric_unit, "metric_unit")
        if self.higher_is_better is not None and not isinstance(
            self.higher_is_better,
            bool,
        ):
            raise ValueError("higher_is_better must be bool or None")
        if self.sample_size is not None:
            _validate_non_negative_int(self.sample_size, "sample_size")
        _validate_non_empty_string(self.source_note, "source_note")

    def to_dict(self) -> dict[str, object]:
        return {
            "metric_name": self.metric_name,
            "value": self.value,
            "metric_unit": self.metric_unit,
            "higher_is_better": self.higher_is_better,
            "sample_size": self.sample_size,
            "source_note": self.source_note,
        }


@dataclass(frozen=True)
class OfflineConfidenceInterval:
    lower_bound: float
    upper_bound: float
    confidence_level: float
    method: str

    def __post_init__(self) -> None:
        lower = _validate_finite_number(self.lower_bound, "lower_bound")
        upper = _validate_finite_number(self.upper_bound, "upper_bound")
        if lower > upper:
            raise ValueError("lower_bound must be <= upper_bound")
        confidence_level = _validate_finite_number(
            self.confidence_level,
            "confidence_level",
        )
        if not 0 < confidence_level < 1:
            raise ValueError("confidence_level must be in (0, 1)")
        _validate_non_empty_string(self.method, "method")

    def to_dict(self) -> dict[str, object]:
        return {
            "lower_bound": self.lower_bound,
            "upper_bound": self.upper_bound,
            "confidence_level": self.confidence_level,
            "method": self.method,
        }


@dataclass(frozen=True)
class OfflineCommandStatus:
    command_name: str
    exit_code: int | None
    success: bool
    stdout_summary: str | None = None
    stderr_summary: str | None = None

    def __post_init__(self) -> None:
        _validate_non_empty_string(self.command_name, "command_name")
        if self.exit_code is not None:
            _validate_int(self.exit_code, "exit_code")
        if not isinstance(self.success, bool):
            raise ValueError("success must be a bool")
        _validate_optional_bounded_string(
            self.stdout_summary,
            "stdout_summary",
        )
        _validate_optional_bounded_string(
            self.stderr_summary,
            "stderr_summary",
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "command_name": self.command_name,
            "exit_code": self.exit_code,
            "success": self.success,
            "stdout_summary": self.stdout_summary,
            "stderr_summary": self.stderr_summary,
        }


@dataclass(frozen=True)
class OfflineReproducibilityMetadata:
    code_commit: str | None = None
    external_repo: str | None = None
    external_commit: str | None = None
    fixture_id: str | None = None
    seed: int | None = None
    environment: str | None = None
    source_note: str = OFFLINE_RESULT_SOURCE_NOTE

    def __post_init__(self) -> None:
        for name in (
            "code_commit",
            "external_repo",
            "external_commit",
            "fixture_id",
            "environment",
        ):
            _validate_optional_non_empty_string(getattr(self, name), name)
        if self.seed is not None:
            _validate_int(self.seed, "seed")
        _validate_non_empty_string(self.source_note, "source_note")

    def to_dict(self) -> dict[str, object]:
        return {
            "code_commit": self.code_commit,
            "external_repo": self.external_repo,
            "external_commit": self.external_commit,
            "fixture_id": self.fixture_id,
            "seed": self.seed,
            "environment": self.environment,
            "source_note": self.source_note,
        }


@dataclass(frozen=True)
class OfflineEvaluationSafetyFlags:
    training_related: bool = False
    self_play_related: bool = False
    league_related: bool = False
    tenhou_related: bool = False
    platform_automation_related: bool = False
    uses_real_platform_data: bool = False
    uses_external_log: bool = False
    uses_third_party_artifact: bool = False

    def __post_init__(self) -> None:
        for name, value in self.to_dict().items():
            if not isinstance(value, bool):
                raise ValueError(f"{name} must be a bool")

    def high_risk_flag_names(self) -> tuple[str, ...]:
        return tuple(name for name, value in self.to_dict().items() if value)

    def to_dict(self) -> dict[str, bool]:
        return {
            "training_related": self.training_related,
            "self_play_related": self.self_play_related,
            "league_related": self.league_related,
            "tenhou_related": self.tenhou_related,
            "platform_automation_related": self.platform_automation_related,
            "uses_real_platform_data": self.uses_real_platform_data,
            "uses_external_log": self.uses_external_log,
            "uses_third_party_artifact": self.uses_third_party_artifact,
        }


@dataclass(frozen=True)
class OfflineEvaluationResultEnvelope:
    evaluation_id: str
    evaluation_stage: str
    evaluation_type: str
    model_or_tool_id: str
    dataset_or_fixture_id: str
    metrics: tuple[OfflineEvaluationMetricValue, ...]
    reproducibility: OfflineReproducibilityMetadata
    safety: OfflineEvaluationSafetyFlags
    schema_version: str = OFFLINE_RESULT_SCHEMA_VERSION
    room: str | None = None
    ruleset: str | None = None
    sample_size: int | None = None
    confidence_interval: OfflineConfidenceInterval | None = None
    command_status: OfflineCommandStatus | None = None
    latency_ms: float | None = None
    warnings: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()
    source_note: str = OFFLINE_RESULT_SOURCE_NOTE

    def __post_init__(self) -> None:
        _validate_non_empty_string(self.schema_version, "schema_version")
        _validate_non_empty_string(self.evaluation_id, "evaluation_id")
        _validate_non_empty_string(self.evaluation_stage, "evaluation_stage")
        _validate_non_empty_string(self.evaluation_type, "evaluation_type")
        _validate_non_empty_string(self.model_or_tool_id, "model_or_tool_id")
        _validate_non_empty_string(
            self.dataset_or_fixture_id,
            "dataset_or_fixture_id",
        )
        if not isinstance(self.metrics, tuple):
            object.__setattr__(self, "metrics", tuple(self.metrics))
        if len(self.metrics) == 0:
            raise ValueError("metrics must contain at least one metric value")
        for metric in self.metrics:
            if not isinstance(metric, OfflineEvaluationMetricValue):
                raise TypeError(
                    "metrics must contain OfflineEvaluationMetricValue objects"
                )
        if not isinstance(self.reproducibility, OfflineReproducibilityMetadata):
            raise TypeError(
                "reproducibility must be OfflineReproducibilityMetadata"
            )
        if not isinstance(self.safety, OfflineEvaluationSafetyFlags):
            raise TypeError("safety must be OfflineEvaluationSafetyFlags")
        _validate_optional_non_empty_string(self.room, "room")
        _validate_optional_non_empty_string(self.ruleset, "ruleset")
        if self.sample_size is not None:
            _validate_non_negative_int(self.sample_size, "sample_size")
        if self.confidence_interval is not None and not isinstance(
            self.confidence_interval,
            OfflineConfidenceInterval,
        ):
            raise TypeError("confidence_interval must be OfflineConfidenceInterval")
        if self.command_status is not None and not isinstance(
            self.command_status,
            OfflineCommandStatus,
        ):
            raise TypeError("command_status must be OfflineCommandStatus")
        if self.latency_ms is not None:
            latency_ms = _validate_finite_number(self.latency_ms, "latency_ms")
            if latency_ms < 0:
                raise ValueError("latency_ms must be >= 0")
        warnings = _validate_string_tuple(self.warnings, "warnings")
        high_risk_flags = self.safety.high_risk_flag_names()
        if high_risk_flags:
            warnings = warnings + tuple(
                f"high-risk safety flag set: {name}" for name in high_risk_flags
            )
            object.__setattr__(self, "warnings", warnings)
        object.__setattr__(
            self,
            "evidence_refs",
            _validate_string_tuple(self.evidence_refs, "evidence_refs"),
        )
        _validate_non_empty_string(self.source_note, "source_note")

    def to_dict(self) -> dict[str, object]:
        return {
            "schema_version": self.schema_version,
            "evaluation_id": self.evaluation_id,
            "evaluation_stage": self.evaluation_stage,
            "evaluation_type": self.evaluation_type,
            "model_or_tool_id": self.model_or_tool_id,
            "dataset_or_fixture_id": self.dataset_or_fixture_id,
            "room": self.room,
            "ruleset": self.ruleset,
            "metrics": [metric.to_dict() for metric in self.metrics],
            "sample_size": self.sample_size,
            "confidence_interval": (
                self.confidence_interval.to_dict()
                if self.confidence_interval is not None
                else None
            ),
            "command_status": (
                self.command_status.to_dict()
                if self.command_status is not None
                else None
            ),
            "latency_ms": self.latency_ms,
            "reproducibility": self.reproducibility.to_dict(),
            "safety": self.safety.to_dict(),
            "warnings": list(self.warnings),
            "evidence_refs": list(self.evidence_refs),
            "source_note": self.source_note,
        }


def _validate_non_empty_string(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value


def _validate_optional_non_empty_string(value: str | None, name: str) -> None:
    if value is not None:
        _validate_non_empty_string(value, name)


def _validate_int(value: int, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{name} must be an integer")
    return value


def _validate_non_negative_int(value: int, name: str) -> int:
    integer = _validate_int(value, name)
    if integer < 0:
        raise ValueError(f"{name} must be >= 0")
    return integer


def _validate_finite_number(value: float, name: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{name} must be a finite number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} must be a finite number")
    return number


def _validate_optional_bounded_string(value: str | None, name: str) -> None:
    if value is None:
        return
    _validate_non_empty_string(value, name)
    if len(value) > COMMAND_SUMMARY_MAX_CHARS:
        raise ValueError(
            f"{name} must be a bounded summary of at most "
            f"{COMMAND_SUMMARY_MAX_CHARS} characters"
        )


def _validate_string_tuple(values: tuple[str, ...], name: str) -> tuple[str, ...]:
    if isinstance(values, str):
        raise ValueError(f"{name} must be an iterable of strings, not a string")
    if not isinstance(values, tuple):
        values = tuple(values)
    for value in values:
        _validate_non_empty_string(value, name)
    return values


def _is_supported_metric_value(value: object) -> bool:
    return value is None or isinstance(value, (int, float, str, bool))


_METRIC_DEFINITIONS: tuple[EvaluationMetricDefinition, ...] = (
    EvaluationMetricDefinition(
        metric_name="stable_dan_point_estimate",
        display_name="Stable Dan Point Estimate",
        metric_unit="dan",
        higher_is_better=True,
        description="Deterministic Tenhou room-specific stable-dan estimate.",
    ),
    EvaluationMetricDefinition(
        metric_name="stable_dan_ci_lower",
        display_name="Stable Dan CI Lower Bound",
        metric_unit="dan",
        higher_is_better=True,
        description="Lower bound of stable-dan bootstrap confidence interval.",
    ),
    EvaluationMetricDefinition(
        metric_name="stable_dan_ci_upper",
        display_name="Stable Dan CI Upper Bound",
        metric_unit="dan",
        higher_is_better=True,
        description="Upper bound of stable-dan bootstrap confidence interval.",
    ),
    EvaluationMetricDefinition(
        metric_name="stable_dan_threshold_outcome",
        display_name="Stable Dan Threshold Outcome",
        metric_unit="category",
        higher_is_better=None,
        description="Categorical outcome for LuckyJ threshold comparison.",
    ),
    EvaluationMetricDefinition(
        metric_name="stable_dan_sample_size_status",
        display_name="Stable Dan Sample-Size Status",
        metric_unit="category",
        higher_is_better=None,
        description="Categorical sample-size guardrail status.",
    ),
    EvaluationMetricDefinition(
        metric_name="legal_action_rate",
        display_name="Legal Action Rate",
        metric_unit="rate",
        higher_is_better=True,
        description="Fraction of selected actions that are legal.",
    ),
    EvaluationMetricDefinition(
        metric_name="invalid_action_rate",
        display_name="Invalid Action Rate",
        metric_unit="rate",
        higher_is_better=False,
        description="Fraction of selected actions that are illegal or rejected.",
    ),
    EvaluationMetricDefinition(
        metric_name="command_exit_code",
        display_name="Command Exit Code",
        metric_unit="exit_code",
        higher_is_better=False,
        description="Process exit code recorded for an offline audit command.",
    ),
    EvaluationMetricDefinition(
        metric_name="latency_ms",
        display_name="Latency",
        metric_unit="ms",
        higher_is_better=False,
        description="Elapsed wall-clock latency in milliseconds.",
    ),
    EvaluationMetricDefinition(
        metric_name="parse_success_rate",
        display_name="Parse Success Rate",
        metric_unit="rate",
        higher_is_better=True,
        description="Fraction of evaluated outputs that parsed successfully.",
    ),
    EvaluationMetricDefinition(
        metric_name="wrapper_smoke_success",
        display_name="Wrapper Smoke Success",
        metric_unit="boolean",
        higher_is_better=True,
        description="Whether a wrapper smoke/integration check succeeded.",
    ),
)

_METRIC_DEFINITIONS_BY_NAME: Mapping[str, EvaluationMetricDefinition] = (
    MappingProxyType({definition.metric_name: definition for definition in _METRIC_DEFINITIONS})
)


def list_metric_definitions() -> tuple[EvaluationMetricDefinition, ...]:
    """Return all registered P5 offline metric definitions."""

    return _METRIC_DEFINITIONS


def get_metric_definition(metric_name: str) -> EvaluationMetricDefinition:
    """Return one registered metric definition by name."""

    normalized_name = _validate_non_empty_string(metric_name, "metric_name")
    try:
        return _METRIC_DEFINITIONS_BY_NAME[normalized_name]
    except KeyError as exc:
        raise ValueError(f"unknown metric_name: {metric_name!r}") from exc
