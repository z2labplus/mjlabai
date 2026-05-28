# 01A_NORTH_STAR_TARGET

## North-star statement

Our goal is not to build a generic mahjong AI. Our goal is to build the strongest possible Tenhou-oriented Japanese riichi mahjong AI.

## Minimum acceptance

| Item | Target | Status | Evidence ID |
|---|---:|---|---|
| Tenhou rank level | Above 10 dan baseline | Not measured | |
| Stable dan | > 10.68 | Not measured | |
| Long-term reproducibility | Required | Not measured | |

## What does not count

- A short lucky streak.
- A model with only high supervised action accuracy.
- A result without enough games.
- A result from an environment that does not match Tenhou scoring incentives.
- A claim without documented evidence.

## Decision principle

Every major task must improve at least one of: stable dan estimate, pt EV, average rank, fourth-place control, high-dan robustness, or decision quality in critical scenarios.
