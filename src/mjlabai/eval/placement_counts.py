"""Placement-count aggregation helpers for stable-dan evaluation."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

from mjlabai.eval.stable_dan import StableDanResult, calculate_stable_dan, placement_rates


PLACEMENT_COUNTS_SOURCE_NOTE = (
    "Offline placement-count aggregation utility for stable-dan evaluation "
    "inputs; not a league runner, Tenhou connector or strength claim."
)

_PLACEMENT_ALIASES = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "1st": 1,
    "2nd": 2,
    "3rd": 3,
    "4th": 4,
}


@dataclass(frozen=True)
class StableDanPlacementCounts:
    first_count: int
    second_count: int
    third_count: int
    fourth_count: int
    total_games: int
    first_rate: float
    second_rate: float
    third_rate: float
    fourth_rate: float
    source_note: str = PLACEMENT_COUNTS_SOURCE_NOTE

    def to_stable_dan_kwargs(self) -> dict[str, int]:
        return {
            "first_count": self.first_count,
            "second_count": self.second_count,
            "third_count": self.third_count,
            "fourth_count": self.fourth_count,
        }

    def to_dict(self) -> dict[str, object]:
        return {
            "first_count": self.first_count,
            "second_count": self.second_count,
            "third_count": self.third_count,
            "fourth_count": self.fourth_count,
            "total_games": self.total_games,
            "first_rate": self.first_rate,
            "second_rate": self.second_rate,
            "third_rate": self.third_rate,
            "fourth_rate": self.fourth_rate,
            "source_note": self.source_note,
        }


def aggregate_placement_counts(
    placements: Iterable[int | str],
) -> StableDanPlacementCounts:
    """Aggregate explicit 1st/2nd/3rd/4th placement values into counts."""

    counts = {1: 0, 2: 0, 3: 0, 4: 0}
    total_games = 0
    for placement in placements:
        normalized = _normalize_placement(placement)
        counts[normalized] += 1
        total_games += 1
    if total_games <= 0:
        raise ValueError("placements must not be empty")
    rates = placement_rates(
        first_count=counts[1],
        second_count=counts[2],
        third_count=counts[3],
        fourth_count=counts[4],
    )
    return StableDanPlacementCounts(
        first_count=counts[1],
        second_count=counts[2],
        third_count=counts[3],
        fourth_count=counts[4],
        total_games=total_games,
        first_rate=rates["first_rate"],
        second_rate=rates["second_rate"],
        third_rate=rates["third_rate"],
        fourth_rate=rates["fourth_rate"],
    )


def aggregate_placement_records(
    records: Iterable[Mapping[str, Any]],
    *,
    placement_key: str = "placement",
) -> StableDanPlacementCounts:
    """Aggregate placement values from mapping records."""

    if not isinstance(placement_key, str) or not placement_key:
        raise ValueError("placement_key must be a non-empty string")
    placements: list[int | str] = []
    record_count = 0
    for index, record in enumerate(records):
        record_count += 1
        if not isinstance(record, Mapping):
            raise ValueError(f"record at index {index} must be a mapping")
        if placement_key not in record:
            raise KeyError(f"record at index {index} is missing {placement_key!r}")
        placements.append(record[placement_key])
    if record_count <= 0:
        raise ValueError("records must not be empty")
    return aggregate_placement_counts(placements)


def calculate_stable_dan_from_placements(
    placements: Iterable[int | str],
    *,
    room: str,
) -> StableDanResult:
    """Calculate deterministic stable dan from offline placement values."""

    counts = aggregate_placement_counts(placements)
    return calculate_stable_dan(**counts.to_stable_dan_kwargs(), room=room)


def _normalize_placement(placement: int | str) -> int:
    if isinstance(placement, bool):
        raise ValueError("bool placement values are not supported")
    if isinstance(placement, int):
        if placement in _PLACEMENT_ALIASES:
            return _PLACEMENT_ALIASES[placement]
        raise ValueError(f"placement must be one of 1, 2, 3 or 4: {placement!r}")
    if isinstance(placement, str):
        normalized = placement.strip().lower()
        if normalized in _PLACEMENT_ALIASES:
            return _PLACEMENT_ALIASES[normalized]
        raise ValueError(f"unsupported placement alias: {placement!r}")
    raise ValueError(f"unsupported placement value type: {type(placement).__name__}")
