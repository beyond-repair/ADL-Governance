# Portfolio Status Report

**Updated:** 2026-09-07T04:00Z (autonomous Sweep-100)
**Census:** Live search total_count **75** (Sweep-098; not re-enumerated this cycle).
**Governing source:** this repository.
**This cycle primary:** random select `adl-capability-matrix`.

## Sweep-100 scope

| Mode | Value |
|------|--------|
| Primary | `beyond-repair/adl-capability-matrix` |
| Classification | RESEARCH |
| Subject mutation | Docs only (`CLAIM_STATUS.md`, README drift note) |
| JSON inventory rewrite | NOT done (would require unsupported new row claims) |

## Subject summary

| Item | Evidence |
|------|----------|
| Validator + tests | Present; prior CI run 33932359958 **success** |
| inventory_count | **67** (snapshot 2026-09-04) |
| Live portfolio | **75** public items |
| Drift | OPEN — documented, not fabricated |
| Head after Sweep-100 | `50ce48524c372f628137c0bd3b7901c5c7c10ba5` |

## Classification (canonical)

### ACTIVE (7)

ADL-Governance, ADL-SEEM, forge-aegis, AEGIS-Project-Nehemiah-, sovereign-clean-room, BlockSwarm, Digital_Double_virtual_workforce.

### RESEARCH (selected)

Includes governance census tools: **adl-capability-matrix**, adl-function-census, ADL-Portfolio-Census, ADL-Nexus, aegis-repo-graph.

Physics/geometry, OS-family, Agent/SEEM siblings unchanged from Sweep-099 report.

### SUPERSEDED / ARCHIVED

Unchanged. `smart_home_BCI` docs-ARCHIVED (GitHub flag still false).

## Security / gaps (inherited)

| Item | Severity |
|------|----------|
| digital-double-mobile committed `.env` | Critical OPEN |
| Digital Double unmerged Dependabot majors | High OPEN |
| Archive flags (incl. smart_home_BCI) | Medium OPEN |
| adl-capability-matrix inventory refresh 67→75 | Medium OPEN |
| No GitHub Releases on ACTIVE products | Medium OPEN |

## Exit criteria

| Criterion | Sweep-100 |
|-----------|-----------|
| Subject claim-capped + drift documented | MET |
| Subject critical CI | MET (last product run success; tests unchanged) |
| Portfolio critical security | NOT MET |
| Portfolio duplicates consolidated | NOT MET |
| Portfolio-wide termination | NOT MET |

One governed sweep; stop.
