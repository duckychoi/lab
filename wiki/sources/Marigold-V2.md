---
title: "Marigold V2 — DiT를 1-step 단안 깊이추정기로 되돌리기"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-paper, depth-estimation, diffusion-transformer, flow-matching, one-step]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# Marigold V2

> [!insight] 핵심 인사이트
> raw는 이것도 `ai-news` 로 넣었지만 **[[slam-3dgs]] 도메인이 맞다** — 단안 깊이추정은 장면 재구성의 입력단이다.
> 기여는 "새 모델"이 아니라 **레시피**: 사전학습된 **다단계 flow-matching DiT**를 **1-step 추론**으로 돌려 SOTA 깊이추정기로 전환한다. 순진한 학습에서 나오는 아티팩트를 진단하고 **두 가지 처방**을 제시 — ①모델 내부 표현을 **GT에서 뽑은 의미 피처와 정렬** ②**Sinkhorn 기반 신규 손실**을 축으로 한 **2단계 파인튜닝**.

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: **KITTI·ETH3D에서 AbsRel 기존 최고 대비 16–26% 개선**(raw가 누락한 핵심 수치). 나아가 **표면 법선 추정·본질 이미지 분해** 등 다른 밀집 회귀 과제에서도 SOTA.
- **실시간 가능성**: **1-step 추론 + 필요시 양자화**로 "cheap to run"을 명시. 다만 **논문이 fps 수치를 제시하지 않는다** → 30fps+ 여부는 **미확인**. DiT 기반이라 단발 추론이어도 백본 크기가 지배할 것.
- **카메라 파이프라인**: 단안 RGB 1장 → 깊이. 별도 센서·스테레오 불요.
- **응용 가능성**: **가장 실질적인 이득은 디테일**이다 — *"resolves **fur, foliage, and hair-thin edges**"*. 3DGS 초기화나 깊이 프라이어가 필요한 파이프라인에서 **경계 품질**이 병목이었다면 직접적 개선.
- **필수 레퍼런스**: **데모 스페이스 즉시 사용 가능** — https://hf.co/spaces/huawei-bayerlab/marigold-v2-web

> [!note] 계보
> "Marigold"는 새 이름이 아니라 **기존 기법의 개정판**(*"we **revisit** Marigold"*). 이미지 생성/편집 모델을 깊이추정기로 **용도 변경(repurpose)** 하는 계열의 2세대. 모델 용량을 보존하면서 실행 비용을 낮추는 것이 설계 목표로 명시됨.

> [!insight] 일반화 가능한 교훈
> *"사전학습 생성모델을 판별 과제로 돌릴 때, 순진하게 학습시키면 특유의 아티팩트가 생기고 — 그 해법은 더 큰 모델이 아니라 **내부 표현을 GT 의미 피처에 정렬**시키는 것"*. [[Representations-Before-Pixels]]·[[Representation-Forcing]] 과 같은 축의 결과.

> [!action] 당장 할 것
> **HF Space에서 내 소스 이미지로 먼저 돌려 본다**(설치 0). 특히 머리카락·잎사귀 경계가 실제로 살아나는지 — 논문의 정성 주장이 내 데이터에서 재현되는지가 채택 판단의 전부.

## 관련 페이지
- [[Representations-Before-Pixels]]
- [[Representation-Forcing]]
- [[WildDet3D]]
- [[OpenSpatial]]
- [[Beyond-Pixels-4D]]

## 원본
- 출처: https://huggingface.co/papers/2609.08084
- 실측(2026-09-09): **업보트 24** · published 2026-09-08 · 저자 9인
- raw 대비 드리프트: 업보트 23 → **24 (+1)**
- 프로젝트: https://hf.co/spaces/huawei-bayerlab/marigold-v2-web
- 신뢰도: ⭐⭐⭐ (HF 데일리 1위 · 정량 개선폭 명시)
