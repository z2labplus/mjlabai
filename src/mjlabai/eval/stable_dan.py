"""Tenhou room-specific stable-dan point estimates."""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from types import MappingProxyType
from typing import Mapping


class StableDanUndefinedError(ValueError):
    """Raised when stable dan cannot be defined for the given counts."""


class StableDanBootstrapUndefinedError(ValueError):
    """Raised when bootstrap CI has no defined stable-dan resamples."""


@dataclass(frozen=True)
class StableDanFormula:
    room: str
    first_weight: int
    second_weight: int


@dataclass(frozen=True)
class StableDanResult:
    room: str
    stable_dan: float
    total_games: int
    first_count: int
    second_count: int
    third_count: int
    fourth_count: int
    first_rate: float
    second_rate: float
    third_rate: float
    fourth_rate: float
    formula_name: str
    formula_weights: Mapping[str, int]
    source_note: str


@dataclass(frozen=True)
class StableDanBootstrapResult:
    point_estimate: StableDanResult
    confidence_level: float
    lower_bound: float
    upper_bound: float
    n_bootstrap: int
    successful_resamples: int
    undefined_resamples: int
    undefined_rate: float
    room: str
    method: str
    seed: int | None
    quantile_method: str
    source_note: str


@dataclass(frozen=True)
class StableDanThresholdComparison:
    threshold: float
    point_estimate: float
    lower_bound: float
    upper_bound: float
    confidence_level: float
    n_bootstrap: int
    successful_resamples: int
    undefined_resamples: int
    undefined_rate: float
    max_undefined_rate: float
    clears_threshold: bool
    point_estimate_above_threshold: bool
    lower_bound_above_threshold: bool
    upper_bound_below_threshold: bool
    reliable: bool
    outcome: str
    explanation: str
    source_note: str


@dataclass(frozen=True)
class StableDanSampleSizeAssessment:
    total_games: int
    fourth_count: int
    undefined_rate: float | None
    min_total_games_for_report: int
    min_fourth_count_for_report: int
    min_total_games_for_threshold_review: int
    min_fourth_count_for_threshold_review: int
    max_undefined_rate: float
    meets_report_minimum: bool
    meets_threshold_review_minimum: bool
    undefined_rate_acceptable: bool
    reporting_status: str
    warnings: tuple[str, ...]
    explanation: str


@dataclass(frozen=True)
class StableDanEvaluationReport:
    schema_version: str
    room: str
    first_count: int
    second_count: int
    third_count: int
    fourth_count: int
    total_games: int
    first_rate: float
    second_rate: float
    third_rate: float
    fourth_rate: float
    point_estimate: float
    confidence_level: float | None
    lower_bound: float | None
    upper_bound: float | None
    n_bootstrap: int | None
    successful_resamples: int | None
    undefined_resamples: int | None
    undefined_rate: float | None
    threshold: float | None
    threshold_outcome: str | None
    clears_threshold: bool | None
    sample_size_assessment: StableDanSampleSizeAssessment
    can_report_stable_dan: bool
    can_enter_threshold_review: bool
    notes: tuple[str, ...]
    source_note: str

    def to_dict(self) -> dict[str, object]:
        return {
            "schema_version": self.schema_version,
            "room": self.room,
            "first_count": self.first_count,
            "second_count": self.second_count,
            "third_count": self.third_count,
            "fourth_count": self.fourth_count,
            "total_games": self.total_games,
            "first_rate": self.first_rate,
            "second_rate": self.second_rate,
            "third_rate": self.third_rate,
            "fourth_rate": self.fourth_rate,
            "point_estimate": self.point_estimate,
            "confidence_level": self.confidence_level,
            "lower_bound": self.lower_bound,
            "upper_bound": self.upper_bound,
            "n_bootstrap": self.n_bootstrap,
            "successful_resamples": self.successful_resamples,
            "undefined_resamples": self.undefined_resamples,
            "undefined_rate": self.undefined_rate,
            "threshold": self.threshold,
            "threshold_outcome": self.threshold_outcome,
            "clears_threshold": self.clears_threshold,
            "sample_size_assessment": {
                "total_games": self.sample_size_assessment.total_games,
                "fourth_count": self.sample_size_assessment.fourth_count,
                "undefined_rate": self.sample_size_assessment.undefined_rate,
                "min_total_games_for_report": (
                    self.sample_size_assessment.min_total_games_for_report
                ),
                "min_fourth_count_for_report": (
                    self.sample_size_assessment.min_fourth_count_for_report
                ),
                "min_total_games_for_threshold_review": (
                    self.sample_size_assessment.min_total_games_for_threshold_review
                ),
                "min_fourth_count_for_threshold_review": (
                    self.sample_size_assessment.min_fourth_count_for_threshold_review
                ),
                "max_undefined_rate": self.sample_size_assessment.max_undefined_rate,
                "meets_report_minimum": (
                    self.sample_size_assessment.meets_report_minimum
                ),
                "meets_threshold_review_minimum": (
                    self.sample_size_assessment.meets_threshold_review_minimum
                ),
                "undefined_rate_acceptable": (
                    self.sample_size_assessment.undefined_rate_acceptable
                ),
                "reporting_status": self.sample_size_assessment.reporting_status,
                "warnings": list(self.sample_size_assessment.warnings),
                "explanation": self.sample_size_assessment.explanation,
            },
            "can_report_stable_dan": self.can_report_stable_dan,
            "can_enter_threshold_review": self.can_enter_threshold_review,
            "notes": list(self.notes),
            "source_note": self.source_note,
        }


