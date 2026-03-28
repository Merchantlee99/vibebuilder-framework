#!/usr/bin/env python3
from __future__ import annotations

from common import emit_json, git_changed_paths, load_event, load_runtime, resolve_repo_root


META_PATHS = {
    "Documentation.md",
    "Implement.md",
    ".vibebuilder/runtime.json",
}


def main() -> None:
    event = load_event()
    if event.get("stop_hook_active"):
        emit_json({"continue": True})
        return

    repo_root = resolve_repo_root(event.get("cwd"))
    runtime, _ = load_runtime(repo_root)

    if not runtime or runtime.get("_invalid"):
        emit_json({"continue": True})
        return

    if runtime.get("task_type") == "framework_bootstrap":
        emit_json({"continue": True})
        return

    mode = runtime.get("mode", "solo-pro")
    if mode == "solo-lite":
        emit_json({"continue": True})
        return

    changed_paths = git_changed_paths(repo_root)
    if not changed_paths:
        emit_json({"continue": True})
        return

    doc_exists = (repo_root / "Documentation.md").exists()
    doc_touched = "Documentation.md" in changed_paths
    meaningful_changes = [
        path
        for path in changed_paths
        if path not in META_PATHS and not path.startswith(".codex/")
    ]

    if doc_exists and meaningful_changes and not doc_touched:
        emit_json(
            {
                "decision": "block",
                "reason": (
                    "Documentation.md를 갱신하세요. 이번 턴에 작업 결과가 바뀌었지만 "
                    "현재 상태와 다음 재개 지점이 아직 문서에 남지 않았습니다."
                ),
            }
        )
        return

    emit_json({"continue": True})


if __name__ == "__main__":
    main()
