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
    LUCKYJ_STABLE_DAN_THRESHOLD,
    StableDanBootstrapResult,
    StableDanBootstrapUndefinedError,
    StableDanResult,
    StableDanThresholdComparison,
    StableDanUndefinedError,
    bootstrap_and_compare_stable_dan_threshold,
    bootstrap_stable_dan_ci,
    calculate_stable_dan,
    compare_stable_dan_to_threshold,
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


class StableDanBootstrapTest(unittest.TestCase):
    def test_bootstrap_returns_result(self) -> None:
        result = bootstrap_stable_dan_ci(
            30, 30, 20, 20, "phoenix", n_bootstrap=200, seed=7
        )

        self.assertIsInstance(result, StableDanBootstrapResult)
        self.assertEqual(result.room, "phoenix")
        self.assertEqual(result.n_bootstrap, 200)
        self.assertEqual(
            result.method,
            "empirical_multinomial_percentile_bootstrap",
        )

    def test_point_estimate_matches_calculator(self) -> None:
        point = calculate_stable_dan(30, 30, 20, 20, "phoenix")
        result = bootstrap_stable_dan_ci(
            30, 30, 20, 20, "phoenix", n_bootstrap=200, seed=8
        )

        self.assertEqual(result.point_estimate, point)

    def test_seed_makes_result_reproducible(self) -> None:
        first = bootstrap_stable_dan_ci(
            30, 30, 20, 20, "phoenix", n_bootstrap=250, seed=9
        )
        second = bootstrap_stable_dan_ci(
            30, 30, 20, 20, "phoenix", n_bootstrap=250, seed=9
        )

        self.assertEqual(first, second)

    def test_confidence_interval_is_ordered(self) -> None:
        result = bootstrap_stable_dan_ci(
            30, 30, 20, 20, "phoenix", n_bootstrap=200, seed=10
        )

        self.assertLessEqual(result.lower_bound, result.upper_bound)

    def test_resample_counts_sum_to_n_bootstrap(self) -> None:
        result = bootstrap_stable_dan_ci(
            30, 30, 20, 20, "phoenix", n_bootstrap=200, seed=11
        )

        self.assertEqual(
            result.successful_resamples + result.undefined_resamples,
            result.n_bootstrap,
        )

    def test_undefined_resamples_are_recorded(self) -> None:
        result = bootstrap_stable_dan_ci(
            2, 0, 0, 1, "phoenix", n_bootstrap=200, seed=12
        )

        self.assertGreater(result.undefined_resamples, 0)
        self.assertGreater(result.undefined_rate, 0)
        self.assertEqual(
            result.successful_resamples + result.undefined_resamples,
            200,
        )

    def test_original_fourth_count_zero_raises_undefined(self) -> None:
        with self.assertRaisesRegex(
            StableDanUndefinedError,
            "stable dan is undefined when fourth_count is zero",
        ):
            bootstrap_stable_dan_ci(10, 10, 10, 0, "phoenix", n_bootstrap=10)

    def test_invalid_n_bootstrap_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "n_bootstrap must be"):
            bootstrap_stable_dan_ci(1, 1, 1, 1, "phoenix", n_bootstrap=0)

    def test_invalid_confidence_level_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "confidence_level must be"):
            bootstrap_stable_dan_ci(
                1, 1, 1, 1, "phoenix", confidence_level=1.0
            )

    def test_unknown_room_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown room"):
            bootstrap_stable_dan_ci(1, 1, 1, 1, "private", n_bootstrap=10)

    def test_bootstrap_does_not_fabricate_infinite_stable_dan(self) -> None:
        result = bootstrap_stable_dan_ci(
            2, 0, 0, 1, "phoenix", n_bootstrap=200, seed=13
        )

        self.assertTrue(math.isfinite(result.lower_bound))
        self.assertTrue(math.isfinite(result.upper_bound))
        self.assertGreater(result.undefined_resamples, 0)

    def test_all_undefined_resamples_raise_clear_error(self) -> None:
        with self.assertRaisesRegex(
            StableDanBootstrapUndefinedError,
            "all resamples had fourth_count equal to zero",
        ):
            bootstrap_stable_dan_ci(1, 0, 0, 1, "phoenix", n_bootstrap=1, seed=4)


