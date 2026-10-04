# Portfolio Status Report

**Updated:** 2026-10-04 (Sweep-220)
**Project / Version:** ADL Portfolio Governance / Sweep-220
**Objective:** One governed discovery and live-verification sweep. Do not delete, rewrite history, or elevate claims.
**Authenticated owner:** `beyond-repair` (id 132061760)
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user sweep contract. A2 GitHub search (`total_count` 83, `incomplete_results` false), Actions, releases API, Dependabot, secret scanning, public tags pages. A3 classifications inherited from `docs/repository_registry.md` for names not re-read this sweep.

## Census

| Field | Value |
|-------|--------|
| Search `user:beyond-repair` | 83, incomplete_results false |
| User object `public_repos` | 78 |
| Private in search payload | 9 |
| GitHub `archived=true` | `CFT-v3.0` only |
| Accounting residual | 78 public + 9 private = 87, not 83. Not resolved. |

Private names observed: `Digital_Double_Virtual_Workforce_4.2`, `CFT-v3.0`, `Digital_Double_Virtual_Workforce_4.`, `blacksite`, `potential-garbanzo`, `SovereignOS`, `test`, `mendthegame`, `atomicdreamlabs`.

## Phase 3 — live verification

Releases API returned an empty list for all four. Public `/tags` pages rendered "There aren't any releases here". Lightweight tags were not separately enumerated.

| Repo | Main head | CI on main | Releases | Secret scanning | Dependabot open critical | Code scanning | Readiness |
|------|-----------|------------|----------|-----------------|--------------------------|---------------|-----------|
| forge-aegis | `590ba108c93a2de04ed8f2390f68cf6353645b1c` | forge-aegis CI run 37065566958 success (2026-10-02) | none | open list empty | open list empty | 404 no analysis | PASS WITH FINDINGS |
| sovereign-clean-room | `4878918cf9f95d3c19e1890bef6d2fd6713e0a16` | Python tests run 37064696194 success (2026-10-02) | none | 404 disabled | critical open empty | not re-listed | PASS WITH FINDINGS |
| BlockSwarm | `6e90f6f85c0969fa8a262a70ceba833d618a22db` | Foundry run 36859452185 success (2026-10-01) | none | open list empty | open list empty | not re-listed | PASS WITH FINDINGS |
| Digital_Double_virtual_workforce | `24e6a29fd26c03900a8d98634d6683996eabdac4` | Digital Double CI run 36861489156 success (2026-10-01) | none | open list empty | #13 open | 404 no analysis | FAIL |

`sovereign-clean-room` branches still present: `main` `4878918c`, `seem-completion-pass` `d6f13042f4f99cd186761ae438b75c3e4e705f11`, `fix/pynacl-1.6.2-cve-2025-69277` `f65d7db6c4f7d98ed3f5ded3defd5d1886c21cc4`. PR #3 Python tests run 37215829476 success. Not merged. VSA completeness remains UNVERIFIED.

Digital Double alert #13: `form-data`, manifest `digital_double/package-lock.json`, scope development, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, matched range `>= 4.0.0, < 4.0.4`, first patched identifier 4.0.4. Not bumped.

## Capability matrix (demonstrated vs planned)

Only code or CI observed this sweep is VERIFIED. Inherited product claims stay capped.

```
Feature | State
forge-aegis offline pipeline + pytest CI on main 590ba108 | VERIFIED
forge-aegis host attestation / auto-remediation | PLANNED
sovereign-clean-room Python tests on main 4878918c | VERIFIED
sovereign-clean-room VSA completeness / production twin | UNVERIFIED
BlockSwarm Foundry workflow on main 6e90f6f | VERIFIED
BlockSwarm production chain deployment | UNVERIFIED
Digital Double CI on main 24e6a29 | VERIFIED
Digital Double dependency-clean release | PLANNED
Product SemVer releases for the four subjects | UNVERIFIED
```

forge-aegis tree at `590ba108` (45 entries, not truncated) contains `python/aegis_pipeline.py`, `python/aegis_validator.py`, `python/tests/test_pipeline.py`, `python/tests/test_validator.py`, FLS notes, and `docs/V0_1_VERTICAL_SLICE.md`. That is a software slice, not a measured host integrity platform.

## Classification

Exactly one class per name. A3 inherited except the four live subjects.

**ACTIVE:** `ADL-Governance`, `ADL-SEEM`, `AEGIS-Project-Nehemiah-`, `BlockSwarm`, `Digital_Double_virtual_workforce`, `forge-aegis`, `sovereign-clean-room`.

