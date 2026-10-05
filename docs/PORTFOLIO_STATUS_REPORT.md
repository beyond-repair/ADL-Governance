# Portfolio Status Report

**Updated:** 2026-10-05 (Sweep-226)
**Project / Version:** ADL Portfolio Governance / Sweep-226
**Objective:** Random repository completion cycle on `Code_Generation_AI_Program`.
**Authenticated owner:** `beyond-repair` (id 132061760)
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user Master Directive v3.0. A2 GitHub search `user:beyond-repair` (`total_count` 83, `incomplete_results` false) plus Actions, releases, tags, branches, Dependabot, secret-scanning, and code-scanning API reads on 2026-10-05. A3 classifications outside the Phase-3 set are inherited from the registry and prior sweeps; they were not re-proven from trees this cycle.

## Sweep-226 subject

| Field | Value |
|-------|--------|
| Repo | `Code_Generation_AI_Program` |
| Visibility | public |
| Default branch | `main` |
| Pre-tree | `63d47ab0b912aef754bc6cc32b43b87234cb699a` (1 blob, `README.md`, not truncated) |
| Workflow commit | `f362a9612971503f07e0599247f2e3708ef36809` |
| Classification | **ARCHIVED** (recommended; reconfirmed) |
| Claim | 0 |
| Successor | none |
| GitHub archived | false |
| Local tests | pytest 2 passed |
| CI | inventory run 37386093314 success on `f362a961` |
| Releases / tags | not created |

No generator, model, dataset, API client, or dependency manifest was present before this sweep. Inventory test and CI added. Not tagged. Not archived. Not promoted.

## Census

- Search inventory: **83** repositories (74 public, 9 private).
- Profile `public_repos`: **78**. Difference is not resolved by deletion. Residual accounting gap.
- GitHub `archived=true`: **only** `CFT-v3.0`.
- Forks in this search set: 0.
- Classifications this sweep (exactly one each; CFT-v3.0 counted ARCHIVED and noted as superseded by `CFTv3.3-IQG-Unified-Framework`): ACTIVE 7, RESEARCH 43, SUPERSEDED 13, ARCHIVED 20.

Inherited classifications were not re-audited repository-by-repository. Label: `UNVERIFIED` outside Phase-3 and the Sweep-223 `RepoRover-` subject.

## Phase-3 live verification

| Repo | Main head | CI (this fetch) | Releases | Tags | Dependabot open | Secret scanning | Code scanning | Readiness |
|------|-----------|-----------------|----------|------|-----------------|-----------------|---------------|-----------|
| forge-aegis | `e7188d529739652a2dd6264bd3d328c1f72e60e5` | forge-aegis CI run 37258127100 success (push, 2026-10-05) | empty | empty | empty | not requested as a finding this cycle | 404 no analysis | PASS WITH FINDINGS |
| sovereign-clean-room | `4878918cf9f95d3c19e1890bef6d2fd6713e0a16` | Python tests run 37064696194 success on main (2026-10-02). Branch `seem-completion-pass` run 37215829476 success, not merged | empty | empty | empty | API 404 disabled | not re-listed | PASS WITH FINDINGS |
| BlockSwarm | `6e90f6f85c0969fa8a262a70ceba833d618a22db` | Foundry run 36859452185 success on main (2026-10-01) | empty | empty | empty | open list empty | 404 no analysis | PASS WITH FINDINGS |
| Digital_Double_virtual_workforce | `24e6a29fd26c03900a8d98634d6683996eabdac4` | Digital Double CI run 36861489156 success on main (2026-10-01) | empty | empty | critical #13 open; first page also 8 high / 11 medium / 1 low and `hasNextPage` true | open list empty | not listed | FAIL |

No local pytest was executed this cycle. CI conclusions are Actions API conclusions, not a re-run of the suite in this environment. VSA completeness on `sovereign-clean-room` remains `UNVERIFIED`. forge-aegis remains a software / runnable sketch, not a host-integrity product.

## Capability matrix (demonstrated vs planned)

