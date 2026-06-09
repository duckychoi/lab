---
title: SANA-WM — 효율적 분 단위 세계 모델링 (하이브리드 선형 확산 트랜스포머)
type: source
domain: ai-news
tags: [ai-news, video-saas, world-model, diffusion-transformer, nvidia, time-series, efficiency]
created: 2026-05-15
updated: 2026-05-15
sources: []
reliability: medium
---

# SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

> [!insight] 핵심 인사이트
> NVIDIA의 **하이브리드 선형 확산 트랜스포머**로 분 단위 시계열 세계 모델링을 효율적으로 처리. 기존 Transformer O(n²) 복잡도 한계를 선형 복잡도로 극복 — 장시간 비디오/시계열 월드 모델 생성에 직접 적용 가능. 업보트 41.

## 도메인별 추출 (ai-news + video-saas)

- **신뢰도**: NVIDIA 연구. HuggingFace 업보트 41. arXiv 2605.15178. ⭐⭐⭐
- **즉시 활용**: 아직 학술 단계. 구현체 공개 여부 확인 필요
- **6개월 영향력**: 분 단위 세계 모델이 가능해지면 [[Sulphur-2-base]], [[Seedance]] 등 T2V 모델의 지속시간 한계를 돌파. 영상 SaaS의 긴 영상 생성 기능 토대
- **대체 관계**: [[RLDX-1]], [[Stream-T1]]과 함께 "장시간 비디오 생성 인프라" 연구군 형성
- **선형 확산 트랜스포머 의의**: [[Mamba4]](SSM 계열)와 유사한 방향 — Transformer 이분법을 넘어 선형 복잡도 하이브리드 아키텍처가 대안으로 부상
- **액션**: NVIDIA 공식 레포 확인 후 추론 비용 vs 품질 트레이드오프 데이터 확보

> [!note] 배경 정보
> SANA 시리즈(NVIDIA 이미지 생성 모델) 후속 세계 모델 버전. 이미지→분 단위 비디오 세계 모델로 확장한 연구.

## 관련 페이지

- [[Mamba4]] — SSM 기반 선형 복잡도 아키텍처
- [[Sulphur-2-base]] — 오픈소스 T2V 모델
- [[Seedance]] — ByteDance 영상 AI SaaS
- [[AI-영상-생성-2026]] — 영상 AI 생태계 지형도

## 원본

- 출처: https://huggingface.co/papers/2605.15178
- arXiv: 2605.15178
- HuggingFace 업보트: 41 (2026-05-15)
- 신뢰도: ⭐⭐⭐ (NVIDIA, 업보트 41)
