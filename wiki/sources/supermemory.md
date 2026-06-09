---
title: supermemoryai/supermemory — AI 앱용 고속 확장형 메모리 엔진
type: source
domain: ai-news
tags: [ai-news, github-trending, local-llm, agent-memory, rag, memory-engine, api]
created: 2026-06-02
updated: 2026-06-04
sources: []
reliability: high
---

# supermemoryai/supermemory — AI 장기 메모리 인프라

**GitHub**: https://github.com/supermemoryai/supermemory  
**스타**: ⭐24,863 (+680 당일, 2026-06-03 기준, prev 24,250)  
**신뢰도**: ⭐⭐⭐⭐

## 핵심 인사이트

> [!insight] 핵심 인사이트
> LLM 대화 간 망각 문제를 외부 메모리 API 하나로 해결. LongMemEval·LoCoMo·ConvoMem 벤치마크 1위. 50ms 응답 속도, Google Drive/Gmail/Notion/GitHub 자동 동기화 내장. 드롭인 래퍼로 LangChain/LangGraph/Vercel AI SDK 즉시 통합.

> [!action] 당장 할 것
> MCP 서버 설치 (Claude/Cursor 연동), npm `supermemory` 또는 pip 설치 후 API 테스트. 현재 [[에이전트-메모리-레이어]] 구축에 즉시 적용 가능.

## 도메인별 추출 (local-llm + ai-news)

**실용성 판단**: 즉시 사용 가능 — SaaS API(`app.supermemory.ai`) + 셀프호스팅 양쪽 지원  
**메모리 아키텍처**: 하이브리드 (RAG + 개인화 컨텍스트 단일 쿼리 결합)  
**Hermes 적용**: MCP 서버로 Claude/hermes-agent 직접 연동 가능  
**신뢰도**: ⭐24,250, 오늘 +647, 벤치마크 1위 수치 존재  
**대체 관계**: [[cognee]], [[claude-mem]] 대비 더 강력한 커넥터 + 벤치마크 실증

**아키텍처:**
- 메모리 추출 엔진: 대화에서 사실·선호도·기술 자동 추출
- 사용자 프로필: 안정적 사실 + 최근 활동 2-tier
- 하이브리드 검색: 지식베이스 + 개인화 메모리 단일 쿼리
- 커넥터: Google Drive, Gmail, Notion, OneDrive, GitHub 자동 동기화
- 멀티포맷: PDF, 이미지(OCR), 영상(자막), 코드(AST) 처리

**성능:**
- 응답 속도: ~50ms 컨텍스트 반환
- 벤치마크 1위: LongMemEval, LoCoMo, ConvoMem

> [!note] 배경 정보
> [[에이전트-메모리-레이어]] 트렌드의 핵심 플레이어. cognee(그래프 기반)와 달리 API 퍼스트 + 외부 서비스 커넥터 강점. 개인 LLM 어시스턴트 장기 기억 구현의 가장 현실적인 선택지.

## 관련 페이지
- [[에이전트-메모리-레이어]]
- [[AI-에이전트-프레임워크]]
- [[hermes-agent]]
- [[cognee]]

## 원본
- 출처: https://github.com/supermemoryai/supermemory
- 신뢰도: ⭐⭐⭐⭐ (⭐24,250, 벤치마크 1위)
