---
title: graphify — 코드베이스를 쿼리 가능한 지식 그래프로
type: source
domain: ai-news
tags: [ai-news, github-trending, knowledge-graph, codebase, tree-sitter, agent-skill, mit]
created: 2026-07-10
updated: 2026-07-17
sources: []
reliability: high
---

# Graphify-Labs/graphify (GitHub ⭐89,575)

**GitHub**: https://github.com/Graphify-Labs/graphify
**스타수**: 89,575 (2026-07-17 기준, 당일 +1,107) ← 85,376 (07-14) ← 81,529 (07-10) · **라이선스**: MIT · **스택**: Python 100%
**설치**: `uv tool install graphifyy` → `graphify install` → IDE에서 `/graphify .`

> [!note] 2026-07-17 갱신
> 스타 85,376→**89,575**(3일 +4,199, 당일 +1,107)로 9만 목전. 하루 +1,100대 유입이 열흘째 안정적으로 유지되는 트렌딩 앵커 — 코드베이스 지식그래프화가 반짝 관심이 아니라 지속 카테고리임을 재확인. 내 [[LLM-Wiki]] 그래프 워크플로우의 코드판이라는 위상 그대로.

> [!note] 2026-07-14 갱신
> 스타 81,529→85,376(4일 +3,847, 당일 +1,095)로 우상향 지속. 코드베이스 지식그래프화 도구의 트렌딩 앵커 유지.

> [!insight] 핵심 인사이트
> **코드베이스·문서·PDF·이미지·영상을 상호 연결된 지식 그래프로 변환하는 AI 코딩 어시스턴트 스킬.** WebFetch 실측: [[Claude-Code-워크플로우|Claude Code]]·Cursor·Codex·Gemini CLI 등 **15+ 어시스턴트**와 연동되며, ①코드는 **tree-sitter AST로 로컬 파싱**(LLM 호출 없이 완전 프라이빗)해 ~40개 언어 지원, ②산출물 3종(인터랙티브 `graph.html` + `GRAPH_REPORT.md` + `graph.json`), ③`/graphify query`·`path`·`explain` 명령으로 질의, ④**코드 커뮤니티 탐지 + "god node"(가장 많이 연결된 핵심)** 하이라이트, ⑤관계 신뢰도를 EXTRACTED/INFERRED/AMBIGUOUS로 태깅. 이것은 사실상 **이 위키가 소스에 대해 하는 일(지식 그래프화)을 코드베이스에 대해 제품화**한 것 — 내 [[LLM-Wiki]] 그래프 워크플로우와 철학이 정확히 겹치고, [[codebase-memory-mcp]]의 상위 호환 후보.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (⭐81,529 당일 +909, MIT, README WebFetch 실측 — tree-sitter 로컬 파싱·3산출물·신뢰도 태깅 확인)
- **즉시 활용**: YES(후보) — Claude Code 스킬로 등록해 내 스킬 저장소(reat-*/pixl-*/obsi-* 등)에 `/graphify .`를 돌리면 스킬 간 의존·중복을 그래프로 가시화 가능. 위키의 wikilink 그래프 개념을 코드로 확장.
- **6개월 영향력**: "코드 이해 = 벡터 임베딩 검색"에서 "코드 이해 = **탐색 가능한 그래프**"로 이동. AI 코딩 어시스턴트가 파일 나열 대신 구조를 질의하는 표준.
- **대체 관계**: [[codebase-memory-mcp]](코드베이스 지식 그래프 MCP)의 직접 경쟁·상위 호환. 벡터 RAG형 코드 검색([[zvec]] 등) 대비 "관계 기반" 접근.
- **허와 실**: "지식 그래프"는 정확하나 tree-sitter AST 기반이라 **정적 구조**에 강하고 런타임/의미 추론은 태깅(INFERRED/AMBIGUOUS)에 의존 — 신뢰도 태그를 반드시 확인해야 함.
- **액션**: 내 스킬 디렉터리에 graphify 설치 → `graph.html`로 스킬 의존도·god node 확인, 위키 그래프 HTML과 비교.

## 관련 페이지
- [[LLM-Wiki]] — 소스 지식 그래프화 = graphify의 코드판 대응
- [[codebase-memory-mcp]] — 코드베이스 지식 그래프 MCP (직접 경쟁)
- [[Ideas-Have-Genomes]] — 같은 배치 "아이디어 계보 그래프" 논문과 그래프-사고 공명
- [[Claude-Code-워크플로우]] — 연동 대상 어시스턴트
- [[ai-news]]

## 원본
- 출처: https://github.com/Graphify-Labs/graphify
- GitHub: ⭐89,575 (2026-07-17, 당일 +1,107) ← 85,376 (07-14) ← 81,529 (07-10, 당일 +909), MIT, Python 100%
- 신뢰도: ⭐⭐⭐ (라이브 스타·README WebFetch 실측. 07-14 이후 갱신은 raw 자동수집 수치)
