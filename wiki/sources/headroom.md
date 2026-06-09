---
title: chopratejas/headroom — LLM 토큰 압축 라이브러리
type: source
domain: ai-news
tags: [ai-news, github-trending, token-compression, rag, llm-infra, cost-reduction, mcp]
created: 2026-06-04
updated: 2026-06-06
sources: []
reliability: high
---

# headroom — LLM 토큰 60~95% 압축 라이브러리

**GitHub**: https://github.com/chopratejas/headroom  
**스타**: ⭐15,000 (2026-06-06 기준, ⭐7,772 → ⭐15,000 +93%)  
**라이선스**: 확인 필요

## 핵심 인사이트

> [!insight] 핵심 인사이트
> tool output·RAG 청크를 LLM에 전달하기 전 60~95% 압축하여 답변 품질은 유지하면서 토큰 비용을 대폭 절감. Library·Proxy·MCP Server 세 가지 형태로 제공해 기존 파이프라인에 드롭인 적용 가능. 당일 +1,265 스타 급등 — 토큰 비용 문제가 실제 고통이라는 방증.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐15,000 (2026-06-06, ⭐7,772→⭐15,000 단 3일 만에 +93%), 실사용 피드백 다수
- **즉시 활용**: YES — Library 형태로 pip install, 또는 MCP Server로 Claude Code 파이프라인에 바로 연결 가능
- **6개월 영향력**: RAG 파이프라인 토큰 비용 구조를 근본적으로 바꿀 수 있음. LLM API 비용의 60~95%가 컨텍스트 길이에서 나오는 경우, 즉각적인 ROI. [[supermemory]]·[[claude-mem]]과 결합 시 메모리 압축 레이어로 활용 가능
- **대체 관계**: LLMLingua, Selective Context 등 기존 압축 라이브러리 대비 — Proxy/MCP 형태 제공이 차별점
- **허와 실**: 60~95% 압축 시 어느 정도의 품질 저하가 있는가? 벤치마크 데이터 확인 필요. "품질 유지"는 마케팅 클레임일 수 있음

> [!action] 당장 할 것
> MCP Server 형태로 Claude Code + RAG 파이프라인에 연결 테스트. 실제 답변 품질 비교 후 비용 절감율 측정.

> [!warning] 주의
> 압축률 60~95%는 최대치일 가능성 높음. 실제 태스크별 품질 저하 측정 필수.

## 관련 페이지

- [[supermemory]] — LLM 에이전트 장기 메모리 엔진
- [[claude-mem]] — Claude Code 세션 간 컨텍스트 압축·주입
- [[에이전트-메모리-레이어]] — 메모리 인프라 전체 패턴
- [[markitdown]] — 문서→마크다운 변환 (RAG 전처리 파이프라인)

## 원본

- 출처: https://github.com/chopratejas/headroom
- 스타: ⭐15,000 (2026-06-06 기준, ⭐7,772→⭐15,000 +93%)
- 신뢰도: ⭐⭐⭐⭐
