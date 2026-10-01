# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-191)

- Sweep-191: re-verified `ftmA.I.bot` archive-guard locally (3 passed) on lock `79d97f92417da64deb6b31f679a7c3a6eb8a2df5`. Actions run 36925900968 still queued with zero jobs. Do not rerun while that dispatch is queued. No archive flag, no trading-script execution.
- Sweep-190: random subject `ftmA.I.bot`. RESEARCH archive-queue reconfirmed. Lock `79d97f92417da64deb6b31f679a7c3a6eb8a2df5`. Local unittest 3 passed. Actions run 36925900968 was queued, not success, at record time. No archive flag, no release, no stub deletion, no trading-script execution.
- Sweep-189: portfolio discovery + Phase-3 re-verify. Docs only. Critical Dependabot #13 still open. Search index 82. Profile `public_repos=77`.
- Sweep-187: `RealityOS` RESEARCH. Lock `59b15e88fab57aeac7fcb435db92d6abf796bc97`. research-guard run 36918662862 success.
- Sweep-184: `digital-double-mobile` SUPERSEDED. Tracked `.env` still an operator residual until removed.

- **Security escalation (critical, inherited Sweep-189):** Digital_Double_virtual_workforce Dependabot alert #13 open. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, patched version 4.0.4. Agent did not bump the lockfile.
- **Security residual:** `digital-double-mobile` tracked `.env`. Rotate credentials, then remove the tracked file in a new commit. Do not rewrite history.
- **Do not execute** historical order-manipulation stubs in `ftmA.I.bot` (`flashloan_front_running.py` and similar). Preservation only. Quarantine without history rewrite is operator-only.
- Apply GitHub `archived=true` only after operator confirmation: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining archive_queue.md entries. Sweep-189 search showed `archived=true` only on CFT-v3.0. `ftmA.I.bot` flag still false this cycle.
- Tag product releases on ACTIVE repos only after operator review. Do not invent `v0.5.0-sagf` while the tags API is empty.
- Enable secret scanning on sovereign-clean-room. Code scanning absence on forge-aegis remains operator choice.
- Reconcile census drift: profile 77, search 82, inherited direct-get union 86.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes

- Sweep-191 subject slice: local invariants reconfirmed. Remote Actions conclusion still unknown. Portfolio exit criteria failed. Stop.
