---
title: "openbmb/MiniCPM5-2B — 밀집 2B가 4B급 5종을 평균에서 상회"
type: source
domain: local-llm
tags: [local-llm, hf-model, on-device, edge-ai, minicpm, long-context, tool-calling]
created: 2026-09-10
updated: 2026-09-10
sources: []
reliability: medium
---

# MiniCPM5-2B

> [!insight] 핵심 인사이트
> MiniCPM5 계열 2번째 모델인 **밀집(dense) 2B** 트랜스포머. 온디바이스·자원제약 배치 대상.
> 카드 벤치마크 **평균 53.9** 로 동급 2B 3종뿐 아니라 **4B급 5종 전부를 평균에서 상회**한다:
> - 2B급: LFM2.5-2.6B **33.2** · Qwen3.5-2B **28.0** · Gemma-4-E2B-it **24.6**
> - 4B급: Qwen3.5-4B **51.1** · granite-4.2-3B **42.7** · Nemotron-3-Nano-4B **32.6** · Gemma-4-E4B-it **31.2** · LFM2.5-8B-A1B **28.4**
> → 볼트 실측: 카드 SVG 레이더 차트에서 `avg 53.9 / 51.1 / 42.7 / 33.2` 라벨 직접 확인.

> [!note] 📊 이기는 축 — 코딩·장문맥·에이전트
> - **SWE-bench Verified 46.4** vs 차상위 36.8 *(볼트 실측: 표 행 원문 대조)*
> - **NoLiMa 68.1** vs 차상위 43.5 — **장문맥 격차가 최대**. 나머지 비교군은 0.5~17.1로 **사실상 붕괴**
> - **τ²-Bench Telecom 97.1** · **LiveCodeBench v6 69.1**
> - **AIME 2025/2026 86.5 / 86.5** · **BrowseComp-ZH 43.5**
> - **GAIA Text-103 88.7** vs 차상위 78.6
> - **LCB-Pro Medium 17.5** — 비교군 대부분 **0.0**

> [!warning] 📊 지는 축 — 누락 금지 (09-09 규칙 적용)
> **일반지식·지시이행에서 진다:**
> - MATH-500 94.6 **vs Qwen3.5-4B 99.0**
> - MMLU-Pro 70.8 **vs 78.0** · MMLU-Redux 84.7 **vs 88.7**
> - GPQA-Diamond 70.2† **vs 77.1†** · SuperGPQA 40.8 **vs 52.8**
> - **SWE-bench Pro 14.4 vs 28.2** *(볼트 실측 확인)* — Verified에서 이기고 **Pro에서 절반으로 진다**
> - Terminal-Bench v2.1 8.6† **vs 25.8†** · LongBenchPro 44.8 **vs 58.4** · AA-LCR 59.0† **vs 61.0†**
> - 🔴 **지시이행은 더 작은 모델에도 진다** — **IFEval 86.7 vs LFM2.5-2.6B 93.4** *(볼트 실측 확인)* · Multi-IF 71.8 vs 76.8
> → **축이 갈린다**: 코딩·수학·장문맥·툴사용·에이전트 **우위** / 일반지식·지시이행 **열위**.
> → [[에이전트축-분기]] 가 **3번째 모델에서 재현**됐다([[Spark-X2.5-4B]] · [[K2-Horizon-MoVA-36B-A4B]] 에 이어). **2점 → 3점**이 됐으므로 09-08의 *"2점으로 추세 주장 금지"* 규칙을 이제 **조건부 해제** 가능. 단 셋 다 자체보고라는 공통 약점은 남는다.

> [!warning] 🔴 수치 출처 구분 — 볼트 원문 실측
> 카드 각주 원문(볼트가 `&dagger;` 57회 + 각주 문장 직접 확인):
> > *"† official **Artificial Analysis** release; **all others are reproduced internally.**"*
> → **평균 53.9와 승리 축 대부분이 벤더 자체 측정**이다. 제3자 측정은 † 항목뿐 — GPQA-Diamond · HLE · AA-LCR · SciCode · GDPval-AA v2 · Terminal-Bench.
> → 🎯 **주목**: **† 항목(제3자 측정)에서는 MiniCPM5-2B가 대체로 진다** — GPQA-D 70.2 vs 77.1, Terminal-Bench 8.6 vs 25.8, AA-LCR 59.0 vs 61.0.
> → **즉 "이기는 축은 자체측정, 지는 축은 제3자 측정"** 이라는 패턴이 보인다. raw는 출처 구분을 정확히 기재했으나 **이 상관관계까지는 지적하지 않았다.** 볼트 추가 발견.
> → [[측정도구-먼저-반증]]

