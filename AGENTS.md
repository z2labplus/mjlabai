# AGENTS.md - Project Rules for AI/Codex

## Mission

This repository follows the mjlabai Tenhou Mahjong AI Codex Methodology v0.4.

North-star target:

```text
Train a Japanese riichi mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum benchmark: above Tenhou 10 dan and stable dan > 10.68.
```

## Core rule

Do not jump stages. Always identify the current stage before doing work. Every task must explain how it helps the north-star target.

## Anti-overdocumentation rule

Documentation is a gate to safe execution, not the project deliverable. Do not
allow definition/review chains to replace implementation indefinitely.

- One boundary may have at most two consecutive docs-only tasks by default:
  one definition and one review.
- After that pair, the next task must be one of: an exact minimal executable
  implementation, an exact approval decision for that implementation, stage
  closure/deferment, or a human decision gate.
- A new adjacent boundary does not reset this count unless it is a genuine
  blocker for the named minimal executable task and the user explicitly
  approves the additional documentation.
- More than four consecutive docs-only tasks in one stage after the last
  executable code/test/experiment requires stopping and obtaining explicit
  user approval before adding another docs-only task.
- Every docs-only task must state: the concrete executable outcome it unlocks,
  the blocker that prevents execution now, the remaining mandatory gate count,
  and the exit criterion for moving to code or closing/deferring the stage.
- A review gate must not automatically create another planning document. If
  the reviewed boundary is sufficient and no real blocker exists, prefer the
  smallest safe code/test/experiment authorized by the stage contract.
- Speculative completeness is not a blocker. Record non-essential details as
  deferred instead of creating more prerequisite documents.
- If safety, compliance or evidence rules still prohibit implementation after
  the allowed docs-only chain, stop and ask the user to choose between an
  explicit exception, stage deferment/closure, or a narrowly approved task.

This rule does not permit bypassing safety, compliance, evidence or stage
gates. It requires those gates to converge toward execution or an explicit
stop decision.

## Algorithm racing-funnel rule

Algorithm selection must use the racing funnel:

```text
F0 registration -> F1 reproducibility -> F2 adapter/legal-action -> F3 offline scenarios -> F4 small league -> F5 medium league -> F6 mainline candidate -> F7 LuckyJ validation
```

Do not fully train every candidate algorithm. Increase resources only after a candidate passes the previous gate.

Current roles:

```text
LuckyJ = target benchmark
Suphx = methodology blueprint
Mortal = first local reproducible baseline candidate
Archer = high-potential Tenhou baseline candidate requiring verification
Akochan = secondary baseline / reviewer
Kanachan = data/model architecture reference
```

## Required reading order

1. AGENTS.md
2. docs/00_HANDOFF.md
3. docs/00_DOCS_INDEX.md
4. docs/09_governance/09_STAGE_TASK_CONTRACT.md
5. docs/10_next/10_NEXT.md
6. Current stage documents

## Execution rules

- Execute only the first unfinished item in `docs/10_next/10_NEXT.md`.
- When the user says “下一步”, execute only one task: the first unchecked task in `docs/10_next/10_NEXT.md`.
- Do not write code unless the current stage contract and `10_NEXT.md` explicitly allow it.
- Do not create platform automation, Tenhou connection, account tooling, scraping, evasion or anti-detection logic unless compliance has been explicitly cleared and the task is lawful and permitted.
- Do not claim the model is stronger unless there is documented evaluation evidence.
- Do not optimize only supervised loss while ignoring Tenhou pt EV, average rank, fourth-place rate and stable dan estimate.
- Do not add features that are not linked to the project goal or a documented experiment.
- Do not fully train every candidate algorithm before funnel gates justify it.
- Enforce the anti-overdocumentation rule when choosing or updating
  `docs/10_next/10_NEXT.md`.
- After finishing any real task, update:
  - `docs/10_next/10_NEXT.md`
  - `docs/09_governance/09_CHANGELOG.md`
  - `docs/00_HANDOFF.md`
- If evidence is required, record it in `docs/09_governance/09_EVIDENCE_LOG.md`.
- If a risk is discovered, record it in `docs/09_governance/09_RISK_REGISTER.md`.
- If the rule-load test is being performed, do not modify files.

## Stage roles

- Goal benchmark: AI research lead + benchmark designer.
- Data system: data engineer + mahjong replay analyst.
- Supervised policy: ML engineer + riichi strategy analyst.
- RL self-play: reinforcement learning engineer.
- Evaluation: benchmark scientist + statistician.
- Engine inference: systems engineer + inference engineer.
- Development execution: local Codex engineer.
- Experiment analysis: research scientist + failure-case reviewer.
- Governance: evidence keeper + scope controller.

## Filename policy

- Project folder, repo name, Python modules, data paths, scripts and model paths should use English/ASCII names.
- Markdown body text may be Chinese.
- Do not commit large datasets, model weights, raw logs or secrets.
