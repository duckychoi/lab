---
title: LongTraceRL — 검색 에이전트 궤적 기반 장문 추론 강화학습 (Tsinghua KEG)
type: source
domain: ai-news
tags: [ai-news, RL, long-context, reasoning, search-agent, trajectory, tsinghua, LLM-training]
created: 2026-06-01
updated: 2026-06-01
sources: []
reliability: high
---

# LongTraceRL — 검색 궤적 + 루브릭 보상으로 장문 추론 능력 강화

> [!insight] 핵심 인사이트
> 검색 에이전트가 수집한 궤적(trace)과 루브릭 기반 보상을 활용해 LLM의 장문 컨텍스트 추론을 강화학습으로 학습. Tsinghua KEG. HF 업보트 28. RAG + RL 결합 접근으로 검색 에이전트의 추론 품질 향상.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — HF 업보트 28, Tsinghua KEG, arXiv 2605.31584
- **즉시 활용**: NO — 연구/훈련 파이프라인 단계
- **6개월 영향력**: RAG 에이전트의 추론 품질을 RL로 개선하는 방향 — [[deer-flow]], [[local-deep-research]] 같은 딥리서치 에이전트 훈련에 적용 가능
- **대체 관계**: [[rubricem]](루브릭 기반 RL) 유사 접근. 검색 에이전트 특화가 차별점
- **액션**: 검색 에이전트 구현 시 훈련 방법론으로 참조

## 관련 페이지

- [[deer-flow]] — ByteDance 장기 작업 SuperAgent
- [[local-deep-research]] — 로컬 딥리서치 에이전트
- [[rubricem]] — 루브릭 기반 메타-RL (Google)
- [[W-RAC]] — RAG 검색 정확도 개선

## 원본

- 출처: https://huggingface.co/papers/2605.31584
- 업보트: 28 (2026-06-01)
- 기관: Tsinghua KEG
- 신뢰도: ⭐⭐⭐