| Feature | State |
|---------|--------|
| forge-aegis offline pipeline + validator tests in CI | VERIFIED (Actions success on `e7188d5`; tree contains `python/aegis_pipeline.py`, `python/tests/`) |
| forge-aegis host measurement, remote attestation, auto-remediation | PLANNED / not claimed |
| sovereign-clean-room Python tests on main | VERIFIED (run 37064696194 success) |
| sovereign-clean-room full VSA / mind / production kernel | UNVERIFIED |
| BlockSwarm Foundry build/test on pinned forge-std and OpenZeppelin submodules | VERIFIED (run 36859452185 success) |
| BlockSwarm mainnet security or autonomous treasury | PLANNED / out of scope |
| Digital Double installable Python core and CI | VERIFIED (run 36861489156 success) |
| Digital Double production workforce / OmniWealth execution | UNVERIFIED |
| Mapping repos (census, capability matrix, function census, repo graph, bridges) | Claim-capped; runtime interop UNVERIFIED |

## Dependency graph (internal, governance-level)

- `ADL-SEEM` → canonical runtime `sovereign-clean-room` (docs contract; not a package import verified this cycle).
- SEEM-* and `Auto_Legion`, `My-mind-A.I.`, `Gia---General-Intelligence-Assistant` → superseded by `sovereign-clean-room`.
- Digital Double versioned and mobile repos → superseded by `Digital_Double_virtual_workforce`.
- `AEGIS-Project-Nehemiah-` spec sibling of `forge-aegis` (not a verified runtime dependency).
- `BlockSwarm` documents advice from Digital Double; no verified on-chain call path this cycle.
- Mapping layer (`ADL-Portfolio-Census`, `aegis-repo-graph`, `adl-capability-matrix`, `adl-function-census`, `seem-sunder-bridge`, `sunder-cleanroom-vsa-adapter`) is claim-capped. No runtime interop claim.
- External: forge-aegis Python; sovereign-clean-room Python/NumPy; BlockSwarm Solidity/Foundry plus forge-std v1.9.4 and OpenZeppelin v4.9.6 submodules (documented, not re-cloned); Digital Double Python plus npm lockfile under `digital_double/`.
- Cycle check this sweep: no verified import cycle. Duplicate workforce and SEEM trees remain historical, not a second canonical.

## Security summary

