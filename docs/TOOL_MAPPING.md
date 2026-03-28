# Tool Mapping

이 문서는 vibebuilder-framework를 실제 도구 위에 어떻게 배치할지 정리한다.

원칙은 간단하다. 도구 이름보다 `역할`이 먼저다.

- `planner-capable agent`: 문제 정의, 대안 비교, 범위 통제
- `writer-capable agent`: 저장소 맥락 기반 구현, 수정, 검증
- `review-capable agent`: 회귀, 누락, 리스크 점검
- `validation-capable agent`: 테스트, API, CLI, runtime check 수행
- `browser-capable agent`: 실제 UI 플로우 재현

## 기본 원칙

- 같은 역할을 여러 도구에 중복 할당하지 않는다.
- 실제 write path를 크게 소유하는 writer는 한 번에 한 명만 둔다.
- planner와 reviewer는 항상 코드를 직접 고치기보다 판단과 피드백을 우선한다.
- 도구를 바꾸는 이유는 브랜드가 아니라 `맥락 적합성`이어야 한다.

## 권장 기본값

혼자 제품을 만드는 빌더라면 아래 구성이 가장 무난하다.

- `Codex app`: 기본 writer, project-local docs 갱신, review/validation/qa 실행
- `ChatGPT`: 초기 아이디어 확장, 대안 비교, 전략적 비교 토론
- `다른 도구`: 정말 특정 강점이 필요할 때만 보조로 사용

즉, 기본 스택은 `ChatGPT로 발산 -> Codex로 수렴과 실행`이다.

## Planner-Of-Record

외부 도구와 대화를 많이 하더라도, 실제 프로젝트 기준 문서를 쓰고 갱신하는 planner는 하나로 고정하는 편이 좋다.

- `exploration partner`: 아이디어를 넓히는 대화 상대
- `planner-of-record`: `Prompt.md`, `PRD.md`, `Plan.md`를 실제 기준 문서로 남기는 주체

권장 기본값:

- 발산: ChatGPT 또는 Claude Code
- 문서 확정: Codex의 `product-planner`

즉, 다른 도구와 대화해도 마지막에는 repo 안 문서로 수렴해야 한다.

## Setup 1: Codex-only

가장 단순한 운영 방식이다.

- `product-planner`: Codex에서 실행
- `main writer`: Codex
- `review`, `validation`, `qa`, `browse`: Codex 안의 별도 턴 또는 별도 역할로 실행

이 setup이 맞는 경우:

- 저장소 맥락이 가장 중요하다
- 도구를 바꾸는 비용을 줄이고 싶다
- 혼자 빠르게 끝까지 가져가고 싶다

주의:

- planner와 writer를 같은 세션에서 섞더라도 역할 전환은 문서로 분리한다
- 구현 중에는 writer 모드로 고정하고, review는 별도 턴에서 다시 수행한다

## Setup 2: ChatGPT + Codex

혼자 바이브코딩하는 사람에게 가장 권장하는 방식이다.

- `ChatGPT`: 초기 문제 재정의, 옵션 비교, wedge 탐색
- `Codex product-planner`: planner-of-record로서 실제 프로젝트 문서로 수렴
- `Codex main writer`: 구현과 검증
- `Codex gstack-gates`: review, validation 또는 qa/browse, ship

이 setup이 맞는 경우:

- 아이디어 단계에서 발산적 대화가 필요하다
- 구현은 저장소 안에서 단단하게 진행하고 싶다
- planner 산출물을 바로 파일로 옮기고 싶다

핵심 규칙:

- 최종 truth는 항상 프로젝트 문서에 남긴다
- ChatGPT 대화 내용이 아니라 `Prompt.md`, `PRD.md`, `Plan.md`가 구현 기준이다
- ChatGPT는 exploration partner일 수 있지만 planner-of-record를 대체하지 않는다

## Setup 3: Claude Code + Codex

실행 품질을 더 끌어올리고 싶을 때 쓰는 보강형 setup이다.

- `Codex`: 기본 writer 또는 기본 운영 허브
- `Claude Code`: planner 보강, 디버깅, 리뷰, 대안 비교
- `main writer`: 둘 중 한 도구만 선택

이 setup이 맞는 경우:

- 다른 모델의 비평 관점이 필요하다
- 디버깅이나 리뷰를 별도 시각으로 한 번 더 보고 싶다
- 한 도구의 맹점을 다른 도구로 보완하고 싶다

핵심 규칙:

- writer는 한 명만 둔다
- 다른 도구는 reviewer나 planner로만 우선 배치한다
- 같은 코드 경로를 동시에 수정하게 두지 않는다

## 역할별 권장 배치

| 역할 | 가장 중요한 능력 | 기본 추천 |
| --- | --- | --- |
| `product-planner` | 문제 재정의, 가정 분리, 범위 통제 | Codex planner-of-record |
| `main writer` | 저장소 맥락 이해, 구현, 검증 | Codex |
| `reviewer` | 회귀, 누락, completeness gap 발견 | Codex 또는 Claude Code |
| `validation` | 테스트, API, CLI, runtime check | Codex |
| `qa/browser` | 실제 흐름 재현 | Codex with browser-capable flow |
| `security` | 민감 표면 점검 | 가장 보수적으로 보는 도구 |

## 언제 도구를 바꿔야 하는가

아래 상황이면 현재 역할 배치를 다시 본다.

- planner 결과가 길기만 하고 scope가 안 줄어든다
- writer가 자꾸 계획 밖 확장을 수용한다
- review가 단순 칭찬 위주로 끝난다
- UI 플로우를 실제로 재현하지 못한다
- 디버깅이 원인 분석 없이 추측성 수정으로 흐른다

## 한 줄 추천

혼자 Codex app을 주로 쓴다면 기본은 `Codex as planner-of-record and writer, separate review turn`으로 두고, 초기 아이디어 발산이 필요할 때만 ChatGPT를 붙이는 것이 가장 안정적이다.
