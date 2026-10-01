# Portfolio Status Report

**Updated:** 2026-10-01 (autonomous Sweep-190)
**Project / Version:** ADL Portfolio Governance / Sweep-190
**Authenticated owner:** `beyond-repair`
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A2 Empirical — search `user:beyond-repair` this cycle `total_count=82`, `incomplete_results=false`. A3 Literature — class labels not re-audited stay inherited from Sweep-189. No promotions.

## This cycle — random select `ftmA.I.bot`

| Field | Value |
|-------|--------|
| Selection | `random.SystemRandom` over 71 names; excluded ADL-Governance and 10 most recently updated subjects |
| Subject | `ftmA.I.bot` |
| Head (pre) | `56c9af544861183d50b0ea647203809acf4d1e2d` |
| Head (post) | `79d97f92417da64deb6b31f679a7c3a6eb8a2df5` |
| Visibility | public |
| Default branch | main |
| GitHub archived flag | false |
| Classification | **RESEARCH** (archive-queue; no promotion; not GitHub-ARCHIVED) |
| Claim | 0 |
| Tree | flat historical stubs; `main.py` absent; `flashloan_front_running.py` preserved, not executed |
| Local guard | PASS (3 unittest cases; no trading imports) |
| CI | archive-guard workflow active; run 36925900968 queued on post head at record time (workflow_dispatch). Not claimed green. |
| Releases / Tags | not created |

Sweep-189 body remains in git history of this file. Class assignments unchanged except this subject reconfirmed as RESEARCH archive-queue rather than GitHub-ARCHIVED.

## Census

Search index 82. Profile `public_repos=77` inherited from Sweep-189 `get_me` (not re-fetched). GitHub `archived=true` still only `CFT-v3.0` at Sweep-189; this subject flag re-checked false.

## Classification

Exactly one class. No promotions this sweep.

- ACTIVE (7): ADL-Governance, ADL-SEEM, forge-aegis, AEGIS-Project-Nehemiah-, sovereign-clean-room, BlockSwarm, Digital_Double_virtual_workforce.
- `ftmA.I.bot`: **RESEARCH** (archive-queue). Local Sweep-126 ARCHIVED.md is intent only.
- Full table: Sweep-189 report body is in git history. Other class assignments unchanged.

## Exit criteria

| Criterion | Sweep-190 |
|-----------|-----------|
| Subject undocumented classification | MET (RESEARCH + claim 0 ledger) |
| Subject local invariant tests | MET (3 passed) |
| Subject Actions conclusion | **NOT MET** — run 36925900968 still queued at record |
| Subject GitHub archive flag | **NOT MET** (operator-only) |
| Portfolio critical security | **NOT MET** — Dependabot #13 inherited open |
| Duplicate canonical implementations | **NOT MET** |
| Portfolio termination | **NOT MET** |
