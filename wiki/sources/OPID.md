---
title: OPID — On-Policy Skill Distillation for Agentic Reinforcement Learning
type: source
domain: ai-news
tags: [ai-news, hf-papers, distillation, reinforcement-learning, agent, on-policy, skill]
created: 2026-06-26
updated: 2026-06-27
sources: []
reliability: medium
---

# OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning

> [!insight] 핵심 인사이트
> HF 데일리 업보트 39 (2026-06-27 재확인, 데일리 3위). 에이전트형 강화학습(agentic RL)에서 **온폴리시 스킬 디스틸레이션** — 강한 교사 정책의 "스킬"을, 학생 에이전트가 *자신이 실제로 굴린 궤적(on-policy)* 위에서 흡수해 분포 불일치를 줄이는 기법. 같은 사이클의 [[DanceOPD]](생성형 온폴리시 디스틸레이션)와 키워드를 공유 — "on-policy distillation"이 생성·에이전트 양 도메인에서 동시 부상. [[ZPPO]]·[[APPO]] 등 에이전트 RL 최적화 계보의 디스틸레이션 버전.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF 데일리 업보트 24. 벤치마크 환경·코드 재현 미확인.
- **즉시 활용**: NO — 에이전트 학습 기법으로, RL 학습을 직접 하지 않으면 즉시 적용 어려움.
- **6개월 영향력**: 온폴리시 디스틸레이션이 소형 에이전트 모델의 도구 사용·멀티스텝 능력을 저비용으로 끌어올리면, 로컬/소형 에이전트의 실용 능력 향상. [[gemma-4-12B-agentic-GGUF]] 같은 에이전트 특화 소형 모델 품질에 간접 영향.
- **대체 관계**: 단순 SFT 모방학습, off-policy 디스틸레이션을 보강/대체.
- **허와 실**: "스킬"의 단위 정의와 평가 환경이 모호하면 일반화 주장 과장 가능.
- **액션**: 관찰 — 소형 에이전트 모델 학습 레시피에 채택되는지 추적.

> [!question] 미해결 질문
> 평가에 쓴 에이전트 환경(웹/툴/게임)은? 교사-학생 모델 규모 차이와 비용 절감 폭은?

## 관련 페이지

- [[DanceOPD]]
- [[ZPPO]]
- [[APPO]]
- [[gemma-4-12B-agentic-GGUF]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://huggingface.co/papers/2606.26790
- HF 업보트: 39 (2026-06-27, 데일리 3위) ← 24 (06-26)
- 신뢰도: ⭐⭐⭐ (데일리 상위, 재현·코드 미확인)
