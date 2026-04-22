---
title: HiVLA — 계층적 시각 기반 로봇 조작 시스템
type: source
domain: ai-news
tags: [ai-news, hf-paper, robotics, vla, manipulation, vision-language-action, slam-3dgs]
created: 2026-04-17
updated: 2026-04-17
sources: []
reliability: medium
---

# HiVLA: Hierarchical Embodied Manipulation System

> [!insight] 핵심 인사이트
> **시각 기반 계층적 로봇 조작 시스템**. HF upvote 15 (2026-04-17). VLA(Vision-Language-Action) 모델의 실세계 manipulation 정확도 향상 — 고수준 언어 명령과 저수준 모터 제어를 계층적으로 분리해 복잡한 조작 태스크 가능.

## 핵심 인사이트

> [!note] 배경 정보
> [[HY-Embodied]] 논문(arXiv 2604.07430)과 연결되는 embodied AI 흐름. 계층적 구조: 상위 레이어(언어 이해+계획) → 하위 레이어(모터 제어). [[slam-3dgs]] 도메인의 로봇 인지 능력과 직결.

> [!question] 미해결 질문
> 실시간 inference 가능? 어떤 로봇 플랫폼에서 검증? 오픈소스 코드?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐ — upvote 15, 학술 논문
- **즉시 활용**: NO — 전문 로봇 하드웨어 필요
- **6개월 영향력**: 로봇 조작 정확도 표준 향상에 기여 가능
- **대체 관계**: RT-2, OpenVLA 등 기존 VLA 모델 대안
- **허와 실**: "계층적" 구조가 실제 복잡한 환경에서 얼마나 강건한지 미검증
- **액션**: slam-3dgs 도메인 심화 시 재검토

## 관련 페이지
- [[HY-Embodied]]
- [[slam-3dgs 도메인]]
- [[OpenSpatial]]

## 원본
- 출처: https://huggingface.co/papers/2604.14125
- 신뢰도: ⭐⭐ (upvote 15)
