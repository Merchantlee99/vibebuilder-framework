---
name: vibe-coding-workflow
description: Use when implementation is approved and you need to run a disciplined build loop with a single writer, scoped execution, validation slices, document updates, and controlled handoff into review and QA gates.
---

# Vibe Coding Workflow

기획이 끝난 뒤 구현을 흔들리지 않게 진행하는 skill이다.

## 언제 쓰는가

- `Prompt.md`, `PRD.md`, `Plan.md`가 준비된 뒤 구현을 시작할 때
- 중간 규모 이상의 기능을 단계적으로 구현할 때
- scope를 지키면서 milestone 단위로 전진해야 할 때
- 구현과 문서 갱신을 같이 관리해야 할 때

기획 자체가 불안정하면 이 skill보다 `product-planner`를 먼저 쓴다.

## 먼저 읽을 것

- [AGENTS.md](../../../AGENTS.md)
- [docs/OPERATING_MODEL.md](../../../docs/OPERATING_MODEL.md)
- [docs/SUBAGENT_POLICY.md](../../../docs/SUBAGENT_POLICY.md)
- [docs/ARTIFACT_GATES.md](../../../docs/ARTIFACT_GATES.md)
- [templates/Implement.md](../../../templates/Implement.md)
- [templates/Documentation.md](../../../templates/Documentation.md)
- `Subagent-Manifest.md` if present

## 목표

구현 중에 자주 생기는 세 가지 문제를 막는다.

- 범위가 조용히 커지는 것
- 여러 writer가 같은 경로를 건드려 충돌하는 것
- 구현은 끝났는데 문서와 검증이 따라오지 않는 것

## 워크플로

1. readiness와 scope freeze 여부를 확인한다.
2. `Implement.md`에 현재 작업 범위, write paths, validation loop를 적는다.
3. 메인 writer 한 명이 code path를 소유한다.
4. milestone을 작은 slice로 나누고 순서대로 구현한다.
5. 각 slice마다 즉시 검증하고 실패하면 바로 수정한다.
6. 결정이 바뀌면 `Documentation.md`와 관련 계획 문서를 갱신한다.
7. 구현 완료 후 `gstack-gates`로 넘긴다.

## 구현 중 판단 기준

- 계획에 없는 요구가 나오면 바로 확장하지 말고 planner로 되돌린다.
- 다른 역할은 읽기와 피드백을 우선한다.
- 병렬 작업이 필요하면 write scope가 겹치지 않아야 한다.
- 테스트, 재현, 데모 방법은 구현이 끝난 뒤가 아니라 구현 중에 쌓는다.

## 권장 출력

항상 아래 정보를 짧게 유지한다.

- `현재 milestone`
- `이번 slice의 write path`
- `검증 방법`
- `현재 리스크`
- `다음 gate`

## 가드레일

- scope freeze 전에는 큰 구현에 들어가지 않는다.
- 구현 시작 후에는 계획 밖 확장을 바로 수용하지 않는다.
- 구현이 끝났는데 문서가 비어 있으면 완료로 보지 않는다.
- review와 QA를 마지막 장식으로 취급하지 않는다.
