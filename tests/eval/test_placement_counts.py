from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval.placement_counts import (  # noqa: E402
    StableDanPlacementCounts,
    aggregate_placement_counts,
    aggregate_placement_records,
    calculate_stable_dan_from_placements,
)
from mjlabai.eval.stable_dan import calculate_stable_dan  # noqa: E402


class PlacementCountsTest(unittest.TestCase):
    def test_aggregate_integer_placements(self) -> None:
        counts = aggregate_placement_counts([1, 2, 3, 4, 1, 4])

        self.assertIsInstance(counts, StableDanPlacementCounts)
        self.assertEqual(counts.first_count, 2)
        self.assertEqual(counts.second_count, 1)
        self.assertEqual(counts.third_count, 1)
        self.assertEqual(counts.fourth_count, 2)
        self.assertEqual(counts.total_games, 6)

    def test_aggregate_string_digits(self) -> None:
        counts = aggregate_placement_counts(["1", "2", "3", "4"])

        self.assertEqual(counts.to_stable_dan_kwargs(), {
            "first_count": 1,
            "second_count": 1,
            "third_count": 1,
            "fourth_count": 1,
        })

    def test_aggregate_word_aliases(self) -> None:
        counts = aggregate_placement_counts(["first", "second", "third", "fourth"])

        self.assertEqual(counts.first_count, 1)
        self.assertEqual(counts.second_count, 1)
        self.assertEqual(counts.third_count, 1)
        self.assertEqual(counts.fourth_count, 1)

    def test_aggregate_ordinal_aliases(self) -> None:
        counts = aggregate_placement_counts(["1st", "2nd", "3rd", "4th"])

        self.assertEqual(counts.first_count, 1)
        self.assertEqual(counts.second_count, 1)
        self.assertEqual(counts.third_count, 1)
        self.assertEqual(counts.fourth_count, 1)

    def test_empty_input_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "placements must not be empty"):
            aggregate_placement_counts([])

    def test_invalid_numeric_placement_raises_value_error(self) -> None:
        for placement in (0, 5):
            with self.subTest(placement=placement):
                with self.assertRaisesRegex(ValueError, "placement must be"):
                    aggregate_placement_counts([placement])

    def test_invalid_string_placement_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported placement alias"):
            aggregate_placement_counts(["win"])

    def test_bool_placement_raises_value_error(self) -> None:
        for placement in (True, False):
            with self.subTest(placement=placement):
                with self.assertRaisesRegex(ValueError, "bool placement"):
                    aggregate_placement_counts([placement])

    def test_float_placement_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported placement value type"):
            aggregate_placement_counts([1.0])

    def test_aggregate_placement_records(self) -> None:
        counts = aggregate_placement_records(
            [
                {"game_id": "a", "placement": 1},
                {"game_id": "b", "placement": "2nd"},
                {"game_id": "c", "placement": "fourth"},
            ]
        )

        self.assertEqual(counts.first_count, 1)
        self.assertEqual(counts.second_count, 1)
        self.assertEqual(counts.third_count, 0)
        self.assertEqual(counts.fourth_count, 1)

    def test_aggregate_placement_records_with_custom_key(self) -> None:
        counts = aggregate_placement_records(
            [{"rank": "1st"}, {"rank": "4th"}],
            placement_key="rank",
        )

        self.assertEqual(counts.first_count, 1)
        self.assertEqual(counts.fourth_count, 1)

    def test_aggregate_records_empty_input_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "records must not be empty"):
            aggregate_placement_records([])

    def test_aggregate_records_missing_key_raises_key_error(self) -> None:
        with self.assertRaisesRegex(KeyError, "missing 'placement'"):
            aggregate_placement_records([{"game_id": "a"}])

    def test_aggregate_records_non_mapping_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be a mapping"):
            aggregate_placement_records([1])

    def test_to_stable_dan_kwargs_calculates_stable_dan(self) -> None:
        counts = aggregate_placement_counts([1, 2, 3, 4, 1, 4])
        result = calculate_stable_dan(**counts.to_stable_dan_kwargs(), room="phoenix")

        self.assertEqual(result.first_count, 2)
        self.assertEqual(result.fourth_count, 2)

    def test_rates_sum_to_one(self) -> None:
        counts = aggregate_placement_counts([1, 2, 3, 4, 1, 4])

        self.assertTrue(
            math.isclose(
                counts.first_rate
                + counts.second_rate
                + counts.third_rate
                + counts.fourth_rate,
                1.0,
            )
        )

    def test_to_dict_is_json_ready(self) -> None:
        counts = aggregate_placement_counts([1, 2, 3, 4])
        result = counts.to_dict()

        self.assertEqual(result["total_games"], 4)
        self.assertIn("source_note", result)

    def test_calculate_stable_dan_from_placements(self) -> None:
        result = calculate_stable_dan_from_placements(
            [1, 2, 3, 4, 1, 4],
            room="phoenix",
        )

        self.assertEqual(result.total_games, 6)
        self.assertEqual(result.first_count, 2)


if __name__ == "__main__":
    unittest.main()
