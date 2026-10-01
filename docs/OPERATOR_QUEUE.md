# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-173)

- Apply GitHub `archived=true` flag to documented ARCHIVED/SUPERSEDED targets: genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, **-Py2APK-main**, **fantom_trading_bot_2**, **Digital_Double_Virtual_Workforce_4.**, Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, **CFT-v3.1**, **Agent-Snake**, **SEEM-Cognitive_Microservice**, **SEEM-Cognitive-Microservice** (hyphen; Sweep-169 re-confirm, still `archived=false` at last subject check), **btc-trading**, and remaining queue entries in archive_queue.md / repository_registry.md.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Live re-verify Sweep-171: all four named targets still have **zero releases** returned by the releases API.
- Rotate / remove committed `.env` on digital-double-mobile; resolve Dependabot HIGH alerts. Not re-fetched this sweep; prior finding retained.
- Review/merge open PRs on Digital_Double_virtual_workforce, re-confirmed Sweep-171: #3, #4 (nanoid GHSA), #5, #6 (Dependabot), #7 (draft evidence journal).
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277` (present at Sweep-171; merge state not re-audited).
- Expand adl-capability-matrix to live 82-row census (locked 67 at last audit; OPEN).
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.
- Optional: remove or LFS-migrate large committed model weight in Digital_Double_Virtual_Workforce_4.2 (hygiene only).
- Audit remaining default-RESEARCH names: atomicdreamlabs (private), mendthegame (private; not read). `bloch-coherence-factor2` closed Sweep-173.

No new operator item from Sweep-173. `bloch-coherence-factor2` stays RESEARCH; do not tag a physics release and do not merge the failed loop-correction branch onto main from this sweep.

## Residual notes from recent sweeps

- Sweep-173: bloch-coherence-factor2 RESEARCH lock. Claim file commit `3cdbc2e3`. Local pytest 11 passed on pre head `05571476`. Main Actions 36844364901 success on that pre head. Releases empty. Loop branch not re-audited (run 36100043944 failed). No archive/release/history action.
- Sweep-172: topological-pinch RESEARCH re-confirm. Lock commit `3e62e04`. Local pytest 5 passed. Default Voronoi residual proxy 0.5/0.4/0.1, not 0.92. Releases empty. No archive/release/history action.
- Sweep-171: portfolio discovery refresh. Census 82 vs profile public_repos 77. Phase 3: forge-aegis CI 36847797174 success; sovereign-clean-room 36815859875 success; BlockSwarm 36859452185 success; Digital_Double_virtual_workforce 36861489156 success. Releases empty. No archive/release/history action.
- Sweep-170: mend RESEARCH lock (CLAIM_STATUS + dependency-free formula witness; local node test 1/1; witness does not import formulas.ts; Actions not run; npm test not run). No archive/release action. mendthegame not read (private).
- Sweep-169: SEEM-Cognitive-Microservice SUPERSEDED re-confirm (docs only at 56c7aae; no product mutation; GitHub archive flag still PENDING). Placeholder API key in seem.py is not a committed live secret.
- Sweep-168: informational-flux-identity RESEARCH lock. Phase 3 numbers superseded by Sweep-171.
- Sweep-166: Digital_Double_Virtual_Workforce_4. SUPERSEDED re-confirm (private; governance docs only).
- Sweep-165: btc-trading ARCHIVED re-confirm; GitHub archive flag still PENDING.

Update this file only when residual operator work changes.
