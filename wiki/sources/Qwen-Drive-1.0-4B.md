---
title: Qwen-Drive-1.0-4B — 자율주행 통합 VLM (가중치)
type: source
domain: ai-news
tags: [ai-news, autonomous-driving, vlm, bev, multimodal, 지는축-누락, 미해결-질문-해소]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [Qwen/Qwen-Drive-1.0-4B, arXiv:2609.00111]
---

# Qwen-Drive-1.0-4B — 자율주행 통합 VLM (가중치)

**HF**: https://huggingface.co/Qwen/Qwen-Drive-1.0-4B · `Qwen/Qwen-Drive-1.0-4B`
**지표(2026-09-13 API 실호출)**: 다운로드 **3,761**(30일 — 이 배치 HF모델 1위) · ♥**192** · **Apache-2.0** · **생성 2026-08-27** · 논문 arXiv:2609.00111
**safetensors 실측**: **4,539,265,536 = 4.54B** — 이름 4B 대비 **+13.5%** → [[단위-불일치]]
**base_model**: `Qwen/Qwen3.5-4B` · 체크포인트 **2종**(`planner-sft` / NAVSIM PDMS·WOD-E2E RFS로 보상최적화한 `planner-rl`)

> [!note] 🔗 짝 아티팩트 — **논문 페이지가 이미 있다**
> 볼트에 [[Qwen-Drive-1.0]](2026-09-02 인제스트, HF 데일리 **1위**·업보트 76)이 있다. 그건 **논문**이고 **이 페이지는 가중치**다.

> [!insight] 🎯 **09-02에 볼트가 "검증 불가"로 남긴 질문이 오늘 해소됐다 — 그리고 답이 볼트에게 불리하다**
> 09-02 [[Qwen-Drive-1.0]] 페이지에 볼트는 이렇게 적었다:
> > *"⚠️ 성능 주장 검증 불가 — 데일리 1위인데 수치가 0개다 ... 벤치마크명·절대 점수·비교 대상이 전량 미기재"*
> > *"미기재 항목: 모델 크기 · 베이스 VLM 버전 · 벤치명 · 비교 모델 · 가중치·코드 공개 여부 · **소속 기관**"*
>
> **오늘 전부 확인됐다** — 모델 크기 4.54B · 베이스 Qwen3.5-4B · 벤치 22종 · 비교 모델 15종 · 가중치 공개(Apache-2.0) · 소속 **Alibaba Qwen 확정**(`Qwen/` 조직).
> 🔴 **그런데 이 가중치 레포는 2026-08-27 생성이다. 볼트가 "검증 불가"라고 쓴 09-02보다 6일 앞선다.**
> → **자료가 없었던 게 아니라 볼트가 찾지 않았다.** 초록만 읽고 "수치 0개"라고 결론지었고, 같은 이름의 모델 카드에 표 22행이 이미 있었다.
> 📌 **규칙 신설**: 논문 인제스트 시 **동명 모델 레포를 반드시 조회**한다. 초록의 수치 부재는 *"저자가 안 냈다"* 가 아니라 *"초록에 없다"* 일 뿐이다 → [[짝-아티팩트-조회]]

## ✅ 이기는 축 (표 실측 — 전건 확인)

| 벤치 | Qwen-Drive-SFT | 베이스 Qwen3.5-4B | 개선 |
|---|---:|---:|---:|
| LingoQA | **77.8** | 70.4 | +7.4 |
| Ego3D RMSE ↓ | **7.78** | 13.17 | -5.39 |
| VLAD | **66.5** | 65.4 | +1.1 |
| SURDS | **66.1** | 53.0 | +13.1 |
| WaymoQA safety | **70.7** | 62.5 | +8.2 |
| WaymoQA all | **74.5** | 67.1 | +7.4 |
| CoC all | **41.3** | 2.6 | **+38.7** |

**NAVSIM PDMS 90.7**(RL) > SpanVLA 90.3 · SimWAM 90.3 · AutoVLA 89.6. best-of-6에서 **91.4**.

## 🔴 지는 축 (같은 표 — 누락 금지)

- **PAI-AV ADE 3s**: SFT **0.37** / RL **0.42** → Alpamayo-1.5 **0.35** 에 짐
- **PAI-AV ADE 5s**: SFT **1.07** / RL **1.11** → Alpamayo-1.5 **1.05** 에 짐
- **AlpaSim at-fault**: SFT **0.27** / RL **0.37** → Alpamayo-1.5 **0.45** 에 짐. **SFT 0.27은 표 내 최하**(SimWAM 0.30보다 낮다)
- **개루프·VQA는 강하고 폐루프는 진다.**

> [!note] 🔀 raw 정정 — WOD-E2E는 SFT가 이긴다
> raw는 *"WOD-E2E ADE 5s test 2.67 → MindVLA-U1 2.66에 짐"* 이라 적었다. 표 실측: **SFT test 2.65 · RL test 2.67 · MindVLA 2.66**.
> → **SFT(2.65)는 MindVLA(2.66)를 이긴다.** 지는 것은 RL 열뿐이다. raw는 **불리한 쪽 열을 골라 적었다**(과소 방향 오류).

