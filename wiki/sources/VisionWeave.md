---
title: "VisionWeave — '평균 43% 절감'의 실체는 벤치별 16.5~55.1% 편차이고, 그 편차가 바로 기여다"
type: source
domain: ai-news
tags: [ai-news, mllm, visual-token, token-pruning, elastic-representation, sglang, qwen, mrope, 복합지표-분해, 배수-조건분산]
created: 2026-10-12
updated: 2026-10-12
sources: []
reliability: high
---

# VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs

> [!insight] 🏆🏆 **볼트 최대 발견 — "평균 43.0% 절감"은 16.5%~55.1% 의 평균이고, 그 분산이 주장의 증거다**
> 🔴 수집기 한줄요약(그리고 초록)은 *"평균 토큰 43.0% 절감"* 으로 적는다. 📌 **볼트가 arXiv HTML 본문 표를 열어 벤치별 절감률을 분해했다**(Qwen3.8-27B 기준):
>
> | 벤치 | 절감률 | 성능 변화 (Native 대비) |
> |---|---:|---|
> | **ScreenSpotV2** (GUI 그라운딩) | **55.1%** | 94.42 → 91.43 (**−3.17%**) |
> | **VideoOCR** | 49.6% | 70.72 → 70.51 (−0.30%) |
> | **HallusionBench** | 44.9% | 73.25 → **73.60** (🟢 **+0.48%**) |
> | **RealWorldQA** | 43.1% | 78.82 → 77.91 (−1.15%) |
> | **DocVQA** | 27.3% | 92.47 → 91.33 (−1.23%) |
> | **InfoVQA** (인포그래픽) | **16.5%** | 74.13 → 71.61 (**−3.40%**) |
>
> 🎯 **절감률이 3.3배 차이난다(16.5% ↔ 55.1%).** 그리고 방향이 의미를 갖는다: **GUI 화면은 절반 이상 버려도 되고(55.1%), 인포그래픽은 16.5%만 줄인다** — 정보 밀도가 높은 입력에서 라우터가 **스스로 절감을 포기한다.**
> ⇒ 📌 **"43.0%"를 단일 상수로 인용하면 이 논문의 핵심 주장(content-adaptive)이 사라진다.** 평균값은 오히려 기여를 가리는 숫자다. → [[복합지표-분해]] · [[배수-조건분산]]

> [!insight] 🏆 **고정 비율 프루닝은 GUI·인포그래픽에서 붕괴한다 — 이것이 진짜 대조다**
> 같은 표의 베이스라인(Qwen3.8-27B):
>
> | 벤치 | FastV† | VisionZip | **VisionWeave** |
> |---|---|---|---|
> | **ScreenSpotV2** | 49.53 (**−47.54%**) | 49.21 (**−47.88%**) | 91.43 (−3.17%) |
> | **InfoVQA** | 55.49 (−25.15%) | 53.96 (−27.21%) | 71.61 (−3.40%) |
> | DocVQA | 77.05 (−16.68%) | 76.01 (−17.80%) | 91.33 (−1.23%) |
>
> 🔴 **ScreenSpotV2에서 기존 프루닝 기법은 성능이 반토막(−47.5~−47.9%) 난다.** 94.42 → 49점대.
> 🎯 ⇒ **초록의 *"88% performance preserved for token pruning baselines"* 는 평균이고, 특정 과제에서는 52% 수준으로 무너진다.** 이것도 평균이 가린 사례다 — 이번에는 **베이스라인 쪽에 불리한 방향**으로 가렸다.
> 📌 ⚖️ 즉 **평균 집계가 양쪽을 모두 평탄화했다**: VisionWeave의 적응성(기여)도, 베이스라인의 붕괴(열위)도 함께 지워졌다.

> [!note] 🏆 **수집기 미확인 해소 — 8개 벤치 목록 확정**(볼트가 arXiv HTML로 뚫었다)
> 수집기 10-12 자기보고 5번: *"[[VisionWeave]] 8개 벤치의 목록 미확인"*. ✅ **해소했다.** 본문 원문:
> > *"cross-domain robustness on eight benchmarks spanning natural-image (**RealWorldQA**), document and infographic understanding (**DocVQA** and **InfoVQA**), GUI grounding (**ScreenSpotV2**), visual hallucination (**HallusionBench**), video details (**VideoOCR**), and video understanding (**Video-MME** and **LongVideoBench**)."*
>
> 1. RealWorldQA — 자연 이미지
> 2. DocVQA — 문서 (**ANLS**)
> 3. InfoVQA — 인포그래픽 (**ANLS**)
> 4. ScreenSpotV2 — GUI 그라운딩
> 5. HallusionBench — 시각 환각 (**aAcc**)
> 6. VideoOCR — 영상 세부
> 7. Video-MME — 영상 이해
> 8. LongVideoBench — 영상 이해
>
> 📌 지표 원문: *"All task scores are reported on a 0–100 scale, using **ANLS** for DocVQA and InfoVQA, **aAcc** for HallusionBench, and the task-specific metric for each remaining benchmark."*
> ⚠️ **구성 편향을 적어 둔다**: 8개 중 **영상이 3개**(VideoOCR·Video-MME·LongVideoBench), **ANLS 문서계열이 2개**. "98.9% 유지"는 이 구성에 의존하는 평균이다.

