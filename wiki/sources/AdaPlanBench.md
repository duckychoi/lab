---
title: AdaPlanBench — LLM 에이전트 적응적 계획 능력 평가 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, planning, llm-agent, adaptive, evaluation, uiuc]
created: 2026-06-06
updated: 2026-06-06
sources: []
reliability: medium
---

# AdaPlanBench — Evaluating Adaptive Planning in LLM Agents

**논문**: https://huggingface.co/papers/2606.05622  
**소속**: UIUC (University of Illinois Urbana-Champaign)  
**HF 업보트**: 35

## 핵심 인사이트

> [!insight] 핵심 인사이트
> LLM 에이전트가 **세계 제약(world constraints)과 사용자 제약(user constraints)** 하에서 계획을 동적으로 조정하는 능력을 평가하는 벤치마크. 고정 계획이 아닌 상황 변화에 따른 재계획(replanning) 능력 측정 — 실제 사용 시나리오에서 에이전트 신뢰성 예측에 중요.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — UIUC 연구팀, 업보트 35, 탑 CS 대학 연구
- **즉시 활용**: NO — 평가 벤치마크. 에이전트 개발 시 AdaPlanBench 점수 추적 가능
- **6개월 영향력**: [[hermes-agent]], [[superpowers]], [[multica]] 같은 에이전트 프레임워크 평가 기준으로 채택 가능. "계획 능력" 메트릭의 표준화
- **대체 관계**: 기존 단일 계획 벤치마크 대비 동적 적응 측정 추가
- **허와 실**: 제약 조건 설정이 현실을 얼마나 반영하는지 — 벤치마크 자체의 생태적 타당도

> [!question] 미해결 질문
> AdaPlanBench에서 현재 SOTA 에이전트 성능은 얼마나 되는가? 인간 기준점과의 갭은?

## 관련 페이지

- [[AI-에이전트-프레임워크]] — 에이전트 평가 맥락
- [[hermes-agent]] — 평가 대상 에이전트 프레임워크
- [[TIDE]] — 같은 날 수집, 에이전트 능력 발굴 접근
- [[ClawBench]] — AI 에이전트 종합 벤치마크 (비교 대상)

## 원본

- 출처: https://huggingface.co/papers/2606.05622
- arXiv: 2606.05622
- 소속: UIUC
- 업보트: 35
- 신뢰도: ⭐⭐⭐
