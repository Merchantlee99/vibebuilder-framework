# Subagent Policy

vibebuilder-framework에서 subagent는 상시 조직이 아니라, 필요한 순간에만 호출하는 전문가다.

`Subagent-Manifest.md`는 아래 중 하나라도 있을 때만 만든다.

- 메인 writer 외 역할을 명시적으로 호출한다
- delegated write scope를 문서화해야 한다
- reviewer, QA, security, release의 호출 시점을 프로젝트별로 고정해야 한다

## 기본 정책

- 메인 writer 외 역할은 기본적으로 read-only다.
- 병렬 작업이 필요하면 write scope를 먼저 문서화한다.
- 같은 경로를 두 writer가 동시에 수정하지 않는다.
- subagent를 부르기 전에 왜 필요한지와 종료 기준을 적는다.

## 기본 역할 표

| 역할 | 주 임무 | 기본 권한 | 호출 시점 | 출력 |
| --- | --- | --- | --- | --- |
| `product-planner` | 문제 정의, 범위 통제, readiness | docs write | 시작 전, scope drift 시 | Prompt, PRD, Plan, readiness |
| `main-writer` | 구현과 수정 | code + docs write | scope freeze 후 | 구현, 테스트, 문서 갱신 |
| `code-mapper` | 관련 파일, 구조, 의존성 파악 | read-only | 큰 코드베이스 탐색 시 | 맵, 영향 범위 |
| `reviewer` | 버그, 회귀, 누락 탐지 | read-only | 구현 후 | findings |
| `validator` | 테스트, API, CLI, runtime check | read-only | UI 없는 변경 후 | validation notes |
| `qa-browser` | 실제 사용자 흐름 재현 | read-only | UI, 웹, 폼 변경 후 | repro steps, screenshots, bugs |
| `security` | 인증, 권한, 데이터 보안 점검 | read-only | 민감 변경 후 | security findings |
| `release` | ship readiness, 문서 동기화 | docs write | merge, release 전 | ship checklist |

## write-enabled 예외

아래 조건을 모두 만족할 때만 메인 writer 외 역할에 쓰기 권한을 줄 수 있다.

- 메인 writer가 직접 승인했다.
- 수정 경로가 다른 writer와 겹치지 않는다.
- `Subagent-Manifest.md`에 write scope가 적혀 있다.
- 종료 후 누가 최종 통합할지 정해져 있다.

## manifest에 꼭 들어갈 것

- 역할 이름
- 왜 필요한가
- 읽는 파일
- 쓰는 파일
- 호출 시점
- 종료 기준

## 권장 순서

1. planner
2. main writer
3. reviewer
4. validator or qa/browser
5. security if needed
6. release

이 순서는 기본값이다. 작은 수정은 줄일 수 있지만, 큰 작업에서는 유지하는 편이 낫다.
