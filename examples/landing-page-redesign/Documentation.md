# Documentation.md

## Current Status

- planner 정리 완료
- scope freeze 완료
- 구현은 Milestone 1부터 시작

## Decisions Log

- Date: 2026-03-27
  Decision: 이번 라운드는 랜딩 메인 페이지 리디자인만 다룬다
  Why: 전체 사이트 개편으로 가면 scope가 과해지고 재작업 리스크가 커진다
- Date: 2026-03-27
  Decision: testimonial 전체 섹션은 이번 라운드에서 제외한다
  Why: 현재 가장 큰 병목은 social proof 부족보다 메시지 구조와 CTA 문제이기 때문이다

## Known Issues

- 실제 전환율 데이터가 아직 없어, 이번 라운드는 질적 판단 중심 검증이다
- secondary CTA 위치는 review 결과에 따라 조정될 수 있다

## How To Run

```bash
npm install
npm run dev
```

## How To Verify

- 첫 화면에서 타깃 사용자와 문제 정의가 보이는지 확인
- primary CTA가 바로 보이는지 확인
- 모바일에서 hero 문구와 버튼이 깨지지 않는지 확인

## Resume Here

- Milestone 1 hero/CTA 구현 후 review gate 실행

## Next Options

- review 통과 후 pain-to-solution 본문 구조 수정
- 필요하면 testimonial teaser만 작은 블록으로 추가 검토
