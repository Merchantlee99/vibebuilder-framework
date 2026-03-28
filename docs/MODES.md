# Modes

vibebuilder-framework는 모든 작업에 같은 강도를 강제하지 않는다. 작업 크기와 리스크에 맞춰 mode를 고른다.

## Mode 1: solo-lite

빠른 실험, 작은 기능, 명백한 버그 수정에 쓴다.

필수:

- `Prompt.md` 또는 한 줄 목표
- `Implement.md`
- `Documentation.md`
- `review` if needed
- `validation` if needed

생략 가능:

- full `PRD.md`
- `Subagent-Manifest.md`
- `security gate` unless sensitive

## Mode 2: solo-pro

기본 권장 모드다. 대부분의 실제 제품 개발은 이 모드를 기준으로 한다.

필수:

- `product-planner`
- `Prompt.md`
- `PRD.md`
- `Plan.md`
- `Implement.md`
- `Documentation.md`
- `review`
- `validation` 또는 `qa` 또는 `browse`

조건부:

- `security gate`
- `ship` if release-bound
- `Subagent-Manifest.md`

## Mode 3: team

여러 역할이나 병렬 작업이 필요한 프로젝트에 쓴다.

필수:

- `product-planner`
- 전체 문서 세트
- `Subagent-Manifest.md`
- 명시된 write scope
- `review`
- `validation` 또는 `qa` 또는 `browse`

조건부:

- `security gate`
- `ship` if release-bound
- 별도 release coordination

## 선택 기준

아래 질문으로 mode를 정한다.

- 범위가 작은가, 큰가
- 재작업 비용이 낮은가, 높은가
- write path가 하나인가, 여러 개인가
- 사용자 영향이 작은가, 큰가
- 보안이나 데이터 리스크가 있는가

확신이 없으면 `solo-pro`를 기본값으로 둔다.
