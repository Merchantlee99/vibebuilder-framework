---
name: gstack-gates
description: Use after implementation to apply gstack-inspired quality gates such as review, validation, QA or browse, security checks, and ship readiness without turning them into always-on orchestration.
---

# gstack Gates

gstack의 강한 부분인 후반 검수 게이트를 가져와, 구현이 끝난 작업을 실제로 잠그는 skill이다.

## 언제 쓰는가

- 기능 구현이 끝나고 merge 또는 ship 전 점검이 필요할 때
- 회귀, 누락, 테스트 부족, 브라우저 플로우 문제가 걱정될 때
- 인증, 권한, 결제, 업로드, 사용자 데이터처럼 보안 민감 변경이 있을 때

기획 단계나 구현 초반에는 쓰지 않는다.

## 먼저 읽을 것

- [AGENTS.md](../../../AGENTS.md)
- [docs/ARTIFACT_GATES.md](../../../docs/ARTIFACT_GATES.md)
- [docs/SUBAGENT_POLICY.md](../../../docs/SUBAGENT_POLICY.md)
- `Plan.md`, `Implement.md`, `Documentation.md` if present

## 기본 게이트 순서

1. `review`
2. `validation` 또는 `qa` 또는 `browse`
3. `cso` if needed
4. `ship` if release-bound

이 skill은 구현 후 게이트를 위한 것이다. `plan-eng-review`는 기본적으로 scope freeze 전에 끝나 있어야 하며, 구현 후에는 누락 여부만 확인한다.

작업의 크기와 위험도에 따라 일부 게이트는 생략할 수 있지만, 이유를 남긴다.

## 각 게이트의 목적

### review

- 실제 버그, 회귀, 누락, completeness gap을 찾는다.
- 발견 사항은 심각도 순으로 정리한다.

### validation 또는 qa 또는 browse

- UI가 없는 작업이면 테스트, API, CLI, runtime check로 충분한지 먼저 본다.
- UI가 있는 작업이면 사용자 플로우를 실제로 재현한다.

- 변경의 핵심 경로를 실제로 재현한다.
- UI가 있으면 네비게이션, 폼, 오류 상태를 같이 확인한다.

### cso

- 인증, 권한, 데이터 노출, 입력 검증, 비밀 관리, 업로드 경로를 본다.

### ship

- 테스트, 문서, 데모, 배포 준비 상태를 확인한다.

## 출력 방식

게이트를 돌릴 때는 항상 아래 형식을 유지한다.

- `gate`
- `status`: pass, warn, block
- `findings`
- `required fixes`
- `skip reason` if skipped
- `notes` if helpful

## 가드레일

- 게이트를 매 대화 턴마다 실행하지 않는다.
- vague feedback 대신 수정 가능한 finding을 남긴다.
- QA나 review가 직접 코드를 고칠 필요가 있으면 write scope를 다시 선언한다.
- ship 전에는 문서 갱신 상태도 같이 본다.
