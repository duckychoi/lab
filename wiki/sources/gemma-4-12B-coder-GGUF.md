---
title: yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF — Gemma-4 12B 코딩 특화 로컬 양자화
type: source
domain: ai-news
tags: [ai-news, hf-model, gemma, google, gguf, quantization, coding, local-llm, fine-tuned]
created: 2026-06-17
updated: 2026-07-07
sources: []
reliability: medium
---

# gemma-4-12B-coder-GGUF (yuxinlu1)

## 핵심 인사이트

> [!update] 2026-07-07 갱신
> HF DL **674,977** (2026-07-07 자동수집; 이전 614k 2026-07-02, +61k). 60만 돌파 후에도 유입 지속 — 로컬 코딩 GGUF 실사용층 안착. [[gemma-4-12B-agentic-GGUF]](에이전트 특화)와 동반 트렌딩 유지.

> [!insight] Gemma-4 12B 기반 코딩 파인튜닝 GGUF — 로컬에서 바로 쓰는 코딩 특화 양자화 모델
> Gemma-4 12B 베이스에 코딩(fable5) + 작곡(composer2.5) 파인튜닝을 결합한 GGUF 양자화 모델. 로컬 추론 최적화. HF 다운로드 674,977 (2026-07-07).

## 도메인별 추출

**핵심 특징:**
- HF 다운로드: **614k** (2026-07-02) ← 550k (06-29, likes 2,460) ← 536k (06-28) ← 516k (06-26) ← 456k (06-24) ← 147k (06-17). 50만 돌파 후에도 +64k 지속 유입 — HF 트렌딩 다운로드 상위 안착. raw.md의 fable5-composer2.5 변형과 동일 모델. 같은 계열 [[gemma-4-12B-agentic-GGUF]](에이전트 특화, 314k DL로 급증)도 동반 트렌딩.
- GGUF 포맷 → llama.cpp, Ollama, LM Studio 등으로 즉시 로컬 실행
- Gemma-4 12B 베이스 = Google 공식 모델 품질 기반
- 코딩 + 창작(composer) 결합 파인튜닝 → 다용도 로컬 모델

**로컬 LLM 관점:**
- [[Gemma-4-12B]], [[Gemma-4-12B-GGUF]](unsloth 버전)와 비교 필요
- 147k DL = 커뮤니티 검증된 실사용 모델
- [[vllm]]으로 서빙하거나 Ollama로 개인 사용 최적

> [!note] fable5+composer2.5 파인튜닝 조합은 독특 — 코드 생성 + 음악/창작 코드 겸용 가능성

## 관련 페이지
- [[Gemma-4-12B]]
- [[Gemma-4-12B-GGUF]]
- [[LoopCoder-v2]]
- [[local-llm]]
- [[vllm]]

## 원본
- 출처: https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF
- HuggingFace 다운로드: 614k (2026-07-02) ← 549,926 (06-29, likes 2,460) ← 536,130 (06-28) ← 516k (06-26) ← 456k (06-24) ← 147k (06-17)
- 신뢰도: ⭐⭐⭐ (커뮤니티 파인튜닝, 다운로드 614k 지속 증가 — HF 트렌딩 다운로드 상위, 실사용층 안착)
