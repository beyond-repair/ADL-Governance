#!/usr/bin/env python3
"""Non-vacuous governance pass checks.

Validates every docs/passes/*.yaml parses as YAML and that
docs/SWEEP_HISTORY.md heading-names every persisted pass id, including the latest.

Does not invent missing historical pass bodies. Markdown records are ignored.
Accepts the two observed schemas:
  - nested PASS.id
  - flat sweep + date (PASS-168)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

PASS_NAME = re.compile(r"^PASS-(\d{4}-\d{2}-\d{2})-(\d+)\.yaml$")
HEADING = re.compile(r"^## .+\s/\s(PASS-\d{4}-\d{2}-\d{2}-\d+)\b", re.M)
REQUIRED_NESTED = ("PASS", "STATE", "OBJECTIVE", "VERIFICATION", "NEXT")


def pass_id_from_name(name: str) -> str:
    match = PASS_NAME.match(name)
    if not match:
        raise SystemExit(f"unexpected pass filename: {name}")
    return f"PASS-{match.group(1)}-{int(match.group(2))}"


def latest_id(names: list[str]) -> str:
    parsed = []
    for name in names:
        match = PASS_NAME.match(name)
        if not match:
            raise SystemExit(f"unexpected pass filename: {name}")
        parsed.append((match.group(1), int(match.group(2)), name))
    if not parsed:
        raise SystemExit("no pass YAML files; check is vacuous")
    parsed.sort()
    date, number, _name = parsed[-1]
    return f"PASS-{date}-{number}"


def check_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    if not isinstance(data, dict) or not data:
        raise SystemExit(f"{path.name}: YAML root is not a non-empty mapping")
    match = PASS_NAME.match(path.name)
    if match is None:
        raise SystemExit(f"{path.name}: filename does not match PASS-YYYY-MM-DD-N.yaml")
    expected = f"PASS-{match.group(1)}-{int(match.group(2))}"
    if "PASS" in data:
        missing = [key for key in REQUIRED_NESTED if key not in data]
        if missing:
            raise SystemExit(f"{path.name}: nested schema missing {missing}")
        pass_id = data["PASS"].get("id") if isinstance(data["PASS"], dict) else None
        if pass_id != expected:
            raise SystemExit(f"{path.name}: PASS.id {pass_id!r} != {expected}")
        return
    if "sweep" in data and "date" in data:
        if str(data["date"]) != match.group(1) or int(data["sweep"]) != int(match.group(2)):
            raise SystemExit(f"{path.name}: flat sweep/date does not match filename")
        return
    raise SystemExit(f"{path.name}: neither nested PASS schema nor flat sweep schema")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    passes = root / "docs" / "passes"
    history = root / "docs" / "SWEEP_HISTORY.md"
    files = sorted(passes.glob("PASS-*.yaml"))
    if not files:
        print("FAIL: docs/passes has no PASS-*.yaml", file=sys.stderr)
        return 1
    for path in files:
        check_file(path)
    ids = [pass_id_from_name(path.name) for path in files]
    latest = latest_id([path.name for path in files])
    body = history.read_text(encoding="utf-8")
    named = set(HEADING.findall(body))
    missing = [pass_id for pass_id in ids if pass_id not in named]
    if missing:
        print(
            f"FAIL: SWEEP_HISTORY.md missing sweep headings for {missing}; named={sorted(named)}",
            file=sys.stderr,
        )
        return 1
    if latest not in named:
        print(
            f"FAIL: SWEEP_HISTORY.md has no sweep heading for {latest}; named={sorted(named)}",
            file=sys.stderr,
        )
        return 1
    print(f"PASS: {len(files)} yaml files parsed; history headings name all ids including {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
