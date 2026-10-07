# Portfolio Status Report

**Updated:** 2026-10-07 (Sweep-271)
**Project / Version:** ADL Portfolio Governance / Sweep-271
**Objective:** One governed portfolio discovery and Phase-3 live verification. Not a random single-repo completion cycle.
**Authenticated owner:** `beyond-repair` (id 132061760). Profile `public_repos` 78. Search `user:beyond-repair` `total_count` 83, `incomplete_results` false, sort updated. Private in that payload: 9. GitHub archived flag true only for `CFT-v3.0`.
**Assumption:** A2 for live API reads this sweep. A3 for classifications copied from `docs/repository_registry.md` (Sweep-238) except where Phase-3 re-fetch contradicts a CI or security claim.

Sweep-270 replaced the visible body of this file. Prior inventory remains at blob `d286661bab62308976594fd0d3d4c41c64cbae54`. This commit does not rewrite that history.

## Exit criteria

Not met. Residuals recorded. Sweep stops.

- Critical security finding remains open: Dependabot alert 13 on `Digital_Double_virtual_workforce` (`form-data`, CVE-2025-7783, critical, manifest `digital_double/package-lock.json`, scope development). https://github.com/beyond-repair/Digital_Double_virtual_workforce/security/dependabot/13
- No release and no tag on the four Phase-3 repositories.
- Duplicate Digital Double and SEEM lines remain; successors are documentary, GitHub archive flag false.
- Code scanning API returned 404 (no analysis) on all four Phase-3 repositories.
- Search count 83 versus profile `public_repos` 78 is unresolved (9 private in the search payload does not close the gap).
- Trees outside the Phase-3 set were not re-read. Capability claims for those repositories stay UNVERIFIED.

## Phase-3 live verification (2026-10-07)

| Repo | Class | CI | Releases | Tags | Tests evidence | Docs | Security | Readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| forge-aegis | ACTIVE (software sketch, not host product) | workflow `forge-aegis CI` active; latest main run 37258127100 success on `e7188d529739652a2dd6264bd3d328c1f72e60e5` | empty | empty | tree has `python/tests/test_pipeline.py`, `python/tests/test_validator.py`; this sweep did not re-execute them. CLAIM_STATUS.md records prior local 2+8 passed. | README, CLAIM_STATUS, fls/, schemas/ | Dependabot open empty. Code scanning 404. Secret scanning not re-listed. License TBD in claim file. | PASS WITH FINDINGS |
| sovereign-clean-room | ACTIVE (SEEM substrate; VSA completeness UNVERIFIED) | `python-tests.yml` active. Latest main run 37064696194 success on `4878918cf9f95d3c19e1890bef6d2fd6713e0a16`. Branch `seem-completion-pass` run 37215829476 success on `d6f13042`, not merged. Prior PR runs 37215706600 and 37214635678 failed. Branches: `main`, `seem-completion-pass`, `fix/pynacl-1.6.2-cve-2025-69277`. | empty | empty | CI conclusion only. Not a VSA completeness proof. | not re-read this sweep | Dependabot open empty. Code scanning 404. | PASS WITH FINDINGS |
| BlockSwarm | ACTIVE (Foundry contracts) | `foundry.yml` active. Latest main run 36859452185 success on `6e90f6f85c0969fa8a262a70ceba833d618a22db` | empty | empty | Foundry workflow conclusion only. This sweep did not run `forge test`. | not re-read | Dependabot open empty. Code scanning 404. | PASS WITH FINDINGS |
| Digital_Double_virtual_workforce | ACTIVE canonical workforce line | `ci.yml` active. Latest main run 36861489156 success on `24e6a29fd26c03900a8d98634d6683996eabdac4` | empty | empty | README documents pytest and smoke. This sweep did not re-execute tests. UI is documented as not wired to the Python core. | README present; claim strip says software | Dependabot critical #13 open (form-data CVE-2025-7783). High alerts include js-yaml #160/#159, browserslist #155, nanoid #153/#147. Medium pytest #168 on `digital_double/pyproject.toml`. First open page hasNextPage true; full open count not enumerated. Secret scanning open list empty. Code scanning 404. | FAIL |

## Demonstrated versus planned (Phase-3 only)

