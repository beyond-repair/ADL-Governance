# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-209)

- **seem-sunder-bridge Dependabot PR #2:** pytest 8.3.5 → 9.0.3 (`dependabot/pip/pip-590e9db7b9`). Branch CI runs 37071847548 and 37071841670 succeeded. Agent did not merge. Operator may merge or close. Not a product runtime dependency.
- **seem-sunder-bridge pin freshness:** witnesses stop at 2026-10-02 commits. Re-read foreign blobs before any claim that default heads still match. Do not import those repos into the bridge.
- **digital-double-mobile security (inherited Sweep-208):** open critical Dependabot #30 `protobufjs` (GHSA-xq3m-2v4x-88gg) and #8 `form-data` (GHSA-fjxv-7rqg-78g4). High alerts include #85 `browserslist`, #83 `nanoid`, #78 `postcss`. Not re-fetched Sweep-209.
- **digital-double-mobile secrets:** working tree had no `.env` at Sweep-208 head `2d9a885`. History was not rewritten. Rotate any credentials that ever lived in a committed `.env` before setting `archived=true`.
- **Security escalation (inherited Sweep-207):** Digital_Double_virtual_workforce Dependabot alert #13 still open as of Sweep-207. Package `form-data` in `digital_double/package-lock.json`, GHSA-fjxv-7rqg-78g4. Not re-fetched Sweep-209.
- Apply GitHub `archived=true` to documented ARCHIVED/SUPERSEDED targets, including digital-double-mobile (after secret rotation), Digital_Double_Virtual_Workforce_4.2, Digital_Double_Virtual_Workforce_4., My-mind-A.I., VigilE.S.A.-Enhanced-Security, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive_Microservice, SEEM-Cognitive-Microservice, btc-trading. Only `CFT-v3.0` was `archived=true` at Sweep-207.
- **4.2 weight:** `models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf` (~77,844,704 bytes) remains in git. Do not delete from history.
- **4.2 misplaced workflow:** `src/.github/workflows/ci.yml` is not a repository workflow. Do not promote it.
- **My-mind-A.I. CI:** replace or disable `.github/workflows/python-package-conda.yml`. Latest known failure run 36851325554 on `b886113`. Not re-fetched.
- Repair or retire operator-owned `.github/workflows/security_pipeline.yml` on VigilE.S.A.-Enhanced-Security. Sweep-193 recorded run 36863696288 failure. Not re-fetched.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Not executed.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277`.
- Fix or close `sovereign-clean-room` pull request branch `seem-completion-pass`. Run 37087542135 failed at `Run tests` on `9412b339`. Not re-fetched.
- Enable secret scanning on sovereign-clean-room (prior API 404). Not re-fetched.
- Enable or accept absence of code scanning on forge-aegis and Digital_Double_virtual_workforce (API 404 no analysis, Sweep-207).
- Expand adl-capability-matrix to live search census (83 non-fork).
- Audit remaining private default-RESEARCH names. Trees not read this cycle.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes from recent sweeps

- Sweep-209: `seem-sunder-bridge` RESEARCH claim ≤1 confirmed. Local pytest 13 passed. CI extended to run `python -m bridge`. Commit `a72abac9`. PR #2 not merged. Pins not re-read. Stopped.
- Sweep-208: `digital-double-mobile` SUPERSEDED claim 0 confirmed. Local pytest 10 passed. Critical Dependabot #30 and #8 remain open. Archive flag false.
- Sweep-207: four-pillar live re-fetch. Exit criteria failed on #13 and unfinished archive/release/private-tree work.
