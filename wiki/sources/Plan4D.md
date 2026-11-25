---
title: "Plan4D — 행동으로 계획 가능한 생성형 4D 월드모델 (arXiv 2611.26516)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, world-model, 4d, scene-flow, model-stitching, depth, video-generation]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.26516]
reliability: medium
---

**논문**: arXiv 2611.26516 · 업보트 **27**(수집기 11-24 — WorldLeague와 단건 동률, 목록 API 순서로 선택) → **29**(볼트 API 11-25) · 소속 표기 없음(githubRepo AMAP-ML/plan4d ★11 — [[Alibaba]] 지도 계열) · 저자 6명

## 핵심 인사이트
> [!insight] 쌍 데이터가 없으면 기성 모델 두 개를 이어 붙인다 — model stitching의 4D 버전
> 관측 장면 + 텍스트 행동으로 미래 RGB 영상과 함께 깊이 · 카메라 · 포인트클라우드 · **장면 흐름(scene flow)** 까지 예측. 쌍 데이터 부족을 [[Depth-Pro-2]] 계열의 3D 재구성(본문은 Depth Anything 3)과 영상 생성(LongCat-Video)을 **이어 붙이고(model stitching)** DPT 헤드로 장면 흐름을 추가해 해결 — 학습 프레임 0.97M으로 비교군(1.36–1.98M)보다 적다. **동결된 본체 2개 + 얇은 헤드** — [[동결-교정층]] 의 교과서적 표본( stitching = 본체 동결 + 접합층만 학습).

> [!warning] 장면 흐름 · 깊이 단독 성능은 전용 모델이 여전히 앞선다
> 본문 표 3(결합 4D 생성): HoiGen 깊이 AbsRel **0.1125** vs TesserAct 1.850 · Gen3R 0.2881, 카메라 RRA@5 0.98–1.00. **지는 행**: 캡션 유사도 HoiGen 0.6854 < VIST3A 0.7851, Chamfer-L1 0.3325 > Gen3R 0.2286, Epic-Kitchens 카메라 RPE-R 0.1568 > TesserAct 0.0946. 표 1 장면 흐름 PointOdyssey EPE 1.22로 V-DPM 0.92 · TraceAnything 0.95보다 나쁨. 표 2 MOVi-F 깊이 δ1 0.8943 vs VGGT 0.9830. 학습은 H100.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA 관계**: 통합(영상+깊이+카메라+흐름)은 앞서지만 각 단일 과제는 전용 모델 열세 — "통합 월드모델"의 현재 상한을 보여주는 표 구성.
- **실용성**: 기성 모델 접합 레시피는 데이터가 적은 상황에서 4D 추출 파이프라인을 만드는 가장 싼 경로 — 단 H100 학습이 전제.
- **액션**: 없음(관찰 — H100급 학습 불가).

## 관련 페이지
- [[Depth-Pro-2]] · [[동결-교정층]] · [[ViDecide]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.26516
- 확인 범위: HF papers API(볼트 11-25 — 업보트 29 · AMAP-ML · githubRepo 일치) · 본문 표 1 · 2 · 3 및 지는 행(수집기 11-24 판독) · 실행 0
- 신뢰도: ⭐⭐ (소속 표기 없음 · ★11 레포 · 자체 결합 벤치 중심)
