# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-182)

- Sweep-181: random select `sunder`. RESEARCH reconfirm. Lock `36d37c247e0e0be2ef8404cc697a1dcd4250de12`. Local pytest 6 passed. Post-push CI not observed. No archive. No release. Claim ≤ 1.
- Sweep-180: portfolio re-verification only. No archive flag, no release tag, no history rewrite, no lockfile bump. Phase-3 CI still green. Critical Dependabot #13 still open. Portfolio termination not met.
- Sweep-179: GAP-BRIDGE-ADAPTER-DEFS closed as documented absence. Lock `32a93564` on `sunder-cleanroom-vsa-adapter`. Local pytest 9 passed. Post-push CI not observed. Claim cap unchanged.
- Sweep-178: random select bloch-coherence-factor2. RESEARCH re-confirm. Lock `77d7063`. Local pytest 11 passed. Main Actions 36881720661 success on pre head. Post-push CI not observed.

- **Security escalation (critical):** Digital_Double_virtual_workforce Dependabot alert #13 remains **open**. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, severity critical, manifest `digital_double/package-lock.json`, scope development. Re-fetched 2026-10-01 Sweep-180. Agent did not bump the lockfile. Not re-fetched Sweep-181.
- **Security escalation (high volume):** same repo has **56** open Dependabot alerts (Sweep-180). Do not treat CI success as dependency clearance.
- Apply GitHub `archived=true` only after operator confirmation: genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive_Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining archive_queue.md entries. Sweep-180 search still shows `archived=true` only on CFT-v3.0.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Sweep-180: releases API and tags API both empty for all four. Do not tag `sunder` (RESEARCH).
- Rotate / remove committed `.env` on digital-double-mobile. Not re-fetched; prior finding retained.
- Review/merge or close dependabot branches still present on Digital Double.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277`.
- Enable secret scanning on sovereign-clean-room (API 404: feature disabled, Sweep-180).
- Enable or accept absence of code scanning on forge-aegis.
- Sweep-182: GAP-GOVERNANCE-CI workflow present. Local checker PASS. Actions 36904879407 and 36904903811 success. No archive. No release.
- Assign cluster/claim caps for the 15 names in `adl-capability-matrix` `matrix/census_gap_2026-10-01.json` (Sweep-175). Do not invent caps.
- Audit private default-RESEARCH names. Contents not read Sweep-181.
- Reconcile census drift: profile 77, search 82, inherited direct-get union 86.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes from recent sweeps

- Sweep-181: sunder RESEARCH. Lock `36d37c24`. Local pytest 6 passed. Claim ledger added.
- Sweep-180: portfolio discovery + Phase-3 re-verify. Docs only. Exit criteria failed on critical security and duplicate canonicals.
- Sweep-179: adapter contract-only AST witness. Lock `32a93564`.
- Sweep-176: seem-sunder-bridge RESEARCH re-confirm. Lock `3ccd7cde`.

Update this file only when residual operator work changes.