LUCKYJ_STABLE_DAN_THRESHOLD = 10.68
DEFAULT_MIN_TOTAL_GAMES_FOR_STABLE_DAN_REPORT = 100
DEFAULT_MIN_FOURTH_COUNT_FOR_STABLE_DAN_REPORT = 10
DEFAULT_MIN_TOTAL_GAMES_FOR_THRESHOLD_REVIEW = 1000
DEFAULT_MIN_FOURTH_COUNT_FOR_THRESHOLD_REVIEW = 50
DEFAULT_MAX_UNDEFINED_RATE_FOR_STABLE_DAN_REPORT = 0.05

_FORMULAS_BY_CANONICAL_ROOM: Mapping[str, StableDanFormula] = MappingProxyType(
    {
        "general": StableDanFormula("general", first_weight=20, second_weight=10),
        "upper": StableDanFormula("upper", first_weight=40, second_weight=10),
        "expert": StableDanFormula("expert", first_weight=50, second_weight=20),
        "phoenix": StableDanFormula("phoenix", first_weight=60, second_weight=30),
    }
)

_ROOM_ALIASES: Mapping[str, str] = MappingProxyType(
    {
        "general": "general",
        "ippan": "general",
        "upper": "upper",
        "joukyu": "upper",
        "expert": "expert",
        "tokujou": "expert",
        "phoenix": "phoenix",
        "houou": "phoenix",
    }
)

ROOM_FORMULAS: Mapping[str, Mapping[str, int]] = MappingProxyType(
    {
        room: MappingProxyType(
            {"first_weight": formula.first_weight, "second_weight": formula.second_weight}
        )
        for room, formula in _FORMULAS_BY_CANONICAL_ROOM.items()
    }
)

SOURCE_NOTE = (
    "Tenhou official manual four-player dan-equivalent / stable-dan formula; "
    "deterministic point estimate only."
)

BOOTSTRAP_SOURCE_NOTE = (
    "Percentile empirical multinomial bootstrap over observed placement counts; "
    "undefined resamples with zero fourth-place count are skipped and reported."
)

THRESHOLD_SOURCE_NOTE = (
    "Stable-dan threshold comparison uses bootstrap lower bound, not point "
    "estimate alone; default threshold is LuckyJ stable dan 10.68."
)

SAMPLE_SIZE_SOURCE_NOTE = (
    "Project-internal stable-dan reporting guardrail; defaults are governance "
    "thresholds, not Tenhou official standards or proof of strength."
)

