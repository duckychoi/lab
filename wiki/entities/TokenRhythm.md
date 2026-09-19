---
title: TokenRhythm
type: entity
domain: local-llm
tags: [local-llm, hf-model, qwen-derivative, agent, post-training, rsi, 신설]
created: 2026-09-18
updated: 2026-09-19
sources: [NeoHorse-1-4B.md, NeoHorse-1-9B.md, NeoHorse-1-Paper.md]
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

> [!note] ✅ 2026-09-19 해소 — **소속 확인됨** (모논문 부록 A → [[NeoHorse-1-Paper]])
> ```
> 1 TokenRhythm Technologies   2 Infinigence AI   3 Tsinghua University
> 4 Peking University          5 CUHK             6 Visionplus Capital
> 7 WX Capital                 8 Alibaba Group
> 교신저자: Yunhe Wang(1) · Yu Wang(3)    저자 37명(Core 18 · Contributors 18 · "NeoHorse Team")
> ```
> - 회사 실체: **TokenRhythm Technologies** · 홈페이지 `tokenrhythm.ai`(README 배지) · 모델은 HF와 **ModelScope** 동시 배포
> - 🎯 **라우팅 하네스 운영사다** — 논문 데이터가 자사 배포 하네스(OpenSquilla 포함)의 실제 트래픽 궤적 10⁵~10⁶ 개. README가 OpenSquilla X 계정을 함께 링크 → 하네스 제품과 모델 팀이 같은 조직권으로 보인다(🔴 명시 문장 없음, 볼트 추정)
> - 📌 **[[Alibaba]] 소속 공저자 2명** — 베이스(Qwen3.5) 제작사 인원이 파생 사후학습 논문에 참여
> - 🔴 **국적·규모(인원·자금)는 여전히 미확인** — 본문에 명시 없음. 투자사 2곳(Visionplus·WX Capital) 소속 저자가 있다는 사실만 확인
> - 🔴 **정정**: 위 인사이트 박스의 "업보트 421 · 코드 ★535" → 09-19 실측 **170 · ★599**, 그리고 레포는 **학습 코드 없음**(README·PDF·추론 예제 2개)

## 산출물
- [[NeoHorse-1-4B]] — 4.21B · DL 19,789 · ♥2,354 · 10벤치 평균 64.87(+5.93) · **10개 축 전부 양(+)**
- [[NeoHorse-1-9B]] — 8.95B · DL 9,856 · ♥881 · 평균 69.04(+3.44) · 🔴 **IFEval −0.37 · IFBench/LCB +0.00**
- [[NeoHorse-1-Paper]] `arxiv:2609.08183` — 업보트 **170**(09-19) · ★599 · ✅ **2026-09-19 인제스트** · 🎯 핵심 증거 = 데이터 출처 대조 +6.26 · 🔴 루프 1회·커리큘럼 절제 없음

> [!action] 당장 할 것
> ~~논문 2609.08183 인제스트 + 조직 정보 조회~~ ✅ **2026-09-19 완료** → [[NeoHorse-1-Paper]]. 🔴 9B 지시수행 회귀의 **원인은 논문에도 없다**(저자는 하락만 인정).
> 🎯 **다음**: NeoHorse 루프 **2회차** 공개 추적 — RSI 주장의 유일한 검증 경로.

## 관련 페이지
- [[NeoHorse-1-Paper]]
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
- 모논문: https://arxiv.org/abs/2609.08183 (부록 A 소속 · 2026-09-19 볼트 본문 확인)
- 신뢰도: ⭐⭐ (모델 지표 API 실측 일치 · 라벨 정직 · 소속 확인 ✅ · 🔴 학습 코드/데이터 비공개 · 국적·규모 미확인)
