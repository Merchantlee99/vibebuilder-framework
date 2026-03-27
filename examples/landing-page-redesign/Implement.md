# Implement.md

## Current Slice

- Milestone 1: hero와 CTA 구조 재설계

## Write Paths

- `src/pages/index.tsx`
- `src/components/landing/Hero.tsx`
- `src/styles/landing.css`

## Read Paths

- `Prompt.md`
- `PRD.md`
- `Plan.md`
- 기존 랜딩페이지 컴포넌트 파일

## Planned Changes

- hero headline을 문제 중심 메시지로 교체
- subcopy를 기능 목록 대신 outcome 중심으로 재작성
- primary CTA를 데모 요청으로 고정
- secondary CTA는 제품 소개 보기로 유지

## Sprint Contract

- Outcome: 첫 화면에서 타깃 사용자, 문제, CTA가 더 빨리 이해된다.
- Done definition: 새 hero layout과 CTA hierarchy가 구현되고, 내부 review에서 방향성이 통과된다.
- Evidence to collect: before/after screenshot, CTA visibility note
- Failure threshold: 첫 화면 메시지가 여전히 모호하거나 CTA가 fold 아래로 밀리면 실패
- Required gate after this slice: review
- Pivot trigger: hero만 수정하려 했는데 정보 구조 전체 재배치가 필요해지는 경우

## Validation Loop

1. desktop hero 스냅샷 확인
2. mobile hero 스냅샷 확인
3. CTA visibility와 copy clarity 자가 점검

## Risks During Implementation

- copy 변경이 많아지면 scope가 content overhaul로 커질 수 있다.
- layout 변경 중 기존 section spacing이 연쇄적으로 깨질 수 있다.

## Gate After This Slice

- review
- qa or browse