REPORT_SOURCE_NOTE = (
    "Stable-dan evaluation report schema for offline statistics; not model "
    "strength evidence by itself and not a Tenhou ranked result."
)

REPORT_NOTES = (
    "this is an offline evaluation statistics report",
    "not model strength evidence by itself",
    "not a Tenhou ranked result",
    "sample-size defaults are governance thresholds, not proof",
)


def calculate_stable_dan(
    first_count: int,
    second_count: int,
    third_count: int,
    fourth_count: int,
    room: str,
) -> StableDanResult:
    """Calculate a deterministic Tenhou stable-dan point estimate."""

    counts = _validate_counts(
        first_count=first_count,
        second_count=second_count,
        third_count=third_count,
        fourth_count=fourth_count,
    )
    total_games = sum(counts.values())
    if total_games <= 0:
        raise ValueError("total_games must be greater than zero")
    if fourth_count == 0:
        raise StableDanUndefinedError(
            "stable dan is undefined when fourth_count is zero"
        )

    formula = _resolve_formula(room)
    stable_dan = (
        (
            first_count * formula.first_weight
            + second_count * formula.second_weight
        )
        / fourth_count
        - 20
    ) / 10
    rates = placement_rates(
        first_count=first_count,
        second_count=second_count,
        third_count=third_count,
        fourth_count=fourth_count,
    )

    return StableDanResult(
        room=formula.room,
        stable_dan=stable_dan,
        total_games=total_games,
        first_count=first_count,
        second_count=second_count,
        third_count=third_count,
        fourth_count=fourth_count,
        first_rate=rates["first_rate"],
        second_rate=rates["second_rate"],
        third_rate=rates["third_rate"],
        fourth_rate=rates["fourth_rate"],
        formula_name="tenhou_four_player_room_stable_dan",
        formula_weights=ROOM_FORMULAS[formula.room],
        source_note=SOURCE_NOTE,
    )


def placement_rates(
    first_count: int,
    second_count: int,
    third_count: int,
    fourth_count: int,
) -> Mapping[str, float]:
    """Return placement rates from non-negative placement counts."""

    counts = _validate_counts(
        first_count=first_count,
        second_count=second_count,
        third_count=third_count,
        fourth_count=fourth_count,
    )
    total_games = sum(counts.values())
    if total_games <= 0:
        raise ValueError("total_games must be greater than zero")
    return MappingProxyType(
        {
            "first_rate": first_count / total_games,
            "second_rate": second_count / total_games,
            "third_rate": third_count / total_games,
            "fourth_rate": fourth_count / total_games,
        }
    )


