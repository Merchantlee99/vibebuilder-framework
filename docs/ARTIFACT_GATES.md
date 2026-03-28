# Artifact Gates

이 문서는 어떤 문서와 어떤 게이트가 있어야 구현과 릴리스를 진행할 수 있는지 정리한다.

## 문서 게이트

| 산출물 | 필수 내용 | 통과 기준 |
| --- | --- | --- |
| `Prompt.md` | 목표, 비목표, 제약, done-when | 한 문장으로 목표를 설명할 수 있다 |
| `PRD.md` | 사용자 문제, 핵심 흐름, acceptance criteria, 리스크 | 무엇을 만들고 무엇을 만들지 않는지 분명하다 |
| `Plan.md` | milestone, 검증 순서, 의존성, 종료 조건 | 구현 순서를 설명할 수 있다 |
| `Implement.md` | 현재 범위, write paths, validation loop | 지금 무엇을 수정하는지 분명하다 |
| `Documentation.md` | 상태, 결정 로그, known issues, 재개 지점 | 다음 세션에서 바로 이어갈 수 있다 |
| `Subagent-Manifest.md` | 역할, 입력, 출력, write scope | 병렬 역할이나 delegated write가 있을 때 충돌하지 않는다 |

## 단계별 게이트

### Gate 0: Problem Framing

기획 초기 확인한다.

- 기능 요청이 아니라 사용자 문제로 다시 썼는가
- 지금 pain과 기존 대안이 정리되었는가
- 이번 라운드의 가장 좁은 wedge가 보이는가
- 핵심 가정이 분리되었는가

이 단계는 `product-planner`가 맡는다.

### Gate 1: Readiness

구현 시작 전 확인한다.

- 목표가 분명한가
- acceptance criteria가 있는가
- 큰 미해결 결정이 남아 있지 않은가
- 이번 라운드 비범위가 적혀 있는가

판정:

- `go`: 구현 시작 가능
- `needs decision`: 구현 전 결정 필요
- `stop`: 문제 정의를 다시 해야 함

### Gate 2: Plan Review

scope freeze 전 확인한다.

- founder lens에서 범위가 과하지 않은가
- engineering lens에서 실패 경로와 검증 계획이 보이는가
- UI가 중요하면 design lens에서 핵심 상호작용이 정리되었는가

### Gate 3: Scope Freeze

구현 직전 확인한다.

- 이번 스프린트 범위가 고정되었는가
- 메인 writer가 누구인지 정해졌는가
- 병렬 작업이 있다면 write scope가 분리되었는가

### Gate 4: Review

- 계획 대비 구현 누락이 없는가
- 버그와 회귀 가능성이 없는가
- 테스트 공백이 없는가

### Gate 5: Validation / QA / Browse

- UI가 없으면 `validation`으로 충분한지 먼저 본다.
- UI가 있으면 `qa` 또는 `browse`로 실제 흐름을 확인한다.

`validation` 예시:

- 테스트 실행
- API smoke check
- CLI 실행 확인
- 수동 재현 절차 검증

- 변경의 핵심 경로를 실제로 재현했는가
- 오류 상태와 edge case를 확인했는가
- UI가 있으면 폼, 네비게이션, 레이아웃이 의도대로 보이는가

### Gate 6: Security

아래 중 하나라도 해당하면 수행한다.

- 인증
- 권한
- 결제
- 파일 업로드
- 사용자 데이터 저장 또는 노출
- 비밀 값과 토큰 처리

### Gate 7: Ship

- merge 또는 release 대상이면 수행한다.
- 테스트와 검증이 끝났는가
- 문서가 최신인가
- 데모 방법이 남아 있는가
- 롤백 또는 대응 포인트를 설명할 수 있는가

## 운영 메모

- 게이트는 체크박스 장식이 아니다.
- 게이트를 건너뛰면 이유를 `Documentation.md`에 남긴다.
- 게이트는 대화 단위가 아니라 산출물 단위로 실행한다.
- `Problem Framing -> Readiness -> Plan Review -> Scope Freeze`가 초기 기획 품질을 결정한다.