```
Feature | State
forge-aegis offline directory hash versus FLS v0.1 policy | VERIFIED as software sketch by prior tests and CI success on e7188d5; not re-run this sweep
forge-aegis host integrity product / kernel agent / remote attestation | PLANNED or UNVERIFIED; CLAIM_STATUS.md forbids the claim
sovereign-clean-room Python tests on main 4878918c | VERIFIED as Actions success only
sovereign-clean-room VSA completeness | UNVERIFIED
BlockSwarm Foundry build/test on main 6e90f6f | VERIFIED as Actions success only
BlockSwarm production network deployment | UNVERIFIED
Digital Double Python orchestrator package | PARTIAL; install path documented; tests not re-run this sweep
Digital Double React UI wired to Python core | PLANNED; README says not wired
Digital Double production workforce | UNVERIFIED
```

## Dependency and redundancy (documentary, not a full graph)

- Internal: SEEM-* and Auto_Legion / Gia / My-mind-A.I. -> sovereign-clean-room (SUPERSEDED, registry).
- Internal: DigitalDoubleVirtualWorkforce3.5, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, Digital-Double_Mobile, digital-double-mobile -> Digital_Double_virtual_workforce.
- Internal: CFT-v3.0 and CFT-v3.1 -> CFTv3.3-IQG-Unified-Framework.
- Internal: AEGIS-Project-Nehemiah- is spec sibling of forge-aegis, not a verified runtime dependency.
- External verified this sweep: BlockSwarm Foundry workflow; Digital Double pip pytest and npm lockfile; forge-aegis Python tests.
- Cycles: none demonstrated. Orphans: not computed. Duplicate infrastructure: Digital Double family and SEEM family.

Component | Canonical repo | Duplicate repo | Action
--- | --- | --- | ---
SEEM substrate | sovereign-clean-room | SEEM-2.0, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, seem-block-system, My-mind-A.I., Gia, Auto_Legion | SUPERSEDE (documentary)
Workforce orchestrator | Digital_Double_virtual_workforce | DigitalDoubleVirtualWorkforce3.5, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, Digital-Double_Mobile, digital-double-mobile | SUPERSEDE (documentary)
CFT writeup | CFTv3.3-IQG-Unified-Framework | CFT-v3.0, CFT-v3.1 | SUPERSEDE (documentary)
AEGIS runtime sketch | forge-aegis | AEGIS-Project-Nehemiah- | KEEP as spec sibling; do not merge

## Gap summary

| Capability | Severity |
| --- | --- |
| Digital Double critical Dependabot #13 still open | Critical |
| No code scanning analysis on Phase-3 repos | High |
| No release tags on Phase-3 repos | Medium |
| Archive flag false on SUPERSEDED and archive-queue repos | Medium (operator) |
| Portfolio search count versus public_repos mismatch | Low |
| Full dependency graph and per-repo test execution | Open |

## Canonical ownership

| Domain | Canonical | Not canonical |
| --- | --- | --- |
| Governance | ADL-Governance | census/map repos are evidence aids |
| Agent infrastructure | forge-aegis | AEGIS-Project-Nehemiah- is spec sibling |
| Security / SEEM | sovereign-clean-room | SEEM-* listed SUPERSEDED |
| Distributed systems | BlockSwarm | none verified |
| Workforce | Digital_Double_virtual_workforce | versioned Digital Double repos SUPERSEDED |

## Inventory rule

All 83 search hits received exactly one class from the Sweep-238 registry, not from a new tree audit:

- ACTIVE: ADL-Governance, ADL-SEEM, AEGIS-Project-Nehemiah-, BlockSwarm, Digital_Double_virtual_workforce, forge-aegis, sovereign-clean-room.
- SUPERSEDED: the SEEM and Digital Double successors listed above, plus CFT-v3.0 and CFT-v3.1.
- ARCHIVED: CFT-v3.0 is the only GitHub-archived repository. Archive-queue names stay recommended ARCHIVED with flag false (RepoRover-, DevelopTool-Unified-Dev-Environment, -Py2APK-main, AtomicNexusAI, genieGPT, Agent-Snake, fantom bots, smart_home_BCI, automate_passive_income, Quantumclustering, quantum_A.I._optimization.py, test, new-program-1.01, btc-trading, Code_Generation_AI_Program, potential-garbanzo, FortiTrade_Multi-Strategy, profile repo beyond-repair).
- RESEARCH: every other name in the 83. Not re-audited this sweep.

Name, language, pushed date, archived flag, and default branch for the 83 are in the search payload used this sweep. They are not repeated here to avoid a second unverified matrix.
