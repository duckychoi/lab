---
title: Beyond the Current Observation — 비마르코프 게임에서 MLLM 평가
type: source
domain: ai-news
tags: [ai-news, hf-paper, mllm, evaluation, non-markov, game, memory, reasoning]
created: 2026-06-18
updated: 2026-06-18
sources: []
reliability: medium
---

# Beyond the Current Observation: Evaluating MLLMs in Non-Markov Games (arXiv 2606.19338)

## 핵심 인사이트

> [!insight] MLLM의 "과거 기억 기반 의사결정" 약점을 비마르코프 게임으로 체계적 폭로
> 현재 관측만으로는 최적 결정이 불가능한 비마르코프 환경에서 멀티모달 LLM을 평가. 대부분의 MLLM이 과거 관측 히스토리를 제대로 활용하지 못함 — 에이전트 메모리 아키텍처의 실질적 취약점 실증.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐ — HF 업보트 33. 벤치마크 논문이므로 방법론 검증 필요
- **즉시 활용**: NO — 연구 인사이트로 활용. MLLM 에이전트 설계 시 히스토리 관리에 주의
- **6개월 영향력**: 에이전트 메모리 레이어 설계의 중요성을 실증 데이터로 뒷받침. [[에이전트-메모리-레이어]] 트렌드 가속 근거
- **대체 관계**: 기존 Markov 가정 기반 벤치마크의 한계 지적
- **허와 실**: 게임 환경이 실제 에이전트 시나리오를 얼마나 대표하는지 검토 필요
- **액션**: 논문 방법론 확인 후 [[에이전트-메모리-레이어]] 페이지에 인용 추가

> [!note] 배경 정보
> 비마르코프 결정 과정(Non-Markov Decision Process, NMDP) — 현재 상태만으로 최적 행동을 결정할 수 없고, 이전 히스토리가 필요한 환경. 포커, 스타크래프트 등 실제 게임 대부분이 해당.

## 관련 페이지

- [[에이전트-메모리-레이어]] — 에이전트 메모리 인프라 패턴
- [[EvoArena]] — LLM 에이전트 메모리 진화 벤치마크
- [[Graph-Memory-LLM-Agents]] — 그래프 기반 에이전트 메모리

## 원본

- 출처: https://huggingface.co/papers/2606.19338
- HF 업보트: ↑33 (2026-06-18)
- 신뢰도: ⭐⭐ (소규모 관심, 방법론 검증 필요)
