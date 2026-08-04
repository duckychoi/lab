---
title: Linear Attention Architectures — 선형 어텐션 변종 비교와 교차층 값 라우팅(CLVR)
type: source
domain: ai-news
tags: [ai-news, local-llm, linear-attention, deltanet, long-context, architecture]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: medium
---

# Linear Attention Architectures (HF papers 2607.07953)

> [!insight] 핵심 인사이트
> softmax 어텐션 + 최신 선형 어텐션 4종(**DeltaNet·Gated DeltaNet·Kimi Delta Attention·Gated DeltaNet-2**)을 **하나의 순환-메모리 표기로 통일**해 비교한 서베이/방법론. 공통 열쇠는 **델타 규칙** — 값 전체가 아니라 "기존 메모리가 예측 못한 잔차"만 저장, 변종마다 decay gate를 scalar→channel-wise로, erase/write gate를 분리해 세밀화. 결론: **단일 최강 아키텍처는 없다(다목적 프론티어)**. 32k 토큰에서 순수 순환 스택이 softmax 대비 **3.6배 빠른 반복**.

**HF Papers**: https://huggingface.co/papers/2607.07953 (upvote 15)  
**신뢰도**: ⭐⭐⭐ (초록 원문 검증 / 재현·수치 미실측)

## 도메인별 추출

- **신뢰도**: 초록 원문 WebFetch 검증. loss 2.273(KDA) 등 수치는 미재현 → medium
- **즉시 활용**: 직접 배포 아님. 다만 **로컬 LLM 선택 기준**을 준다 — long-context가 중요하면 순수 선형 스택(3.6배 스루풋), loss가 중요하면 하이브리드. [[Qwen3.6-27B]]/[[Qwen3.6-35B-A3B-MTP-GGUF]]의 **Gated DeltaNet+Attention 하이브리드**가 왜 그 구조인지 설명
- **6개월 영향력**: 선형 어텐션이 "실험"에서 "설계 선택지"로 — 로컬/엣지 long-context의 표준 옵션. [[Mamba4]] 계보와 함께 "순환-메모리로의 회귀"를 정당화
- **트레이드오프**: 검증손실 vs 스루풋 vs 옵티마이저 민감도(Muon이 일관 개선하나 다른 LR 필요). 하이브리드는 loss 회복하되 스루풋 희생
- **핵심 기여 CLVR**: **Cross-Layer Value Routing** — write value를 zero-init 투영으로 공유 residual에 흘려보냄. 소폭이지만 일관된 개선(단, 학습이 길어지면 이득 감소 = 저학습 모델에 유효)
- **액션**: 로컬 서빙 모델 고를 때 "hybrid vs pure" 판단 근거로 이 프론티어 참조

> [!note] 배경 정보
> 초기 시도 CLER은 실패(라우팅 잔차가 독립 학습된 값 공간과 경쟁) → 델타 규칙 오차가 아니라 **write value**가 층간 전파 대상이라는 통찰이 CLVR의 핵심.

## 관련 페이지
- [[local-llm]]
- [[Mamba4]]
- [[Qwen3.6-27B]]
- [[Qwen3.6-35B-A3B-MTP-GGUF]]

## 원본
- 출처: https://huggingface.co/papers/2607.07953
- 신뢰도: ⭐⭐⭐ (초록 검증)
