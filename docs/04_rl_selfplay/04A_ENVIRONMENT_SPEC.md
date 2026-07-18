# 04A_ENVIRONMENT_SPEC

| Component | Requirement | Status |
|---|---|---|
| Legal action engine | Must exactly enforce rules | Planned |
| Scoring engine | Must match target ruleset | Planned |
| Hidden information | Must not leak unseen tiles | Planned |
| Opponent policies | Support league/self-play opponents | Planned |
| Logging | Full decision trace reproducible | Planned |
| Synthetic transition contract smoke | Prove one authoritative strict-action match and immutable state progression | Implemented in `src/mjlabai/environment/synthetic_transition_smoke.py`; not a rules engine |
| Proven local riichi environment path | Pin a maintained licensed environment exposing legal actions, state transition and observation | MahJax `v0.1.2` / commit `3f9cee1` / Apache-2.0 selected in `04J`; exact integration smoke is next |

## Invalid environment examples

- Hidden tiles leaked to the policy.
- Scoring does not match target Tenhou rules.
- Legal actions differ from real riichi rules.
- Opponents are too weak to expose high-dan mistakes.
