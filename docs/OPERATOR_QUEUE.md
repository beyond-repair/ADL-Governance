# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-179)

- Sweep-179: GAP-BRIDGE-ADAPTER-DEFS closed as documented absence. Lock `32a93564` on `sunder-cleanroom-vsa-adapter`. Local pytest 9 passed. No archive/release/history action. Post-push CI not observed. Claim cap unchanged.
- Sweep-178: random select bloch-coherence-factor2. RESEARCH re-confirm. Lock `77d7063`. Local pytest 11 passed. Main Actions 36881720661 success on pre head. No archive/release/history action. Post-push CI not observed. Optional operator tag would not raise claim level; not applied.

- **Security escalation (critical):** Digital_Double_virtual_workforce Dependabot alert #13 remains **open**. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, severity critical. Re-fetched 2026-10-01 Sweep-177. Agent did not bump the lockfile.
- **Security escalation (high volume):** same repo has **56** open Dependabot alerts on the first page (`per_page=100`). Newly listed this sweep (not previously in this queue as a count): high alerts include `js-yaml` GHSA-2883-xcg3-v3hh (#160/#159), `browserslist` GHSA-73wf-gq98-2v4g (#155), `nanoid` GHSA-xwg4-73v4-xw9w (#153/#147), `brace-expansion` GHSA-3jxr-9vmj-r5cp (#122), `js-yaml` GHSA-5p4m-2wfm-xmqj (#112/#111). Medium includes `pytest` CVE-2025-71176 (#168) and multiple `vite` advisories. Do not treat CI success as dependency clearance.
- Apply GitHub `archived=true` only after operator confirmation: genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive_Microservice, SEEM-Cognitive-Microservice, btc-trading, and remaining archive_queue.md entries. Sweep-177 still shows `archived=true` only on CFT-v3.0.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Sweep-177: releases API and tags API both empty for all four.
- Rotate / remove committed `.env` on digital-double-mobile. Not re-fetched this sweep; prior finding retained.
- Review/merge or close dependabot branches still present: `dependabot/npm_and_yarn/digital_double/npm_and_yarn-790e04dbfc`, `dependabot/npm_and_yarn/digital_double/rollup-4.63.1`, `dependabot/npm_and_yarn/npm_and_yarn-95bbd494c8`, `fix/nanoid-5.1.11-ghsa-xwg4`.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277` (still present). High+ Dependabot open list on that repo was empty (0).
- Enable secret scanning on sovereign-clean-room (API 404: feature disabled).
- Enable or accept absence of code scanning on forge-aegis, sovereign-clean-room, BlockSwarm, Digital_Double_virtual_workforce (API 404: no analysis).
- Add a non-vacuous CI workflow to ADL-Governance (workflows total_count 0 at Sweep-177; not re-checked Sweep-179). Next basilisk slice: GAP-GOVERNANCE-CI.
- Assign cluster/claim caps for the 15 names in `adl-capability-matrix` `matrix/census_gap_2026-10-01.json` (Sweep-175). Do not invent caps.
- Audit private default-RESEARCH names: `atomicdreamlabs`, `mendthegame`, `blacksite`, `test`, `SovereignOS` (private confirmed Sweep-177; contents not read).
- Reconcile census drift: profile 77, search 82, direct-get union 86. Do not delete names to force equality.
- Backfill pass YAML for 171, 172, 175, 177, 178 only from existing history evidence. Do not invent missing bodies.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes from recent sweeps

- Sweep-179: adapter contract-only AST witness. Lock `32a93564`. Local pytest 9 passed. No runtime import.
- Sweep-177: portfolio discovery + Phase-3 re-verify. No archive flag, no release tag, no history rewrite, no lockfile bump. Exit criteria failed on critical security and duplicate canonicals. Stop.
- Sweep-176: seem-sunder-bridge RESEARCH re-confirm. Lock `3ccd7cde`. Local pytest 8 passed. Post-push CI not observed.
- Sweep-175: adl-capability-matrix RESEARCH. Lock `e57ec52`. Gap 15 unassigned names. Post-push CI success 36889001703.
- Sweep-174: Phase 3 CI IDs reconfirmed in Sweep-177 (same success runs still latest).

Update this file only when residual operator work changes.
