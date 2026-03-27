---
name: product-planner
description: Use when a request is new, ambiguous, likely to sprawl, or strategically important and you need to turn it into a scoped build-ready plan with prompt, PRD, plan, assumptions, and a readiness check before implementation.
---

# Product Planner

아이디어를 바로 구현으로 보내지 말고, build-ready 상태로 정리하는 skill이다.

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

## 워크플로

1. 요청을 기능이 아니라 사용자 문제로 다시 쓴다.
2. 목표, 비목표, 제약, 미정 사항을 분리한다.
3. 가장 위험한 가정 3개를 뽑고 우선순위를 매긴다.
4. 가능한 접근법을 2개 이상 비교하고 비용과 리스크를 적는다.
5. 이번 라운드에 맞는 가장 좁은 범위를 추천한다.
6. `Prompt.md`, `PRD.md`, `Plan.md`를 작성하거나 갱신한다.
7. readiness check를 수행하고 `go`, `needs decision`, `stop` 중 하나로 판정한다.

## 산출물 기준

planner를 마치면 최소한 아래가 남아 있어야 한다.

- `Prompt.md`에 목표, 비목표, 제약, done-when이 있다.
- `PRD.md`에 문제 정의, 핵심 흐름, acceptance criteria, 리스크가 있다.
- `Plan.md`에 milestone과 검증 순서가 있다.
- 구현을 막는 미해결 결정이 무엇인지 분명하다.

## 출력 방식

항상 아래 순서를 지킨다.

1. `문제 재정의`
2. `이번 범위`
3. `하지 않을 것`
4. `핵심 가정`
5. `추천 접근`
6. `준비 상태 판정`

## 가드레일

- planner 단계에서 코드 구현으로 넘어가지 않는다.
- 문서를 길게 만드는 것이 목적이 아니다. 구현에 필요한 결정만 남긴다.
- 대안은 보여주되, 마지막에는 하나를 추천한다.
- scope가 흔들리면 구현을 계속 밀지 말고 이 단계로 되돌린다.
