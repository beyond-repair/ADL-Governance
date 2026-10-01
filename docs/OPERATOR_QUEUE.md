# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-167)

- Apply GitHub `archived=true` flag to documented ARCHIVED/SUPERSEDED targets: genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, **-Py2APK-main**, **fantom_trading_bot_2**, **Digital_Double_Virtual_Workforce_4.**, Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, **CFT-v3.1**, **Agent-Snake**, **SEEM-Cognitive_Microservice**, **btc-trading**, and remaining queue entries in archive_queue.md / repository_registry.md.
- Tag product releases on ACTIVE repos (BlockSwarm v0.5.0-sagf, forge-aegis v0.1.0, Digital_Double_virtual_workforce, **sovereign-clean-room v1.3.x**, etc.).
- Rotate / remove committed `.env` on digital-double-mobile; resolve Dependabot HIGH alerts.
- Expand adl-capability-matrix to live 82-row census (currently locked 67; OPEN but claim-capped).
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent.
- Optional: remove or LFS-migrate large committed model weight in Digital_Double_Virtual_Workforce_4.2 (hygiene only; do not delete without operator decision).
- Review/merge open Dependabot PRs #3/#4/#5/#6 and draft evidence PR #7 on Digital_Double_virtual_workforce.
- Audit remaining unlisted census names (default RESEARCH): atomicdreamlabs, bloch-coherence-factor2, informational-flux-identity, mend, mendthegame. finite-gasket-spectral-derivatives closed Sweep-167.

## Residual notes from recent sweeps

- Sweep-167: finite-gasket-spectral-derivatives RESEARCH lock (kernel tests + claim table; free mult(6) remains CLAIMED prose; Actions not observed). No archive/release action.
- Sweep-166: Digital_Double_Virtual_Workforce_4. SUPERSEDED re-confirm (private; governance docs only; README empty-ref claim corrected; SUPERSEDED.md + CLAIM_STATUS.md added at 12798ac; no product mutation); GitHub archive flag still PENDING.
- Sweep-165: btc-trading ARCHIVED re-confirm (README + ARCHIVED.md + SECURITY.md terminal, claim 0, hardcoded historical key noted; no subject mutation); GitHub archive flag still PENDING (already in archive_queue.md).
- Sweep-163: ADL-Nexus RESEARCH re-confirm (CI SUCCESS run 14, claim ≤ 2 locked, no subject mutation); gap closed; no new operator archive/release action required for subject.
- Sweep-162: CFTv3.3-IQG-Unified-Framework RESEARCH re-confirm (docs-ci SUCCESS runs 1–2, claim ≤ 2 locked, no subject mutation); gap closed; no new operator archive/release action required for subject.
- Sweep-161: m2-renormalization-law RESEARCH re-confirm (CI SUCCESS run 3, parameter-free lock + 6 pytest; no subject mutation); gap "m2 first CI" closed; no new operator archive/release action required for subject.
- Sweep-160: Portfolio discovery reconstruction; PORTFOLIO_STATE refreshed (census 77, momentum-closure CI success, ADL-Nexus re-confirm); no subject product mutation; no new operator archive/release action required.
- Sweep-146: Digital_Double_Virtual_Workforce_4. SUPERSEDED re-confirmed (docs banner only; empty product surface); superseded by Sweep-166 docs lock.

Update this file only when residual operator work changes.
