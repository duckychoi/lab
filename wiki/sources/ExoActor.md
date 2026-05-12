---
title: ExoActor — 3인칭 영상 생성 기반 휴머노이드 로봇 제어
type: source
domain: ai-news
tags: [ai-news, slam-3dgs, hf-paper, humanoid-robot, video-generation, imitation-learning, embodied-ai]
created: 2026-05-01
updated: 2026-05-01
sources: []
reliability: high
---

# ExoActor — Exocentric Video Generation for Humanoid Control

**arXiv**: https://arxiv.org/abs/2604.27711  
**신뢰도**: ⭐⭐⭐⭐ (논문)

> [!insight] 핵심 인사이트
> **3인칭(exocentric) 영상 생성 모델**로 휴머노이드 로봇 행동을 제어. **추가 실데이터 없이 새로운 시나리오로 일반화** 가능. 영상 생성 모델(video diffusion)을 로봇 제어 정책으로 전환하는 새로운 파이프라인 — "영상 AI + 로봇공학"의 교차점에 있는 연구.

> [!note] 배경 정보
> 기존 모방 학습은 대량의 실로봇 데이터 필요. ExoActor는 합성 영상 생성으로 이를 대체 — 데이터 수집 비용 절감과 시나리오 다양화 가능.

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: 3인칭 영상 기반 휴머노이드 제어 — 유사 접근법으로 [[HY-Embodied]], [[UniT-Humanoid-Policy]] 존재
- **실시간 가능성**: 로봇 제어 적용 시 지연 문제 — 영상 생성 추론 속도가 병목. 현재는 오프라인 계획 수준
- **카메라 파이프라인**: 외부 카메라(exocentric)에서 캡처한 3인칭 영상 → 로봇 행동 정책 추출
- **응용 가능성**: 영상 AI SaaS의 3인칭 촬영 데이터를 로봇 학습에 재활용하는 파이프라인으로 확장 가능
- **필수 레퍼런스**: [[HY-Embodied]], [[HY-Embodied-0.5]], [[DeVI]]와 함께 embodied AI 연구 맥락 파악

## 관련 페이지
- [[HY-Embodied]]
- [[HY-Embodied-0.5]]
- [[UniT-Humanoid-Policy]]
- [[DeVI]]
- [[AI-영상-생성-2026]]

## 원본
- 출처: https://arxiv.org/abs/2604.27711
- 신뢰도: ⭐⭐⭐⭐ (논문)
