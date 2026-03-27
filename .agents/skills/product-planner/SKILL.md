---
name: product-planner
description: Use when a request is new, ambiguous, likely to sprawl, or strategically important and you need to turn it into a scoped build-ready plan with prompt, PRD, plan, assumptions, and a readiness check before implementation.
---

# Product Planner

아이디어를 바로 구현으로 보내지 말고, build-ready 상태로 정리하는 skill이다.

이 skill은 세 가지 레퍼런스를 목적별로 재해석해 사용한다.

- `pm-skills`: discovery, assumption mapping, prioritization, PRD 구조화
- `gstack`: office-hours 식 문제 재정의, founder lens, eng lens, design lens
- `AGENTS.md`: 저장소 전역 규칙과 artifact gate 기준

## 언제 쓰는가

- 새 기능이나 새 제품을 시작할 때
- 사용자가 말한 해결책보다 실제 문제를 다시 정의해야 할 때
- 범위가 쉽게 커질 것 같을 때
- 구현 전에 acceptance criteria와 리스크를 고정해야 할 때
- 구현 중 scope drift가 발생해 다시 정리해야 할 때

작고 명백한 버그 수정에는 쓰지 않는다.

## 먼저 읽을 것

- [AGENTS.md](../../../AGENTS.md)
- [docs/ARTIFACT_GATES.md](../../../docs/ARTIFACT_GATES.md)
- [templates/Prompt.md](../../../templates/Prompt.md)
- [templates/PRD.md](../../../templates/PRD.md)
- [templates/Plan.md](../../../templates/Plan.md)

## 목표

구현을 시작하기 전에 아래 질문에 답할 수 있게 만든다.

- 지금 해결하려는 실제 문제는 무엇인가
- 이번 스프린트에서 어디까지 할 것인가
- 무엇을 하지 않을 것인가
- 성공 판단 기준은 무엇인가
- 지금 구현해도 되는가, 아니면 더 결정이 필요한가

## 계획 렌즈

planner는 아래 렌즈를 순서대로 적용한다.

### 1. Discovery Lens

사용자가 말한 기능을 그대로 받지 않는다. 먼저 실제 pain, 반복 패턴, 기존 우회 방법, 지금 당장 해결해야 하는 이유를 묻고 정리한다.

### 2. Founder Lens

gstack의 `office-hours`, `plan-ceo-review` 감각으로 본다.

- 이 요청이 진짜 문제를 풀고 있는가
- 더 작은 wedge로 배울 수 있는가
- 사용자 가치에 비해 복잡도가 과한가
- 지금 범위를 줄여도 되는가

### 3. PM Lens

pm-skills의 discovery/execution 흐름으로 본다.

- 가치, 사용성, 실행 가능성, 사업성 가정을 분리한다
- 가장 위험한 가정을 우선순위로 정한다
- acceptance criteria와 비범위를 명시한다

### 4. Engineering Lens

gstack의 `plan-eng-review` 감각으로 본다.

- 데이터 흐름과 상태 변화가 설명 가능한가
- 실패 경로와 edge case가 보이는가
- 테스트와 검증 계획이 있는가
- 지금 시점에 기술적으로 막히는 결정이 남아 있는가

### 5. Design Lens

UI가 중요한 작업일 때만 적용한다.

- 핵심 화면과 사용자 흐름이 분명한가
- 디자인 난이도에 비해 범위가 과하지 않은가
- 구현 전에 고정해야 할 상호작용 결정이 남아 있는가

## 워크플로

1. 요청을 기능이 아니라 사용자 문제로 다시 쓴다.
2. 현재 pain, 기존 대안, 왜 지금 해야 하는지를 정리한다.
3. 목표, 비목표, 제약, 미정 사항을 분리한다.
4. 가치, 사용성, 실행 가능성, 사업성 가정을 분리하고 우선순위를 매긴다.
5. 가능한 접근법을 2개 이상 비교하고 가장 좁은 wedge를 추천한다.
6. 핵심 흐름, acceptance criteria, failure path, open decision을 정리한다.
7. `Prompt.md`, `PRD.md`, `Plan.md`를 작성하거나 갱신한다.
8. founder lens, engineering lens, design lens if needed로 readiness check를 수행한다.
9. `go`, `needs decision`, `stop` 중 하나로 판정한다.

## 산출물 기준

planner를 마치면 최소한 아래가 남아 있어야 한다.

- `Prompt.md`에 목표, 비목표, 제약, done-when이 있다.
- `PRD.md`에 문제 정의, 사용자 pain, 핵심 흐름, acceptance criteria, 리스크, 비범위가 있다.
- `Plan.md`에 milestone, 검증 순서, plan review 포인트가 있다.
- 구현을 막는 미해결 결정이 무엇인지 분명하다.
- 이번 라운드에서 하지 않을 것이 문장으로 적혀 있다.

## 출력 방식

항상 아래 순서를 지킨다.

1. `문제 재정의`
2. `사용자 pain과 현재 대안`
3. `이번 범위`
4. `하지 않을 것`
5. `핵심 가정`
6. `대안 비교`
7. `추천 wedge`
8. `readiness 판정`
9. `구현 전 남은 결정`

## readiness 판정 규칙

### go

- 문제 정의가 분명하다
- 범위와 비범위가 분리되어 있다
- acceptance criteria가 있다
- 큰 미해결 결정이 구현을 막지 않는다

### needs decision

- 방향은 맞지만 핵심 결정 1~2개가 남아 있다
- 이 상태로 구현하면 재작업 가능성이 높다

### stop

- 기능 설명만 있고 사용자 문제는 불분명하다
- 범위가 너무 넓다
- 대안 비교 없이 바로 구현하려 한다

## 가드레일

- planner 단계에서 코드 구현으로 넘어가지 않는다.
- 문서를 길게 만드는 것이 목적이 아니다. 구현에 필요한 결정만 남긴다.
- 대안은 보여주되, 마지막에는 하나를 추천한다.
- scope가 흔들리면 구현을 계속 밀지 말고 이 단계로 되돌린다.
- UI가 핵심이면 design lens를 생략하지 않는다.
- 인증, 결제, 권한, 데이터 모델이 있으면 engineering lens를 더 엄격하게 본다.
