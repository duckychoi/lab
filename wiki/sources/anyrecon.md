---
title: AnyRecon — Arbitrary-View 3D Reconstruction with Video Diffusion Model
type: source
domain: slam-3dgs
tags: [slam-3dgs, 3d-reconstruction, video-diffusion, novel-view-synthesis, sparse-view]
created: 2026-04-22
updated: 2026-04-22
sources: []
reliability: medium
---

# AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model

**출처**: https://huggingface.co/papers/2604.19747
**HF 데일리**: 3위 (2026-04-22), upvote 24

## 핵심 인사이트

> [!insight] 비디오 디퓨전 모델로 단일/희소 시점 → 고품질 3D 재구성
> 임의 시점(Arbitrary-View)에서 3D 재구성 수행. 단일 이미지나 희소 뷰(sparse view)만으로도 비디오 디퓨전 모델의 시공간 일관성을 활용해 3D 구조 추론. 별도 3D 학습 없이 비디오 디퓨전의 사전 지식 활용이 핵심.

## 도메인별 추출

### slam-3dgs 템플릿

**현재 SOTA**: 단일 이미지 3D 재구성 — ZeroNVS, Zero123 계열 대비 임의 시점 자유도 향상
**실시간 가능성**: 디퓨전 기반이므로 배치 처리 위주. 실시간 SLAM 수준 아님.
**카메라 파이프라인**: 단일 이미지 입력 → 비디오 디퓨전으로 멀티뷰 생성 → 3D 재구성
**응용 가능성**: 제품 사진 → 3D 모델 자동 생성 (이커머스, 게임 에셋). [[Meshy]], [[Tripo]] 대비 추가 학습 없이 범용 활용 가능 가능성.
**필수 레퍼런스**: 비디오 디퓨전 3D 재구성 계열 — CAT3D, ViewCrafter 연구 흐름.

> [!note] 배경
> 3DGS([[GlobalSplat]])가 피드포워드 패스 3D 재구성을 추구하는 반면, AnyRecon은 디퓨전 기반 생성적 접근. 두 방향이 수렴하면 실시간 + 고품질 3D 재구성 가능해짐.

> [!question] 미해결 질문
> - [[GlobalSplat]] 대비 품질/속도 트레이드오프는?
> - 코드 공개 여부?

## 관련 페이지

- [[AI-3D-생성]]
- [[GlobalSplat]]
- [[Meshy]]
- [[Tripo]]
- [[HY-World-2.0]]

## 원본

- 출처: https://huggingface.co/papers/2604.19747 (arXiv 2604.19747)
- 신뢰도: ⭐⭐ (미심사 arXiv, HF 데일리 3위)
