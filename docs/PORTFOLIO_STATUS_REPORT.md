# Portfolio Status Report

**Updated:** 2026-10-06 17:07Z (Sweep-246)
**Project / Version:** ADL Portfolio Governance / Sweep-246
**Objective:** Close GAP-ATOMICNEXUS-DEPLOY-FAILURE from PASS-2026-10-06-244. Fetch the failed job log. Apply the smallest matching fix. Do not raise claims.
**Authenticated owner:** `beyond-repair` (id 132061760). Profile `public_repos` 78. Search `user:beyond-repair` `total_count` 83, `incomplete_results` false.
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user directive requires a persisted pass. A2 run 37492591439 is the Sweep-244 cited failure. A3 Sweep-245 classifications outside this gap remain inherited.

## Sweep-246 result

Selected gap: `GAP-ATOMICNEXUS-DEPLOY-FAILURE` on `AtomicNexusAI`.
Classification: RESEARCH. Claim level remains 0. Not elevated.
Exit criteria for the portfolio were not met.
No repository was deleted. No history was rewritten. No archive flag was flipped. No tag was created.

| Field | Observation |
|-------|-------------|
| Failed run | 37492591439, job 112368862487, conclusion failure |
| Head of that run | `663df6a76400a1c5ef36bc3bceedfd270cca2881` |
| Failure | `./deploy.sh: Permission denied`, exit 126, after in-job pytest 11 passed |
| Script | `deploy.sh` echoes only |
| Fix commit | `45a68454b2b661e38ac4abd728dc2bcf0b8f663b` changes the step to `bash deploy.sh` |
| Claim note commit | `f7ec8a0d10a261b4fff2a3b5d507db6b5abef5fa` |
| Post-fix Actions | not observed in this pass |
| Readiness | PASS WITH FINDINGS |

Sweep-245 draw of `bloch-coherence-factor2` remains recorded and was not re-audited. Digital_Double Dependabot #13 was not re-fetched. Accounting 78 vs 83 was not forced.

Sweep-246 stop. Portfolio exit criteria not met. Do not treat the invocation change as a release.
