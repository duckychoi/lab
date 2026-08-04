---
title: MemDreamer — 계층적 그래프 메모리로 긴 영상 이해
type: source
domain: ai-news
tags: [ai-news, hf-paper, video-understanding, hierarchical-memory, graph-memory, agentic-retrieval, long-video]
created: 2026-06-10
updated: 2026-06-10
sources: []
reliability: medium
---

# MemDreamer: Long Video Understanding via Hierarchical Graph Memory

## 핵심 인사이트

> [!insight] 긴 영상 이해 = 인식·추론 분리 + 계층 그래프 메모리
> 수십 분~수 시간 영상을 이해하기 위해 "인식(perception)"과 "추론(reasoning)"을 분리하고, 계층적 그래프 메모리 + 에이전틱 검색으로 필요한 장면만 동적으로 접근. 전체 영상을 메모리에 올리는 대신 그래프 구조로 압축.

## 도메인별 추출

- **신뢰도**: HuggingFace 논문 (arXiv 2606.07512)
- **즉시 활용**: 부분적 — 긴 영상 분석 파이프라인 설계 시 아키텍처 참고
- **6개월 영향력**: 영상 AI SaaS에서 "긴 영상 이해" 기능 구현의 학술적 기반 제공
- **대체 관계**: 단순 sliding window 방식 대비 메모리 효율 대폭 향상
- **허와 실**: 그래프 메모리 구축 오버헤드 존재 — 짧은 영상에는 과설계
- **액션**: [[video-saas]] 도메인에서 긴 영상 처리 파이프라인 설계 시 참고

## 관련 페이지

- [[AI-영상-생성-2026]]
- [[에이전트-메모리-레이어]]
- [[video-saas]]

## 원본

- 출처: https://huggingface.co/papers/2606.07512
- 신뢰도: ⭐⭐ (HF 논문)
