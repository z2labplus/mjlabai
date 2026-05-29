# 07I_AKOCHAN_F1_REPRO_AUDIT

## Scope

Date: 2026-05-29.

Stage:

```text
P3 / baseline reproducibility audit
Akochan = F1 reproducibility audit
```

Goal:

```text
Decide whether Akochan can become the next runnable baseline or reviewer path before any F2 adapter work.
```

Restrictions followed:

- No model training.
- No hyperparameter tuning.
- No self-play.
- No real Tenhou connection.
- No platform automation, scraping, account, evasion or anti-detection tooling.
- No unknown model weight download or use.
- No third-party source vendoring into this repository.
- No adapter implementation and no F2 work.

## A. Repository Audit

Repository:

```text
critter-mj/akochan
```

Result:

| Item | Result |
|---|---|
| Repository accessibility | Public GitHub repository was accessible through GitHub metadata. |
| Clone URL | `https://github.com/critter-mj/akochan.git` |
| Visibility | Public |
| Default branch | `master` |
| Audited commit | `53188a0b926fbab38177f88c3cd87d554cf412af` |
| Commit date | `2022-07-05 17:40:37 +0900` |
| Commit message | `[bug fix] fixed legal chi and dahai judge` |
| README/docs/examples | `readme.md`, `readme_jpn.md`, `LICENSE`, `Makefile`, `Makefile_Linux`, `Makefile_MacOS`, `ai_src/Makefile_*`, `setup_mjai.json`, `setup_match.json`, `mjai.sh`, `haifu_log_sample.json`, `match_result/haifu_log_1000_0.json` |

Local source access check:

```text
git ls-remote --symref https://github.com/critter-mj/akochan.git HEAD
```

returned:

```text
ref: refs/heads/master HEAD
53188a0b926fbab38177f88c3cd87d554cf412af HEAD
```

Normal clone result:

```text
git clone --depth 1 https://github.com/critter-mj/akochan.git /tmp/mjlabai_akochan_audit_...
```

failed:

```text
Could not resolve host: github.com
```

Explicit host-resolution clone result:

```text
git -c http.curloptResolve=github.com:443:20.205.243.166 clone --depth 1 https://github.com/critter-mj/akochan.git /tmp/mjlabai_akochan_audit_20260529_084246
```

succeeded.

Interpretation:

- The repository is available and inspectable.
- The local environment still has unreliable normal GitHub DNS, so source access is not yet fully reproducible without an explicit host-resolution workaround.

## B. License / Usage Audit

License file:

```text
LICENSE
```

The file is a custom Japanese usage agreement, not a standard OSI license. It was read by converting from Shift_JIS to UTF-8 with:

```text
iconv -f SHIFT_JIS -t UTF-8 LICENSE
```

Key terms, paraphrased:

- The whole repository is defined as the program.
- The `ai_src` directory is defined as the AI part.
- The program can be used freely for non-public research and examination.
- Non-commercial output publication is allowed with attribution to the program.
- Other uses, including commercial publication, require author permission.
- Non-commercial individuals or groups may redistribute the program only without AI-part modification, with credit and inherited terms.
- Redistribution with AI-part modification is prohibited in principle.
- IP rights for the program and analysis results belong to the creator.
- If non-creators modify the program, IP discussions should happen in advance.
- Terms may change without prior notice.
- Japanese law and Tokyo District Court jurisdiction apply.

Usage assessment:

| Use case | Assessment | Notes |
|---|---|---|
| Private research audit | Allowed | Fits non-public research / examination. |
| Baseline or reviewer comparison | Allowed only for private research | Public output sharing should be non-commercial, attributed and reviewed. |
| Modify source | Restricted / unclear | Local source modification may trigger IP discussion; AI-part modified redistribution is prohibited in principle. Prefer wrapper/adapters outside Akochan source. |
| Redistribute | Restricted | Non-commercial redistribution without AI-part changes may be allowed with credit and inherited terms; commercial or AI-modified redistribution needs permission. |
| Future commercial or public release | Restricted | Requires legal review and likely author permission. |

License conclusion:

```text
Akochan can be audited privately and used as an internal reviewer/baseline candidate,
but source modification, redistribution, commercial use and public release are constrained.
```

## C. Dependency / Build Audit

Project shape:

- Language: C++.
- Standard: C++11.
- Build system: Makefiles.
- Main build products:
  - `ai_src` builds `libai.so`.
  - root build links `libai.so` and builds `system.exe`.

Documented Linux build:

```text
cd ai_src
make -f Makefile_Linux
cd ..
make -f Makefile_Linux
```

