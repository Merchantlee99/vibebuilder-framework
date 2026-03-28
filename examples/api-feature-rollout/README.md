# api-feature-rollout

이 예시는 UI가 없는 API 기능 변경을 `vibebuilder-framework`로 어떻게 굴리는지 보여주는 샘플 문서 세트다.

상황은 단순하다. 기존 API에 `meeting summary export` 기능을 추가해야 하지만, 범위를 잘못 잡으면 인증, 비동기 처리, 파일 생성까지 한 번에 커질 수 있다. 그래서 `PM planner -> scope freeze -> single-writer implementation -> review -> validation` 흐름으로 다루는 경우를 가정한다.

## 이 예시가 보여주는 것

- UI가 없는 작업에서 `validation` 게이트를 어떻게 쓰는지
- `qa/browse` 없이도 프레임워크가 자연스럽게 동작하는 방식
- API 기능에서 `write path`와 `pivot trigger`를 어떻게 선언하는지
- release-bound 작업이 아닐 때 `ship`을 생략할 수 있는 방식

## 폴더 구성

- `Prompt.md`: 목표, 비목표, 제약
- `PRD.md`: 사용자 문제, acceptance criteria, 리스크
- `Plan.md`: milestone, oversight plan, validation 계획
- `Implement.md`: 현재 slice와 sprint contract
- `Documentation.md`: 상태 기록과 재개 지점
- `artifacts/review-notes.md`: review gate 샘플 출력
- `artifacts/validation-notes.md`: validation gate 샘플 출력

이 예시는 실제 서비스 코드 전체를 담는 폴더가 아니다. UI 없는 기능에서도 프레임워크가 어떻게 적용되는지 보여주는 참고 샘플이다.
