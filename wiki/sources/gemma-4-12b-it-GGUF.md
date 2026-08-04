---
title: gemma-4-12b-it-GGUF
type: source
domain: ai-news
tags: [gguf, local-llm, gemma, google, unsloth, quantization, multimodal, llama-cpp]
created: 2026-06-09
updated: 2026-06-10
sources: []
reliability: high
---

# gemma-4-12b-it-GGUF (unsloth)

## 핵심 인사이트

> [!insight] Gemma-4 12B의 로컬 실행 표준화 — unsloth GGUF가 구글 모델 접근성 혁신
> Gemma-4 12B 인스트럭션 튜닝 모델의 GGUF 양자화 버전. unsloth 최적화 + llama.cpp·Ollama 호환으로 일반 PC에서 Google 최신 멀티모달 모델 실행 가능.

## 도메인별 추출

**스펙:**
- HF 660,000 다운로드 (2026-06-10; 이전 660,140 2026-06-09) — 급속 확산 유지
- unsloth 최적화 GGUF: Q4_K_M, Q8_0 등 다양한 양자화 레벨
- llama.cpp, Ollama, LM Studio 모두 호환
- Gemma-4의 any-to-any 멀티모달 능력을 로컬에서 활용 가능

**포지셔닝:**
- [[Qwen3.6-35B-A3B-GGUF]]에 이어 unsloth GGUF 포맷이 대형 모델 로컬 실행 표준으로 굳어지는 흐름
- Google 공식 모델([[gemma-4-12B-it]])의 로컬 실행 최적화 버전
- 18GB RAM 이하 환경에서 12B 멀티모달 실행 가능

> [!action] Ollama로 gemma-4-12b-it GGUF 설치 후 Gemma-4-31B 대비 성능/속도 비교

## 관련 페이지
- [[gemma-4-12B-it]]
- [[Qwen3.6-35B-A3B-GGUF]]
- [[Gemma-4-31B]]
- [[gemma-4-e4b-obliterated]]

## 원본
- 출처: https://huggingface.co/unsloth/gemma-4-12b-it-GGUF
- HF 660,000 다운로드 (2026-06-10)
- 신뢰도: ⭐⭐⭐⭐⭐
