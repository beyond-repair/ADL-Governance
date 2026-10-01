# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

Canonical path: `docs/OPERATOR_QUEUE.md` (repository root has no `OPERATOR_QUEUE.md`).

## Open items (as of Sweep-192)

- Sweep-192: search index 82 (`incomplete_results=false`). Phase-3 CI still success on forge-aegis 36847797174, sovereign-clean-room 36815859875, BlockSwarm 36859452185, Digital_Double_virtual_workforce 36861489156. Releases and tags empty on all four. No lockfile edit. No archive flag. No product mutation.
- Sweep-191 residual still open: `ftmA.I.bot` run 36925900968 remains `queued` on `79d97f92417da64deb6b31f679a7c3a6eb8a2df5` (`updated_at` 2026-10-01T21:02:13Z). Do not dispatch another run while this one is queued. Do not execute trading stubs.
- **Security escalation (critical):** Digital_Double_virtual_workforce Dependabot alert #13 open. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, patched version 4.0.4. Agent did not bump the lockfile.
- **Security escalation (high):** Dependabot #160 `js-yaml` GHSA-2883-xcg3-v3hh still open. Further high alerts exist; exact count not returned.
- **Security residual:** `digital-double-mobile` tracked `.env` (Sweep-184). Rotate credentials, then remove the tracked file in a new commit. Do not rewrite history.
- Apply GitHub `archived=true` only after operator confirmation. Search this cycle still shows `archived=true` only on `CFT-v3.0`. Queue remains: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining `docs/archive_queue.md` entries.
- Tag product releases on ACTIVE repos only after operator review. Do not invent `v0.5.0-sagf` while the tags API is empty.
- Enable secret scanning on sovereign-clean-room and decide code scanning on forge-aegis. Not re-queried this cycle.
- Reconcile census drift: search 82 this cycle; profile `public_repos=77` inherited from Sweep-189 and not re-fetched.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes

- Sweep-192 exit criteria failed on critical security, duplicate canonicals, archive flags, and the queued archive-guard run. Stop.
