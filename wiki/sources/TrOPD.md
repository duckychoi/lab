---
title: TrOPD — Trust Region On-Policy Distillation (Samsung Research)
type: source
domain: ai-news
tags: [ai-news, hf-paper, llm-distillation, on-policy, trust-region, math-reasoning, code-generation, samsung]
created: 2026-06-04
updated: 2026-06-04
sources: []
reliability: high
---

# TrOPD — 신뢰 구간 기반 온폴리시 LLM 증류

**논문**: https://huggingface.co/papers/2606.01249  
**저자**: Samsung Research  
**태스크**: LLM 온폴리시 지식 증류 (On-Policy Distillation)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> LLM 온폴리시(on-policy) 증류의 핵심 문제인 **훈련 불안정성**을 신뢰 구간(Trust Region) 제한으로 해결. 수학 추론·코드 생성·일반 벤치마크에서 기존 OPD 기반 SOTA를 전반적으로 능가. Samsung Research의 실용 지향 LLM 압축 연구.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — Samsung Research, arXiv 등재, HF Papers 수록
- **즉시 활용**: NO (연구 단계) — 구현체가 공개됐는지 확인 필요. 원리 이해는 지금 가능
- **6개월 영향력**: 소형 모델에 대형 모델 추론 능력 이식하는 비용을 낮춤. [[MiniCPM5-1B]]·[[LFM2.5-8B]] 같은 소형 모델 파인튜닝 시 적용 고려
- **대체 관계**: GKD(Generalized KD), DistiLLM 등 기존 on-policy KD 대비 안정성 개선
- **허와 실**: "SOTA 전반 능가"는 특정 벤치마크셋 기준. 실제 배포 모델에서의 검증 필요

## 기술 요약

온폴리시 증류(OPD)는 학생 모델이 직접 생성한 샘플로 교사 모델로부터 학습하는 방식:
- **문제**: 학생 모델의 분포 이동(distribution shift)이 훈련 불안정성 야기
- **해결**: PPO의 Trust Region 개념 차용 — 업데이트 크기 제한으로 안정적 학습
- **결과**: 수학 추론, 코드 생성, 일반 NLP 벤치마크 전반 개선

## 관련 페이지

- [[MiniCPM5-1B]] — 온폴리시 증류(OPD) 활용 소형 모델 (SFT+RL+OPD)
- [[Draft-OPD]] — OPD 관련 선행 연구
- [[Accelerating-RL-Post-Training]] — RL 기반 포스트트레이닝
- [[에이전트-메모리-레이어]] — 경량화 모델 활용 에이전트 인프라

## 원본

- 출처: https://huggingface.co/papers/2606.01249
- arXiv: 2606.01249
- 저자: Samsung Research
- 신뢰도: ⭐⭐⭐⭐
