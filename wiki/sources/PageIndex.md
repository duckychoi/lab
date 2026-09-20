---
title: "PageIndex — 관련성 판단을 검색기에서 모델로 옮긴 두 번째 독립 사례"
type: source
domain: ai-news
tags: [ai-news, github, rag, vectorless, retrieval, reasoning, 관련성-판단-주체, 하네스-설계-축]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: high
---

# PageIndex

> [!insight] 🎯 핵심 인사이트 — 볼트가 09-03에 연 축이 **두 번째 사례**를 얻었다
> README 44행 원문: *"Vector-based RAG retrieves by semantic **similarity**. But **similarity ≠ relevance** — what retrieval actually needs is relevance, and **relevance requires reasoning**."*
> 청킹·임베딩·벡터DB를 **전부 제거**하고 문서를 **계층 트리 인덱스**로 만든 뒤 LLM이 그 트리를 탐색한다. 검색 단계 자체가 LLM 추론이다.
>
> 📌 **[[에이전트-메모리-레이어]] 가 09-03에 [[Declarative-Attention]] 으로 연 축이 정확히 이것이다** — 볼트 원문: *"**관련성 판단의 주체**가 바뀐 것이 핵심이다: RAG는 검색기가, 프록시 점수 방식은 외부 스코어러가, 이건 **모델 자신이** 판단한다."*
> 🎯 **두 사례의 층이 다르다**: Declarative-Attention은 **KV 캐시 읽기**에서, PageIndex는 **문서 검색**에서 같은 이동을 한다. **독립된 두 층에서 같은 방향이 나온 것**이므로 축으로 승격할 근거가 생겼다 → [[관련성-판단-주체]].

> [!warning] 🔴 수집기 정정 — *"비용이 수치로 제시되지 않았다"* 는 사실과 다르다
> 수집기 raw: *"트리 생성 비용이 LLM 호출에 비례한다는 점은 README에 **수치로 제시되지 않았다**."*
> 🔴 **README 117·126·153행에 전부 있다:**
> - 인덱싱 **약 $0.001/page**(`gpt-5.6-luna`), 1,000쪽 교과서 = **1달러 조금 넘음, 수 분, 1회성**
> - 인덱싱 시간 **13초 ~ 4.5분**(9~1,098쪽 PDF 9건), 기준선 **$0.0011/page**
> - 원문 PDF 통째 투입 대비: **52쪽에서 2.1배 · 420쪽에서 16.6배 비쌈**(`gpt-5.6-sol`, 프롬프트 캐싱 제외), **805쪽에서는 컨텍스트에 아예 안 들어감**
>
> 📌 **볼트가 09-19에 수집기에 보낸 요청 1**(*"'수치 0개' 3건은 전부 본문에 표가 있었다"*)이 **README 층에서 재발**했다. 이번엔 본문도 아니고 **README 안**이다.

> [!note] 🎯 벤치 설계가 정직하다 — 실패 모드를 격리했다
> **PageIndex-OSS-Benchmark**(별도 레포): **62개 조회 질문 · 34개 PDF · 1,945쪽**, 출처는 MMLongBench-Doc-V2.
> README 139행: *"Every question's answer is a fact stated in running text, so a wrong answer is a **retrieval or reading failure, not a reasoning one**."*
> 🎯 **틀린 답의 원인을 추론 실패와 분리하도록 데이터를 고른 것** — 볼트가 여러 벤치에서 없다고 적어 온 설계다.
> ✅ 하네스·데이터·러너 **전부 별도 공개**(PageIndex-OSS-Benchmark · MMLongBench-Doc-V2).

> [!warning] ⚠️ 다만 두 가지가 걸린다
> 1. 🔴 **정확도 수치가 그림 안에 있다.** `results-light.png` = *"Accuracy against average cost per question"* — **표가 아니라 차트**다. 볼트는 정확도 값을 전사하지 못했다. 📌 볼트 자기한계 1번(*"그림 속 수치 미전사"*)이 또 걸렸다 — **비용은 텍스트, 정확도는 그림**이라는 배치가 우연인지 아닌지는 확인 못 했다.
> 2. ⚠️ **자기 벤치·자기 데이터셋이다.** MMLongBench-Doc-V2 도 `VectifyAI` 소유다. [[m-a-p]] 가 [[YuE2-3B]] 를 자기 WildSongBench로 잰 것과 **같은 형태**다. 🎯 **단 PageIndex 쪽이 낫다** — m-a-p는 비교군을 골라 보였고, 여기는 러너·데이터·결과를 전부 열어 뒀다. **닫힌 자기평가가 아니라 열린 자기평가**다.

