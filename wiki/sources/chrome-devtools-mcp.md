---
title: ChromeDevTools/chrome-devtools-mcp
type: source
domain: ai-news
tags: [ai-news, mcp, chrome, devtools, browser-automation, debug]
created: 2026-04-18
updated: 2026-11-16
sources: []
reliability: high
---

# ChromeDevTools/chrome-devtools-mcp

> [!update] 2026-09-03 갱신 — ⭐**50,774**(5만 돌파) · **배치 최저 부채 밀도 0.0261**
> **지표(2026-09-03 GitHub API 실호출)**: ⭐**50,774** · 포크 **3,560** · 이슈 **93** · 워치 **253** · TypeScript · **Apache-2.0** · 생성 **2025-09-11** · **당일 푸시**(2026-09-03T07:02Z) · 트렌딩 **6위**(raw 기준 당일 +148) — raw 표기 50,772 대비 **+2 드리프트**(배치 최소)
> **34일간(07-31→09-03) +2,563(+5.32%·일평균 +75).** 07-05→07-31 구간의 +304/일에서 **4분의 1로 감속**했으나, **5만 스타 돌파**와 **당일 푸시 유지**로 표준 지위는 흔들리지 않는다. 벤더 공식 도구의 전형적 곡선 — 폭발 없이 꾸준하다.
> 📌 **부채 밀도 0.0261건/포크 — 이번 배치 GitHub 5건 중 2위로 낮다**([[VoiceStudio]] 0.0056 < **본 레포 0.0261** < [[ponytail]] 0.0305 < [[TimesFM]] 0.0812 < [[hermes-agent]] **0.786**). raw가 *"배치에서 가장 낮은 부채 밀도"* 로 기록했으나 **[[VoiceStudio]]가 더 낮다 — raw 주장 정정.**
> ⚠️ 다만 **VoiceStudio는 Discord로 문제 보고가 흡수될 수 있고 워치도 73으로 낮다.** 본 레포는 **워치 253 + 당일 푸시 + 이슈 93**이라는 조합이라, **낮은 이슈 수가 "안 쓰인다"가 아니라 "빨리 닫힌다"에 가깝다**고 읽을 근거가 더 있다. **⚠️ 닫힘 속도를 직접 측정하지는 않았다.**
> 📌 **같은 배치에 MCP 서버가 둘**이다 — 본 레포(브라우저 제어)와 [[VoiceStudio]](음성 생성). **에이전트가 붙는 주변장치가 늘어나는 방향**이며, 내 lightpanda 자동화와 [[reat-voice]] 파이프라인이 각각 대응한다.
> **reliability high 유지** — 벤더 공식 + 지표 실검증. ⚠️ 단 **커버리지(어떤 CDP 기능이 노출되는가)는 07-31 이후 여전히 미확인**이다.

> [!update] 2026-07-31 갱신 — ⭐48,211 (WebFetch "48.2k"·Apache-2.0 실확인)
> GitHub 스타 **48,211**(2026-07-31 자동수집, 당일 +80) ← 45,886(07-05). 약 4주간 +2.3k 완만 성장으로 공식 MCP의 표준 지위 굳힘. **WebFetch 재확인: 48.2k·TypeScript·Apache-2.0**(기존 페이지에 라이선스 미표기였음 — 이번에 확정), CDP를 MCP로 노출해 코딩 에이전트가 라이브 Chrome을 제어·검사한다는 성격 동일. 내 lightpanda 브라우저 자동화와 같은 축의 공식 레퍼런스.

> [!insight] 핵심 인사이트
> Chrome DevTools 공식팀이 직접 MCP 서버를 만들었다 — 브라우저 디버깅이 LLM 에이전트의 1급 도구로 편입되는 시점. Claude Code 등 코딩 에이전트가 브라우저를 직접 열어 콘솔 오류 확인·DOM 조작·네트워크 탭 분석까지 수행 가능.

## 도메인별 추출

