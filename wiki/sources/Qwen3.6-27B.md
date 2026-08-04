---
title: Qwen3.6-27B — Qwen3.6 27B 멀티모달 모델
type: source
domain: ai-news
tags: [ai-news, local-llm, qwen, multimodal, image-text, alibaba]
created: 2026-04-23
updated: 2026-07-10
sources: []
reliability: high
---

# Qwen/Qwen3.6-27B

> [!insight] 핵심 인사이트
> [[Qwen3.6-35B-A3B]](MoE 35B/활성 3B)의 덴스 27B 버전. 출시 후 빠른 성장세로 2.45M 다운로드 돌파. Qwen 시리즈가 오픈소스 멀티모달 기준으로 자리잡은 상태에서 새 크기 버전 추가.

**HuggingFace**: https://huggingface.co/Qwen/Qwen3.6-27B  
**다운로드**: 4,840,000 (2026-07-10 월간 기준, 이전 5,240,000)  
**Likes**: 1,940  
**신뢰도**: ⭐⭐⭐⭐

> [!note] 2026-07-10 갱신 — 아키텍처·벤치 실측, 제작 [[Alibaba]]
> WebFetch 모델카드 실측으로 스펙 확정: **27B 덴스**가 아니라 **Gated DeltaNet + Gated Attention 하이브리드** 아키텍처(hidden 5120·64층), **네이티브 262K 컨텍스트(YaRN로 최대 ~1.01M)**, **Image-Text-to-Text 멀티모달**(텍스트+이미지+비디오). 벤치(카드 명시): **SWE-bench Verified 77.2**·SWE-bench Pro 53.5·MMLU-Pro 86.2·C-Eval 91.4·**AIME 2026 94.1**·MMMU 82.9·**VideoMME 87.7**. "agentic coding" + 반복 개발용 **thinking preservation** 강조, Apache 2.0. 월간 DL 5.24M→**4.84M**(월간 창이라 소폭 감소, 여전히 오픈 멀티모달 최상위권·likes 1,940). → 로컬 배포 시 [[ThinkingCap-Qwen3.6-27B-GGUF]](추론 토큰 -50%)·[[Qwen3.6-27B-NVFP4]](4비트)로 파생 생태계 형성.

## 도메인별 추출

- **신뢰도**: Alibaba Qwen 공식 출시, HF 트렌딩 — 높은 신뢰도
- **즉시 활용**: 이미지+텍스트 이해·생성. [[Qwen3.6-35B-A3B-GGUF]] 대비 GGUF 양자화 버전 대기 중
- **6개월 영향력**: 27B 덴스 모델로 MoE 대비 더 예측 가능한 성능. 로컬 배포 시 VRAM 요구사항 높음
- **Hermes/로컬 LLM**: 24GB VRAM GPU에서 실행 가능 여부 확인 필요 (Q4 양자화 시 약 14-15GB)
- **대체 관계**: [[Gemma-4-31B]](5.1M DL) vs Qwen3.6-27B — 성능 벤치마크 비교 필요

## 관련 페이지
- [[Alibaba]] — 제작사
- [[ThinkingCap-Qwen3.6-27B-GGUF]] — 추론 토큰 -50% 파인튜닝 GGUF(파생, 2026-07-10)
- [[Qwen3.6-27B-NVFP4]] — NVFP4 4비트 양자화(파생)
- [[Qwen3.6-27B-GGUF]] — unsloth GGUF 양자화(파생)
- [[Qwen3.6-35B-A3B]] · [[Gemma-4-31B]] · [[GLM-5.2]]

## 원본
- 출처: https://huggingface.co/Qwen/Qwen3.6-27B
- 아키텍처: Gated DeltaNet+Gated Attention 하이브리드 / 262K(→1M YaRN) / 멀티모달 / Apache 2.0
- 벤치: SWE-bench Verified 77.2 · AIME2026 94.1 · VideoMME 87.7 · MMLU-Pro 86.2
- 다운로드: 4.84M(2026-07-10 월간) · 제작 [[Alibaba]]
- 신뢰도: ⭐⭐⭐⭐ (모델카드 WebFetch 실측)
