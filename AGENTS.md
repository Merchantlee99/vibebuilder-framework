# AGENTS.md

vibebuilder-framework를 사용하는 저장소는 이 문서를 기본 운영 헌법으로 삼습니다.

## 기본 원칙

- 기본 응답 언어는 한국어다.
- 가정은 숨기지 않고 짧게 명시한다.
- 길게 설명하는 것보다, 다음 행동과 판단 기준을 분명하게 적는다.
- 장기 작업의 기억은 채팅이 아니라 파일에 남긴다.
- 구현 품질보다 속도가 중요한 순간은 있어도, 방향이 틀린 채 빠르게 가는 것은 허용하지 않는다.

## 운영 모델

- 기본 구조는 `planner -> main writer -> evaluators`다.
- 작업 강도는 `docs/MODES.md` 기준으로 고른다. 확신이 없으면 `solo-pro`를 기본값으로 둔다.
- 어떤 감독과 평가가 필요한지는 `docs/OVERSIGHT_POLICY.md` 기준으로 planner가 선언한다.
- `product-planner`는 시작 단계와 산출물 게이트에서만 개입한다.
- 실제 코드 경로를 크게 수정하는 writer는 한 명만 둔다.
- reviewer, QA, security, browser 역할은 기본적으로 읽기와 검증을 맡는다.
- subagent나 추가 역할은 항상 필요한 순간에만 켠다. 상시 대기 조직을 만들지 않는다.

## 언제 planner를 먼저 써야 하는가

아래 조건 중 하나라도 해당하면 구현보다 먼저 `product-planner`를 적용한다.

- 새 기능, 새 제품, 새 워크플로를 시작한다.
- 요청이 모호하거나 범위가 쉽게 커질 수 있다.
- 사용자 문제와 해결 방식이 아직 분리되지 않았다.
- 인증, 결제, 데이터 모델, 권한처럼 초기에 잘못 잡으면 비용이 큰 결정이 있다.
- 구현 도중 범위가 바뀌어 기존 계획이 흔들린다.

아래처럼 작은 작업은 planner를 생략할 수 있다.

- 단일 파일의 명백한 버그 수정
- 문구 수정, 스타일 미세 조정, 사소한 리팩터링
- 기존 acceptance criteria 안에서 끝나는 작업

작은 작업이어도 `Documentation.md`에는 무엇을 바꿨는지 남긴다.

## 필수 산출물

비사소한 작업은 아래 파일을 기준으로 진행한다.

- `Prompt.md`: 목표, 비목표, 제약, done-when
- `PRD.md`: 사용자 문제, 핵심 흐름, acceptance criteria, 리스크
- `Plan.md`: milestone, 검증 계획, 순서, 종료 조건
- `Implement.md`: 현재 작업 범위, write paths, 검증 루프
- `Documentation.md`: 상태, 결정 로그, known issues, 재개 지점
- `Subagent-Manifest.md`: 역할, 호출 시점, write scope, 종료 기준

프로젝트마다 이 파일들을 `templates/`에서 복사해 시작한다.

`Subagent-Manifest.md`는 항상 필요한 문서는 아니다. 아래 중 하나라도 있을 때만 만든다.

- 메인 writer 외에 역할을 명시적으로 호출한다.
- write scope를 둘 이상으로 나눠야 한다.
- reviewer, QA, security, release 중 누가 언제 개입하는지 문서화가 필요하다.

## 구현 전 게이트

구현은 아래 조건이 만족된 뒤 시작한다.

- 문제 정의가 한 문장으로 요약된다.
- 이번 스프린트의 범위와 비범위가 분리되어 있다.
- acceptance criteria가 문장으로 적혀 있다.
- 큰 미해결 의사결정이 남아 있지 않다.
- 누가 쓰고 누가 검토하는지 정해져 있다.
- founder lens와 engineering lens에서 큰 반려 사유가 없다.
- UI가 중요하면 design lens 점검이 끝나 있다.

이 상태를 `scope freeze`라고 부른다. freeze 전에는 큰 코드 작업을 시작하지 않는다.

## 구현 중 원칙

- 메인 writer 한 명만 실제 write path를 소유한다.
- 여러 사람이 병렬로 일해야 하면 write scope가 서로 겹치지 않아야 한다.
- 구현은 milestone 단위로 자르고, 각 slice마다 바로 검증한다.
- 계획 밖 요청이 들어오면 바로 확장하지 말고 planner 단계로 되돌린다.
- 구현 중 발견한 변경은 `docs/PIVOT_POLICY.md` 기준으로 minor 또는 major pivot으로 분류한다.
- 코드를 바꾸면 `Implement.md`와 `Documentation.md`도 같이 갱신한다.

## 구현 후 게이트

구현이 끝나면 아래 순서로 통과시킨다.

1. `review`
2. `validation` 또는 `qa` 또는 `browse`
3. `cso` if needed
4. `ship` if release-bound

게이트는 대화 중간중간 끼어드는 상시 심판이 아니다. 산출물이 생겼을 때만 동작한다.

초기 기획 단계에는 별도의 plan review 게이트가 있다. `product-planner`는 discovery, founder, PM, engineering, design 렌즈를 거쳐 readiness를 판정한다.

## 역할 규칙

- `product-planner`: 문제 정의, 범위 통제, readiness 판단
- `main writer`: 구현과 수정의 단일 책임자
- `reviewer`: 버그, 회귀, 누락, 테스트 부족 탐지
- `validation`: 테스트, API, CLI, runtime check 확인
- `qa/browser`: 실제 흐름 재현, 회귀 확인
- `security`: 인증, 권한, 데이터 민감 구간 점검
- `release`: 배포 준비, 체크리스트, 문서 동기화

리뷰어, validator, QA가 직접 코드를 고치는 일은 예외다. 예외가 필요하면 write scope를 다시 선언한다.

## 문서 갱신 규칙

작업 종료 전에 반드시 확인한다.

- `Documentation.md`에 현재 상태와 다음 재개 지점이 적혀 있는가
- 결정이 바뀌었으면 이유가 남아 있는가
- 테스트, 데모, 실행 방법이 최신 상태인가
- 기존 계획과 달라진 점이 있으면 `Plan.md`나 `PRD.md`에 반영했는가

## 금지 사항

- 계획이 없는 상태에서 큰 구현부터 시작하기
- 같은 코드 경로를 여러 writer가 동시에 수정하기
- planner를 매 턴 호출해서 흐름을 끊기
- 장기 맥락을 채팅에만 남기고 파일에 기록하지 않기
- review, validation, QA, security 게이트를 "시간 없으니 이번엔 생략"으로 습관화하기
