---
title: vercel-labs/skills — AI 에이전트용 오픈 스킬 레지스트리
type: source
domain: ai-news
tags: [ai-news, vercel, agent-skill, registry, npx, open-agents, package-manager, duplicate-catch]
created: 2026-04-23
updated: 2026-09-11
sources: []
reliability: high
---

# vercel-labs/skills

> [!insight] 핵심 인사이트
> Vercel Labs가 공식 출시한 AI 에이전트용 범용 스킬 레지스트리. npx 한 줄로 설치. [[awesome-agent-skills]]와 함께 "스킬 마켓플레이스" 생태계의 두 핵심 축.

**GitHub**: https://github.com/vercel-labs/skills  
**스타**: ⭐15,695 (+333 오늘)  
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출

- **신뢰도**: Vercel 공식 Labs 출시 + 15K 스타 — 높은 신뢰도
- **즉시 활용**: `npx @vercel/skills` 로 에이전트 스킬 설치·실행
- **6개월 영향력**: 에이전트 스킬 표준화 주도. Next.js 생태계와 자연스러운 연결
- **대체 관계**: [[awesome-agent-skills]](17K⭐, 커뮤니티 큐레이션) vs vercel-skills(공식 레지스트리) — 상보적
- **대형 플랫폼 진입**: Vercel의 공식 에이전트 인프라 포지셔닝 신호

> [!insight] 인사이트
> Vercel이 에이전트 스킬 레지스트리를 직접 운영한다는 것은 "프론트엔드 플랫폼 → 에이전트 플랫폼"으로의 전환 신호. [[open-agents-vercel]]과 함께 Vercel의 에이전트 생태계 야망 확인.

