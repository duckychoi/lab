---
title: NatureBench — 코딩 에이전트의 Nature급 SOTA 재현 능력 평가
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, coding-agent, reproducibility, sota, science]
created: 2026-06-24
updated: 2026-06-24
sources: []
reliability: medium
---

# NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?

> [!insight] 핵심 인사이트
> HF 데일리 36 upvotes. 코딩 에이전트가 *Nature 계열 논문*에 보고된 SOTA 결과를 **코드로 재현**할 수 있는지 측정하는 벤치마크. 이번 사이클의 "에이전트를 만드는 단계 → 측정·검증하는 단계" 이동([[World-Action-Models-Survey]]·[[PlanBench-XL]]·[[EnterpriseClawBench]] 흐름)을 *과학 재현성*이라는 가장 엄격한 잣대로 끌어올린 사례. SWE-bench가 소프트웨어 버그 수정이라면 NatureBench는 "논문 결과 자체 재현"으로 난이도를 한 단계 올림.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF 추천 36, arXiv 2606.24530. 벤치마크 설계의 공정성(데이터 누출, 논문 선정 편향)은 원문 확인 필요.
- **즉시 활용**: NO(직접) — 평가용 벤치마크. 단, 내가 코딩 에이전트(Claude Code 등) 성능을 *내 작업에* 신뢰할지 판단하는 외부 레퍼런스로 유용.
- **6개월 영향력**: "에이전트가 진짜 연구를 재현/수행하는가"는 [[karpathy-autoresearch]]가 던진 질문의 평가 인프라. 자율 연구 에이전트 신뢰도의 기준점이 될 수 있음.
- **대체 관계**: SWE-bench, [[GameCraft-Bench]], [[EnterpriseClawBench]]와 보완 — 각각 버그수정/게임제작/업무세션을 측정. NatureBench는 과학 재현 축 추가.
- **허와 실**: "Nature-family"라는 권위 프레이밍은 주목도 장치. 핵심은 재현에 필요한 데이터·환경이 에이전트에 공정하게 제공됐는지.
- **액션**: 리더보드 확인 → Claude Code/현재 사용 코딩 에이전트의 재현 점수 위치 파악.

> [!warning] 신뢰도 주의
> 벤치마크는 측정 대상 논문 풀과 채점 기준에 따라 결과가 크게 달라짐. 단일 점수로 에이전트 우열 단정 금지([[Beyond-Static-Leaderboards]] 경고와 동일 맥락).

## 관련 페이지

- [[karpathy-autoresearch]]
- [[PlanBench-XL]]
- [[EnterpriseClawBench]]
- [[GameCraft-Bench]]
- [[Beyond-Static-Leaderboards]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://huggingface.co/papers/2606.24530
- HF 추천: 36 upvotes (2026-06-24)
- 신뢰도: ⭐⭐⭐ (HF 추천 상위, 프리프린트 — 설계 공정성 미검증)
