# Portfolio Status Report

**Updated:** 2026-10-06 10:18 EDT (Sweep-238)
**Project / Version:** ADL Portfolio Governance / Sweep-238
**Objective:** Master Directive portfolio sweep. Live-verify the four named systems. Record residuals. Do not loop.
**Authenticated owner:** `beyond-repair` (id 132061760). Profile `public_repos` 78. Search `user:beyond-repair` `total_count` 83, `incomplete_results` false.
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user sweep directive. A2 this cycle re-fetched search metadata, main heads, Actions conclusions, releases, tags, and selected security lists for the four named systems. A3 classifications outside those four remain inherited and were not re-audited.

## Sweep-238 result

Exit criteria were not met. Inventory below is retained. Four named systems were re-fetched. No archive flag was flipped. No repository was deleted. No claim was elevated.

Accounting residual: profile `public_repos` 78 versus search total 83. Payload contains 9 private repositories and 0 forks. Equality was not forced.

| Repo | main HEAD | Latest recorded CI on that head | Releases | Tags | Security |
|------|-----------|----------------------------------|----------|------|----------|
| forge-aegis | `e7188d529739652a2dd6264bd3d328c1f72e60e5` | 37258127100 success | empty | empty | Dependabot open empty; code scanning 404 |
| sovereign-clean-room | `4878918cf9f95d3c19e1890bef6d2fd6713e0a16` | 37064696194 success on main | empty | empty | high Dependabot filter empty; secret scanning disabled |
| BlockSwarm | `6e90f6f85c0969fa8a262a70ceba833d618a22db` | 36859452185 success | empty | empty | Dependabot open empty |
| Digital_Double_virtual_workforce | `24e6a29fd26c03900a8d98634d6683996eabdac4` | 36861489156 success | empty | empty | Dependabot critical #13 open; secret scanning open empty |

Readiness: forge-aegis PASS WITH FINDINGS; sovereign-clean-room PASS WITH FINDINGS; BlockSwarm PASS WITH FINDINGS; Digital Double FAIL on unresolved critical Dependabot #13. Local tests were not re-run. Actions success is not a product-complete claim.

## Sweep-236 result

Subject: `The-Origin-Point-Hypothesis.` Classification **RESEARCH**. Claim cap ≤1. Pre-tree `7c669b46534063906b9649ef1e39e8b9acd08211`. Post-tree `43397b19acbbd6e8f5e3ab610868c78fe1458fb6`. Local pytest 4 passed. docs-presence run 37475853468 **success** on that head. Historical PDF not rewritten. No tag. No archive. No license invented. No claim elevation. Portfolio termination not met.

Registry correction: this row is no longer "inherited default; not re-audited".

## Sweep-235 result

Exit criteria were not met. Inventory below is retained from that cycle except the subject row. No archive flag was flipped. No repository was deleted.

Accounting residual: profile `public_repos` 78 versus search total 83. Payload contains 9 private repositories and 0 forks. Equality was not forced.

## Subject verification (Sweep-236)

| Item | State |
|------|--------|
| Classification | RESEARCH |
| Claim cap | ≤1; SPARC and dark-matter elimination UNSUPPORTED |
| Canonical W(n) | not this repo; index token (n-3) retained |
| Historical PDF | retained, unverified, presence-checked |
| CI | docs-presence 37475853468 success |
| License | absent; operator-only |
| Termination | not met for the portfolio |

## Inventory (83)

Class column is Sweep-238 live only for the four named systems. `The-Origin-Point-Hypothesis.` remains Sweep-236. All other classes are inherited and labeled. All other classes are inherited and labeled. GitHub `archived=true` only for `CFT-v3.0`.

