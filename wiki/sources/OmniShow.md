---
title: OmniShow — 멀티모달 인간-사물 상호작용 영상 생성
type: source
domain: video-saas
tags: [video-saas, ai-news, video-generation, multimodal, human-object-interaction, bytedance]
created: 2026-04-14
updated: 2026-04-14
sources: []
reliability: high
---

# OmniShow: Multimodal Human-Object Interaction Video Generation

> [!insight] 핵심 인사이트
> ByteDance 발표. 텍스트·이미지·포즈 등 멀티모달 조건을 통합하여 인간이 물체를 사용하는 장면을 일관성 있게 생성. 제품 시연 영상·광고 자동화에 직결되는 기술.

## 핵심 인사이트

> [!action] 당장 할 것
> 제품 데모 영상 자동 생성 파이프라인 구성 시 OmniShow 코드 공개 여부 확인. [[Seedance]]·[[Higgsfield]] 대비 HOI(Human-Object Interaction) 특화 강점 파악.

> [!note] 배경 정보
> [[ByteDance]]([[Seedance]] 개발사)의 연구 부서 발표. 기존 영상 생성 모델이 인간-사물 간 상호작용 일관성을 잘 못 지킨다는 문제를 해결. 예: 손이 컵을 올바르게 쥐는 영상 생성.

## 도메인별 추출 (video-saas 템플릿)

- **기능 벤치마킹**: HOI 특화 생성 — 기존 Runway/Kling 대비 사물 조작 장면 품질 우위 가능
- **크리에이터 인사이트**: 제품 광고·요리 튜토리얼·스포츠 동작 영상에서 즉각 활용 가능
- **프롬프트 패턴**: 멀티모달 조건(이미지+포즈+텍스트) → 일관된 HOI 영상
- **워크플로우**: 레퍼런스 이미지 + 행동 설명 → 자동 영상 생성
- **경쟁 우위 빈틈**: HOI 일관성은 기존 툴의 약점 — 이 분야 특화로 차별화 가능

## 관련 페이지

- [[Seedance]]
- [[Higgsfield]]
- [[AI-영상-생성-2026]]
- [[Uni-ViGU]]
- [[LPM-1.0]]

## 원본

- 출처: https://huggingface.co/papers/2604.11804
- 신뢰도: ⭐⭐⭐ (HF 업보트 35, ByteDance 연구)