> [!warning] 🎯 볼트 실측 — **RL 체크포인트에 과적합 서명이 있다** (raw·카드 양쪽 미신고)
> **WOD-E2E ADE 5s (val / test)**:
> - **Qwen-Drive-RL: 1.27 → 2.67** (**2.10배** 악화)
> - MindVLA-U1: 2.28 → 2.66 (1.17배)
> - Qwen-Drive-SFT: 2.31 → 2.65 (1.15배)
>
> **RL 열만 val에서 압도적이고(1.27, 2위의 절반) test에서 꼴찌 근처로 내려온다.** 그리고 카드 57행이 스스로 적는다: *"`planner-rl` is further **reward-optimized on NAVSIM PDMS, WOD-E2E RFS**"*.
> 🎯 **보상 최적화를 건 바로 그 벤치에서 val/test 격차가 가장 크다.** 이건 과적합의 교과서적 서명이고, **val 수치만 인용하면 성능을 2배로 과대평가하게 된다.**
> → **RL 체크포인트의 val 수치는 인용하지 않는다.**

> [!warning] 🎯 볼트 실측 — *"일반 VLM 능력 보존"* 주장의 반증 (논문 초록이 한 주장)
> 09-02 논문 초록은 *"while **largely preserving** general vision-language capability"* 라고 했다. **오늘 표로 측정 가능해졌다.**
> **일반 VLM 15개 과제에서 베이스 Qwen3.5-4B 대비 — 10개에서 진다:**
> - CountQA **31.7 vs 35.9**(-4.2) · RefSpatial **50.8 vs 54.5**(-3.7) · MMMU-Pro std **62.7 vs 64.9**(-2.2) · MMMU-Pro vis **59.7 vs 61.3**(-1.6) · MMBench **85.5 vs 87.1**(-1.6) · Omni3D **45.8 vs 47.4**(-1.6) · SimpleVQA **46.1 vs 47.8**(-1.7) · MMMU **72.7 vs 73.4**(-0.7) · CharXiv **64.4 vs 65.1**(-0.7) · OCRBench **86.4 vs 86.9**(-0.5)
> - 이기는 5개: ODinW13 +5.1 · EmbSpatial +2.9 · RealWorldQA +2.7 · ERQA +2.2 · MMStar +0.6
>
> → *"largely preserving"* 은 **거짓은 아니지만(대부분 1~2점대 손실) 방향은 일관되게 하락**이다. **15개 중 10개 하락**을 병기하지 않으면 주장이 과대 전달된다.
> 📌 **raw는 주행 표에는 "지는 축"을 성실히 적용했으나 일반 VLM 표에는 적용하지 않았다.** 같은 규칙을 표마다 일관 적용해야 한다.

> [!note] ⚠️ 심판 교체 — 다만 보수적 방향이다
> 각주 **457행**: *"LingoQA is scored with **Qwen-Plus as the judge instead of the official LingoJudge**, which we found to score leniently and inconsistently... Under the official LingoJudge protocol, Qwen-Drive-1.0-SFT obtains a LingoScore of **79.4**."*
> 🔀 자사 계열 모델을 심판으로 썼다는 점은 이해상충이나, **공식 프로토콜 79.4 > 표기값 77.8** 이라 **불리한 쪽을 실었다**. 과장 방향이 아니다. 각주 458행: *"The same judge scores **every** method."*
> 비교 공정성 각주 148행: *"AutoVLA and SimWAM **train a separate model on each dataset**."* · SFT 열은 *"conditioned on planning reasoning"* 조건부.
> 디코딩: 전 벤치 동일 설정(greedy=false, top-p=0.001, top-k=1, temp=0.01).

## 도메인별 추출 (ai-news)

- **신뢰도**: 다운로드 3,761 · Apache-2.0 · **22개 벤치 · 15개 비교모델 전량 공개** · 지는 축을 표에 그대로 둠 → **high**
- **즉시 활용**: 주행 도메인 밖에서는 **NO**(일반 VLM은 베이스가 낫다). 주행 VQA·3D 인지 연구에는 **YES**.
- **허와 실**: 실력은 **개루프·VQA**에 있다. **폐루프(AlpaSim at-fault 0.27)는 최하위권**이고, RL 체크포인트는 **val 과적합** 신호가 있다.
- **대체 관계**: 베이스 Qwen3.5-4B를 대체하지 **못한다** — 주행 특화의 대가로 일반 능력 10개 과제가 내려갔다.
- **액션**: `planner-sft` 기준으로만 인용. **RL val 수치 인용 금지.**

## 관련 페이지
- [[Qwen-Drive-1.0]] — **논문**(09-02). 이 페이지가 그 미해결 질문을 해소한다
- [[짝-아티팩트-조회]] — 이 건에서 신설된 규칙
- [[Alibaba]] — 소속 **확정**(09-02 "미확정"에서 갱신)
- [[단위-불일치]] · [[측정도구-먼저-반증]] · [[한정어-탈락]] · [[임바디드-AI]]

## 원본
- 출처: https://huggingface.co/Qwen/Qwen-Drive-1.0-4B
- 신뢰도: ⭐⭐⭐ (HF API + safetensors + 카드 567행 HTML 표 **전수 파싱**(22행×15열) + 각주 원문 대조)
