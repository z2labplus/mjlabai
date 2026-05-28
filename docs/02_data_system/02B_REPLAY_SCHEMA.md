# 02B_REPLAY_SCHEMA

## Replay entity

| Field | Type | Required | Notes |
|---|---|---|---|
| game_id | string | yes | Stable unique ID |
| ruleset | string | yes | Tenhou-compatible rules description |
| players | list | yes | Anonymized when needed |
| rounds | list | yes | Full hand sequence |

## Decision state entity

| Field | Type | Required | Notes |
|---|---|---|---|
| visible_state | object | yes | Hand, discards, calls, dora, scores, winds, round |
| legal_actions | list | yes | Discard / riichi / call / win / kan / pass |
| action_taken | object | yes | Human or model action |
| result | object | yes | Hand result and rank result |

## Rule

Every training example must be reproducible from a replay and a step index.
