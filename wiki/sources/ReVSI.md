---
title: ReVSI — VLM 3D 공간 추론 평가 프레임워크 재구성
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, vlm, 3d-reasoning, spatial-intelligence, evaluation]
created: 2026-04-28
updated: 2026-04-28
sources: []
reliability: medium
---

# ReVSI (HF arXiv 2604.24300, upvotes: 36)

> [!insight] 핵심 인사이트
> 비전-언어 모델(VLM)의 3D 공간 추론 능력을 기존 벤치마크들이 부정확하게 측정해왔다는 문제를 지적·수정. "깊이 추정", "물체 위치 관계", "카메라 시점 변환" 등 3D 추론 하위 능력을 분리해 정밀 측정. [[OpenSpatial]]·[[WildDet3D]] 등 3D 공간 이해 연구의 평가 기반을 다시 설계.

**HuggingFace**: https://huggingface.co/papers/2604.24300  
**upvotes**: 36 (2026-04-28 기준)  
**신뢰도**: ⭐⭐⭐ — arXiv 논문, upvotes 36

## 핵심 인사이트

> [!note] 배경 정보
> 기존 VLM 공간 추론 벤치마크들이 2D 시각 정보만으로 답할 수 있는 질문을 "3D 추론"으로 분류해 성능 측정을 오염시킨다는 주장. ReVSI는 순수한 3D 공간 추론만을 요구하는 태스크를 재설계.

> [!action] 당장 할 것
> [[slam-3dgs]] 도메인 연구 시 VLM 3D 이해 능력 평가에 ReVSI 기준 참조. [[HY-Embodied]], [[HiVLA]] 등 로봇 VLA 성능 비교 시 새 기준점으로 활용.

> [!question] 미해결 질문
> 현재 어떤 VLM이 ReVSI에서 최고 성능? GPT-4V, Gemini, Qwen-VL 비교 결과는?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — arXiv, upvotes 36
- **즉시 활용**: 평가 설계 참조용 YES — 실제 코드 공개 여부 확인 후 직접 사용
- **6개월 영향력**: 3D 공간 AI(SLAM, 로봇, 자율주행)가 성장할수록 정확한 VLM 3D 평가 기준의 중요성 증가
- **대체 관계**: [[OpenSpatial]](3D 데이터 엔진), [[WildDet3D]](3D 탐지), [[Spatial-Intelligence-Generative]](생성+추론) — 3D 공간 이해 클러스터 구성
- **허와 실**: 새 벤치마크가 이전 문제를 해결했다고 해도 새로운 측정 편향이 생길 수 있음
- **액션**: 논문 → 데이터셋 공개 여부 → slam-3dgs 도메인 VLM 평가에 적용

## 관련 페이지

- [[OpenSpatial]]
- [[WildDet3D]]
- [[HY-Embodied]]
- [[HiVLA]]
- [[World-R1]]
- [[slam-3dgs]]
- [[Spatial-Intelligence-Generative]]

## 원본

- 출처: https://huggingface.co/papers/2604.24300
- 신뢰도: ⭐⭐⭐
