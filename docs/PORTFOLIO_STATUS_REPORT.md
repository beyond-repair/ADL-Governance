# Portfolio Status Report

**Updated:** 2026-10-01 (autonomous Sweep-198)
**Project / Version:** ADL Portfolio Governance / Sweep-198
**Authenticated owner:** `beyond-repair` (id 132061760)
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A2 Empirical — search `user:beyond-repair` this cycle `total_count=82`, `incomplete_results=false`, page 2 empty. A1 User — one governed sweep; stop if exit criteria fail. A2 — profile `public_repos=77` does not equal the search index.

## This cycle

Phase 1 discovery plus Phase 3 live verification of `forge-aegis`, `sovereign-clean-room`, `BlockSwarm`, and `Digital_Double_virtual_workforce`. Residual re-check of `ftmA.I.bot` run 36925900968. Documentation only in ADL-Governance. No product mutation. No archive flag. No release tag. No history rewrite. No lockfile edit.

Census: search index 82. Public 73. Private 9. GitHub `archived=true` only `CFT-v3.0`.

## Phase 3 — live verification

| Repo | Default-branch head | Latest product CI | Releases | Tags | Critical Dependabot |
|------|---------------------|-------------------|----------|------|---------------------|
| forge-aegis | `968595a72f50f38b64c9495b180cefd99abde45d` | run 36847797174 success, same SHA, `ci.yml` | empty | empty | open critical list empty |
| sovereign-clean-room | `5fbd20b201a02b41b1c8a9e698b78d9954a34da0` | run 36815859875 success, same SHA, `python-tests.yml` | empty | empty | open critical list empty |
| BlockSwarm | `6e90f6f85c0969fa8a262a70ceba833d618a22db` | run 36859452185 success, same SHA, `foundry.yml` | empty | empty | open critical list empty |
| Digital_Double_virtual_workforce | `24e6a29fd26c03900a8d98634d6683996eabdac4` | run 36861489156 success, same SHA, `ci.yml` | empty | empty | #13 open |

CI conclusions are Actions results on the current default-branch heads. They are not a claim that every planned feature is implemented.

`ftmA.I.bot` run 36925900968 remains `queued`. `created_at` and `updated_at` still `2026-10-01T21:02:13Z`. Jobs `total_count` 0. No conclusion. Not re-dispatched.

Secret scanning on `sovereign-clean-room`: API 404, secret scanning disabled. Code scanning on `forge-aegis`: API 404, no analysis found. Neither is a clean scan.

## Classification

Exactly one class per repository. Classes not re-audited this cycle are inherited from `docs/repository_registry.md` and marked inherited. Unaudited names stay RESEARCH. GitHub `archived=true` is a flag, not a silent class change.

### ACTIVE (inherited; four product heads re-verified this cycle)

`ADL-Governance`, `ADL-SEEM`, `forge-aegis`, `AEGIS-Project-Nehemiah-`, `sovereign-clean-room`, `BlockSwarm`, `Digital_Double_virtual_workforce`.

No promotion this cycle.

### SUPERSEDED (inherited)

| Name | Successor |
|------|-----------|
| SEEM-2.0-Self-Evolving-Emergent-Mind | sovereign-clean-room |
| SEEM-Cognitive-Microservice | sovereign-clean-room |
| SEEM-Cognitive_Microservice | sovereign-clean-room |
| seem-block-system | sovereign-clean-room |
| My-mind-A.I. | sovereign-clean-room |
| Gia---General-Intelligence-Assistant | sovereign-clean-room |
| Auto_Legion | sovereign-clean-room |
| CFT-v3.0 | CFTv3.3-IQG-Unified-Framework (also GitHub `archived=true`) |
| CFT-v3.1 | CFTv3.3-IQG-Unified-Framework / ware-constant-phenomenology |
| DigitalDoubleVirtualWorkforce3.5 | Digital_Double_virtual_workforce |
| Digital_Double_Virtual_Workforce_4. | Digital_Double_virtual_workforce |
| Digital_Double_Virtual_Workforce_4.2 | Digital_Double_virtual_workforce |
| Digital-Double_Mobile | Digital_Double_virtual_workforce |
| digital-double-mobile | Digital_Double_virtual_workforce |

### ARCHIVED

None under the governance class except the GitHub flag on `CFT-v3.0`, which remains classified SUPERSEDED because a successor is recorded. Archive-queue names stay unflagged. Do not treat queue membership as `archived=true`.

### RESEARCH

All other names in the 82-row census, including unaudited private `atomicdreamlabs` and `mendthegame`. `ADL-Nexus` remains RESEARCH. Claim contradiction from Sweep-196 not resolved this cycle.

