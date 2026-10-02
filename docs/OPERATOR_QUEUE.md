# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-201)

- **Security escalation:** Digital_Double_virtual_workforce Dependabot alert #13 remains open as of Sweep-200. Package `form-data` in `digital_double/package-lock.json`, GHSA-fjxv-7rqg-78g4 / CVE-2025-7783, severity critical, vulnerable range `>= 4.0.0, < 4.0.4`, patched 4.0.4. Not re-fetched Sweep-201. Agent did not bump the lockfile.
- Apply GitHub `archived=true` to documented ARCHIVED/SUPERSEDED targets, including **My-mind-A.I.** (SUPERSEDED, default branch `main2`, flag still false at Sweep-201), **VigilE.S.A.-Enhanced-Security**, genieGPT, ftmA.I.bot, smart_home_BCI, potential-garbanzo, -Py2APK-main, fantom_trading_bot_2, Digital_Double_Virtual_Workforce_4., Digital_Double_Virtual_Workforce_4.2, DigitalDoubleVirtualWorkforce3.5, CFT-v3.1, Agent-Snake, SEEM-Cognitive_Microservice, SEEM-Cognitive-Microservice, btc-trading. Census still shows `archived=true` only on `CFT-v3.0`.
- **My-mind-A.I. CI:** replace or disable `.github/workflows/python-package-conda.yml`. It calls `conda env update --file environment.yml` and expects `$CONDA` after `actions/setup-python`. `environment.yml` is not in the tree. Latest run 36851325554 failed on `b886113`. A stdlib unittest workflow would be sufficient. Requires `workflow` scope. Agent did not edit the workflow file.
- Repair or retire operator-owned `.github/workflows/security_pipeline.yml` on VigilE.S.A.-Enhanced-Security. Sweep-193 recorded run 36863696288 failure. Not re-fetched Sweep-201.
- Tag product releases on ACTIVE repos (BlockSwarm, forge-aegis, Digital_Double_virtual_workforce, sovereign-clean-room). Sweep-200: tags API empty on all four.
- Rotate / remove committed `.env` on digital-double-mobile; resolve Dependabot HIGH alerts. Not re-fetched.
- Decide disposition of `sovereign-clean-room` branch `fix/pynacl-1.6.2-cve-2025-69277`. Not re-listed.
- Enable secret scanning on sovereign-clean-room (prior API 404). Not re-fetched.
- Enable or accept absence of code scanning on forge-aegis (prior API 404). Not re-fetched.
- Expand adl-capability-matrix to live 82-row census.
- Audit remaining private default-RESEARCH names: `atomicdreamlabs`, `blacksite`, `mendthegame`, `potential-garbanzo`, `SovereignOS`, `test`.
- Operator review of any claim-level elevation requests.
- History rewrite or force-push: never by agent. Repository deletion: never by agent.

## Residual notes from recent sweeps

- Sweep-201: selected `My-mind-A.I.`. SUPERSEDED confirmed. Local unittest passed. Conda CI still failed. `CLAIMS.md` added. No archive flag.
- Sweep-200: census 82 reconfirmed. Phase-3 CI success retained on prior heads. Dependabot critical #13 still open. Tags empty. No product mutation.
- Sweep-193: VigilE.S.A.-Enhanced-Security documentary ARCHIVED. Local cargo test 19 passed. claim0-tests workflow added. Security Pipeline left failing. No archive flag.
