---
title: "agent-browser — Vercel Labs 브라우저 자동화 CLI (★ 둔화 중 월 npm 532만)"
type: source
domain: ai-news
tags: [ai-news, github-trending, browser-automation, rust, agent-web, vercel, cdp, observability, tool]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: high
---

# vercel-labs/agent-browser — 에이전트용 네이티브 Rust 브라우저 CLI

**GitHub**: https://github.com/vercel-labs/agent-browser
**스타수**: ⭐**43,140** (2026-09-24 볼트 실측 · 수집기 43,138 → 드리프트 **+2** · 당일 **+62**) · forks 2,896 · open issues **813**
**언어**: Rust · Apache-2.0 · **created** 2026-01-11 · **pushed** 2026-09-23
**npm**: `agent-browser` v0.38.1 · **버전 127개** · **월 다운로드 5,326,951**(2026-08-23~09-21 실측)

> [!insight] 🎯 핵심 인사이트 — **★ 증분이 둔화한 레포가 월 530만 번 설치된다**
> 수집기는 *"9개월도 안 된 레포에 ★43k인데 당일 증가는 +62로 **둔화**"* 라고 썼다. 볼트가 npm을 조회하니 **월 다운로드 5,326,951**이다. 🔴 **★ 증분으로 채택을 읽으면 정확히 거꾸로 읽는다** — ★는 *발견*의 속도를 세고 npm DL은 *사용*의 양을 센다. ★가 43k에서 포화하는 동안 설치는 초당 2회씩 일어난다.
> 📌 이것은 [[원본-파생-역전]] 의 GitHub 판이다: 거기서는 *다운로드는 파일을, 좋아요는 정체를 센다* 였고, 여기서는 **npm DL은 사용을, ★는 인지를 센다.** 정렬 키를 바꾸면 순위가 바뀐다 → [[상대속도-가림]]

> [!note] 확인 범위 (볼트 실측)
> **README 2,036행 전문 확보 후 구조·핵심 섹션 열람**(수집기는 상단 45행만). GitHub API 실측. **npm registry + downloads API 실측**(수집기 미조회). 🔴 **코드 미실행** — CLI 미설치, 브라우저 미구동.

## 실제 능력 — README 섹션 구조(28개 `##`)로 확인

수집기는 *"실제 명령 체계·능력은 **미확인**"* 이라 유보했다. 전문 구조를 열어 확인한 결과:

- **세션 계층**: `Sessions`(720) · `Chrome Profile Reuse`(781) · `Persistent Profiles`(803) · `Session Persistence`(828) — 프로필 재사용과 세션 지속이 **네 개 섹션으로 분리**돼 있다. 로그인 상태 유지가 일급 관심사다.
- **인증**: `Authentication`(653) · `Authenticated Sessions`(1387)
- **에이전트 전용**: `Agent Mode`(1297) · `Selectors`(1245) · `Snapshot Options`(980) · `Annotated Screenshots`(1010) — ref 기반 워크플로
- **🎯 `Observability Dashboard`(1095)**: `agent-browser dashboard start` — 포트 4848 로컬 웹 대시보드에 **라이브 뷰포트 + 명령 활동 피드**. 모든 세션이 자동 표출.
- **연동**: `CDP Mode`(1511) · `Streaming (Browser Preview)`(1570) · `Integrations`(1767~2034, **267행**)
- **설치 4경로**: npm 글로벌/프로젝트 · Homebrew · cargo. `agent-browser install` 이 **Chrome for Testing 을 직접 내려받는다**(시스템 Chrome 의존 없음).

### 플랫폼 — 5종 전부 네이티브 Rust (README 1708행 표)
macOS ARM64 · macOS x64 · Linux ARM64 · Linux x64 · Windows x64 — **전부 `Native Rust`**, `Planned` 칸 없음.
🎯 **같은 배치 [[agent-desktop]] 과 정반대다**: agent-desktop은 7개 기능 전부 macOS만 `Yes`, Windows·Linux는 `Planned`.

