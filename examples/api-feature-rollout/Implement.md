# Implement.md

## Current Slice

- Milestone 2: json export endpoint 구현

## Write Paths

- `src/api/meeting-summaries/export.ts`
- `src/services/meeting-summary-service.ts`
- `src/lib/http/errors.ts`

## Read Paths

- `Prompt.md`
- `PRD.md`
- `Plan.md`
- 기존 summary 조회 route 및 인증 미들웨어

## Planned Changes

- export 전용 route 추가
- `json` 포맷만 허용하는 검증 로직 추가
- summary fetch 재사용 후 export payload 반환
- 잘못된 포맷과 not found 오류 응답 정리

## Sprint Contract

- Outcome: 인증된 사용자가 meeting summary를 `json`으로 export할 수 있다.
- Done definition: 새 endpoint가 정상, 잘못된 포맷, 없는 리소스 케이스를 처리하고 review를 통과한다.
- Evidence to collect: curl output, error response note, regression note
- Failure threshold: 기존 조회 API 계약이 깨지거나 export 요청이 기존 인증을 우회하면 실패
- Required gate after this slice: validation
- Pivot trigger: 포맷 요구가 늘어나거나 응답을 파일 저장 방식으로 바꿔야 하는 경우

## Validation Loop

1. 정상 export curl 확인
2. invalid format curl 확인
3. 기존 조회 endpoint 회귀 확인

## Risks During Implementation

- 조회 로직 재사용 중 기존 응답 계약을 건드릴 수 있다.
- 포맷 분기 로직이 커지면 범위가 serializer 리팩터링으로 확대될 수 있다.

## Gate After This Slice

- review
- validation or qa or browse
