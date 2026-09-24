---
title: "agent-desktop — 접근성 트리 기반 컴퓨터 유즈 (수치가 이미지 alt 속성에 있었다)"
type: source
domain: ai-news
tags: [ai-news, github-trending, computer-use, accessibility, rust, macos, fail-closed, 검사가능성, tool]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: high
---

# lahfir/agent-desktop — 픽셀 대신 OS 접근성 트리로 앱을 조작한다

**GitHub**: https://github.com/lahfir/agent-desktop
**스타수**: ⭐**1,621** (2026-09-24 09:00 · 당일 **+107** · 드리프트 **0** — 수집기 값과 완전일치) · forks 109 · open issues 20
**언어**: Rust (1.89+) · Apache-2.0 · **created** 2026-02-19 · **pushed** 2026-09-23 · topics `computer-use` `accessibility-api`

> [!insight] 핵심 인사이트
> **픽셀을 추측하지 않는 컴퓨터 유즈다.** 스크린샷에서 좌표를 짐작하는 대신 macOS 접근성 트리에서 실제 UI 구조를 읽고, 요소마다 **한정 ref**(`@s8f3k2p9:e1`)를 발급해 재시도가 안전해진다. 🎯 그런데 이 레포의 진짜 가치는 능력이 아니라 **자기 능력의 경계를 값으로 노출한 방식**이다 — 명령 4개는 `ACTION_NOT_SUPPORTED` 로 **fail-closed** 하고, 권한은 `granted/denied/unknown` **3값**으로 답한다.

> [!note] 확인 범위 (볼트 실측)
> **README 487행 전문 열람**(수집기는 상단 45행만) — 목차 14개 `##` 전수 + `Platform Support` 표 + `Key Features` + FAQ. GitHub API 실측. 🔴 **코드 미실행** — macOS 미보유 환경이라 CLI 구동 자체가 불가(플랫폼 제약이 곧 실행 장벽).

## 🎯 볼트 최대 발견 — **수치는 있었다. 산문이 아니라 이미지 alt 속성에 있었다**

수집기: *"「78–96% 토큰 감소」는 **저자 주장이고 측정 조건·대조군이 README 상단에 없다**(488행 중 45행만 열람)"* — 정직한 유보였다. 볼트가 487행 전문을 확인한 결과:

1. 🔴 **`benchmark` · `methodology` · `measured` · `baseline` · `evaluation` 어휘가 전문에 0건.** 측정 방법 서술은 실제로 없다. → **유보를 확정 부재로 승격**(범위: README 487행 전수).
2. 🎯 **그런데 구체 수치 1쌍이 있었다 — 29행 `<img>` 의 `alt` 속성 안에**:
   > *"Slack accessibility snapshots: **30,743 tokens** for a regular snapshot versus **383** for a skeleton overview, with focused drilling for controls"*
   → **383 / 30,743 = 1.246% → 감소율 98.75%**
3. 🔴 **그 값은 헤드라인 주장 범위(78–96%)를 벗어난다 — 위로.** 저자의 단일 예시가 저자의 헤드라인보다 **좋다.** [[한정어-탈락]] 은 보통 주장이 근거를 초과하는 방향인데, 여기선 **반대로 헤드라인이 더 보수적이다.**

> [!warning] 🔴 볼트 자신에 대한 교훈 — 어휘 grep은 마크업 속성을 못 본다
> 볼트 1차 판정은 *"측정 근거 0건"* 이었다. `benchmark|measured|baseline` 로 grep 했기 때문이다. **수치는 `alt=` 안에 있었고 그 어휘를 하나도 쓰지 않았다.**
> 볼트는 이미 *"정확도는 **그림 안에만**"*([[PageIndex]])을 기록해 뒀다. 이번은 한 칸 더 나쁜 형태다 — **그림 안이 아니라 그림의 설명 속성 안**이라서, 사람은 그림을 보면 알지만 **텍스트 검색은 통과한다.** → 앞으로 README 수치 탐색에 `alt=` · `title=` · 이미지 캡션을 포함한다.

## 능력 — README 축자 대조

| 항목 | README 원문 | 볼트 확인 |
|---|---|---|
| 명령 수 | 44행 *"**58 command names, 54 operational commands**"* | ✅ 축자 일치 |
| fail-closed 4개 | 44행 *"The four held-input names are **reserved for a stateful daemon and fail closed** in the stateless CLI"* · 307행 `key-down`/`key-up` → `ACTION_NOT_SUPPORTED` | ✅ 확인 |
| 권한 3값 | 95행 *"Automation reports `granted`, `denied`, or `unknown`; **`unknown` means macOS would need to prompt or System Events could not be probed without prompting**"* | ✅ 축자 일치 |
| C-ABI cdylib | 99행 — `libagent_desktop_ffi`, Python/Swift/Go/Ruby/Node/C 에서 `dlopen` | ✅ (수집기는 4언어, 실제 **6언어**) |
| 요구사항 | 75행 *"Requires Rust 1.89+ and macOS 13.0+"* | ✅ |

