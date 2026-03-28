# Pivot Policy

scope freeze는 변경 금지가 아니라 무단 변경 금지다. 구현 중 인사이트는 허용하지만, 어떤 수준의 변경인지 구분해서 처리해야 한다.

## Minor Pivot

현재 sprint 안에서 처리 가능한 변경이다.

조건 예시:

- acceptance criteria의 핵심 의미가 유지된다
- 기존에 선언한 write path 범위 안에서 끝난다
- 새로운 민감 표면이 생기지 않는다
- required gate가 늘어나지 않는다
- 현재 milestone 안에서 끝낼 수 있다

처리 방식:

1. `Documentation.md`에 pivot note를 남긴다.
2. `Implement.md`의 sprint contract를 갱신한다.
3. 현재 sprint 안에서 계속 진행한다.

## Major Pivot

현재 sprint를 넘어 계획 재조정이 필요한 변경이다.

조건 예시:

- acceptance criteria 또는 non-goal의 의미가 바뀐다
- 비범위였던 기능이 핵심 범위로 들어온다
- 선언하지 않았던 새 디렉터리나 새 도메인으로 write path가 확장된다
- 인증, 권한, 결제, 업로드, 데이터 저장 같은 새 민감 표면이 생긴다
- review 외에 새 gate나 보안 검토가 필요해진다
- 현재 milestone을 넘겨 일정과 리스크가 다시 계산되어야 한다

처리 방식:

1. 구현을 잠시 멈춘다.
2. `product-planner`를 다시 호출한다.
3. `Prompt.md`, `PRD.md`, `Plan.md`를 갱신한다.
4. 새 `readiness`와 `scope freeze`를 수행한다.

## Pivot Trigger 예시

- 핵심 사용자 흐름이 바뀌었다
- UI 구조가 단일 화면에서 다단계 흐름으로 바뀌었다
- 단순 CRUD라고 생각했는데 권한 모델이 필요해졌다
- 로컬 상태만 다루려 했는데 서버 저장과 동기화가 필요해졌다

## 빠른 판정 체크

아래 질문 중 하나라도 `예`면 major pivot으로 본다.

- acceptance criteria를 다시 써야 하는가
- 기존 non-goal을 scope 안으로 가져와야 하는가
- 처음에 선언하지 않은 write path가 필요한가
- security gate 또는 추가 review gate가 새로 필요한가
- 현재 sprint 안에서 끝내기 어렵고 plan을 다시 잘라야 하는가

## 규칙

- pivot은 실패가 아니다. 숨기는 것이 실패다.
- minor pivot은 빠르게 흡수한다.
- major pivot은 planner로 되돌린다.
- 어떤 pivot이었는지 기록이 남아야 한다.
