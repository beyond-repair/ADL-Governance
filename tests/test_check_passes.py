"""Tests for scripts/check_passes.py.

The live repository corpus is checked as-is. Failure cases use temp roots
so docs/passes and the constitution are not mutated.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_passes", ROOT / "scripts" / "check_passes.py"
)
assert SPEC is not None and SPEC.loader is not None
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def _tree(tmp: Path, files: dict[str, str], history: str) -> Path:
    passes = tmp / "docs" / "passes"
    passes.mkdir(parents=True)
    for name, text in files.items():
        (passes / name).write_text(text, encoding="utf-8")
    (tmp / "docs" / "SWEEP_HISTORY.md").write_text(history, encoding="utf-8")
    return tmp


def _nested(pass_id: str) -> str:
    return (
        "PASS:\n"
        f"  id: {pass_id}\n"
        "STATE: {}\n"
        "OBJECTIVE: {}\n"
        "VERIFICATION: {}\n"
        "NEXT: {}\n"
    )


def test_real_repository_passes(capsys: pytest.CaptureFixture[str]) -> None:
    names = [path.name for path in (ROOT / "docs" / "passes").glob("PASS-*.yaml")]
    assert names, "live corpus must not be empty"
    latest = mod.latest_id(names)
    assert mod.main([]) == 0
    out = capsys.readouterr().out
    assert f"PASS: {len(names)} yaml files parsed" in out
    assert latest in out
    assert latest == mod.latest_id(names)


def test_latest_id_sorts_by_date_then_numeric_suffix() -> None:
    assert mod.latest_id(
        ["PASS-2026-01-01-10.yaml", "PASS-2026-01-01-9.yaml", "PASS-2026-01-02-1.yaml"]
    ) == "PASS-2026-01-02-1"
    assert mod.latest_id(
        ["PASS-2026-01-01-9.yaml", "PASS-2026-01-01-10.yaml"]
    ) == "PASS-2026-01-01-10"


def test_pass_id_strips_leading_zeros() -> None:
    assert mod.pass_id_from_name("PASS-2026-01-01-007.yaml") == "PASS-2026-01-01-7"


def test_nested_and_flat_and_markdown_ignored(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = _tree(
        tmp_path,
        {
            "PASS-2026-01-01-1.yaml": _nested("PASS-2026-01-01-1"),
            "PASS-2026-01-01-2.yaml": "sweep: 2\ndate: 2026-01-01\n",
            "PASS-2026-01-01-9.md": "not yaml and not checked\n",
        },
        "## Index / PASS-2026-01-01-1\n\n## Index / PASS-2026-01-01-2\n",
    )
    assert mod.main([str(root)]) == 0
    out = capsys.readouterr().out
    assert "PASS: 2 yaml files parsed" in out
    assert "PASS-2026-01-01-2" in out


def test_missing_heading_fails(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = _tree(
        tmp_path,
        {"PASS-2026-01-01-1.yaml": _nested("PASS-2026-01-01-1")},
        "# Sweep History\n\nNo pass heading here.\n",
    )
    assert mod.main([str(root)]) == 1
    err = capsys.readouterr().err
    assert "missing sweep headings" in err
    assert "PASS-2026-01-01-1" in err


def test_no_yaml_fails(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    passes = tmp_path / "docs" / "passes"
    passes.mkdir(parents=True)
    (passes / "notes.md").write_text("ignored\n", encoding="utf-8")
    (tmp_path / "docs" / "SWEEP_HISTORY.md").write_text("# none\n", encoding="utf-8")
    assert mod.main([str(tmp_path)]) == 1
    assert "no PASS-*.yaml" in capsys.readouterr().err


def test_missing_history_and_passes_dir(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert mod.main([str(tmp_path)]) == 1
    assert "is not a directory" in capsys.readouterr().err
    passes = tmp_path / "docs" / "passes"
    passes.mkdir(parents=True)
    (passes / "PASS-2026-01-01-1.yaml").write_text(
        _nested("PASS-2026-01-01-1"), encoding="utf-8"
    )
    assert mod.main([str(tmp_path)]) == 1
    assert "is missing" in capsys.readouterr().err


def test_usage_rejects_extra_args(capsys: pytest.CaptureFixture[str]) -> None:
    assert mod.main(["one", "two"]) == 2
    assert "usage:" in capsys.readouterr().err


@pytest.mark.parametrize(
    "name,text,fragment",
    [
        ("PASS-2026-01-01-1.yaml", "{}\n", "non-empty mapping"),
        ("PASS-2026-01-01-1.yaml", "[]\n", "non-empty mapping"),
        ("PASS-2026-01-01-1.yaml", "PASS:\n  id: PASS-2026-01-01-1\n", "nested schema missing"),
        ("PASS-2026-01-01-1.yaml", _nested("PASS-2026-01-01-9"), "PASS.id"),
        ("PASS-2026-01-01-1.yaml", "note: hello\n", "neither nested"),
        ("PASS-2026-01-01-2.yaml", "sweep: 9\ndate: 2026-01-01\n", "flat sweep/date"),
        ("PASS-2026-01-01-2.yaml", "sweep: 2\ndate: 2026-02-02\n", "flat sweep/date"),
        ("PASS-nope.yaml", _nested("PASS-2026-01-01-1"), "filename does not match"),
    ],
)
def test_check_file_rejects(tmp_path: Path, name: str, text: str, fragment: str) -> None:
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    with pytest.raises(SystemExit) as caught:
        mod.check_file(path)
    assert fragment in str(caught.value)


def test_unexpected_filename_helpers() -> None:
    with pytest.raises(SystemExit):
        mod.pass_id_from_name("notes.yaml")
    with pytest.raises(SystemExit):
        mod.latest_id([])
