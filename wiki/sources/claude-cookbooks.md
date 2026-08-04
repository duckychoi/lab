---
title: claude-cookbooks — Anthropic 공식 Claude API 실전 레시피 모음
type: source
domain: ai-news
tags: [ai-news, github-trending, claude, anthropic, api, rag, tool-use, prompt-caching, cookbook]
created: 2026-07-12
updated: 2026-07-26
sources: []
reliability: high
---

# anthropics/claude-cookbooks (GitHub ⭐50,007)

> [!update] 2026-07-26 갱신 — 5만 돌파 (WebFetch 실검증)
> ⭐**50,007** (2026-07-26 WebFetch 실검증) ← ⭐48,650 (07-13). 2주 새 +1,357로 **5만 스타 돌파**, Jupyter Notebook 유지. [[Anthropic]]의 모델→[[Claude-Code-워크플로우|Claude Code]]→Agent Skills→cookbooks 풀스택 에이전트 레이어에서 *실제 API 구현 원본*으로 계속 우상향. reliability high 유지(벤더 1차 공식 자료).

> [!insight] 핵심 인사이트
> [[Anthropic]] 공식 **Claude API 실사용 패턴 노트북 모음** — 복붙 가능한 코드로 실무 레시피를 제공한다. ⭐48,650(2026-07-13, 당일 +459; 하루 유입이 +219→+459로 배증하며 우상향 가속, Jupyter 94.3%). 커버리지가 넓다: **분류·[[RAG]]·요약(Capabilities), 툴 use·함수호출·고객서비스 에이전트·SQL(Tool Use), Pinecone/Wikipedia/Voyage 임베딩(3rd-party), 비전·차트해석·폼추출(Multimodal), 서브에이전트(Haiku+Opus)·PDF파싱·자동평가·JSON모드·콘텐츠 모더레이션·prompt caching(Advanced)**. 이론이 아니라 "지금 붙여 쓰는 코드"라, 위키의 Claude/에이전트 스킬 계보([[stitch-skills]]·[[agent-skills]])에서 *실제 API 호출 레이어*를 채워주는 레퍼런스 상수.

**GitHub**: https://github.com/anthropics/claude-cookbooks
**스타**: ⭐50,007 (2026-07-26 WebFetch 실검증) ← ⭐48,650 (07-13) ← ⭐48,084 (07-12)
**신뢰도**: ⭐⭐⭐⭐⭐ (Anthropic 공식·5.0만 스타·MIT)

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — [[Anthropic]] 공식 레포·4.8만 스타·MIT. 벤더 1차 자료라 정확도·지속성 최상.
- **즉시 활용**: YES — prompt caching·서브에이전트(Haiku+Opus)·툴 use·자동평가 레시피는 내 스케줄/에이전트 워크플로우에 바로 이식 가능. 특히 **prompt caching**은 반복 시스템 프롬프트 비용 절감에 직결.
- **6개월 영향력**: 스킬 생태계가 "무엇을 하나"라면 cookbooks는 "**어떻게 API로 구현하나**" — [[Claude-Code-워크플로우]]·[[stitch-skills]]의 하부 구현 참조로 정착.
- **대체 관계**: 커뮤니티 큐레이션([[awesome-claude-code]])이 "고르는 지도"라면 cookbooks는 "**공식 구현 원본**". 상보 관계.
- **허와 실**: 마케팅 없음 — 공식 예제라 과장 리스크 낮음. 다만 예제 수준이라 프로덕션 안정화·비용 최적화는 별도 작업 필요.
- **액션**: prompt caching·자동평가(evals) 노트북을 떼어 내 반복 태스크에 적용해 토큰비 절감 실측.

> [!action] 당장 할 것
> claude-cookbooks의 **prompt caching + 서브에이전트(Haiku+Opus) + 자동평가** 레시피를 위키 자동수집 파이프에 이식해, 반복 시스템 프롬프트 비용과 인제스트 품질 평가를 코드로 표준화.

## 관련 페이지
- [[Anthropic]]
- [[Claude-Code-워크플로우]]
- [[stitch-skills]]
- [[agent-skills]]
- [[awesome-claude-code]]
- [[ai-news]]

## 원본
- 출처: https://github.com/anthropics/claude-cookbooks
- 스타: ⭐50,007 (2026-07-26 WebFetch 실검증) ← ⭐48,650 (07-13) ← ⭐48,084 (07-12), MIT, Jupyter Notebook
- 제작: Anthropic 공식 (구 anthropic-cookbook)
- 신뢰도: ⭐⭐⭐⭐⭐ (벤더 1차 공식 자료, README 실측)
