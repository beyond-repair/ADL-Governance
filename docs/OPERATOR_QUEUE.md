# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-186)

- Sweep-186: portfolio discovery + Phase-3 re-verify. Docs only in ADL-Governance. Search index 82 (`incomplete_results=false`). Profile `public_repos=77`. Phase-3 CI still green: forge-aegis 36847797174 on `968595a`, sovereign-clean-room 36815859875 on `5fbd20b`, BlockSwarm 36859452185 on `6e90f6f`, Digital Double CI 36861489156 on `24e6a29`. Releases API and tags API empty on all four. Critical Dependabot #13 re-fetched open. Open Dependabot count re-fetched: 56 (`hasNextPage=false`). No archive. No release. No product mutation. Portfolio termination not met.
- Sweep-185: history heading coverage. Governance CI only. Not re-run this cycle.
- Sweep-184: `digital-double-mobile` SUPERSEDED. Lock `c14f50f41a40eab78e0530fa57a73048d2e8c8a2`. Guard run 36911252324 success. Committed `.env` not re-fetched this cycle; treat as still open until operator confirms removal.

- **Security escalation (critical, re-fetched Sweep-186):** Digital_Double_virtual_workforce Dependabot alert #13 remains **open**. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, severity critical, manifest `digital_double/package-lock.json`, scope development, patched version 4.0.4. Agent did not bump the lockfile.
- **Security escalation (volume, re-fetched Sweep-186):** same repo has **56** open Dependabot alerts (`hasNextPage=false`). Do not treat CI success as dependency clearance.
- **Security residual (not re-fetched Sweep-186):** `digital-double-mobile` tracked `.env` from Sweep-184. Rotate any credentials that ever lived in that blob, then remove the tracked file in a new commit. Do not rewrite history.
- Apply GitHub `archived=true` only after operator confirmation: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining archive_queue.md entries. Sweep-186 search still shows `archived=true` only on CFT-v3.0.
- Tag product releases on ACTIVE repos only after operator review (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Sweep-186: releases API and tags API both empty. Do not tag superseded forks.
- Review/merge or close dependabot branches still present on Digital Double (`dependabot/npm_and_yarn/...`, `fix/nanoid-5.1.11-ghsa-xwg4`).
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277` (still present; sha `f65d7db6c4f7d98ed3f5ded3defd5d1886c21cc4`).
- Enable secret scanning on sovereign-clean-room (API 404: feature disabled, Sweep-186).
- Enable or accept absence of code scanning on forge-aegis (API 404: no analysis, Sweep-186).
- Assign cluster/claim caps for census-gap names. Do not invent caps.
- Audit private default-RESEARCH names. Contents not read Sweep-186.
- Reconcile census drift: profile 77, search 82, inherited direct-get union 86.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes

- Sweep-186: exit criteria failed on critical security, duplicate canonicals still present as live repos, archive flag, and import-level dependency map. Stop.
- Sweep-184: committed secret residual on digital-double-mobile. Stop.
- Sweep-183: same portfolio residuals. Stop.

Update this file only when residual operator work changes.
