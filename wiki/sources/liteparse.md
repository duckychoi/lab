---
title: run-llama/liteparse — Rust 기반 고속 경량 문서 파서
type: source
domain: ai-news
tags: [ai-news, github-trending, document-parsing, rust, rag, llamaindex, pdf-parsing, liteparse]
created: 2026-06-01
updated: 2026-06-01
sources: []
reliability: high
---

# run-llama/liteparse

> [!insight] 핵심 인사이트
> LlamaIndex 공식 Rust 기반 오픈소스 PDF 파서. 클라우드·LLM 의존 없이 로컬에서 고속 공간 텍스트 파싱 + 바운딩박스 + OCR 지원. [[markitdown]]이 범용 변환기라면, liteparse는 **RAG 전처리 특화 고속 파서** — 속도와 정확도 균형에서 차별화.

## 핵심 인사이트

> [!action] 당장 할 것
> `pip install liteparse` 또는 `npm install @llamaindex/liteparse` 설치 후 RAG 파이프라인 전처리 단계에 테스트. defuddle·markitdown 대비 속도 벤치마크 비교.

> [!note] 배경 정보
> Rust 코어 기반 PDFium C 라이브러리로 공간 레이아웃 재구성 (Grid Projection). OCR은 Tesseract 내장, HTTP 서버(EasyOCR, PaddleOCR, 커스텀) 플러그인 지원. Rust/Node.js/Python/WASM 멀티 바인딩. PDF·DOCX·XLSX·PPTX·이미지 입력 모두 지원.

> [!question] 미해결 질문
> defuddle 대비 실제 처리 속도 차이는? 한국어 OCR 품질은? LlamaIndex Cloud LlamaParse와의 통합 시너지?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — LlamaIndex 공식, GitHub ⭐8,081 (+925 당일), Apache 2.0
- **즉시 활용**: YES — pip install liteparse, Python/Node.js/CLI 즉시 가능
- **6개월 영향력**: [[markitdown]]과 함께 LLM 문서 파이프라인 전처리 이중 표준 구도 형성 예상. Rust 기반이라 처리 속도 우위 확보 가능
- **대체 관계**: defuddle, PyMuPDF, pypdf 대체 가능. markitdown과 상호 보완 — markitdown은 Office 형식 강세, liteparse는 레이아웃 보존 정확도 강세
- **허와 실**: "dense tables, multi-column layouts, handwritten text"는 클라우드 LlamaParse 권장 — 완전한 대체재 아님. OCR 품질은 Tesseract 수준에 의존
- **액션**: RAG 파이프라인에서 defuddle 대비 벤치마크 → wiki ingest 전처리에 적합한지 평가

## 아키텍처 요약

- **입력**: PDF, DOCX, XLSX, PPTX, 이미지
- **코어 파이프라인**: LibreOffice 변환 → PDFium 텍스트 추출 → Selective OCR → OCR Merge → Grid Projection
- **출력**: 구조화 JSON (텍스트+바운딩박스), 레이아웃 보존 평문, PNG 스크린샷
- **바인딩**: Rust CLI / Node.js(napi-rs) / Python(PyO3) / Browser WASM

## 관련 페이지

- [[markitdown]] — Microsoft 범용 문서→마크다운 변환기 (보완 관계)
- [[MinerU2.5]] — VLM 기반 정밀 문서 파싱 (복잡 레이아웃용)
- [[LLM-Wiki]] — 지식 인제스트 파이프라인에서 활용 가능
- [[RAG-Anything]] — 멀티모달 RAG 파이프라인

## 원본

- 출처: https://github.com/run-llama/liteparse
- 스타: ⭐8,081 (2026-06-01 기준, +925 당일)
- 신뢰도: ⭐⭐⭐ (LlamaIndex 공식 OSS, Apache 2.0)
