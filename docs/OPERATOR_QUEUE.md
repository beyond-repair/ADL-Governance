# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

Canonical path: `docs/OPERATOR_QUEUE.md` (repository root has no `OPERATOR_QUEUE.md`).

## Open items (as of Sweep-194)

- Sweep-194 re-fetch: `ftmA.I.bot` run 36925900968 still `queued` on `79d97f92417da64deb6b31f679a7c3a6eb8a2df5`. `created_at` and `updated_at` `2026-10-01T21:02:13Z`. Jobs `total_count` 0. No conclusion. Do not dispatch another run. Do not cancel from the agent. Do not execute trading stubs.
- Sweep-193 subject: `DigitalDoubleVirtualWorkforce3.5` head `367fb3699da832a902c6c5cb8f3419bb2acb87a0`. Classification SUPERSEDED. `supersede-guard` run 36932535230 success. GitHub `archived` still false. Do not delete the repo. Do not rename the import-statement filenames. Do not treat `tests/conftest.py` as a product suite (`src.core.agent` is absent).
- Sweep-192 residual still open: product CI last recorded success on forge-aegis 36847797174, sovereign-clean-room 36815859875, BlockSwarm 36859452185, Digital_Double_virtual_workforce 36861489156. Releases and tags empty on all four. Not re-queried this cycle.
- **Security escalation (critical):** Digital_Double_virtual_workforce Dependabot alert #13 open at Sweep-192. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, patched version 4.0.4. Not re-queried. Agent did not bump the lockfile.
- **Security escalation (high):** Dependabot #160 `js-yaml` GHSA-2883-xcg3-v3hh still open at Sweep-192. Further high alerts exist; exact count not returned.
- **Security residual:** `digital-double-mobile` tracked `.env` (Sweep-184). Rotate credentials, then remove the tracked file in a new commit. Do not rewrite history.
- Apply GitHub `archived=true` only after operator confirmation. Inherited archived flag: `CFT-v3.0` only. Queue remains: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining `docs/archive_queue.md` entries.
- Tag product releases on ACTIVE repos only after operator review. Do not invent `v0.5.0-sagf` while the tags API is empty.
- Enable secret scanning on sovereign-clean-room and decide code scanning on forge-aegis. Not re-queried this cycle.
- Reconcile census drift: search 82 this cycle; profile `public_repos=77` at Sweep-194 get_me. Private count 9 was recorded in Sweep-192 and not re-fetched.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.
- Persistence gap closed in Sweep-194: PASS-192 and PASS-193 yaml reconstructed from `docs/SWEEP_HISTORY.md`. They are not new product verification.

## Residual notes

- Sweep-194 exit criteria failed on archive-guard still queued, archive flag, inherited critical security, and duplicate canonicals. Stop.
