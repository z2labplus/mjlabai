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
- P0-P12 project roadmap from rule setup through LuckyJ 10.68 validation.
- v0.1 technical execution plan: technical-plan-first execution, paper-as-future-summary.

Current stage interpretation:

```text
P0 / P1 / P2 are basically established.
The project is in P3 baseline reproducibility audit.
Mortal F1 is currently blocked by local reproducibility prerequisites.
```

## Current methodology

The project uses a strict local Codex workflow:

```text
1. Load rules first.
2. Execute only the first unchecked task in docs/10_next/10_NEXT.md.
3. Do not skip stages.
4. Do not train or modify code unless the current task explicitly asks for it.
5. After each real task, update changelog, evidence/risk notes when needed, handoff and 10_NEXT.
```

Current execution charter:

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
```

Role split:

- Web ChatGPT Pro: solution design, research, review and decision support.
- Local Codex App: code, tests and documentation landing.
- Git + docs: only source of truth.

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

Main technical route:

```text
Suphx-style SL + RL
+ Tenhou stable dan / pt EV reward
+ ACH-inspired policy improvement
+ risk model / search
+ baseline racing funnel
```

LuckyJ remains the target benchmark, not a direct full-reproduction object.

## Current next task

See:

```text
docs/10_next/10_NEXT.md
```

Latest Mortal F1 audit summary:

- GitHub connector could inspect `Equim-chan/Mortal` at commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- License is AGPL-3.0-or-later for code.
- Official inference path is mjai/Docker-oriented and requires a separate trained model artifact.
- System DNS still cannot resolve GitHub domains, but Mortal source tarball was obtained through `codeload.github.com` with explicit host resolution and checksum `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`.
- Normal `git clone` still failed; local `rustc`, `cargo`, `docker`, `conda` and PyTorch were not available.
- Official gist evidence says there is currently no plan to release trained model parameters.
- Minimal inference sample was not run; Mortal must remain at F1 Reproduce blocked.

Current expected direction:

```text
Decide whether a lawful Mortal trained model artifact can be provided.
If not, pause Mortal as a runnable baseline and move the next baseline F1 audit to Akochan.
```

## Do not forget

- The final metric is not loss.
- The final metric is not action prediction accuracy.
- The final metric is Tenhou-like strength: stable dan, pt EV, average placement and fourth-place control.
- No candidate can be promoted without evidence and a rollback path.
- P3 is an audit stage: do not train, tune, self-play or connect to real Tenhou.
- Technical decisions from Web ChatGPT Pro must be written into Git + docs before becoming project facts.
