---
title: sentence-transformers/all-MiniLM-L6-v2
type: source
domain: ai-news
tags: [ai-news, embedding, sentence-transformer, rag, semantic-search, local-llm]
created: 2026-04-15
updated: 2026-04-15
sources: []
reliability: high
---

# all-MiniLM-L6-v2

> [!insight] 핵심 인사이트
> 22.7M 파라미터 경량 문장 임베딩 모델. HuggingFace 월 198M 다운로드로 RAG·시맨틱 검색 파이프라인의 실용적 표준. "작지만 충분히 좋다"의 완벽한 사례.

## 핵심 인사이트

**스펙:**
- 파라미터: 22.7M (매우 경량, CPU에서도 실용적 속도)
- 다운로드: 198M/월 (HF 역대 최다 수준)
- 용도: 문장 임베딩, 시맨틱 검색, RAG, 클러스터링

> [!action] 당장 할 것
> wiki 파이프라인에 시맨틱 검색 추가 시 첫 번째 선택지. `pip install sentence-transformers` 후 즉시 사용 가능.

## 도메인별 추출

- **즉시 활용**: YES — RAG 파이프라인, LLM-Wiki 쿼리 시맨틱 검색에 바로 쓸 수 있음
- **Hermes 적용**: ChinameBot 문서 검색에 all-MiniLM-L6-v2 임베딩 레이어 추가 가능
- **트레이드오프**: 품질은 large 모델 대비 낮지만 속도·비용 압도적 우위

## 관련 페이지

- [[LLM-Wiki]]
- [[RAG vs LLM-Wiki]]
- [[MinerU2.5]]
- [[markitdown]]

## 원본

- 출처: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- 신뢰도: ⭐⭐⭐ (198M 다운로드/월, 업계 표준)
