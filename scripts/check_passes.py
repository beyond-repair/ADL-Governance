#!/usr/bin/env python3
"""Non-vacuous governance pass checks.

Validates every docs/passes/*.yaml parses as YAML and that
docs/SWEEP_HISTORY.md heading-names every persisted pass id, including the latest.

Does not invent missing historical pass bodies. Markdown records are ignored.
Contract sidecars named PASS-YYYY-MM-DD-N.contract.yaml are parsed and must use
the nested schema, but they do not replace the canonical file in the latest-id
or heading check. Accepts the two observed schemas:
  - nested PASS.id
  - flat sweep + date (PASS-168)

docs/passes/HEADINGS.md is concatenated into the heading search when present.
It is an index supplement. It does not replace SWEEP_HISTORY.md.

Usage:
  python scripts/check_passes.py [ROOT]

ROOT defaults to the repository that contains this script. There is no
config file. This checker does not enforce claim levels or the constitution.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

PASS_NAME = re.compile(r"^PASS-(\d{4}-\d{2}-\d{2})-(\d+)\.yaml$")
CONTRACT_NAME = re.compile(r"^PASS-(\d{4}-\d{2}-\d{2})-(\d+)\.contract\.yaml$")
HEADING = re.compile(r"^## .+\s/\s(PASS-\d{4}-\d{2}-\d{2}-\d+)\b", re.M)
REQUIRED_NESTED = ("PASS", "STATE", "OBJECTIVE", "VERIFICATION", "NEXT")


def pass_id_from_name(name: str) -> str:
    match = PASS_NAME.match(name) or CONTRACT_NAME.match(name)
    if not match:
        raise SystemExit(f"unexpected pass filename: {name}")
    return f"PASS-{match.group(1)}-{int(match.group(2))}"


def is_contract(name: str) -> bool:
    return CONTRACT_NAME.match(name) is not None


def latest_id(names: list[str]) -> str:
    parsed = []
    for name in names:
        if is_contract(name):
            continue
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
    match = PASS_NAME.match(path.name) or CONTRACT_NAME.match(path.name)
    if match is None:
        raise SystemExit(
            f"{path.name}: filename does not match PASS-YYYY-MM-DD-N.yaml "
            "or PASS-YYYY-MM-DD-N.contract.yaml"
        )
    if is_contract(path.name) and "PASS" not in data:
        raise SystemExit(f"{path.name}: contract sidecar requires nested PASS schema")
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
    # Preserved abbreviated stubs are not rewritten. They must still name this pass.
    expected_id = f"PASS-{match.group(1)}-{int(match.group(2))}"
    if data.get("id") == expected_id:
        return
    if "sweep" in data and int(data["sweep"]) == int(match.group(2)):
        return
    raise SystemExit(f"{path.name}: neither nested PASS schema nor flat sweep schema nor preserved stub")


def heading_body(root: Path, history: Path) -> str:
    body = history.read_text(encoding="utf-8")
    extra = root / "docs" / "passes" / "HEADINGS.md"
    if extra.is_file():
        body = body + "\n" + extra.read_text(encoding="utf-8")
    return body


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("usage: python scripts/check_passes.py [ROOT]", file=sys.stderr)
        return 2
    root = Path(args[0]).resolve() if args else Path(__file__).resolve().parents[1]
    passes = root / "docs" / "passes"
    history = root / "docs" / "SWEEP_HISTORY.md"
    if not passes.is_dir():
        print(f"FAIL: {passes} is not a directory", file=sys.stderr)
        return 1
    if not history.is_file():
        print(f"FAIL: {history} is missing", file=sys.stderr)
        return 1
    files = sorted(passes.glob("PASS-*.yaml"))
    if not files:
        print("FAIL: docs/passes has no PASS-*.yaml", file=sys.stderr)
        return 1
    for path in files:
        check_file(path)
    canonical = [path for path in files if PASS_NAME.match(path.name)]
    if not canonical:
        print("FAIL: docs/passes has no canonical PASS-YYYY-MM-DD-N.yaml", file=sys.stderr)
        return 1
    ids = [pass_id_from_name(path.name) for path in canonical]
    latest = latest_id([path.name for path in canonical])
    body = heading_body(root, history)
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
