---
title: EnterpriseClawBench — 실제 업무 세션 기반 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, agent, enterprise, real-world-tasks]
created: 2026-06-23
updated: 2026-06-23
sources: []
reliability: medium
---

# EnterpriseClawBench

> [!insight] 핵심 인사이트
> HF 추천수 48. **실제 직장 작업 세션**을 기반으로 에이전트 성능을 평가하는 벤치마크. 합성 태스크가 아닌 현실 업무 흐름을 평가 대상으로 삼는다는 점이 핵심 — [[Beyond-Static-Leaderboards]]가 지적한 "정적 벤치마크의 예측 타당성 한계"에 대한 실무 지향 응답.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — arXiv 2606.23654, HF 추천 48. 실세션 기반이라 데이터 출처·라이선스·재현성 확인 필요.
- **즉시 활용**: PARTIAL — 내 업무 자동화 에이전트가 "실제 업무"에서 얼마나 버티는지 가늠하는 기준점.
- **6개월 영향력**: 에이전트 평가가 토이 태스크 → 실업무 세션으로 이동하는 흐름의 대표 사례. 기업 도입 의사결정에 영향.
- **대체 관계**: [[PlanBench-XL]](장기 계획), [[GameCraft-Bench]](게임 제작) 등과 함께 "도메인 특화 실태스크 벤치마크" 군을 형성.
- **허와 실**: 실세션 = 일반화 한계도 큼. 특정 업무 도메인 편향 가능.

> [!action] 당장 할 것
> 벤치마크 태스크 구성을 읽고, 내 wiki/reat 자동화가 다루는 작업 유형과의 중첩도 파악 → 약점 영역 식별.

## 관련 페이지

- [[Beyond-Static-Leaderboards]]
- [[PlanBench-XL]]
- [[GameCraft-Bench]]
- [[AI-에이전트-프레임워크]]
- [[CLI-Universe]]

## 원본
- 출처: https://huggingface.co/papers/2606.23654
- HF 추천: 48 (2026-06-23)
- 신뢰도: ⭐⭐⭐ (벤치마크 논문)
