---
title: GlobalSplat — Efficient Feed-Forward 3DGS
type: source
domain: ai-news
tags: [ai-news, slam-3dgs, 3dgs, gaussian-splatting, feed-forward, real-time]
created: 2026-04-19
updated: 2026-04-19
sources: []
reliability: medium
---

# GlobalSplat — Efficient Feed-Forward 3DGS

> [!insight] 핵심 인사이트
> 전역 장면 토큰(global scene token)으로 3D Gaussian Splatting을 단일 피드포워드 패스로 처리 — 기존 최적화 기반 3DGS 대비 처리 속도 대폭 향상. 실시간 3D 재구성의 현실화 단계.

## 도메인별 추출

**현재 SOTA**: 피드포워드 패스로 3DGS 처리 — 반복 최적화 없이 단일 추론으로 장면 재구성
**실시간 가능성**: 단일 패스 → 실시간 30fps+ 가능성 향상
**응용 가능성**: 영상에서 실시간 3D 추출 → video-saas × slam-3dgs 교차 도메인
**필수 레퍼런스**: arXiv 2604.15284

> [!note] 배경 정보
> 기존 3DGS는 장면마다 수백~수천 이터레이션 최적화 필요. 피드포워드 방식은 학습된 모델로 단번에 처리.

## 관련 페이지

- [[LIO-SAM]]
- [[OpenSpatial]]
- [[AI-3D-생성]]
- [[HY-World-2.0]]

## 원본

- 출처: https://huggingface.co/papers/2604.15284
- 업보트: 18 (2026-04-19)
- 신뢰도: ⭐⭐⭐
