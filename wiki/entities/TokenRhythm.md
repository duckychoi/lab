---
title: TokenRhythm
type: entity
domain: local-llm
tags: [local-llm, hf-model, qwen-derivative, agent, post-training, rsi, 신설]
created: 2026-09-18
updated: 2026-09-18
sources: [NeoHorse-1-4B.md, NeoHorse-1-9B.md]
reliability: medium
---

# TokenRhythm

> [!insight] 핵심 인사이트 — **모델을 만들지 않고 에이전트 궤적으로 다시 굽는다**
> Qwen3.5 계열(4B·9B)을 **에이전틱 사후학습**으로 재조정해 [[NeoHorse-1-4B]]·[[NeoHorse-1-9B]] 를 배포. 두 모델 모두 **apache-2.0 · BF16 단일 · 2026-09-05 동시 공개**.
> 🎯 **자리의 성격**: [[Comfy-Org]] 가 런타임에 맞게 **재포장**하고 [[DavidAU]] 가 **양자화·탈검열**한다면, TokenRhythm은 **용도에 맞게 다시 학습**한다. 세 층이 전부 "모델을 만들지 않는 모델 공급자"이고 **개입 깊이가 다르다**: 재포장 < 양자화 < 사후학습.
> ✅ **라벨이 정직하다** — `base_model:finetune:Qwen/Qwen3.5-*` 로 실체와 태그가 일치한다(볼트 실측). [[파생표기-함정]] **사례가 아니다.**

> [!insight] 🎯 이 조직의 특징 — **모논문을 먼저 내고 모델을 냈다**
> ```
> 2026-09-05  모델 2종 공개 (4B · 9B)
> 2026-09-08  논문 arXiv 2609.08183 — 업보트 421 · 코드 ★535
>             "NeoHorse-1: Towards Recursive Self-Improvement via
>              Agentic Post-Training with Routing Harness"
> ```
> 🔴 **볼트는 모델 2건을 오늘(09-18) 받았고 논문은 아직 없다.** 업보트 421은 볼트가 관측한 논문 중 최상위권이다 → [[선발창-누락]]
> **방법의 골자**(초록): 이질적 모델 풀 + 지능형 라우팅으로 **매 턴의 예측 능력수요·선택된 서비스 티어·후속 상호작용을 기록**하고, 그 기록을 **구조 검증 + 6차원 의미 평가**를 통과시켜 학습 예제로 변환한다.
> 🎯 **즉 하네스가 학습 데이터 생산 장치다.** 이 배치의 [[하네스-설계-축]] 4건 중 **하네스를 학습 루프 안으로 넣은 유일한 사례**.

> [!warning] 🔴 주장의 온도 — RSI는 달성이 아니라 지향이다
> 논문 제목의 *"Towards Recursive Self-Improvement"*, 카드의 *"초기 프로토타입"*, 그리고 *"extending this loop across successive iterations is the **next step**"* — **세 곳 모두 미래형이다.**
> ✅ **볼트 판정: 과장이 아니다.** 저자가 달성했다고 쓰지 않았다. 🔴 **위험은 요약 단계에 있다** → [[RSI-프레이밍]]
> 🎯 **같은 배치 [[SoL-Pi]]([[NVIDIA]] NVlabs)도 *"RSI-inspired"* 를 쓴다.** 두 독립 조직이 같은 달에 같은 프레이밍을 채택했다.

> [!warning] 🔴 볼트가 이 조직에 대해 모르는 것
> **소속·국적·규모 전부 불명.** 논문 저자 명단을 볼트가 조회하지 않았고, HF 조직 페이지도 확인하지 않았다.
> 🎯 **그런데 모델 품질 지표는 낮지 않다** — 4B가 ♥2,354(트렌딩 상위), 논문 업보트 421, 코드 ★535. **인지도 대비 볼트의 정보가 가장 적은 조직**이다.

## 산출물
- [[NeoHorse-1-4B]] — 4.21B · DL 19,789 · ♥2,354 · 10벤치 평균 64.87(+5.93) · **10개 축 전부 양(+)**
- [[NeoHorse-1-9B]] — 8.95B · DL 9,856 · ♥881 · 평균 69.04(+3.44) · 🔴 **IFEval −0.37 · IFBench/LCB +0.00**
- 논문 `arxiv:2609.08183` (업보트 421 · ★535) — 🔴 **볼트 미보유**

> [!action] 당장 할 것
> **논문 2609.08183 인제스트 + TokenRhythm 조직 정보 조회.** 🎯 볼트가 보유한 모델 2건의 **설계 근거가 전부 그 논문에 있다** — 특히 9B의 지시수행 회귀 원인.

## 관련 페이지
- [[NeoHorse-1-4B]]
- [[NeoHorse-1-9B]]
- [[선발창-누락]]
- [[RSI-프레이밍]]
- [[하네스-설계-축]]
- [[SoL-Pi]]
- [[에이전트축-분기]]
- [[Comfy-Org]]
- [[DavidAU]]
- [[파생표기-함정]]
- [[Alibaba]]

## 원본
- 출처: https://huggingface.co/TokenRhythm
- 볼트 실측(2026-09-18, HF API): 모델 2종 전건 확인 · `base_model:finetune` 라벨 정합 · 양쪽 `arxiv:2609.08183` 태그 보유
- 신뢰도: ⭐⭐ (모델 지표는 API 실측 일치 · 라벨 정직 · 🔴 그러나 조직 실체 정보 전무 · 모논문 미인제스트)
