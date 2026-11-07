---
title: "LiquidAI LFM3-1.7B — 컨볼루션·SWA·글로벌 어텐션 삼중 하이브리드 1.7B 에이전트 모델. 9B 를 도구 사용에서 이기고 지식·장문에서 진다"
type: source
domain: local-llm
tags: [local-llm, hf-model, slm, edge-ai, liquid-ai, hybrid-architecture, agent, tool-use, on-device, 256k-context]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/LiquidAI/LFM3-1.7B, LFM2.5-8B.md]
reliability: medium
---

**HF**: [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) · 다운로드 **66,003(30일 = 누적)**(볼트 11-07 · 수집기 11-06 60,681 → +5,322/1일) · ♥1,532 · trendingScore 218 · license `other` = **LFM Open License v1.0**(연매출 1,000만 달러 이상 기업은 상업 이용 제한 — 수집기 LICENSE 5절) · base `LiquidAI/LFM3-1.7B-Base` · 1,728,801,536 파라미터 · created 10-23 · sha `0dc4268b`(lastModified 11-03) · `custom_code`

## 핵심 인사이트
> [!insight] 1.7B 가 9B 를 "에이전트 행동"에서 이기는 것은 사후학습 표적의 결과다
> 24층 = **gated short conv 13 · sliding-window attention 5 · global attention 6** · 컨텍스트 256K · 어휘 128K · 16개 언어(한국어 포함). Hermes Agent · Pi · OpenClaw 같은 **에이전트 하니스용으로 사후학습**했다. 4비트 약 1 GB. 카드 Benchmarks 표(대조 `Qwen3.5 9B`, 볼트 grep 전건 검출): `AutomationBench (public)` **41.29 vs 15.10** · `WebArena-Verified` 38.42 vs 28.94 · `BFCL V4` 71.39 vs 62.83 · `IFBench` 73.03 vs 48.84. 반대로 `GPQA Diamond` **63.37 vs 80.40** · `RULER 128K` **65.56 vs 87.11** · `SWE-bench Verified (OpenCode)` 43.40 vs 51.20. **지식·장문 기억은 크기를 못 이기고, 도구 호출·지시수행은 학습 표적으로 이긴다** — 사용자의 로컬 에이전트(Hermes/ChinameBot) 백엔드 선택 기준과 정확히 맞물리는 분해다.

> [!warning] 1위로 보이는 칸 중 하나는 기권 효과다
> - `AA-Omniscience (public)` **0.50(6모델 중 1위)** 는 정확도가 아니다 — 같은 표 `accuracy` **7.07(6모델 중 최하)** · `non-hallucination` 92.93. **모르면 답하지 않아서** 얻은 점수다 → [[복합지표-분해]].
> - `Average` 49.37 vs 47.24 는 표 전체 단순평균(음수 가능 지표 포함).
> - 카드는 *"not recommended for agentic coding"* 이라 적으면서 SWE-bench 를 보고한다(볼트 grep 1건).
> - 엣지 속도 주장(32K 에서 prefill ≥2.5배 · decode ≥1.8배)은 **LFM3 만 LFM3 지원 llama.cpp 빌드, 비교 모델은 릴리스 b11744** — 빌드가 다르다(수집기 기준 · 그림 미판독) → [[비매칭-비교]].
> - 평가 조건: vLLM BF16 · 풀 컨텍스트(LFM3·Qwen3.5 262,144 / 나머지 131,072) · temperature 0.6/top_p 0.95(BFCL 등 일부 greedy).

## 도메인별 추출 (local-llm)
- **실용성 판단**: 4bit ~1 GB · BF16·FP8·NVFP4·GGUF·MLX-4bit·ONNX 제공 — 휴대폰·라즈베리파이급까지 실배포 가능. 지연 수치는 그림에만 있음(미판독).
- **메모리 아키텍처**: conv + SWA 로 KV 캐시를 줄이고 글로벌 6층만 전체 어텐션 — 256K 를 싸게. 단 RULER 128K 65.56 은 장문 회상이 약하다는 뜻.
- **Hermes 적용**: **YES(실험)** — 도구 호출(BFCL 71.39)·지시수행(IFBench 73.03)이 9B 급 이상이라 ChinameBot 의 라우팅/도구 선택 경량 모델 후보. 지식 질의·장문 요약은 큰 모델에 넘겨야 한다.
- **트레이드오프**: 1.7B vs 9B — 에이전트 +, 지식 −17, 장문 −21.
- **오픈소스 구현체**: 가중치 + SFT·DPO·GRPO·CPT 파인튜닝 노트북. 라이선스는 연매출 1천만 달러 미만이면 상업 이용 가능(개인 사용 무관).

## 관련 페이지
- [[LFM2.5-8B]] (전세대 MoE) · [[Mamba4]] (하이브리드 아키텍처) · [[OpenClaw-Foundation]] · [[NousResearch]] (Hermes Agent)
- [[복합지표-분해]] · [[비매칭-비교]] · [[하네스-설계-축]] · [[Qwen]]
- 같은 날 모델: [[Qwen3.5-4B-3D-Coder]] · [[DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF]]

## 원본
- 출처: https://huggingface.co/LiquidAI/LFM3-1.7B
- 확인 범위: HF API expand(볼트 11-07) · 카드 raw 606행 grep(표 수치 12개 + "not recommended" 검출) · LICENSE 5절·평가 조건·엣지 속도는 수집기 기준 · 그림 미판독 · 실행 0회
- 신뢰도: ⭐⭐ (Liquid AI 공식 · 자기측정 표 · 대조군 1개)
