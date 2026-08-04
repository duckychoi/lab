---
title: RynnBrain 1.1 — 더 범용적인 임바디드 파운데이션 모델 (2B/9B/122B)
type: source
domain: ai-news
tags: [ai-news, hf-paper, embodied-ai, foundation-model, vla, robotics, 3d-grounding, spatial-reasoning]
created: 2026-07-21
updated: 2026-07-21
sources: []
reliability: medium
---

# RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model

> [!insight] 핵심 인사이트
> **2B / 9B / 122B-A10B** 세 규모의 임바디드(로봇) 파운데이션 모델 패밀리로, **통합 시공간·물리 근거(spatio-temporal & physically grounded) 프레임**으로 학습. 임바디드 지각·공간추론·로컬라이제이션·플래닝을 지원하고, 신규로 **접촉점 예측(contact-point prediction)** 과 소형(2B/9B) **네이티브 3D 그라운딩** 을 추가. 실로봇 평가에서 RynnBrain으로 초기화한 **VLA(Vision-Language-Action) 정책이 여러 로봇 embodiment에서 경쟁 기법을 상회**하며, 통합 **81차원 행동공간 + embodiment별 마스킹**(RynnBrain-VLA)으로 휴머노이드·양팔·다지손 등 이종 로봇에 배포. VSI-Bench·MMSI·RefSpatial-Bench SOTA, 파라미터 스케일에 따른 능력 상승 곡선 확인. [[임바디드-AI]]·[[Xiaomi-Robotics-VLA-Scaling]]·[[LaMem-VLA]] 계보의 최신 항으로, **"규모별 임바디드 FM 패밀리 + 다중 embodiment VLA"** 를 정면으로 다룸.

## 도메인별 추출 (ai-news / slam-3dgs·임바디드 교차)

- **신뢰도**: ⭐⭐⭐ — WebFetch로 초록·구조 실확인(2B/9B/122B·접촉점·3D그라운딩·81차원·VSI/MMSI/RefSpatial 등 구체). 미래형 ID(2607.17977)로 원문·재현 미검증 → medium. 업보트 28.
- **즉시 활용**: NO — 로봇 파운데이션 모델(하드웨어 필요). 내 작업과 직접 접점은 낮으나, **네이티브 3D 그라운딩·공간추론**은 [[slam]]/[[3dgs]] 인지 스택과 개념적 교차.
- **6개월 영향력**: 중간 — 임바디드 FM이 "단일 모델"에서 **규모별 패밀리 + 다중 embodiment 통합 행동공간**으로 성숙. VLA가 로봇별 재학습 없이 이식 가능해지는 흐름의 사례.
- **대체 관계**: [[Xiaomi-Robotics-VLA-Scaling]](VLA 데이터 스케일링)·[[LaMem-VLA]](이중 메모리 VLA)·[[LingBot-Video]](임바디드 비디오 사전학습)와 같은 임바디드 계열. 차별점은 **접촉점 예측 + 소형 3D 그라운딩 + 81차원 통합 행동공간**.
- **허와 실**: "스케일 커질수록 능력 상승"·다중 embodiment 상회는 자체 실로봇 실험. 122B-A10B급은 로컬·개인 재현 불가, 벤치·실로봇 성공률은 원문 검증 필요.
- **액션**: 원문·모델카드 공개 시 2B/9B 네이티브 3D 그라운딩 방식 확인 → slam-3dgs 인지 스택과의 접점 여부 판단(직접 활용은 유보).

> [!warning] 신뢰도 medium — 미래형 ID·원문 미검증
> arXiv 2607.17977은 초록 수준만 확인. 실로봇 성능·SOTA는 자체 리포트로 독립 재현 전.

## 관련 페이지
- [[임바디드-AI]]
- [[Xiaomi-Robotics-VLA-Scaling]]
- [[LaMem-VLA]]
- [[LingBot-Video]]
- [[slam-3dgs]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.17977 · 업보트 28
- 신뢰도: ⭐⭐⭐ (초록 WebFetch 검증, 미래형 ID·원문 미검증 medium)
