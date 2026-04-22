---
title: microsoft/markitdown — Microsoft 오픈소스 문서→마크다운 변환기
type: source
domain: ai-news
tags: [ai-news, github-trending, document-parsing, markdown, pdf, office, LLM-pipeline, microsoft]
created: 2026-04-11
updated: 2026-04-14
sources: []
reliability: high
---

# microsoft/markitdown

> [!insight] 핵심 인사이트
> PDF·Office·HTML·이미지 등 모든 파일 형식을 LLM 입력용 마크다운으로 일괄 변환. Microsoft 공식 오픈소스, ⭐107,555(+4,548). [[MinerU2.5]]가 VLM 기반 정밀 파싱이라면, markitdown은 범용 파이프라인 통합 도구 — 서로 보완적.

## 핵심 인사이트

> [!action] 당장 할 것
> **즉시 적용 가능**: pip install markitdown → wiki 인제스트 파이프라인에서 PDF/DOCX/HTML 일괄 변환 테스트. 현재 defuddle 대비 파일 형식 커버리지 비교.

> [!note] 배경 정보
> Microsoft 오픈소스 프로젝트. 접근성 자동화(ARIA) 기반으로 문서 구조를 보존하는 방식. Python 패키지, pip install 즉시 가능. LLM 기반 RAG·위키 파이프라인에 바로 연결 가능.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — Microsoft 공식, ⭐103,007, 커뮤니티 대규모 검증
- **즉시 활용**: YES — pip install markitdown, 즉시 사용
- **6개월 영향력**: LLM 데이터 준비 파이프라인의 사실상 표준이 될 가능성 높음
- **대체 관계**: defuddle, pypdf, docx2txt 대체. Office 파일까지 커버하는 것이 차별점
- **허와 실**: 복잡한 레이아웃(2단, 표, 수식)은 [[MinerU2.5]] 대비 품질 낮을 수 있음. 용도 구분 필요
- **액션**: pip install → wiki ingest pipeline 통합. 수식/표 많은 문서는 MinerU2.5와 병용

## 관련 페이지

- [[MinerU2.5]] — VLM 기반 정밀 문서 파싱 (보완 관계)
- [[LLM-Wiki]] — 지식 인제스트 파이프라인
- [[문서-파싱]]

## 원본

- 출처: https://github.com/microsoft/markitdown
- 스타: 103,007 (2026-04-12 기준, +3,086 당일)
- 신뢰도: ⭐⭐⭐⭐
