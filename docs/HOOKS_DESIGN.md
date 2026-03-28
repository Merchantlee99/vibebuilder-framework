# Hooks Design

이 문서는 vibebuilder-framework를 Codex hooks 위에서 더 강하게 작동시키기 위한 설계안이다.

목표는 프레임워크의 철학을 바꾸는 것이 아니다. `PM-first`, `single-writer`, `dynamic oversight`, `gated review`를 사람이 잊어도 계속 지키기 쉽게 만드는 것이다.

## 이 문서가 다루는 것

- 어떤 hook 이벤트를 쓸 것인가
- 어디까지는 경고하고 어디부터는 막을 것인가
- `solo-lite`, `solo-pro`, `team`에서 강도를 어떻게 나눌 것인가
- hooks가 읽을 최소 상태를 어디에 둘 것인가

## 전제

이 설계는 현재 Codex hooks 제약을 전제로 한다.

- hooks는 유용한 guardrail이지만 완전한 hard gate는 아니다.
- 특히 `PreToolUse`는 shell 기반 행동을 막는 데 더 적합하다.
- 그래서 핵심 차단은 `UserPromptSubmit`와 `SessionStart`에서 먼저 걸고, shell 행동은 `PreToolUse`로 한 번 더 막는 구조가 현실적이다.

즉, 이 설계는 `hard harness`가 아니라 `soft harness를 강하게 만드는 설계`다.

## 설계 원칙

- 문서 철학을 해치지 않는다. 문서는 계속 source of truth다.
- mode에 따라 강도를 다르게 둔다.
- 작은 작업은 가능한 한 흐름을 막지 않는다.
- 새 기능, 민감 변경, release 전 단계는 더 엄격하게 본다.
- hooks는 긴 설명 대신 다음 행동을 짧게 지시한다.
- 가능한 한 `경고 -> 차단` 순서로 설계한다.

## 권장 파일 구조

```text
.codex/
  hooks/
    session_start.py
    user_prompt_submit.py
    pre_tool_use.py
    post_tool_use.py
    stop.py
.vibebuilder/
  runtime.json
```

## 왜 별도 runtime 상태 파일이 필요한가

현재 프레임워크의 진짜 기준은 `Prompt.md`, `PRD.md`, `Plan.md`, `Implement.md`, `Documentation.md`다.

하지만 hooks가 자유 서술형 문서를 매번 안정적으로 파싱하는 것은 취약하다. 그래서 hooks 전용으로 아주 작은 상태 파일을 하나 둔다.

- 문서가 source of truth
- `.vibebuilder/runtime.json`은 hooks가 읽는 control plane

즉, runtime 파일은 문서를 대체하지 않는다. hooks가 빠르게 판정하기 위한 요약 상태만 가진다.

## runtime.json 권장 스키마

```json
{
  "mode": "solo-pro",
  "planner_of_record": "codex-product-planner",
  "task_type": "ui_feature",
  "docs": {
    "prompt": true,
    "prd": true,
    "plan": true,
    "implement": true,
    "documentation": true,
    "subagent_manifest": false
  },
  "planning": {
    "readiness": "go",
    "scope_freeze": true,
    "required_gates": ["review", "qa"],
    "security_needed": false,
    "release_bound": false
  },
  "execution": {
    "current_slice": "hero redesign and CTA rewrite",
    "writer": "codex",
    "write_paths": ["src/app", "src/components/marketing"],
    "review_done": false,
    "validation_done": false,
    "qa_done": false,
    "security_done": false,
    "ship_done": false
  }
}
```

## 권장 상태 해석

- `mode`: [docs/MODES.md](./MODES.md)의 적용 강도
- `task_type`: `small_fix`, `backend_change`, `ui_feature`, `sensitive_change`, `release_prep`
- `readiness`: `go`, `needs_decision`, `stop`
- `scope_freeze`: 큰 구현을 시작해도 되는지
- `required_gates`: 이번 라운드에서 실제로 필요한 게이트
- `write_paths`: 현재 `Implement.md`와 맞아야 하는 경로

## Hook 이벤트 설계

### 1. SessionStart

세션을 열자마자 현재 프로젝트 상태를 짧게 주입한다.

