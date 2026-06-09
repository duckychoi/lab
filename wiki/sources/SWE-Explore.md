---
title: SWE-Explore
type: source
domain: ai-news
tags: [benchmark, coding-agent, repository-exploration, swe-bench, evaluation]
created: 2026-06-09
updated: 2026-06-09
sources: []
reliability: high
---

# SWE-Explore

## 핵심 인사이트

> [!insight] 코딩 에이전트의 "레포 탐색 능력" 벤치마크 — SWE-bench 다음 측정 지점
> 코딩 에이전트가 낯선 레포지토리를 얼마나 잘 탐색하는지 측정하는 벤치마크. 탐색 전략 차이가 실제 작업 성공률에 직결됨을 분석. SWE-bench가 "결과"를 측정했다면, SWE-Explore는 "과정(탐색)"을 측정.

## 도메인별 추출

**왜 중요한가:**
- HF upvotes 85 — 코딩 에이전트 연구자 관심 집중
- [[GitNexus]] 같은 코드 지식 그래프 도구의 필요성을 학술적으로 뒷받침
- 에이전트가 코드베이스를 이해하는 방식(파일 탐색, 구조 파악, 의존성 추적)의 체계화

**핵심 발견:**
- 탐색 전략이 다르면 동일 모델도 성공률이 크게 달라짐
- → 코딩 에이전트 성능 향상의 핵심 변수가 "탐색 효율"임을 시사
- [[claude-code-best-practice]]의 CLAUDE.md 컨텍스트 주입 전략과 직접 연결

> [!insight] GitNexus(서버리스 코드 지식 그래프)가 SWE-Explore 벤치마크에서 고득점할 가능성 높음 — 탐색 능력이 곧 코드 이해 능력

## 관련 페이지
- [[GitNexus]]
- [[claude-code-best-practice]]
- [[Dive-into-Claude-Code]]
- [[Scaling-Test-Time-Agentic-Coding]]

## 원본
- 출처: https://huggingface.co/papers/2606.07297
- HF upvotes 85 (2026-06-09 기준)
- 신뢰도: ⭐⭐⭐⭐
