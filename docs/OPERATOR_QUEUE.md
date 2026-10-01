# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-174)

- **Security escalation:** Digital_Double_virtual_workforce Dependabot alert #13 remains open. Package `form-data` in `digital_double/package-lock.json`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, severity critical, vulnerable range `>= 4.0.0, < 4.0.4`, patched 4.0.4. Created 2025-07-22. Agent did not bump the lockfile this sweep.
- Apply GitHub `archived=true` flag to documented ARCHIVED/SUPERSEDED targets: genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, **-Py2APK-main**, **fantom_trading_bot_2**, **Digital_Double_Virtual_Workforce_4.**, Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, **CFT-v3.1**, **Agent-Snake**, **SEEM-Cognitive_Microservice**, **SEEM-Cognitive-Microservice**, **btc-trading**, and remaining queue entries in archive_queue.md / repository_registry.md. Sweep-174 census still shows `archived=true` only on `CFT-v3.0`.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Sweep-174: releases API and tags API both empty for all four.
- Rotate / remove committed `.env` on digital-double-mobile; resolve Dependabot HIGH alerts. Not re-fetched this sweep; prior finding retained.
- Review/merge open PRs on Digital_Double_virtual_workforce. Sweep-171 recorded #3, #4, #5, #6, #7. Not re-listed this sweep. Dependabot branches still present: `dependabot/npm_and_yarn/digital_double/npm_and_yarn-790e04dbfc`, `dependabot/npm_and_yarn/digital_double/rollup-4.63.1`, `dependabot/npm_and_yarn/npm_and_yarn-95bbd494c8`.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277` (still present Sweep-174; merge state not re-audited). High+ Dependabot open list on that repo was empty.
- Enable secret scanning on sovereign-clean-room (API 404: feature disabled).
- Enable or accept absence of code scanning on forge-aegis (API 404: no analysis).
- Expand adl-capability-matrix to live 82-row census (locked 67 at last audit; OPEN).
- Audit remaining private default-RESEARCH names: `atomicdreamlabs`, `mendthegame`, `potential-garbanzo`, `SovereignOS`, `test`.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.
- Optional: remove or LFS-migrate large committed model weight in Digital_Double_Virtual_Workforce_4.2 (hygiene only).

## Residual notes from recent sweeps

- Sweep-174: portfolio discovery refresh. Census 82 vs profile public_repos 77. Private 9. Archived flag 1 (`CFT-v3.0`). Phase 3 CI still success: forge-aegis 36847797174, sovereign-clean-room 36815859875, BlockSwarm 36859452185, Digital_Double_virtual_workforce 36861489156. Releases and tags empty. New verified residual: Dependabot critical #13. Secret scanning disabled on sovereign-clean-room. No archive/release/history action.
- Sweep-173: bloch-coherence-factor2 RESEARCH lock. Claim file commit `3cdbc2e3`. Local pytest 11 passed on pre head `05571476`. Main Actions 36844364901 success on that pre head. Releases empty. Loop branch not re-audited (run 36100043944 failed).
- Sweep-172: topological-pinch RESEARCH re-confirm. Lock commit `3e62e04`. Local pytest 5 passed. Default Voronoi residual proxy 0.5/0.4/0.1, not 0.92.
- Sweep-171: prior Phase 3 verify. Numbers confirmed again in Sweep-174.
- Sweep-170: mend RESEARCH lock. mendthegame not read (private).

Update this file only when residual operator work changes.
