# Operator Queue

## Sweep-273 additions (2026-10-07)

- **Digital_Double_virtual_workforce:** Dependabot alert 13 remains open (`form-data`, CVE-2025-7783, critical, manifest `digital_double/package-lock.json`, development scope, matched range `>= 4.0.0, < 4.0.4`, first patched `4.0.4`). Do not mark the repository security-clean. Lockfile bump is allowed only after a human reviews the npm tree. Do not dismiss the alert from an agent.
- High open alerts on the same lockfile remain operator-owned (observed this sweep: 160, 159, 155, 153, 147, 122, 112, 111). Nested `digital_double/` manifests may be the stale path. Do not delete the nested tree from an agent.
- Medium pytest alert 168 (CVE-2025-71176, `< 9.0.3`) on `digital_double/pyproject.toml` is operator-owned. Do not bump it from this sweep.
- Do not merge `seem-completion-pass` (`d6f13042`) or `fix/pynacl-1.6.2-cve-2025-69277` (`f65d7db6`) on sovereign-clean-room from an agent.
- Do not tag releases for forge-aegis, sovereign-clean-room, BlockSwarm, or Digital_Double_virtual_workforce from an agent.
- Do not set GitHub `archived=true` on SUPERSEDED or archive-queue repositories from an agent.
- Code scanning is not enabled (API 404 no analysis) on forge-aegis, BlockSwarm, and Digital Double. Secret scanning is disabled on sovereign-clean-room (404). Enabling either is operator-only.
- Search `total_count` 83 versus profile `public_repos` 78 remains. Private names in the search payload: 9. Do not delete names to force a match.

## Sweep-272 additions (2026-10-07)

- **Project-Cold-Boot:** do not tag a release from an agent. Do not set GitHub `archived=true`. Do not promote RESEARCH to ACTIVE. Godot smoke (`tools/smoke_test.sh`) was not executed in Sweep-272 because the sweep host had no Godot binary. A green `structure` workflow is not a playable-slice or DLRSE proof. Commercial 1.0, Steam packaging, and audio remain operator/content work.

## Sweep-271 additions (2026-10-07)

- Same Digital Double critical alert and unmerged clean-room branches as Sweep-273. Retained so the queue does not drop the prior instruction.

## Sweep-270 additions (retained)

- **DigitalDoubleVirtualWorkforce3.5:** do not set GitHub `archived=true` from an agent. Classification SUPERSEDED is documentary. Canonical successor remains `Digital_Double_virtual_workforce`. Do not tag a release. Do not merge this tree into the successor from an autonomous sweep. Do not treat a green `supersede-guard` run as CAP proof, torch quantization, or product parity.
- Archive-queue row for this name stays operator-owned.

Prior queue bodies before Sweep-270 are not in this blob. Sweep-270 recorded that loss. Restore from git history if an operator needs them. This file does not rewrite history.
