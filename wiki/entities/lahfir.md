---
title: lahfir
type: entity
domain: ai-news
tags: [ai-news, 개인개발자, rust, computer-use, macos]
created: 2026-09-24
updated: 2026-09-24
sources: [agent-desktop.md]
reliability: medium
---

# lahfir

[[agent-desktop]](★1,621 · Rust · Apache-2.0) 제작자. **개인 계정**이며 macOS 접근성 트리 기반 컴퓨터 유즈 CLI를 만든다.

> [!insight] 🎯 규모는 작고 **문서 규율은 상급**이다
> ★1,621은 이번 배치 최소 규모지만, README 487행이 다음을 **전부 값으로** 적었다:
> - 명령 수를 **두 개로 구분**: *"58 command names, **54 operational** commands"* — 이름과 동작을 분리
> - 동작하지 않는 4개를 **`ACTION_NOT_SUPPORTED` 로 fail-closed** (307행)
> - 권한을 **`granted`/`denied`/`unknown` 3값**으로, `unknown` = *"프롬프트 없이는 확인 불가"*
> - 플랫폼을 **7×3 표**로, Windows·Linux는 `Planned`(기능 없음을 숨기지 않음)
> → [[자기제한-명시]] · [[검사가능성-공사]] 양쪽의 사례. **작은 레포가 큰 레포보다 자기 경계를 잘 적는다**는 볼트 상관 관찰(09-17: *"한정어를 지킨 3건 전부 high"*)과 정합.

> [!warning] 🔴 단 하나의 예외 — 유일한 수치가 이미지 alt 속성 안에 있다
> *"78–96% token reduction"* 의 측정 방법이 **487행 전수에 없다**(`benchmark`·`measured`·`baseline` 어휘 0건). 구체 수치 1쌍은 29행 `<img alt="...30,743 tokens ... versus 383 ...">` **속성 안**에 있다(감소율 98.75% = 헤드라인 범위 **위**).
> → 문서 규율이 높은 저자도 **수치를 산문 밖에 둔다.** 볼트 [[PageIndex]](*"정확도는 그림 안에만"*)의 한 단계 나쁜 형태.

## ⬜ 미확인
- 실명·소속·국적 미확인. README에 저자 소개 없음.
- 다른 레포 미조회. `docs/faq.md`·`docs/architecture.png` 미열람.
- 🔴 **코드 미실행** — macOS 13.0+ 전용이라 볼트 환경에서 구동 자체 불가.

## 관련 페이지
- [[agent-desktop]] — 확인된 산출물
- [[agent-browser]] — agent-desktop이 CDP 경로로 선호 지목
- [[자기제한-명시]] · [[검사가능성-공사]] · [[PageIndex]]
- [[ai-news]]
