---
title: From Pixels to Words — 대규모 네이티브 단일 비전 모델 연구
type: source
domain: ai-news
tags: [ai-news, VLM, vision, language, pixels, unified-model, one-vision, multimodal, scale]
created: 2026-05-28
updated: 2026-05-28
sources: []
reliability: medium
---

# From Pixels to Words — Towards Native One-Vision Models at Scale

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 이미지 토큰화 없이 픽셀을 직접 처리하여 텍스트를 생성하는 "네이티브 단일 비전 모델" 대규모 학습 연구. 토크나이저 없는 엔드투엔드 접근으로 VLM 복잡도 감소. HF 업보트 48.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — HF 업보트 48, arXiv 2605.28820. 학술 연구 단계
- **즉시 활용**: NO — 학습 파이프라인 연구. 오픈소스 모델 공개 여부 확인 필요
- **6개월 영향력**: VLM이 "패치 임베딩" 없이 순수 픽셀에서 시작하면 해상도 제약·정보 손실 해소 가능. [[PseudoUnification]]과 함께 멀티모달 통합 아키텍처 방향성 시사
- **대체 관계**: ViT 기반 VLM([[Gemma-4-31B]], [[GLM-5V-Turbo]]) 대비 중간 표현 없는 접근 — 단순함 vs 최적화 트레이드오프
- **허와 실**: "네이티브" 픽셀 처리가 계산 비용 증가로 이어질 수 있음. 실제 스케일에서의 효율성 데이터 필요

## 연구 핵심

- **문제**: 기존 VLM은 이미지 토크나이저(패치 분할 → 임베딩) 단계에서 정보 손실
- **방법**: 픽셀 수준 직접 처리 → 텍스트 생성 엔드투엔드 통합
- **의의**: VLM 아키텍처 단순화 + 해상도 유연성 향상

## 관련 페이지

- [[PseudoUnification]] — 통합 멀티모달 모델 엔트로피 프로빙
- [[GLM-5V-Turbo]] — Zhipu AI 비전+언어 통합 모델
- [[Gemma-4-31B]] — Google VLM 멀티모달
- [[Uni-ViGU]] — 영상 생성+이해 통합 단일 프레임워크

## 원본

- 출처: https://huggingface.co/papers/2605.28820
- 업보트: 48 (2026-05-28)
- 신뢰도: ⭐⭐⭐
