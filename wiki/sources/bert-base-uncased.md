---
title: google-bert/bert-base-uncased
type: source
domain: ai-news
tags: [ai-news, bert, google, nlp, classification, fine-tuning]
created: 2026-04-15
updated: 2026-04-15
sources: []
reliability: high
---

# BERT Base Uncased

> [!insight] 핵심 인사이트
> Google의 110M 파라미터 BERT 기본 모델. 월 65.1M 다운로드로 여전히 NLP 파인튜닝·분류 작업의 기준점. 2018년 모델이 2026년에도 HF 최다 다운로드 상위권 — "검증된 구식이 신뢰할 수 없는 신형보다 낫다"는 실용 원칙.

## 핵심 인사이트

**스펙:**
- 파라미터: 110M
- 다운로드: 65.1M/월
- 용도: 텍스트 분류, NER, QA 파인튜닝, 임베딩

> [!note] 배경 정보
> 2026년 기준으로 LLM 시대임에도 BERT가 이 다운로드 수를 유지하는 이유: (1) 엔터프라이즈 레거시 파이프라인, (2) 분류 태스크에서 여전히 충분한 성능, (3) 추론 비용이 LLM 대비 극히 낮음.

## 도메인별 추출

- **즉시 활용**: 텍스트 분류, 스팸 탐지, 감정 분석 등에 즉시 파인튜닝 가능
- **트레이드오프**: 생성 능력 없음, 긴 컨텍스트 처리 불가 (512 토큰 제한)

## 관련 페이지

- [[all-MiniLM-L6-v2]]
- [[Falconsai/nsfw_image_detection]]

## 원본

- 출처: https://huggingface.co/google-bert/bert-base-uncased
- 신뢰도: ⭐⭐⭐ (65.1M 다운로드/월, Google, 업계 검증 완료)