## 관련 페이지
- [[open-agents-vercel]]
- [[awesome-agent-skills]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/vercel-labs/skills

---

## 🔄 2026-09-11 갱신 — **4.5개월 만에 스타 2배, 그리고 성격이 바뀌었다**

> [!warning] 🔴 볼트 중복 탐지 — raw가 "중복 0건"이라고 했으나 **이 페이지가 이미 있었다**
> 2026-09-11 배치에서 raw는 `vercel-labs/skills` 를 **신규 소스**로 올리며 *"raw.md 기존 URL과의 **중복 0건**"* 이라고 보고했다. **틀렸다.** 이 페이지는 **2026-04-23에 이미 생성**돼 있었다(⭐15,695 기록).
> → raw의 중복 검사는 **`raw.md` 의 기존 URL** 과만 대조한다. 그런데 `raw.md` 는 **처리 후 항목을 즉시 삭제**하는 대기열이다 — **처리된 것은 raw.md에 남아 있지 않다.**
> → 🎯 **구조적 결함이다.** raw는 원리상 **이미 인제스트된 소스를 절대 탐지할 수 없다.** 대조 대상이 틀렸다(대기열이 아니라 `wiki/sources/` 와 `index.md` 를 봐야 한다).
> → [[요약자와-판정자-분리]] 에 **새 유형 추가**: 지금까지 raw 오류는 **판정 단계**(과장·누락·역전)였는데, 이건 **탐지 단계**의 오류다. 그리고 **볼트가 안 잡았으면 1,001번째 소스로 중복 생성될 뻔했다.**

> [!insight] 무엇이 달라졌나 — 레지스트리에서 **패키지 매니저**로
> 2026-04-23 기록은 *"npx 한 줄로 설치하는 스킬 레지스트리"* 였다. 2026-09-11 현재 **설치 이외의 동사가 생겼다**:
> - **`npx skills use <source>`** — *"Use one skill **without installing**"*(README 137행). 스킬 파일을 임시 디렉터리에 쓰고 **생성된 프롬프트만 stdout으로 출력**한다(26행).
>   - 예: `npx skills use vercel-labs/agent-skills@web-design-guidelines | claude` (22행) — **파이프로 넘긴다.**
> - **`--agent` 지정 시 지원 에이전트를 프롬프트와 함께 대화형으로 기동**(26행)
> - `skills add` / `skills remove` + `--agent '*'` / `--skill '*'` **와일드카드**(109·238·250행)
> → 🎯 **설치 → 사용 → 제거의 생애주기와 와일드카드 대상 지정**이 생겼다. 이건 레지스트리가 아니라 **패키지 매니저의 문법**이다.
> → 볼트 [[에이전트-스킬]] 계보에서 **"포맷 → 묶음 → 버전관리"** 다음 칸: **의존성 관리 도구화**.

> [!note] 📊 실측 수치 (2026-09-11)
> - ⭐**31,337** (2026-04-23 기록 15,695 → **+15,642, 약 2.0배**) · 당일 **+122**
> - fork **2,672** · **MIT** · TypeScript · created 2026-01-14 · pushed 2026-09-08

> [!warning] ⚠️ 지원 에이전트 수 — **README가 자기 자신과 1 어긋난다**
> raw는 *"총 **79개** 에이전트 지원(README 자동생성 목록)"* 이라 적었다. 볼트 실측:
> - README **5~7행**(자동생성 마커 `agent-list:start`): *"Supports **OpenCode**, **Claude Code**, **Codex**, **Cursor**, and **[75 more]**"* → **4 + 75 = 79**
> - README **269행~**(자동생성 마커 `supported-agents:start`)의 표: **69행**, `--agent` 식별자 실카운트 **78개**
>   (다중 식별자 행 3개: `Amp/Replit/Universal`=3 · `Cline/Dexto/Kimi Code CLI/Loaf/Sarvam Code/Warp/Zed`=7 · `Zencoder/Zenflow`=2 → 66 + 12 = **78**)
> → **같은 README의 두 자동생성 블록이 79와 78로 다르다.** 볼트는 **어느 쪽이 맞는지 판정하지 못했다** — 생성 스크립트를 읽지 않고는 알 수 없다.
> → 🎯 raw는 **산문 요약(79)** 을 인용했다. 그건 표에서 파생된 표기다 → [[파생표기-함정]] 의 사례가 하나 더 늘었다. **다만 이번엔 원문(표)도 자동생성이라 "원문이 무엇인가"가 애매하다** — 함정의 새 변종.
> → **인용 시 "README 자기보고 79 / 표 실카운트 78"로 병기할 것.**

> [!action] 2026-09-11 갱신 액션
> **`npx skills use` 를 이 볼트 워크플로우에 실험.** 설치 없이 프롬프트만 뽑아 파이프로 넘기는 방식은 **스킬을 영구 설치하지 않고 1회성으로 쓰는** 경로다. 내 `~/.claude/skills/` 가 비대해지는 것을 막는 실질적 대안.

## 관련 페이지 (2026-09-11 추가)
- [[에이전트-스킬]]
- [[요약자와-판정자-분리]]
- [[파생표기-함정]]
- [[Vercel]]
- [[i-have-adhd]]
- [[llm_wiki]]
- [[단위-불일치]]

## 원본 (2026-09-11 실측)
- 출처: https://github.com/vercel-labs/skills
- GitHub API 실호출: ⭐**31,337**(raw 31,330→31,332, 드리프트 +5~7) · fork **2,672**(일치) · **MIT**(일치) · TypeScript · created **2026-01-14** · pushed 2026-09-08
- **README 원문 대조**: 22·23·26행 `skills use`/`--agent` **원문 확인** · 137행 "without installing" 확인 · 109·238·250행 와일드카드 확인 · 5~7행 "79" vs 269행~ 표 78 **불일치 실측**
- **🔴 볼트 중복 탐지**: raw "중복 0건" → **실제 중복 1건**(이 페이지, 2026-04-23 생성). 신규 페이지 생성 대신 **본 페이지 갱신으로 처리**
- 신뢰도: ⭐⭐⭐⭐ (Vercel 공식 · API 실측 · README 원문 대조 / 에이전트 수만 자기모순 미해소)
