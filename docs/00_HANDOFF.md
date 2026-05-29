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
Mortal F1 runnable-baseline path is paused because no lawful, verifiable and usable trained model artifact is currently available.
Akochan F1 is currently blocked by local build/toolchain prerequisites.
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
- Mortal: paused as a runnable baseline; retained as source-code, mjai-interface, methodology and engineering reference.
- Archer: high-potential Tenhou baseline candidate requiring verification.
- Akochan: next baseline/reviewer candidate; F1 blocked until build and minimal JSON/log sample run.
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
- Current project decision: because there is no lawful, verifiable and usable Mortal trained model artifact, Mortal is paused as a runnable baseline.
- Do not use unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Mortal remains useful as source-code, mjai-interface, methodology and engineering reference.

Current expected direction:

```text
Provide a supported build environment with Docker Linux or verified local LLVM/Boost/OpenMP, then rerun Akochan build plus minimal legal_action and/or mjai_log sample.
Do not start F2 adapter work for Akochan until F1 minimal build/run evidence exists.
```

Latest Akochan F1 audit summary:

- GitHub repository `critter-mj/akochan` is public and inspectable.
- Clone URL: `https://github.com/critter-mj/akochan.git`.
- Default branch: `master`.
- Audited commit: `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Normal `git clone` failed because local DNS could not resolve `github.com`; clone with explicit `http.curloptResolve` succeeded in `/tmp/mjlabai_akochan_audit_20260529_084246`.
- License is a custom Japanese usage agreement, not a standard OSI license. Private research audit is allowed, but redistribution, AI-part modification, commercial use and public release are restricted and need review/permission.
- Build path is C++11 Makefile-based: build `ai_src` into `libai.so`, then root into `system.exe`.
- Dependencies include g++/clang++, OpenMP, Boost.System/Boost.Asio, pthread on Linux, Homebrew LLVM/Boost on macOS and repository-included `params/` text files.
- No external neural-network `*.pth`/`*.pt`/checkpoint/snapshot artifact was detected; 709 text parameter files are included under `params/`.
- Source exposes promising `mjai_log`, `stats_mjai`, `game_server`, `legal_action`, `legal_action_log_all`, `pipe`, `pipe_detailed` and `mjai_client` entry points.
- Local macOS ARM build failed: MacOS Makefile expects `/opt/homebrew/opt/llvm/bin/clang++`; Linux Makefile is incompatible with this macOS target due `/proc/cpuinfo`, `-mcmodel=medium` and `-fopenmp`.
- `mjai` CLI was not installed.
- No `system.exe` was produced, so minimal run was not executed.
- F1 conclusion: Blocked.

Latest Akochan F1 blocker-resolution attempt:

- Docker is not installed: `docker: command not found`.
- Host is macOS 26.2 / Darwin 25.2.0 on arm64.
- `/usr/bin/g++`, `/usr/bin/clang++` and `/usr/bin/make` exist, but `g++`/`clang++` are Apple clang 21.0.0.
- Homebrew exists, but usable Boost, LLVM and OpenMP/libomp files were not present under the expected `/opt/homebrew/opt/*` paths.
- Akochan was cloned outside the repository to `/tmp/mjlabai_akochan_build_audit` and checked out at `53188a0b926fbab38177f88c3cd87d554cf412af`.
- `make -f Makefile_MacOS` in `ai_src` failed because `/opt/homebrew/opt/llvm/bin/clang++` was missing.
- `make -f Makefile_Linux` in `ai_src` failed because `/proc/cpuinfo` is absent on macOS and Apple clang rejected `-mcmodel=medium` and `-fopenmp`.
- Root Makefile attempts failed for the same missing LLVM / unsupported OpenMP reasons.
- No `libai.so` or `system.exe` was generated, so no minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample was run.
- F1 conclusion remains: Blocked.

## Do not forget

- The final metric is not loss.
- The final metric is not action prediction accuracy.
- The final metric is Tenhou-like strength: stable dan, pt EV, average placement and fourth-place control.
- No candidate can be promoted without evidence and a rollback path.
- P3 is an audit stage: do not train, tune, self-play or connect to real Tenhou.
- Technical decisions from Web ChatGPT Pro must be written into Git + docs before becoming project facts.
