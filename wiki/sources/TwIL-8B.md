---
title: "webAI-Official/TwIL-8B — Granite 4.2 8B 를 SFT+GRPO/DAPO+길이 인식 RL 로. MATH-500 98.2 · LCB 81.6(verbose 측정), GPQA 70.2 는 Qwen3.5-9B 아래, 상업 이용 불가"
type: source
domain: local-llm
tags: [local-llm, slm, hf-model, reasoning, gguf, granite, grpo, dapo, non-commercial, webai]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/webAI-Official/TwIL-8B]
reliability: medium
---

**HF**: [webAI-Official/TwIL-8B](https://huggingface.co/webAI-Official/TwIL-8B) · dl30 **22,737**(볼트 11-09 · 수집기 15,324 → **+7,413/1일, +48%**) · ♥243 · trending 238 · license **webAI Non-Commercial 1.0**(베이스 Apache-2.0) · base `ibm-granite/granite-4.2-8b` · 8,791,592,960 파라미터 · created **2026-10-14**(수집기 미기재)

## 핵심 인사이트
> [!insight] 두 변형 = 같은 가중치 구조, 다른 RL 단계 — 점수는 verbose, 기본값은 balanced
> SFT → GRPO/DAPO(verbose) → 길이 인식 RL(**balanced, 기본**). 카드 표에서 † 표시(LiveCodeBench 81.6 · IFBench 74.4 · MMLU-Pro 76.5 · HLE 12.6)는 **verbose 로 측정** — 기본 배포 변형의 값이 아니다([[비매칭-비교]]). 토큰 효율: AIME 2026 문제당 ~19.5k(Qwen3.5-9B 31.2k).

> [!warning] 약점과 조건 (카드 grep 전건 검출)
> GPQA Diamond **70.2**(Qwen3.5-9B 81.7) · AIME 2026 88.3 < Qwen3.5-9B 92.5 · HMMT Feb 2026 68.2. 경쟁 모델 수치는 **공개치 인용, 재실행 안 함**. 카드 스스로 "지식형 모델 아님" · 안전 튜닝은 베이스 수준.

## 도메인별 추출 (local-llm)
- **실용성**: Q4_K_M GGUF **4.98GiB** → CPU·8GB GPU. bf16 16.38GiB
- **Hermes 적용**: NO(상업 불가 라이선스) — 개인 실험용 수학·코딩 추론기로만
- **트레이드오프**: 수학·코딩↑ / 지식(GPQA)↓ / 상업 불가
- **오픈소스 구현체**: 가중치 공개(비상업)

## 관련 페이지
- [[Qwen3.5-9B]] · [[Gemma-4-31B]] · [[비매칭-비교]] · [[PLatour]](같은 배치 소형 모델 축) · [[LFM3-1.7B]](11-07 소형)

## 원본
- 출처: https://huggingface.co/webAI-Official/TwIL-8B
- 확인 범위: HF API(볼트 11-09) · 카드 raw grep(19개 수치 중 18 검출 · 131072 는 리터럴 미검출)
- 신뢰도: ⭐⭐ (dl 2.3만 · 자체 측정 · 비교치 인용)
