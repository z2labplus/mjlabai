from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from mjlabai.eval.stable_dan import (  # noqa: E402
    StableDanUndefinedError,
    calculate_stable_dan,
    placement_rates,
)


class StableDanTest(unittest.TestCase):
    def test_phoenix_formula(self) -> None:
        result = calculate_stable_dan(30, 30, 20, 20, "phoenix")

        self.assertEqual(result.room, "phoenix")
        self.assertEqual(result.total_games, 100)
        self.assertEqual(result.stable_dan, 11.5)
        self.assertEqual(
            dict(result.formula_weights),
            {"first_weight": 60, "second_weight": 30},
        )

    def test_expert_formula(self) -> None:
        result = calculate_stable_dan(30, 30, 20, 20, "expert")

        self.assertEqual(result.room, "expert")
        self.assertEqual(result.stable_dan, 8.5)
        self.assertEqual(
            dict(result.formula_weights),
            {"first_weight": 50, "second_weight": 20},
        )

    def test_general_and_upper_formulas(self) -> None:
        general = calculate_stable_dan(30, 30, 20, 20, "general")
        upper = calculate_stable_dan(30, 30, 20, 20, "upper")

        self.assertEqual(general.stable_dan, 2.5)
        self.assertEqual(upper.stable_dan, 5.5)

    def test_room_aliases(self) -> None:
        self.assertEqual(calculate_stable_dan(30, 30, 20, 20, "ippan").room, "general")
        self.assertEqual(calculate_stable_dan(30, 30, 20, 20, "joukyu").room, "upper")
        self.assertEqual(calculate_stable_dan(30, 30, 20, 20, "tokujou").room, "expert")
        self.assertEqual(calculate_stable_dan(30, 30, 20, 20, "houou").room, "phoenix")

    def test_placement_rates_sum_to_one(self) -> None:
        rates = placement_rates(30, 30, 20, 20)

        self.assertTrue(math.isclose(sum(rates.values()), 1.0))
        self.assertEqual(rates["first_rate"], 0.3)
        self.assertEqual(rates["fourth_rate"], 0.2)

    def test_fourth_count_zero_raises_undefined(self) -> None:
        with self.assertRaisesRegex(
            StableDanUndefinedError,
            "stable dan is undefined when fourth_count is zero",
        ):
            calculate_stable_dan(10, 10, 10, 0, "phoenix")

    def test_negative_count_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "first_count must be"):
            calculate_stable_dan(-1, 0, 0, 1, "phoenix")

    def test_unknown_room_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown room"):
            calculate_stable_dan(1, 1, 1, 1, "private")

    def test_third_count_affects_total_and_rates_not_numerator(self) -> None:
        low_third = calculate_stable_dan(30, 30, 0, 20, "phoenix")
        high_third = calculate_stable_dan(30, 30, 200, 20, "phoenix")

        self.assertEqual(low_third.stable_dan, high_third.stable_dan)
        self.assertEqual(low_third.total_games, 80)
        self.assertEqual(high_third.total_games, 280)
        self.assertNotEqual(low_third.third_rate, high_third.third_rate)


if __name__ == "__main__":
    unittest.main()
