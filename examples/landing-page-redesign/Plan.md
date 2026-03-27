# Plan.md

## Objective

- 기존 랜딩페이지를 더 명확한 메시지 구조와 CTA 흐름으로 리디자인해, 제품 가치 전달과 데모 요청 가능성을 높인다.

## Readiness Decision

- Status: go
- Why: 문제 정의, 이번 라운드 범위, acceptance criteria, 주요 리스크가 충분히 정리되었고 구현을 막는 큰 결정이 없다.

## Oversight Plan

- Mode: solo-pro
- Required lenses: discovery, founder, pm, engineering, design
- Optional lenses skipped: security
- Required gates: review, qa
- Evidence needed: before/after screenshot, mobile viewport check, CTA visibility check
- Pivot triggers: testimonial 요구 추가, 새 페이지 생성 요구, write path가 3개 이상 컴포넌트로 확대

## Milestones

### Milestone 1

- Outcome: 새 hero와 CTA 구조를 확정한다.
- Tasks: headline, subcopy, CTA hierarchy, hero layout 재설계
- Validation: 첫 화면만 보고도 타깃 사용자와 문제 정의가 이해되는지 자체 점검

### Milestone 2

- Outcome: pain-to-solution 본문 구조를 정리한다.
- Tasks: pain section, solution section, lightweight proof section 배치
- Validation: 정보 흐름이 기능 나열이 아니라 문제 해결 흐름으로 보이는지 점검

### Milestone 3

- Outcome: 모바일 레이아웃과 마감 품질을 정리한다.
- Tasks: spacing, wrap, CTA 위치, 섹션 간 간격 수정
- Validation: 모바일 뷰포트와 데스크톱에서 block issue가 없는지 확인

## Dependencies

- 기존 디자인 토큰
- 기존 랜딩페이지 컴포넌트 구조
- 제품 핵심 메시지 정리본

## Plan Review

- Founder lens: 전체 개편이 아니라 가장 큰 전환 병목인 hero와 메시지 구조에 집중하는 범위가 적절하다.
- Engineering lens: 프론트엔드 리디자인만으로 제한되어 있어 write path와 리스크가 통제 가능하다.
- Design lens if needed: UI 완성도보다 메시지 전달과 CTA hierarchy를 우선하는 방향이 맞다.

## Risk Register

- Risk: 범위가 전체 사이트 리브랜딩으로 확장될 수 있다.
  Mitigation: 이번 라운드는 랜딩 메인 페이지만 대상으로 고정한다.
- Risk: copy 수정과 layout 수정이 동시에 커질 수 있다.
  Mitigation: first pass에서 정보 구조를 먼저 잠그고 세부 표현은 후순위로 둔다.

## Validation Plan

- before/after 비교 메모를 남긴다.
- review에서 completeness gap과 CTA visibility를 본다.
- QA에서 모바일 2개 뷰포트와 데스크톱 1개 뷰포트를 확인한다.

## Exit Criteria

- acceptance criteria가 모두 충족된다.
- review finding이 block 없이 정리된다.
- QA finding이 warn 이하로 정리된다.
