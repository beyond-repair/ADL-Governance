# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-170)

- Apply GitHub `archived=true` flag to documented ARCHIVED/SUPERSEDED targets: genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, **-Py2APK-main**, **fantom_trading_bot_2**, **Digital_Double_Virtual_Workforce_4.**, Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, **CFT-v3.1**, **Agent-Snake**, **SEEM-Cognitive_Microservice**, **SEEM-Cognitive-Microservice** (hyphen; Sweep-169 re-confirm, still `archived=false`), **btc-trading**, and remaining queue entries in archive_queue.md / repository_registry.md.
- Tag product releases on ACTIVE repos (BlockSwarm v0.5.0-sagf, forge-aegis v0.1.0, Digital_Double_virtual_workforce, **sovereign-clean-room v1.3.x**, etc.). Live re-verify Sweep-168: all four named targets still have **zero releases**.
- Rotate / remove committed `.env` on digital-double-mobile; resolve Dependabot HIGH alerts.
- Expand adl-capability-matrix to live 82-row census (currently locked 67; OPEN but claim-capped).
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent.
- Optional: remove or LFS-migrate large committed model weight in Digital_Double_Virtual_Workforce_4.2 (hygiene only; do not delete without operator decision).
- Review/merge open Dependabot PRs #3/#4/#5/#6 and draft evidence PR #7 on Digital_Double_virtual_workforce (still open at Sweep-168).
- Audit remaining unlisted census names (default RESEARCH): atomicdreamlabs, bloch-coherence-factor2, mendthegame. mend closed Sweep-170. informational-flux-identity closed Sweep-168. finite-gasket-spectral-derivatives closed Sweep-167.

## Residual notes from recent sweeps

- Sweep-170: mend RESEARCH lock (CLAIM_STATUS + dependency-free formula witness; local node test 1/1; witness does not import formulas.ts; Actions not run; npm test not run). No archive/release action. mendthegame not read (private).
- Sweep-169: SEEM-Cognitive-Microservice SUPERSEDED re-confirm (docs only at 56c7aae; no product mutation; GitHub archive flag still PENDING). Placeholder API key in seem.py is not a committed live secret.
- Sweep-168: informational-flux-identity RESEARCH lock (local witness 349/366 signed net 0; tests + workflow pushed at 54fe690; Actions not observed). Phase 3: four named ACTIVE targets CI success, releases empty. No archive/release action.
- Sweep-167: finite-gasket-spectral-derivatives RESEARCH lock (kernel tests + claim table; free mult(6) remains CLAIMED prose; Actions not observed). No archive/release action.
- Sweep-166: Digital_Double_Virtual_Workforce_4. SUPERSEDED re-confirm (private; governance docs only; README empty-ref claim corrected; SUPERSEDED.md + CLAIM_STATUS.md added at 12798ac; no product mutation); GitHub archive flag still PENDING.
- Sweep-165: btc-trading ARCHIVED re-confirm (README + ARCHIVED.md + SECURITY.md terminal, claim 0, hardcoded historical key noted; no subject mutation); GitHub archive flag still PENDING (already in archive_queue.md).

Update this file only when residual operator work changes.
