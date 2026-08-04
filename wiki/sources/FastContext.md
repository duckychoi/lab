---
title: FastContext — Microsoft, 코딩 에이전트용 레포지토리 효율 탐색 모델
type: source
domain: ai-news
tags: [ai-news, hf-paper, microsoft, coding-agent, context-retrieval, repository, efficient, swe]
created: 2026-06-17
updated: 2026-06-17
sources: []
reliability: high
---

# FastContext

## 핵심 인사이트

> [!insight] 전체 레포 파싱 없이 필요 컨텍스트만 추출 — 코딩 에이전트의 맥락 탐색 혁신
> Microsoft의 코딩 에이전트용 레포지토리 탐색 모델. 대형 코드베이스 전체를 파싱하는 대신, 필요한 파일·함수만 지능적으로 선택해 컨텍스트 효율 극대화. HF upvotes 40.

## 도메인별 추출

**핵심 기여:**
- arXiv 2606.14066, HF upvotes: 40
- 레포 전체 토큰화 없이 쿼리 관련 코드 섹션만 추출
- 대규모 코드베이스(수십만 줄)에서도 빠른 컨텍스트 수집
- [[Claude-Code-워크플로우]] 같은 에이전트 코딩 도구와 직접 연관

**코딩 에이전트 맥락:**
- [[OpenHands]], [[SWE-Explore]] 등 코딩 에이전트의 핵심 병목(컨텍스트 탐색) 해결
- [[microsoft-fara]]와 함께 MS의 에이전트 생산성 도구 전략 일환
- [[vllm]] 기반 서빙으로 사내 코딩 어시스턴트에 통합 가능

> [!action] 대규모 레포 코딩 에이전트 구축 시 FastContext 방식의 선택적 파일 로딩 패턴 채택 검토

## 관련 페이지
- [[OpenHands]]
- [[SWE-Explore]]
- [[microsoft-fara]]
- [[Claude-Code-워크플로우]]

## 원본
- 출처: https://huggingface.co/papers/2606.14066
- HuggingFace upvotes: 40
- 신뢰도: ⭐⭐⭐⭐
