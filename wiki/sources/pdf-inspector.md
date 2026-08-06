---
title: firecrawl/pdf-inspector — Rust PDF 분류·텍스트 추출
type: source
domain: ai-news
tags: [ai-news, github-trending, pdf, rust, ocr, document-pipeline, preprocessing, firecrawl]
created: 2026-08-04
updated: 2026-08-05
sources: []
reliability: high
---

# firecrawl/pdf-inspector — 스캔본 vs 텍스트 PDF 자동 판별·추출

**GitHub**: https://github.com/firecrawl/pdf-inspector
**스타수**: ⭐9,016 (2026-08-04 자동수집, 당일 **+1,699**) · **제작**: [[Firecrawl]]
**스택**: Rust · **성격**: 문서 파이프라인 전처리 라이브러리

> [!update] 2026-08-05 갱신 — ⭐10,636 (당일 +2,540 급상승)
> ⭐**10,636**(2026-08-05 자동수집, 당일 +2,540 급상승) ← 9,016(08-04). 하루 새 +2,540으로 **1만 스타 돌파** — [[Firecrawl]] Rust PDF 스캔/텍스트 판별·OCR 분기 전처리의 관심 급확대. [[Unlimited-OCR]] 한국어 PDF 게이트에 "스캔본 분류→OCR 분기" 전처리 편입 actionable 유지. reliability high 유지. *raw 자동수집 수치 반영 — 실WebFetch 미수행(타임라인 유지).*

> [!insight] 핵심 인사이트
> **PDF가 "스캔 이미지 기반"인지 "텍스트 레이어 기반"인지 자동 판별하고 텍스트를 추출**하는 Rust 라이브러리. raw 한줄요약 기준 핵심 가치는 *분류*에 있다 — 문서 파이프라인에서 가장 먼저 필요한 결정이 "이 PDF는 그냥 텍스트를 뽑으면 되는가, OCR로 보내야 하는가"인데, 이 분기(OCR routing)를 값싸게 자동화한다. [[Firecrawl]]이 만든 만큼 "웹/문서 → LLM 정제 데이터"라는 그들의 수집 인프라 계보와 정확히 맞물린다 — 크롤링([[Firecrawl]] 코어)의 문서 버전 전처리 말단. OCR 자체를 하는 도구([[Unlimited-OCR]]·olmocr)와 달리, **OCR을 *언제* 부를지 결정하는 게이트키퍼**라는 점이 위치를 가른다.

> [!note] 배경 정보
> 문서 인제스트 파이프라인은 보통 ①입력 PDF 분류 → ②텍스트 레이어 있으면 직접 파싱 → ③없으면(스캔본) OCR → ④정제·청킹 순인데, ①단계를 대충 하면 텍스트 PDF에 불필요한 OCR을 돌려 비용·오류가 폭증하거나, 스캔본을 텍스트로 오인해 빈 결과를 낸다. pdf-inspector는 이 ①을 Rust로 빠르게 처리 — 대량 배치에서 OCR 호출량을 줄이는 비용 최적화 지점.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐9,016·당일 +1,699 급성장 + [[Firecrawl]](웹→LLM 데이터 수집 표준) 제작이라 실체 신뢰도 상위. raw 자동수집 수치, 세부 판별 정확도·라이선스 원문은 미검증(실WebFetch 미수행, 타임라인 유지).
- **즉시 활용**: YES(후보) — 내 문서/자료 인제스트에서 PDF가 섞일 때 "OCR 분기 전처리"로 바로 편입 가치. [[Unlimited-OCR]] 게이트 아이디어(한국어 PDF)와 자연스럽게 연결 — pdf-inspector로 분류 → 스캔본만 OCR로 라우팅.
- **6개월 영향력**: 중간 — LLM 문서 파이프라인이 성숙하며 "OCR을 언제 부를지" 같은 *라우팅·전처리 계층*이 별도 도구로 분화되는 흐름. Rust라 성능·임베드 용이.
- **대체 관계**: 범용 PDF 파서(pdfplumber·PyMuPDF)에 "스캔 판별" 기능을 얹은 전처리 특화. OCR 엔진([[Unlimited-OCR]])의 *대체가 아니라 앞단 게이트*.
- **허와 실**: "자동 판별"의 정확도(텍스트 레이어가 부분만 있는 하이브리드 PDF, 이미지+투명 텍스트 등 엣지케이스)가 실제 얼마나 견고한지는 실측 필요. 급상승 +1,699은 관심도 지표.
- **액션**: [[Unlimited-OCR]] 한국어 PDF 게이트 actionable에 "pdf-inspector로 스캔본 분류 → OCR 분기" 전처리 단계로 묶어 실험(라이선스 확인 후).

> [!question] 미해결 질문
> 스캔/텍스트 판별 정확도(하이브리드 PDF)? 라이선스? Rust 바인딩(Python FFI) 제공 여부? [[Firecrawl]] 코어 파이프라인 통합 여부?

## 관련 페이지
- [[Firecrawl]] — 제작사 (웹→LLM 데이터 수집 표준)
- [[Unlimited-OCR]] — OCR 엔진 (pdf-inspector의 뒷단 후보)
- [[ai-news]]

## 원본
- 출처: https://github.com/firecrawl/pdf-inspector
- 스타: ⭐9,016 (2026-08-04 자동수집, 당일 +1,699), Rust
- 성격: 스캔본 vs 텍스트 PDF 자동 판별 + 텍스트 추출, OCR 분기 전처리
- 신뢰도: ⭐⭐⭐ (Firecrawl 제작·급성장 실체 상위, raw 자동수집 수치·판별 정확도/라이선스 미검증)
