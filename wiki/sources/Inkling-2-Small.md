---
title: "Inkling-2-Small — Thinking Machines 594B(활성 17B) 멀티모달 MoE, 1M 컨텍스트"
type: source
domain: local-llm
tags: [local-llm, ai-news, hf-model, moe, multimodal, nvfp4, open-weights, thinking-machines]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/thinkingmachines/Inkling-2-Small]
reliability: high
---

**모델**: thinkingmachines/Inkling-2-Small · 다운로드 **55,885**(수집기 11-24) → **67,132**(볼트 API 11-25) · 좋아요 1,454 → **1,480** · trendingScore 88(트렌딩 24위) · HF 내부 ID `6aeb8ca9…`(일치 확인) · Apache-2.0(+별도 AUP) · safetensors **594,050,672,720**(일치 확인) · 생성 2026-11-04

## 핵심 인사이트
> [!insight] NVFP4로 사전학습부터 — 저정밀이 "양자화 단계"가 아니라 "학습 형식"이 된 원본
> 볼트 [[Inkling]] · [[Inkling-2-Mini-GGUF]] 의 상위 모델. 48층 디코더, 384 expert 중 8 라우팅, 국소/전역 하이브리드 어텐션, 텍스트 + 이미지 입력 → 텍스트, 컨텍스트 1M. **NVFP4로 사전학습부터 학습**(원본 정밀도). 단 NVFP4 체크포인트도 **총 VRAM 500GB 이상(B300 2장 또는 H200 4장)**, MXFP8은 800GB — 로컬 단일 GPU 불가. SGLang · vLLM · TokenSpeed · Unsloth 지원, Together · Baseten · Cloudflare 등 API 제공. [[파라미터-다중표기]] 사례 — 594B 총계 vs 활성 17B.

> [!note] 카드 비교표(13개 모델 — 행 · 열 귀속 확인, 수집기 11-24)
> **강점**: BrowseComp 90.2%(표 최고), AA-Omniscience 비환각률 73.3%(최고), ARC-AGI-2 81.7(Gemini 3.8 Flash 89.2 다음), HLE-Diamond 28.7, DesignArena 4종 최고. **지는 행 — 같은 체급 DeepSeek-V4.1-Flash-1017(16B/552B)에**: AA Index 30.6 vs 32.6 · Vals 56.1 vs 61.3 · DeepSWE 72.1 vs 77.0 · Terminal Bench Science 5.7 vs 12.9 · Vibe Code 81.6 vs 87.7 · GDPVal 1630 vs 1746 · Tax Agent 38.9 vs 44.4 · ArxivMath 27.7 vs 38.3. HLE(텍스트) 44.1 < MiniMax-M3.1-Flash 48.0. 안전성: **FORTRESS(benign) 79.7%로 13개 중 최저**(나머지 84.0–97.4) — 무해 요청 처리율이 낮아 과잉 거부 가능성, HoneyBench(낮을수록 좋음) 52.6%는 최저.

## 도메인별 추출 (local-llm)
- **실용성**: API로 쓰는 에이전트 · 검색 · 시각 작업용 오픈웨이트 상위권. 로컬 실행은 불가(500GB+) — 볼트 로컬 축에서는 GGUF 파생([[Inkling-2-Mini-GGUF]]) 쪽만 유효.
- **대체 관계**: 코딩 단독이면 DeepSeek-V4.1-Flash가 카드 수치상 우세 — "범용 상위권 vs 특화 체급" 선택 기준 제공.
- **과잉 거부 주의**: FORTRESS benign 최저(79.7%) — 무해 요청이 막힐 가능성을 카드가 공개. 에이전트 워크플로우에서 거부율은 직접 비용.
- **액션**: 없음(로컬 불가 — API 선택지로만 기록).

## 관련 페이지
- [[Inkling]] · [[Inkling-2-Mini-GGUF]] · [[Thinking-Machines-Lab]] · [[원본-파생-역전]] · [[파라미터-다중표기]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/thinkingmachines/Inkling-2-Small
- 확인 범위: HF API 재확인(볼트 11-25 — dl · 좋아요 · 내부 ID · safetensors 총계 · 생성일 전부 일치) · 모델 카드 비교표(수집기 11-24 — 행 · 열 귀속 확인) · 실행 0
- 신뢰도: ⭐⭐⭐ (카드가 지는 행까지 공개 · 수치 API 검증)
