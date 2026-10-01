# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

Canonical path: `docs/OPERATOR_QUEUE.md` (repository root has no `OPERATOR_QUEUE.md`).

## Open items (as of Sweep-198)

- **Security escalation (critical), re-verified:** `Digital_Double_virtual_workforce` Dependabot #13 still open. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, scope development, patched version 4.0.4. Alert `updated_at` `2025-07-22T06:57:23Z`. Agent did not bump the lockfile.
- **Security escalation (high), re-verified first page:** #160 and #159 `js-yaml` GHSA-2883-xcg3-v3hh; #155 `browserslist` GHSA-73wf-gq98-2v4g; #153 `nanoid` GHSA-xwg4-73v4-xw9w. High page not exhausted. Branch `fix/nanoid-5.1.11-ghsa-xwg4` was not merged by this sweep.
- Product CI re-fetched on current default-branch heads: forge-aegis 36847797174 on `968595a72f50f38b64c9495b180cefd99abde45d`; sovereign-clean-room 36815859875 on `5fbd20b201a02b41b1c8a9e698b78d9954a34da0`; BlockSwarm 36859452185 on `6e90f6f85c0969fa8a262a70ceba833d618a22db`; Digital_Double_virtual_workforce 36861489156 on `24e6a29fd26c03900a8d98634d6683996eabdac4`. All conclusions `success`. Releases API empty. Tags API empty. Do not invent tags.
- **Secret scanning:** `sovereign-clean-room` returned 404 (secret scanning disabled). Enable it before claiming a clean secret scan. Unmerged branch `fix/pynacl-1.6.2-cve-2025-69277` was not re-fetched this cycle. Do not claim that CVE is closed.
- **Code scanning:** `forge-aegis` returned 404 (no analysis found). Operator decision required before treating absence as a pass.
- `ftmA.I.bot` run 36925900968 still `queued` on `79d97f92417da64deb6b31f679a7c3a6eb8a2df5`. `created_at` and `updated_at` unchanged at `2026-10-01T21:02:13Z`. Jobs `total_count` 0. Do not dispatch another run. Do not cancel from the agent. Do not execute trading stubs.
- **ADL-Nexus claim contradiction (inherited, not re-fetched):** README badge says claim ≤1. `docs/CLAIM_STATUS.md` says core claim level 2. Do not promote. Operator must pick one claim level and update both files in one commit.
- **ADL-Nexus PR #3** (`repair/kernel-path`) was open at Sweep-196. Not re-fetched. Do not merge from the agent.
- `DigitalDoubleVirtualWorkforce3.5` remains SUPERSEDED with GitHub `archived=false`. Do not delete. Do not rename import-statement filenames.
- **Security residual (inherited):** `digital-double-mobile` tracked `.env` (Sweep-184). Rotate credentials, then remove the tracked file in a new commit. Do not rewrite history.
- Apply GitHub `archived=true` only after operator confirmation. Inherited archived flag: `CFT-v3.0` only. Queue remains: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, and remaining `docs/archive_queue.md` entries.
- Reconcile census drift: search 82 (73 public, 9 private); profile `public_repos=77` this cycle.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.
- Census cluster/cap refresh for UNASSIGNED names: operator-gated. Do not invent caps.

## Residual notes

- Sweep-198 confirmed current heads equal the last successful product CI SHAs. That does not close #13.
- Sweep-197 local pytest on `sunder-cleanroom-vsa-adapter` was not re-run.
- Portfolio exit criteria still fail on critical Dependabot #13, duplicate workforce lines, archive flags, empty releases, and the queued archive-guard. Stop.
