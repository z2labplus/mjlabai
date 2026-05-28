# 02_DATA_SYSTEM

## Goal

Build the data foundation for a Tenhou-oriented Japanese riichi mahjong AI.

## Questions

- What replay formats are supported?
- Which data is allowed to use?
- How do we represent hidden information, visible state and legal actions?
- Which labels are needed for discard, riichi, call, kan, win, defense and ranking decisions?
- How do we separate train / validation / test by player, time and table level?

## Output

A reproducible data pipeline specification with quality gates before training.
