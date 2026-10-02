# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-206)

- **Security escalation (inherited, not re-fetched):** Digital_Double_virtual_workforce Dependabot alert #13 remains the last known open critical. Package `form-data` in `digital_double/package-lock.json`, scope development, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, vulnerable range `>= 4.0.0, < 4.0.4`, patched 4.0.4. High alerts also last known open, including #160 `js-yaml` and #155 `browserslist`. Agent did not bump the lockfile.
- Apply GitHub `archived=true` to documented ARCHIVED/SUPERSEDED targets, including **Digital_Double_Virtual_Workforce_4.2** (SUPERSEDED, private, flag still false at Sweep-205, head `02c0a3d`), **Digital_Double_Virtual_Workforce_4.**, **My-mind-A.I.**, **VigilE.S.A.-Enhanced-Security**, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive_Microservice, SEEM-Cognitive-Microservice, btc-trading. Census at Sweep-204 showed `archived=true` only on `CFT-v3.0`.
- **4.2 weight:** `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` (~77,844,704 bytes) remains in git. Do not delete from history. Operator may leave it or migrate with a non-rewriting disposition.
- **4.2 misplaced workflow:** `src/.github/workflows/ci.yml` is not a repository workflow. Do not promote it to `.github/workflows/` on a SUPERSEDED repo.
- **My-mind-A.I. CI:** replace or disable `.github/workflows/python-package-conda.yml`. Latest known failure run 36851325554 on `b886113`. Not re-fetched Sweep-206.
- Repair or retire operator-owned `.github/workflows/security_pipeline.yml` on VigilE.S.A.-Enhanced-Security. Sweep-193 recorded run 36863696288 failure. Not re-fetched.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Sweep-204: tags and releases empty on all four. Not re-fetched Sweep-206. ADL-SEEM tags also empty; do not tag a constitution release from this sweep.
- Rotate / remove committed `.env` on digital-double-mobile; resolve Dependabot HIGH alerts. Not re-fetched.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277`. Not re-listed.
- Enable secret scanning on sovereign-clean-room (prior API 404). Not re-fetched.
- Enable or accept absence of code scanning on forge-aegis (prior API 404). Not re-fetched.
- Expand adl-capability-matrix to live census (83).
- Audit remaining private default-RESEARCH names: `atomicdreamlabs`, `blacksite`, `mendthegame`, `potential-garbanzo`, `SovereignOS`, `test`.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes from recent sweeps

- Sweep-206: `ADL-SEEM` ACTIVE constitution confirmed, claim 0. Stale blocked-on-chunks sentence removed from `docs/CANONICAL.md`. Green head `2d042604`. Docs-contract run 37075801340 success. Run 37075634775 failed on a quoted token and was corrected. No tag. VSA completeness not re-measured.
- Sweep-205: `Digital_Double_Virtual_Workforce_4.2` SUPERSEDED confirmed. Local claim-0 pytest 17 passed. Docs commit `02c0a3d`. No archive flag. No tag.
- Sweep-204: Phase-3 live re-fetch. Four product CI runs success. Tags and releases empty. #13 still open.
- Sweep-203: `scale-functional-I` registered RESEARCH claim ≤ 1. Local unittest 1 passed. No workflow.
- Sweep-202: `Digital_Double_Virtual_Workforce_4.` SUPERSEDED confirmed. Docs-only. No archive flag.