> [!insight] 🎯 **검증 전략이 2단이다 — 4B에서 먼저 성립시키고 27B로 올렸다**
> 원문: *"Through **self-distillation alone**, we validate this capability on **Qwen3.5-4B** and scale to **Qwen3.8-27B** with over **30K A100 GPU-hours**."*
> 🔴 **그런데 두 규모의 절감률이 다르다**: Qwen3.5-4B 의 Average 절감은 **35.8%**(성능 73.25 → 72.59, −0.90%), 27B 는 **43.0%**.
> ⇒ 📌 **절감 여력이 모델 규모와 함께 커진다**(35.8% → 43.0%). 초록의 43.0%는 **27B 전용 수치**이고, 작은 모델에 그대로 기대하면 안 된다.
> 🆕 볼트 관측: 4B에서도 **성능 유지율이 −0.90%** 로 좋다 — 즉 **기법은 작은 모델에서도 성립하고, 다만 절감 폭이 작다.**

> [!warning] 🔴 **30K+ A100 GPU-시간은 재현 장벽이다 — "native capability"의 대가**
> 논문의 프레이밍은 *"a **native capability** we term elastic visual representation weaving"* 이다. 즉 **사후 프루닝이 아니라 모델이 학습으로 획득한 능력**이라는 주장이고, 그것이 베이스라인 붕괴를 피한 이유다.
> 🔴 **그 대가가 30K+ A100 시간**이다. ⇒ 📌 **이 기법은 "내가 적용할 수 있는 최적화"가 아니라 "파운데이션 제공자가 모델에 넣어 주는 기능"이다.** 소비자 측 행동은 설치가 아니라 **그런 모델이 나오면 고르는 것**이다.
> ⚖️ 수집기가 *"학습 비용 30K+ A100 GPU-시간은 재현 장벽이다"* 라고 적은 판단은 **옳다**.

> [!note] ✅ 서빙 수치 — 조건 명시됨
> 원문: *"When deployed on **SGLang** serving engine, our method achieves a **2.3x throughput** gain while reducing **mean TTFT by 54.4%** and **mean TPOT by 60.6%**."*
> ✅ 수집기 보고 일치. 📌 **엔진이 SGLang으로 특정**되어 있다 — vLLM·TensorRT-LLM 등에서의 수치는 **미확인**.
> ⚠️ 본문에 *"TTFT) and time per output token (TPOT) decrease by 57..."* 로 **다른 숫자(57%대)** 가 등장하는 구간이 있다 — 측정 조건(모델 규모/입력 길이)이 다른 표로 보이나 **대조 불명**. 초록 값(54.4% / 60.6%)을 기준으로 삼는다.

