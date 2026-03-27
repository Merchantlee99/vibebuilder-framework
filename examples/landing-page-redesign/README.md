# landing-page-redesign

이 예시는 `vibebuilder-framework`를 실제로 어떻게 굴리는지 보여주는 샘플 문서 세트다.

상황은 단순하다. 이미 있는 SaaS 랜딩페이지가 너무 일반적이고 전환 포인트가 약해서, `PM planner -> scope freeze -> single-writer implementation -> review/QA gate` 흐름으로 리디자인하는 경우를 가정한다.

## 이 예시가 보여주는 것

- planner가 문제를 기능이 아니라 사용자 pain으로 다시 쓰는 방식
- `solo-pro` mode를 고르는 기준
- oversight plan을 어떻게 선언하는지
- `scope freeze` 이후 구현 slice를 어떻게 자르는지
- review와 QA 결과를 어떤 식으로 남기는지

## 폴더 구성

- `Prompt.md`: 목표와 제약
- `PRD.md`: 문제 정의와 acceptance criteria
- `Plan.md`: milestone과 oversight plan
- `Implement.md`: 현재 sprint contract
- `Documentation.md`: 상태 기록과 재개 지점
- `artifacts/review-notes.md`: review gate 샘플 출력
- `artifacts/qa-notes.md`: QA gate 샘플 출력

이 예시는 실제 서비스 코드 전체를 담는 폴더가 아니다. 프레임워크를 프로젝트에 적용했을 때 문서와 게이트가 어떻게 채워지는지를 보여주는 참고 샘플이다.
