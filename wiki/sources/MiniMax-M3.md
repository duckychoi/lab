---
title: MiniMax-M3 — MiniMax 427B MoE 멀티모달 대형 모델
type: source
domain: ai-news
tags: [ai-news, hf-model, minimax, multimodal, moe, 427B, image-text, large-model]
created: 2026-06-17
updated: 2026-06-19
sources: []
reliability: high
---

# MiniMax-M3

## 핵심 인사이트

> [!insight] 427B MoE 멀티모달 — MiniMax의 플래그십 오픈 멀티모달 모델
> MiniMax의 427B 파라미터 이미지-텍스트 멀티모달 모델. 대규모 MoE(Mixture of Experts) 아키텍처 기반 범용 멀티모달 추론. [[MiniMax-M2.7]]의 후속. HF 다운로드 25.1k.

## 도메인별 추출

**핵심 특징:**
- HF 다운로드: 56.2k (+31.1k 이틀 만에 폭증)
- 427B 파라미터 MoE = 대규모이지만 활성 파라미터는 일부 → 효율적
- 이미지 + 텍스트 입력 통합 처리
- MiniMax = 중국 스타트업 중 가장 적극적인 오픈소스 전략

**포지셔닝:**
- [[MiniMax-M2.7]] → M3 진화: 파라미터 확장 + 멀티모달 강화
- [[DeepSeek-V4-Pro]](862B), [[MiniMax-Sparse-Attention]] 등 대형 중국 AI 모델 경쟁 구도
- 427B MoE = 실제 활성 파라미터 약 40-80B 수준 → 서빙 비용 합리적

> [!note] 25.1k DL은 모델 크기 대비 낮은 편 — 427B 서빙 인프라 요구사항이 채택 장벽

## 관련 페이지
- [[MiniMax-M2.7]]
- [[MiniMax-Sparse-Attention]]
- [[DeepSeek-V4-Pro]]
- [[diffusiongemma-26B]]

## 원본
- 출처: https://huggingface.co/MiniMaxAI/MiniMax-M3
- HuggingFace 다운로드: 56.2k (2026-06-19 기준)
- 신뢰도: ⭐⭐⭐⭐