def bootstrap_stable_dan_ci(
    first_count: int,
    second_count: int,
    third_count: int,
    fourth_count: int,
    room: str,
    *,
    n_bootstrap: int = 10000,
    confidence_level: float = 0.95,
    seed: int | None = None,
) -> StableDanBootstrapResult:
    """Estimate a percentile bootstrap CI for Tenhou stable dan."""

    if not isinstance(n_bootstrap, int) or isinstance(n_bootstrap, bool):
        raise ValueError("n_bootstrap must be a positive integer")
    if n_bootstrap <= 0:
        raise ValueError("n_bootstrap must be a positive integer")
    if not isinstance(confidence_level, (int, float)) or isinstance(
        confidence_level, bool
    ):
        raise ValueError("confidence_level must be in (0, 1)")
    if not 0 < float(confidence_level) < 1:
        raise ValueError("confidence_level must be in (0, 1)")

    point_estimate = calculate_stable_dan(
        first_count=first_count,
        second_count=second_count,
        third_count=third_count,
        fourth_count=fourth_count,
        room=room,
    )
    counts = [
        point_estimate.first_count,
        point_estimate.second_count,
        point_estimate.third_count,
        point_estimate.fourth_count,
    ]
    total_games = point_estimate.total_games
    rng = random.Random(seed)
    stable_dan_samples: list[float] = []
    undefined_resamples = 0

    for _ in range(n_bootstrap):
        sample_counts = [0, 0, 0, 0]
        for placement in rng.choices(range(4), weights=counts, k=total_games):
            sample_counts[placement] += 1
        if sample_counts[3] == 0:
            undefined_resamples += 1
            continue
        sample_result = calculate_stable_dan(
            first_count=sample_counts[0],
            second_count=sample_counts[1],
            third_count=sample_counts[2],
            fourth_count=sample_counts[3],
            room=point_estimate.room,
        )
        stable_dan_samples.append(sample_result.stable_dan)

    successful_resamples = len(stable_dan_samples)
    if successful_resamples == 0:
        raise StableDanBootstrapUndefinedError(
            "stable-dan bootstrap CI is undefined because all resamples had "
            "fourth_count equal to zero"
        )

    stable_dan_samples.sort()
    alpha = 1.0 - float(confidence_level)
    lower_bound = _linear_quantile(stable_dan_samples, alpha / 2)
    upper_bound = _linear_quantile(stable_dan_samples, 1 - alpha / 2)

    return StableDanBootstrapResult(
        point_estimate=point_estimate,
        confidence_level=float(confidence_level),
        lower_bound=lower_bound,
        upper_bound=upper_bound,
        n_bootstrap=n_bootstrap,
        successful_resamples=successful_resamples,
        undefined_resamples=undefined_resamples,
        undefined_rate=undefined_resamples / n_bootstrap,
        room=point_estimate.room,
        method="empirical_multinomial_percentile_bootstrap",
        seed=seed,
        quantile_method="linear_interpolation",
        source_note=BOOTSTRAP_SOURCE_NOTE,
    )


def compare_stable_dan_to_threshold(
    bootstrap_result: StableDanBootstrapResult,
    *,
    threshold: float = LUCKYJ_STABLE_DAN_THRESHOLD,
    max_undefined_rate: float = 0.05,
) -> StableDanThresholdComparison:
    """Compare a stable-dan bootstrap CI against a target threshold."""

    if not isinstance(bootstrap_result, StableDanBootstrapResult):
        raise TypeError("bootstrap_result must be a StableDanBootstrapResult")
    threshold_value = _validate_finite_number(threshold, "threshold")
    max_undefined_rate_value = _validate_rate(
        max_undefined_rate, "max_undefined_rate"
    )
    if bootstrap_result.lower_bound > bootstrap_result.upper_bound:
        raise ValueError("bootstrap_result lower_bound must be <= upper_bound")

    point_estimate = bootstrap_result.point_estimate.stable_dan
    point_estimate_above_threshold = point_estimate > threshold_value
    lower_bound_above_threshold = bootstrap_result.lower_bound > threshold_value
    upper_bound_below_threshold = bootstrap_result.upper_bound <= threshold_value
    reliable = bootstrap_result.undefined_rate <= max_undefined_rate_value

    if not reliable:
        outcome = "unreliable"
        clears_threshold = False
        explanation = (
            "undefined bootstrap resample rate is too high; do not claim "
            "threshold pass even if point estimate or CI bound looks good"
        )
    elif lower_bound_above_threshold:
        outcome = "clear_pass"
        clears_threshold = True
        explanation = "bootstrap lower bound exceeds threshold"
    elif upper_bound_below_threshold:
        outcome = "clear_fail"
        clears_threshold = False
        explanation = "even upper bound does not exceed threshold"
    elif point_estimate_above_threshold:
        outcome = "point_estimate_only"
        clears_threshold = False
        explanation = (
            "point estimate exceeds threshold, but bootstrap lower bound does "
            "not; cannot claim clear pass"
        )
    else:
        outcome = "inconclusive"
        clears_threshold = False
        explanation = "confidence interval overlaps threshold"

    return StableDanThresholdComparison(
        threshold=threshold_value,
        point_estimate=point_estimate,
        lower_bound=bootstrap_result.lower_bound,
        upper_bound=bootstrap_result.upper_bound,
        confidence_level=bootstrap_result.confidence_level,
        n_bootstrap=bootstrap_result.n_bootstrap,
        successful_resamples=bootstrap_result.successful_resamples,
        undefined_resamples=bootstrap_result.undefined_resamples,
        undefined_rate=bootstrap_result.undefined_rate,
        max_undefined_rate=max_undefined_rate_value,
        clears_threshold=clears_threshold,
        point_estimate_above_threshold=point_estimate_above_threshold,
        lower_bound_above_threshold=lower_bound_above_threshold,
        upper_bound_below_threshold=upper_bound_below_threshold,
        reliable=reliable,
        outcome=outcome,
        explanation=explanation,
        source_note=THRESHOLD_SOURCE_NOTE,
    )


