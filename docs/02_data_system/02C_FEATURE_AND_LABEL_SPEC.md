# 02C_FEATURE_AND_LABEL_SPEC

## Feature groups

| Feature group | Purpose | Status |
|---|---|---|
| Hand tiles | Own hand representation | Planned |
| Visible tiles | Discards, calls, dora, revealed info | Planned |
| Seat / round | Wind, dealer, honba, riichi sticks | Planned |
| Scores / rank | Rank-aware decisions | Planned |
| Opponent signals | Riichi, calls, danger indicators | Planned |

## Labels / heads

| Head | Decision | Notes |
|---|---|---|
| Discard | Which tile to discard | Core policy |
| Riichi | Declare or not | Include score/rank context |
| Call | Chi/pon/kan/pass | Include speed and defense |
| Win / pass | Ron/tsumo/pass | Legal action validation |
| Value | Expected rank/pt/hand outcome | Needed for search/RL |
| Danger | Deal-in risk | Needed for defense/search |
