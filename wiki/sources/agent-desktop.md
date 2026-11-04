---
title: "agent-desktop — 접근성 트리 기반 컴퓨터 유즈 (수치가 이미지 alt 속성에 있었다)"
type: source
domain: ai-news
tags: [ai-news, github-trending, computer-use, accessibility, rust, macos, fail-closed, 검사가능성, tool]
created: 2026-09-24
updated: 2026-11-04
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

## 🔄 2026-11-03 갱신 (인제스트 2026-11-03) — ★11,167 · **lahfir → vercel-labs 이관 · Windows/Linux 정식 지원 · 볼트가 찾은 alt 속성 수치(30,743→383)는 README에서 사라짐**

**GitHub API 실측(11-03 09시대)**: `api.github.com/repos/lahfir/agent-desktop` 가 **`vercel-labs/agent-desktop` 으로 리다이렉트**된다(created 2026-02-19 동일 = 같은 저장소의 조직 이관). ★**11,167**(수집기 11,158 · +9 드리프트) · fork **768**(수집기 764) · open_issues **133**(이슈+PR 합산) · Apache-2.0 ✅ · Rust ✅ · pushed 2026-11-03T08:54Z · description *"Computer use CLI for AI agents"* · 최신 릴리스 **v1.1.0(11-03 04:13Z)** · v1.0.2(10-30) · v1.0.1(10-28) · **v1.0.0(10-28)** · v0.11.1(10-25)
- 📈 볼트 마지막 기록 ★1,621 · fork 109 · open issues 20(09-24) → **★ +9,546(6.9배) · fork +659 · open_issues +113 / 40일.** 이 페이지는 09-24 이후 미갱신이었다 → [[캐시된-지표-신선도]].
- 🔴 **볼트 페이지 자체가 낡았다(정정)**: 
  - 소유자: 09-24 본문은 [[lahfir]] 개인 계정. v1.0.2 노트 #332 *"remove the personal funding link, badges and name references **before the org transfer**"* · #333 *"point repository links at vercel-labs/agent-desktop **after the org transfer**"* — [[vercel-labs]] 로 이관됐고 README 상단에 `LABS-PRODUCT` 배지가 붙었다. lahfir는 여전히 주 커밋자(v1.1.0 PR 다수).
  - 플랫폼: 09-24 표는 Windows/Linux **`Planned`** 였다. 현재 README `## Platform support` 표(126~135행)는 Windows 전 항목 **Yes**, Linux는 AT-SPI 기반 **조건부 Yes**(마우스 X11 `--headed` · 스크린샷 X11 창/Wayland portal · 클립보드 Wayland는 `wl-clipboard` · 알림 GNOME Shell). 즉 09-24 "즉시 활용 NO — 플랫폼 제약" 판정의 근거가 바뀌었다.
  - 명령 수: 58/54 → README 104행 **"60 command names, 56 operational commands"**. fail-closed 4개는 `key-down/key-up/mouse-down/mouse-up` 로 명시(데몬 전까지 거부) — [[자기제한-명시]] 성격은 유지.
- 🔴 **성능 수치 0건 — 이번엔 alt 속성에도 없다.** README(raw 187행·9.7KB) 의 `alt=` 4개는 전부 배지(`Vercel Labs Product`·npm version·License·npm downloads). 09-24에 볼트가 29행 `<img alt>` 에서 찾은 *"30,743 tokens vs 383 skeleton"* 과 헤드라인 *"78–96% 토큰 감소"* 는 **현 README에서 0건**(grep `30,743|383|%` · 측정 경로: `api.github.com/repos/vercel-labs/agent-desktop/readme` raw). skeleton 기능 자체는 77행 `snapshot --skeleton --app Slack -i --compact` 로 남았다. ⇒ 수집기 "성능 수치 README 0건" ✅ 정확. 단 **이전에는 있었다가 이관 정리 과정에서 빠졌다**는 이력은 수집기가 모른다.
- ✅ 수집기 서술 확인: "호출마다 별도 프로세스 · headless 시 포그라운드 활성화·합성입력 금지"(README 14행) · 프라이버시 문단(16행) · JEV helper 외부 전송(16행).
  - ⚖️ 보강(docs/faq.md 74~80행): 네이티브 CLI는 원격 모델 서비스를 요구하지 않는다. JEV helper는 **목표(goal)와 화면 설명**을 공급자에 보내며, *"value-suppression 옵션이 라벨·제목·조상 경로·목표 자체의 사적 텍스트는 지우지 않는다"* 고 스스로 적는다. 디버그 HTML은 스크린샷+접근성 데이터를 내장하고, 세션 trace는 구조화 필드를 가려도 증거 아티팩트가 남는다. — 문서가 자기 마스킹의 한계를 값으로 적은 사례 → [[검사가능성-공사]].
