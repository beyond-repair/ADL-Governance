# Repository Lifecycle Policy

## States

```text
CREATE → ACTIVE or RESEARCH
ACTIVE → FROZEN | SUPERSEDED | ARCHIVED
RESEARCH → FROZEN | SUPERSEDED | ARCHIVED | (rare) ACTIVE
SUPERSEDED → ARCHIVED
ARCHIVED → (terminal; un-archive only with written justification)
```

## Create

1. Name, description, license, README required.
2. Classification set in repository_registry.md within 7 days.
3. ACTIVE repos must add CI within 30 days.

## Promote to ACTIVE

- Documented purpose
- Tests + CI green
- Reference to ADL-Governance
- SECURITY.md present

## Supersede

1. Banner at top of README naming successor.
2. Stop feature work.
3. Migrate unique docs if needed.
4. Close or migrate issues.
5. Archive when stable.

## Archive

1. ARCHIVED.md in repo root.
2. Archive via GitHub (read-only).
3. Do not delete history.

## Versioning

- SemVer for ACTIVE libraries/services.
- Research repos: date-stamped releases optional.
