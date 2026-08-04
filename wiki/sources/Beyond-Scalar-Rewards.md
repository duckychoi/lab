---
title: Beyond Scalar Rewards — 추론을 점수 분포에 내재화한 강화학습
type: source
domain: ai-news
tags: [ai-news, hf-paper, reinforcement-learning, reward-modeling, score-distribution, reasoning, tongyi]
created: 2026-06-11
updated: 2026-06-11
sources: []
reliability: medium
---

# Beyond Scalar Rewards by Internalizing Reasoning into Score Distributions

## 핵심 인사이트

> [!insight] 보상 함수에 추론 과정을 내재화
> Alibaba Tongyi-MAI 팀. 단순한 스칼라(0~1 점수) 대신 추론 과정을 점수 분포 자체에 내재화 → LLM의 강화학습 훈련 품질 향상. "왜 좋은가"를 설명하는 보상이 단순 점수보다 더 나은 학습 신호 제공.

## 도메인별 추출

- **신뢰도**: HuggingFace 논문 (arXiv 2606.09076), Alibaba Tongyi-MAI — 산업 연구소
- **즉시 활용**: NO — 대규모 RLHF 훈련 파이프라인 필요
- **6개월 영향력**: LLM 훈련 방법론 개선 — [[DeepSeek-V4-Pro]], [[Qwen3.6-35B-A3B]] 후속 모델에 채택 가능
- **대체 관계**: 기존 RLHF 스칼라 보상의 개선된 대안
- **허와 실**: 학습 효과는 검증됐지만 추가적인 추론 비용과 복잡성 발생
- **액션**: 파인튜닝 파이프라인 설계 시 보상 모델 선택 기준으로 참고

## 관련 페이지

- [[DeepSeek-V4-Pro]]
- [[Qwen3.6-35B-A3B]]
- [[Role-Agent]]

## 원본

- 출처: https://huggingface.co/papers/2606.09076
- 신뢰도: ⭐⭐ (HF 논문, Alibaba Tongyi)
