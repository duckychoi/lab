---
title: TIDE — 템플릿 기반 다중 문제 선제적 발굴 프레임워크
type: source
domain: ai-news
tags: [ai-news, hf-paper, problem-discovery, template-guided, kaist, iterative, multi-problem]
created: 2026-06-06
updated: 2026-06-06
sources: []
reliability: medium
---

# TIDE — Proactive Multi-Problem Discovery via Template-Guided Iteration

**논문**: https://huggingface.co/papers/2606.04743  
**소속**: KAIST AI  
**HF 업보트**: 36

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 하나의 문제만 해결하는 게 아닌 **패턴 기반으로 유사 문제군을 선제적으로 탐색·발굴**하는 프레임워크. 템플릿을 추출하고 이를 반복 적용해 다수 문제를 자동 생성 — "문제 하나 해결" → "문제 클래스 전체 해결"로 패러다임 전환. KAIST AI 연구팀.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — KAIST AI 연구팀, 업보트 36, 국내 주요 연구기관
- **즉시 활용**: NO — 연구 프레임워크. 에이전트 태스크 생성 파이프라인에 응용 가능
- **6개월 영향력**: [[auto-research]] 스킬이나 [[wiki]] 스킬의 자동 탐색 방향에 영향 가능. 에이전트가 스스로 할 일을 찾는 "proactive AI" 패턴
- **대체 관계**: 기존 단일 문제 해결 접근 대비 다중 문제 공간 탐색
- **허와 실**: "선제적 발굴"의 실제 품질 — 쓸모없는 문제를 많이 생성할 가능성 있음

> [!question] 미해결 질문
> 자동 생성된 문제의 품질 필터링 기준은 무엇인가? 실제 유용한 문제 비율은?

## 관련 페이지

- [[AI-에이전트-프레임워크]] — 에이전트 자율성 패턴
- [[COLLEAGUE-SKILL]] — 에이전트 스킬 자동 생성
- [[AdaPlanBench]] — 적응적 계획 평가 (같은 날 수집, 에이전트 능력 평가 도메인)

## 원본

- 출처: https://huggingface.co/papers/2606.04743
- arXiv: 2606.04743
- 소속: KAIST AI
- 업보트: 36
- 신뢰도: ⭐⭐⭐
