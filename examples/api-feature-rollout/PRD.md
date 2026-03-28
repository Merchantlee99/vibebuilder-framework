# PRD.md

## Problem Statement

- 현재 meeting summary 결과는 조회는 가능하지만 내보내기가 안 돼서, 사용자가 다른 워크플로에 재사용하려면 수동 복사에 의존해야 한다.

## User Pain And Current Workaround

- Pain: 운영팀은 요약 결과를 보고서나 다른 시스템에 넘길 때 반복 수작업을 한다.
- Current workaround: 응답 본문이나 UI에서 텍스트를 복사해 다른 문서나 툴에 붙여넣는다.
- Why now: 요약 결과 재사용 수요가 늘었고, export가 없어서 운영 비용이 계속 쌓인다.

## Target User

- 회의 요약 결과를 후속 문서나 내부 도구로 옮겨야 하는 운영 담당자

## User Story

- 운영 담당자로서, 이미 생성된 회의 요약을 다시 가공하지 않고 바로 내려받고 싶다. 그래야 수동 복사를 줄일 수 있다.

## Core Flow

1. 인증된 사용자가 meeting summary export endpoint를 호출한다.
2. 서버가 요청한 포맷과 summary 존재 여부를 검증한다.
3. 유효한 경우 export payload를 반환하고, 잘못된 경우 명확한 오류를 반환한다.

## Scope For This Round

- `json` export endpoint 추가
- 포맷 검증 및 오류 응답 추가
- 기존 인증 미들웨어 재사용
- 최소 회귀 검증

## Out Of Scope

- `csv`, `pdf` 같은 추가 포맷
- 비동기 export job
- 외부 파일 저장소 업로드
- export 이력 관리

## Options Considered

- Option: 기존 조회 API에 `export=true` 파라미터 추가
  Why not chosen: 조회와 export 책임이 섞여 응답 계약이 흐려진다.
- Option: 범용 export 서비스부터 설계
  Why not chosen: 이번 라운드 scope와 리스크가 과하다.

## Acceptance Criteria

- 인증된 사용자가 특정 meeting summary를 `json` 형식으로 export할 수 있다.
- 지원하지 않는 포맷 요청은 4xx 오류와 명확한 메시지를 반환한다.
- summary가 없으면 일관된 not found 응답을 반환한다.
- 기존 summary 조회 API 계약은 유지된다.

## Key Assumptions

- 현재 가장 필요한 포맷은 `json` 하나면 충분하다.
- export 응답은 동기 처리 범위 안에서 끝낼 수 있다.
- 기존 인증 미들웨어를 재사용해도 권한 요구사항이 맞는다.

## Risks

- export 요구가 곧 추가 포맷 요구로 커질 수 있다.
- 응답 크기 제한이 없으면 API 비용과 지연이 커질 수 있다.
- 기존 조회 로직과 분리하지 않으면 회귀 위험이 생긴다.

## Open Decisions

- 응답 크기 상한을 이번 라운드에 둘지
- 파일 다운로드 헤더를 지금 넣을지 다음 라운드로 미룰지

## Success Signal

- 운영팀이 수동 복사 없이 샘플 summary를 export할 수 있다.
- validation에서 새 endpoint와 기존 조회 endpoint가 모두 정상 동작한다.