> [!note] ✅ 볼트 실측
> arXiv API + HTML 본문 실조회(2026-10-12): `2610.07987` · **published 2026-10-06T08:48:50Z** · **cs.CV, cs.AI, cs.CL** · 저자 **12명**(Yuan Feng, Qize Yang, Ruizhe Chen, Sibo Song, Haolin He, Muzhi Zhu, Zihan Liu, **Yunfei Chu** 외) · HTML 본문 64,373자
> 구조 원문: *"a **gated spatial pooler** constructs coarse-grained representations alongside native fine-grained representations within a **shared MRoPE coordinate**, while a **granularity router** learns their content-adaptive allocation."*
> ⚠️ 초록 43.0% vs 본문 *"averaging 43.1%"* — **0.1p 불일치**(반올림 추정, 경위 미확인).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — 업보트 47, arXiv cs.CV 등재, 저자 12인(Qwen 팀 인물 포함), **벤치별 절감·성능을 전부 표로 공개**하고 베이스라인 3종과 대조한다. 📌 볼트가 **본문으로 전 수치를 재확인**했다.
- **즉시 활용**: **NO**. 이유 — 30K+ A100 학습이 전제인 **모델 내장 능력**이다. 🎯 **단 지금 바로 쓸 수 있는 지식 1개**: 시각 토큰 프루닝 도구(FastV·VisionZip 류)를 **GUI 스크린샷·인포그래픽에 적용하면 안 된다**(−47%). 내 파이프라인에 그런 최적화가 끼어 있다면 **해당 입력 유형에서 끈다.**
- **6개월 영향력**: **높음**. Qwen 계열 차기 모델에 들어오면 **동일 품질에서 비용 43% 절감 + 처리량 2.3배**가 API 가격에 반영된다. 📌 영상·문서 처리 비용이 큰 작업의 손익분기가 움직인다.
- **대체 관계**: **FastV · VisionZip 등 사후 토큰 프루닝을 대체**한다(같은 과제에서 −3% vs −47%). 내가 그 도구를 쓰고 있지는 않으므로 직접 교체는 없다.
- **허와 실**: ✅ 실 — 표가 전부 공개되고 조건이 명시된다. 🔴 허에 가까운 것은 **"43.0%"라는 단일 숫자의 유통 방식**이다. 실제 값은 16.5~55.1%이고, 평균만 보면 적응성이라는 기여 자체가 안 보인다.
- **액션**: ✅ **지금 할 것 1개** — 내 쪽 시각 입력 파이프라인에 고정비율 다운샘플/프루닝이 있는지 점검, GUI·인포그래픽 경로에서는 해제.

> [!action] 당장 할 것
> 🎯 **고정 비율 시각 토큰 축소를 GUI 스크린샷·인포그래픽 입력에 쓰지 않는다.** 근거: 동일 조건에서 FastV/VisionZip이 ScreenSpotV2에서 **−47.5~−47.9%**, InfoVQA에서 **−25~−27%** 붕괴. 📌 **입력 유형별로 축소율을 분리하거나, 축소를 끄는 쪽이 안전하다.**

> [!question] 미해결 질문
> 1. 🔴 **SGLang 외 엔진(vLLM 등)에서의 2.3배 재현 여부** — 미확인.
> 2. 🔴 본문의 **TTFT 57%대 수치**가 어떤 조건인지 — 초록 54.4%와 불일치 구간.
> 3. 🔴 **코드·가중치 공개 여부** — 초록·본문에서 확인 못 함.
> 4. 라우터 임계값 `t` 의 기본값과 민감도 — 본문에 *"With a default routing threshold t = 0…"* 로 시작하는 구간이 있으나 값 미확정.
> 5. 43.0 vs 43.1 불일치 경위.

## 관련 페이지
- [[복합지표-분해]] — **평균 43.0%가 16.5~55.1%를 가린다 / 베이스라인 88%가 52%를 가린다**
- [[배수-조건분산]] · [[한정어-탈락]] · [[표-부분인용]]
- [[Qwen3.8-27B]] — 기반 모델, **같은 날 배치**
- [[Qwen]] · [[Alibaba]]
- [[Reflex]] — **경계선**: 정적 이해는 토큰을 줄여도 되지만 반응형 제어는 시간 이력 제거 시 붕괴
- [[SoftwareGym]] — ScreenSpotV2/GUI 축에서 접점
- [[DiffusionART]] · [[AAArena]] — 2026-10-12 동일 배치
- [[ai-news]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2610.07987 · arXiv `2610.07987`
- 볼트 실측(2026-10-12): arXiv API(초록) **+ arXiv HTML 본문 전문**(`arxiv.org/html/2610.07987v1`, 341,343B → 본문 64,373자) — **수집기 10-06 확립 경로 ② 재집행, 성공**
- HF 데일리: 업보트 **47** · published **2026-10-06T08:48:50Z**
- raw 대비: ✅ 43.0%·98.9%·88%·2.3배·TTFT −54.4%·TPOT −60.6%·30K A100 **전건 일치** · 🏆 **볼트 해소: 8개 벤치 목록 확정** · 🏆 **볼트 신규: 벤치별 절감률 16.5~55.1% 분해** · 🏆 **볼트 신규: 베이스라인이 ScreenSpotV2에서 −47.5% 붕괴** · 🏆 **볼트 신규: 4B 절감 35.8% vs 27B 43.0%** · ⚠️ 43.0 vs 43.1 불일치 발견
- 신뢰도: ⭐⭐⭐⭐⭐ (전 벤치 표 공개·베이스라인 3종 대조·조건 명시 / 재현 비용 과대, 코드 미확인)
