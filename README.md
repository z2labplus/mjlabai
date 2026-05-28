# MjLabAI Tenhou Mahjong AI

North-star target:

```text
Train a Tenhou Japanese Mahjong AI whose long-term stable dan exceeds LuckyJ 10.68.
```

## Local Codex rule

Always read:

```text
AGENTS.md
docs/00_HANDOFF.md
docs/10_next/10_NEXT.md
```

Only execute the first unchecked task in `docs/10_next/10_NEXT.md`.

## Current methodology

Algorithm selection uses a racing funnel:

```text
F0 registration -> F1 reproducibility -> F2 adapter/legal-action -> F3 offline scenarios -> F4 small league -> F5 medium league -> F6 mainline candidate -> F7 LuckyJ validation
```

Do not fully train every candidate algorithm. Increase resources only after a candidate passes the previous stage.
