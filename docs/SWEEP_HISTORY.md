# Sweep History

## Sweep-243 — 2026-10-06 governance pytest pin

- Selection: recorded next objective GAP-DEPENDABOT-GOVERNANCE-PYTEST from PASS-2026-10-06-240. Sweep-242 did not close it.
- Alert: ADL-Governance Dependabot #1 still open. pytest GHSA-6w46-j5rx-g56g / CVE-2025-71176. Vulnerable range < 9.0.3. Manifest requirements.txt. Scope runtime. First patched identifier 9.0.3.
- Pre-head: c7befdd7994ce04c039ac0c82c91a395b20a5104. Pin before change pytest==8.3.5.
- Action: bump only pytest to 9.0.3. Workflow file not edited. No archive. No tag. No history rewrite. No claim elevation.
- Local verification: pytest 9.0.3 against tests/test_check_passes.py — 17 passed. scripts/check_passes.py PASS on 59 yaml files including PASS-2026-10-06-242.
- Commit: `48f4a2d3ab8aa88b77158a902b136740e55ef488` for the pin and pass file. History heading is this commit. Remote Dependabot closure and governance-ci are not yet observed.
- Exit: pin aligned to the advisory patched identifier. Portfolio termination not met. Stop. Do not loop.

## Index / PASS-2026-10-06-243

Body is the Sweep-243 section above. Contract file is `docs/passes/PASS-2026-10-06-243.yaml`.


## Sweep-242 — 2026-10-06 random completion sweep

- Selection: `random.SystemRandom().choice` over 80 names from search `user:beyond-repair` total_count 83, incomplete_results false, excluding `ADL-Governance`, `aegis-repo-graph`, and `sunder`.
- Subject: `AtomicNexusAI` (public, main). Pre-head `e5434837c4d13676ff3e834ad012c55ae62b48c7`. Tree not truncated (153 entries).
- Classification: **RESEARCH**. Claim cap 0. Inherited ARCHIVED-target row corrected. GitHub archived flag remains false.
- Discover: README, CLAIM_STATUS, ARCHIVED.md, pyproject, CI workflow, tests. Actions list total_count 0. Releases empty. Tags empty.
- Local pytest before workflow edit: 11 passed.
- Finding: workflow pinned Python 3.8 and `flake8 .` while `requires-python` is >=3.10 and orphan root trees are not the Claim-0 surface.
- Action: CI job installs `.[dev]` on Python 3.11 and runs `pytest -q`. Claim status and README aligned. Orphan trees not deleted.
- Commits: `453b36085ef8d4c9ea195f1889980232c268d0ee`, `35850a059a8c12c23948aad6c15ba2810c722cce`, `663df6a76400a1c5ef36bc3bceedfd270cca2881`.
- Remote CI on the new head not yet observed. No tag. No archive. No history rewrite. No claim elevation.
- Exit: subject re-audited and claim-capped. Portfolio termination not met. Stop. Do not loop.

## Index / PASS-2026-10-06-242

Body is the Sweep-242 section above. Contract file is `docs/passes/PASS-2026-10-06-242.yaml`.


## Index / PASS-2026-10-06-241

Body is the Sweep-241 section in git history before this index repair. Contract file is `docs/passes/PASS-2026-10-06-241.yaml`.

## Index / PASS-2026-10-06-240

Body is the Sweep-240 section in git history. Contract file is `docs/passes/PASS-2026-10-06-240.yaml`.

## Index / PASS-2026-10-06-239

Contract file is `docs/passes/PASS-2026-10-06-239.yaml`.

## Index / PASS-2026-10-06-238

Contract file is `docs/passes/PASS-2026-10-06-238.yaml`.

## Index / PASS-2026-10-06-237

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-06-236

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-06-235

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-06-234

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-06-233

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-06-231

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-232

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-230

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-229

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-228

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-227

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-226

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-225

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-224

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-223

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-05-222

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-04-220

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-04-219

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-04-218

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-04-215

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-04-214

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-03-213

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-03-212

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-03-211

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-03-210

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-02-207

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-02-206

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-02-205

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-02-204

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-02-203

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-199

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-198

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-197

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-196

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-195

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-194

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-193

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-192

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-191

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-190

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-189

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-188

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-185

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-184

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-183

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-182

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-179

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-176

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-173

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-170

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-168

Body not inlined. Source is the matching file under `docs/passes/`.

## Index / PASS-2026-10-01-167

Body not inlined. Source is the matching file under `docs/passes/`.
