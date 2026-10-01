# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-187)

- Sweep-187: random subject `RealityOS`. RESEARCH reconfirmed. Lock `59b15e88fab57aeac7fcb435db92d6abf796bc97`. research-guard run 36918662862 success. No archive, no release, no connector implementation, no claim promotion. No new destructive action on this repo.
- Sweep-186: portfolio discovery + Phase-3 re-verify. Docs only. Search index 82. Profile `public_repos=77`. Phase-3 CI still green at that cycle. Critical Dependabot #13 was open. Open Dependabot count 56. Not re-fetched Sweep-187.
- Sweep-184: `digital-double-mobile` SUPERSEDED. Lock `c14f50f41a40eab78e0530fa57a73048d2e8c8a2`. Guard run 36911252324 success. Committed `.env` not re-fetched; treat as still open until operator confirms removal.

- **Security escalation (critical, not re-fetched Sweep-187):** Digital_Double_virtual_workforce Dependabot alert #13 was open at Sweep-186. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, severity critical, manifest `digital_double/package-lock.json`, scope development, patched version 4.0.4. Agent did not bump the lockfile.
- **Security escalation (volume, not re-fetched Sweep-187):** same repo had 56 open Dependabot alerts. Do not treat CI success as dependency clearance.
- **Security residual:** `digital-double-mobile` tracked `.env` from Sweep-184. Rotate any credentials that ever lived in that blob, then remove the tracked file in a new commit. Do not rewrite history.
- Apply GitHub `archived=true` only after operator confirmation: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining archive_queue.md entries. Sweep-186 search still showed `archived=true` only on CFT-v3.0. RealityOS is not an archive candidate.
- Tag product releases on ACTIVE repos only after operator review. Do not tag RealityOS or other RESEARCH/SUPERSEDED repos from this sweep.
- Review/merge or close dependabot branches still present on Digital Double.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277`.
- Enable secret scanning on sovereign-clean-room (API 404 at Sweep-186).
- Enable or accept absence of code scanning on forge-aegis (API 404 at Sweep-186).
- Assign cluster/claim caps for census-gap names. Do not invent caps.
- Audit private default-RESEARCH names. Contents not read.
- Reconcile census drift: profile 77, search 82, inherited direct-get union 86.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes

- Sweep-187: RealityOS subject gate met for this slice (tests + CI + docs). Portfolio exit criteria still failed on critical security, duplicate canonicals, archive flag, and import graph. Stop.
- Sweep-186: same portfolio residuals. Stop.
- Sweep-184: committed secret residual on digital-double-mobile. Stop.
