# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

Canonical path: `docs/OPERATOR_QUEUE.md` (repository root has no `OPERATOR_QUEUE.md`).

## Open items (as of Sweep-195)

- **Security escalation (critical):** `Digital_Double_virtual_workforce` Dependabot #13 still open. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, patched version 4.0.4, scope development. Agent did not bump the lockfile.
- **Security escalation (high):** #160 and #159 `js-yaml` GHSA-2883-xcg3-v3hh; #155 `browserslist` GHSA-73wf-gq98-2v4g; #153 `nanoid` GHSA-xwg4-73v4-xw9w. High page not exhausted. Branch `fix/nanoid-5.1.11-ghsa-xwg4` exists and was not merged by this sweep.
- `ftmA.I.bot` run 36925900968 still `queued` on `79d97f92417da64deb6b31f679a7c3a6eb8a2df5`. `created_at` and `updated_at` `2026-10-01T21:02:13Z`. No conclusion. Do not dispatch another run. Do not cancel from the agent. Do not execute trading stubs.
- `DigitalDoubleVirtualWorkforce3.5` remains SUPERSEDED with GitHub `archived=false`. Do not delete. Do not rename import-statement filenames.
- Product CI last recorded success: forge-aegis 36847797174, sovereign-clean-room 36815859875, BlockSwarm 36859452185, Digital_Double_virtual_workforce 36861489156. Releases API empty on all four. Do not invent tags.
- Unmerged security branch `fix/pynacl-1.6.2-cve-2025-69277` on sovereign-clean-room. Review before merge. Do not claim the CVE is closed.
- **Security residual:** `digital-double-mobile` tracked `.env` (Sweep-184). Rotate credentials, then remove the tracked file in a new commit. Do not rewrite history.
- Apply GitHub `archived=true` only after operator confirmation. Inherited archived flag: `CFT-v3.0` only. Queue remains: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining `docs/archive_queue.md` entries.
- Enable secret scanning on sovereign-clean-room and decide code scanning on forge-aegis. Not re-queried this cycle.
- Reconcile census drift: search 82 (73 public, 9 private); profile `public_repos=77`.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes

- Sweep-195 exit criteria failed on critical Dependabot #13, duplicate workforce lines, and archive flags. Stop.
