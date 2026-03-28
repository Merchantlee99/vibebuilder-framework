# Documentation.md

## Current Status

- planner 정리 완료
- scope freeze 완료
- 구현은 export endpoint slice 진행 중

## Decisions Log

- Date: 2026-03-29
  Decision: 이번 라운드는 `json` export만 지원한다
  Why: 가장 좁은 usable release를 먼저 만들고 추가 포맷 요구는 나중에 검증하기 위해
- Date: 2026-03-29
  Decision: 기존 조회 API와 export API를 분리한다
  Why: 조회와 export 계약을 섞으면 회귀 위험이 커지기 때문이다

## Known Issues

- 응답 크기 상한은 아직 명시되지 않았다
- 다운로드 헤더는 다음 라운드 결정으로 미뤘다

## How To Run

```bash
npm install
npm run dev
```

## How To Verify

- 인증된 요청으로 export endpoint를 호출해 `json` 응답을 확인한다
- 잘못된 포맷 요청이 4xx로 막히는지 확인한다
- 기존 summary 조회 endpoint가 그대로 동작하는지 확인한다

## Resume Here

- export endpoint 구현 후 review와 validation gate 실행

## Next Options

- review/validation 통과 후 응답 크기 제한 정책 정리
- 실제 수요가 확인되면 `csv` 포맷을 다음 라운드 후보로 검토
