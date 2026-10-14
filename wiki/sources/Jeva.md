---
title: "Jeva — 결정 문제의 4요건을 아키텍처로 못박았다. 저자 2명이고 핵심 수치는 비정량이다"
type: source
domain: ai-news
tags: [ai-news, local-llm, system-one, typed-decisions, permutation-invariance, null-aware, caching, 수치-미제시]
created: 2026-10-14
updated: 2026-10-14
sources: []
reliability: medium
---

# Jeva: System One Models from First Principles

**출처**: https://huggingface.co/papers/2610.18773
**업보트 52**(볼트 실측 · 수집기 47 → **+5**) · 발행 **2026-10-13** · 🔴 **저자 2명**

> [!insight] 핵심 인사이트 — **"직렬화된 텍스트로 답을 예측하는 관행"을 정면으로 비판한다**
> 초록 1~2문장이 논점이다: System One 모델은 저지연 결정을 가능하게 하지만, *"recent practice of predicting an answer from **serialized text** does not, by itself, respect the **structure of a decision problem**."*
> 🎯 ⇒ **텍스트로 선택지를 늘어놓고 생성시키는 방식 자체가 결정 문제의 구조를 위반한다**는 주장이다. 그 구조를 **4요건**으로 명시한다.

> [!note] 📐 4요건 — 이 논문의 진짜 기여
> | # | 요건 | 내용 | 직렬화 텍스트의 문제 |
> |---|---|---|---|
> | i | **null-aware** | 답 부재와 후보 간 불확실성을 **구별** | 둘을 같은 저확률로 뭉갠다 |
> | ii | **permutation-invariant** | 선택지 순서를 바꿔도 결정 불변 | 순서가 결과를 바꾼다 |
> | iii | **option-scalable** | 후보 집합이 늘어도 출력 공간 재정의 불필요 | 고정 라벨 집합이 한계 |
> | iv | **cacheable** | 반복되는 선택지에 대한 **요청 독립 연산을 재사용** | 매 요청 전체 재계산 |
>
> 🏆 **볼트 관측: (iv) cacheable 이 [[VideoJev]] 의 Cached inference 와 같은 아이디어다.** 같은 날 올라온 두 논문이 **캐시 가능성을 독립적으로 1급 설계 요건으로 올렸다** → [[System-One-모델]]

> [!insight] 아키텍처 — 비대칭 구조가 핵심이다
> - **공용 인코더**가 **요청과 각 선택지를 독립적으로** 표현한다
> - **컴팩트한 decision stack** 이 **불변 선택지 메모리(immutable option memory)에 대해 요청 상태만 정제**한다
> - **대칭 집계(symmetric aggregation)** → 순열 **등변(equivariant)** 확률
> - **공유 점수화** → 가변 크기 후보 집합 수용
> - **별도의 coverage 추정** → 답 부재 vs 후보 경쟁 구별 = 명시적 null 출력
>
> 🎯 **비대칭이 전부다**: 선택지는 **불변(immutable)** 이고 요청만 갱신된다 ⇒ **선택지 표현을 요청 간에 재사용**할 수 있다(= iv 달성). 이것이 Choice/Noul/Score 출력을 통합하는 근거다.

> [!warning] 🔴 **핵심 주장 3개 중 2개가 비정량이다 — 볼트 초록 전문 확인**
> 원문: *"Jeva combines strong typed-decision performance with **near-perfect null detection** and **no decision flips under any tested permutations**. It scales to **thousands of candidates** and **substantially reduces latency** through cross-request reuse **without changing decisions**."*
>
> | 주장 | 정량성 | 볼트 판정 |
> |---|---|---|
> | 순열 하 **결정 반전 0건** | ✅ **정량**(0건) | 가장 강한 주장 — 단 *"tested"* 순열 범위가 미제시 |
> | **null 검출 "거의 완벽"** | 🔴 **비정량** | 수치 0개 |
> | **지연 "상당히" 감소** | 🔴 **비정량** | 배수·ms 0개 |
> | typed-decision 성능 "strong" | 🔴 **비정량** | 벤치명·점수 0개 |
>
> ✅ **수집기 판정 *"'거의 완벽'·'상당한 지연 감소'의 구체 수치가 초록에 없다"* 가 정확하다.**
> 🆕 **볼트 추가 2건**: ① **"strong typed-decision performance"도 비정량이다** — 수집기가 이건 안 지적했다. **벤치마크 이름이 초록에 하나도 없다.** ② **지연 감소에 조건이 붙어 있다**: *"without changing decisions"* — 즉 **캐시 재사용이 결정을 바꾸지 않는다는 것이 주장의 일부**다. 캐시가 정확도를 깎는 흔한 트레이드오프를 **피했다고 주장**하는 것이고, 이건 수치가 있어야 믿을 수 있는 종류다.

