---
title: MinerU — 문서→LLM 입력 변환 파싱 도구
type: source
domain: ai-news
tags: [ai-news, github-trending, document-parsing, ocr, rag, agent-pipeline, vlm]
created: 2026-06-27
updated: 2026-06-29
sources: []
reliability: high
---

# MinerU (opendatalab/MinerU)

> [!insight] 핵심 인사이트
> ⭐72,033 (2026-06-29, 06-27 대비 +1.3K). PDF·DOCX·PPTX·XLSX·이미지·웹페이지를 **LLM이 바로 먹을 수 있는 Markdown/JSON으로 변환**하는 문서 파싱 도구. 수식은 LaTeX, 표는 HTML로 자동 변환하고 헤더/푸터/잡음을 제거해 자연스러운 읽기 순서로 출력한다. 백엔드 엔진은 [[MinerU2.5]]-Pro(1.2B VLM, OmniDocBench 95.39%)를 핵심으로 한 **VLM + OCR 듀얼 엔진**. 이전에 페이퍼로 인제스트한 [[MinerU2.5]]가 "모델"이라면, 이 레포는 그 모델을 감싼 **프로덕션 파이프라인 + 통합 레이어**다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — ⭐70.7K, OpenDataLab(상하이 AI Lab 계열) 운영, 벤치마크 수치(95.39%)와 논문([[MinerU2.5]]) 근거 보유.
- **즉시 활용**: YES — **위키 인제스트 파이프라인에 직결**. 현재 raw.md는 URL/텍스트 중심인데, PDF·논문·슬라이드를 자동으로 깨끗한 markdown으로 바꿔 인제스트 입력으로 넣을 수 있음. [[markitdown]]·[[liteparse]]와 같은 슬롯의 강력한 후보.
- **6개월 영향력**: 높음 — 문서 기반 지식 인제스트의 표준 전처리 레이어. RAG·에이전트 데이터 수집 단계에서 [[firecrawl]](웹)과 짝을 이루는 "문서" 쪽 정제기.
- **대체 관계**: [[markitdown]](Microsoft) / [[liteparse]](LlamaIndex) / [[PaddleOCR]]를 부분 대체·보강. VLM 기반이라 복잡 레이아웃·수식·표에서 우위.
- **허와 실**: 정확도 클레임은 OmniDocBench 근거가 있어 신뢰 가능. 단 1.2B VLM 추론이므로 CPU-only는 느림 — 대량 처리 시 GPU 권장.
- **액션**: 설치 후 내 위키 인제스트용 PDF→markdown 전처리로 시험. MCP Server 통합 옵션 확인.

> [!action] 당장 할 것
> MinerU MCP Server 또는 CLI를 위키 인제스트 전처리로 시험 — 논문 PDF 1편을 markdown 변환해 [[markitdown]]/[[liteparse]] 결과와 품질 비교.

> [!note] 통합 표면
> MCP Server, LangChain/Dify/FastGPT 호환, Python/Go/TypeScript SDK, CLI, REST API, Docker, 웹 UI. 109개 언어 OCR. 라이선스: MinerU Open Source License (Apache 2.0 기반).

## 관련 페이지
- [[MinerU2.5]]
- [[markitdown]]
- [[liteparse]]
- [[PaddleOCR]]
- [[Unlimited-OCR]]
- [[firecrawl]]

## 원본
- 출처: https://github.com/opendatalab/MinerU
- 스타: ⭐72,033 (2026-06-29) ← ⭐70,738 (06-27, +960)
- 백엔드 모델: MinerU2.5-Pro (1.2B, OmniDocBench 95.39%)
- 신뢰도: ⭐⭐⭐⭐ (대형 레포 + 벤치마크 + 논문 근거)
