---
title: Latent-Spatial-Memory
type: source
domain: ai-news
tags: [world-model, video, spatial-memory, navigation, latent-space]
created: 2026-06-09
updated: 2026-06-09
sources: []
reliability: medium
---

# Latent Spatial Memory for Video World Models

## 핵심 인사이트

> [!insight] 비디오 월드 모델에 공간 기억 추가 — 장거리 일관성 문제 해결 접근
> 비디오 월드 모델에 잠재 공간 메모리 모듈을 추가해 장거리 공간 일관성과 내비게이션 정확도를 향상. 긴 영상에서 공간이 일관되게 유지되지 않는 문제(방 크기가 변하거나 물체가 사라지는 현상)를 메모리 아키텍처로 해결.

## 도메인별 추출

**핵심 내용:**
- HF upvotes 35
- 잠재 공간 메모리 모듈: 이전 프레임의 공간 정보를 압축 보존
- 내비게이션 정확도 향상 → 게임 월드 모델, 로봇 시뮬레이션에 직접 적용 가능
- [[Matrix-Game-3.0]]의 장기 메모리 스트리밍과 유사한 문제 접근

**연결 맥락:**
- [[gameworld]] 벤치마크에서 이 구조의 에이전트가 높은 점수 받을 가능성
- [[DV-World]]의 데이터 시각화 에이전트와 공간 이해 연구 흐름 공유

## 관련 페이지
- [[Matrix-Game-3.0]]
- [[gameworld]]
- [[SpatialWorld]]

## 원본
- 출처: https://huggingface.co/papers/2606.09828
- HF upvotes 35 (2026-06-09 기준)
- 신뢰도: ⭐⭐⭐
