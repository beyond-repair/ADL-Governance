# Portfolio Status Report

**Updated:** 2026-09-06T17:10Z (autonomous Sweep-080)
**Census:** 75 visible repositories (`user:beyond-repair` search, `incomplete_results=false`). Profile `public_repos` field reported 72; search inventory is the governing count this cycle.

## Sweep-080 selected repo — CFTv3.3-IQG-Unified-Framework

| Field | Value |
|-------|--------|
| Selection | Uniform random among 64 non-recent names (seed 202609061307) |
| Classification | **RESEARCH** |
| CI / tests | none (ledger tree: md/tex/LICENSE only) |
| Releases / tags | none observed |
| Tree | paper + CONSISTENCY.md + RESEARCH.md lock |
| Implement | `24e190964850324c0bfc1e8971b6354efaa1b58c` |
| Physics confirmation | **unsupported** (claim ≤2; Bullet r0/c FAIL; SPARC χ²_red ~9.1 open) |

## Executive Summary

| Priority | Target | Live state | Terminal? |
|----------|--------|------------|----------|
| P0 | forge-aegis | CI **success** run 33904082644 (Sweep-078); releases=[] | No (no tag) |
| P1 | sovereign-clean-room | Python tests **success** 33979476402 | Near |
| P1 | Digital_Double_virtual_workforce | Main CI **success** 33979714262; Dependabot HIGH process OPEN | No |
| P2 | BlockSwarm | Foundry **success** 33986287866 | Near |
| P2 | sunder | RESEARCH; CI success 33996778685 | Classification yes |
| P2 | CFTv3.3-IQG-Unified-Framework | RESEARCH lock Sweep-080 | Classification yes |
| P2 | fantom_trading_bot_2 | ARCHIVED Sweep-079; GitHub flag pending | Classification yes |
| P2 | digital-double-mobile | SUPERSEDED; `.env` still tracked | Archive pending |
| P2 | ADL-Governance | This report synchronized | Yes (self this cycle) |

Portfolio-wide exit criteria: **NOT MET**.

## Phase 2 classification (directive four-state map)

Directive allows exactly: ACTIVE | RESEARCH | SUPERSEDED | ARCHIVED.

### ACTIVE (7)

ADL-Governance, ADL-SEEM, forge-aegis, AEGIS-Project-Nehemiah-, sovereign-clean-room, BlockSwarm, Digital_Double_virtual_workforce.

### RESEARCH

Includes CFTv3.3-IQG-Unified-Framework (Sweep-080 lock), coherence-drive, ware-constant-phenomenology, CFT-v3.1 (superseded *as product paper*; ledger is 3.3), LegionOS, SovereignOS, sunder, and the remainder listed in Sweep-079 report.

### SUPERSEDED

SEEM-* → sovereign-clean-room; Digital Double lineage → Digital_Double_virtual_workforce; CFT-v3.0 → CFTv3.3-IQG-Unified-Framework.

### ARCHIVED / archive-queue candidates

CFT-v3.0 already `archived=true`. fantom_trading_bot_2 documented ARCHIVED (flag false). Other candidates retain `archived=false`.

## Phase 3 — Mandatory live verification

Not re-polled Sweep-080. Evidence remains Sweep-078 Actions API + tree + releases list.

| Repo | Latest product CI | Releases |
|------|-------------------|----------|
| forge-aegis | 33904082644 success | [] |
| sovereign-clean-room | 33979476402 success | [] |
| BlockSwarm | 33986287866 success | [] |
| Digital_Double_virtual_workforce | 33979714262 success | [] |

Security findings (operator, not agent-closed):

- digital-double-mobile: committed `.env` still on `main` (Critical).
- Digital_Double_virtual_workforce: Dependabot HIGH process OPEN until PR merge.

## Canonical ownership map

| Domain | Canonical owner |
|--------|-----------------|
| Governance | ADL-Governance (+ ADL-SEEM) |
| Agent integrity / FLS | forge-aegis |
| Offline VSA / clean-room runtime | sovereign-clean-room |
| On-chain SAGF | BlockSwarm |
| Virtual workforce product | Digital_Double_virtual_workforce |
| CFT / IQG symbol ledger | CFTv3.3-IQG-Unified-Framework (RESEARCH) |
| Ware master index | coherence-drive (RESEARCH) |
| Local coding-agent experiment | sunder (RESEARCH) |

## Exit criteria checklist

- [x] 75-name census classified
- [x] Phase 3 live re-verify of mandatory four (Sweep-078; stale-by-two-sweeps)
- [x] CFTv3.3 classified RESEARCH; RESEARCH.md lock
- [ ] `.env` blob removed after rotation
- [ ] No unresolved HIGH security findings
- [ ] No missing tags on ACTIVE four
- [ ] Archive candidates GitHub-archived
- [ ] sunder README badge aligned

**Maintenance mode not entered.**