> [!warning] 🔴 **저자 2명 — 금일 논문 중 최소이고 [[VideoJev]] 의 1/9 다**
> 볼트 API 실측: Jeva **2명** vs VideoJev **18명** · X-Ragent **12명** · TPPO **9명** · Urbex **8명**.
> ⚖️ **저자 수는 품질 지표가 아니다.** 그러나 **업보트 3위(52)이면서 벤치 수치가 0개이고 저자가 2명**인 조합은 적어 둔다 — *"from First Principles"* 라는 제목이 **이론 제안 성격**임과 일관된다.
> 📌 ⇒ **이 논문은 "측정 결과"가 아니라 "설계 원칙"으로 읽어야 한다.** 그러면 수치 부재가 결함이 아니라 성격이다. 🔴 **단 초록이 "strong performance"·"near-perfect"라고 **성능 주장을 하므로** 면제되지는 않는다.

## 도메인별 추출 (local-llm 교차)

- **실용성 판단**: 🔴 **현 시점 판정 불가.** 코드·가중치·모델 크기가 초록에 없다. **지연 수치가 없어 "저지연"이라는 전제 자체가 미검증이다.**
- **메모리 아키텍처**: 🏆 **볼트 관심 축에 정확히 들어온다.** *"immutable option memory"* + *"request-independent option representations … support reuse across newly assembled sets"* ⇒ **외부 DB·RAG 가 아니라 "불변 후보 표현 캐시"** 형태다. 📌 **[[local-llm]] 의 에이전트 메모리 분류에 새 칸이 필요하다**: RAG/KV/압축/외부DB 어디에도 정확히 안 들어간다 — **"선택지 측 캐시"** 다.
- **Hermes/ChinameBot 적용**: ⚖️ **직접 적용은 불가**(구현체 없음). 🎯 **그러나 패턴은 적용 가능하다**: 봇이 **고정된 후보 집합**(명령어·FAQ·메뉴)에 대해 반복 분류할 때, **후보 측 임베딩을 선계산·고정하고 요청만 갱신**하는 구조가 (iv)의 저가형 구현이다. 📌 **이건 지금 당장 할 수 있다.**
- **트레이드오프**: 🔴 **수치가 없어 적을 수 없다.** 유일한 정량값이 "결정 반전 0건"이다.
- **오픈소스 구현체**: 🔴 **초록에 없다.** ⚖️ **주의**: 트렌딩 모델 `autotrust/JEV-35B` 가 `system-one`·`noul`·`choice`·`score` 태그를 달고 조어 `Noul` 까지 일치하지만, **그 카드가 인용한 arXiv 는 `2609.14973`(구논문)이고 본 논문(`2610.18773`)이 아니다** ⇒ 🔴 **"JEV-35B 는 Jeva 의 구현체"라고 적으면 틀린다.** ✅ 수집기 교차검증 판정을 볼트가 수용한다.

> [!question] 미해결
> - **벤치마크 이름·점수 전무** — 어떤 typed-decision 과제로 평가했는지 초록에 없다. 📌 해소 경로 = arXiv 본문. **금일 미시도.**
> - *"any tested permutations"* 의 **테스트 범위**(순열 수·후보 수) 미제시 — "0건"의 분모를 모른다.
> - null 검출 "거의 완벽"의 지표(정밀도/재현율) 미제시.
> - 지연 감소 배수 미제시.
> - `JEV-35B` ↔ `2609.14973` ↔ 본 논문의 **계보 관계 미확인**(같은 그룹인지 불명).

## 관련 페이지
- [[VideoJev]] — 🏆 **cacheable ↔ Cached inference 동일 아이디어** · 같은 배치
- [[System-One-모델]] — 🆕 금일 신설 개념
- [[Urbex]] — 같은 배치
- [[SearchJev]] — 볼트 기보유 Jev 계열 소스(관계 **미확인**)
- [[임계-의존-성공률]] · [[관심-검증-역상관]] — 🆕 **업보트 52 · 벤치 수치 0개**
- [[local-llm]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.18773
- 수집: 2026-10-14 자동수집(ai-news) · 인제스트 2026-10-14
- 볼트 실측: HF Papers API HTTP 200 — 업보트 **52**(수집기 47) · publishedAt **2026-10-13** · 저자 **2명** · 초록 전문 수신·전수 검색
- raw 대비: ✅ 4요건·"거의 완벽"·"상당한 지연 감소" 비정량 판정 **일치** · ✅ JEV-35B 구논문 인용 경고 **수용** · 🆕 **볼트 추가 3건**: *"strong typed-decision performance"도 비정량*(수집기 미지적) · *"without changing decisions"* 조건 발굴 · **저자 2명 = 금일 최소**(VideoJev 의 1/9)
- 신뢰도: ⭐⭐ (설계 원칙은 명료 / 🔴 **벤치 이름조차 없음 · 구현체 없음**)
