---
title: Lance — 멀티태스크 시너지 기반 통합 멀티모달 모델 (ByteDance)
type: source
domain: ai-news
tags: [ai-news, multimodal, bytedance, unified-model, multi-task, video-saas]
created: 2026-05-19
updated: 2026-05-28
sources: []
reliability: high
---

# Lance — 멀티태스크 시너지 기반 통합 멀티모달 모델 (ByteDance)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> ByteDance가 개발한 멀티태스크 시너지 통합 멀티모달 모델. 이해·생성 태스크를 하나의 모델에서 동시에 처리 — 각 태스크에 특화된 모델을 따로 두는 기존 파이프라인 대비 단일 모델 통합 효율. [[LLaDA2.0-Uni]], [[Uni-ViGU]]와 같은 "통합 멀티모달" 트렌드의 ByteDance 버전.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: HF 다운로드 2,510, 좋아요 943 (2026-05-28), arXiv 2605.18678, ByteDance 공식 연구 — 신뢰도 높음. 출시 3시간 만에 트렌딩 1위 달성.
- **즉시 활용**: NO — 모델 공개 여부 확인 필요. 연구 논문 단계
- **6개월 영향력**: ByteDance의 멀티모달 통합 방향([[Seedance]], [[OmniShow]], [[cointeract]])이 Lance로 기술적 기반을 확장. 이해+생성 통합이 성숙하면 video-saas 워크플로우(생성 → 이해 → 수정) 단일 모델화 가능
- **대체 관계**: [[LLaDA2.0-Uni]](확산+이해 통합)·[[Uni-ViGU]](영상 생성+이해) 등 통합 모델 경쟁 중 ByteDance의 멀티태스크 접근
- **허와 실**: "멀티태스크 시너지"가 실제로 각 태스크 특화 모델 대비 성능 열세 없는지 확인 필요

## 관련 페이지

- [[LLaDA2.0-Uni]] — 확산 기반 멀티모달 이해+생성 통합
- [[Uni-ViGU]] — 영상 생성+이해 통합 단일 프레임워크
- [[Seedance]] — ByteDance VFX 특화 영상 AI
- [[OmniShow]] — ByteDance 인간-사물 상호작용 영상 생성
- [[AI-영상-생성-2026]] — 영상 AI 전체 지형도

## 원본

- 출처: https://huggingface.co/papers/2605.18678
- 모델: https://huggingface.co/bytedance-research/Lance
- 신뢰도: ⭐⭐⭐⭐ (HF DL 2,510 / 좋아요 943, arXiv 2605.18678, ByteDance, 트렌딩 1위, 2026-05-28)
