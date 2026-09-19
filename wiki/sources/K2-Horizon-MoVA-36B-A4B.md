---
title: "IFM/K2-Horizon-MoVA-36B-A4B — 토큰당 4B 활성 MoE + MoVA 어텐션"
type: source
domain: local-llm
tags: [local-llm, hf-model, moe, mova, long-context, agent, terminal-bench]
created: 2026-09-09
updated: 2026-09-19
sources: [K2-Horizon-7B.md]
reliability: medium
---

# K2-Horizon-MoVA-36B-A4B

> [!insight] 핵심 인사이트
> **36B 저장 / 토큰당 4B만 활성**하는 MoE에 **MoVA(Mixture-of-Values) 어텐션**, **네이티브 512K 컨텍스트**. 비교 대상이 **Nemotron 3 Ultra(550B, 활성 55B)** — 저장 기준 **약 15배**, 활성 기준 **약 14배** 큰 모델이다.
> raw의 판정 *"15× 크기 모델 능가는 **축 한정 주장**"* 은 **카드 표로 정확히 확인된다.**

> [!note] 실측 대조 (vs Nemotron 3 Ultra 550B-A55B · 카드 표)
> **이기는 축 — 에이전트/터미널**
> - tau3-Banking(agentic tool use): **26.8 vs 14.2** — 약 1.9배
> - Terminal-Bench 2.1(agentic terminal use): **58.6 vs 53.9** — 표 내 **전 모델 1위**
>
> **지는 축 — 지식/과학추론**
> - GPQA Diamond: **80.8 vs 86.7**
> - Humanity's Last Exam: **25.2 vs 28.4**
> - SciCode: **38.9 vs 39.9**
> - AA-LCR(장문맥 추론): **66.3 vs 71.0**
> - CritPt(프런티어 물리): **2.1 vs 3.1** — 단, **전 모델이 0~3.1점대**로 사실상 전멸
> → **[[Spark-X2.5-4B]] 과 같은 형태의 분기**가 다른 규모에서 재현됐다 → [[에이전트축-분기]]

> [!insight] raw가 놓친 축 — 환각 저항
> **AA-Omniscience Non-Hallucination: K2-Horizon 69.2** vs Nemotron 3 Ultra 70.3 · **Nemotron 3 Super 13.0 · Muse Glimmer-30B 18.1 · Gemma 4 31B 15.0 · Qwen3.6-35B-A3B 49.5**(1위는 G9v3-39A5B **87.0**).
> → **같은 급 오픈웨이트 모델 사이에서 이 지표의 분산이 13~87로 극단적이다.** 사실 정확도(AA-Omniscience Accuracy)는 K2가 18.8로 낮은 편인데 **비환각률은 상위** — *"모르면 모른다고 하는" 성향과 "많이 아는" 성향이 분리 측정된다*는 뜻. 볼트 운영 원칙과 직결되는 지표다.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **조건부.** 활성 4B라 추론은 가볍지만 **가중치 36B를 전부 적재**해야 한다 — 온디바이스라기엔 무겁고 서버로는 가볍다. 512K 컨텍스트는 실사용 가치 큼.
- **메모리 아키텍처**: MoE(라우팅) + **MoVA(Mixture-of-Values)** — 어텐션의 value 쪽을 혼합하는 방식. **카드에 MoVA의 구체적 정의·수식이 부족**해 볼트가 메커니즘을 검증하지 못했다.
- **Hermes 적용**: Terminal-Bench 1위라 **터미널 에이전트 백엔드 후보**로는 매력적. 다만 아래 경고 참조.
- **트레이드오프**: 지식 −6~−7점을 내주고 에이전트 +5~+13점을 얻는 교환.
- **오픈소스 구현체**: Apache-2.0 가중치 공개. **그러나 중간 체크포인트·학습 데이터·코드는 "예고(coming)" 상태로 미공개.**

> [!warning] 신뢰도 유보 — 09-08 규칙 적용
> ① **벤치마크가 전부 자체 보고**이며 제3자 재현을 볼트가 확인하지 않았다. 특히 *"15배 모델 능가"* 는 **저자가 고른 비교군·고른 지표**다.
> ② **미공개 예고 항목**(체크포인트·데이터·코드)이 있다 — 09-08 [[AutoHedge]] 건에서 배운 *"README의 'Coming soon'은 검증되지 않은 약속"* 규칙 적용 대상. 다운로드 3,205로 이 배치 HF 모델 중 최저이며 생성 8일차라 **커뮤니티 검증이 아직 없다**.
> → 신뢰도 **medium**.

> [!action] 당장 할 것
> 지금 받지 말고 **4주 뒤 재확인**: ①다운로드가 1만을 넘겼는가 ②예고한 코드·체크포인트가 실제로 공개됐는가 ③제3자 Terminal-Bench 재현이 있는가. 셋 중 둘이면 그때 평가.


> [!note] 🆕 2026-09-19 — 09-09 "4주 후 재확인"이 형제 [[K2-Horizon-7B]] 로 조기 도착: 중간 체크포인트 공개(69 태그) ✅ · 학습 코드(ifm-ai/xllm, 빈 레포)·기술보고서는 여전히 "In Progress, 9월 말" 🔴

## 관련 페이지
- [[K2-Horizon-7B]]
- [[Spark-X2.5-4B]]
- [[에이전트축-분기]]
- [[Nemotron-3-Nano-Omni]]
- [[Muse-Glimmer-30B]]
- [[Qwen3.6-35B-A3B]]
- [[IFM]]
- [[Long-Horizon-Terminal-Bench]]

## 원본
- 출처: https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B
- 실측(2026-09-09): 다운로드 **3,205**(3회 고정) · ♥247 · gated=False · Apache-2.0 · created 2026-09-01
- raw 대비 드리프트: **완전 일치**
- 신뢰도: ⭐⭐ (자체보고 벤치마크 · 미공개 예고 항목 · 커뮤니티 검증 부재)