## Capability matrix (verified only)

| Feature | State |
|---------|--------|
| forge-aegis CI on current head | VERIFIED (run 36847797174) |
| forge-aegis release / tag | ABSENT (releases and tags empty) |
| sovereign-clean-room pytest workflow on current head | VERIFIED (run 36815859875) |
| sovereign-clean-room benchmark cells | UNVERIFIED unless `results/execution_record.json` records them (README) |
| BlockSwarm Foundry workflow on current head | VERIFIED (run 36859452185) |
| BlockSwarm release tag | ABSENT |
| Digital Double CI on current head | VERIFIED (run 36861489156) |
| Digital Double form-data critical alert closed | NOT VERIFIED — #13 still open |
| Portfolio single canonical workforce | NOT MET — duplicate lines remain |

## Canonical ownership

| Domain | Canonical repo | Duplicates | Action |
|--------|----------------|------------|--------|
| Portfolio governance | ADL-Governance | ADL-SEEM (constitution sibling, not a product duplicate) | KEEP |
| Agent integrity / FLS | forge-aegis | AEGIS-Project-Nehemiah- (spec sibling) | KEEP sibling; do not merge by agent |
| Security / cognitive substrate | sovereign-clean-room | SEEM-* and Auto_Legion lines | SUPERSEDE (already classified) |
| Distributed systems / SAGF | BlockSwarm | none verified this cycle | KEEP |
| Workforce automation | Digital_Double_virtual_workforce | 3.5, 4., 4.2, mobile lines | SUPERSEDE; do not delete |

## Dependency notes

Static import graph was not recomputed this cycle. Documented internal edges only:

- Coherence Drive satellites (`m2-renormalization-law`, `topological-pinch`, `momentum-closure`, `stress-tensor-modification`, `-ware-constant-derivation`, `thrust-target-30`, `sierpinski-geometry-045`) describe dependence on the Coherence Drive / Ware Constant line. Implementation coupling UNVERIFIED.
- `sunder-cleanroom-vsa-adapter` remains contract-only toward `sovereign-clean-room` (Sweep-197 local pytest, not re-run).
- `CFTv3.3-IQG-Unified-Framework` description cites `ware-constant-phenomenology`.
- Digital Double npm lock is an external dependency surface (Dependabot). No new external API claims.

Cycles: not recomputed. Orphans: not recomputed. Do not treat this section as a complete graph.

## Security summary

- Critical open: Digital Double Dependabot #13, `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, scope development, patched 4.0.4. Updated_at on the alert object `2025-07-22T06:57:23Z`.
- High open on the same repo, first page: #160 and #159 `js-yaml` GHSA-2883-xcg3-v3hh; #155 `browserslist` GHSA-73wf-gq98-2v4g; #153 `nanoid` GHSA-xwg4-73v4-xw9w. Page not exhausted.
- forge-aegis, sovereign-clean-room, BlockSwarm: open critical Dependabot lists empty.
- Secret scanning disabled on sovereign-clean-room. Code scanning analysis absent on forge-aegis.

## Gap summary

| Capability | Severity |
|------------|----------|
| Critical Dependabot #13 still open | Critical |
| Duplicate workforce canonical lines, GitHub archive flags false | Critical (governance) |
| No release tags on the four verified product repos | Medium |
| Secret scanning disabled on sovereign-clean-room | Medium |
| Code scanning not configured on forge-aegis | Medium |
| Search 82 vs profile public_repos 77 | Low (index drift) |
| ADL-Nexus claim badge vs CLAIM_STATUS | Medium (inherited, not re-fetched) |

## Code-review readiness (this cycle)

| Repo | Result |
|------|--------|
| forge-aegis | PASS WITH FINDINGS (CI success; no release; code scanning absent) |
| sovereign-clean-room | PASS WITH FINDINGS (CI success; secret scanning disabled; VSA completeness not re-proven) |
| BlockSwarm | PASS WITH FINDINGS (Foundry success; no release tag) |
| Digital_Double_virtual_workforce | FAIL (CI success does not close critical #13) |

## Exit criteria

| Criterion | Sweep-198 |
|-----------|-----------|
| Census defined | MET (82 names) |
| Four product heads re-verified | MET |
| Critical security closed | NOT MET (#13) |
| Duplicate canonical workforce removed | NOT MET |
| Archive flags applied | NOT MET (operator-only) |
| ftmA.I.bot archive-guard concluded | NOT MET (still queued) |
| Releases present | NOT MET (empty) |
| Portfolio termination | **NOT MET** |

Stop.