## 도메인별 추출 (local-llm)

- **실용성 판단**: **높음.** 밀집 2B는 **가중치 전체가 작아** 온디바이스 실배포에 진짜로 맞는다([[K2-Horizon-MoVA-36B-A4B]] 는 활성 4B라도 36B를 다 적재해야 했다 — 이쪽이 실질적으로 훨씬 가볍다). 배포 백엔드 **9종**: Transformers · vLLM · SGLang · **llama.cpp · Ollama · LM Studio · MLX** · ArcLight · vLLM Ascend.
- **메모리 아키텍처**: 별도 메모리 층 없음. **NoLiMa 68.1**(차상위 43.5) 이 시사하는 바는 **긴 컨텍스트를 그냥 밀어넣어도 버틴다**는 것 — 소형 모델에서 RAG 없이 장문맥을 쓰는 경로.
- **Hermes 적용**: **후보로 유력.** 온디바이스 + 툴콜 + 장문맥 조합이 맞다. 단 **IFEval 86.7 열위**가 걸린다 — 에이전트는 지시 위반이 치명적이므로 **먼저 지시이행부터 실측**해야 한다.
- **트레이드오프**: 일반지식 −7 내주고 코딩/에이전트 +10~+25 얻는 교환. **2B에서 SWE-bench Verified 46.4는 이례적**.
- **오픈소스 구현체**: **Apache-2.0** · 후학습 **SFT 400B 토큰**(SFT→RL→OPD 3단계) · **학습 코퍼스 동시 공개**(Ultra-FineWeb · UltraX · UltraData-Code/Math/SFT/RL) · 테크리포트 arXiv 2506.07900 · UltraData 논문 arXiv 2602.09003 · GitHub OpenBMB/MiniCPM
- 🎯 **데이터까지 공개한 점이 [[K2-Horizon-MoVA-36B-A4B]] 와 결정적으로 다르다** — K2는 코드·체크포인트가 "예고(coming)" 상태였다. 여기는 **코퍼스가 실제로 나와 있다.**

> [!action] 당장 할 것
> **Ollama/llama.cpp로 받아 직접 2가지만 측정**: ①**IFEval류 지시이행**(카드가 인정한 약점이 실사용에서 얼마나 아픈지) ②**긴 문서 요약**(NoLiMa 68.1이 진짜인지). 2B라 실험 비용이 거의 0이고, **자체보고 벤치마크를 내 손으로 반증할 수 있는 드문 기회**다.

> [!question] 미해결 질문
> 다운로드 **2,879**는 생성 4일차치고 낮은 편인데 **♥1,007** 은 높다(비율 2.9:1). 관심 대비 실사용이 적다 — 커뮤니티 검증이 아직 없다는 뜻.

## 관련 페이지
- [[OpenBMB]]
- [[에이전트축-분기]]
- [[Spark-X2.5-4B]]
- [[K2-Horizon-MoVA-36B-A4B]]
- [[측정도구-먼저-반증]]
- [[Qwopus3.8-27B-Flash-GGUF]]
- [[PI-Desktop]]

## 원본
- 출처: https://huggingface.co/openbmb/MiniCPM5-2B
- 실측(2026-09-10): 다운로드 **2,879**(raw와 동일) · ♥**1,007**(raw 1,005 대비 +2) · **gated=False** · Apache-2.0 · created 2026-09-06 · modified 2026-09-10
- **모델카드 원문 대조(111,167바이트)**: 평균 53.9 · SWE-bench V 46.4 · SWE-bench Pro 14.4 vs 28.2 · IFEval 86.7 vs 93.4 · NoLiMa 68.1 · † 각주 문구 **전 항목 일치**
- raw 대비 드리프트: ♥ +2. **수치 전건 일치** · 볼트가 **"자체측정=승리축 / 제3자측정=패배축" 상관** 추가 발견
- 신뢰도: ⭐⭐ (벤치 대부분 벤더 자체측정 · 커뮤니티 검증 부재 / 단 코퍼스·리포트 공개는 가점)
