# Sweep History

## Sweep-210 — 2026-10-03 scale-functional-I function audit

- Selection: persisted next action from PASS-2026-10-02-207. Sweeps 208 and 209 did not close it.
- Subject: `scale-functional-I` head `9768280b4d6eb039defa7072cabf243f3e3740b2`.
- Classification unchanged: RESEARCH. No cluster and no claim cap assigned. Locked matrix remains 67 rows.
- Discover: module functions `dumbbell_mask`, `perimeter`, `main`. Tests import and execute only the first two. `eigvalsh` is imported and unused.
- Witness: `python3 -m unittest tests.test_scale_functional` → 1 test OK. Families (8, 5) and (10, 6): I strictly decreases; finite-difference beta_I negative.
- Actions: `matrix/function_audit_scale_functional_I.json` and test in `adl-capability-matrix` commit `b3b6412b391149a82bd63a263b97d639b6ccf2a7`. Local pytest 19 passed. No continuum, selected W, thrust, or 0.08 comparison claimed.
- Exit: GAP-SCALE-FUNCTIONAL-I-AUDIT closed at test-executed surface only.

## Index / PASS-2026-10-03-210

Body is the Sweep-210 section above.

## Sweep-209 — 2026-10-03 portfolio completion sweep

- Selection: `random.Random(20261003).choice` over 82 names from search `user:beyond-repair` (`incomplete_results=false`), excluding `ADL-Governance`.
- Subject: `seem-sunder-bridge` (public, `main`, pre-head `6f6d5b07207f5de85ce0f629379dc1ac5541fb5b`, post-head `a72abac9f6b8bcb1019469802f5baf55e9082f07`).
- Classification: RESEARCH confirmed. Claim ≤1 MODULE_SURFACE. Q-003 is a contract checker, not runtime interop.
- Discover: `bridge/` contract, check, engine, witness; frozen 2026-10-01 and 2026-10-02 witnesses; tests; CI. No foreign imports.
- Audit: main CI run 37071653220 success ran pytest only, not `python -m bridge`. Open dependabot PR #2. Pins not re-read this cycle.
- Actions: CI step `python -m bridge`; test that local defs stay disjoint from the foreign-op ban; `CLAIM_STATUS.md`; README CI sentence. No version bump. No tag. No archive. No history rewrite. No merge of PR #2.
- Test: local Python 3.11 `pytest -q` → 13 passed. `python -m bridge` → OK / exit 0. Post-push CI conclusion not available at record time.
- Exit: termination conditions not met. Sweep stopped.

## Index / PASS-2026-10-03-209

Index only. Body is the Sweep-209 section above. Not a second execution.

## Sweep-208 — 2026-10-03 portfolio completion sweep

- Subject: `digital-double-mobile`. SUPERSEDED claim 0. Local pytest 10 passed. Critical Dependabot #30 and #8 open. Archive flag false. Full body remains in git history before this condensation.

## Index / PASS-2026-10-03-208

Index only. Not a second execution.

## Sweep-207 — 2026-10-03 portfolio completion sweep

- Four-pillar live re-fetch. Exit criteria failed. Full body remains in git history.

## Index / PASS-2026-10-03-207

Index only. Not a second execution.

Earlier sweep bodies remain in git history before this condensation.

## Heading index (not new executions)

These headings exist only so `scripts/check_passes.py` can find every persisted yaml id. Bodies remain in `docs/passes/` or earlier git history.

## Index / PASS-2026-10-01-167

Index only. Not a new execution.

## Index / PASS-2026-10-01-168

Index only. Not a new execution.

## Index / PASS-2026-10-01-170

Index only. Not a new execution.

## Index / PASS-2026-10-01-173

Index only. Not a new execution.

## Index / PASS-2026-10-01-176

Index only. Not a new execution.

## Index / PASS-2026-10-01-179

Index only. Not a new execution.

## Index / PASS-2026-10-01-182

Index only. Not a new execution.

## Index / PASS-2026-10-01-183

Index only. Not a new execution.

## Index / PASS-2026-10-01-184

Index only. Not a new execution.

## Index / PASS-2026-10-01-185

Index only. Not a new execution.

## Index / PASS-2026-10-01-188

Index only. Not a new execution.

## Index / PASS-2026-10-01-189

Index only. Not a new execution.

## Index / PASS-2026-10-01-190

Index only. Not a new execution.

## Index / PASS-2026-10-01-191

Index only. Not a new execution.

## Index / PASS-2026-10-01-192

Index only. YAML exists. Narrative body remains in git history. Not a new execution.

## Index / PASS-2026-10-01-193

Index only. Not a new execution.

## Index / PASS-2026-10-01-194

Index only. Not a new execution.

## Index / PASS-2026-10-01-195

Index only. Not a new execution.

## Index / PASS-2026-10-01-196

Index only. Not a new execution.

## Index / PASS-2026-10-01-197

Index only. Not a new execution.

## Index / PASS-2026-10-01-198

Index only. Not a new execution.

## Index / PASS-2026-10-01-199

Index only. Not a new execution.

## Index / PASS-2026-10-02-200

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-201

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-202

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-203

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-204

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-205

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-206

Index only. Body remains in git history. Not a second execution.

## Index / PASS-2026-10-02-207

Index only. YAML exists. Narrative body remains in git history. Not a second execution.
