---
title: gemma-4-12B-agentic-fable5-composer2.5-v2-GGUF — Gemma-4 12B 에이전트 특화 양자화
type: source
domain: ai-news
tags: [ai-news, hf-model, gemma, google, gguf, quantization, agentic, local-llm, fine-tuned]
created: 2026-06-25
updated: 2026-07-04
sources: []
reliability: medium
---

# gemma-4-12B-agentic-GGUF (yuxinlu1)

> [!insight] 핵심 인사이트
> HF 다운로드 **343k** (2026-07-04, ← 314k 07-02 ← 165k 06-25; 2일 +29k, 상승세 지속). [[Ornith-1.0-9B]]·[[Qwen3.6-27B-NVFP4]]와 함께 "로컬 에이전트·코딩 모델" 수요가 계속 실측되는 흐름. [[gemma-4-12B-coder-GGUF]]의 **에이전트 작업 특화 형제 모델** — 같은 Gemma-4 12B 베이스에 fable5+composer2.5 파인튜닝을 얹되, **tau2 벤치(에이전트 도구 사용·다단계 작업)에 3.5x 튜닝**한 변형. 코딩 특화판(496k DL)과 에이전트 특화판(165k DL)이 *동시에* 트렌딩하는 것은, 로컬 12B가 "코드 생성"을 넘어 **도구 호출·다단계 작업까지 로컬에서 처리**하려는 수요를 보여준다 — [[hermes-agent]] 류 프레임워크의 로컬 백엔드 후보.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 165k DL로 실사용 진입. 단 tau2 "3.5x" 클레임은 벤치 셋업 의존, 일반화 여부 미검증.
- **즉시 활용**: YES(후보) — GGUF라 llama.cpp/Ollama로 즉시 로컬 실행. [[hermes-agent]]·[[ChinameBot]]의 로컬 도구호출 백엔드로 코딩판보다 적합할 수 있음. 한국어 + function-calling 정확도 테스트 필요.
- **6개월 영향력**: "로컬 12B로 에이전트 돌리기"가 현실화되는 신호. 클라우드 API 의존을 줄이는 [[local-llm]] 핵심 거점.
- **대체 관계**: 클라우드 function-calling API(또는 코딩 특화 [[gemma-4-12B-coder-GGUF]])를 에이전트 용도로 대체/보강.
- **허와 실**: "agentic"·"tau2 3.5x"는 마케팅 위험. 실제 도구호출 성공률·환각률을 직접 측정해야 함. 12B 한계상 복잡 추론은 약할 공산.
- **액션**: 코더판과 동일 환경에서 function-calling 벤치 대조 → 에이전트 용도 우위 확인 시 로컬 백엔드 채택.

> [!note] 배경 정보
> 같은 제작자(yuxinlu1)의 2종 분화: **coder**(코드 생성·496k DL) vs **agentic**(도구 사용·다단계·165k DL). 용도별 파인튜닝이 로컬 모델에서도 표준화되는 흐름.

## 관련 페이지

- [[gemma-4-12B-coder-GGUF]]
- [[Gemma-4-12B]]
- [[hermes-agent]]
- [[local-llm]]
- [[vllm]]

## 원본
- 출처: https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF
- HuggingFace 다운로드: 343k (2026-07-04) ← 314k (07-02) ← 165k (06-25)
- 신뢰도: ⭐⭐⭐ (커뮤니티 파인튜닝, 343k DL로 실사용층 확대, 에이전트 성능 미검증)