Documented output:

```text
libai.so
system.exe
```

Observed dependencies:

| Dependency | Evidence |
|---|---|
| `g++` / clang-compatible C++ compiler | `Makefile_Linux`, `Makefile_MacOS` |
| C++11 | `-std=c++11` |
| OpenMP | `-fopenmp`, `omp_get_thread_num()` |
| pthread | Linux root and AI Makefiles use `-pthread` |
| Boost.System / Boost.Asio | `-lboost_system`, `boost::asio` in `mjai_client.*` |
| Linux `/proc/cpuinfo` | Linux AI Makefile uses `grep -c ^processor /proc/cpuinfo` for `NPROCS` |
| Homebrew LLVM and Boost on macOS | macOS Makefiles use `brew --prefix llvm` and `brew --prefix boost` |
| Internal AI library | root Makefile links `-lai` against `libai.so` |
| Internal text parameters | 709 files under `params/` |

Local environment:

```text
OS: Darwin arm64
g++: Apple clang version 21.0.0
make: GNU Make 3.81
mjai CLI: not found
params: 709 tracked files, about 2.8M
```

Local build attempt 1:

```text
cd /tmp/mjlabai_akochan_audit_20260529_084246/ai_src
make -f Makefile_MacOS
```

Result:

```text
make: /opt/homebrew/opt/llvm/bin/clang++: No such file or directory
make: *** [obj/agari.o] Error 1
```

Local build attempt 2:

```text
cd /tmp/mjlabai_akochan_audit_20260529_084246/ai_src
make -f Makefile_Linux
```

Result:

```text
grep: /proc/cpuinfo: No such file or directory
clang++: error: unsupported argument 'medium' to option '-mcmodel=' for target 'arm64-apple-macosx26.0.0'
clang++: error: unsupported option '-fopenmp'
make: *** [obj/agari.o] Error 1
```

Build conclusion:

```text
Build is blocked on this macOS ARM environment.
No `libai.so` or `system.exe` was produced.
Root build was not attempted because `ai_src` did not build.
```

Likely supported path:

- Linux with `g++`, `libboost-all-dev`, OpenMP and pthread.
- Or a corrected macOS Homebrew toolchain with LLVM clang++, OpenMP and Boost.System available.

## D. Artifact Audit

External neural-network artifact:

```text
No external `*.pth`, `*.pt`, checkpoint or snapshot artifact was detected or needed in the audited repository.
```

Repository-included runtime data:

- `params/` contains 709 tracked text parameter files.
- `setup_mjai.json` and `setup_match.json` configure tactics and parameter selectors.
- `haifu_log_sample.json` and `match_result/haifu_log_1000_0.json` provide sample logs.

Artifact conclusion:

```text
Akochan does not appear to require external neural network weights for F1.
It does require repository-included text parameter files under `params/`.
The audited commit SHA is the current provenance record for those files.
```

Checksum status:

- No separate external artifact checksum was required.
- If future work extracts or mirrors `params/` separately, record source commit and checksums before use.

## E. Minimal Run Viability

Discovered official/source entry points:

| Entry point | Evidence | F1 note |
|---|---|---|
| `system.exe test [[seed_init] seed_end]` | `readme.md`, `main.cpp` | Self-match. Not run because self-play is forbidden in this task. |
| `system.exe check` | `main.cpp` | Requires `haifu_log.json`; not run because build failed. |
| `system.exe mjai_log <file> <id> [line_index]` | `main.cpp` | Reviewer-like entry for a log and player id; promising minimal reviewer sample after build. |
| `system.exe full_analyze <file> <id>` | `main.cpp` | Writes full analysis output; not run because build failed. |
| `system.exe para_check` | `main.cpp` | OpenMP sanity check; not run because build failed. |
| `system.exe stats <dir_name>` | `main.cpp` | Log stats; not run because build failed. |
| `system.exe stats_mjai [dir_name] [player_prefix]` | `main.cpp` | mjai log stats; not run because build failed. |
| `system.exe game_server <json>` | `main.cpp` | JSON request processor; promising for local harness after build. |
| `system.exe legal_action <json>` | `main.cpp` | JSON legal-action enumerator; promising for legal-action checks after build. |
| `system.exe legal_action_log_all <file>` | `main.cpp` | Computes legal actions over a log file; promising after build. |
| `system.exe pipe <tactics_json> <id>` | `main.cpp` | stdin/stdout JSON action stream; promising adapter target after F1. |
| `system.exe pipe_detailed <tactics_json> <id>` | `main.cpp` | detailed review stream; promising reviewer target after F1. |
| `system.exe mjai_client [port] [setup_json]` | `main.cpp`, `mjai.sh` | Local mjai client mode; requires build and `mjai` CLI/server. |

