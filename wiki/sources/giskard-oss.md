---
title: Giskard-AI/giskard-oss — LLM 에이전트 평가·테스트 오픈소스 라이브러리
type: source
domain: ai-news
tags: [ai-news, github-trending, LLM-eval, testing, RAG, hallucination, bias, agent, quality]
created: 2026-05-28
updated: 2026-05-28
sources: []
reliability: medium
---

# Giskard-AI/giskard-oss — LLM 에이전트 평가·테스트 라이브러리

## 핵심 인사이트

> [!insight] 핵심 인사이트
> LLM 에이전트와 RAG 파이프라인의 품질을 편향·환각·취약성 세 축으로 자동 검증. 프로덕션 배포 전 LLM 시스템의 안전성·신뢰성을 코드 한 줄로 점검. ⭐5,398.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — ⭐5,398, 전문 AI 평가 회사 Giskard 공식 OSS, 활발한 유지보수
- **즉시 활용**: YES — pip install giskard 후 RAG 파이프라인·LLM 에이전트 즉시 테스트 가능
- **6개월 영향력**: LLM 에이전트 프로덕션 배포가 증가하면서 평가·모니터링 수요 급증. [[langfuse]](관측성)와 결합하면 배포→모니터링→재평가 사이클 완성
- **대체 관계**: LangSmith(LangChain 생태계), DeepEval, RAGAS(RAG 평가 특화) 등과 경쟁. Giskard는 편향·안전성에 더 집중
- **허와 실**: 오픈소스 버전과 유료 플랫폼 기능 차이 확인 필요. 클레임("취약성 자동 탐지")의 실제 커버리지 검증 요

> [!action] 당장 할 것
> 기존 RAG 파이프라인에 `giskard scan()` 적용해 환각 비율 측정. [[langfuse]]와 통합해 지속적 품질 모니터링 구성

## 주요 기능

- **자동 취약성 스캔**: 환각(Hallucination), 편향(Bias), 주입 공격 등 자동 탐지
- **RAG 파이프라인 평가**: 검색 품질, 문맥 활용도, 응답 신뢰성 측정
- **LLM 에이전트 테스트**: 멀티턴 대화, 도구 사용, 계획 수립 품질 평가
- **CI/CD 통합**: GitHub Actions 등에 통합해 자동 회귀 테스트

## 관련 페이지

- [[langfuse]] — LLM 관측성, Giskard와 상호보완
- [[ClawBench]] — AI 에이전트 종합 벤치마크
- [[DR3-Eval]] — AI 딥리서치 에이전트 평가 프레임워크
- [[AI-에이전트-프레임워크]] — 에이전트 인프라 전체 현황

## 원본

- 출처: https://github.com/Giskard-AI/giskard-oss
- 스타: 5,398 (2026-05-28 기준)
- 언어: Python
- 신뢰도: ⭐⭐⭐
