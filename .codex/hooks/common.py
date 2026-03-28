#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


PROJECT_DOCS = (
    "Prompt.md",
    "PRD.md",
    "Plan.md",
    "Implement.md",
    "Documentation.md",
    "Subagent-Manifest.md",
)


def load_event() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def resolve_repo_root(cwd: str | None) -> Path:
    if not cwd:
        return Path.cwd()
    try:
        result = subprocess.run(
            ["git", "-C", cwd, "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        )
        return Path(result.stdout.strip())
    except Exception:
        return Path(cwd)


def runtime_path(repo_root: Path) -> Path:
    return repo_root / ".vibebuilder" / "runtime.json"


def load_runtime(repo_root: Path) -> tuple[dict | None, Path]:
    path = runtime_path(repo_root)
    if not path.exists():
        return None, path
    try:
        return json.loads(path.read_text(encoding="utf-8")), path
    except json.JSONDecodeError:
        return {"_invalid": True}, path


def existing_project_docs(repo_root: Path) -> list[str]:
    return [name for name in PROJECT_DOCS if (repo_root / name).exists()]


def expected_docs_for_mode(mode: str) -> list[str]:
    if mode == "solo-lite":
        return ["Implement.md", "Documentation.md"]
    if mode == "team":
        return [
            "Prompt.md",
            "PRD.md",
            "Plan.md",
            "Implement.md",
            "Documentation.md",
        ]
    return ["Prompt.md", "PRD.md", "Plan.md", "Implement.md", "Documentation.md"]


def git_changed_paths(repo_root: Path) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True,
        )
    except Exception:
        return []

    paths: list[str] = []
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return paths


def emit_json(payload: dict) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False))
