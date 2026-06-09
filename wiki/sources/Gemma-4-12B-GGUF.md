---
title: unsloth/gemma-4-12b-it-GGUF — Gemma 4 12B 로컬 추론 최적화 양자화 버전
type: source
domain: ai-news
tags: [ai-news, huggingface-model, gemma, google, gguf, quantization, local-llm, unsloth, 12B]
created: 2026-06-06
updated: 2026-06-08
sources: []
reliability: high
---

# unsloth/gemma-4-12b-it-GGUF — Gemma 4 12B GGUF 양자화

**HuggingFace**: https://huggingface.co/unsloth/gemma-4-12b-it-GGUF  
**다운로드**: 645,000 (2026-06-08 기준, prev 458,000)  
**기반 모델**: [[Gemma-4-12B]] (google/gemma-4-12B-it)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> Gemma 4 12B 인스트럭션 튜닝 모델의 GGUF 양자화 버전. **DL 458,000** — Google의 12B 멀티모달 모델을 로컬(llama.cpp, Ollama 등)에서 실행하려는 수요 폭발적. unsloth 특유의 메모리 최적화 적용으로 일반 GGUF 대비 효율 개선.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — unsloth 공식 양자화, DL 458,000, Ollama/llama.cpp 생태계 검증
- **즉시 활용**: YES — `ollama run gemma4:12b` 또는 llama.cpp로 즉시 실행. 텍스트·이미지 입력 가능
- **6개월 영향력**: 12B 멀티모달 모델의 로컬 실행 기준점. [[project-nomad]] 같은 오프라인 AI 시스템에서 메인 모델로 활용 가능
- **대체 관계**: Qwen3 계열·Llama 계열 로컬 모델 대비 Google 공식 멀티모달 + 한국어 능력
- **허와 실**: 양자화로 인한 성능 저하 — Q4 vs Q8 vs F16 비교 필요. 이미지 입력 시 GGUF 포맷에서 멀티모달 완전 지원 여부 확인 필요

> [!action] 당장 할 것
> Ollama로 gemma-4-12b-it Q4 로컬 실행 테스트. 이미지 입력 테스트 후 [[Gemma-4-31B]] 대비 성능/속도 비교.

## 관련 페이지

- [[Gemma-4-12B]] — 원본 모델
- [[Gemma-4-31B]] — 더 큰 Gemma 4 버전
- [[project-nomad]] — 오프라인 AI 시스템
- [[open-notebook]] — 로컬 배포 NotebookLM 대체재

## 원본

- 출처: https://huggingface.co/unsloth/gemma-4-12b-it-GGUF
- 다운로드: 458,000 (2026-06-06 기준)
- 신뢰도: ⭐⭐⭐⭐⭐
