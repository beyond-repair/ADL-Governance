# Portfolio Status Report

**Updated:** 2026-10-04 (Sweep-217)
**Project / Version:** ADL Portfolio Governance / Sweep-217
**Objective:** Random repository completion cycle on one subject.
**Authenticated owner:** `beyond-repair` (id 132061760)
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user sweep contract; redraw excludes the Sweep-214 subject. A2 search index (83, incomplete_results false), tree, local pytest, Actions, Dependabot, secret scanning. A3 inherited classifications for names not re-read.

## Selection

Search `user:beyond-repair`, `incomplete_results=false`, `total_count=83`.
User object `public_repos` 78.
First `random.SystemRandom` seed `8769574556656521699` modulo 83 selected index 28 on a name-sorted pool: `DevelopTool-Unified-Dev-Environment` (Sweep-214 subject). Excluded for this cycle.
Second seed `18170008514042234352` modulo 82 selected `digital-double-mobile`.

## Subject

| Field | Value |
|-------|--------|
| Repo | `digital-double-mobile` |
| Visibility | public |
| Default branch | `main` |
| Pre-head | `d081c0c1f7cc9881d5b7ed76891064bc2b4060d9` |
| Post-head | `7c65eb04a678f457929671cd4909bebd61ac2eac` |
| Classification | **SUPERSEDED** |
| Claim | 0 |
| Successor | `Digital_Double_virtual_workforce` |
| GitHub archived | false |

Surface: Claim-0 FastAPI in `dd_mobile/`, Vite React `src/`, historical Flutter leftovers, superseded-guard workflow. Tree had 137 entries, not truncated. No working-tree `.env`.

## Verification

- Local `pytest`: 10 passed on pre-head, then again after the guard change.
- CI: superseded-guard run 37230662637 success on post-head `7c65eb04` (2026-10-04). Prior run 37124864136 success on `d081c0c1`.
- Open critical Dependabot: #30 `protobufjs` GHSA-xq3m-2v4x-88gg CVE-2026-41242 (runtime); #8 `form-data` GHSA-fjxv-7rqg-78g4 CVE-2025-7783 (runtime). Not bumped.
- Secret scanning alert #1 open: OpenRouter type, historical `.env`, publicly leaked, validity unknown. Value not copied into this report.

## Gap summary

| Gap | Severity |
|-----|----------|
| Secret scanning alert #1 not revoked | Critical (operator) |
| Dependabot #30 and #8 open | Critical |
| GitHub archive flag still false | Medium (operator; blocked on rotation) |
| `npm run build` not a CI gate | Low |
| Inherited Digital Double Dependabot #13 | Critical (not this subject) |
| `public_repos` 78 vs search 83 | Low / accounting |

## Exit

Subject slice re-audited and claim-capped. CI green on post-head. Not promoted. Not archived. Portfolio termination not met. Stop. Do not loop.
