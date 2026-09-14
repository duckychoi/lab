---
title: "SAS — 희소 어텐션 선택기를 증류가 아니라 LM 손실로 직접 학습"
type: source
domain: local-llm
tags: [local-llm, hf-daily-paper, sparse-attention, long-context, triton, flashattention, 선택비용과-중복성]
created: 2026-09-14
updated: 2026-09-14
sources: [raw.md]
reliability: high
identifiers: [arXiv:2609.13141, huggingface.co/papers/2609.13141]
---

# SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking

**HF**: https://huggingface.co/papers/2609.13141 · **arXiv**: 2609.13141
**지표(2026-09-14 HF API 실호출)**: 업보트 **44** · 저자 **9인** · 발행 **2026-09-11**
**드리프트**: raw 43 → 실제 **44**(+1) · 저자 수 **완전 일치** · 발행일 **완전 일치**
**도메인 재판정**: raw `ai-news` → **`local-llm`** 이관. 주제가 *"고정된 어텐션 예산 하에서 무엇을 유지할까"* 이고, 볼트가 [[DeepSeek-V4.1-Flash]](KV 압축)·[[선택비용과-중복성]] 을 local-llm 으로 다뤄 온 축과 동일하다.

> [!insight] 핵심 인사이트 — **문제는 희소화가 아니라 "무엇을 기준으로 순위를 매기나"였다**
> 기존 학습형 희소 어텐션의 구조적 결함을 초록이 한 문장으로 짚는다:
> *"hard Top-K selection that **blocks gradients from the language modeling loss**. Consequently, these methods commonly **distill layer-wise dense attention distributions**."*
>
> **하드 Top-K가 미분 불가능 → LM 손실이 선택기에 도달 못 함 → 어쩔 수 없이 dense 어텐션을 흉내내는 증류로 우회**했다는 것이다.
> 그리고 그 우회가 왜 틀렸는지도 같은 문장에서 적는다: *"the ranking is **not directly aligned with their impact on predictions under a fixed attention budget**"*
>
> 🎯 **dense 어텐션 가중치가 큰 토큰 ≠ 예산이 빡빡할 때 살려야 할 토큰.** dense 모델은 예산 제약이 없으므로, 그 분포를 베껴 봐야 **제약 하의 최적 순위를 가르쳐 주지 않는다.** 증류 목표와 실제 목표가 어긋나 있었다.

> [!insight] 해법 — **게이트를 소프트맥스 "안쪽"에 로그로 넣는다**
> 선택기의 **연속 점수를 어텐션 로짓에 주입**해 표준 역전파로 선택기를 갱신한다. 초록이 *"several choices **crucial** for this simple design to work well in practice"* 라며 3가지를 명시한다 — **전건 원문 확인**:
> ① *"placing the gate **inside the attention softmax in log form**"* — 바깥에 곱하면 정규화가 게이트를 씻어낸다
> ② *"using **normalized softmax gates to calibrate historical context against the always-retained current block**"* — 현재 블록은 **항상 유지**되므로 과거 컨텍스트만 그것과 견주어 캘리브레이션
> ③ *"**preserving continuous selector scores** so the model learns **relative priorities** rather than only hard selections"* — 하드 선택만 배우면 상대 우선순위 정보가 소실
>
> 🎯 **셋 다 "미분 가능하게 만들기" 트릭이 아니라 "무엇을 학습 신호로 남길까"의 문제다.** 이름은 Simple인데 **단순함이 성립하는 조건이 3개나 붙는다.**

