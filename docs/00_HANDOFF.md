# 00_HANDOFF

## Project card

Project name: MjLabAI Tenhou Mahjong AI

North-star target:

```text
Train a Japanese Mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum target: Tenhou stable dan > 10.68.
```

## Current status

The project documentation now includes:

- North-star goal and LuckyJ benchmark.
- Tenhou-oriented success metrics.
- Data, supervised policy, self-play RL, evaluation, inference and governance structure.
- Algorithm candidate table for Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer.
- Algorithm ranking protocol.
- v0.4 racing-funnel mechanism for staged algorithm selection.

## Current methodology

The project uses a strict local Codex workflow:

```text
1. Load rules first.
2. Execute only the first unchecked task in docs/10_next/10_NEXT.md.
3. Do not skip stages.
4. Do not train or modify code unless the current task explicitly asks for it.
5. After each real task, update changelog, evidence/risk notes when needed, handoff and 10_NEXT.
```

## Algorithm selection stance

Current interpretation:

```text
Do not fully train every candidate algorithm.
Use a racing funnel:
F0 candidate registration
F1 reproducibility audit
F2 interface/legal-action adapter
F3 offline scenario evaluation
F4 small self-play league
F5 medium promotion league
F6 mainline candidate gate
F7 LuckyJ target validation
```

Roles:

- LuckyJ: final benchmark target, not implementation seed.
- Suphx: main methodology blueprint, split into reproducible modules.
- Mortal: first local reproducible baseline candidate.
- Archer: high-potential Tenhou baseline candidate requiring verification.
- Akochan: secondary baseline and reviewer.
- Kanachan: data/model architecture reference; not direct Tenhou baseline until adapted.

## Current next task

See:

```text
docs/10_next/10_NEXT.md
```

Current expected direction:

```text
Run local Codex rule-load test.
Then use templates/prompts/09_ALGORITHM_RACING_FUNNEL.md.
Then start Mortal F1 reproducibility audit unless new evidence changes the order.
```

## Do not forget

- The final metric is not loss.
- The final metric is not action prediction accuracy.
- The final metric is Tenhou-like strength: stable dan, pt EV, average placement and fourth-place control.
- No candidate can be promoted without evidence and a rollback path.
