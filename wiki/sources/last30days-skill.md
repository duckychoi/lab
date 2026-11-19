---
title: last30days-skill — 멀티소스 자율 조사·종합 AI 에이전트 스킬
type: source
domain: ai-news
tags: [ai-news, agent-skill, social-media, research, reddit, youtube, hn]
created: 2026-04-23
updated: 2026-11-19
sources: []
reliability: high
---

# mvanhorn/last30days-skill

> [!update] 2026-11-19 갱신 — ⭐70,378 (당일 +1,059 · 07-31 대비 +14,603) · v4.3.2
> ⭐**70,378**(GitHub API 11-19 볼트 확인 · MIT · Python · HEAD 2623916 11-19T08:23Z) ← 55,775(07-31). **릴리스(볼트 API 확인)**: v4.2.1(11-16) → **v4.3.0(11-16 23:57Z)** → v4.3.1 → **v4.3.2(11-17)** — 이틀에 4개. v4.3.0 변경(수집기 판독): Polymarket 엔티티 주제 우선 노출 · 부분 검색 결과 보고 · 회사 조사 시 채용 신호 탐지. 50+ Agent Skills 호스트(`npx skills add`).
> 🔴 **로컬 `~/.claude/skills/last-30days/SKILL.md` 는 `v2.9.5`(볼트 확인 · 5행 제목) — 상류 v4.3.2 대비 메이저 2단계 뒤처짐.** 07-28 이후 추가된 소스(TikTok · Instagram · Bluesky · arXiv 등) · v4 파이프라인 반영 여부는 업그레이드 전 diff 필요. ✅ actionable 등록.
> 📌 같은 날 [[Resolution-Hypothesis]]: engagement 가중(업보트 · 좋아요 · 베팅액) 요약도 결국 "무엇을 고를지"의 점수 함수다 — 가중치가 품질 신호인지 인기 신호인지는 이 스킬이 검증하지 않는다.

> [!update] 2026-07-31 갱신 — ⭐55,775 (당일 +378, WebFetch "55.8k"·MIT 실확인)
> ⭐**55,775**(2026-07-31 자동수집, 당일 +378) ← 54,415(07-28). **WebFetch 재확인: 55.8k·Python·MIT**, 조사 소스가 Reddit·X·YouTube·HN·Polymarket·웹까지 실사용 engagement 순으로 종합한다는 성격 동일. 이 vault [[last-30days]] 스킬의 상위 레퍼런스 — arXiv 소스 편입 후보 유지.

> [!update] 2026-07-28 갱신 — ⭐54,415 (당일 +240) + 소스 대폭 확장
> ⭐**54,415**(2026-07-28, 당일 +240, WebFetch "54.4k" 일치) ← ⭐50,062(07-07). MIT·Python 유지. WebFetch 재확인: 조사 소스가 **Reddit·X·YouTube·HN·Polymarket에 더해 TikTok·Instagram·Bluesky·StockTwits·Pinterest·LinkedIn·Techmeme·arXiv·GitHub·웹**까지 확장, **engagement 순 스코어링**(업보트·조회수·예측시장 오즈), **Discovery 모드(속도 랭킹으로 신흥 토픽)**·라이브러리/피드 구독 추가. Claude Code·Grok·Cursor·Copilot·MCP 등 50+ 호스트. 이 vault [[last-30days]] 스킬의 상위 레퍼런스 — arXiv 소스 추가는 위키 자동수집 파이프라인에 직접 이식 후보.

> [!update] 2026-07-07 갱신
> ⭐50,062 (2026-07-07 자동수집; 이전 ⭐39,417 2026-06-11, 약 +10,645). MIT·Python 97%. WebFetch 실측: Reddit·X·YouTube·**TikTok·HN·Polymarket·GitHub·웹** 교차 조사, 실제 engagement 순 랭킹 + 엔티티 지능 해석(예: "OpenClaw"→정확한 repo·subreddit) + 공유용 HTML 브리프. 이 vault의 [[last-30days]] 스킬과 동일 계열 — 자동수집 소셜 레이어 실물 레퍼런스.

> [!insight] 핵심 인사이트
> Reddit·X·YouTube·HN·Polymarket 등 멀티소스를 자율 조사·종합하는 AI 에이전트 스킬. [[awesome-agent-skills]] 생태계와 직접 연결되는 실용 에이전트 스킬. 이 vault의 자동 수집 파이프라인 고도화에 직접 활용 가능.

**GitHub**: https://github.com/mvanhorn/last30days-skill  
**스타**: ⭐39,417 (2026-06-11; 이전 ⭐35,739 2026-06-09 → ⭐23,614 최초)  
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출

- **신뢰도**: ⭐39,417 (2026-06-11), 빠른 성장세 — 에이전트 스킬 수요 반영
- **즉시 활용**: Claude Code 에이전트에 직접 연결해 소셜 트렌드 자동 수집
- **6개월 영향력**: wiki raw.md 자동 수집 파이프라인의 소셜 레이어 구성 가능
- **대체 관계**: [[TrendRadar]](54K⭐) + [[worldmonitor]](51K⭐)의 소셜 미디어 특화 경량 대안
- **액션**: 이 스킬을 자동 수집 훅에 연결해 raw.md 자동 채우기 시도

## 관련 페이지
- [[TrendRadar]]
- [[worldmonitor]]
- [[awesome-agent-skills]]
- [[AI-에이전트-프레임워크]]
- [[에이전트-스킬]] · [[Resolution-Hypothesis]]

## 원본
- 출처: https://github.com/mvanhorn/last30days-skill
- 스타: ⭐**70,378** (2026-11-19, 당일 +1,059, GitHub API · v4.3.2) ← ⭐55,775 (2026-07-31, 당일 +378, WebFetch "55.8k"·MIT·Python 실확인) ← 54,415(07-28) ← 50,062(07-07) ← 39,417(06-11)
- 신뢰도: ⭐⭐⭐⭐