- Digital Double Dependabot **critical #13** still open: `form-data` GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, development scope, matched range `>= 4.0.0, < 4.0.4`, patched identifier 4.0.4. Not patched.
- Same repo first open page (20 alerts, next page exists): high includes `js-yaml` GHSA-2883-xcg3-v3hh (#160, #159), `browserslist` GHSA-73wf-gq98-2v4g (#155), `nanoid` GHSA-xwg4-73v4-xw9w (#153, #147), `brace-expansion` GHSA-3jxr-9vmj-r5cp (#122), `js-yaml` GHSA-5p4m-2wfm-xmqj (#112, #111). Not an exhaustive open-alert census.
- forge-aegis and BlockSwarm Dependabot open lists empty. sovereign-clean-room Dependabot open list empty.
- digital-double-mobile secret scanning alert #1 was not re-fetched this cycle. Prior operator item stands. Do not treat absence of `.env` as rotation. Secret material is not copied into this report.
- sovereign-clean-room secret scanning remains disabled (API 404).

## Gap summary

| Capability | Severity |
|------------|----------|
| Unresolved critical Dependabot #13 on canonical Digital Double | Critical |
| digital-double-mobile secret alert #1 not closed (prior evidence; not re-fetched) | Critical (operator) |
| GitHub archive flags false for ARCHIVED recommendations | Medium |
| No product tags/releases on the four Phase-3 repos | Medium |
| Code scanning absent on forge-aegis and BlockSwarm | Medium |
| Secret scanning disabled on sovereign-clean-room | Medium |
| Duplicate historical implementations retained | Low (required; no deletion) |
| Profile public_repos 78 vs search 83 | Low |

## Canonical ownership

| Domain | Canonical | Not canonical |
|--------|-----------|----------------|
| Governance | ADL-Governance | profile README `beyond-repair` |
| SEEM / clean-room | sovereign-clean-room | SEEM-* , Auto_Legion, My-mind-A.I., Gia |
| AEGIS software slice | forge-aegis | AEGIS-Project-Nehemiah- is spec sibling, not a second runtime |
| Distributed advice substrate | BlockSwarm | — |
| Workforce product | Digital_Double_virtual_workforce | 3.5 / 4 / 4.2 / mobile trees |
| Coherence research | coherence-drive index plus claim-capped satellites | CFT-v3.0 archived; CFT-v3.1 superseded |

## Inventory

Evidence label for non-Phase-3 rows: inherited classification, metadata re-read 2026-10-05 (name, visibility, language, pushed_at, GitHub archived flag). Tree, CI, and tests not re-read.

| Name | Class | Domain | Lang | Pushed | Visibility | GitHub archive flag |
|------|-------|--------|------|--------|------------|---------------------|
| `-Entanglement-and-Emergence` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `-Py2APK-main` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `-text-informational-fork-protocol-` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `-ware-constant-derivation` | RESEARCH | Research | Python | 2026-10-03 | public | flag-false |
| `acoustic-token-modem` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `adl-capability-matrix` | RESEARCH | Governance | Python | 2026-10-03 | public | flag-false |
| `adl-function-census` | RESEARCH | Governance | Python | 2026-10-02 | public | flag-false |
| `ADL-Governance` | ACTIVE | Governance | Python | 2026-10-05 | public | flag-false |
| `ADL-Nexus` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `ADL-Portfolio-Census` | RESEARCH | Governance | Python | 2026-10-02 | public | flag-false |
| `ADL-SEEM` | ACTIVE | Governance | — | 2026-10-02 | public | flag-false |
| `AEGIS-Project-Nehemiah-` | ACTIVE | Agent Infrastructure | — | 2026-10-01 | public | flag-false |
| `aegis-repo-graph` | RESEARCH | Governance | Python | 2026-10-02 | public | flag-false |
| `Agent-Snake` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `atomicdreamlabs` | RESEARCH | Research | JavaScript | 2026-10-01 | private | flag-false |
| `AtomicNexusAI` | ARCHIVED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `Auto_Legion` | SUPERSEDED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `automate_passive_income` | ARCHIVED | Unassigned | — | 2026-10-01 | public | flag-false |
| `beyond-repair` | RESEARCH | Governance | — | 2026-10-01 | public | flag-false |
| `blacksite` | RESEARCH | Research | JavaScript | 2026-10-02 | private | flag-false |
| `bloch-coherence-factor2` | RESEARCH | Research | Python | 2026-10-01 | public | flag-false |
| `BlockSwarm` | ACTIVE | Distributed Systems | Solidity | 2026-10-01 | public | flag-false |
| `btc-trading` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `CFT-v3.0` | ARCHIVED | Unassigned | Python | 2026-10-02 | private | github-archived |
| `CFT-v3.1` | SUPERSEDED | Unassigned | TeX | 2026-10-01 | public | flag-false |
| `CFTv3.3-IQG-Unified-Framework` | RESEARCH | Research | TeX | 2026-09-07 | public | flag-false |
| `Code_Generation_AI_Program` | ARCHIVED | Unassigned | Python | 2026-10-05 | public | flag-false |
| `coherence-drive` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `DevelopTool-Unified-Dev-Environment` | ARCHIVED | Unassigned | Python | 2026-10-04 | public | flag-false |
| `digital-double-mobile` | SUPERSEDED | Unassigned | TypeScript | 2026-10-04 | public | flag-false |
| `Digital-Double_Mobile` | SUPERSEDED | Unassigned | — | 2026-10-01 | public | flag-false |
| `Digital_Double_virtual_workforce` | ACTIVE | Workforce Automation | TypeScript | 2026-10-01 | public | flag-false |
| `Digital_Double_Virtual_Workforce_4.` | SUPERSEDED | Unassigned | — | 2026-10-02 | private | flag-false |
| `Digital_Double_Virtual_Workforce_4.2` | SUPERSEDED | Unassigned | TypeScript | 2026-10-02 | private | flag-false |
| `DigitalDoubleVirtualWorkforce3.5` | SUPERSEDED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `ExoAxis-1` | RESEARCH | Research | — | 2026-10-01 | public | flag-false |
| `fantom-smart-contracts-first-bot` | ARCHIVED | Unassigned | Rust | 2026-10-01 | public | flag-false |
| `fantom_trading_bot_2` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `finite-gasket-spectral-derivatives` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `forge-aegis` | ACTIVE | Agent Infrastructure | Python | 2026-10-05 | public | flag-false |
| `FortiTrade_Multi-Strategy` | ARCHIVED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `ftmA.I.bot` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `genieGPT` | ARCHIVED | Unassigned | — | 2026-10-01 | public | flag-false |
| `Gia---General-Intelligence-Assistant` | SUPERSEDED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `informational-flux-identity` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `LegionOS` | RESEARCH | Research | Python | 2026-10-01 | public | flag-false |
| `m2-renormalization-law` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `mend` | RESEARCH | Research | JavaScript | 2026-10-01 | public | flag-false |
| `mendthegame` | RESEARCH | Research | JavaScript | 2026-10-01 | private | flag-false |
| `momentum-closure` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `My-mind-A.I.` | SUPERSEDED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `new-program-1.01` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `Open-Energy-Fusion` | RESEARCH | Research | Python | 2026-10-01 | public | flag-false |
| `optimization-limit-conjecture` | RESEARCH | Research | Python | 2026-10-04 | public | flag-false |
| `os-family-constitution-map` | RESEARCH | Governance | Python | 2026-10-01 | public | flag-false |
| `potential-garbanzo` | ARCHIVED | Unassigned | — | 2026-10-01 | private | flag-false |
| `Project-Cold-Boot` | RESEARCH | Research | GDScript | 2026-10-02 | public | flag-false |
| `quantum_A.I._optimization.py` | ARCHIVED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `Quantumclustering` | ARCHIVED | Unassigned | — | 2026-10-01 | public | flag-false |
| `RealityOS` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `RepoRover-` | ARCHIVED | Unassigned | Python | 2026-10-05 | public | flag-false |
| `scale-functional-I` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `SEEM-2.0-Self-Evolving-Emergent-Mind` | SUPERSEDED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `seem-block-system` | SUPERSEDED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `SEEM-Cognitive-Microservice` | SUPERSEDED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `SEEM-Cognitive_Microservice` | SUPERSEDED | Unassigned | Python | 2026-10-02 | public | flag-false |
| `seem-identity-unifier` | RESEARCH | Governance | Python | 2026-10-01 | public | flag-false |
| `seem-sunder-bridge` | RESEARCH | Research | Python | 2026-10-03 | public | flag-false |
| `sierpinski-geometry-045` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `smart_home_BCI` | ARCHIVED | Unassigned | Python | 2026-10-01 | public | flag-false |
| `sovereign-clean-room` | ACTIVE | Security / Clean-Room | Python | 2026-10-04 | public | flag-false |
| `Sovereign-Epistemic-Reality-Engine` | RESEARCH | Research | — | 2026-10-01 | public | flag-false |
| `Sovereign-OS` | RESEARCH | Research | Python | 2026-09-20 | public | flag-false |
| `SovereignOS` | RESEARCH | Research | Python | 2026-10-01 | private | flag-false |
| `stress-tensor-modification` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `sunder` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `sunder-cleanroom-vsa-adapter` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `test` | ARCHIVED | Unassigned | — | 2026-10-01 | private | flag-false |
| `The-Origin-Point-Hypothesis.` | RESEARCH | Research | TeX | 2026-09-07 | public | flag-false |
| `thrust-target-30` | RESEARCH | Research | Python | 2026-10-01 | public | flag-false |
| `topological-pinch` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |
| `VigilE.S.A.-Enhanced-Security` | RESEARCH | Security | Rust | 2026-10-02 | public | flag-false |
| `ware-constant-phenomenology` | RESEARCH | Research | Python | 2026-10-02 | public | flag-false |

## Exit

Sweep-226 subject slice documented and claim-capped. Local tests passed. CI run 37386093314 success. Not tagged. Not archived. Not promoted.

Phase-3 verified. Inventory has no undefined name in the 83-set. Exit criteria **not** met: critical Dependabot #13 open; archive flags unresolved; no product releases on canonical four; duplicate historical trees retained by rule; secret-scanning residual. Stop. Do not loop.
