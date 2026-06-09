---
title: mnfst/manifest — AI 에이전트 스마트 모델 라우팅
type: source
domain: ai-news
tags: [ai-news, github-trending, model-routing, cost-optimization, llm-infra, agent]
created: 2026-06-04
updated: 2026-06-04
sources: []
reliability: medium
---

# manifest — AI 에이전트 비용/성능 기반 자동 모델 라우팅

**GitHub**: https://github.com/mnfst/manifest  
**스타**: ⭐6,786 (2026-06-04 기준)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> AI 에이전트 요청을 비용·성능 기준으로 최적 모델에 자동 라우팅. 비용 최대 70% 절감 목표. 단순 쿼리는 저렴한 모델, 복잡한 추론은 고성능 모델로 동적 분기 — [[headroom]] 토큰 압축과 결합하면 비용 최적화 이중 레이어 구성 가능.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — ⭐6,786, 소규모이나 성장 중
- **즉시 활용**: YES (가능성) — LiteLLM이나 다른 라우터와 비교 후 선택
- **6개월 영향력**: 멀티모델 에이전트 인프라에서 비용 제어 레이어로 표준화될 가능성. 라우팅 품질이 전체 에이전트 성능에 직접 영향
- **대체 관계**: [[litellm]] 대비 라우팅 특화. OpenRouter와 유사하나 셀프호스팅
- **허와 실**: "70% 비용 절감"은 특정 워크로드 기준. 실제 사용 패턴에 따라 다름

> [!warning] 주의
> 라우팅 로직이 잘못되면 중요 쿼리가 저성능 모델로 가서 품질 저하 발생.

## 관련 페이지

- [[litellm]] — 100+ LLM API 단일 인터페이스 (비교 대상)
- [[headroom]] — 토큰 압축 (비용 절감 결합 가능)
- [[에이전트-메모리-레이어]] — 에이전트 인프라

## 원본

- 출처: https://github.com/mnfst/manifest
- 스타: ⭐6,786 (2026-06-04)
- 신뢰도: ⭐⭐⭐
