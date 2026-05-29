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


def _resolve_formula(room: str) -> StableDanFormula:
    if not isinstance(room, str):
        raise ValueError("room must be a string")
    canonical_room = _ROOM_ALIASES.get(room.strip().lower())
    if canonical_room is None:
        supported = ", ".join(sorted(_ROOM_ALIASES))
        raise ValueError(f"unknown room {room!r}; supported rooms: {supported}")
    return _FORMULAS_BY_CANONICAL_ROOM[canonical_room]


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