확인할 것:

- `AGENTS.md` 존재 여부
- `.vibebuilder/runtime.json` 존재 여부
- 필수 문서 존재 여부
- 현재 mode
- readiness / scope freeze 상태
- 아직 안 끝난 게이트

행동:

- 상태 요약을 developer context로 주입
- 누락 문서나 미완료 게이트가 있으면 첫 턴에서 짧게 경고
- `solo-pro` 이상인데 runtime 파일이 없으면 먼저 초기화하라고 유도

절대 하지 말 것:

- 세션 시작마다 장문 강의
- `solo-lite` 작은 수정까지 planner를 강제 차단

### 2. UserPromptSubmit

실질적인 workflow gate의 중심이다. 사용자의 새 요청이 들어올 때 분류하고, 지금 상태에서 바로 실행 가능한지 판단한다.

분류 예시:

- `new_feature`
- `small_fix`
- `continuation`
- `review_request`
- `debug_request`
- `release_request`

주요 규칙:

- `new_feature`인데 `solo-pro` 이상이고 `Prompt/PRD/Plan`이 없으면 차단
- `new_feature`인데 `readiness != go`면 차단
- 큰 구현 요청인데 `scope_freeze == false`면 차단
- `small_fix`면 경고만 하고 통과 가능
- `release_request`인데 필수 게이트가 안 끝났으면 차단

반환 메시지 원칙:

- 긴 설명 대신 왜 막았는지 한 줄
- 다음 행동 한 줄
- 필요한 skill 또는 문서 한 줄

예시:

- `새 기능 작업인데 아직 PRD/Plan이 없습니다. 먼저 product-planner로 범위를 고정하세요.`
- `현재 scope freeze 전입니다. 큰 구현 대신 Prompt.md와 Plan.md를 먼저 정리하세요.`

### 3. PreToolUse

shell 기반 행동을 막는 보조 게이트다.

우선순위가 높은 차단 대상:

- `git add`, `git commit`, `git push` 같은 릴리스 성격 명령
- 대규모 코드 생성 또는 실행 명령
- 위험한 파일 조작 명령

주요 규칙:

- `scope_freeze == false`인데 대규모 구현/빌드/커밋 성격 명령이면 차단
- `review_done == false`인데 `git commit`이면 차단
- `required_gates`에 `validation`이 있는데 `validation_done == false`이면 커밋 또는 푸시 차단
- `required_gates`에 `qa`가 있는데 `qa_done == false`이면 release 성격 명령 차단
- `security_needed == true`인데 `security_done == false`이면 merge/push 차단

주의:

- 이 hook은 shell 행동에 더 적합하다.
- editor 내부 변경 자체를 완전하게 막는 용도라고 가정하면 안 된다.

### 4. PostToolUse

도구 사용 결과를 보고 다음 행동을 수정한다.

예시:

- 테스트가 실패했으면 `validation_done`을 false로 유지하고 다음 턴에서 수정 루프로 유도
- 브라우저 재현이 실패했으면 `qa_done`을 false로 유지
- review 결과가 심각하면 ship 단계로 못 가게 경고

권장 역할:

- 상태 파일 갱신 보조
- 실패한 검증 결과를 문서 갱신 요구와 연결

### 5. Stop

세션 종료 직전에 문서 동기화를 강하게 체크한다.

확인할 것:

- `Documentation.md`가 오늘 작업 상태를 반영하는가
- write path가 바뀌었으면 `Implement.md`가 갱신됐는가
- major pivot이 있었으면 `PRD.md` 또는 `Plan.md`가 갱신됐는가
- 미완료 게이트가 남아 있으면 다음 재개 지점이 적혀 있는가

행동:

- 종료 자체를 무조건 막기보다 마지막 경고를 준다
- `solo-pro` 이상에서는 `Documentation.md` 미갱신 시 종료 직전 강한 경고

## Mode별 강도

### solo-lite

기본값:

- 경고 중심
- 차단은 release/파괴적 행동 위주

차단 권장:

- 리뷰나 문서 없는 상태의 release 요청
- 민감 변경인데 security 없이 push하려는 경우

