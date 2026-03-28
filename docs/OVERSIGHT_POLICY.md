# Oversight Policy

vibebuilder-framework는 고정된 렌즈 매트릭스를 강제하지 않는다. 대신 `product-planner`가 이번 작업에 필요한 감독 계획을 선언하고, 구현 중에는 `main writer`가 재평가를 요청할 수 있다.

## 원칙

- 모든 작업에 같은 평가 렌즈를 강제하지 않는다.
- planner는 작업의 성격, 리스크, 범위에 맞춰 필요한 감독을 고른다.
- writer는 구현 중 새로운 리스크를 발견하면 감독 계획의 상향 조정을 요청할 수 있다.

## Oversight Plan

비사소한 작업은 planner가 아래 항목을 선언한다.

- `mode`
- `required lenses`
- `optional lenses skipped`
- `required gates`
- `evidence needed`
- `pivot triggers`

## 사용 가능한 렌즈

- `discovery`: 사용자 pain, 기존 대안, 왜 지금인지
- `founder`: 더 좁은 wedge, 가치 대비 복잡도, 범위 축소 가능성
- `pm`: 가정 분리, 우선순위, acceptance criteria, 비범위
- `engineering`: 데이터 흐름, 실패 경로, 검증 계획, 기술 리스크
- `design`: UI 흐름, 상호작용, 화면 복잡도, 디자인 리스크
- `security`: 인증, 권한, 비밀 값, 데이터 노출, 업로드 경로

## 기본 책임

- 초기 선언: `product-planner`
- 구현 중 재평가 요청: `main writer`
- 최종 게이트 판정: 각 gate 역할

## 상향 조정이 필요한 경우

아래 중 하나라도 발생하면 planner 또는 writer가 oversight plan 재평가를 요청한다.

- 범위가 커졌다
- UI 복잡도가 예상보다 커졌다
- 인증, 권한, 결제, 업로드가 새로 들어왔다
- write path가 늘었다
- 검증 방법이 기존 계획으로 충분하지 않다

## 출력 예시

```md
Mode: solo-pro
Required lenses: discovery, pm, engineering
Optional lenses skipped: design
Required gates: review, validation or qa
Evidence needed: demo path, regression check
Pivot triggers: acceptance criteria change, write path expansion
```
