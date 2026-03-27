# Pivot Policy

scope freeze는 변경 금지가 아니라 무단 변경 금지다. 구현 중 인사이트는 허용하지만, 어떤 수준의 변경인지 구분해서 처리해야 한다.

## Minor Pivot

현재 sprint 안에서 처리 가능한 변경이다.

조건 예시:

- acceptance criteria의 핵심 의미는 유지된다
- write path가 크게 늘어나지 않는다
- 검증 방법이 크게 바뀌지 않는다
- 일정과 리스크가 급격히 증가하지 않는다

처리 방식:

1. `Documentation.md`에 pivot note를 남긴다.
2. `Implement.md`의 sprint contract를 갱신한다.
3. 현재 sprint 안에서 계속 진행한다.

## Major Pivot

현재 sprint를 넘어 계획 재조정이 필요한 변경이다.

조건 예시:

- acceptance criteria의 의미가 바뀐다
- 비범위였던 기능이 핵심 범위로 들어온다
- write path가 크게 늘어난다
- 새로운 gate나 보안 검토가 필요해진다

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

## 규칙

- pivot은 실패가 아니다. 숨기는 것이 실패다.
- minor pivot은 빠르게 흡수한다.
- major pivot은 planner로 되돌린다.
- 어떤 pivot이었는지 기록이 남아야 한다.
