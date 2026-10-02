# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

Canonical path: `docs/OPERATOR_QUEUE.md` (repository root has no `OPERATOR_QUEUE.md`).

## Open items (as of Sweep-199)

- **Security escalation (critical), inherited from Sweep-198, not re-fetched:** `Digital_Double_virtual_workforce` Dependabot #13 still open at last check. Package `form-data`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, manifest `digital_double/package-lock.json`, scope development, patched version 4.0.4. Alert `updated_at` `2025-07-22T06:57:23Z`. Agent did not bump the lockfile.
- **Security escalation (high), inherited first page:** #160 and #159 `js-yaml` GHSA-2883-xcg3-v3hh; #155 `browserslist` GHSA-73wf-gq98-2v4g; #153 `nanoid` GHSA-xwg4-73v4-xw9w. High page not exhausted. Branch `fix/nanoid-5.1.11-ghsa-xwg4` was not merged.
- Product CI last verified in Sweep-198, not re-fetched this cycle: forge-aegis 36847797174; sovereign-clean-room 36815859875; BlockSwarm 36859452185; Digital_Double_virtual_workforce 36861489156. All conclusions `success` at that time. Releases API empty. Tags API empty. Do not invent tags.
- **Secret scanning:** `sovereign-clean-room` returned 404 (secret scanning disabled) in Sweep-198. Not re-fetched.
- **Code scanning:** `forge-aegis` returned 404 (no analysis found) in Sweep-198. Not re-fetched.
- `ftmA.I.bot` run 36925900968 was still `queued` on `79d97f92417da64deb6b31f679a7c3a6eb8a2df5` in Sweep-198. Not re-fetched. Do not dispatch another run. Do not execute trading stubs.
- **ADL-Nexus claim contradiction (inherited):** README badge says claim ≤1. `docs/CLAIM_STATUS.md` says core claim level 2. Do not promote.
- **ADL-Nexus PR #3** (`repair/kernel-path`) was open at Sweep-196. Not re-fetched. Do not merge from the agent.
- `DigitalDoubleVirtualWorkforce3.5` remains SUPERSEDED with GitHub `archived=false`. Do not delete.
- **Security residual (inherited):** `digital-double-mobile` tracked `.env` (Sweep-184). Rotate credentials, then remove the tracked file in a new commit. Do not rewrite history.
- **This cycle:** `quantum_A.I._optimization.py` is governance-class ARCHIVED and claim 0. CI run 36943905023 success on `6e5e1070e65db766389daf1d1f2156c51d12fe70`. Do not set GitHub `archived=true` until operator confirmation. Do not delete. Do not tag a release from the agent.
- Apply GitHub `archived=true` only after operator confirmation. Inherited archived flag: `CFT-v3.0` only. Queue remains: digital-double-mobile, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive-Microservice, SEEM-Cognitive_Microservice, btc-trading, quantum_A.I._optimization.py, and remaining `docs/archive_queue.md` entries.
- Reconcile census drift: search 82 (73 public, 9 private); profile `public_repos=77` last cycle.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.
- Census cluster/cap refresh for UNASSIGNED names: operator-gated. Do not invent caps.

## Residual notes

- Sweep-199 closed the Python 3.9 CI failure on the selected sketch. That does not close Dependabot #13.
- Portfolio exit criteria still fail on critical Dependabot #13, duplicate workforce lines, archive flags, empty releases, and the queued archive-guard. Stop.
