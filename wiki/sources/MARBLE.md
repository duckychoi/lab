---
title: MARBLE — 디퓨전 강화학습 다중 목표 보상 균형 최적화
type: source
domain: ai-news
tags: [ai-news, diffusion, reinforcement-learning, reward-balance, multi-objective, zhejiang-university]
created: 2026-05-08
updated: 2026-05-08
sources: []
reliability: medium
---

# MARBLE: Multi-Aspect Reward Balance for Diffusion RL

> [!insight] 핵심 인사이트
> 디퓨전 모델 RL 파인튜닝에서 "다중 보상 상충(reward conflict)" 문제 해결. 미적 품질 vs 텍스트 정렬 vs 안전성 등 여러 목표를 동시에 최적화할 때 발생하는 불균형을 체계적으로 조정.

## 핵심 인사이트

> [!insight] 영상/이미지 생성 RL의 핵심 미해결 문제
> RLHF로 이미지 품질을 올리면 다른 속성(텍스트 정렬, 다양성)이 떨어지는 것이 고질적 문제. MARBLE은 이 trade-off를 보상 가중치 동적 조정으로 해결 시도.

> [!note] video-saas 연결점
> [[Stream-R1]]·[[RLDX-1]] 등 영상 생성 RL 연구와 직결. 향후 영상 SaaS 모델의 파인튜닝 전략에 영향.

## 도메인별 추출 (ai-news)

- **신뢰도**: arXiv 2605.06507, Zhejiang University → 중간 (peer review 전)
- **즉시 활용**: 현시점 NO — 연구 단계
- **6개월 영향력**: 텍스트-이미지/비디오 생성 모델 RL 파인튜닝의 표준 방법론 후보
- **대체 관계**: 단순 단일 보상 RL 대비 다목적 최적화에서 우위

## 관련 페이지

- [[Stream-R1]]
- [[RLDX-1]]
- [[RAD-2]]
- [[ViPO]]
- [[AI-영상-생성-2026]]

## 원본

- 출처: https://huggingface.co/papers/2605.06507
- arXiv: 2605.06507
- 신뢰도: ⭐⭐⭐ (Zhejiang University, arXiv)
