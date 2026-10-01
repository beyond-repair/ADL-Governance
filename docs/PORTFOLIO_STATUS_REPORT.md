# Portfolio Status Report

**Updated:** 2026-10-01 (autonomous Sweep-189)
**Project / Version:** ADL Portfolio Governance / Sweep-189
**Authenticated owner:** `beyond-repair` (`public_repos=77`, `get_me` this cycle)
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A2 Empirical — search `user:beyond-repair` returned `total_count=82`, `incomplete_results=false`. A3 Literature — class labels not re-audited this cycle stay inherited from `docs/repository_registry.md` (Sweep-173) unless contradicted by this cycle's live calls. No class promotions.

No repository deletion. No history rewrite. No archive flag. No release tag. No product-repo mutation.

## Census

| Source | Count | Note |
|--------|------:|------|
| Search `user:beyond-repair` | 82 | `incomplete_results=false`. Page 2 empty. Full name list captured. |
| Profile `public_repos` | 77 | `get_me` this cycle |
| GitHub `archived=true` in search payload | 1 | `CFT-v3.0` only (observed in truncated tail) |
| Direct-get union 86 | not re-fetched | Inherited drift. Do not treat as closed. |

## Classification (exactly one)

Inherited unless noted. No promotions this cycle.

- **ACTIVE (7):** `ADL-Governance`, `ADL-SEEM`, `forge-aegis`, `AEGIS-Project-Nehemiah-`, `sovereign-clean-room`, `BlockSwarm`, `Digital_Double_virtual_workforce`.
- **SUPERSEDED:** SEEM lineage and Digital Double forks toward the ACTIVE owners below. `CFT-v3.1` toward `CFTv3.3-IQG-Unified-Framework` / `ware-constant-phenomenology` (inherited). `digital-double-mobile` remains SUPERSEDED (Sweep-184).
- **ARCHIVED:** `CFT-v3.0` only (GitHub flag observed). Archive-queue names are **not** flagged this cycle and stay RESEARCH or SUPERSEDED until the operator sets `archived=true`.
- **RESEARCH:** all other search-index names, including OS-family sketches, Coherence Drive satellites, `sunder`, mapping repos, and `RealityOS` (reconfirmed Sweep-187, not re-tested this cycle).

### Canonical ownership

| Domain | Canonical repo | Non-canonical |
|--------|----------------|---------------|
| Governance | `ADL-Governance` | profile README `beyond-repair` is an index only |
| SEEM / clean-room | `sovereign-clean-room` (constitution sibling `ADL-SEEM`) | `SEEM-2.0-Self-Evolving-Emergent-Mind`, `SEEM-Cognitive-Microservice`, `SEEM-Cognitive_Microservice`, `seem-block-system`, `My-mind-A.I.`, `Gia---General-Intelligence-Assistant`, `Auto_Legion` |
| Agent integrity | `forge-aegis` | spec sibling `AEGIS-Project-Nehemiah-` (not a second runtime) |
| Distributed / SAGF | `BlockSwarm` | none verified |
| Workforce | `Digital_Double_virtual_workforce` | `DigitalDoubleVirtualWorkforce3.5`, `Digital_Double_Virtual_Workforce_4.`, `Digital_Double_Virtual_Workforce_4.2`, `Digital-Double_Mobile`, `digital-double-mobile` |
| Coherence Drive research | `coherence-drive` (RESEARCH, claim-capped) | satellite theorem repos; not a device claim |
| Mapping | `adl-capability-matrix`, `aegis-repo-graph`, `adl-function-census`, bridges | contract only; no runtime interop |

Duplicate canonical implementations remain: OS-family sketches (`SovereignOS`, `Sovereign-OS`, `LegionOS`, `RealityOS`) are RESEARCH, not a second OS. Mapping repos must not be read as kernels.

## Phase 3 — live verification (this cycle)

| Repo | Latest product CI | Head | Releases | Tags | Dependabot open | Secret / code scan |
|------|-------------------|------|----------|------|-----------------|--------------------|
| `forge-aegis` | success run 36847797174, workflow `forge-aegis CI`, 2026-10-01T10:13:42Z | `968595a72f50f38b64c9495b180cefd99abde45d` | empty | empty | none returned | code scanning 404 no analysis |
| `sovereign-clean-room` | success run 36815859875, workflow `Python tests`, 2026-10-01T04:35:54Z | `5fbd20b201a02b41b1c8a9e698b78d9954a34da0` | empty | empty | none returned | secret scanning 404 disabled |
| `BlockSwarm` | success run 36859452185, workflow `Foundry`, 2026-10-01T12:05:12Z | `6e90f6f85c0969fa8a262a70ceba833d618a22db` | empty | empty | none returned | not re-listed |
| `Digital_Double_virtual_workforce` | success run 36861489156, workflow `Digital Double CI`, 2026-10-01T12:24:02Z | `24e6a29fd26c03900a8d98634d6683996eabdac4` | empty | empty | critical #13 open; high/medium/low pages non-empty | secret scanning list returned empty |

