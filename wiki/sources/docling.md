---
title: "docling — 문서를 LLM 입력으로 바꾸는 층이 ★67,310까지 왔다"
type: source
domain: ai-news
tags: [ai-news, github, document-parsing, rag, pdf, context-engineering, 하네스-설계-축]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: high
---

# docling

> [!insight] 핵심 인사이트 — 모델이 아니라 **입력의 표준형**을 만든다
> PDF·DOCX·PPTX·XLSX·HTML·EPUB·이미지·LaTeX에 더해 **WAV/MP3/WebVTT 오디오까지** 하나의 `DoclingDocument` 표현으로 수렴시킨다. PDF는 페이지 레이아웃·읽기 순서·표 구조·수식·코드까지 분해한다.
> 🎯 **이 레포의 자리는 "무엇을 읽느냐"가 아니라 "읽은 것을 어떤 모양으로 넘기느냐"다.** [[하네스-설계-축]] 이 *모델을 바꾸지 않고 감싸는 층을 바꾼다* 고 했을 때, docling은 그 층의 **가장 앞단**이다.
> ✅ **자체 논문 보유**: arXiv 2408.09869(README 배지 실확인). 추가로 DocTags(2503.11576)·DocLayNet(2206.01062) 을 README 안에서 직접 참조한다 — **포맷 자체를 논문으로 정의**하는 방식.
> ✅ **LF AI & Data 배지 실확인**(README 27행). 조직 위치 **Switzerland**(IBM Research Zurich 계열 — VLM 경로가 `ibm-granite/granite-docling-258M`).

> [!note] 📌 볼트 실측 (2026-09-20, GitHub API)
> ★**67,310** · fork **4,845** · **MIT** · Python · created **2024-07-09** · pushed 2026-09-18 · archived false
> **open issues 935** — 수집기 분해(이슈 809 / PR 126) **합계 정확히 일치**.
> **issues:PR = 6.4:1 — 이번 배치 5건 중 유일한 "이슈 적체형"** ([[mem0]] 0.74:1 · [[TensorRT-LLM]] 0.66:1 은 반대). 🎯 **파서는 사용자가 깨진 입력을 들고 오고, 추론 런타임은 기여자가 패치를 들고 온다** — 비율의 부호가 그 차이를 보여준다(추정, 미검증).
> **open issues / ★ = 1.39%** — 중위값 대역.
> ⚠️ 수집기 기록 ★67,301 → 볼트 실측 **67,310**(+9, **+0.013%**). [[상대속도-가림]] 대역 이하의 드리프트.
> `topics` **15개** — 이번 배치에서 가장 많다([[higgsfield]] 9 · [[PageIndex]] 12 · [[TensorRT-LLM]] 5 · [[mem0]] 14).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ★67,310 · MIT · **자체 논문 3편 참조** · LF AI & Data · 2년 2개월 연속 개발. 이번 배치 최상위.
- **즉시 활용**: **YES.** 볼트의 `/obsi-cleanmk`·[[mark-clean]] 계열이 **웹 페이지**를 처리한다면 docling은 **로컬 문서**를 처리한다 — 겹치지 않고 보완한다. 오디오(WAV/MP3/WebVTT) 파싱이 붙어 있어 `/down-analysis` 트랜스크립트 경로와도 접점이 있다.
- **6개월 영향력**: 🎯 **"어떤 청킹이냐"가 아니라 "어떤 문서 표현이냐"로 RAG 논쟁의 층이 내려간다.** 같은 배치의 [[PageIndex]] 가 *인덱스 구조*를 바꾸는 동안 docling은 *그 앞의 표현*을 표준화한다 — **두 레포는 경쟁이 아니라 직렬**이다.
- **대체 관계**: unstructured·PyMuPDF 류 파서를 대체한다. WebFetch/defuddle 는 대체하지 않는다(대상이 다르다).
- **허와 실**: 🔴 **README에 정확도 표가 없다.** "레이아웃·읽기 순서·표 구조를 분해한다"는 **기능 목록**이고, *얼마나 정확히* 분해하는지는 README 안에서 확인되지 않는다 — 수치는 인용 논문 쪽에 있다. **기능 주장과 품질 근거가 다른 문서에 있다**는 점을 병기해야 한다.
- **액션**: 볼트의 실제 PDF(논문 PDF·화이트페이퍼)로 표 추출 정확도를 직접 잰다. → 🎯 **마침 이번 배치에 대상이 있다**: [[Ternary-Bonsai-2-27B]] 의 근거는 **GitHub에 올라온 PDF 화이트페이퍼**다. docling으로 그 PDF의 벤치 표를 뽑으면 **볼트가 못 읽은 표를 읽는 동시에 docling을 검증**한다.

> [!action] 당장 할 것
> `pip install docling` → **Bonsai-2 화이트페이퍼 PDF**(`PrismML-Eng/Bonsai-demo/bonsai-2-27b-whitepaper.pdf`)를 파싱해 14개 벤치 표를 추출한다. 성공하면 도구 검증 + [[Ternary-Bonsai-2-27B]] 의 미확인 수치 해소가 **한 번에** 된다.

> [!question] 미해결 질문
> 표 추출 정확도 수치가 README에 없다. 인용 논문(2408.09869)에 있는지 미확인 — **이번 인제스트는 README까지만 읽었다.**

## 관련 페이지
- [[PageIndex]]
- [[mem0]]
- [[하네스-설계-축]]
- [[컨텍스트-엔지니어링]]
- [[ai-news]]

## 원본
- 출처: https://github.com/docling-project/docling
- 볼트 실측(2026-09-20, GitHub API): ★**67,310** · fork 4,845 · **MIT** · Python · open issues **935** · created 2024-07-09T07:50:26Z · pushed 2026-09-18T13:47:32Z · archived false · topics 15 · homepage docling-project.github.io/docling
- raw 대비: ★ +9(0.013%) · 이슈/PR 분해 **합계 일치** · 볼트 추가 = **LF AI & Data 배지·arXiv 3편 README 실확인** · **issues:PR 부호가 배치 내 유일하게 반대** · **README 내 정확도 표 0개**
- 신뢰도: ⭐⭐⭐ (지표·거버넌스·논문 전부 실확인 / 품질 수치는 README 밖)