`mjai.sh`:

```text
mjai server --port=11602 --game_type=tonpu --room=default --games=5 --log_dir='./mjai_result' './system.exe mjai_client 11602 setup_mjai.json' mjai-manue mjai-manue mjai-manue
```

Local check:

```text
mjai not found
```

Minimal run result:

```text
Not run.
Blocked by failed build and missing `system.exe`.
`mjai.sh` is additionally blocked by missing `mjai` CLI.
```

No self-match was run.

## F. Input / Output / Logging Fit

Observed fit:

- `haifu_log_sample.json` and `match_result/haifu_log_1000_0.json` are newline-delimited JSON game logs with `start_game`, `start_kyoku`, `tsumo`, `dahai` and related events.
- `mjai_client` handles mjai-style events and sends JSON responses over a local TCP connection.
- `pipe` and `pipe_detailed` read JSON events from stdin and write JSON decisions/reviews to stdout.
- `legal_action` and `legal_action_log_all` expose local JSON legal-action checks.
- `mjai_log` can review a log from a specified player perspective.
- `stats_mjai` suggests existing mjai log summary support.

Fit assessment:

| Role | Assessment | Reason |
|---|---|---|
| Runnable baseline | Blocked for now | Needs successful build and minimal sample before baseline use. |
| Reviewer | Promising after build | `mjai_log`, `pipe_detailed`, `full_analyze` and sample logs fit reviewer use. |
| Legal-action checker | Promising after build | `legal_action` and `legal_action_log_all` are directly relevant. |
| Only reference | Not necessary yet | The source has enough I/O surfaces to justify resolving build blockers before demoting to reference-only. |

Unified evaluator fit:

```text
Potentially good, but not ready for F2.
F2 should only be defined after local build plus at least one minimal JSON/log/legal-action sample succeeds.
```

## G. F1 Gate Conclusion

Conclusion:

```text
Blocked
```

Reason:

- Repository is accessible and inspectable.
- License allows private research audit, but redistribution, source modification and commercial/public use are restricted.
- No external neural-network weight artifact appears required.
- Source exposes promising JSON, mjai, pipe, log review and legal-action entry points.
- However, local build failed on the current macOS ARM environment.
- No `system.exe` was produced, so no minimal run, legal-action sample, mjai log review or pipe sample could be executed.

F1 gate decision:

```text
Do not promote Akochan to F2 yet.
Resolve the build/toolchain blocker and run minimal `legal_action` and/or `mjai_log` samples first.
```

Next required task:

```text
Resolve Akochan F1 blocker: establish a supported build environment and rerun build plus minimal legal_action/mjai_log sample.
```

## H. 2026-05-29 Blocker Resolution Attempt

Goal:

```text
Resolve the Akochan F1 build/toolchain blocker and obtain minimal build/run evidence.
```

Result:

```text
Blocked
```

### A. Environment Probe

Local machine:

```text
OS: macOS 26.2 / Darwin 25.2.0
Arch: arm64
```

Tooling check:

| Tool | Result |
|---|---|
| Docker | Not available: `docker: command not found`. |
| `g++` | Present at `/usr/bin/g++`; Apple clang version 21.0.0. |
| `clang++` | Present at `/usr/bin/clang++`; Apple clang version 21.0.0. |
| `make` | Present at `/usr/bin/make`; GNU Make 3.81. |
| Homebrew | Present at `/opt/homebrew/bin/brew`. |
| Boost | Not installed/usable: no `/opt/homebrew/opt/boost`, no boost include dir, no `libboost_system` found. |
| LLVM | Not installed/usable: no `/opt/homebrew/opt/llvm/bin/clang++`. |
| OpenMP/libomp | Not installed/usable: no `omp.h` or `libomp` found in searched Homebrew/system paths. |

Build path selection:

```text
Docker Linux: unavailable.
Native Linux: unavailable, host is macOS arm64.
macOS Homebrew: blocked by missing usable LLVM/Boost/OpenMP.
Final selected path: blocked after environment probe and official Makefile attempts.
```

No global install command such as `brew install` or `sudo apt install` was run.

### B. Build Attempt

Temporary external clone:

```text
/tmp/mjlabai_akochan_build_audit
```

Clone and checkout:

```text
git -c http.curloptResolve=github.com:443:20.205.243.166 clone https://github.com/critter-mj/akochan.git /tmp/mjlabai_akochan_build_audit
cd /tmp/mjlabai_akochan_build_audit
git checkout 53188a0b926fbab38177f88c3cd87d554cf412af
```

