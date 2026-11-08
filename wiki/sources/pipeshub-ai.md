---
title: "pipeshub-ai/pipeshub-ai — 사내 50+ 앱을 권한 인식 에이전트 검색으로 묶는 셀프호스트 컨텍스트 레이어. 독립 벤치 1건(93.24) + 자체 측정 다수"
type: source
domain: local-llm
tags: [local-llm, agent-memory, rag, enterprise-search, mcp, knowledge-graph, permission-aware, self-host, github-trending, apache-2.0]
created: 2026-11-08
updated: 2026-11-08
sources: [https://github.com/pipeshub-ai/pipeshub-ai]
reliability: medium
---

**GitHub**: [pipeshub-ai/pipeshub-ai](https://github.com/pipeshub-ai/pipeshub-ai) · ★**4,045**(볼트 11-08 API · 수집기 4,035) · 포크 655 · 이슈 232 · Apache-2.0 · Python · created 2025-03-06 · pushed 2026-11-08

## 핵심 인사이트
> [!insight] RAG 의 병목은 검색 품질이 아니라 "권한"이다
> 커넥터가 Slack·Drive·Jira·Confluence·GitHub·M365·Notion 의 **원본 권한까지 동기화**하고, 질의는 단발 RAG 가 아니라 **에이전트 루프**(하이브리드 검색 · grep · 지식그래프 탐색 · 원문 전체 읽기)로 처리한다. 모든 도구 호출이 *질문자 권한으로 필터*되고 블록 단위 인용이 붙는다. MCP 로 Claude Code·Cursor·Codex 에 연결 ⇒ "사내 지식을 코딩 에이전트에 안전하게 붙이는" 경로. Glean 의 셀프호스트 대안.

> [!warning] 수치의 출처를 나눠 읽어야 한다
> - ✅ **독립(제3자 운영) 1건**: EnterpriseRAG-Bench(Onyx 운영, 11-03 기준) **39개 시스템 중 1위 93.24**(OpenAI File Search 61.03 · Amazon Q 48.96 · Azure AI Search 48.42 · Vertex 41.87) — 볼트 README grep 전건 검출. 단 운영 주체 Onyx 도 경쟁 제품사라는 점은 열어둔다.
> - 🟡 **자체 측정**: Google FRAMES 92.7%(표준 RAG 18종 최고 78.9%) · 앱별 MCP 커넥터 대비 사실 발견률 Haiku 55→80% · Sonnet 65→89% · Opus 85→92% — README 가 *PipesHub 자체 실시*임을 명시. **모델이 강할수록 이득이 줄어든다**(+25 → +24 → +7%p) — 이 수렴을 지우면 과장이 된다 → [[한정어-탈락]].

## 도메인별 추출 (local-llm)
- **메모리 아키텍처**: RAG + 지식그래프 + 에이전트 루프(원문 재독). 권한 필터가 1급 시민.
- **Hermes 적용**: 조건부 — 개인 볼트 규모엔 과잉. 팀/연구실 단위 문서를 에이전트에 붙일 때 후보.
- **트레이드오프**: Docker Compose 원커맨드지만 커넥터 50+ 의 권한 동기화 운영 부담. BYO 모델.
- **오픈소스 구현체**: YES.

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[한정어-탈락]] · [[mem0]]
- 같은 배치: [[rivet]] · [[EvoMemState]]

## 원본
- 출처: https://github.com/pipeshub-ai/pipeshub-ai
- 확인 범위: GitHub API(볼트 11-08) · README raw grep(93.24·61.03·48.96·48.42·41.87·92.7%·78.9%·55→80·65→89·85→92·39 systems 검출) · 실행 0회
- 신뢰도: ⭐⭐ (★4K · 독립 벤치 1)