나머지는 가능한 한 경고만 한다.

### solo-pro

기본값:

- planning과 finish gate는 일부 차단
- 작은 수정은 통과 가능

차단 권장:

- 새 기능인데 planner 문서 없음
- `scope_freeze == false` 상태의 큰 구현 요청
- `review` 또는 `validation/qa` 미완료 상태의 commit/push

### team

기본값:

- 가장 강한 차단
- 역할 충돌과 write scope 충돌을 적극적으로 막음

추가 차단 권장:

- `Subagent-Manifest.md` 없음
- write scope 미선언
- planner-of-record 미정 상태

## 어떤 요청을 자동 차단할 것인가

아래는 차단 가치가 높은 항목이다.

- 새 기능인데 planner 문서가 없다
- `readiness`가 `go`가 아니다
- `scope_freeze` 전에 큰 구현을 시작한다
- 필수 게이트 없이 commit/push/release를 하려 한다
- 민감 변경인데 security gate가 빠졌다
- 병렬 작업인데 write scope가 선언되지 않았다

## 어떤 요청은 경고만 할 것인가

아래는 흐름을 해치지 않기 위해 경고에 머무는 편이 좋다.

- `solo-lite`의 작은 버그 수정
- 문구 수정, 스타일 미세 조정
- 기존 acceptance criteria 안에서 끝나는 작은 리팩터링
- 세션 종료 직전 문서 갱신 누락

## Hook별 판정 매트릭스

| 상황 | solo-lite | solo-pro | team |
| --- | --- | --- | --- |
| 새 기능인데 PRD/Plan 없음 | warn | block | block |
| scope freeze 전 큰 구현 | warn | block | block |
| review 없이 commit | warn | block | block |
| validation/qa 없이 push | warn | block | block |
| security 없이 민감 변경 push | block | block | block |
| Documentation 미갱신 종료 | warn | warn strong | warn strong |
| Subagent manifest 없이 병렬 작업 | warn | warn | block |

## 구현 순서 권장

처음부터 모든 hook을 다 켜지 않는다.

### Phase 1

- `SessionStart`
- `Stop`

효과:

- 문서 맥락 복구
- 종료 전 기록 누락 감소

### Phase 2

- `UserPromptSubmit`

효과:

- 새 기능과 작은 수정 구분
- planner 미통과 구현 감소

### Phase 3

- `PreToolUse`
- `PostToolUse`

효과:

- commit/push/release 전 게이트 누락 차단
- 테스트/QA 실패 후 상태 복구

## 엣지케이스

### 1. planner 없이 바로 시작해도 되는 작은 수정

모든 수정에 planner를 강제하면 프레임워크가 안 쓰인다. 반드시 `small_fix` 분류 경로를 둬야 한다.

### 2. 문서는 있는데 runtime 상태 파일이 낡았다

이 경우 hooks는 강차단보다 `runtime.json 갱신 필요` 경고를 먼저 주는 편이 안전하다.

### 3. UI 없는 프로젝트

`qa/browse`를 강제하지 않는다. 이 경우 `validation`이 기본 게이트다.

### 4. 디버깅 세션

디버깅은 구현과 달리 `systematic-debugging` skill로 우회 진입할 수 있어야 한다. 다만 write path가 커지면 major pivot 검사로 다시 planner에 연결해야 한다.

### 5. 문서가 없는 기존 프로젝트에 프레임워크를 도입하는 경우

처음 한 번은 `retrofit mode`를 허용해야 한다. 즉, 기존 상태를 역으로 문서화하는 턴은 막지 않는다.

## 이 설계에서 일부러 하지 않는 것

- 모든 대화 턴에 planner를 강제하지 않는다.
- 모든 작업에 full PRD를 강제하지 않는다.
- 모든 write 행동을 기술적으로 봉쇄하려고 하지 않는다.
- hooks가 문서를 대체하게 만들지 않는다.

## 한 줄 결론

vibebuilder-framework용 hooks는 `사람이 프레임워크를 기억해야만 작동하는 상태`에서 `Codex가 상태를 읽고 먼저 경고하고, 중요한 순간에는 막아주는 상태`로 올리기 위한 설계다.
