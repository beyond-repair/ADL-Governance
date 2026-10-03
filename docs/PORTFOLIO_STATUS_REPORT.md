# Portfolio Status Report

**Updated:** 2026-10-03 (autonomous Sweep-208)
**Project / Version:** ADL Portfolio Governance / Sweep-208
**Objective:** Randomly select one repository, discover and audit it, apply only safe idempotent changes, and record state.
**Authenticated owner:** `beyond-repair` (id 132061760)
**Governing source:** `beyond-repair/ADL-Governance`
**Evidence rule:** Code > Documentation > Roadmap.
**Assumptions:** A1 user sweep contract. A2 empirical GitHub search, tree, Actions, Dependabot, and local pytest this cycle.

## Selection

| Field | Value |
|-------|--------|
| Method | `random.SystemRandom().choice` over 83 names from search `user:beyond-repair` (`incomplete_results=false`) |
| Subject | `digital-double-mobile` |
| Visibility | public |
| Default branch | `main` |
| Pre-head | `2d9a885e986999f76df1b97a2fd6f49e1e20252a` |
| Classification | SUPERSEDED (confirmed, not newly assigned) |
| Claim | 0 |
| Successor | `Digital_Double_virtual_workforce` |
| GitHub archived | false |

Census this cycle: search index 83 non-fork names. Prior Sweep-207 owned-total split (78 public list + 9 private = 87 including 4 forks) was not re-paginated.

## Subject discovery

Claim-0 surfaces: `dd_mobile/` FastAPI in-memory tasks, `tests/` (app, metrics, main smoke), `scripts/superseded_guard.py`, Vite `src/` (not executed this cycle), historical `backend/api/` and Flutter leftovers under `frontend/`.

Working-tree `.env` absent on a depth-1 clone. Empty historical stubs remain: `ar-view.html`, `dashboard.html`, `workspace.html`, `settings.html`, `favicon.ico`, `icons.png`, `distressed-metal-bg.png`.

Duplicate names still exist (`Digital-Double_Mobile`, `Digital_Double_virtual_workforce`, private 4.x). Not merged. Not deleted.

## Verification

| Check | Result |
|-------|--------|
| Local `python3 -m pytest -q` | 10 passed, 1 Starlette deprecation warning |
| Local `scripts/superseded_guard.py` | PASS |
| Prior main CI | superseded-guard run 37050163229 success on `2d9a885` |
| This cycle CI change | workflow now installs requirements and runs pytest before the banner guard. Conclusion not available at record time. |
| Dependabot critical | #30 `protobufjs` GHSA-xq3m-2v4x-88gg; #8 `form-data` GHSA-fjxv-7rqg-78g4. Both open. |
| Dependabot high (not exhaustive) | #85 `browserslist`, #83 `nanoid`, #78 `postcss` |

Lockfile was not bumped. Archive flag was not set. No release tag.

## Exit criteria

Not satisfied for the subject or the portfolio.

Failed: GitHub archive flag still false; critical Dependabot open; duplicate Digital Double implementations remain; post-push CI conclusion not yet observed; `npm run build` not re-run.

Satisfied this cycle: classification and claim cap confirmed; working-tree secret file absent; local pytest green; governance files updated; destructive actions queued.
