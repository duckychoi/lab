---
title: CoRT — 반사실 리플레이 기반 토큰 단위 Rubric-Guided 정책 최적화
type: source
domain: ai-news
tags: [ai-news, hf-paper, rl, rubric, counterfactual, policy-optimization, reasoning]
created: 2026-07-30
updated: 2026-07-30
sources: []
reliability: medium
---

# CoRT (논문 2607.25659)

> [!insight] 핵심 인사이트
> **Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization** — 학습 중 **반사실적(counterfactual) 리플레이**를 적용해 **토큰 단위 채점기준(rubric)** 으로 LLM 정책을 최적화하는 RL 기법. raw 요약 기준, "이 토큰을 다르게 골랐다면?"이라는 반사실 신호를 rubric에 결합해 **최종 정답 이진 보상보다 촘촘한 토큰 레벨 크레딧 할당**을 노린다. [[Progress-Reward-Modeling]]("최종성공 이진→진행도 조밀 리워드")의 언어판, [[Trust-Region-Policy-Distillation]]·[[UP-Asymmetric-Optimization]] 등 **안정적 정책 최적화** 계보와 맞닿는다. 같은 배치 [[DecoEvo]](solver↔rubric 분리 공진화)와 함께 **"rubric 중심 RL"** 트렌드를 형성.

> [!action] 토큰 단위 크레딧 할당 = 촘촘한 보상 설계
> "반사실 리플레이 + 토큰 rubric"은 긴 추론/도구호출 체인의 **어느 스텝이 성패를 갈랐는지** 귀속하는 문제와 동형. [[Long-Horizon-Terminal-Bench]]·[[LongStraw]] 장기 에이전트 학습의 크레딧 할당 참고 아이디어.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — raw 한줄요약 기반. **미래형 arxiv ID(2607.25659)로 원문·수치 재현 미검증**. 개선폭·베이스라인 미확보.
- **즉시 활용**: 낮음(방법론) — 직접 도입은 아니나, 토큰 단위 rubric·반사실 신용할당은 에이전트 실패 진단 설계 원리로 참고.
- **6개월 영향력**: RLVR/정책최적화가 "결과 보상"에서 **"토큰 단위 rubric·반사실"** 로 세밀화. [[온폴리시-증류]]·[[Progress-Reward-Modeling]]과 함께 조밀 보상 신호 확산.
- **대체 관계**: [[DecoEvo]](rubric 공진화)·[[Trust-Region-Policy-Distillation]]·[[UP-Asymmetric-Optimization]]·[[AEPO]] 등 **정책 최적화·rubric** 계보. 반사실 리플레이가 차별 요소.
- **허와 실**: 토큰 단위 rubric은 이론적으로 강하나 **rubric 신뢰도·계산비용**이 관건. 반사실 리플레이의 실효는 원문 확인 전.
- **액션**: [[DecoEvo]]와 묶어 "rubric-guided RL" 미니 클러스터로 추적. 원문 공개 시 크레딧할당 개선 수치 확인.

## 관련 페이지
- [[DecoEvo]]
- [[Progress-Reward-Modeling]]
- [[Trust-Region-Policy-Distillation]]
- [[UP-Asymmetric-Optimization]]
- [[온폴리시-증류]]
- [[Long-Horizon-Terminal-Bench]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.25659 (arXiv 2607.25659)
- 핵심(raw): 반사실 리플레이 + 토큰 단위 rubric으로 LLM 정책 최적화
- 신뢰도: ⭐⭐⭐ (raw 한줄요약 기반, 미래형 ID·원문 재현 미검증 medium)
