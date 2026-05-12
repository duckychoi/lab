---
title: LearningCircuit/local-deep-research — 로컬 멀티LLM 딥리서치 도구
type: source
domain: local-llm
tags: [local-llm, ai-news, github-trending, deep-research, multi-llm, search-engine, rag, simpleqa]
created: 2026-05-08
updated: 2026-05-10
sources: []
reliability: high
---

# LearningCircuit/local-deep-research

> [!insight] 핵심 인사이트
> 다중 LLM + 다중 검색엔진을 조합해 SimpleQA 기준 ~95% 성능 달성. "로컬에서도 클라우드 딥리서치 수준"을 증명하는 핵심 구현체. Perplexity 대체 가능성 있음.

## 핵심 인사이트

> [!insight] 로컬 딥리서치 실용성 입증
> SimpleQA ~95%는 상용 서비스 수준. 핵심은 단일 LLM이 아닌 **여러 LLM + 여러 검색엔진 조합** — 각 LLM의 강점을 분야별로 라우팅하는 오케스트레이션 레이어가 성능의 핵심.

> [!action] 당장 할 것
> wiki 자동 수집 파이프라인에 이 패턴 적용 검토. URL 인제스트 시 단순 fetch 대신 멀티소스 검증 레이어 추가 가능성 탐색.

> [!note] local-llm + ai-news 교차 도메인
> [[에이전트-메모리-레이어]]와 결합 시 "기억 있는 로컬 딥리서치 에이전트" 구현 가능.

## 도메인별 추출 (local-llm)

- **실용성 판단**: 실배포 가능 — 로컬 LLM(Ollama 등) + 검색 API 조합으로 구성
- **메모리 아키텍처**: 검색 결과 기반 동적 RAG — 외부 검색엔진이 지식 소스
- **Hermes 적용**: 리서치 에이전트 백엔드로 활용 가능 (질문→검색→합성 파이프라인)
- **트레이드오프**: 검색 API 비용 vs 정확도 향상 — API 없이 순수 로컬은 성능 저하
- **오픈소스 구현체**: https://github.com/LearningCircuit/local-deep-research (즉시 설치 가능)

## 관련 페이지

- [[에이전트-메모리-레이어]]
- [[cognee]]
- [[RAG-Anything]]
- [[deer-flow]]
- [[W-RAC]]

## 원본

- 출처: https://github.com/LearningCircuit/local-deep-research
- GitHub ⭐: 6,873 (2026-05-10 기준, +559 2026-05-09)
- 신뢰도: ⭐⭐⭐ (성능 수치 자체 보고, 독립 검증 필요)
