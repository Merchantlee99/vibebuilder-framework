---
name: systematic-debugging
description: Use when a bug is unclear, recurring, or expensive to guess at and you need a disciplined loop to reproduce the issue, isolate the root cause, apply the smallest fix, and verify the result before moving on.
---

# Systematic Debugging

추측성 패치를 줄이고, 원인 분석을 먼저 하게 만드는 skill이다.

이 skill은 `superpowers`의 debugging discipline을 solo builder 환경에 맞게 가볍게 번역한 것이다.

## 언제 쓰는가

- 버그를 여러 번 건드렸는데 해결되지 않을 때
- 증상은 보이는데 원인이 분명하지 않을 때
- 로그, 상태, 재현 경로가 섞여 있어 추측성 수정이 쉬울 때
- 고치면 다른 기능을 깨뜨릴 가능성이 큰 문제일 때

작고 명백한 오타나 단순 설정 실수에는 굳이 쓰지 않는다.

## 먼저 읽을 것

- [AGENTS.md](../../../AGENTS.md)
- [docs/PIVOT_POLICY.md](../../../docs/PIVOT_POLICY.md)
- [templates/Implement.md](../../../templates/Implement.md)
- [templates/Documentation.md](../../../templates/Documentation.md)
- `Prompt.md`, `PRD.md`, `Plan.md` if present

## 목표

수정 전에 아래를 분명하게 만든다.

- 실제 증상은 무엇인가
- 기대 동작은 무엇인가
- 어디까지 재현되는가
- 가장 가능성이 높은 원인은 무엇인가
- 가장 작은 수정은 무엇인가
- 고친 뒤 무엇으로 검증할 것인가

## 워크플로

1. 증상을 한 문장으로 다시 쓴다.
2. 기대 동작과 실제 동작을 분리한다.
3. 재현 절차를 가장 짧은 경로로 적는다.
4. 로그, 상태, 입력, 환경 차이를 모은다.
5. 가능한 원인 가설을 적고 가장 싼 검증부터 확인한다.
6. 원인이 확인되기 전까지 큰 수정을 하지 않는다.
7. 수정 범위나 검증 방법이 바뀌면 `Implement.md`를 먼저 갱신한다.
8. 가장 작은 수정으로 문제를 고친다.
9. 원래 재현 절차와 인접 회귀 경로를 다시 검증한다.
10. `Documentation.md`에 원인과 검증 결과를 남긴다.

## 출력 방식

항상 아래 순서를 지킨다.

1. `증상`
2. `기대 동작`
3. `재현 절차`
4. `관찰된 증거`
5. `원인 가설`
6. `검증 계획`
7. `write path impact`
8. `수정안`
9. `검증 결과`
10. `회귀 위험`

## 가드레일

- 원인 분석 전에 큰 패치를 쌓지 않는다.
- 재현되지 않으면 먼저 관찰 가능성을 높인다.
- 여러 가설이 있으면 가장 싸게 반증 가능한 것부터 본다.
- 수정이 계획 범위를 벗어나면 `PIVOT_POLICY`를 다시 본다.
- 수정으로 write path나 validation loop가 바뀌면 `Implement.md`를 같이 갱신한다.
- 해결했더라도 왜 해결됐는지 설명할 수 없으면 종료로 보지 않는다.
