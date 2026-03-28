# review-notes.md

## Gate

- review

## Status

- warn

## Findings

- export handler에서 포맷 검증이 route 안에 직접 들어가 있어, 다음 포맷 확장 시 분기 로직이 커질 수 있다.
- 기존 summary fetch 로직을 재사용했지만, not found 오류 메시지는 기존 조회 API와 문구를 맞출 필요가 있다.

## Required Fixes

- 포맷 검증을 작은 helper로 분리한다.
- not found 오류 문구를 기존 조회 API와 일치시킨다.

## Notes

- block issue는 없다.
- 이번 라운드는 `json` 단일 포맷이라 구조를 과하게 일반화할 필요는 없다.
