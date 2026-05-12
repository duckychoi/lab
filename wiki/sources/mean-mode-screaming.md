---
title: Mean Mode Screaming — 1000층 Diffusion Transformer 안정화 기법
type: source
domain: ai-news
tags: [ai-news, hf-paper, diffusion-transformer, dit, training-stability, deep-network, mv-split-residuals]
created: 2026-05-11
updated: 2026-05-11
sources: []
reliability: high
---

# Mean Mode Screaming: 1000층 DiT 학습 안정화

> [!insight] 핵심 인사이트
> Diffusion Transformer(DiT) 수백 층 학습 시 발생하는 **평균 지배 붕괴(Mean Mode Screaming, MMS)** 현상을 최초 규명. **MV-Split Residuals** 기법으로 1000층 DiT의 안정적 학습 달성. 영상 생성(T2V) 모델이 깊어질수록 만나는 근본 문제를 해결 — [[Stream-R1]], [[Stream-T1]], [[RLDX-1]] 같은 대형 DiT 기반 영상 AI의 스케일업 경로를 여는 연구.

## 도메인별 추출 (ai-news)

- **신뢰도**: arXiv 2605.06169 — 실험 수치 구체적 (1000층 달성)
- **즉시 활용**: NO (연구 참조용) — DiT 기반 영상 생성 모델 직접 훈련하는 경우라면 필수 참조
- **6개월 영향력**: DiT 기반 영상 생성 모델(Sora 류)의 깊이 확장 한계를 해제. 더 깊은 모델 → 더 좋은 영상 품질 경로 열림
- **대체 관계**: 기존 LayerNorm/RMS Norm 조합으로 해결 안 되던 심층 DiT 불안정성 문제를 직접 타겟

## 핵심 내용

### MMS (Mean Mode Screaming) 현상
- 깊은 DiT에서 특정 채널의 평균(mean)이 점점 지배적이 되어 학습이 붕괴하는 현상
- 잔차 연결(residual connections)이 깊어질수록 평균값이 누적·증폭

### MV-Split Residuals
- Mean(평균)과 Variance(분산) 경로를 분리하여 잔차 전파
- 평균 성분이 누적되지 않도록 구조적으로 차단
- 1000층 DiT에서 안정적 수렴 확인

> [!note] 배경 정보
> DiT(Diffusion Transformer)는 Sora, Stable Diffusion 3, [[UniVidX]], [[Edit-R1]] 등 최신 영상/이미지 생성 모델의 핵심 아키텍처.

## 관련 페이지
- [[Stream-R1]]
- [[Stream-T1]]
- [[RLDX-1]]
- [[UniVidX]]
- [[Edit-R1]]
- [[AI-영상-생성-2026]]

## 원본
- 출처: https://arxiv.org/abs/2605.06169
- 신뢰도: ⭐⭐ (arXiv 논문)