Checked commit:

```text
53188a0b926fbab38177f88c3cd87d554cf412af
```

Build attempt 1:

```text
cd /tmp/mjlabai_akochan_build_audit/ai_src
make -f Makefile_MacOS
```

Result:

```text
make: /opt/homebrew/opt/llvm/bin/clang++: No such file or directory
make: *** [obj/agari.o] Error 1
```

Build attempt 2:

```text
cd /tmp/mjlabai_akochan_build_audit/ai_src
make -f Makefile_Linux
```

Result:

```text
grep: /proc/cpuinfo: No such file or directory
clang++: error: unsupported argument 'medium' to option '-mcmodel=' for target 'arm64-apple-macosx26.0.0'
clang++: error: unsupported option '-fopenmp'
make: *** [obj/agari.o] Error 1
```

Root build attempts were also checked after `ai_src` failed:

```text
make -f Makefile_MacOS
make -f Makefile_Linux
```

They failed for the same missing LLVM and unsupported OpenMP/macOS flag reasons.

Generated files:

| File | Result |
|---|---|
| `ai_src/libai.so` | Not generated. |
| root `libai.so` | Not generated. |
| `system.exe` | Not generated. |

### C. Minimal Non-Training Run

No minimal run was executed because `system.exe` was not generated.

Confirmed non-training candidate commands from `main.cpp` remain:

- `system.exe legal_action <json>`
- `system.exe legal_action_log_all <file>`
- `system.exe mjai_log <file> <id> [line_index]`
- `system.exe stats_mjai [dir_name] [player_name_prefix]`

Forbidden commands were not run:

- No `system.exe test`.
- No match/self-play command.
- No training command.
- No real Tenhou connection.

### D. F1 Gate Update

Conclusion:

```text
Blocked
```

Reason:

- Docker is not installed, so the preferred temporary Linux path cannot be used.
- Native Linux is not available on the host.
- macOS Homebrew build path is blocked because required LLVM/Boost/OpenMP files are absent.
- Official Linux Makefile is incompatible with this macOS ARM host.
- No `system.exe` was generated.
- No minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample could be run.

Updated next required task:

```text
Resolve Akochan F1 blocker: provide a supported build environment with Docker Linux or verified local LLVM/Boost/OpenMP, then rebuild Akochan and run minimal legal_action and/or mjai_log sample.
```

## I. 2026-05-29 GitHub Actions Ubuntu Build-Audit Workflow

Goal:

```text
Provide a supported Ubuntu Linux build environment for the next Akochan F1 build/minimal-run audit.
```

Added workflow:

```text
.github/workflows/akochan-f1-build-audit.yml
```

Workflow properties:

| Item | Value |
|---|---|
| Name | `Akochan F1 Build Audit` |
| Trigger | Manual `workflow_dispatch` only |
| Runner | `ubuntu-latest` |
| Input `akochan_commit` | Default `53188a0b926fbab38177f88c3cd87d554cf412af` |
| Input `run_minimal_samples` | Default `true` |

Workflow actions:

- Installs Ubuntu build dependencies inside the temporary GitHub-hosted runner.
- Clones `https://github.com/critter-mj/akochan.git` into `${{ runner.temp }}/akochan`.
- Checks out the requested Akochan commit.
- Attempts the Linux build path:

```text
cd ai_src
make -f Makefile_Linux
cd ..
make -f Makefile_Linux
```

- If `system.exe` is generated and `run_minimal_samples` is true, runs only minimal non-training samples:

```text
./system.exe legal_action <minimal JSON>
./system.exe mjai_log haifu_log_sample.json 0 2
```

Workflow guardrails:

- Does not train models.
- Does not tune hyperparameters.
- Does not run `system.exe test`, match or self-play tasks.
- Does not connect to real Tenhou.
- Does not create platform automation, scraping, account, evasion or anti-detection tooling.
- Does not download or use unknown model weights.
- Does not vendor or copy Akochan source into this repository.
- Does not write adapters or enter F2.
- Does not upload third-party source, `system.exe`, binaries or build artifacts.
- Writes only a short text summary to the GitHub step summary.

Current F1 status:

```text
Akochan remains F1 Blocked.
Adding the workflow is not build/run evidence by itself.
F1 can be reconsidered only after a manual workflow run succeeds and the logs are reviewed.
```

Next required task:

```text
Run the manual GitHub Actions workflow `Akochan F1 Build Audit`,
then review whether Ubuntu build produces `system.exe` and runs at least one minimal non-training sample.
```
