---
title: "moonshotai/Kimi-K3.1-Pro — K3 의 RL 사후학습판(2.8T/104B·Gated DSA). 비교 모델만 \"w/ fallback\" 설정, Program Bench·TB-Science·HLE(도구 없음)는 프런티어 아래"
type: source
domain: ai-news
tags: [ai-news, hf-model, moonshot, kimi, moe, sparse-attention, mxfp4, qat, agentic, open-weights, 비매칭-비교]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/moonshotai/Kimi-K3.1-Pro]
reliability: medium
---

**HF**: [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · dl30 **25,569**(볼트 11-09 · 수집기 22,571) · ♥1,751 · trending 571(수집기 기준 2위) · license `kimi-k3.1-pro`(커스텀) · safetensors **2,780,110,363,392** · created 2026-11-02

## 핵심 인사이트
> [!insight] K3 → K3.1: 구조 변경은 어텐션, 성능 변경은 RL
> MoE 896 전문가 중 16(+공유 2) 활성, 93층 = **KDA 69층 + Gated DSA 24층**(K3 의 full-attention Gated MLA 를 희소 어텐션으로 교체 → 장문맥 효율), MoonViT-V2(401M), **MXFP4 가중치 / MXFP8 활성 QAT**. 수백 도메인 공동 RL. [[Kimi-K3]] 대비 GPQA 93.5→**94.2** · BrowseComp 91.2→**92.1**(둘 다 자체 보고 간 비교).

> [!warning] 표의 조건이 비대칭 — 볼트 표 전수 판독(카드 HTML 파싱)
> 열 머리: Kimi = **"(max)"**, Claude Fable 5.1 · GPT-6 Astra · Claude Opus 5.5 = **"(max, w/ fallback)"**. 같은 설정이 아니다([[비매칭-비교]]).
> 수집기가 적은 강점(TB 4.0 65.7 · SWE Marathon 51.7 = 비교군 최고 · HLE w/ tools 70.0 · BrowseComp 92.1) 외에 **수집기 미기재 약점 행**: Terminal-Bench-**Science** 38.1(GPT-6 Astra 68.1 · Opus 5.5 63.3) · GPQA 94.2 < GPT-6 Astra 96.1. 기재된 약점: Program Bench 31.5(Opus 65.0) · HLE-Full 51.1 · HLE-Diamond 39.4 · ExploitBench 74.7(GPT-6 Astra 100) ⇒ [[표-부분인용]]. Kimi Code Bench·Business Operation·DECK-Arena 등은 **(Internal)**.

## 도메인별 추출 (ai-news)
- **신뢰도**: 카드 자체 측정 + 타사 수치 혼재 · 논문 미확인 · dl 2.5만
- **즉시 활용**: NO(로컬) — 2.8T 는 대형 클러스터 전제. API/서드파티 호스팅으로만 현실적
- **6개월 영향력**: 오픈웨이트가 터미널·장기 SWE 에서 클로즈드 프런티어와 같은 구간에 들어옴 — 단 도구 없는 추론(HLE)·코드 생성(Program Bench)은 격차 유지
- **허와 실**: "에이전트 강함"은 도구·브라우징 축 한정
- **액션**: 없음(관찰)

## 관련 페이지
- [[Kimi-K3]] · [[Moonshot AI]] · [[비매칭-비교]] · [[표-부분인용]] · [[DeepSeek-V4.1-Flash-1017]]

## 원본
- 출처: https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- 확인 범위: HF API(볼트 11-09) · 카드 raw 47,653B — 평가표 HTML `<td>` 파싱(11행 전 열 대조)
- 신뢰도: ⭐⭐⭐ (원문 대조 · 자체 측정)