| Name | Class (source) | Visibility | Lang | Pushed | GH archived | Open issues |
|------|----------------|------------|------|--------|-------------|-------------|
| `-Entanglement-and-Emergence` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `-Py2APK-main` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `-text-informational-fork-protocol-` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 1 |
| `-ware-constant-derivation` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-03 | False | 0 |
| `acoustic-token-modem` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `adl-capability-matrix` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-03 | False | 0 |
| `adl-function-census` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 1 |
| `ADL-Governance` | ACTIVE (inherited Sweep-225; not re-audited) | public | Python | 2026-10-06 | False | 0 |
| `ADL-Nexus` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 3 |
| `ADL-Portfolio-Census` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-06 | False | 1 |
| `ADL-SEEM` | ACTIVE (inherited Sweep-225; not re-audited) | public | None | 2026-10-02 | False | 0 |
| `AEGIS-Project-Nehemiah-` | ACTIVE (inherited Sweep-225; not re-audited) | public | None | 2026-10-01 | False | 0 |
| `aegis-repo-graph` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-06 | False | 0 |
| `Agent-Snake` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `atomicdreamlabs` | RESEARCH (inherited default; not re-audited) | private | JavaScript | 2026-10-01 | False | 0 |
| `AtomicNexusAI` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-02 | False | 0 |
| `Auto_Legion` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-01 | False | 0 |
| `automate_passive_income` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | None | 2026-10-01 | False | 0 |
| `beyond-repair` | PROFILE (inherited) | public | None | 2026-10-01 | False | 0 |
| `blacksite` | RESEARCH (inherited default; not re-audited) | private | JavaScript | 2026-10-02 | False | 1 |
| `bloch-coherence-factor2` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-01 | False | 0 |
| `BlockSwarm` | ACTIVE (Sweep-238 reconfirmed) | public | Solidity | 2026-10-01 | False | 0 |
| `btc-trading` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `CFT-v3.0` | SUPERSEDED → CFTv3.3-IQG-Unified-Framework (inherited) | private | Python | 2026-10-02 | True | 0 |
| `CFT-v3.1` | SUPERSEDED → CFTv3.3-IQG-Unified-Framework (inherited) | public | TeX | 2026-10-01 | False | 0 |
| `CFTv3.3-IQG-Unified-Framework` | RESEARCH (inherited default; not re-audited) | public | TeX | 2026-09-07 | False | 0 |
| `Code_Generation_AI_Program` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-05 | False | 0 |
| `coherence-drive` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 2 |
| `DevelopTool-Unified-Dev-Environment` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-04 | False | 23 |
| `digital-double-mobile` | SUPERSEDED → Digital_Double_virtual_workforce (inherited) | public | TypeScript | 2026-10-04 | False | 1 |
| `Digital-Double_Mobile` | SUPERSEDED → Digital_Double_virtual_workforce (inherited) | public | None | 2026-10-01 | False | 0 |
| `Digital_Double_virtual_workforce` | ACTIVE (Sweep-238 reconfirmed) | public | TypeScript | 2026-10-01 | False | 5 |
| `Digital_Double_Virtual_Workforce_4.` | SUPERSEDED → Digital_Double_virtual_workforce (inherited) | private | None | 2026-10-02 | False | 0 |
| `Digital_Double_Virtual_Workforce_4.2` | SUPERSEDED → Digital_Double_virtual_workforce (inherited) | private | TypeScript | 2026-10-02 | False | 1 |
| `DigitalDoubleVirtualWorkforce3.5` | SUPERSEDED → Digital_Double_virtual_workforce (inherited) | public | Python | 2026-10-02 | False | 0 |
| `ExoAxis-1` | RESEARCH (inherited default; not re-audited) | public | None | 2026-10-01 | False | 0 |
| `fantom-smart-contracts-first-bot` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Rust | 2026-10-01 | False | 0 |
| `fantom_trading_bot_2` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `finite-gasket-spectral-derivatives` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `forge-aegis` | ACTIVE (Sweep-238 reconfirmed) | public | Python | 2026-10-05 | False | 0 |
| `FortiTrade_Multi-Strategy` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-02 | False | 1 |
| `ftmA.I.bot` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `genieGPT` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | None | 2026-10-01 | False | 0 |
| `Gia---General-Intelligence-Assistant` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-01 | False | 2 |
| `informational-flux-identity` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `LegionOS` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-01 | False | 0 |
| `m2-renormalization-law` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 1 |
| `mend` | RESEARCH (inherited default; not re-audited) | public | JavaScript | 2026-10-01 | False | 0 |
| `mendthegame` | RESEARCH (inherited default; not re-audited) | private | JavaScript | 2026-10-01 | False | 0 |
| `momentum-closure` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 1 |
| `My-mind-A.I.` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-02 | False | 0 |
| `new-program-1.01` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `Open-Energy-Fusion` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-01 | False | 0 |
| `optimization-limit-conjecture` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-04 | False | 0 |
| `os-family-constitution-map` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-01 | False | 0 |
| `potential-garbanzo` | ARCHIVED target (inherited; GitHub flag true only if noted) | private | None | 2026-10-01 | False | 0 |
| `Project-Cold-Boot` | RESEARCH (inherited default; not re-audited) | public | GDScript | 2026-10-02 | False | 0 |
| `quantum_A.I._optimization.py` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-02 | False | 16 |
| `Quantumclustering` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | None | 2026-10-01 | False | 0 |
| `RealityOS` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `RepoRover-` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-05 | False | 0 |
| `scale-functional-I` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `SEEM-2.0-Self-Evolving-Emergent-Mind` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-02 | False | 0 |
| `seem-block-system` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-02 | False | 0 |
| `SEEM-Cognitive-Microservice` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-02 | False | 0 |
| `SEEM-Cognitive_Microservice` | SUPERSEDED → sovereign-clean-room (inherited) | public | Python | 2026-10-02 | False | 2 |
| `seem-identity-unifier` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-01 | False | 0 |
| `seem-sunder-bridge` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-03 | False | 1 |
| `sierpinski-geometry-045` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `smart_home_BCI` | ARCHIVED target (inherited; GitHub flag true only if noted) | public | Python | 2026-10-01 | False | 0 |
| `sovereign-clean-room` | ACTIVE (Sweep-238 reconfirmed) | public | Python | 2026-10-04 | False | 2 |
| `Sovereign-Epistemic-Reality-Engine` | RESEARCH (inherited default; not re-audited) | public | None | 2026-10-01 | False | 0 |
| `Sovereign-OS` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-09-20 | False | 0 |
| `SovereignOS` | RESEARCH (inherited default; not re-audited) | private | Python | 2026-10-01 | False | 0 |
| `stress-tensor-modification` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 2 |
| `sunder` | RESEARCH (Sweep-233 re-audit; claim ≤1; not re-tested this cycle) | public | Python | 2026-10-06 | False | 1 |
| `sunder-cleanroom-vsa-adapter` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |
| `test` | ARCHIVED target (inherited; GitHub flag true only if noted) | private | None | 2026-10-01 | False | 0 |
| `The-Origin-Point-Hypothesis.` | RESEARCH (Sweep-236 re-audit; claim ≤1) | public | TeX | 2026-10-06 | False | 0 |
| `thrust-target-30` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-01 | False | 0 |
| `topological-pinch` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 1 |
| `VigilE.S.A.-Enhanced-Security` | RESEARCH (inherited default; not re-audited) | public | Rust | 2026-10-02 | False | 0 |
| `ware-constant-phenomenology` | RESEARCH (inherited default; not re-audited) | public | Python | 2026-10-02 | False | 0 |

Sweep-238 stop. Exit criteria not met. Do not loop.