> [!warning] 🔴 **초록에 절대 수치가 0개다 — raw의 판정이 정확했다 (볼트 전문 대조 확인)**
> 성능 서술 전문: *"Across reasoning, long-context understanding, and agentic tasks, SAS **consistently outperforms trainable sparse attention baselines** across attention budgets, with **especially large gains under tight budgets**."*
>
> **이 문장에 숫자가 하나도 없다.** 그리고 빠진 것이 숫자만이 아니다:
> - **베이스라인 방법 이름 0개** — *"trainable sparse attention baselines"* 로만 지칭
> - **베이스 모델명 0개** — 어떤 사전학습 트랜스포머에 적용했는지 없음
> - **"tight budget"의 정의 없음** — 예산을 토큰 수로도 비율로도 안 적는다
> - **벤치마크 이름 0개** — 과제 범주(추론·장문맥·에이전트)만
>
> 🔴 **이 페이지에서 SAS의 성능 우위는 어떤 형태로도 인용 금지.** 검증 가능한 것은 **메커니즘(게이트 배치 3원칙)과 커널 제공 사실**뿐이다.

> [!note] 엔지니어링 자산 — 여기는 구체적이다
> *"we implement a **memory-efficient Triton kernel** that integrates SAS into **FlashAttention-style computation**"* — 장문 학습을 지원하기 위한 것이라고 용도를 명시. **성능 주장은 비었지만 구현 경로는 명확하다.**

## 도메인별 추출 (local-llm)

- **실용성 판단**: ⚠️ **판단 보류.** 하드웨어·지연시간·예산 수치가 **전부 없다.** 다만 FlashAttention 통합 Triton 커널은 기존 학습 스택에 얹을 수 있는 형태다.
- **메모리 아키텍처**: RAG/외부DB 아님. **어텐션 내부의 컨텍스트 선택** — [[DeepSeek-V4.1-Flash]] 의 KV 압축(저장 단가)과 **다른 축**이다. 저쪽은 *"KV를 어떻게 작게 저장하나"*, 이쪽은 *"주어진 예산으로 무엇을 볼까"*. **둘은 배타적이지 않고 합성 가능하다.**
- **트레이드오프**: 🔴 **수치 미제공.** 초록이 방향(*"예산이 빡빡할수록 격차가 크다"*)만 적는다.
- **Hermes 적용**: 🟡 **간접.** 지금 당장 ChinameBot에 얹을 형태가 아니다(사전학습 모델 재학습 필요). 다만 **"증류 목표와 실제 목표의 어긋남"** 이라는 진단은 [[온폴리시-증류]] 와 같은 함정이고, 볼트가 다른 증류 사례를 볼 때 쓸 렌즈다.
- **오픈소스 구현체**: 🔴 **초록에 repo 링크가 없다.** 커널 공개 여부 미확인.

> [!action] 당장 할 것
> arXiv 본문에서 **베이스라인 이름·베이스 모델·예산 정의·벤치명**을 확인한다. 초록만으로는 이 논문의 성능 주장을 볼트에 올릴 수 없다. **확인 전까지는 메커니즘 페이지로만 유지한다.**

> [!question] 미해결 질문
> ② *"항상 유지되는 현재 블록"* 은 **블록 단위 희소화**를 전제한다. 토큰 단위 선택과 블록 단위 선택 중 어느 쪽인지 초록이 *"tokens or blocks"* 로 양쪽을 열어 둔다 — **실험이 어느 쪽인지 불명.**

## 관련 페이지
- [[선택비용과-중복성]] — 이 개념의 *"축출(무엇을 버릴까)"* 층에 **"순위 기준을 어디서 배우나"** 라는 질문을 추가한다
- [[DeepSeek-V4.1-Flash]] — 같은 배치. **KV 저장 단가 vs 어텐션 예산 배분**, 직교하는 두 축
- [[온폴리시-증류]] — dense 분포 증류가 **목표 불일치**를 낳는다는 이 논문의 진단과 직결
- [[측정도구-먼저-반증]] · [[한정어-탈락]] — 수치 0개 초록의 취급
- [[Benchmark-Radar]] — 벤치명조차 없는 성능 주장이 왜 문제인지의 반대 사례

## 원본
- 출처: https://huggingface.co/papers/2609.13141
- 신뢰도: ⭐⭐ (HF API 실호출 + 초록 전문 대조. **메커니즘 high · 성능 주장 검증 불가**)
