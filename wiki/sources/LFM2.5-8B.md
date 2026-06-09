---
title: LiquidAI/LFM2.5-8B-A1B — Liquid AI 8B MoE 언어 모델 (활성 1B)
type: source
domain: ai-news
tags: [ai-news, local-llm, LFM, liquid-ai, MoE, 8B, text-generation, edge-ai]
created: 2026-05-29
updated: 2026-06-04
sources: []
reliability: medium
---

# LFM2.5-8B-A1B — Liquid Foundation Model, 8B MoE, 활성 1B

## 핵심 인사이트

> [!insight] 핵심 인사이트
> Liquid AI의 LFM(Liquid Foundation Model) 시리즈 2.5. 8B 총 파라미터 중 1B만 활성화하는 MoE 구조로 소형 디바이스에서의 효율적 추론 목표. HF DL 60,171 (2026-06-03, prev 37,900). MATH500 74.8→88.8, AIME25 20→42.5, 비환각률 7.5→63.5로 전작 대비 전 지표 대폭 개선.

## 도메인별 추출 (local-llm 템플릿)

- **실용성 판단**: YES (가능성) — 활성 1B은 엣지/온디바이스 수준. MoE 특성상 전체 8B 로드 필요하지만 추론 시 1B 활성
- **메모리 아키텍처**: MoE(Mixture of Experts) — 라우팅으로 1B 활성 파라미터만 연산
- **Hermes 적용**: 검토 가능 — 활성 1B 수준의 성능과 로컬 추론 속도 우선 확인
- **트레이드오프**: 8B 전체 로드 필요 but 추론 연산은 1B 수준 — 메모리 vs 속도 균형
- **오픈소스 구현체**: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B

> [!question] 미해결 질문
> LFM 아키텍처가 일반 트랜스포머 MoE와 어떻게 다른가? "Liquid" 특성이 실제로 성능에 기여하는가?

## 관련 페이지

- [[MiniCPM5-1B]] — 유사 소형 효율 모델 (순수 1B)
- [[Qwen3.6-35B-A3B]] — 더 큰 MoE 참조 (35B/활성 3B)
- [[Zaya1-8B]] — 동급 8B 모델 비교 대상
- [[에이전트-메모리-레이어]] — 경량 LLM 에이전트 백엔드

## 원본

- 출처: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- 다운로드: 60,171 (2026-06-03 기준, prev 37,900)
- 태스크: Text Generation
- 신뢰도: ⭐⭐⭐
