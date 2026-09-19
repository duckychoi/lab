---
title: Uno — draft 모델 없이 3배 가속, 그리고 8B가 26B를 이겼다 (AR 가중치는 그대로 둔 채 diffusion만 증류)
type: source
domain: ai-news
tags: [ai-news, hf-paper, diffusion, inference-optimization, speculative-decoding, llm, 무손실가속]
created: 2026-09-08
updated: 2026-09-19
sources: [K2-Horizon-7B.md]
reliability: high
---

# Unlocking Lossless Speedups in LLMs via Discrete Diffusion (Uno)

**HF 논문**: https://huggingface.co/papers/2609.04010
**업보트 19** (2026-09-08 API 실측 · raw 19 **완전 일치** · **이번 배치 1위**) · 게시 **2026-09-03** · 저자 **17인**
**코드·체크포인트 공개**: https://s-sahoo.github.io/uno/ (초록 명시) · GitHub: https://github.com/ifm-ai/uno

> [!insight] 🎯 **핵심 구조 — 가중치를 두 벌로 쪼개고, 무거운 쪽은 건드리지 않는다**
> 초록 원문 실측 기준 구조:
> - **AR 가중치**: 표준 next-token-prediction(NTP)으로 학습 — **기존 그대로**
> - **diffusion 가중치**: **경량**, 여러 토큰 동시 생성용으로 학습
> - 연결: **Diffusion Distillation** 단계 — 저자 표현 *"기존 LLM 학습 파이프라인에 **무시할 만한 오버헤드**(negligible overhead)를 추가"*
> - 샘플러: **Ψ-Spec** — 고정 컨텍스트 길이에서 무손실 가속 + 추론시 스케일링
> **핵심은 "AR 모델 분포를 정의하면서 diffusion으로 그 분포에서 여러 토큰을 병렬로 뽑는다"** 는 점이다. 분포는 AR의 것이고 뽑는 방식만 바뀐다 → **무손실**의 근거가 여기 있다.

> [!insight] 🔴 **두 개의 대조군을 동시에 이긴다 — 이게 이 논문의 진짜 주장이다**
> 초록은 **두 계열과 명시적으로 선을 긋는다**:
> - **vs speculative decoding**: *"별도 draft 모델이 필요 없다"* + **"평가한 모든 배치 크기에서 더 높은 처리량"**. → speculative decoding의 고질적 약점(**배치가 커지면 이득이 사라짐**)을 정면으로 겨냥한 표현이다.
> - **vs diffusion LLM(d-LLM)**: *"기반 AR 모델의 품질을 희생하지 않고 가속한다"*. → d-LLM은 빠르지만 품질이 떨어지는 트레이드오프가 있었고, 여기선 그게 없다는 주장.
> **수치**: 베이스 AR 모델 대비 **최대 3배**, **디바이스가 지원하는 최대 배치 크기에서도** 성립.
> **가장 강한 주장**: **8B Uno가 26B DiffusionGemma와 상용 Mercury 2를 에이전트 툴사용·코딩·롱컨텍스트 전 벤치에서 상회.** raw 기재와 초록 원문이 **일치**한다.

> [!insight] 볼트 축 연결 — [[선택비용과-중복성]] 의 네 번째 층
> 볼트는 *중복성을 줄이거나 심어서 이득을 얻는* 사례를 축적해 왔다: [[Random-Attention]](KV 축출·추론) · [[Minima]](정밀도·추론) · [[Dont-Drop-Dropout]](학습 시 결손 → 추론 시 유연성).
> Uno는 **네 번째 형태**다: **순차성(sequentiality) 자체가 중복**이라는 관점. AR은 토큰을 하나씩 뽑아야 한다고 가정하는데, **그 가정이 분포의 요구가 아니라 샘플링 절차의 관성**이었음을 보인다.
> → 앞선 셋이 *"무엇을 버릴까"* 였다면 Uno는 *"무엇을 동시에 할까"* 다. **버리기(축출·정밀도)와 병렬화는 다른 조작**이므로 축에 **병렬성 항목을 신설**할 근거가 된다.

> [!insight] [[온폴리시-증류]] 계보와의 관계 — 증류의 목적이 바뀌었다
> 이 배치에는 증류 논문이 4건 있다([[FlowBalance]]·[[One-Symptom-Three-Levers]]·[[TGOPD]]·본 논문). **앞의 셋은 "더 잘하게" 하려고 증류하고, Uno는 "더 빠르게" 하려고 증류한다.**
> Uno의 Diffusion Distillation은 **능력 이전이 아니라 병렬 샘플링 능력 부여**이며, 교사도 학생도 **같은 모델의 다른 가중치 집합**이다. 볼트가 [[온폴리시-증류]] 에 정리한 *"앵커의 내부화 3형태"* 와는 **다른 축**이므로 혼동하지 않도록 여기 명시한다.

