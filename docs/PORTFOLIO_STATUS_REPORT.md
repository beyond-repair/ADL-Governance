# Portfolio Status Report

**Updated:** 2026-10-06 17:15Z (Sweep-247)
**Project / Version:** ADL Portfolio Governance / Sweep-247
**Objective:** Close GAP-DD-DEPENDABOT-13 named by PASS-2026-10-06-246. Re-fetch only. Do not mark fixed unless GitHub state is fixed.
**Authenticated owner:** `beyond-repair` (id 132061760). Profile `public_repos` 78 inherited from Sweep-244. Search `user:beyond-repair` `total_count` 83, `incomplete_results` false.
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user directive requires one governed sweep and a persisted pass. A2 alert 13 is the named residual. A3 classifications outside this re-fetch are inherited from `docs/repository_registry.md` (Sweep-238 census) and are not re-derived.

## Sweep-247 result

Selected gap: `GAP-DD-DEPENDABOT-13`.
GitHub state: **open**. Not marked fixed.
Portfolio exit criteria: **not met**. Sweep stops.
No repository deleted. No history rewritten. No archive flag flipped. No tag created. No lockfile edited.

| Field | Observation |
|-------|-------------|
| Alert | 13 |
| State | open |
| Package | npm `form-data` |
| Manifest | `digital_double/package-lock.json` |
| Scope | development |
| Advisory | GHSA-fjxv-7rqg-78g4 / CVE-2025-7783 |
| Severity | critical |
| Matched range | `>= 4.0.0, < 4.0.4` |
| First patched identifier | 4.0.4 |
| Open critical filter | only alert 13; `hasNextPage` false |
| Readiness | FAIL |

## Inventory

Search returned 83 repositories, 0 forks. One GitHub `archived=true` row is inherited: `CFT-v3.0`. Accounting 78 vs 83 is not forced. Full name list is the Sweep-247 search payload; names are not copied here as a second registry. Canonical list remains `docs/repository_registry.md` until an operator expands it.

## Classifications (inherited unless noted)

Exactly one class per name remains the registry contract. This sweep did not reclassify.

| Class | This sweep |
|-------|------------|
| ACTIVE | `ADL-Governance`, `forge-aegis`, `sovereign-clean-room`, `BlockSwarm`, `Digital_Double_virtual_workforce` re-fetched. Digital Double stays ACTIVE as canonical owner and FAIL on security. |
| RESEARCH | `AtomicNexusAI` claim cap 0 retained. `bloch-coherence-factor2` not re-audited. |
| SUPERSEDED | Inherited. No new successor assigned. |
| ARCHIVED | Inherited targets. GitHub flag not flipped. |

## Phase 3 live verification

| Repo | CI | Releases | Tags | Security | Readiness |
|------|----|----------|------|----------|-----------|
| forge-aegis | 37258127100 success on `e7188d52` | empty | empty | code scanning 404; dependabot open not re-listed | PASS WITH FINDINGS |
| sovereign-clean-room | main Python tests 37064696194 success on `4878918c`; latest listed runs are `seem-completion-pass` | empty | empty | secret scanning not re-fetched | PASS WITH FINDINGS |
| BlockSwarm | Foundry 36859452185 success on `6e90f6f8` | empty | empty; `v0.5.0-sagf` absent | not re-listed | PASS WITH FINDINGS |
| Digital_Double_virtual_workforce | CI 36861489156 success on `24e6a29f` | empty | empty | alert 13 open critical | FAIL |

AtomicNexusAI is not one of the four. Post-fix Deploy run 37501039089 success, CI/CD 37501039100 success, Security Audit 37501039019 success, head `f7ec8a0d`. `deploy.sh` remains an echo stub. Claim cap 0.

## Capability matrix (verified this sweep only)

| Feature | State |
|---------|-------|
| forge-aegis CI on recorded main head | VERIFIED |
| forge-aegis host-integrity product | UNVERIFIED |
| sovereign-clean-room main Python tests | VERIFIED |
| sovereign-clean-room VSA completeness | UNVERIFIED |
| BlockSwarm Foundry on recorded main head | VERIFIED |
| BlockSwarm tag `v0.5.0-sagf` | UNVERIFIED |
| Digital Double CI on recorded main head | VERIFIED |
| Digital Double form-data boundary safety | PLANNED (alert 13 open; patched identifier 4.0.4) |
| AtomicNexusAI deploy workflow exit 0 | VERIFIED as bash echo only |
| AtomicNexusAI production deploy | PLANNED |

## Dependency graph

Not rebuilt this sweep. Inherited internal edges from the registry SUPERSEDED table: SEEM-* and Auto_Legion and Gia and My-mind-A.I. point at `sovereign-clean-room`; Digital Double versioned names and `digital-double-mobile` point at `Digital_Double_virtual_workforce`; `CFT-v3.0` and `CFT-v3.1` point at `CFTv3.3-IQG-Unified-Framework`. Cycles were not recomputed. Label: UNVERIFIED for any edge not in that table.

## Security summary

- Digital Double alert 13 open critical. Additional open high/medium alerts exist (first page included pytest 168, js-yaml 160/159, brace-expansion). Not closed.
- ADL-Governance alert 1 state fixed at 2026-10-06T16:10:51Z.
- forge-aegis code scanning: 404 no analysis.
- digital-double-mobile secret alert 1 not re-fetched. Prior rotation item stands.

## Gap summary

| Capability | Severity |
|------------|----------|
| form-data < 4.0.4 on Digital Double lockfile | Critical |
| No product releases/tags on the four mandatory repos | Medium |
| Code scanning absent on forge-aegis | Medium |
| `seem-completion-pass` unmerged | Medium |
| Archive flags false on recommended ARCHIVED names | Low (operator) |
| public_repos 78 vs search 83 | Low (do not delete) |

## Canonical ownership

| Domain | Owner | Claim cap |
|--------|-------|-----------|
| Governance | ADL-Governance | docs only |
| Agent / FLS software sketch | forge-aegis | software sketch, not host product |
| Security / SEEM substrate | sovereign-clean-room | CI green is not VSA completeness |
| Distributed / SAGF | BlockSwarm | Foundry green; tag sentence unverified |
| Workforce automation | Digital_Double_virtual_workforce | CI green; security FAIL |

Duplicate canonical implementations were not deleted. SUPERSEDE remains the only allowed action and is already recorded for the historical names above.

Sweep-247 stop.
