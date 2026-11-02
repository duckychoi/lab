---
title: "HiFOR — 단기·이정표·최종목표를 함께 예측하고 행동 표현으로 미래를 골라 읽는 VLA"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, vla, world-model, foresight, libero, robotwin]
created: 2026-11-02
updated: 2026-11-02
sources: [https://huggingface.co/papers/2610.40373]
reliability: medium
---

**HF**: published 2026-10-29 · upvote 19 · Rongxing Ding 외 7인 (HF 조직 표기 없음) · arXiv 2610.40373 · 코드 **없음** (HF `githubRepo` null · 본문에 레포 언급 없음)

## 핵심 인사이트
> [!insight] 예측한 미래를 "통째로 붙이지" 않고 행동이 필요로 하는 부분만 꺼내 쓴다
> 단기 상태 변화 · 의미적 이정표(milestone) · 최종 목표 상태를 계층 의존 마스크(HDM)로 한 번에 예측하고, 그 잠재 표현을 horizon×view×spatial 축으로 정리한다. 디노이징 중인 행동 표현이 이 구조에서 필요한 미래만 검색(AWR)한다. 어블레이션에서 단기 예측 추가가 가장 큰 한 단계(+3.80%p)였고, 검색(AWR)은 +2.45%p였다. 저자가 그린 주의 시각화에서는 작업 단계마다 주로 보는 horizon이 바뀌었다(이정표 60% → 단기 52% → 목표 53%).

> [!warning] "최고 성능"의 실제 폭 — LIBERO는 1.0%p, RoboTwin 기준선은 저자 재현값
> - **LIBERO 평균 98.3%** vs 차순위 **VLA-Adapter 97.3%** → **+1.0%p**. LEAP-VLA·OpenVLA-OFT 97.1%. LIBERO-Object는 **99.2%로 VLA-Adapter와 동률이고, LEAP-VLA(99.4%)보다 낮다**. 본문의 "π0.5 대비 +1.4%p"는 자기 베이스 대비 값이다.
> - **RoboTwin 2.0 (Hard, 20과제 · 과제당 100 rollout) 49.40%** vs **π0.5 40.35%**. 이 π0.5 값은 **† 저자 재현값**이다. 다른 기준선 중 최고는 Spatial Forcing 29.40%다. 본문의 "9.05%"는 상대값이 아니라 **%p**다.
> - 표 1은 20과제 중 **10과제만** 싣고 "전체는 부록"이라고 적었다. 그런데 arXiv HTML에는 부록 표가 없다(미확인).
> - 어블레이션 첫 행이 π0.5 값과 정확히 같다. 따라서 HiFOR는 **π0.5 위에 얹은 모듈**로 읽힌다. 다만 본문에는 "VLA backbone"이라고만 적혀 있다.

> [!warning] 실로봇 · 한계
> 실로봇 실험은 AgileX Piper 6-DoF 단일 팔에서 6과제로 했다. 평균 **81.7% vs π0.5 +11.0%p**이고, 적층 과제에서는 +16.0%p다. 그림에는 "leading models"와 비교한다고 적었지만 **본문 수치는 π0.5 하나만** 비교한다. 과제별 시도 횟수는 HTML 본문에서 확인하지 못했다(그림 4). **한계 절이 없고**, 추론 지연·Hz도 보고하지 않았다. 학습은 H200 8장, 배포는 RTX 4090 1장이다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: LIBERO 98.3% · RoboTwin 2.0 Hard 49.40%(저자 주장). 코드 미공개라 재현할 수 없다.
- **실시간 가능성**: 보고 없음. RTX 4090 1장 배포만 명시했다.
- **카메라 파이프라인**: 손목 + 3인칭 RealSense D435i 2대 · 언어 지시 · 로봇 상태 → VLA 백본 → 계층 예측 → 행동 디노이징.
- **응용 가능성**: 단기 예측 길이(5스텝)를 정책 갱신 주기(5스텝)와 맞췄을 때 가장 좋았다. "예측 horizon = 실행 주기" 정렬은 다른 [[VLA]]에도 그대로 옮길 수 있는 설계 규칙이다. RGB 미래 예측보다 의미 특징 예측이 LIBERO-Long에서 +1.6%p 좋았다.
- **필수 레퍼런스**: π0.5 · RoboTwin 2.0 · LIBERO.

## 관련 페이지
- [[VLA]] · [[월드모델]] · [[임바디드-AI]] · [[GroundingPI]] · [[HiFi-UMI]]
- [[한정어-탈락]] (재현 기준선 · %p 표기) · [[천장-기준선]] (LIBERO 98%대 포화) · [[선언된-구현체-공백]]

## 원본
- 출처: https://huggingface.co/papers/2610.40373
- 확인 범위: HF `api/papers` · arXiv HTML 본문(표 1~3, 4장 본문) · 🔴 20과제 전체 표와 실로봇 과제별 수치는 미확인(부록·그림) · 코드 실행 0회
- 신뢰도: ⭐⭐ (코드 없음 · 소속 미표기 · LIBERO 포화 구간에서 낸 우위)
