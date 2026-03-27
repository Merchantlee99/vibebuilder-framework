# Reference Alignment

이 문서는 vibebuilder-os가 어떤 레퍼런스를 어떻게 해석해 사용하고 있는지 정리한다.

## 참고 레퍼런스

- [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
- [garrytan/gstack](https://github.com/garrytan/gstack)
- [agentsmd/agents.md](https://github.com/agentsmd/agents.md)

## 레퍼런스별 반영 방식

| 레퍼런스 | 가져온 핵심 | vibebuilder-os에서 반영한 위치 | 그대로 복제하지 않은 이유 |
| --- | --- | --- | --- |
| `pm-skills` | discovery, assumption mapping, PRD/execution 구조화 | `product-planner`, `templates/PRD.md`, `templates/Plan.md` | 전체 마켓플레이스를 들이는 대신 planner 핵심 절차만 가져오기 위해 |
| `gstack` | office-hours식 재정의, CEO/eng/design review, review/qa/browse/ship 게이트 | `product-planner`, `gstack-gates`, `docs/ARTIFACT_GATES.md` | 상시 오케스트레이션보다 단계별 게이트로 쓰는 것이 더 안정적이기 때문 |
| `agents.md` | 예측 가능한 전역 지시 파일 | `AGENTS.md` | 프로젝트 헌법은 얇고 강하게 두는 편이 좋기 때문 |

## 현재 해석

vibebuilder-os는 레퍼런스를 이렇게 나눠 쓴다.

- `agents.md`는 규칙의 위치를 정한다.
- `pm-skills`는 기획자의 사고 절차를 제공한다.
- `gstack`는 계획 검토와 후반 품질 게이트를 제공한다.

즉, 이 저장소는 어떤 하나의 레퍼런스를 그대로 따르지 않는다. 각 레퍼런스가 가장 잘하는 지점만 따로 가져와 하나의 운영체계로 합친다.

## 프로급 기준에서의 체크포인트

아래가 유지되면 프로급 운영으로 본다.

- 새 작업은 planner를 거친다.
- planner는 problem framing과 assumption prioritization을 수행한다.
- scope freeze 전에는 큰 구현을 시작하지 않는다.
- 구현은 single writer가 맡는다.
- 구현 후 review, QA, security, ship 게이트가 존재한다.
- 장기 맥락은 프로젝트 문서에 남는다.

이 체크포인트 중 빠진 것이 있으면, vibebuilder-os의 핵심 설계가 무너진 것으로 본다.
