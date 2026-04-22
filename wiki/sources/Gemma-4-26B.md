---
title: Google Gemma 4 26B-A4B — 효율적 MoE 멀티모달 모델 (원본 + GGUF)
type: source
domain: ai-news
tags: [ai-news, hf-trending, google, gemma, MoE, multimodal, local-llm, GGUF, quantization]
created: 2026-04-11
updated: 2026-04-16
sources: []
reliability: high
---

# Google Gemma 4 26B-A4B (+ Unsloth GGUF)

> [!insight] 핵심 인사이트
> 전체 26B이지만 활성 파라미터 4B(A4B) 수준의 MoE 구조. 이미지+텍스트 입력 지원 멀티모달. HF 주간 다운로드 150만+ (원본+GGUF 합산). [[Gemma-4-31B]]과 함께 Gemma 4 패밀리가 멀티모달 로컬 LLM 시장 지배.

## 핵심 인사이트

> [!action] 당장 할 것
> Unsloth GGUF 버전으로 로컬 테스트. 실효 4B 파라미터이므로 일반 게이밍 GPU(RTX 3060 12GB+)에서 실행 가능. 멀티모달 기능 실제 성능 확인.

> [!note] 배경 정보
> **원본**: `google/gemma-4-26B-A4B-it` — HF 다운로드 2,200,000 (2026-04-16)
> **GGUF 경량화**: `unsloth/gemma-4-26B-A4B-it-GGUF` — HF 다운로드 1,523,972 (주간)
> Unsloth의 GGUF 다운로드가 원본을 소폭 초과 → 로컬 실행 수요가 더 높음.
> Apache 2.0 라이선스.

> [!note] Gemma 4 패밀리
> - **31B-it**: 이미지+텍스트, 주간 2M 다운로드 ([[Gemma-4-31B]])
> - **26B-A4B-it**: MoE, 활성 4B, 이미지+텍스트, 주간 1.5M 다운로드 (이 페이지)

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — Google 공식 모델, HF 다운로드 220만+ 검증
- **즉시 활용**: YES — GGUF로 로컬 즉시 실행. Ollama, LM Studio 지원
- **6개월 영향력**: 4B 수준 연산으로 멀티모달 처리 — 엣지 디바이스 배포 가속
- **대체 관계**: [[unsloth/gemma-4-26B-A4B-it-GGUF]], Qwen2.5-VL-7B, LLaVA 계열 대체
- **허와 실**: "활성 4B"는 추론 속도 기준. 메모리 로딩은 전체 가중치 필요할 수 있음
- **액션**: Ollama `ollama run gemma4:26b-gguf` 테스트. 이미지 이해 성능 확인

## 관련 페이지

- [[Gemma-4-31B]] — 같은 패밀리 대형 버전
- [[local-llm]] — 로컬 LLM 도메인
- [[Gemma-4-패밀리]]

## 원본

- 원본 모델: https://huggingface.co/google/gemma-4-26B-A4B-it (1,523,413 다운로드)
- GGUF 버전: https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF (1,523,972 다운로드)
- 신뢰도: ⭐⭐⭐⭐