def bootstrap_and_compare_stable_dan_threshold(
    first_count: int,
    second_count: int,
    third_count: int,
    fourth_count: int,
    room: str,
    *,
    threshold: float = LUCKYJ_STABLE_DAN_THRESHOLD,
    n_bootstrap: int = 10000,
    confidence_level: float = 0.95,
    seed: int | None = None,
    max_undefined_rate: float = 0.05,
) -> StableDanThresholdComparison:
    """Bootstrap stable dan and compare it against a target threshold."""

    bootstrap_result = bootstrap_stable_dan_ci(
        first_count=first_count,
        second_count=second_count,
        third_count=third_count,
        fourth_count=fourth_count,
        room=room,
        n_bootstrap=n_bootstrap,
        confidence_level=confidence_level,
        seed=seed,
    )
    return compare_stable_dan_to_threshold(
        bootstrap_result,
        threshold=threshold,
        max_undefined_rate=max_undefined_rate,
    )


def assess_stable_dan_sample_size(
    *,
    total_games: int,
    fourth_count: int,
    undefined_rate: float | None = None,
    min_total_games_for_report: int = DEFAULT_MIN_TOTAL_GAMES_FOR_STABLE_DAN_REPORT,
    min_fourth_count_for_report: int = DEFAULT_MIN_FOURTH_COUNT_FOR_STABLE_DAN_REPORT,
    min_total_games_for_threshold_review: int = (
        DEFAULT_MIN_TOTAL_GAMES_FOR_THRESHOLD_REVIEW
    ),
    min_fourth_count_for_threshold_review: int = (
        DEFAULT_MIN_FOURTH_COUNT_FOR_THRESHOLD_REVIEW
    ),
    max_undefined_rate: float = DEFAULT_MAX_UNDEFINED_RATE_FOR_STABLE_DAN_REPORT,
) -> StableDanSampleSizeAssessment:
    """Assess whether a stable-dan result has enough sample for reporting."""

    total_games_value = _validate_positive_int(total_games, "total_games")
    fourth_count_value = _validate_non_negative_int(fourth_count, "fourth_count")
    min_total_report = _validate_positive_int(
        min_total_games_for_report,
        "min_total_games_for_report",
    )
    min_fourth_report = _validate_non_negative_int(
        min_fourth_count_for_report,
        "min_fourth_count_for_report",
    )
    min_total_threshold = _validate_positive_int(
        min_total_games_for_threshold_review,
        "min_total_games_for_threshold_review",
    )
    min_fourth_threshold = _validate_non_negative_int(
        min_fourth_count_for_threshold_review,
        "min_fourth_count_for_threshold_review",
    )
    max_undefined_rate_value = _validate_rate(
        max_undefined_rate,
        "max_undefined_rate",
    )
    if min_total_threshold < min_total_report:
        raise ValueError(
            "min_total_games_for_threshold_review must be >= "
            "min_total_games_for_report"
        )
    if min_fourth_threshold < min_fourth_report:
        raise ValueError(
            "min_fourth_count_for_threshold_review must be >= "
            "min_fourth_count_for_report"
        )
    undefined_rate_value = None
    if undefined_rate is not None:
        undefined_rate_value = _validate_rate(undefined_rate, "undefined_rate")

    warnings: list[str] = []
    meets_report_minimum = (
        total_games_value >= min_total_report
        and fourth_count_value >= min_fourth_report
    )
    undefined_rate_acceptable = (
        undefined_rate_value is None
        or undefined_rate_value <= max_undefined_rate_value
    )
    if not meets_report_minimum:
        reporting_status = "insufficient_sample"
        meets_threshold_review_minimum = False
        if total_games_value < min_total_report:
            warnings.append("total_games below report minimum")
        if fourth_count_value < min_fourth_report:
            warnings.append("fourth_count below report minimum")
        explanation = "sample does not meet minimum stable-dan report guardrails"
    elif not undefined_rate_acceptable:
        reporting_status = "unreliable_undefined_rate"
        meets_threshold_review_minimum = False
        warnings.append("undefined_rate above maximum")
        explanation = "undefined bootstrap resample rate is too high"
    else:
        meets_threshold_review_minimum = (
            total_games_value >= min_total_threshold
            and fourth_count_value >= min_fourth_threshold
        )
        if meets_threshold_review_minimum:
            reporting_status = "threshold_review_candidate"
            explanation = "sample meets internal threshold-review guardrails"
        else:
            reporting_status = "reportable_estimate"
            if total_games_value < min_total_threshold:
                warnings.append("total_games below threshold-review minimum")
            if fourth_count_value < min_fourth_threshold:
                warnings.append("fourth_count below threshold-review minimum")
            explanation = (
                "sample may be reported as an estimate but is not ready for "
                "project-level threshold review"
            )

    return StableDanSampleSizeAssessment(
        total_games=total_games_value,
        fourth_count=fourth_count_value,
        undefined_rate=undefined_rate_value,
        min_total_games_for_report=min_total_report,
        min_fourth_count_for_report=min_fourth_report,
        min_total_games_for_threshold_review=min_total_threshold,
        min_fourth_count_for_threshold_review=min_fourth_threshold,
        max_undefined_rate=max_undefined_rate_value,
        meets_report_minimum=meets_report_minimum,
        meets_threshold_review_minimum=meets_threshold_review_minimum,
        undefined_rate_acceptable=undefined_rate_acceptable,
        reporting_status=reporting_status,
        warnings=tuple(warnings),
        explanation=explanation,
    )