> [!warning] 미확인 — 무손실 주장의 검증 범위
> **"lossless"는 강한 주장**이다. 초록은 *"기반 AR 모델 품질을 희생하지 않는다"* 고 하나, **어떤 지표로 동등성을 확인했는지는 초록에 없다**(perplexity? 벤치 점수? 분포 거리?).
> **미기재 항목**: Diffusion Distillation의 실제 비용(*"negligible"* 은 정성 표현) · diffusion 가중치의 크기 비율 · 8B Uno의 베이스 모델 정체 · 벤치마크 이름과 점수(*"전 벤치 상회"* 만 있고 표는 초록 밖).
> ⚠️ **업보트 19는 이번 배치 1위이나 절대 수치로는 작다.** 볼트가 반복 확인했듯 업보트는 **주목**이지 검증이 아니다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 초록 원문 실검증 · **코드·체크포인트 공개 명시**(재현 가능) · 저자 17인 · 배치 업보트 1위. **감점**: 무손실 판정 기준과 벤치 수치가 초록 밖.
- **즉시 활용**: **🟡 조건부 YES.** 체크포인트가 공개돼 있으므로 **받아서 돌려볼 수 있다.** 다만 *"기존 오픈 웨이트 AR LLM을 증강해 만들 수 있다"* 는 경로가 실제로 얼마나 싼지가 도입 판단의 전부인데 **그 비용이 미공개**다.
- **6개월 영향력**: **높음.** speculative decoding은 현재 추론 가속의 사실상 표준이고, 그것을 **모든 배치 크기에서** 이긴다면 표준이 바뀐다. 로컬 추론([[local-llm]] 축)에서 특히 크다 — draft 모델을 함께 올릴 VRAM이 없는 환경이 많다.
- **대체 관계**: **speculative decoding 대체**(draft 모델 제거 = VRAM 절약). d-LLM 계열([[DiffusionGemma]] 등) 대체.
- **허와 실**: 걷어내면 **"AR 분포를 유지한 채 병렬 디코딩하는 방법을 제안했고, 코드를 공개했고, 8B로 26B를 이겼다고 주장한다"** — **공개했다는 사실이 이 배치에서 가장 강한 신호**다. 검증은 볼트가 직접 할 수 있다.
- **액션**: 아래.

> [!action] 당장 할 것
> 1. **체크포인트를 실제로 받아 3배 주장을 1회 측정**한다. 이 배치의 논문 5건 중 **볼트가 직접 검증할 수 있는 유일한 건**이다(코드+가중치 공개).
> 2. **"draft 모델 없는 가속"을 [[local-llm]] 도메인의 추적 항목으로 등록** — 로컬 환경에서 VRAM 제약은 항상 결정 변수다.

> [!question] 미해결
> **"lossless"의 판정 지표가 무엇인가** — 초록에 없다. · **Diffusion Distillation의 실제 GPU 비용** · **8B Uno의 베이스 모델** · 26B DiffusionGemma·Mercury 2와의 **벤치별 점수**(요약만 있고 표 없음).


> [!note] 🆕 2026-09-19 — **베이스 확정: [[K2-Horizon-7B]]** (HF `IFM/K2-Horizon-7B-Uno`, LoRA 어댑터, DL 50,562 = 베이스의 약 3.9배). 비교 대상 "26B DiffusionGemma" = Diff-Gemma 26B-A4B(활성 4B). 🔴 "무손실"인데 SWE-bench Verified 70.1 vs 베이스 70.6. 시스템 처리량 1위(5,255)지만 요청당 405 < Mercury 2(769)·Diff-Gemma(836) — **배치 서빙용, 단일 사용자 지연용 아님**.

## 관련 페이지
- [[K2-Horizon-7B]]
- [[온폴리시-증류]] — 증류 계보(단 **목적이 다름: 능력 vs 속도**)
- [[선택비용과-중복성]] — **병렬성 항목 신설 근거**
- [[FlowBalance]] · [[One-Symptom-Three-Levers]] · [[TGOPD]] — 같은 배치 증류 3건
- [[Random-Attention]] · [[Minima]] · [[Dont-Drop-Dropout]] — 중복성 선행 3층
- [[Mamba4]] · [[검사가능성-공사]]

## 원본
- 출처: https://huggingface.co/papers/2609.04010
- 코드: https://s-sahoo.github.io/uno/ · https://github.com/ifm-ai/uno
- 수집: 2026-09-08 자동수집 (ai-news)
- 검증: HF 논문 API **초록 원문 전문 실측** (2026-09-08 · 업보트 19 raw와 완전 일치 · 게시 09-03 · 저자 17인)
- 신뢰도: ⭐⭐⭐⭐ (초록 실검증 · 코드/체크포인트 공개 · **수치 표는 초록 밖 미확인**)