> [!note] 📌 볼트 실측 (2026-09-20, GitHub API)
> ★**35,766**(raw **완전일치**) · fork **3,152** · **MIT** · Python · created **2025-04-01**(1년 5개월) · pushed **2026-09-20T07:22:54Z**(배치 5건 중 **가장 최근**) · archived false
> **open issues 107** — 수집기 분해(이슈 34 / PR 73) **합계 정확히 일치**.
> **open issues / ★ = 0.30% — 배치 최저.** `topics` 12개.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ★35,766 · MIT · **벤치 레포·데이터셋 레포 분리 공개** · 비용 수치 텍스트 명시. 이번 배치에서 [[docling]] 과 함께 최상위.
- **즉시 활용**: **YES, 조건부.** SDK 로컬 모드로 자기 LLM 키만 있으면 색인·검색이 돈다. 🔴 단 **인덱스 생성이 LLM 호출**이므로 문서가 많으면 초기 비용이 실재한다 — 위 수치로 계산 가능하다(1,000쪽 ≈ $1).
- **6개월 영향력**: 🎯 **"임베딩을 고르는 일"이 "탐색 모델을 고르는 일"로 바뀐다.** README 102행이 직설적이다 — *"`chat=`: **use the best model you can afford**"*. 비용이 임베딩 인프라에서 **추론 토큰**으로 이동한다.
- **대체 관계**: 벡터DB(Qdrant·Chroma 등)를 **제거 대상**으로 명시. 반대로 [[docling]] 과는 **직렬**이다 — docling이 문서를 표현으로, PageIndex가 표현을 인덱스로.
- **허와 실**: 마케팅을 걷어내도 **비용 비교는 남는다**(420쪽 16.6배 · 805쪽 미적재). 🔴 걷어내야 할 것은 정확도 쪽이다 — **그림 안에만 있다.**
- **액션**: 볼트의 긴 PDF(논문·화이트페이퍼)로 로컬 모드 색인 1건 → 같은 질문을 원문 투입과 비교. **[[docling]] 파싱 → PageIndex 색인**을 한 파이프라인으로 세워 본다.

> [!action] 당장 할 것
> `results-light.png` 를 내려받아 **정확도 수치를 직접 읽는다** — 볼트 자기한계 1(그림 속 수치)을 **이번에 한 건이라도 깬다.** 그림 1장이면 된다.

## 관련 페이지
- [[관련성-판단-주체]]
- [[Declarative-Attention]]
- [[에이전트-메모리-레이어]]
- [[docling]]
- [[mem0]]
- [[하네스-설계-축]]
- [[m-a-p]]
- [[VectifyAI]]
- [[ai-news]]

## 원본
- 출처: https://github.com/VectifyAI/PageIndex
- 볼트 실측(2026-09-20, GitHub API): ★**35,766**(raw 완전일치) · fork 3,152 · **MIT** · Python · open issues **107**(이슈 34/PR 73 합계 일치) · created 2025-04-01T10:53:54Z · pushed 2026-09-20T07:22:54Z · topics 12 · homepage pageindex.ai
- 수치 출처: README 44·102·117·126·139·153행 **원문 실열람**
- raw 대비: 볼트 추가 = 🔴 **수집기 "수치 없음" 정정(비용 수치 3종 실재)** · **[[관련성-판단-주체]] 축의 두 번째 독립 사례로 승격** · **벤치 실패모드 격리 설계 확인** · ⚠️ **자기 데이터셋(MMLongBench-Doc-V2도 VectifyAI)** · 🔴 **정확도는 그림 안**
- 신뢰도: ⭐⭐⭐ (지표 완전일치 · 비용·시간 수치 텍스트 명시 · 하네스/데이터 공개 / 정확도 수치는 그림, 자기 데이터셋)
