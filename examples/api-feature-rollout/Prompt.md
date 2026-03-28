# Prompt.md

## Working Title

- Meeting Summary Export API

## Goal

- 기존 회의 요약 데이터를 내려받을 수 있는 export API를 추가해, 운영팀이 수동 복사 없이 결과를 재사용할 수 있게 만든다.

## Non-Goals

- 새 대시보드 화면 추가
- 파일 저장용 외부 스토리지 도입
- 대용량 비동기 배치 처리
- 권한 모델 전면 개편

## User Problem

- 운영팀은 회의 요약 결과를 다른 도구로 넘길 때 매번 화면에서 복사해 붙여넣는다.
- 현재 API는 조회만 가능하고 재사용 가능한 export 형태를 제공하지 않는다.

## Constraints

- 이번 라운드는 기존 API 서버 안에서 끝나야 한다.
- 동기 요청 기준으로 작은 파일만 지원한다.
- 기존 인증 체계를 재사용해야 한다.

## Inputs We Already Have

- 기존 meeting summary 조회 API
- 인증 미들웨어
- 샘플 요약 데이터

## Unknowns

- export 포맷을 `json`만 지원할지 `csv`까지 열어둘지
- 최대 응답 크기를 어느 수준에서 제한할지

## Deliverables

- 새 export endpoint
- 포맷 검증 로직
- 최소 회귀 검증 절차
- 문서화된 실행 및 검증 방법

## Done-When

- 인증된 사용자가 meeting summary를 export할 수 있다.
- 잘못된 포맷 요청은 명확한 오류를 반환한다.
- 기존 조회 API 동작에 회귀가 없다.

## Notes

- 이번 라운드는 범용 export 시스템이 아니라 가장 좁은 usable endpoint가 목표다.