> [!warning] 🟡 수집기 정정 — "리눅스/윈도우 **불가**" 는 README가 쓴 말이 아니다
> README **460행 `## Platform Support`** 표 실측: 7개 기능(접근성 트리·클릭/타이핑·마우스·스크린샷·클립보드·앱/윈도우 관리·알림) 전부 **macOS `Yes` / Windows `Planned` / Linux `Planned`**.
> - 수집기: *"macOS 13.0+ **전용** — 리눅스/윈도우 **불가**"*
> - README: **`Planned`**
> 🎯 그리고 99행은 cdylib을 **macOS·Linux·Windows 3플랫폼에 배포**한다고 쓴다. 235행이 이 긴장을 스스로 해소한다 — *"Windows and Linux **inherit the adapter's no-op**"*. → **배포 대상 ≠ 동작 대상.** 바이너리는 3플랫폼에 가고 기능은 1플랫폼에만 있다. *"불가"* 와 *"Planned"* 는 로드맵 유무가 다르므로 [[한정어-탈락]] 의 경미한 사례로 기록한다.

> [!insight] 🎯 `unknown` — 볼트 자신의 미이행 actionable이 5일째 외부에서 재확인되고 있다
> `unknown` 의 정의가 *"프롬프트 없이는 확인할 수 없다"* 다. **이것은 "권한이 없다"가 아니라 "확인 수단이 없다"** 를 가리키는 전용 값이다.
> 볼트 [[검사가능성-공사]] 는 09-17에 [[security-audit-skill]] `needs_validation` · [[oh-my-hermes]] `Code · reported done` 두 생태계의 수렴을 기록했고, **09-20 actionable "볼트 판정값 3값화 — `⬜ 미검증` 칸 신설"** 을 등록했다. 그 항목은 **아직 `상태: 대기`** 다.
> 🔴 **4일 만에 세 번째 독립 생태계가 같은 칸을 만들었고, 볼트는 아직 안 만들었다.** 규칙의 존재와 적용은 별개라는 09-23 자기비판이 여기서 그대로 반복된다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ★1,621(당일 +107)은 낮지만 README 487행이 명령 수·실패 모드·권한 상태·플랫폼 표를 **전부 값으로** 적었고 Apache-2.0이다. 규모는 작고 문서 규율은 상급. **medium~high 경계 → high 부여**(근거: 검증 가능한 진술 밀도).
- **즉시 활용**: 🔴 **NO — 플랫폼 제약** (macOS 13.0+ 전용, Windows/Linux `Planned`). 내 환경에서 실행 불가.
- **6개월 영향력**: 중간 — 접근성 트리 경로가 픽셀 경로보다 안정적이라는 주장은 설득력 있으나, macOS 단일 플랫폼이면 채택 상한이 낮다. Windows `Planned` 가 실현되면 재평가.
- **대체 관계**: 스크린샷 기반 컴퓨터 유즈를 대체하는 방향. 웹은 [[agent-browser]] 에 넘기고 **네이티브 UI만 담당**하는 분업을 스스로 선언(239행).
- **허와 실**: 실 = 58/54 · 3값 권한 · 6언어 FFI · fail-closed. 허 = **78–96% 의 측정 방법이 없고**, 유일한 구체 예시는 alt 속성 안에 있으며 그 값(98.75%)은 헤드라인 범위 밖이다. 단일 앱(Slack) 1회 관측.
- **액션**: macOS 확보 시 `snapshot` vs `skeleton` 토큰 수 **직접 재측정**(저자 예시 30,743→383 재현 여부). 지금은 **보류**.

## 관련 페이지
- [[lahfir]] — 제작자
- [[agent-browser]] — 짝 레포(이 페이지가 선호 지목)
- [[nasiko]] — 같은 배치 Rust 3종
- [[검사가능성-공사]] — `unknown` 3값 수렴 3번째 사례
- [[자기제한-명시]] — 54/58 fail-closed
- [[한정어-탈락]] — `Planned` → *"불가"*
- [[PageIndex]] — "그림 안에만" 선행 사례
- [[Electron-CDP-브리지]] · [[에이전트-웹접근]]
- [[ai-news]]

## 원본
- 출처: https://github.com/lahfir/agent-desktop
- 확인 범위: **README 487행 전문** · GitHub API 실측 · `docs/faq.md`·`docs/architecture.png` **미열람**
- 신뢰도: ⭐⭐⭐ (★1,621 · Apache-2.0 · 진술 검증 가능성 높음)
