---
title: Rethinking RAG in Long Videos — 장시간 영상 특화 RAG 재정의
type: source
domain: ai-news
tags: [ai-news, video-understanding, rag, long-video, video-rag, multimodal-retrieval, video-saas]
created: 2026-06-15
updated: 2026-06-15
sources: []
reliability: medium
---

# Rethinking RAG in Long Videos (arXiv 2606.13141)

> [!insight] 핵심 인사이트
> HuggingFace Papers ❤️30 (2026-06-15). 장시간 영상(long video)에서 **RAG의 "무엇을 검색하고 어떻게 활용하는가"를 근본적으로 재정의**. 기존 영상 RAG는 프레임 단위 유사도 검색에 그침 — 이 논문은 의미 단위(semantic unit) 기반 검색과 맥락적 활용을 제안.

## 핵심 인사이트

> [!insight] 영상 RAG의 패러다임 전환
> 문제: 장시간 영상(1시간+)에서 관련 구간을 찾는 기존 RAG는 프레임 균등 샘플링 → 의미 희석. 해결: 장면 전환, 대화 구간, 시각 변화 등 의미 경계를 기준으로 청크 생성 + 다층 검색. video-saas 파이프라인에서 긴 영상 QA 및 요약 품질을 크게 향상시킬 기술.

> [!action] video-saas 적용
> [[down-analysis]] 스킬이 현재 트랜스크립트+장면 분석을 수행하는데, 이 논문의 의미 단위 청크 전략을 적용하면 긴 영상 분석 정확도 향상 가능. 특히 1시간 이상 강연/영화 분석 품질 개선 기대.

> [!note] RAG vs LLM-Wiki 관점
> [[RAG vs LLM-Wiki]]의 논쟁에서 영상 도메인은 RAG가 여전히 필수 — 영상 전체를 컨텍스트에 넣을 수 없기 때문.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐ — 30 likes, 연구팀 미확인
- **즉시 활용**: NO — 논문 수준, 코드 확인 필요
- **6개월 영향력**: 장시간 영상 이해 시스템(영상 QA, 요약, 장면 검색)에 적용 가능
- **대체 관계**: 단순 프레임 샘플링 기반 영상 RAG 시스템 개선
- **액션**: 코드 공개 확인, down-analysis 파이프라인 개선 실험

## 관련 페이지

- [[RAG vs LLM-Wiki]]
- [[AI-영상-생성-2026]]
- [[OmniDirector]]
- [[VideoKR]]
- [[UniVidX]]

## 원본

- 출처: https://arxiv.org/abs/2606.13141
- 신뢰도: ⭐⭐ (HuggingFace Papers ❤️30 · 2026-06-15)
