#!/usr/bin/env python3
from __future__ import annotations

from common import (
    emit_json,
    existing_project_docs,
    expected_docs_for_mode,
    load_event,
    load_runtime,
    resolve_repo_root,
)


def main() -> None:
    event = load_event()
    repo_root = resolve_repo_root(event.get("cwd"))
    runtime, runtime_file = load_runtime(repo_root)

    if runtime is None:
        emit_json(
            {
                "continue": True,
                "systemMessage": (
                    "vibebuilder runtime.json이 없습니다. "
                    "현재 hooks는 수동 문서 상태만 참고하는 약한 모드로 동작합니다."
                ),
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": (
                        f"Repo root: {repo_root}\n"
                        f"Expected runtime file: {runtime_file}\n"
                        "Before large implementation, create .vibebuilder/runtime.json and set mode/readiness/scope_freeze."
                    ),
                },
            }
        )
        return

    if runtime.get("_invalid"):
        emit_json(
            {
                "continue": True,
                "systemMessage": "vibebuilder runtime.json 형식이 잘못되었습니다. JSON을 먼저 고치세요.",
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": "Runtime parsing failed. Treat the session as planning-first until runtime.json is valid.",
                },
            }
        )
        return

    mode = runtime.get("mode", "solo-pro")
    planning = runtime.get("planning", {})
    execution = runtime.get("execution", {})
    task_type = runtime.get("task_type", "unspecified")
    existing_docs = existing_project_docs(repo_root)
    expected_docs = expected_docs_for_mode(mode)
    missing_docs = [name for name in expected_docs if name not in existing_docs]
    required_gates = planning.get("required_gates", [])

    lines = [
        "Vibebuilder runtime summary:",
        f"- mode: {mode}",
        f"- task type: {task_type}",
        f"- readiness: {planning.get('readiness', 'unknown')}",
        f"- scope freeze: {planning.get('scope_freeze', False)}",
        f"- required gates: {', '.join(required_gates) if required_gates else 'none'}",
        f"- current slice: {execution.get('current_slice', 'not set')}",
        f"- writer: {execution.get('writer', 'not set')}",
    ]

    if task_type == "framework_bootstrap":
        lines.append("- note: this repo is the framework itself, so project-doc enforcement stays passive.")
    elif missing_docs:
        lines.append(f"- missing docs: {', '.join(missing_docs)}")

    emit_json(
        {
            "continue": True,
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": "\n".join(lines),
            },
        }
    )


if __name__ == "__main__":
    main()
