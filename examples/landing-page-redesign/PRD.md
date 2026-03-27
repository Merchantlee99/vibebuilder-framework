# PRD.md

## Problem Statement

- 현재 랜딩페이지는 디자인 완성도보다 메시지 구조가 약해서, 방문자가 제품을 빠르게 이해하지 못하고 이탈한다.

## User Pain And Current Workaround

- Pain: 바쁜 팀 리더나 창업자는 제품을 검토할 시간이 짧아서, 첫 화면에서 가치가 안 보이면 바로 닫는다.
- Current workaround: 사용자는 FAQ나 하단 섹션까지 내려가며 제품을 이해하려 하지만, 대부분 그 전에 이탈한다.
- Why now: 현재 데모 요청 전환율이 낮고, 제품 소개 콜에서도 랜딩페이지가 제품을 충분히 설명하지 못하고 있다.

## Target User

- 일정 관리와 회의 준비에 시간을 많이 쓰는 팀 리더, 창업자, 운영 담당자

## User Story

- 바쁜 방문자로서, 첫 화면에서 바로 이 제품이 어떤 문제를 해결하는지 알고 싶다. 그래야 데모를 요청할지 빠르게 판단할 수 있다.

## Core Flow

1. 방문자가 첫 화면에서 타깃 사용자와 핵심 문제를 이해한다.
2. 그다음 섹션에서 현재 pain과 제품 해결 방식을 짧게 본다.
3. CTA를 통해 데모 요청 또는 제품 소개 확인으로 이동한다.

## Scope For This Round

- 히어로 메시지 재작성
- pain-to-solution 섹션 추가 또는 재구성
- CTA hierarchy 정리
- 모바일 레이아웃 정리

## Out Of Scope

- 가격 페이지 개편
- 블로그, FAQ 전체 리뉴얼
- 고객 사례 CMS화
- A/B 테스트 도구 연동

## Options Considered

- Option: 기존 구조를 유지하고 문구만 다듬기
  Why not chosen: 메시지보다 구조 자체가 약해서 copy만 바꿔서는 개선 폭이 작다.
- Option: 전체 사이트를 새 디자인 시스템으로 갈아엎기
  Why not chosen: 이번 라운드 scope와 리스크가 너무 크다.

## Acceptance Criteria

- 첫 화면에서 타깃 사용자와 문제 정의가 한눈에 보인다.
- 핵심 CTA가 above the fold에서 식별된다.
- 모바일 width에서 hero, CTA, body section이 깨지지 않는다.
- 제품 기능이 아니라 사용자 pain과 outcome 중심으로 정보가 배치된다.

## Key Assumptions

- 전환 저하의 핵심 원인은 메시지 구조와 CTA 배치다.
- 이번 라운드에서 testimonial 없이도 가치 전달은 개선될 수 있다.
- 기존 코드 구조를 유지한 채 리디자인이 가능하다.

## Risks

- copy와 layout을 같이 바꾸면 범위가 커질 수 있다.
- 디자인 욕심이 커지면 이번 sprint를 넘길 수 있다.

## Open Decisions

- testimonial teaser를 넣을지
- CTA를 단일 버튼으로 갈지, secondary CTA를 둘지

## Success Signal

- 내부 리뷰에서 "첫 화면만으로 무엇을 하는 제품인지 이해된다"는 피드백을 얻는다.
- QA에서 모바일 레이아웃 이슈가 block 없이 통과한다.
