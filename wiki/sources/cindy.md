---
title: "cindy — Claude Code·Codex 하네스를 한 클라이언트에서 갈아끼우는 데스크톱 에이전트. 🔴 '로컬 실행'이지만 기본 서버는 Cindy 클라우드"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-client, harness, electron, mcp, telemetry, coding-plan, 신생레포]
created: 2026-10-25
updated: 2026-10-27
sources: []
reliability: low
---

# cindy

**GitHub**: https://github.com/makecindy/cindy
**실측(2026-10-25 KST)**: ★ **4,338**(수집기 4,336 · +2) · Apache-2.0 · TypeScript · created **2026-07-22**(3개월) · pushed 10-25(당일) · +477★ today(트렌딩 daily 10위)
**신뢰도**: ⭐⭐ (신생 · 유료 호스티드 서비스와 결합 · 수치 주장 없음)

> [!insight] 핵심 인사이트 — **하네스가 교체 가능한 부품이 됐다 — 그리고 그 교체 레이어를 쥐는 쪽이 수익 모델을 갖는다**
> README: 작업 도중 하네스×모델 전환, *"your workspace, memory, skills and tools"* 공유 · *"authorize the **Claude Code / Codex Coding Plan** you already"* have.
> 🎯 [[하네스-설계-축]]에서 하네스는 점수를 바꾸는 변수였다(예: [[DeepSeek-V4.1-Flash-1017]] TB 4.0 하네스 교체 의심). **cindy 는 그 변수를 사용자 UI 의 드롭다운으로 내렸다.** 메모리·스킬이 하네스 밖(클라이언트)에 있으므로 하네스는 상품이 되고 클라이언트가 락인 지점이 된다.

> [!warning] 🔴 "로컬 실행" 의 범위 한정
> README 원문: *"**About the default servers:** the client connects to Cindy's official cloud"* · *"Privacy & telemetry … in to a cloud account the client sends an online heartbeat to Cindy services"* · 표 항목 *"Hosted service | Cindy cloud account | … See pricing"*.
> ⇒ **클라이언트 코드는 오픈(Apache-2.0)·로컬 실행이지만 기본 연결·원격 개발·호스티드 기능은 Cindy 클라우드 경유.** 수집기 요약 *"로컬 실행 AI 에이전트 클라이언트"* 는 **한정어 탈락** → [[한정어-탈락]].

## 도메인별 추출 (ai-news)
- **신뢰도**: ★4,338 · 3개월 · 벤치 없음
- **즉시 활용**: **NO** — 볼트는 단일 하네스(Claude Code)로 충분, 텔레메트리·클라우드 기본값 검토 부담
- **6개월 영향력**: 중간 — "하네스 멀티플렉서" 범주가 생기면 메모리·스킬 포맷 표준화 압력
- **대체 관계**: [[9router]](모델 라우터)보다 한 층 위(하네스 라우터)
- **허와 실**: 오픈소스 클라이언트 + 유료 서비스의 오픈코어형
- **액션**: 관찰만. 셀프호스팅 서버 지정 가능 여부는 미확인

## 관련 페이지
- [[하네스-설계-축]] · [[에이전트-메모리-레이어]] · [[에이전트-스킬]] · [[Claude-Code-워크플로우]] · [[한정어-탈락]]
- 같은 배치: [[freellmapi]](모델 층 라우터) · [[claude-howto]] · [[gemini-cli]]
- [[9router]] · [[ai-news]]

## 원본
- 출처: https://github.com/makecindy/cindy
- 신뢰도: ⭐⭐ (GitHub 스타 4,338 · 신생)

## 🔄 2026-10-27 갱신 (인제스트 2026-10-27) — **2일 만에 ★ +2,656. 🔴 열린 이슈 2,066 = ★ 의 29.5%**

**GitHub API 실측(2026-10-27T09:05Z)**: ★ **6,994**(수집기 6,989 · +5) · fork 841 · 🔴 **open issues 2,066** · Apache-2.0 · TypeScript · pushed 10-27(당일)
- 10-25 ★4,338 → **+2,656 / 2일** · 금일 +1,296(수집기) — 트렌딩 10위(10-25) → 상위 재진입.
- 🔴 **이슈/★ 29.5%** — 같은 배치 [[thinkrail]] 6.7%, [[TradingAgents]] 0.07% 대비 이례적. `open_issues_count` 는 **PR 포함**이므로 봇 PR·자동 리포트 가능성 → 분해 미실시(10-06 해소 경로: GitHub Search `is:issue`/`is:pr`).
- ✅ README 재확인: *"Cindy runs locally on your own machine"* + 로그인 표의 **"Skip Sign-In … Server-backed capabilities are unavailable"** ⇒ 10-25 볼트 판정(🔴 *'로컬 실행'이지만 기본 서버는 Cindy 클라우드*) **유지**. 수집기 금일 요약은 이 단서를 빠뜨렸다(*"로컬 권한이 넓어 보안 설정 확인 필요"* 만 언급).
- 하네스: Claude Code · Codex 지원 · *"a native harness is in the works"* — 수집기 일치.

> [!insight] 같은 배치 [[Trial-by-Trace]] 기준: Claude Code(Agent 1위)와 Codex(Harness Macro 최하 59.8 · Clean 2.8%)는 **하네스 신뢰성 격차가 12%p** 다. cindy 의 가치 제안(*"작업 도중 하네스를 바꿔도 메모리·스킬 유지"*)은 **하네스 선택이 결과를 바꾼다는 실측**을 얻었다 — 단 교체 시 신뢰도도 같이 바뀐다.
