# 05H_STABLE_DAN_EVALUATION_API

## Purpose

This document describes the current stable-dan evaluation API for offline placement inputs.

The API exists for P5 evaluation groundwork:

- convert offline placement results into first/second/third/fourth counts.
- calculate Tenhou room-specific stable-dan point estimates.
- estimate bootstrap confidence intervals.
- compare the confidence interval against the LuckyJ stable-dan threshold.
- build a JSON-serializable stable-dan evaluation report.

It is not:

- a training module.
- a league or match runner.
- a CLI.
- a real Tenhou integration.
- a model-strength proof.
- evidence that any model exceeds LuckyJ.

Do not claim a model exceeds LuckyJ from a synthetic fixture, small sample or point estimate alone.

## Synthetic Fixture

The current smoke fixture is:

```text
tests/fixtures/eval/stable_dan_placements_smoke.json
```

This fixture is project-authored synthetic data only:

- not Tenhou data.
- not a real haifu or replay.
- not an external log.
- not a model result.
- not a league result.
- not strength evidence.

The fixture contains 100 placement records:

```text
first_count = 30
second_count = 30
third_count = 20
fourth_count = 20
```

For the phoenix / houou formula, the deterministic point estimate is:

```text
((30 * 60 + 30 * 30) / 20 - 20) / 10 = 11.5
```

This sample can validate the report code path, but it has only 100 games. It cannot support a project-level LuckyJ 10.68 claim because it does not meet the threshold-review sample-size guardrail.

## API Flow

Use the current API directly. Do not add a CLI for this path.

```python
import json
from pathlib import Path

from mjlabai.eval import (
    aggregate_placement_records,
    bootstrap_stable_dan_ci,
    build_stable_dan_evaluation_report,
    compare_stable_dan_to_threshold,
)


fixture_path = Path("tests/fixtures/eval/stable_dan_placements_smoke.json")
records = json.loads(fixture_path.read_text(encoding="utf-8"))

counts = aggregate_placement_records(records, placement_key="placement")

bootstrap = bootstrap_stable_dan_ci(
    first_count=counts.first_count,
    second_count=counts.second_count,
    third_count=counts.third_count,
    fourth_count=counts.fourth_count,
    room="phoenix",
    n_bootstrap=300,
    confidence_level=0.95,
    seed=12345,
)

comparison = compare_stable_dan_to_threshold(bootstrap)

report = build_stable_dan_evaluation_report(
    bootstrap,
    comparison,
    schema_version="stable_dan_report_example_v0.1",
)

report_dict = report.to_dict()
```

Current `StableDanEvaluationReport` does not store `model_name`, `dataset_name`, `evaluation_context` or arbitrary caller notes. Keep such metadata outside this report object until a documented task extends the schema.

## Output Fields

`report.to_dict()` returns a JSON-serializable dictionary with these key fields:

- `schema_version`: report schema version string.
- `room`: canonical room used by the stable-dan formula.
- `first_count`, `second_count`, `third_count`, `fourth_count`: placement counts.
- `total_games`: total placement records.
- `first_rate`, `second_rate`, `third_rate`, `fourth_rate`: placement rates.
- `point_estimate`: deterministic stable-dan estimate.
- `confidence_level`: bootstrap confidence level.
- `lower_bound`: bootstrap lower bound.
- `upper_bound`: bootstrap upper bound.
- `n_bootstrap`: requested bootstrap resample count.
- `successful_resamples`: defined bootstrap resamples.
- `undefined_resamples`: resamples skipped because stable dan was undefined.
- `undefined_rate`: `undefined_resamples / n_bootstrap`.
- `threshold`: comparison threshold, normally LuckyJ stable dan `10.68`.
- `threshold_outcome`: `clear_pass`, `point_estimate_only`, `clear_fail`, `unreliable` or `inconclusive`.
- `clears_threshold`: whether the lower-bound threshold rule passed.
- `sample_size_assessment`: nested sample-size guardrail result.
- `can_report_stable_dan`: whether the sample meets minimum report guardrails.
- `can_enter_threshold_review`: whether the sample meets internal threshold-review guardrails.
- `notes`: report notes that frame the result as offline statistics, not strength evidence.
- `source_note`: source note for the report schema.

The nested `sample_size_assessment` includes:

- `total_games`.
- `fourth_count`.
- `undefined_rate`.
- `min_total_games_for_report`.
- `min_fourth_count_for_report`.
- `min_total_games_for_threshold_review`.
- `min_fourth_count_for_threshold_review`.
- `max_undefined_rate`.
- `meets_report_minimum`.
- `meets_threshold_review_minimum`.
- `undefined_rate_acceptable`.
- `reporting_status`.
- `warnings`.
- `explanation`.

## Guardrails

Stable-dan reporting must stay conservative:

1. Point estimate alone cannot support a LuckyJ 10.68 claim.
2. A clear threshold pass requires bootstrap `lower_bound > 10.68` and acceptable `undefined_rate`.
3. High `undefined_rate` must be treated as unreliable.
4. Insufficient sample size cannot enter threshold review.
5. Synthetic fixtures can never be model-strength evidence.
6. A stable-dan report is an offline statistical report, not a real Tenhou ranked result.
7. Final LuckyJ comparison requires:
   - lawful sample source.
   - enough sample size.
   - room and rule consistency.
   - bootstrap lower bound above threshold.
   - sample-size guardrails passed.
   - human review.
   - a fuller evaluation protocol.

Project-internal default sample-size guardrails are:

```text
report minimum: total_games >= 100
report minimum: fourth_count >= 10
threshold-review minimum: total_games >= 1000
threshold-review minimum: fourth_count >= 50
max undefined rate: 0.05
```

These are governance defaults, not Tenhou official standards or proof.

## Verification

Run the existing tests:

```bash
python3 -m unittest tests/eval/test_stable_dan_report_smoke.py
python3 -m unittest tests/eval/test_placement_counts.py
python3 -m unittest tests/eval/test_stable_dan.py
```

These commands validate the API path and statistical helpers. They do not train a model, run a league, read Tenhou data or prove model strength.
