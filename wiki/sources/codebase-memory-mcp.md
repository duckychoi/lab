---
title: codebase-memory-mcp — 코드베이스를 지식 그래프로 인덱싱하는 MCP 서버
type: source
domain: ai-news
tags: [ai-news, github-trending, mcp, knowledge-graph, codebase, indexing, local-llm, token-reduction]
created: 2026-06-19
updated: 2026-06-29
sources: []
reliability: medium
---

# codebase-memory-mcp (DeusData/codebase-memory-mcp)

> [!insight] 핵심 인사이트
> ⭐20,534 (2026-06-29, 당일 +2,190; ⭐7,379→20,534 10일 만에 +178%, 급등 장기화). 코드베이스 전체를 지식 그래프로 변환해 MCP로 노출 — 에이전트가 "코드 지도"를 가진 채 작업. 158개 언어 지원 + 밀리초 쿼리 + 토큰 99% 절감 주장은 검증 필요하나 방향성 타당. 급등이 5일째 일 +1,000대 지속 = 단발 바이럴이 아닌 실수요 신호로 확정.

## 핵심 인사이트

> [!warning] 신뢰도 주의
> "토큰 사용량 99% 절감" — 마케팅 클레임. 전체 파일 전송 대신 그래프 노드 쿼리로 절감하는 원리는 타당하나, 99%는 이상적 케이스. 실측치 확인 필요.

> [!note] 배경 정보
> 오늘 하루 +2,322 — 이 정도 급등은 HackerNews/Twitter 바이럴 또는 주요 유튜버 소개 신호. 출시 초기 버그 가능성 높음.

> [!action] 당장 할 것
> Claude Code + codebase-memory-mcp 연동 실험. 대형 프로젝트(현재 작업 중인 코드베이스)에서 실제 토큰 절감 측정.

## 도메인별 추출

- **신뢰도**: ⭐⭐ (신생 프로젝트, 오늘 급등 중 — 검증 전)
- **즉시 활용**: MAYBE — MCP 서버 설치 후 Claude Code와 연동. 158개 언어 파서 의존성 확인 필요.
- **6개월 영향력**: 대형 코드베이스에서 LLM 에이전트의 컨텍스트 비용 문제가 핵심 병목 — 이 방향의 해법은 실제 수요. 성숙하면 AI 코딩 에이전트 필수 인프라가 될 수 있음.
- **대체 관계**: IDE 내장 인덱싱(Cursor, Copilot) vs 독립 MCP 서버. MCP는 Claude Code 등 범용 에이전트에 통합 가능한 장점.
- **허와 실**: 그래프 인덱싱 정확도가 관건. 동적 타입 언어(Python, JS)에서 호출 그래프가 불완전할 수 있음.
- **액션**: 즉시 star. 다음 대형 프로젝트 시 테스트.

> [!question] 미해결 질문
> 실제 토큰 절감 수치? 동적 임포트/메타프로그래밍 처리? 인덱싱 속도?

## 관련 페이지

- [[Claude-Code-워크플로우]]
- [[crewAI]]
- [[에이전트-메모리-레이어]]

## 원본
- 출처: https://github.com/DeusData/codebase-memory-mcp
- 스타: ⭐20,534 (2026-06-29, 당일 +2,190) ← ⭐13,589 (06-24, +1,300) ← ⭐7,379 (06-19)
- 신뢰도: ⭐⭐⭐ (급등 10일+ 지속·⭐20K 돌파 — 실수요 확정, 여전히 신생)
