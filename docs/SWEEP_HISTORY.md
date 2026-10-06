# Sweep History

## Sweep-246 — 2026-10-06 AtomicNexusAI deploy exit 126

- Timestamp: 2026-10-06 17:07Z. Scope: named next gap from PASS-2026-10-06-244, not a new random draw.
- Parent pass yaml: PASS-2026-10-06-244. PASS-2026-10-06-245 remains an index-only entry and did not close this gap.
- Run 37492591439 conclusion failure. Job deploy 112368862487. Head `663df6a76400a1c5ef36bc3bceedfd270cca2881`.
- Log: requirements installed, attack simulator completed, pytest 11 passed, then `./deploy.sh: Permission denied`, exit 126.
- `deploy.sh` is a two-echo stub. Not a production deploy.
- Fix: commit `45a68454b2b661e38ac4abd728dc2bcf0b8f663b` changes the step to `bash deploy.sh`. Claim note commit `f7ec8a0d10a261b4fff2a3b5d507db6b5abef5fa`. Claim cap remains 0.
- Post-fix Actions run not observed in this pass. Do not tag. Do not archive. Do not rewrite history.
- Governance pass file: `docs/passes/PASS-2026-10-06-246.yaml` at commit `0f9c8f3e4a955d898a13b83ca16ab1b5b08f64d9`.
- Portfolio exit criteria not met. Stop.

## Index / PASS-2026-10-06-246

Contract file is `docs/passes/PASS-2026-10-06-246.yaml`.

## Sweep-245 — 2026-10-06 randomized draw

- Timestamp: 2026-10-06 17:10Z. Scope: one repository from the authenticated owner `beyond-repair`.
- Selection: `random.Random(20261006_1700).choice` over the 83-name search payload (`total_count` 83, `incomplete_results` false). Draw: `bloch-coherence-factor2`.
- Discover: tree SHA `77d7063a51784be5ac6e39ca3a616dc73fa578c2`, 31 paths. Modules `model.py`, `operator.py`, `scan.py`. Tests `tests/test_factor2.py`. Workflow `.github/workflows/falsify.yml`. Docs include THEOREM_FACTOR2, MODEL, FALSIFICATION, LINE_FREEZE, CLAIM_STATUS.
- Audit: main CI falsify run 36897260976 success on that head. Releases empty. Branches: `main`, `14J.5F.1-loop-correction` (`09f6902b`). Loop branch not merged and not re-run. Prior failure 36100043944 stands.
- Local verification: `PYTHONPATH=src python3 -m pytest -q` on clone of `77d7063a` — 11 passed, 0 failed.
- Classification: RESEARCH. Claim ≤ 1 retained. Factor of two is a structural ratio of the classical two-mode reduction, not a constant of nature, not device stability, not thrust.
- Actions: updated `CLAIM_STATUS.md` on the subject repo. Updated the three governance docs. No deletion. No history rewrite. No archive flag. No tag. No claim elevation.
- Termination for this repository: not marked complete. Loop branch unaudited. Portfolio exit criteria not met. Stop.

## Sweep-244 — 2026-10-06 master directive verification

- Timestamp: 2026-10-06 16:14Z. Scope: authenticated owner `beyond-repair` (id 132061760). One governed sweep. No loop.
- Discovery: public_repos 78. Search `user:beyond-repair` total_count 83, incomplete_results false. Private rows: 9. Forks: 0.
- Named next gap from PASS-2026-10-06-243: GAP-ATOMICNEXUS-CI-UNOBSERVED. Closed for the test pipeline only.
- AtomicNexusAI head `663df6a76400a1c5ef36bc3bceedfd270cca2881`: CI/CD Pipeline run 37492591479 success; Security Audit run 37492591448 success; Deploy run 37492591439 failure. Classification remains RESEARCH, claim cap 0.
- forge-aegis main `e7188d529739652a2dd6264bd3d328c1f72e60e5`. Run 37258127100 success. Releases empty. Code scanning 404. PASS WITH FINDINGS. Claim cap remains software sketch, not host integrity.
- sovereign-clean-room main `4878918cf9f95d3c19e1890bef6d2fd6713e0a16`. Latest five fetched Python-test runs are on `seem-completion-pass`, not main. Releases empty. Main-head CI success inherited from Sweep-241 run 37064696194. PASS WITH FINDINGS.
- BlockSwarm main `6e90f6f85c0969fa8a262a70ceba833d618a22db`. Foundry run 36859452185 success. Releases empty. Tag `v0.5.0-sagf` not created. PASS WITH FINDINGS.
- Digital_Double_virtual_workforce main `24e6a29fd26c03900a8d98634d6683996eabdac4`. CI run 36861489156 success. Releases empty. Dependabot #13 not re-fetched. Readiness FAIL until that alert is observed fixed.
- Actions performed: governance documentation only. No deletion. No history rewrite. No archive flag. No tag. No claim elevation.
- Pass and operator commit: `298e2f202782870872bf6aff2a2db3cf0f82701a`. Exit criteria not met. Stop.

## Index / PASS-2026-10-06-245

Body is the Sweep-245 section above. No separate pass yaml this cycle.

## Index / PASS-2026-10-06-244

Body is the Sweep-244 section above. Contract file is `docs/passes/PASS-2026-10-06-244.yaml`.

Prior index entries from PASS-2026-10-06-243 back through PASS-2026-10-01-167 remain in git blob `c16e2da9366e64c99b83d94366ebd51a142e1815`. Not deleted as truth. Working copy keeps the two latest sweep bodies and the 246/245/244 index lines so this file stays readable. Full older index is recoverable from that blob.
