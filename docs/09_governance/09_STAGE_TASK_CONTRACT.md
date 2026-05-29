# 09_STAGE_TASK_CONTRACT

## Current stage

P3 / baseline reproducibility audit.

Current funnel focus:

```text
Mortal = F1 paused as runnable baseline / ReferenceOnly
Akochan = F2 task defined after F1 Conditional Pass on Ubuntu GitHub Actions build/minimal-run evidence
```

## AI role

Local Codex engineer + evidence keeper + scope controller.

## Stage goal

Verify whether the first local baseline candidate can be installed, built, run on a minimal sample and described well enough to later enter the unified evaluation interface.

This stage supports the north-star target by creating a reproducible baseline and engineering reference before any supervised learning, RL, search or LuckyJ validation work begins.

## Inputs

- `AGENTS.md`
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/04_rl_selfplay/04G_ALGORITHM_RACING_FUNNEL.md`
- `docs/05_evaluation/05G_RACING_FUNNEL_EVALUATION.md`
- `docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md`

## Do

- Execute only the first unchecked task in `docs/10_next/10_NEXT.md`.
- Check repository accessibility, license, dependencies, build path, model artifacts, minimal sample run, input/output schema and logging ability.
- Record commit/version, local environment results and blockers.
- Keep candidate promotion tied to documented evidence.

## Do not

- Do not train models.
- Do not tune hyperparameters.
- Do not start self-play.
- Do not connect to real Tenhou.
- Do not create platform automation, scraping, evasion or account tooling.
- Do not claim strength improvement from reproducibility checks.
- Do not use unknown model weights, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Do not vendor or copy third-party source into this repository.
- Do not exceed the documented Akochan F2 wrapper skeleton boundary: fixed `legal_action` / `mjai_log` samples only until later evidence justifies more.
- Do not vendor or store Akochan source, `system.exe`, `libai.so`, `params/`, third-party binaries or unknown artifacts in this repository.
- Do not promote Mortal to F2 unless a lawful, verifiable and usable trained model artifact is provided and Mortal F1 is re-opened with source, version/tag, usage constraints and checksum.

## Task boundary

F1 is an audit stage only. It may inspect external source repositories and local dependencies, but it must not create project source code or training scripts.

F2 may create only the documented minimal wrapper skeleton for fixed `legal_action` / `mjai_log` samples. F2 must keep Akochan source and binaries outside this repository and must not become training, self-play, Tenhou integration or platform automation.

## Output files

After a real P3/F1/F2 task, update:

- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/00_HANDOFF.md`

If the task changes candidate status or records audit evidence, update:

- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`

If a blocker or project risk is discovered, update:

- `docs/09_governance/09_RISK_REGISTER.md`

## Acceptance criteria

- The current stage and candidate funnel stage are explicit.
- License and dependency notes are recorded.
- Minimal run result is recorded as pass/fail/blocked.
- Input/output and logging viability are noted.
- The next lowest-cost action is recorded in `docs/10_next/10_NEXT.md`.

## Only next step

Implement minimal Akochan F2 wrapper skeleton for fixed legal_action/mjai_log samples under the documented no-vendor, no-training, no-Tenhou constraints.
