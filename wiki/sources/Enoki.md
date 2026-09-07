---
title: Enoki — 환각 탐지에서 "claim↔span 정렬 단계"를 표현 하나로 없앤 논문
type: source
domain: ai-news
tags: [ai-news, hf-paper, hallucination, factuality, open-ie, evaluation, dataset]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: high
---

# Enoki: Efficient Multi-Level Hallucination Detection

**arXiv**: 2609.00581 · **HF 업보트 12** · **공개 2026-09-01**
**저자 8인**: Elisei Rykov, Timur Ionov, Nikolay Ivanov, Maksim Savkin, Maksim Makarenko, **Alexander Panchenko** 외

> [!insight] 핵심 인사이트 — **두 층을 잇는 비용이 문제였고, 답은 "잇지 말고 하나로 표현하라"**
> 기존 환각 탐지는 **한 층에서만** 돈다:
> - **claim 수준** — 해석 가능한 사실 단위를 준다
> - **span 수준** — 근거 없는 텍스트의 **위치**를 잡는다
> 둘을 이으려는 순간 비용이 터진다: LLM 중심 파이프라인은 **분해·검증 호출을 여러 번** 하고, 모듈형 시스템은 **claim-to-span 정렬** 단계를 따로 둬야 한다.
> Enoki는 **Open IE로 텍스트에 앵커된 관계 사실(text-anchored relational facts)** 을 뽑는다. 사실이 처음부터 **원문 위치에 붙어 있으므로**, 지지되지 않는 사실을 **span으로 역투영(project back)** 하면 끝이다. **정렬 단계가 필요 없어지는 게 아니라 존재할 이유가 없어진다.**

> [!insight] 볼트 교차 — **"중간 정렬 단계 제거"가 이 배치에서 두 번 나왔다**
> 같은 배치 [[Motion-Omni]] 은 *음성→모션* 캐스케이드의 **두 번째 추론 패스**를 없앴다. 방법은 **음성을 만드는 hidden state에서 모션을 바로 뽑는 것** — 즉 **공유 표현**.
> Enoki는 *claim→span* 정렬 단계를 없앴다. 방법은 **텍스트에 앵커된 사실 표현** — 즉 **공유 표현**.
> **서로 무관한 두 도메인(아바타 생성 / 사실성 검증)에서 같은 날 같은 처방이 나왔다**: *파이프라인 두 단계를 잇는 비용이 크면, 잇는 방법을 개선하지 말고 **두 단계가 같은 표현을 쓰게 하라**.*
> → 볼트의 [[선택비용과-중복성]] 과 다른 축이다. 그쪽은 *"선택을 없앤다"* 였고 이건 **"변환을 없앤다"** 다. 새 관측 축으로 기록한다.

> [!note] 추출기를 갈아끼울 수 있다 — 정확도·비용의 다이얼
> *"Enoki supports **LLM-based, encoder-based, and rule-based** extraction regimes, balancing accuracy and inference cost through a common interface."*
> 같은 인터페이스 아래 **LLM / 인코더 / 규칙** 중 선택. 볼트의 [[local-llm]] 축에서 반복된 *"비용을 내리려면 무엇을 포기하나"* 가 **설정값으로 노출**된 사례이며, 규칙 기반까지 지원한다는 건 **LLM 없이도 돌아가는 경로**가 있다는 뜻이다.

> [!warning] 성능 주장의 정확한 형태 — **대등 + 우위의 조합이지 전면 우위가 아니다**
> 초록 원문: *"Enoki **remains competitive with** strong claim-level systems **while using fewer resources** and achieves **superior performance on fine-grained span- and entity-level localization**."*
> 정확히 두 가지다:
> 1. **claim 수준** — 강한 기존 시스템과 **대등**, 단 **자원을 덜 씀**
> 2. **span·엔티티 수준 위치추정** — **우위**
> *"환각 탐지에서 SOTA"* 로 뭉뜽그리면 **틀린다.** claim 층에서는 이기지 않았다.
> 🔴 **그리고 초록에 구체 수치가 하나도 없다.** raw 기재(*"초록에 구체 수치는 제시되지 않음"*)가 **정확**하다. 볼트 규칙상 **위 두 문장 이상은 인용 금지**.