class StableDanThresholdComparisonTest(unittest.TestCase):
    def make_bootstrap_result(
        self,
        *,
        point_estimate: float,
        lower_bound: float,
        upper_bound: float,
        undefined_rate: float = 0.0,
    ) -> StableDanBootstrapResult:
        base_point = calculate_stable_dan(30, 30, 20, 20, "phoenix")
        point = StableDanResult(
            room=base_point.room,
            stable_dan=point_estimate,
            total_games=base_point.total_games,
            first_count=base_point.first_count,
            second_count=base_point.second_count,
            third_count=base_point.third_count,
            fourth_count=base_point.fourth_count,
            first_rate=base_point.first_rate,
            second_rate=base_point.second_rate,
            third_rate=base_point.third_rate,
            fourth_rate=base_point.fourth_rate,
            formula_name=base_point.formula_name,
            formula_weights=base_point.formula_weights,
            source_note=base_point.source_note,
        )
        n_bootstrap = 100
        undefined_resamples = round(undefined_rate * n_bootstrap)
        return StableDanBootstrapResult(
            point_estimate=point,
            confidence_level=0.95,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            n_bootstrap=n_bootstrap,
            successful_resamples=n_bootstrap - undefined_resamples,
            undefined_resamples=undefined_resamples,
            undefined_rate=undefined_resamples / n_bootstrap,
            room="phoenix",
            method="test",
            seed=1,
            quantile_method="test",
            source_note="test",
        )

    def test_clear_pass_requires_lower_bound_above_threshold(self) -> None:
        comparison = compare_stable_dan_to_threshold(
            self.make_bootstrap_result(
                point_estimate=11.8,
                lower_bound=10.9,
                upper_bound=12.4,
            )
        )

        self.assertIsInstance(comparison, StableDanThresholdComparison)
        self.assertTrue(comparison.clears_threshold)
        self.assertEqual(comparison.outcome, "clear_pass")
        self.assertTrue(comparison.lower_bound_above_threshold)

    def test_point_estimate_only_does_not_clear_threshold(self) -> None:
        comparison = compare_stable_dan_to_threshold(
            self.make_bootstrap_result(
                point_estimate=11.2,
                lower_bound=10.5,
                upper_bound=11.8,
            )
        )

        self.assertFalse(comparison.clears_threshold)
        self.assertEqual(comparison.outcome, "point_estimate_only")
        self.assertTrue(comparison.point_estimate_above_threshold)
        self.assertFalse(comparison.lower_bound_above_threshold)

    def test_clear_fail_when_upper_bound_does_not_exceed_threshold(self) -> None:
        comparison = compare_stable_dan_to_threshold(
            self.make_bootstrap_result(
                point_estimate=9.7,
                lower_bound=8.9,
                upper_bound=10.68,
            )
        )

        self.assertFalse(comparison.clears_threshold)
        self.assertEqual(comparison.outcome, "clear_fail")
        self.assertTrue(comparison.upper_bound_below_threshold)

    def test_inconclusive_when_ci_overlaps_threshold(self) -> None:
        comparison = compare_stable_dan_to_threshold(
            self.make_bootstrap_result(
                point_estimate=10.2,
                lower_bound=9.7,
                upper_bound=11.1,
            )
        )

        self.assertFalse(comparison.clears_threshold)
        self.assertEqual(comparison.outcome, "inconclusive")

    def test_high_undefined_rate_is_unreliable(self) -> None:
        comparison = compare_stable_dan_to_threshold(
            self.make_bootstrap_result(
                point_estimate=12.0,
                lower_bound=11.0,
                upper_bound=13.0,
                undefined_rate=0.06,
            )
        )

        self.assertFalse(comparison.clears_threshold)
        self.assertFalse(comparison.reliable)
        self.assertEqual(comparison.outcome, "unreliable")

    def test_threshold_can_be_overridden(self) -> None:
        comparison = compare_stable_dan_to_threshold(
            self.make_bootstrap_result(
                point_estimate=9.0,
                lower_bound=8.0,
                upper_bound=9.5,
            ),
            threshold=7.5,
        )

        self.assertEqual(comparison.threshold, 7.5)
        self.assertTrue(comparison.clears_threshold)

    def test_invalid_max_undefined_rate_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "max_undefined_rate must be"):
            compare_stable_dan_to_threshold(
                self.make_bootstrap_result(
                    point_estimate=11.0,
                    lower_bound=10.0,
                    upper_bound=12.0,
                ),
                max_undefined_rate=1.1,
            )

    def test_invalid_threshold_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "threshold must be"):
            compare_stable_dan_to_threshold(
                self.make_bootstrap_result(
                    point_estimate=11.0,
                    lower_bound=10.0,
                    upper_bound=12.0,
                ),
                threshold=math.inf,
            )

    def test_invalid_bootstrap_result_type_raises_type_error(self) -> None:
        with self.assertRaisesRegex(
            TypeError,
            "bootstrap_result must be a StableDanBootstrapResult",
        ):
            compare_stable_dan_to_threshold(object())

    def test_lower_bound_above_upper_bound_raises_value_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "lower_bound must be <= upper_bound"):
            compare_stable_dan_to_threshold(
                self.make_bootstrap_result(
                    point_estimate=11.0,
                    lower_bound=12.0,
                    upper_bound=10.0,
                )
            )

    def test_bootstrap_and_compare_helper_returns_comparison(self) -> None:
        comparison = bootstrap_and_compare_stable_dan_threshold(
            30,
            30,
            20,
            20,
            "phoenix",
            threshold=LUCKYJ_STABLE_DAN_THRESHOLD,
            n_bootstrap=200,
            seed=14,
        )

        self.assertIsInstance(comparison, StableDanThresholdComparison)
        self.assertEqual(comparison.threshold, LUCKYJ_STABLE_DAN_THRESHOLD)


if __name__ == "__main__":
    unittest.main()