- ✅ v1.1.0 노트: Windows 종료 크래시(#342)·오버레이 좌표 이중 스케일링(#343)·검은 사각형 플래시(#344) 수정, Linux/Windows ref 재식별 규칙(#442), macOS Dock·메뉴바·시스템 패널 접근(#480). **사고·보안 공개 항목 0건**(v1.1.0·v1.0.2 노트 전문 확인) — 수집기 일치. 참고: v1.1.0의 "fix: remove the macOS command host"(#414), v1.0.2 "permission guide … leave no stale host"(#330)는 권한 위임 호스트 정리로 읽히나 사고 서술은 없다.

> [!insight] 개인 레포가 벤더 Labs 제품이 되면 "수치 근거"가 먼저 정리된다
> 09-24 볼트의 핵심 발견(헤드라인 78–96% · alt 속성의 98.75% 예시)이 이관 후 README에서 **둘 다 삭제**됐다. 과장 문구를 걷어낸 정리일 수도, 근거 있는 예시까지 함께 버린 것일 수도 있다(🔴 삭제 커밋·사유 미확인). 어느 쪽이든 **볼트가 인용하던 수치의 출처가 소멸**했으므로 09-24 본문의 98.75%는 "과거 README 기준"으로만 읽는다. ★는 이관 이후 7배가 됐고 측정값은 0이 됐다 → [[스타-근거-비동행]].

- **즉시 활용(재판정)**: 🟡 **조건부 가능** — Linux는 AT-SPI + GNOME/X11 조건부 지원이라 이 볼트 서버(헤드리스 GCP)에서는 그래픽 세션이 없어 여전히 실익 낮음. 설치는 npm(`agent-desktop`). 코드 미실행.
- **수집기 평가**: 수치·프라이버시·릴리스 확인 정확. 누락 = 조직 이관(v1.0.2 노트에 명시) · v1.0.0 메이저 도달(10-28) · 볼트 기존 판정(Planned·58/54·alt 수치)과의 충돌.
- 관련: [[agent-browser]](같은 vercel-labs, 문서 사이트도 `agent-browser.dev/desktop` 에 합쳐짐 — v1.0.2 #335) · [[Vercel]] · [[에이전트-웹접근]]

## 🔄 2026-11-04 갱신 (인제스트 2026-11-04) — ★13,659 · **`agent-desktop mcp` 머지(67개 도구, 미릴리스) · README 하루 만에 재작성(187→178행) · 새 릴리스 0건**

**GitHub API 실측(11-04 09시대)**: `vercel-labs/agent-desktop`(owner type **Organization** ✅) · ★**13,659**(수집기 13,652 · +7) · fork **935** · open_issues **152**(이슈+PR) · watchers 31 · Apache-2.0 ✅ · Rust · pushed 2026-11-03T23:16Z · topics에 `mcp` 추가 · 최신 릴리스 **여전히 v1.1.0(11-03 04:13Z)** — 이후 새 릴리스 0건. main은 v1.1.0보다 **5커밋 앞**(`/compare/v1.1.0...main`).
- 📈 볼트 직전 ★11,167 · fork 768 · open 133(11-03) → **★ +2,492 · fork +167 · open +19 · 릴리스 +0 / 1일.**
- ⚖️ 수집기 "+3,791 today"는 API 1일 차(+2,492)보다 크다 — 트렌딩 "today" 창과 볼트 관측 간격(약 24h)이 다르다 → [[지표-창길이]]. "금일 최대 증분"은 트렌딩 페이지 기준으로만 참.

- 🆕 **#519 `feat: agent-desktop mcp`(11-03 23:13Z merged, lahfir)** — PR 본문: 각 leaf CLI 명령을 stdio MCP 도구 하나로 노출(**67개 도구**, `desktop_snapshot`·`desktop_session_start` 등), 도구 이름·스키마를 clap 명령 트리에서 런타임 생성, 호출마다 자식 프로세스 실행. 테스트: **Linux(Xvfb·openbox·AT-SPI·GTK3 앱)에서만 실기 확인, "macOS and Windows were not run"**. README 105~113행에 이미 문서화됐지만 **npm 최신(v1.1.0)에는 없다.**
  - ⚖️ 수치 대조: README 117행 "60 command names, 56 operational" vs MCP 도구 67 — 도구는 *leaf* 명령(하위 명령 포함) 단위라 셈법이 다르다(PR 문구 기준 해석, 개별 대조 안 함).
- 📝 **README 재작성(#481 "simplify the README", 11-03 18:01Z)** — 볼트 11-03 확인(09시대, raw 187행) 이후. 현재 raw **178행·8,950B**. `## Platform support`(131~139행)가 기능별 Yes 표 → **OS별 요구사항 표**(macOS 13+ AX API · Windows 10 1809+ UI Automation · Ubuntu 24.04+ X11/Wayland AT-SPI)로 바뀌고, *"각 플랫폼 페이지가 headless로 되는 것·`--headed` 필요한 것·거부하는 것을 적는다"* 로 세부를 외부 문서(agent-browser.dev/desktop)로 넘겼다. 🔴 **볼트 11-03 기록의 "126~135행 Linux 조건부 Yes(X11 `--headed`·Wayland portal·wl-clipboard·GNOME Shell)" 행 번호와 표 형태는 현 README에 없다** — 내용 자체의 폐기 여부는 플랫폼 페이지 미열람으로 ⬜ 미확인.
- ✅ 수집기 서술 확인: 스크린샷·픽셀 매칭 없음/ref JSON/모델 내장 없음/CLI+C 라이브러리(12행) · 스냅샷·클립보드·스크린샷·디버그 산출물에 개인 데스크톱 정보 포함 경고(14행) · 3 OS(3행) · v1.1.0 = 수정 위주(11-03 볼트 확인, 사고·보안 항목 0건 유지). 성능 수치 0건 유지(`%`는 배지 URL의 `%20`뿐).
- ⬜ 수집기 "접근성 트리 빈약한 앱(게임·캔버스형) 한계 예상(미검증)" — README는 이 한계를 직접 언급하지 않는다(grep `game|canvas` 0건). 수집기 추정임을 스스로 밝혀 둔 것은 적절.

> [!insight] CLI가 MCP 서버를 겸하면 "에이전트 측 루프" 설계가 어느 하네스에도 꽂힌다
> 12행 *"The loop lives in your agent; agent-desktop has no model inside"* + #519 = Claude Code·Codex 등 MCP 하네스가 설정 한 줄(`{"command":"agent-desktop","args":["mcp"]}`)로 데스크톱 조작을 얻는다. 단 **실기 검증은 Linux 하나뿐**이라 macOS/Windows MCP 경로는 저자도 돌려 보지 않은 상태다. 이 볼트 서버는 헤드리스라 Xvfb를 띄워야 같은 조건이 된다 — 저자 테스트 조건과 동일하므로 **재현 시도 비용이 낮은 드문 경우**. → [[에이전트-웹접근]] · [[검사가능성-공사]]

- **수집기 평가**: 수치·경고·릴리스 서술 정확. 누락 = ① **MCP 서버 머지**(topics에도 반영) ② README 재작성으로 플랫폼 세부가 외부 문서로 빠짐 ③ 새 릴리스 0건(v1.1.0을 11-03 그대로 재서술).
- **즉시 활용(재판정)**: 🟡 조건부 유지. 다음 릴리스(MCP 포함) 후 Xvfb+AT-SPI로 `desktop_snapshot` 1회 호출 정도는 저비용 실험 후보. 코드 미실행.
