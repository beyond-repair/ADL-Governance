# Operator Queue

Pending destructive / operator-only actions. Autonomous agent does **not** execute these.

## Open items (as of Sweep-216)

- **Digital_Double_virtual_workforce Dependabot alert #13:** re-fetched open. `form-data` / GHSA-fjxv-7rqg-78g4 / CVE-2025-7783. Manifest `digital_double/package-lock.json`. Scope development. Vulnerable range observed for this alert: `>= 4.0.0, < 4.0.4`, patched identifier 4.0.4. Not patched. Green CI does not close it.
- **Digital_Double_virtual_workforce high Dependabot (sample, not exhaustive):** #160 and #159 `js-yaml` GHSA-2883-xcg3-v3hh / CVE-2026-84375; #155 `browserslist` GHSA-73wf-gq98-2v4g / CVE-2026-73088; #153 `nanoid` GHSA-xwg4-73v4-xw9w / CVE-2026-73086. Development scope. Operator must decide bump versus dismiss.
- **sovereign-clean-room `seem-completion-pass`:** PR #3 still open. Head `d6f13042f4f99cd186761ae438b75c3e4e705f11`. Python tests run 37215829476 success. Prior failures 37214635678 and 37215706600 were float I drift. Not merged. VSA completeness still UNVERIFIED.
- **sovereign-clean-room branch `fix/pynacl-1.6.2-cve-2025-69277`:** still present at `f65d7db6`. Disposition undecided. Not merged.
- **Secret scanning disabled** on `sovereign-clean-room` (API 404). Enabling it is operator-only.
- **DevelopTool-Unified-Dev-Environment archive flag:** classification ARCHIVED / archive queue. `archived=true` still false. Pushed 2026-10-04. Agent did not set the flag.
- Other archive-queue flags remain false. Only `CFT-v3.0` is GitHub-archived.
- Product tags/releases, code scanning enablement, secret rotation, and GitHub archive flags remain operator-only. History rewrite and repository deletion remain forbidden.

## Residual notes from Sweep-216

Census 83 confirmed. Four named subjects re-verified for CI and releases. Portfolio exit criteria failed on critical security and unset archive flags. Sweep stopped.

## Residual notes from Sweep-215

`seem-completion-pass` CI is green on `d6f13042` only. Main was not updated. PR #3 was not merged. Recorded I literals are not cross-runner bit-stable (GAP-SEEM-FLOAT-LOCK).
