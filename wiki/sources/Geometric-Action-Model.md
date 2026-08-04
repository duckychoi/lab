---
title: Geometric Action Model — ETH Zürich, SE(3) 대칭성 기반 로봇 정책 학습
type: source
domain: ai-news
tags: [ai-news, hf-paper, robotics, eth-zurich, se3, sample-efficiency, policy-learning, geometry]
created: 2026-06-17
updated: 2026-06-17
sources: []
reliability: high
---

# Geometric Action Model

## 핵심 인사이트

> [!insight] 기하학적 대칭성으로 로봇 학습 샘플 효율을 혁신 — 적은 데이터로 더 잘 학습
> ETH Zürich의 로봇 정책 학습용 기하학적 액션 모델. SE(3)(3D 회전·평행이동 대칭 그룹)을 활용해 샘플 효율 대폭 개선. 같은 데이터로 더 빠르게 로봇이 배움.

## 도메인별 추출

**핵심 기여:**
- arXiv 2606.17046, HF upvotes: 67
- SE(3) 대칭성 활용 → 관찰한 동작을 회전·반전에 무관하게 일반화
- 샘플 효율 개선 = 데이터 수집 비용 절감 (로봇 학습의 핵심 병목 해결)
- ETH Zürich = 로봇공학 최고 연구기관 중 하나

**로봇 AI 맥락:**
- [[ACE-Ego-0]], [[HiVLA]], [[Qwen-VLA]] 등 VLA 모델들의 액션 표현 개선에 직접 적용 가능
- [[Introduction-to-Autonomous-Robots]] 교과서의 제어 이론 + 이 연구 결합

> [!note] SE(3)은 로봇 팔·드론 조작에서 핵심 — "어느 방향에서 보든 같은 물체"를 AI가 이해

## 관련 페이지
- [[ACE-Ego-0]]
- [[Introduction-to-Autonomous-Robots]]
- [[HiVLA]]
- [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2606.17046
- HuggingFace upvotes: 67
- 신뢰도: ⭐⭐⭐⭐