**즉시 활용**: YES — [[Claude-Code-워크플로우]]에서 웹 디버깅 자동화에 바로 통합 가능
**신뢰도**: ⭐⭐⭐⭐⭐ (Chrome DevTools 공식 레포, ⭐45,886 / +304/일, 2026-07-05) ← ⭐35,992 (2026-04-18)
**6개월 영향력**: 코딩 에이전트가 "실행-디버그-수정" 루프를 브라우저 수준에서 닫을 수 있게 됨 → 수동 브라우저 디버깅 감소
**대체 관계**: Playwright MCP, Puppeteer 대비 DevTools 프로토콜 직접 접근으로 더 낮은 레벨 제어

## 주요 기능

- MCP 서버로 Chrome DevTools Protocol 노출
- 코딩 에이전트가 자연어로 브라우저 제어·디버깅 수행
- 콘솔 오류, 네트워크 요청, DOM 상태를 LLM이 직접 읽고 수정
- 공식 Chrome DevTools 팀 개발 → 장기 지원 기대

> [!action] 당장 할 것
> 설치 후 Claude Code + chrome-devtools-mcp 연결 테스트. 프론트엔드 디버깅 워크플로우에 통합.

## 관련 페이지

- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]
- [[superpowers]]

## 원본

- 출처: https://github.com/ChromeDevTools/chrome-devtools-mcp
- 스타: ⭐**48,211** (2026-07-31, 당일 +80, WebFetch "48.2k"·Apache-2.0 실확인) ← ⭐45,886 (2026-07-05, +304/일) ← ⭐35,992 (2026-04-18)
- 라이선스: Apache-2.0 / TypeScript
- 신뢰도: ⭐⭐⭐⭐⭐

---

## 📊 2026-11-16 재관측 — 커버리지 질문의 답: 도구 63개, 그리고 기본 수집되는 사용 통계

★ **57,305**(볼트 11-16 09:04Z 실측 · 수집기 11-15 ★56,516) · fork 4,832 · Apache-2.0 · repo id 1054793726 · 최신 릴리스 v1.13.0(2026-11-11). 볼트 직전 기록 ★50,774 @ 09-03 → 74일간 약 +6,500.

> [!insight] 09-03 미해결 "어떤 CDP 기능이 노출되는가" → `docs/tool-reference.md` 기준 **도구 63개 · 13범주**(볼트 `###` 계수 63 확인)
> Input automation · Navigation · Emulation · Performance · Network · Debugging(`lighthouse_audit` · `get_css_styles` · screencast) · **Memory**(최대 범주, 수집기 14개) · Network mocks · Extensions · Third-party · WebMCP · PWA · WebAuthn. 볼트 기록에 없던 것(도입 시점 미확인): MCP 없는 `chrome-devtools` CLI, 스킬 7종(a11y · cookie · LCP · memory-leak · troubleshooting 등)과 Claude Code/Copilot/Gemini CLI 플러그인 경로 → [[에이전트-스킬]].

> [!warning] 🔴 기본값이 "보낸다" — 브라우저에 로그인 세션이 있으면 먼저 끌 것 (README 39 · 45행 · 볼트 확인)
> - *"Data collection is **enabled by default**"* — 도구 호출 성공률 · 지연 · 환경 정보를 Google 이 수집. `--no-usage-statistics` 또는 `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS`/`CI` 환경변수로 해제(Chrome 자체 통계 옵트아웃과 별개).
> - 성능 도구가 트레이스 URL 을 CrUX API 로 전송 → `--no-performance-crux`.
> - 브라우저 인스턴스 내용이 MCP 클라이언트에 노출 — 공식 지원은 Chrome · Chrome for Testing 뿐.

## 관련 페이지 추가
- [[에이전트-스킬]] · [[에이전트-웹접근]] · [[Electron-CDP-브리지]] · [[Google]]

## 원본 갱신
- 실측(2026-11-16 · GitHub API): ★57,305 · fork 4,832 · Apache-2.0 · pushed 2026-11-16T05:21Z
- 확인 범위: README 39 · 45 · 48행 · tool-reference.md 범주 13 · 도구 63(볼트) · 🔴 범주별 개수 · 스킬 7종 목록은 수집기 판독 · 미실행