README claim that BlockSwarm tag lineage includes `v0.5.0-sagf` is **UNVERIFIED** against the tags API (empty). Do not treat CI green as a release.

Tests were not re-executed locally this cycle. CI success is an Actions conclusion only. sovereign-clean-room VSA completeness remains UNVERIFIED.

## Capability matrix (demonstrated vs planned)

| Feature | State |
|---------|--------|
| forge-aegis CI on main | VERIFIED (run 36847797174 success) |
| forge-aegis FLS runtime / v0.1.0 release | PLANNED / UNVERIFIED (no tag, no release) |
| sovereign-clean-room Python tests workflow | VERIFIED (run 36815859875 success) |
| sovereign-clean-room production VSA completeness | UNVERIFIED |
| BlockSwarm Foundry workflow | VERIFIED (run 36859452185 success) |
| BlockSwarm `v0.5.0-sagf` tag | UNVERIFIED (tags API empty) |
| BlockSwarm AI-cannot-execute invariant | documented; on-chain proof not re-read this cycle — PARTIAL |
| Digital Double CI + installable package commit message | VERIFIED at Actions level (run 36861489156) |
| Digital Double 16 pytest cases | documented in commit message; not re-run here — PARTIAL |
| Digital Double dependency clearance | FAIL (Dependabot #13 open) |
| Mapping-repo runtime interop | not claimed |
| RealityOS connectors | absent at Sweep-187; not re-fetched |

## Dependency graph (declared, not import-parsed)

Internal (governance-declared, not AST-verified this cycle):

- `ADL-SEEM` → `sovereign-clean-room` (canonical pointer)
- `sunder-cleanroom-vsa-adapter` → `sunder`, `sovereign-clean-room` (contract only)
- `seem-sunder-bridge` → `sunder`, `sovereign-clean-room`, `SEEM-2.0-Self-Evolving-Emergent-Mind` (contract only)
- `aegis-repo-graph` → portfolio names (metadata)
- `BlockSwarm` → forge-std / OpenZeppelin submodules (documented in CI commit; pins not re-read)
- Digital Double forks → `Digital_Double_virtual_workforce` (successor, not a build dependency)

External (observed):

- `Digital_Double_virtual_workforce` → npm `form-data` (critical advisory), `js-yaml` (high, alert #160), pip `pytest` (medium, alert #168)
- `forge-aegis` / `sovereign-clean-room` → Python (no open Dependabot page returned)
- `BlockSwarm` → Solidity / Foundry

Cycles: none proven. Import-level graph remains **NOT MET**. Orphans: archive-queue experiments with no successor other than historical preservation.

## Gap summary

| Capability | Severity |
|------------|----------|
| Dependabot #13 `form-data` GHSA-fjxv-7rqg-78g4 / CVE-2025-7783 on Digital Double (`digital_double/package-lock.json`, development, patched 4.0.4) | Critical |
| Additional open Dependabot alerts (high #160 `js-yaml`, medium #168 `pytest`; low page also non-empty). Exact open total not returned by API page | High |
| `digital-double-mobile` tracked `.env` | Critical residual (not re-fetched) |
| Secret scanning disabled on `sovereign-clean-room` | High |
| Code scanning no analysis on `forge-aegis` | Medium |
| Empty releases/tags on ACTIVE products; BlockSwarm tag claim UNVERIFIED | Medium |
| Import-level dependency map | Medium |
| Archive flag not applied | Operator |
| Census drift 77 vs 82 (86 inherited, not re-fetched) | Medium |
| Pass YAML missing for sweeps 186 and 187 | Low (governance) |

## Code-review readiness (Phase 10)

| Repo | Result |
|------|--------|
| `forge-aegis` | PASS WITH FINDINGS |
| `sovereign-clean-room` | PASS WITH FINDINGS |
| `BlockSwarm` | PASS WITH FINDINGS |
| `Digital_Double_virtual_workforce` | FAIL (critical Dependabot #13 open; CI success does not clear it) |
| Remainder | UNVERIFIED this cycle |

## Exit criteria

| Criterion | Sweep-189 |
|-----------|-----------|
| No undefined search-index names | MET (82 named) |
| Stale registry fully refreshed | NOT MET (registry file not rewritten; status report is the sweep authority) |
| Unsupported implementation claims | MET for this sweep (capped; tag claim marked UNVERIFIED) |
| Critical CI failures on Phase-3 subjects | MET (latest product runs success) |
| Critical security | **NOT MET** (Dependabot #13) |
| Duplicate canonicals | **NOT MET** (OS family + workforce forks retained; no deletion) |
| Archive candidates flagged on GitHub | **NOT MET** |
| Dependencies import-mapped | **NOT MET** |
| Docs updated | MET for this report, operator queue, sweep history, pass YAML |

Portfolio residuals remain. Stop. Do not loop.
