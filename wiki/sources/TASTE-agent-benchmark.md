---
title: TASTE — 에이전트 벤치마크 자동 생성 방법론
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, agent, evaluation, task-synthesis, tool-use]
created: 2026-06-02
updated: 2026-06-02
sources: []
reliability: medium
---

# A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks

**arxiv**: https://arxiv.org/abs/2605.28556  
**HuggingFace**: https://huggingface.co/papers/2605.28556  
**GitHub**: https://github.com/tomerkeren42/TASTE-task-synthesis-from-tool-sequence-evolution  
**신뢰도**: ⭐⭐⭐ (논문, 실증 존재)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 기존 에이전트 벤치마크(τ²-Bench)가 포화 → TASTE는 **도구 시퀀스 역순 생성**으로 자동 벤치마크 확장. Gemini-3-Flash 기존 0.82~0.94 → τ^c-Bench에서 0.28~0.61 (진짜 어려운 문제 노출). 벤치마크 포화 현상 해결의 방법론 논문.

## 도메인별 추출 (ai-news)

**신뢰도**: ⭐⭐⭐ (논문, 11개 모델 실증)  
**즉시 활용**: NO — 개념/방법론 논문, 자체 벤치마크 구축 시 참고  
**6개월 영향력**: 에이전트 평가 인프라 개선, 포화 벤치마크 대체 방법 확산  
**대체 관계**: 기존 수동 작성 벤치마크 대비 자동 확장 가능

**TASTE 방법론 (Task Synthesis from Tool Sequence Evolution):**
- 기존: 자연어 시나리오 → 도구 시퀀스
- TASTE: 도구 시퀀스 → 자연어 문제 (역순)
- Adaptive Contrastive n-gram으로 유효 시퀀스 샘플링
- 클러스터링으로 다양한 도구 조합 커버리지 확보
- 반복적 난이도 진화(Iterative Difficulty Evolution)

**결과:**
- τ²-Bench 3개 도메인 → τ^c-Bench로 확장
- 도구 조합 2배 이상 증가
- 최강 모델도 성능 절반 이하로 떨어짐 → 실제 능력 측정

> [!note] 배경 정보
> [[K-BrowseComp]]와 같은 날 발표된 에이전트 평가 논문들 — 에이전트 벤치마크 포화 문제 업계 공통 인식. TASTE는 자동화 측면, K-BrowseComp는 도메인 특화 측면 접근.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[K-BrowseComp]]

## 원본
- 출처: https://huggingface.co/papers/2605.28556
- 신뢰도: ⭐⭐⭐ (논문, 11개 모델 실증)