> [!note] EnokiQA — 이 배치 세 번째 벤치마크 공개
> *"dual-granularity dataset with **aligned** claim-level verification and span-level localization annotations."*
> **두 층의 주석이 서로 정렬된** 데이터셋은 드물다. 정렬 단계를 없앤 방법이 **정렬된 평가셋**을 함께 낸 것은 일관된 설계다.
> [[Motion-Omni]](SwDA-500) · [[WorldSculpt]](UE-MeshyScene) · Enoki(EnokiQA) — **논문 5건 중 3건이 벤치마크 동반**. → [[검사가능성-공사]] 갱신 근거.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — HF 논문 초록 원문 대조·데이터셋 공개 선언·업보트 12. **감점**: 수치 전무.
- **즉시 활용**: **조건부 YES.** 이 볼트가 **정확히 이 문제를 갖고 있다** — 위키 페이지의 주장이 소스에 실제로 근거하는지 검증하는 문제. 특히 **span 역투영**은 *"이 문장의 근거가 원문 어디인가"* 를 자동으로 잡는 것이라, 볼트의 `- 출처:` 규율을 **문장 단위**로 내릴 수 있다.
- **6개월 영향력**: 환각 탐지가 **claim/span 둘 중 하나**를 고르는 문제에서 **하나의 표현으로 둘 다**로 옮겨가면, 검증 비용이 내려가 **인제스트 시 자동 사실검사**가 현실적 옵션이 된다.
- **대체 관계**: 볼트가 쓰는 도구 중 대체 대상 없음. [[DRIFT]]·[[Personalization-Mirage]] 와 **같은 사실성 축**.
- **허와 실**: 마케팅을 걷어내면 **"Open IE를 환각 탐지에 재적용하고 정렬 단계를 없앴다"** 이다. Open IE 자체는 오래된 기법이고, 신규성은 **적용 위치**에 있다. **수치가 없으므로 효과 크기는 미판정.**
- **액션**: 아래.

> [!action] 당장 할 것
> **EnokiQA 공개 위치와 라이선스 확인.** 방법을 안 써도, *"claim 검증 + span 위치추정이 정렬된"* 평가셋은 볼트가 **자기 인제스트 정확도를 재는 도구**로 전용할 수 있다. 볼트에는 현재 **자기 출력의 사실성을 재는 수단이 전혀 없다** — 이게 [[LLM-Wiki]] 의 확인된 공백이다.

> [!question] 미해결
> **Open IE 추출기가 놓친 사실은 어떻게 되는가.** 추출되지 않은 주장은 검증 대상에서 **조용히 빠진다**. 재현율(recall) 수치가 없어 이 실패 모드의 크기를 알 수 없다 — **이 방법의 가장 큰 미확인 위험**이며, 수치 부재가 정확히 여기서 아프다.

## 관련 페이지
- [[DRIFT]] · [[Personalization-Mirage]] · [[Motion-Omni]] · [[WorldSculpt]] · [[Ask-Before-You-Optimize]] · [[검사가능성-공사]] · [[LLM-Wiki]] · [[RAG vs LLM-Wiki]] · [[에이전트-메모리-레이어]] · [[open-science]]

## 원본
- 출처: https://huggingface.co/papers/2609.00581 (arXiv 2609.00581)
- 수집: 2026-09-07 자동수집 (ai-news)
- 검증: HF 논문 API 초록 원문 대조 (2026-09-07 · 업보트 12 raw와 일치)
- 신뢰도: ⭐⭐⭐⭐ (초록 검증 · **정량 수치 전무**)