**SUPERSEDED:** `SEEM-2.0-Self-Evolving-Emergent-Mind`, `SEEM-Cognitive-Microservice`, `SEEM-Cognitive_Microservice`, `seem-block-system`, `My-mind-A.I.`, `Gia---General-Intelligence-Assistant`, `Auto_Legion` (successor `sovereign-clean-room`); `CFT-v3.0`, `CFT-v3.1` (successor `CFTv3.3-IQG-Unified-Framework` / ware phenomenology); `DigitalDoubleVirtualWorkforce3.5`, `Digital_Double_Virtual_Workforce_4.`, `Digital_Double_Virtual_Workforce_4.2`, `Digital-Double_Mobile`, `digital-double-mobile` (successor `Digital_Double_virtual_workforce`).

**ARCHIVED (recommended; GitHub flag false except `CFT-v3.0`):** `RepoRover-`, `DevelopTool-Unified-Dev-Environment`, `-Py2APK-main`, `AtomicNexusAI`, `genieGPT`, `Agent-Snake`, `fantom_trading_bot_2`, `fantom-smart-contracts-first-bot`, `ftmA.I.bot`, `smart_home_BCI`, `automate_passive_income`, `Quantumclustering`, `quantum_A.I._optimization.py`, `test`, `new-program-1.01`, `btc-trading`, `Code_Generation_AI_Program`, `potential-garbanzo`, `FortiTrade_Multi-Strategy`.

**RESEARCH (remainder, claim-capped):** `optimization-limit-conjecture`, `-ware-constant-derivation`, `adl-capability-matrix`, `seem-sunder-bridge`, `sunder-cleanroom-vsa-adapter`, `adl-function-census`, `finite-gasket-spectral-derivatives`, `aegis-repo-graph`, `ADL-Portfolio-Census`, `sunder`, `Project-Cold-Boot`, `RealityOS`, `acoustic-token-modem`, `informational-flux-identity`, `coherence-drive`, `stress-tensor-modification`, `sierpinski-geometry-045`, `momentum-closure`, `topological-pinch`, `m2-renormalization-law`, `ware-constant-phenomenology`, `-text-informational-fork-protocol-`, `-Entanglement-and-Emergence`, `scale-functional-I`, `VigilE.S.A.-Enhanced-Security`, `ADL-Nexus`, `bloch-coherence-factor2`, `mend`, `blacksite`, `seem-identity-unifier`, `os-family-constitution-map`, `SovereignOS`, `Open-Energy-Fusion`, `LegionOS`, `beyond-repair`, `atomicdreamlabs`, `Sovereign-Epistemic-Reality-Engine`, `ExoAxis-1`, `thrust-target-30`, `Sovereign-OS`, `The-Origin-Point-Hypothesis.`, `CFTv3.3-IQG-Unified-Framework`, `mendthegame`.

## Dependency and redundancy

Internal (documented, not re-resolved from lockfiles this sweep):

- `ADL-SEEM` → `ADL-Governance`
- `sovereign-clean-room` ← superseded SEEM-* names
- `Digital_Double_virtual_workforce` ← Digital Double version and mobile names
- `forge-aegis` ↔ `AEGIS-Project-Nehemiah-` (spec sibling; not a proven import)
- `sunder-cleanroom-vsa-adapter` / `seem-sunder-bridge` name `sunder` and `sovereign-clean-room` (interop UNVERIFIED)
- `BlockSwarm` → OpenZeppelin / forge-std (submodules documented on main; not re-cloned)

No new dependency cycle was proven. Duplicate surfaces remain the Digital Double lineage, SEEM lineage, OS-family names (`RealityOS`, `LegionOS`, `Sovereign-OS`, `SovereignOS`), and CFT version chain. Action is SUPERSEDE or RESEARCH, not delete.

## Gap summary

| Capability | Severity |
|------------|----------|
| Digital Double Dependabot #13 open | Critical |
| digital-double-mobile secret alert #1 and Dependabot #30/#8 (prior sweep; not re-closed) | Critical |
| Secret scanning disabled on sovereign-clean-room | High |
| No product release for the four ACTIVE subjects | Medium |
| GitHub archive flags false for recommended ARCHIVED set | Medium |
| `public_repos` 78 vs search 83 | Low |
| Code scanning absent on forge-aegis and Digital Double | Medium |

## Canonical ownership

| Domain | Canonical | Not canonical |
|--------|-----------|----------------|
| Governance | ADL-Governance | census/matrix repos are indexes |
| SEEM rules | ADL-SEEM | — |
| Agent / VSA substrate | sovereign-clean-room | SEEM-* , sunder |
| Endpoint integrity spec/slice | forge-aegis + AEGIS-Project-Nehemiah- | not a host product |
| Distributed / SAGF | BlockSwarm | — |
| Workforce | Digital_Double_virtual_workforce | versioned and mobile copies |
| Research physics | coherence-drive / CFTv3.3 | CFT-v3.0, CFT-v3.1 |

## Exit

Criteria failed. Critical security findings remain open. Archive candidates are not GitHub-archived. Duplicate lineages are classified but not operator-archived. No unsupported completion claim was added. Sweep stopped.
