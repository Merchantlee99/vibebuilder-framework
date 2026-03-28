# Plan.md

## Objective

- meeting summary export API를 가장 좁은 범위로 추가해 수동 재사용 비용을 줄인다.

## Readiness Decision

- Status: go
- Why: 문제 정의, 첫 라운드 범위, acceptance criteria, 핵심 리스크가 정리되었고 구현을 막는 큰 결정이 없다.

## Oversight Plan

- Mode: solo-pro
- Required lenses: discovery, pm, engineering
- Optional lenses skipped: design
- Required gates: review, validation
- Evidence needed: curl repro, error case check, regression check
- Pivot triggers: csv 요구 추가, 비동기 처리 요구, 새 저장소 도입, write path가 인증 레이어까지 확대

## Milestones

### Milestone 1

- Outcome: export endpoint 계약을 고정한다.
- Tasks: route shape, request params, error contract 정의
- Validation: 인증/없는 리소스/잘못된 포맷 케이스를 문장으로 설명 가능해야 한다

### Milestone 2

- Outcome: json export endpoint를 구현한다.
- Tasks: handler 추가, summary fetch 재사용, format validation 추가
- Validation: 샘플 summary를 정상 export하고 2개 오류 케이스를 재현한다

### Milestone 3

- Outcome: 회귀와 문서를 정리한다.
- Tasks: 기존 조회 API 재검증, run/verify 문서 갱신
- Validation: 기존 조회 endpoint와 새 export endpoint를 둘 다 확인한다

## Dependencies

- 기존 summary 조회 로직
- 인증 미들웨어
- 샘플 summary fixture 또는 seed 데이터

## Plan Review

- Founder lens: 범용 export 시스템 대신 가장 자주 필요한 `json` export만 먼저 여는 범위가 적절하다.
- Engineering lens: 기존 인증과 조회 로직을 재사용하면 새 write path를 API 레이어와 serializer 범위로 제한할 수 있다.
- Design lens if needed: 없음. UI가 없는 작업이다.

## Risk Register

- Risk: export 요구가 여러 포맷 확장 요구로 바로 커질 수 있다.
  Mitigation: 이번 라운드는 `json` 한 가지 포맷으로 고정한다.
- Risk: 구현 중 응답 크기나 권한 요구가 예상보다 복잡할 수 있다.
  Mitigation: 동기 처리 가능한 작은 payload와 기존 인증 범위로 한정한다.

## Validation Plan

- curl 또는 테스트로 새 export endpoint 정상 케이스 확인
- 잘못된 포맷 요청과 not found 응답 확인
- 기존 summary 조회 API 회귀 확인

## Exit Criteria

- acceptance criteria가 충족된다.
- review finding이 block 없이 정리된다.
- validation에서 정상/오류/회귀 경로가 모두 확인된다.
