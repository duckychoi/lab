---
title: DreamX-Phi 1.0 — 로봇 조작용 행동조건부 비디오 월드모델 (2608.13489)
type: source
domain: ai-news
tags: [ai-news, hf-paper, world-model, video, robotics, manipulation, slam-3dgs, video-saas]
created: 2026-08-14
updated: 2026-08-16
sources: []
reliability: medium
---

# DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

**HF 논문**: https://huggingface.co/papers/2608.13489
**지표**: HF 데일리 **3위** · 업보트 87 (2026-08-16 자동수집) ← 데일리 3위·업보트 80 (08-15) ← 2위·62 (08-14) · **소속**: Alibaba Group (raw 기재)

> [!update] 2026-08-16 갱신 — 업보트 87·데일리 3위 유지
> **업보트 87·HF 데일리 3위 유지**(2026-08-16) ← 80·3위(08-15) ← 62·2위(08-14). 업보트 80→87로 완만 상승하며 상단권 지속 — 행동조건부 비디오 월드모델의 로봇 제어 응용 관심 안정([[slam-3dgs]]×[[video-saas]]·[[임바디드-AI]] 교차 유지). 미래형 ID·원문 미재현·Alibaba 소속 raw 기재 동일. reliability medium 유지.

> [!update] 2026-08-15 갱신 — 업보트 80·데일리 3위
> 재수집에서 **업보트 80·HF 데일리 3위**(2026-08-15) ← 62·2위(08-14). 업보트는 62→80으로 늘었으나 순위는 [[LLMRouter]] 상승에 밀려 2위→3위 — 행동조건부 비디오 월드모델의 로봇 제어 응용 관심 지속([[slam-3dgs]]×[[video-saas]] 교차 유지). 미래형 ID·원문 미재현·Alibaba 소속 raw 기재 동일. reliability medium 유지.

> [!insight] 핵심 인사이트
> **로봇 조작(robotic manipulation)을 위한 행동조건부 비디오 월드모델** — 행동(action) 입력에 따라 미래 프레임을 예측하는 구조(제목·raw 기반). 위키의 [[월드모델]]·[[Diffusion-월드모델]] 계보에서 "예측형 월드모델"을 **로봇 제어 루프에 직접 물린** 사례로, [[SimWAM]](자율주행 월드 액션 모델)·[[Articulated-Object-Reconstruction]](관절형 객체 3D)·[[임바디드-AI]] VLA 흐름과 교차. "행동을 넣으면 그 결과 영상을 상상"하는 구조는 [[EnvACE]] 월드 리허설·[[ChronoVision]] 잠재 동역학과 같은 결이되, **비디오 픽셀 예측을 조작 정책의 시뮬레이터로 쓴다**는 점에서 [[slam-3dgs]]×[[video-saas]](영상 생성이 곧 물리 예측)의 로보틱스 응용 교차점. 데일리 2위·업보트 62·Alibaba 소속(raw)으로 상단 진입.

> [!warning] 신뢰도 medium — 미래형 arxiv ID, 원문 미재현
> 논문 ID 2608.13489는 **미래형(2026-08) arxiv ID로 원문 초록·수치·방법 재현 불가**. 제목·raw 한줄요약·HF 데일리 순위/업보트만 근거이며, **예측 지평·성능 지표·표현 방식(디퓨전/latent 여부)은 미기재**. 소속 "Alibaba Group"은 **raw 기재값으로 원문 대조 전까지 미검증**([[CLAUDE.md]] 사실확인 원칙).

## 도메인별 추출 (slam-3dgs / video-saas / 임바디드-AI 교차)

- **신뢰도**: ⭐⭐ (medium) — HF 데일리 3위·업보트 80(08-15). 원문 미재현·소속 raw 기재.
- **현재 SOTA**: 미확인 — 예측 정확도·조작 성공률 원문 필수.
- **응용 가능성**: 중(개념) — 영상 생성 모델을 "물리 결과 예측기"로 재해석하는 관점은 내 영상 자동화의 물리적 일관성 논의와 개념 접점.
- **6개월 영향력**: 중 — 월드모델이 로봇 제어 시뮬레이터로 수렴하는 흐름([[SimWAM]]·[[HY-World-2.0]] 계보) 강화.
- **허와 실**: "world model"·"1.0" 프레이밍 강함 — 실제 조작 루프 폐쇄 여부·실기 이전은 원문이 가름.
- **필수 레퍼런스**: 원문 공개 시 [[SimWAM]]·[[EnvACE]]와 행동조건 예측 방식 대조.

## 관련 페이지
- [[월드모델]] · [[Diffusion-월드모델]] · [[JEPA]] — 월드모델 계보
- [[SimWAM]] · [[EnvACE]] · [[ChronoVision]] — 행동조건·잠재 동역학 축
- [[Articulated-Object-Reconstruction]] · [[임바디드-AI]] — 로봇 조작·3D 교차
- [[Alibaba]] — 소속(raw 기재)
- [[slam-3dgs]] · [[video-saas]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2608.13489
- 신뢰도: ⭐⭐ (HF 데일리 3위·업보트 80·Alibaba raw 기재, 미래형 ID·원문 미재현)
