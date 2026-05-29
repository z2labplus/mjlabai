# 09_STAGE_TASK_CONTRACT

## Current stage

P3 / baseline reproducibility audit.

Current funnel focus:

```text
Mortal = F1 paused as runnable baseline / ReferenceOnly
Akochan = F1 Blocked on local build/toolchain
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
- Do not enter F2 before F1 minimal build/run evidence exists.
- Do not promote Mortal to F2 unless a lawful, verifiable and usable trained model artifact is provided and Mortal F1 is re-opened with source, version/tag, usage constraints and checksum.

## Task boundary

F1 is an audit stage only. It may inspect external source repositories and local dependencies, but it must not create project source code or training scripts.

## Output files

After a real P3/F1 task, update:

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

Resolve Akochan F1 blocker: provide a supported build environment with Docker Linux or verified local LLVM/Boost/OpenMP, then rebuild Akochan and run minimal `legal_action` and/or `mjai_log` sample.
