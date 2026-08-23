# Operator Queue

**Last updated:** 2026-08-23T19:00Z (autonomous sweep)

Destructive or account-level actions that require human operator. Agent places items here; does not execute.

## Immediate (P0)

| Action | Repo / Target | Command / Notes | Status |
|--------|---------------|-----------------|--------|
| Create and push git tag | BlockSwarm | `git tag -a v0.5.0-sagf -m "SAGF production candidate" && git push origin v0.5.0-sagf` | PENDING |
| Archive batch | RepoRover-, genieGPT, Agent-Snake, Auto_Legion, AtomicNexusAI | `gh repo archive beyond-repair/<name>` | PENDING |
| Archive | Digital-Double_Mobile (if confirmed empty) | after content check | PENDING |

## High (P1)

| Action | Repo / Target | Notes | Status |
|--------|---------------|-------|--------|
| Confirm CI green on main | forge-aegis | Inspect Actions tab; fix if red | PENDING |
| Confirm CI green + CLI stable | sovereign-clean-room | Run local pytest + CLI smoke if possible | PENDING |
| Decide product canonical | Digital_Double_* family | Public: Digital_Double_virtual_workforce; private 4.2 is newer candidate | DECIDED (see STATUS) |

## Medium

| Action | Notes |
|--------|-------|
| Profile README refresh | Point at ACTIVE set only |
| Archive remaining FROZEN/legacy per registry | After markers verified |
| Security scan critical issues | None flagged as critical in last census |

## Completed (recent)

- BlockSwarm root cleanup, tests, CI workflow, release docs (agent + prior)
- Digital Double role assignment
- SEEM-* classified SUPERSEDED → sovereign-clean-room

---

**Rule:** Never delete repos or rewrite history. Prefer archive + supersede notes.
