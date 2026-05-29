"""Tenhou room-specific stable-dan point estimates."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping


class StableDanUndefinedError(ValueError):
    """Raised when stable dan cannot be defined for the given counts."""


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


def _resolve_formula(room: str) -> StableDanFormula:
    if not isinstance(room, str):
        raise ValueError("room must be a string")
    canonical_room = _ROOM_ALIASES.get(room.strip().lower())
    if canonical_room is None:
        supported = ", ".join(sorted(_ROOM_ALIASES))
        raise ValueError(f"unknown room {room!r}; supported rooms: {supported}")
    return _FORMULAS_BY_CANONICAL_ROOM[canonical_room]


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
