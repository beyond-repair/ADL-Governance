# Repository Registry

**Account:** beyond-repair · **Census date:** 2026-08-28 (Sweep-029) · **Governing source:** this repository

Visible GitHub search count: 60. Classifications: ACTIVE | RESEARCH | FROZEN | SUPERSEDED | ARCHIVED.
Maturity 1–5: Incomplete → Production Ready. Claim levels 0–5 per CLAIM_VALIDATION.md.

---

## ACTIVE

| Name | Lang | Last update | Issues | Maturity | Notes |
|------|------|-------------|--------|----------|-------|
| [BlockSwarm](https://github.com/beyond-repair/BlockSwarm) | Solidity | 2026-08-24 | 0 | 4 | SAGF; CI green (32707027387); tag v0.5.0-sagf PENDING |
| [sovereign-clean-room](https://github.com/beyond-repair/sovereign-clean-room) | Python | 2026-08-24 | 0 | 2* | Canonical SEEM substrate; **CI red** (missing VSA b64 5–7). Maturity suspended. Medium Dependabot: PyNaCl. |
| [forge-aegis](https://github.com/beyond-repair/forge-aegis) | Python | 2026-08-24 | 0 | 2 | FLS early; CI 6/6 green; v0.1.0 open |
| [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) | Docs | 2026-08-28 | 0 | 3 | This repo |
| [AEGIS-Project-Nehemiah-](https://github.com/beyond-repair/AEGIS-Project-Nehemiah-) | — | 2026-08-24 | 0 | 2 | Spec sibling to forge-aegis |
| [Digital_Double_virtual_workforce](https://github.com/beyond-repair/Digital_Double_virtual_workforce) | TS | 2026-08-24 | 1 | 3 | Public canonical; product CI **32707099628 success** |

\* Do not treat sovereign-clean-room as maturity 4 while CI is red.

---

## RESEARCH (Claim level ≤ 2)

| Name | Maturity | Claim level (default) | Notes |
|------|----------|----------------------|-------|
| coherence-drive | 3 | 1 | Master physics index |
| ware-constant-phenomenology | 3 | 1–2 | |
| -ware-constant-derivation | 2 | 1 | |
| CFTv3.3-IQG-Unified-Framework | 2 | 1 | Prefer over CFT-v3.x |
| CFT-v3.1 | 2 | 1 | Prefer 3.3 |
| momentum-closure | 2 | 1 | Satellite |
| stress-tensor-modification | 2 | 1 | Satellite |
| m2-renormalization-law | 2 | 1 | Satellite |
| topological-pinch | 2 | 1 | Satellite |
| thrust-target-30 | 2 | 1 | Engineering *target*, not Level 5 |
| sierpinski-geometry-045 | 2 | 1 | Geometry |
| -Entanglement-and-Emergence | 2 | 0–1 | |
| -text-informational-fork-protocol- | 2 | 0–1 | |
| The-Origin-Point-Hypothesis. | 2 | 0–1 | |
| optimization-limit-conjecture | 2 | 1 | |
| acoustic-token-modem | 2 | 0–1 | Measurement gate explicit |
| RealityOS | 1 | 0–1 | Decision-infra concept; no Level-5 |
| LegionOS | 1 | 0–1 | Company holarchy concept |
| Sovereign-OS | 1 | 0–1 | Public constitutional OS sketch |
| SovereignOS | 1 | 0–1 | Private sibling; consolidate |

**Canonical Ware law:** `W(n)=0.08*exp(0.23*(n-3))`

**Not claimed:** experimental thrust, energy extraction, AGI-in-a-box, production OS autonomy.

---

## SUPERSEDED

| Name | Successor |
|------|-----------|
| SEEM-2.0-Self-Evolving-Emergent-Mind | sovereign-clean-room |
| SEEM-Cognitive-Microservice | sovereign-clean-room |
| SEEM-Cognitive_Microservice | sovereign-clean-room |
| seem-block-system | sovereign-clean-room (docs absorbed) |
| My-mind-A.I. | sovereign-clean-room (TaskAtom / Episode patterns) |
| Gia---General-Intelligence-Assistant | sovereign-clean-room (CapabilityRegistry patterns) |
| Auto_Legion | sovereign-clean-room (atomic work-unit concept) |
| CFT-v3.0 | CFTv3.3-IQG-Unified-Framework (already GitHub-archived) |

---

## FROZEN / product (select or archive)

| Name | Maturity | Action |
|------|----------|--------|
| Digital_Double_Virtual_Workforce_4.2 | 2 | Private newer candidate; merge value into public canonical or keep isolated |
| DigitalDoubleVirtualWorkforce3.5 | 2 | Archive after verify |
| Digital_Double_Virtual_Workforce_4. | 1 | Archive |
| Digital-Double_Mobile / digital-double-mobile | 1–2 | Archive unless mobile surface revived |
| FortiTrade_Multi-Strategy | 2 | Isolate; archive |
| VigilE.S.A.-Enhanced-Security | 2 | Hardening ideas noted for AEGIS; freeze or archive |

---

## ARCHIVED (target / recommended)

| Name | Reason |
|------|--------|
| CFT-v3.0 | Already archived |
| RepoRover- | Dormant utility |
| DevelopTool-Unified-Dev-Environment | Stub; many stale issues |
| -Py2APK-main | One-off |
| AtomicNexusAI, genieGPT, Agent-Snake | Experiments |
| fantom_trading_bot_2, fantom-smart-contracts-first-bot, ftmA.I.bot | Old bots |
| smart_home_BCI, automate_passive_income, Quantumclustering | Dormant |
| quantum_A.I._optimization.py | Stale |
| test | Empty private stub |
| new-program-1.01, btc-trading, Code_Generation_AI_Program | Dormant |
| potential-garbanzo | Empty private stub |

---

## Profile

| Name | Notes |
|------|-------|
| beyond-repair | Profile README — point at canonical ACTIVE set |

---

## Relationship map (Stage-1 active boundary)

```text
ADL-Governance (policy · claims · lifecycle)
    ├── sovereign-clean-room (ACTIVE, CI-blocked) ←── SEEM-* + My-mind + Gia patterns
    ├── BlockSwarm (ACTIVE, tag pending)
    ├── forge-aegis (ACTIVE) ↔ AEGIS-Project-Nehemiah-
    ├── Digital_Double_virtual_workforce (ACTIVE product, CI green)
    ├── coherence-drive (RESEARCH ≤2) ←── Ware/CFT satellites
    └── RealityOS / LegionOS / Sovereign-OS* (RESEARCH; consolidate)
```
