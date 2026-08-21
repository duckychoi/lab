---
title: SWE-bench Science — 코딩 에이전트의 과학 엔지니어링 태스크 해결 평가
type: source
domain: ai-news
tags: [ai-news, hf-paper, coding-agent, benchmark, science, evaluation, ai-scientist]
created: 2026-08-21
updated: 2026-08-21
sources: []
reliability: medium
---

# SWE-bench Science — Can Coding Agents Resolve Engineering Tasks in Science? (HF 데일리 4위·업36)

**HF Papers**: https://huggingface.co/papers/2608.19799
**지표**: 업보트 **36** (HF 데일리 **4위**) · arxiv **2608.19799**(미래형 ID) · **도메인**: ai-news (agent-eval)

> [!insight] 핵심 인사이트
> **코딩 에이전트가 "과학 분야의 엔지니어링 태스크"(연구 코드베이스 수정·재현·실험 파이프라인 등)를 실제로 해결할 수 있는지 재는 벤치** — 일반 소프트웨어 이슈 해결(SWE-bench 계열)을 과학 연구 소프트웨어 맥락으로 옮겨, "AI 과학자"의 능력을 코드 실행 수준에서 검증한다. 08월 상단을 채운 **"AI 과학자: 능력↔평가" 짝**을 3부작으로 확장: 프로젝트 단위 자율 연구 능력 [[ASI-Bench]](능력 지향 벤치)·옴니모달 AI 과학자 [[OmniScientist]](능력 시스템)에 이어, SWE-bench Science는 그 능력을 **"과학 코드 태스크를 실제로 고치는가"**로 좁혀 측정 — 연구 자동화 계열([[Spark-to-Paper]]·[[AI-for-Auto-Research]]·[[Long-Horizon-AI-RnD-Eval]])의 실행 검증 하류에 자리.

> [!warning] 신뢰도 — 미래형 arxiv ID·원문 미검증 (medium)
> 업보트 36·데일리 4위는 raw 자동수집 신호이며 arxiv **2608.19799는 미래형 ID로 원문 초록·태스크 구성·수치 재현 불가**([[CLAUDE.md]] 사실확인 원칙). "과학 엔지니어링 태스크"의 **범위·난이도·해결률(pass@k)·대상 분야·소속은 raw 미기재 → 원문 대조 전 미검증**. 제목·한줄요약 기반 medium(수치·순위 인용 금지). 기존 SWE-bench 원 벤치와의 계보는 제목 유사이며 별개 항목으로 취급.

## 도메인별 추출 (ai-news · agent-eval)

- **신뢰도**: 업36·데일리 4위 (raw)·미래형 ID·태스크/수치 미검증 → medium
- **즉시 활용**: NO(원문·리더보드 공개 전) — "과학 코드 태스크 해결률" 평가 프레임만 참고.
- **6개월 영향력**: "AI 과학자" 주장이 논문 산출을 넘어 **실행 가능한 과학 코드 수정 능력**으로 검증되는 흐름 — 능력↔평가 짝의 성숙.
- **대체 관계**: 산출 자동화([[Spark-to-Paper]]) 대비, **실행 검증(코드가 실제로 돌아가나)** 하류로 상보.
- **허와 실**: 데일리 4위는 관심이지 해결 능력 아님 — 과학 태스크 해결률·재현성 실측이 실체.
- **액션**: 원문/리더보드 공개 시 "과학 코드 태스크" 정의만 발췌해 내 코딩 에이전트 한계 진단 프레임으로 참조(낮음).

## 관련 페이지
- [[ASI-Bench]] — 프로젝트 단위 자율 연구 능력 벤치("AI 과학자" 짝)
- [[OmniScientist]] — 옴니모달·옴니학문 AI 과학자 시스템("AI 과학자" 짝)
- [[Spark-to-Paper]] · [[AI-for-Auto-Research]] — 연구 산출 자동화(상류)
- [[Long-Horizon-AI-RnD-Eval]] — 장기 R&D 에이전트 과정 평가(평가 계보)
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2608.19799 (arxiv 2608.19799·미래형 ID)
- 지표: 업보트 36 (2026-08-21, HF 데일리 4위)
- 신뢰도: medium (미래형 arxiv ID·원문 미검증·태스크/해결률/소속 미기재·raw 자동수집)
- 수집: 2026-08-21 아침 자동수집 (HF 논문)
