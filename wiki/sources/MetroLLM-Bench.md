---
title: MetroLLM-Bench — 지하철 키오스크 런타임으로서의 LLM 평가
type: source
domain: local-llm
tags: [local-llm, hf-daily-paper, benchmark, peft, slm, tool-use, 측정도구-먼저-반증]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [arXiv:2609.10016, continker/metrollm-bench]
---

# MetroLLM-Bench — Evaluating Language Models as Transit Kiosk Runtimes

**HF**: https://huggingface.co/papers/2609.10016 · **arXiv**: 2609.10016 · **코드**: https://github.com/continker/metrollm-bench
**지표(2026-09-13 API 실호출)**: 업보트 **29** · **저자 1인**(Remco Hendriks) · **발행 2026-09-09**
**드리프트**: 업보트·저자 수 **완전 일치**. 🔴 발행일 raw *"09-11"* → 실제 **09-09**(이 배치 5편 중 가장 오래됨)
**도메인 재판정**: raw `ai-news` → **`local-llm`** 이관. 4B 학생 모델·**Q4_K_M 2.6GB**·키오스크 온디바이스 배치가 주제다. 09-11/09-12에 [[MiniCPM5-2B-GGUF]]·[[X-AuT]] 에 적용한 기준과 동일.

> [!insight] 핵심 인사이트 — **벤치를 "질문"이 아니라 "런타임"으로 설계했다**
> 모델이 답을 쓰는 게 아니라 **구조화 툴을 호출하고 기계판독 가능한 종료 상태**를 제출해야 한다 — 결과 + (해당 시) **티켓별 요금 견적** + **키오스크 동작**. 실제 지하철 **6개 노선망(역 37~414개)** · **11개 범주**(경로·요금·운행중단·접근성·적대적 입력 포함) · **955 케이스**.
> 채점을 둘로 쪼갠 것이 설계의 핵심: **Tier 1 = 결정적 채점 14요소**, **Tier 2 = 의미품질 8요소(그중 6개가 LLM 심판)**.
> 🎯 **결정적으로 채점 가능한 부분을 LLM 심판에서 분리해 냈다** — 볼트 [[요약자와-판정자-분리]] 의 벤치마크 판본이다. 요금 계산은 정답이 있고, 설명 품질은 없다. 둘을 한 점수로 뭉개지 않는다.

> [!warning] 🔴 **볼트 실측 — 헤드라인 비교가 구조적으로 불공정하다 (raw·초록 양쪽 미신고)**
> 초록에 이 문장이 있다: *"A stratified **75/25 split reserves 717 cases for training-data generation** and 238 for held-out evaluation."*
> 그리고 헤드라인은 *"4B Qwen 3.5 학생이 GPT-5.6 양 티어를 넘음(91.3 vs 90.6·90.0)"* 이다.
>
> **두 문장을 붙이면 비교의 성격이 바뀐다:**
> - 4B 학생은 **이 벤치 자신의 717 케이스에서 생성한 데이터로 학습**됐다 → **분포 내(in-distribution)**
> - GPT-5.6·GPT-5.4는 그 학습을 받지 않았다 → **제로샷**
>
> 🎯 **"작은 모델이 큰 모델을 이겼다"가 아니라 "이 과제에 맞춰 학습한 모델이 안 맞춘 모델을 이겼다"** 이다. 같은 홀드아웃 238 케이스를 쓰더라도 **출제 범위를 아는 쪽과 모르는 쪽의 시험**이다.
> raw는 초록의 반증 5개를 잘 뽑았지만 **이 문장은 지나쳤고**, 초록도 이 둘을 나란히 놓지 않는다. **결손은 인용이 아니라 배치에서 생긴다.**

> [!warning] 🔴 저자가 같은 초록에 적은 반증 5개 (전건 원문 확인)
> ① *"Larger **9B and 27B students provide no further Tier 1 improvement** over the 4B student at this training scale."* → **스케일업이 안 먹힌다**
> ② *"the PEFT gain over the corresponding base model **decreases from +7.03 points at 2B** (three training seeds) **to -0.91 at 27B**; every seed shows the same direction at every size."* → **27B에서는 미세조정이 손해**. 전 시드 동일 방향
> ③ *"A deterministic **rule-based baseline reaches 84.6** on Tier 1"* → **규칙엔진 대비 실질 우위 6.7점**. 남은 우위는 *"policy adaptation, compound scenarios, accessibility, and temporal reasoning"* 에 집중
> ④ *"**Muse Glimmer 30B leads the composite ranking**"* → **종합 1위는 4B 학생이 아니다.** Tier1 1위 ≠ 종합 1위
> ⑤ *"**serving configuration alone** moves the Qwen 3.5-to-3.8 comparison by **2.7 Tier 1 points**"* → **서빙 설정 교란이 모델 간 격차와 맞먹는다**
>
> 🎯 ②와 ③을 같이 읽으면 더 날카롭다: **모델을 키울수록 미세조정 이득이 사라지고, 바닥에는 규칙엔진 84.6이 깔려 있다.** 이 과제에서 LLM이 실제로 사는 구간은 **4B 부근의 좁은 창**이다.

> [!note] 평가 규모
> **26개 모델 / 6개 벤더** 평가, **23개만 순위화**(3개 제외 사유 초록에 없음). Tier2 8요소 중 **6요소가 LLM 심판** — 심판 의존도가 높은 절반은 별도로 봐야 한다.

## 도메인별 추출 (local-llm)

- **실용성 판단**: ✅ **배포 가능.** **Q4_K_M 2.6GB** 는 키오스크·엣지 하드웨어에 실제로 올라간다. 다만 성능 근거는 **분포 내 학습** 전제다.
- **메모리/구조**: RAG 아님. **PEFT + 구조화 툴 호출**. 지식을 모델에 넣지 않고 **툴에 남긴다**.
- **트레이드오프**: 2B→+7.03 / 27B→-0.91. **미세조정 투자 대비 효과가 모델 크기에 반비례**한다는 실측 곡선이 이 논문의 최대 자산이다.
- **Hermes 적용**: 🎯 직접 해당. *"작은 모델 + 결정적 툴 + 좁은 도메인"* 조합이 ChinameBot 류 배치와 동형이다. **단, 규칙엔진 84.6을 먼저 만들어 보고 LLM 우위를 재야 한다** — 이게 이 논문이 준 가장 실용적인 절차다.
- **오픈소스 구현체**: `continker/metrollm-bench` 공개.

> [!action] 당장 할 것
> 좁은 도메인 과제를 LLM으로 풀기 전에 **결정적 규칙 베이스라인을 먼저 만들어 점수를 재고**, LLM이 그 위에 얹는 실제 증분을 측정한다. 이 논문에서는 그 증분이 **6.7점**이었다.

## 관련 페이지
- [[요약자와-판정자-분리]] — Tier1/Tier2 분리가 이 원칙의 벤치 구현
- [[측정도구-먼저-반증]] — 서빙 설정이 2.7점을 움직인다 = **측정 장치가 신호와 같은 크기의 잡음을 만든다**
- [[온폴리시-증류]] · [[에이전트-스킬]] · [[단위-불일치]]
- [[Edge0-35B-A3B-preview]] — 같은 배치 local-llm. **양쪽 다 "작게 만들어 엣지에 올린다"이나 경로가 다르다**(PEFT 증류 vs 양자화+오프로드)

## 원본
- 출처: https://huggingface.co/papers/2609.10016
- 신뢰도: ⭐⭐⭐ (HF API 실호출 + 초록 원문 전문 대조. 저자 1인·코드 공개)
