---
title: PlanBench-XL — 대규모 툴 생태계에서 LLM 에이전트의 장기 계획 평가
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, agent, long-horizon-planning, tool-use]
created: 2026-06-23
updated: 2026-06-23
sources: []
reliability: medium
---

# PlanBench-XL

> [!insight] 핵심 인사이트
> HF 추천수 51. 대규모 도구 사용 환경에서 LLM 에이전트의 **장기 계획(long-horizon planning)** 능력을 측정하는 벤치마크. 단일 호출이 아닌 "많은 툴이 깔린 환경에서 멀리 내다보는 계획"을 평가 — 에이전트가 실패하는 지점이 모델 추론보다 **계획·툴 선택**임을 드러내는 흐름.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — arXiv 2606.22388, HF 추천 51. 벤치마크라 재현 가능성·평가 설계가 핵심.
- **즉시 활용**: PARTIAL — 직접 쓰진 않지만, 내 에이전트 워크플로우(reat/wiki 자동화)의 **계획 실패 패턴 진단 렌즈**로 유용.
- **6개월 영향력**: 에이전트 평가가 "정답률"에서 "장기 계획·툴 선택 정확도"로 이동. 모델 고를 때 long-horizon 점수가 기준이 될 수 있음.
- **대체 관계**: [[AdaPlanBench]], [[PlanBench]] 계열의 확장(XL = 대규모 툴 생태계 스케일).
- **허와 실**: 벤치마크 점수와 실제 프로덕션 신뢰성의 갭은 [[Beyond-Static-Leaderboards]] 경고대로 주의.

> [!action] 당장 할 것
> 리더보드에서 내가 쓰는 모델군의 long-horizon 순위 확인 → 멀티스텝 자동화에 적합한 모델 선택 근거로 활용.

## 관련 페이지

- [[AdaPlanBench]]
- [[Beyond-Static-Leaderboards]]
- [[AI-에이전트-프레임워크]]
- [[EnterpriseClawBench]]
- [[deer-flow]]

## 원본
- 출처: https://huggingface.co/papers/2606.22388
- HF 추천: 51 (2026-06-23)
- 신뢰도: ⭐⭐⭐ (벤치마크 논문)