def build_stable_dan_evaluation_report(
    bootstrap_result: StableDanBootstrapResult,
    threshold_comparison: StableDanThresholdComparison | None = None,
    *,
    schema_version: str = "stable_dan_report_v0.1",
) -> StableDanEvaluationReport:
    """Build a JSON-serializable stable-dan evaluation report object."""

    if not isinstance(bootstrap_result, StableDanBootstrapResult):
        raise TypeError("bootstrap_result must be a StableDanBootstrapResult")
    if threshold_comparison is not None:
        if not isinstance(threshold_comparison, StableDanThresholdComparison):
            raise TypeError(
                "threshold_comparison must be a StableDanThresholdComparison"
            )
        _validate_threshold_comparison_matches_bootstrap(
            threshold_comparison,
            bootstrap_result,
        )
    if not isinstance(schema_version, str) or not schema_version.strip():
        raise ValueError("schema_version must be a non-empty string")

    point = bootstrap_result.point_estimate
    sample_size_assessment = assess_stable_dan_sample_size(
        total_games=point.total_games,
        fourth_count=point.fourth_count,
        undefined_rate=bootstrap_result.undefined_rate,
    )
    threshold = None
    threshold_outcome = None
    clears_threshold = None
    notes = list(REPORT_NOTES)
    if threshold_comparison is not None:
        threshold = threshold_comparison.threshold
        threshold_outcome = threshold_comparison.outcome
        clears_threshold = threshold_comparison.clears_threshold
        if (
            threshold_comparison.clears_threshold
            and not sample_size_assessment.meets_threshold_review_minimum
        ):
            notes.append(
                "clear_pass does not authorize a project-level claim because "
                "sample-size threshold review minimum is not met"
            )

    return StableDanEvaluationReport(
        schema_version=schema_version,
        room=point.room,
        first_count=point.first_count,
        second_count=point.second_count,
        third_count=point.third_count,
        fourth_count=point.fourth_count,
        total_games=point.total_games,
        first_rate=point.first_rate,
        second_rate=point.second_rate,
        third_rate=point.third_rate,
        fourth_rate=point.fourth_rate,
        point_estimate=point.stable_dan,
        confidence_level=bootstrap_result.confidence_level,
        lower_bound=bootstrap_result.lower_bound,
        upper_bound=bootstrap_result.upper_bound,
        n_bootstrap=bootstrap_result.n_bootstrap,
        successful_resamples=bootstrap_result.successful_resamples,
        undefined_resamples=bootstrap_result.undefined_resamples,
        undefined_rate=bootstrap_result.undefined_rate,
        threshold=threshold,
        threshold_outcome=threshold_outcome,
        clears_threshold=clears_threshold,
        sample_size_assessment=sample_size_assessment,
        can_report_stable_dan=sample_size_assessment.meets_report_minimum,
        can_enter_threshold_review=(
            sample_size_assessment.meets_threshold_review_minimum
        ),
        notes=tuple(notes),
        source_note=REPORT_SOURCE_NOTE,
    )


