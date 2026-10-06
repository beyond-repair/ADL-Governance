# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Residual notes from Sweep-243

Dependabot alert #1 was open on pytest 8.3.5. requirements.txt now pins pytest==9.0.3 (GHSA-6w46-j5rx-g56g, first patched identifier). Local pytest 17 passed. governance-ci run 37493687709 succeeded on 58abab2d after the history heading was added. Run 37493586060 failed before that heading existed. Do not treat alert #1 as fixed until GitHub marks it fixed. Do not edit governance-ci.yml for this pin. No archive. No tag. No history rewrite. No claim elevation. PASS body: `docs/passes/PASS-2026-10-06-243.yaml`.

## Residual notes from Sweep-242

Random subject `AtomicNexusAI`. Classification RESEARCH, claim 0. Do not flip the GitHub archive flag. Do not delete orphan root trees (`utils/`, `security/`, `ecurity/`, `github/`, `**LICENSE**`). Do not treat the CI workflow edit as a green Actions conclusion until a run is fetched. No tag. No history rewrite. No claim elevation. PASS body: `docs/passes/PASS-2026-10-06-242.yaml`.

## Open items still open

- Prior residual notes from Sweep-241 through Sweep-233 remain in git at blob `bd2acc18ab1e36895ca8cb2937fc5a085c5c0fd3`. Not deleted as truth; this commit keeps the still-actionable open items below.
- **aegis-repo-graph catalog expansion:** operator-only. Do not silently add the 18 observation-only names or delete catalog-only names. Spelling variant is not a rename.
- **Digital_Double_virtual_workforce Dependabot alert #13:** re-fetched Sweep-235, still open. `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Manifest `digital_double/package-lock.json`. Scope development. Vulnerable range `4.0.0 inclusive through versions before 4.0.4`. Patched identifier 4.0.4. Not patched. Lockfile edit is allowed later only as a verified dependency bump, not in this cycle.
- **digital-double-mobile secret scanning alert #1:** not re-fetched. Prior record: OpenRouter API key, historical path `.env`, publicly leaked, validity unknown. Rotate and revoke. Do not rewrite history.
- **digital-double-mobile Dependabot critical #30 and #8:** not re-fetched. Archive-queue gate still requires credential rotation first.
- **RepoRover- and Code_Generation_AI_Program archive flags:** inherited ARCHIVED. `archived=true` still false. Not executed.
- **BlockSwarm README tag sentence:** `v0.5.0-sagf` remains unverified. Releases list empty this cycle. Do not create the tag to match the sentence.
- **forge-aegis license:** `License TBD` remains operator-only.
- **The-Origin-Point-Hypothesis. license:** absent. Operator-only. Do not invent a license in this sweep.
- **sovereign-clean-room branches** `seem-completion-pass` and `fix/pynacl-1.6.2-cve-2025-69277`: not merged. Secret scanning still disabled.
- Product tags, code scanning enablement, secret rotation, and GitHub archive flags remain operator-only. History rewrite and repository deletion remain forbidden.
- Accounting: user `public_repos` 78 vs search total 83. Do not delete repositories to force equality.
- **sunder unused dependencies:** `pynacl` and `httpx` are declared and unused. Removal is optional and was not done.
- **ADL-Governance Dependabot alert #1:** pin moved to 9.0.3 in commit 48f4a2d3. Closure not re-fetched in the operator note itself. Do not mark fixed until the alert state is fixed.
