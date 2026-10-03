# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-208)

- **digital-double-mobile security (re-fetched Sweep-208):** open critical Dependabot #30 `protobufjs` (GHSA-xq3m-2v4x-88gg, `package-lock.json`) and #8 `form-data` (GHSA-fjxv-7rqg-78g4). High alerts include #85 `browserslist`, #83 `nanoid`, #78 `postcss`. Not exhaustive. Agent did not bump the lockfile on a SUPERSEDED repo.
- **digital-double-mobile secrets:** working tree has no `.env` (depth-1 clone, head `2d9a885`). History was not rewritten. Rotate any credentials that ever lived in a committed `.env` (including historical OpenRouter-style placeholders) before setting `archived=true`.
- **Security escalation (inherited Sweep-207):** Digital_Double_virtual_workforce Dependabot alert #13 is still open as of Sweep-207. Package `form-data` in `digital_double/package-lock.json`, GHSA-fjxv-7rqg-78g4. Not re-fetched Sweep-208.
- Apply GitHub `archived=true` to documented ARCHIVED/SUPERSEDED targets, including **digital-double-mobile** (after secret rotation), **Digital_Double_Virtual_Workforce_4.2**, **Digital_Double_Virtual_Workforce_4.**, **My-mind-A.I.**, **VigilE.S.A.-Enhanced-Security**, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive_Microservice, SEEM-Cognitive-Microservice, btc-trading. Only `CFT-v3.0` was `archived=true` at Sweep-207. Not re-listed Sweep-208.
- **4.2 weight:** `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` (~77,844,704 bytes) remains in git. Do not delete from history. Not re-measured Sweep-208.
- **4.2 misplaced workflow:** `src/.github/workflows/ci.yml` is not a repository workflow. Do not promote it to `.github/workflows/` on a SUPERSEDED repo.
- **My-mind-A.I. CI:** replace or disable `.github/workflows/python-package-conda.yml`. Latest known failure run 36851325554 on `b886113`. Not re-fetched.
- Repair or retire operator-owned `.github/workflows/security_pipeline.yml` on VigilE.S.A.-Enhanced-Security. Sweep-193 recorded run 36863696288 failure. Not re-fetched.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Not re-fetched Sweep-208.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277`.
- Fix or close `sovereign-clean-room` pull request branch `seem-completion-pass`. Run 37087542135 failed at `Run tests` on `9412b339`. Not re-fetched.
- Enable secret scanning on sovereign-clean-room (prior API 404). Not re-fetched.
- Enable or accept absence of code scanning on forge-aegis and Digital_Double_virtual_workforce (API 404 no analysis, Sweep-207).
- Expand adl-capability-matrix to live search census (83 non-fork).
- Audit remaining private default-RESEARCH names. Trees not read this cycle.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes from recent sweeps

- Sweep-208: `digital-double-mobile` SUPERSEDED claim 0 confirmed. Local pytest 10 passed. CI workflow extended to run pytest. Critical Dependabot #30 and #8 remain open. Archive flag false. Stopped.
- Sweep-207: four-pillar live re-fetch. Main CI green on forge-aegis `590ba108` / run 37065566958, sovereign-clean-room `4878918c` / run 37064701216, BlockSwarm `6e90f6f` / run 36859452185, Digital Double `24e6a29` / run 36861489156. Exit criteria failed on #13 and unfinished archive/release/private-tree work. Stopped.
- Sweep-206: `ADL-SEEM` ACTIVE constitution confirmed, claim 0. Stale blocked-on-chunks sentence removed from `docs/CANONICAL.md`. Green head `2d042604`. Docs-contract run 37075801340 success. Run 37075634775 failed on a quoted token and was corrected. No tag. VSA completeness not re-measured.
- Sweep-205: `Digital_Double_Virtual_Workforce_4.2` SUPERSEDED confirmed. Local claim-0 pytest 17 passed. Docs commit `02c0a3d`. No archive flag. No tag.
- Sweep-204: Phase-3 live re-fetch. Four product CI runs success. Tags and releases empty. #13 still open.
- Sweep-203: `scale-functional-I` registered RESEARCH claim ≤ 1. Local unittest 1 passed. No workflow.
- Sweep-202: `Digital_Double_Virtual_Workforce_4.` SUPERSEDED confirmed. Docs-only. No archive flag.
