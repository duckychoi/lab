---
title: DeepSearch-World — 검증가능 환경에서 자기증류로 딥서치 에이전트 학습
type: source
domain: ai-news
tags: [ai-news, hf-paper, deep-search, web-agent, self-distillation, rl, verifiable-environment]
created: 2026-07-21
updated: 2026-07-21
sources: []
reliability: medium
---

# DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

> [!insight] 핵심 인사이트
> 웹 에이전트를 **교사 모델 없이 자기 경험으로 개선**하는 자기증류(self-distillation) 프레임(DeepSearch-Evolve). 결정론적(deterministic) 환경 안에 **42만(420K) 멀티홉 QA 태스크**를 두고, 진행 검증(progress verification)·실패 복구(failure recovery) 같은 에이전트 행동을 지원하며 **자기 생성 궤적으로 반복 학습**. 결과 **9B 모델**이 다수 벤치에서 경쟁력 있는 성능 — "검증 가능한 환경이 롱호라이즌 웹 에이전트의 확장 가능한 자기개선을 가능케 한다"는 주장. [[온폴리시-증류]]·[[DeepSearch-World|self-distillation]] 계보로, **교사 없이 스스로 진화**한다는 점이 [[LongStraw]](고정예산 장문맥 RL)·[[Trust-Region-Policy-Distillation]]과 같은 "에이전트 RL 인프라" 흐름을 연장.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — WebFetch로 초록 실확인(420K 멀티홉 QA·9B·자기증류 등 구체). 미래형 ID(2607.07820)로 원문·재현 미검증 → medium. 업보트 51.
- **즉시 활용**: NO — 학습 방법. 다만 "검증 가능한 환경 + 자기증류"는 무인 크론으로 이 위키를 갱신하는 내 파이프의 **자기평가 루프** 설계에 개념적 참조.
- **6개월 영향력**: 중간 — 딥서치/웹 에이전트가 "교사 distillation·약한 보상"에서 **"결정론적 환경 자기진화"** 로 이동. 소형(9B) 모델의 웹 리서치 능력 확보 경로로 유의미.
- **대체 관계**: 교사 기반 distillation·[[온폴리시-증류]] 대비 **교사 없는 자기증류 + 검증환경**이 차별점. [[LongStraw]](장문맥 RL)와 함께 에이전트 후학습 인프라 계열.
- **허와 실**: "자기 경험으로 진화"는 매력적이나 420K가 결정론적 QA 환경에 국한 — 개방형 실제 웹으로의 일반화는 미확인. 9B "경쟁력"의 비교 대상·조건이 원문에서 검증돼야.
- **액션**: 원문 공개 시 "진행 검증·실패 복구" 정의와 자기증류 루프 구조 확인 → 무인 리서치 에이전트 자기평가 설계 참고.

> [!warning] 신뢰도 medium — 미래형 ID·원문 미검증
> arXiv 2607.07820은 초록 수준만 확인. 성능·비교는 자체 리포트로 독립 재현 전.

## 관련 페이지
- [[온폴리시-증류]]
- [[LongStraw]]
- [[Trust-Region-Policy-Distillation]]
- [[에이전트-메모리-레이어]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.07820 · 업보트 51
- 신뢰도: ⭐⭐⭐ (초록 WebFetch 검증, 미래형 ID·원문 미검증 medium)
