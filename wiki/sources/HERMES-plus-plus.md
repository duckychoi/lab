---
title: HERMES++ — 자율주행용 통합 3D 장면 이해·생성 세계 모델
type: source
domain: ai-news
tags: [ai-news, slam-3dgs, autonomous-driving, world-model, 3d, scene-understanding]
created: 2026-05-07
updated: 2026-05-07
sources: []
reliability: medium
---

# HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation

> [!insight] 핵심 인사이트
> 자율주행을 위한 통합 세계 모델 — 3D 장면 이해(인식)와 생성(시뮬레이션)을 단일 모델로 처리. 업보트 63. slam-3dgs 도메인과 ai-news 교차 — 자율주행 시뮬레이션을 AI 영상 생성과 결합하는 방향성.

**HuggingFace**: https://huggingface.co/papers/2604.28196  
**업보트**: 63 (2026-05-07 기준)  
**신뢰도**: ⭐⭐⭐

## 도메인별 추출 (slam-3dgs 관점)

- **신뢰도**: 업보트 63 — 중간 이상. 자율주행은 검증 요구 수준 높은 도메인
- **현재 SOTA**: 단일 모델로 3D 이해+생성 통합 — 기존 분리된 파이프라인 대비 효율적
- **실시간 가능성**: 자율주행 실시간 요건(30fps+) 충족 여부 미확인
- **응용 가능성**: 자율주행 외 로봇 탐색·3D 씬 생성에 전이 가능
- **slam-3dgs 연결**: [[LIO-SAM]](라이다 SLAM) + HERMES++ 조합으로 실세계 3D 이해→시뮬레이션 파이프라인 구성 가능성

> [!note] 배경 정보
> "세계 모델" = 환경 상태를 이해하고 미래를 예측·시뮬레이션하는 모델. 자율주행에서 센서 데이터로 주변 3D 세계를 실시간 재구성·예측하는 것이 핵심.

## 관련 페이지
- [[LIO-SAM]]
- [[HY-World-2.0]]
- [[Matrix-Game-3.0]]
- [[RLDX-1]]

## 원본
- 출처: https://huggingface.co/papers/2604.28196
- 신뢰도: ⭐⭐⭐ (업보트 63)