def _resolve_formula(room: str) -> StableDanFormula:
    if not isinstance(room, str):
        raise ValueError("room must be a string")
    canonical_room = _ROOM_ALIASES.get(room.strip().lower())
    if canonical_room is None:
        supported = ", ".join(sorted(_ROOM_ALIASES))
        raise ValueError(f"unknown room {room!r}; supported rooms: {supported}")
    return _FORMULAS_BY_CANONICAL_ROOM[canonical_room]


def _validate_threshold_comparison_matches_bootstrap(
    comparison: StableDanThresholdComparison,
    bootstrap_result: StableDanBootstrapResult,
) -> None:
    checks = {
        "point_estimate": (
            comparison.point_estimate,
            bootstrap_result.point_estimate.stable_dan,
        ),
        "lower_bound": (comparison.lower_bound, bootstrap_result.lower_bound),
        "upper_bound": (comparison.upper_bound, bootstrap_result.upper_bound),
        "confidence_level": (
            comparison.confidence_level,
            bootstrap_result.confidence_level,
        ),
        "n_bootstrap": (comparison.n_bootstrap, bootstrap_result.n_bootstrap),
        "successful_resamples": (
            comparison.successful_resamples,
            bootstrap_result.successful_resamples,
        ),
        "undefined_resamples": (
            comparison.undefined_resamples,
            bootstrap_result.undefined_resamples,
        ),
        "undefined_rate": (
            comparison.undefined_rate,
            bootstrap_result.undefined_rate,
        ),
    }
    for name, (left, right) in checks.items():
        if left != right:
            raise ValueError(
                "threshold_comparison does not match bootstrap_result "
                f"for {name}"
            )


def _validate_finite_number(value: float, name: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError(f"{name} must be a finite number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} must be a finite number")
    return number


def _validate_positive_int(value: int, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _validate_non_negative_int(value: int, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return value


def _validate_rate(value: float, name: str) -> float:
    rate = _validate_finite_number(value, name)
    if not 0 <= rate <= 1:
        raise ValueError(f"{name} must be in [0, 1]")
    return rate


def _linear_quantile(sorted_values: list[float], q: float) -> float:
    if not sorted_values:
        raise ValueError("sorted_values must not be empty")
    if not 0 <= q <= 1:
        raise ValueError("q must be in [0, 1]")
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = (len(sorted_values) - 1) * q
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return sorted_values[lower_index]
    lower_value = sorted_values[lower_index]
    upper_value = sorted_values[upper_index]
    fraction = position - lower_index
    return lower_value + (upper_value - lower_value) * fraction


def _validate_counts(
    *,
    first_count: int,
    second_count: int,
    third_count: int,
    fourth_count: int,
) -> Mapping[str, int]:
    counts = {
        "first_count": first_count,
        "second_count": second_count,
        "third_count": third_count,
        "fourth_count": fourth_count,
    }
    for name, count in counts.items():
        if not isinstance(count, int) or isinstance(count, bool):
            raise ValueError(f"{name} must be a non-negative integer")
        if count < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    return counts
