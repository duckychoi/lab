---
title: PaddleOCR — 경량 다국어 OCR 툴킷 (LLM 파이프라인 연동 최적화)
type: source
domain: ai-news
tags: [ai-news, github-trending, paddlepaddle, ocr, document-parsing, pdf, llm-pipeline, multilingual, open-source]
created: 2026-06-07
updated: 2026-06-07
sources: []
reliability: high
---

# PaddleOCR (GitHub ⭐81,113)

> [!insight] 핵심 인사이트
> PDF·이미지를 구조화 데이터로 변환하는 경량 OCR 툴킷. 100개 언어 지원, LLM 파이프라인 연동 최적화 — 문서 파싱 파이프라인에서 [[markitdown]]·[[MinerU2.5]]와 함께 선택지. 오늘 +433으로 급상승 중.

## 핵심 인사이트

> [!action] 당장 할 것
> 문서→LLM 파이프라인 구성 시 MinerU2.5 vs PaddleOCR 비교 실험. 수식·표 포함 PDF라면 MinerU2.5, 일반 이미지/스캔 문서라면 PaddleOCR이 더 가벼울 수 있음.

> [!note] 배경 정보
> PaddlePaddle(Baidu 딥러닝 프레임워크) 기반. PP-OCR 시리즈로 경량화 지속 진행. OCR + 레이아웃 분석 + 표 인식 통합 파이프라인 제공. PaddleNLP와 연계하여 문서→텍스트→LLM 흐름 구성 가능.

> [!note] 오늘 급상승
> +433 — LLM 파이프라인에서 문서 파싱 수요 증가 반영. RAG 파이프라인 구축 인구 증가와 상관관계.

> [!warning] 주의
> PaddlePaddle 프레임워크 의존성으로 PyTorch 생태계 대비 통합 비용 발생. CUDA 환경 설정 복잡도 확인 필요.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — Baidu 공식, ⭐81,113, 실제 프로덕션 사용 사례 다수
- **즉시 활용**: YES — `pip install paddlepaddle paddleocr` 후 2줄 코드로 실행
- **6개월 영향력**: RAG 파이프라인 인구 증가로 문서 파싱 수요 지속. [[MinerU2.5]], [[liteparse]]와 경쟁
- **대체 관계**: [[markitdown]](전방위 문서), [[MinerU2.5]](수식/표 특화), [[liteparse]](Rust 고속)와 비교 필요
- **허와 실**: OCR 정확도는 언어·폰트·이미지 품질에 크게 의존. 복잡한 레이아웃 처리 한계 있음
- **액션**: 스캔 문서/이미지 기반 RAG 파이프라인 구성 시 벤치마크 비교 실험

## 관련 페이지

- [[markitdown]] — Microsoft 전방위 문서→마크다운 변환기
- [[MinerU2.5]] — 1.2B 문서 파싱 VLM, PDF/수식/표 SOTA
- [[liteparse]] — Rust 기반 고속 로컬 문서 파서

## 원본

- 출처: https://github.com/PaddlePaddle/PaddleOCR
- 신뢰도: ⭐⭐⭐⭐ (Baidu 공식 GitHub 81,113 스타)
