---
title: "Clover-35B-A3B-Preview — Gated DeltaNet × 블록 확산의 MoE 확산 언어모델 · RTX 5070 Ti 16GB 97.6 tok/s (arXiv 2611.24636)"
type: source
domain: ai-news
tags: [ai-news, paper, diffusion-lm, moe, gated-deltanet, coding-agent, consumer-gpu, sglang]
created: 2026-11-24
updated: 2026-11-24
sources: [https://huggingface.co/papers/2611.24636]
reliability: medium
---

**논문**: arXiv 2611.24636 · 업보트 **40**(볼트 API 11-24 · 수집기 11-23 32) · 11-23 데일리 3위 · 소속 Diffuspace · 코드 https://github.com/DiffuSpace/Clover-35B-A3B-Preview (★161) · 가중치 공개 여부는 레포에서 미확인

## 핵심 인사이트
> [!insight] 이미 만든 문맥은 순환 메모리로, 지금 블록만 양방향 어텐션 — 자기회귀를 버린 코딩 에이전트 모델
> 총 35B · 활성 3B **MoE 확산 언어모델**(자기회귀 아님), 사고 모드 지원. 이미 생성한 문맥은 Gated DeltaNet 순환 메모리로, 현재 블록 안은 양방향 softmax 어텐션 — 둘을 같은 softmax 에서 경쟁시키는 구조.

> [!warning] 에이전트 7지표 1위, 그러나 지식 · 수학 · 경쟁 코딩은 Qwen에 밀린다
> **본문 표 1(자체 측정)**: 에이전트 7지표 전부 1위 — SWE-bench Verified **73.6**(Mercury 2.5 65.8 · Qwen3.6-35B-A3B 61.4) · Terminal-Bench 2.1 **51.7** · τ³ 65.3 · BFCL-v4 67.9 · IFBench 72.3 · AA-LCR 72.0 · GPQA-D 83.8. 🔴 **지는 행(같은 표)**: HLE 12.8 vs Qwen3.5-35B-A3B 21.6 · Qwen3.6 21.2, AIME 2026 83.3 vs 90.4, MATH-500 96.2 vs 97.2, MMLU-Pro 84.8 vs 85.2, LiveCodeBench v6 72.6 vs 74.3, SciCode 30.9 vs Qwen3.6 31.3. **"평가 전부 in-house" 명시 — 외부 재현 전**([[비매칭-비교]] 아님 · 그러나 자체 측정). 볼트 11-24 본문 HTML 문자열 검증 통과(73.6 · 51.7 · 680 · 97.52 · 106.25 전부 적중).

## 도메인별 추출 (ai-news)
- **소비자 GPU 수치(표 4)** — 이 배치의 가장 실용적인 행: **RTX 5070 Ti 16GB + CPU 하이브리드**(SGLang + KTransformers, INT4)에서 MATH-500 전체 **97.6% · 97.52 tok/s**(expert 배치 최적화 top-8) / top-6 으로 줄이면 **106.25 tok/s · 96.0%**. 같은 조건 Qwen3.6-35B-A3B 는 93.8% · 47.04 tok/s. GB300 1장 BF16 배치1 내부 에이전트 워크로드 680 tok/s(자칭).
- **즉시 활용**: 조건부 — 16GB 에서 돌아가는 35B-A3B 코딩 에이전트 후보로 가장 직접적인 논문이나 **가중치 공개가 전제**. 코드 ★161, 가중치 공개 여부 미확인 → actionable 로 조건부 등재.
- **확산 LM 동향**: 자기회귀 대체 후보가 "텍스트 생성"에서 "에이전트 워크로드"로 주장 지점을 옮김 — 순차 디코딩의 KV캐시 병목([[Mooncake]]이 풀는 문제)을 구조적으로 우회하려는 시도로 읽을 수 있다.
- **액션**: 가중치 공개 확인 후 시험(actionable 등재).

## 관련 페이지
- [[Edge0-35B-A3B-preview]] · [[mini-swe-agent]] · [[Mooncake]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.24636
- 확인 범위: HF papers API(업보트 · 조직 · githubRepo — 볼트 11-24) · 🔴 **본문 HTML 직접 판독** — 표 1 · 4 수치 5개 문자열 검출 통과(수집기 11-23 표 판독과 일치) · 가중치 공개 여부 레포 미확인 · 실행 0
- 신뢰도: ⭐⭐⭐