> [!insight] 🎯 같은 배치의 두 레포가 서로를 지목한다 — 그리고 방향이 일방적이다
> [[agent-desktop]] README **239행**이 CDP로 Chromium 앱을 넘길 때 **agent-browser 를 명시적으로 선호**한다고 적는다: *"with **agent-browser preferred** for its ref-based agent workflow and bundled `electron` skill."* agent-browser 쪽 README에는 agent-desktop 언급이 없다(전문 확보 후 확인).
> → **★1,621 짜리가 ★43,140 짜리를 권하는 단방향 참조.** 같은 트렌딩 목록에 함께 오른 두 레포가 **경쟁이 아니라 계층 분업**(네이티브 UI = agent-desktop · 웹 콘텐츠 = agent-browser)을 이미 합의해 둔 상태다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ★43,140 · Apache-2.0 · **Vercel Labs 공식 제품 배지** · npm 127버전·월 532만 DL. 볼트 GitHub 소스 중 **npm 실채택 수치가 가장 큰 건**. high.
- **즉시 활용**: **YES** — 단일 바이너리 + `npm i -g` 로 즉시 설치 가능하고 Chrome을 스스로 받아온다. 볼트 [[browser-use]]·[[에이전트-웹접근]] 축의 현실적 대체·보완 후보. **로컬 대시보드(4848)** 가 있어 에이전트 브라우저 행동을 눈으로 볼 수 있다.
- **6개월 영향력**: 높음 — Vercel이 Labs 제품으로 밀고 npm 채택이 이미 월 500만대다. 에이전트 웹접근의 **기본 CLI**가 될 궤도.
- **대체 관계**: Playwright/Puppeteer를 대체하지 않고 **그 위에 에이전트 규약(ref·snapshot·agent mode)을 얹는다**. CDP를 그대로 노출하므로 기존 도구와 공존.
- **허와 실**: 실 = 5플랫폼 네이티브·npm 532만·대시보드 내장. 허 = **open issues 813건 = ★ 대비 1.9%** 로 같은 배치 최고 비율([[agent-desktop]] 1.2% · [[nasiko]] 0.7%). 9개월 레포에 813건은 표면적이 빠르게 넓어졌다는 뜻이기도 하다.
- **액션**: `npm i -g agent-browser` 설치 후 대시보드 1회 구동 — **볼트 코드 실행 0건을 깨기에 가장 비용이 낮은 후보**(설치 1줄, 외부 스택 0). ★최우선 등록.

> [!warning] ⚠️ 유보 사항
> - 🔴 **명령 체계 세부는 여전히 미열람** — `Commands` 섹션이 **113~653행(540행)** 이다. 섹션 존재와 범위만 확인했고 개별 명령 목록은 안 봤다.
> - ⬜ **월 532만 DL의 구성 미확인** — CI 재설치·미러가 얼마인지 npm API로는 분리 불가. [[상대속도-가림]] 의 경고가 npm 에도 적용된다.
> - ⬜ `Integrations` 267행 미열람 — 어떤 프레임워크와 붙는지 목록 미확인.

## 관련 페이지
- [[vercel-labs]] — 제작 조직
- [[agent-desktop]] — 짝 레포(agent-desktop이 이쪽을 선호 지목)
- [[nasiko]] — 같은 배치 Rust 3종
- [[browser-use]] — 같은 축 기존 앵커
- [[에이전트-웹접근]] · [[상대속도-가림]] · [[에이전트축-분기]]
- [[ai-news]]

## 원본
- 출처: https://github.com/vercel-labs/agent-browser
- 확인 범위: **README 2,036행 확보 + 섹션 구조 28개·핵심 6섹션 열람**(`Commands` 540행 미열람) · GitHub API 실측 · **npm registry·downloads API 실측**
- 신뢰도: ⭐⭐⭐ (★43,140 · Apache-2.0 · Vercel Labs 공식 · npm 월 532만)
