---
title: HY-World-2.0
domain: ai-news
type: source
source_type: huggingface
url: https://huggingface.co/tencent/HY-World-2.0
date_ingested: 2026-04-22
tags: [3d-generation, image-to-3d, world-model, tencent, slam-3dgs]
---

# HY-World-2.0

## 개요
Tencent의 Image-to-3D 월드 모델. 이미지·영상에서 3D 월드를 생성. 출시 1시간 만에 534 likes로 트렌딩 4위 진입.

- **제작**: Tencent
- **likes**: 534 (출시 당일, 2026-04-22)
- **HF 트렌딩**: 4위 (출시 당일)

## 핵심 특징
- 이미지 → 3D 월드 생성
- 영상(video) → 3D 재구성 지원
- 단일 뷰에서 완전한 3D 월드 모델 생성

## SLAM 연관성
- 단일 이미지 3D 재구성 → monocular SLAM의 prior로 활용 가능
- 3D Gaussian Splatting 렌더링과 결합 시 novel view synthesis 강화
- [[AnyRecon]]과 유사한 sparse-view 3D 재구성 계열

## 연관 개념
- [[3DGS-SLAM]]
- [[novel-view-synthesis]]
- [[world-model]]
- [[image-to-3d]]
- [[AnyRecon]]
