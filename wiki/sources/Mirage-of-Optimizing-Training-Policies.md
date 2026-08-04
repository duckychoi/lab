---
title: The Mirage of Optimizing Training Policies — 추론 정책이 진짜 목표 (MIPI/MIPU)
type: source
domain: local-llm
tags: [ai-news, hf-paper, rl, llm-post-training, training-inference-mismatch, off-policy]
created: 2026-07-06
updated: 2026-07-06
sources: []
reliability: high
---

# The Mirage of Optimizing Training Policies (arXiv 2606.29526)

**HF Papers**: https://huggingface.co/papers/2606.29526 — **2026-07-06 데일리 페이퍼 #1**

> [!insight] 핵심 인사이트
> LLM 강화학습(RL) 사후학습이 불안정한 근본 원인을 "**학습-추론 불일치(training-inference mismatch)**"로 지목. LLM은 생성 효율(추론 엔진)과 학습 정밀도(학습 엔진)를 위해 **별도 엔진**을 쓰는데, 파라미터가 같아도 같은 궤적에 대한 확률이 엔진 간 달라 *상시적 off-policy성*이 학습을 오염시킴. 핵심 통찰: **학습 엔진의 정책을 잘 개선해도 실제 배포되는 추론 정책의 개선을 보장하지 않는다** — 지금까지 다들 최적화하던 대상(학습 정책)이 신기루라는 것. 해법으로 **MIPI**(Monotonic Inference Policy Improvement) 목적함수 + **MIPU** 2단계 프레임워크 제안.

## 핵심 인사이트

> [!note] MIPU 작동 방식 (초록 실측)
> 1. 샘플러(추론 엔진) 참조 후보 업데이트 구성
> 2. **추론 측 gap proxy**로 동기화 후보를 선택적으로 수용
> → 두 모델 규모·고불일치 조건 실험에서 평균 추론 성능 + 학습 안정성 향상. "학습 손실"이 아니라 "배포될 추론 정책의 단조 개선"을 최적화 대상으로 재정의.

> [!insight] 6/30~7월 효율·안정성 흐름의 이론적 기둥
> 6/30 "벤치의 날"→7/1 "효율의 날"→7/2 "인프라·평가의 날" 흐름에서, 이 논문은 **RL 사후학습의 목적함수 자체를 재정의**하는 상류 이론. [[온폴리시-증류]]([[DanceOPD]]·OPID 클러스터)가 "학생 자기생성 샘플에 교사 신호"로 분포 불일치를 교정하려던 문제와 **정확히 같은 병(학습≠추론 분포)**을 RL 관점에서 공격.

## 도메인별 추출 (local-llm / RL)

- **실용성 판단**: 모델 학습자용 이론·기법 — 직접 배포 도구는 아니나 내가 쓰는 사후학습 모델([[Ornith-1.0-9B]]·[[GLM-5.2]] 등)의 안정성 근거.
- **메모리 아키텍처**: 해당 없음(학습 최적화 논문).
- **트레이드오프**: 추가 후보 구성·수용 판정 비용 vs 학습 안정성/최종 추론 성능. 고불일치 환경일수록 이득.
- **오픈소스 구현체**: 초록 단계, 코드 공개 여부 미확인.
- **6개월 영향력**: RL 사후학습 레시피가 "학습 정책 최적화"에서 "추론 정책 단조 개선"으로 이동하면 오픈모델 안정성 전반 향상.

> [!warning] 검증 범위
> HF 초록·데일리 1위는 확인(2026-07-06). 단 MIPU의 성능 향상 폭·재현성은 논문 본문/코드 미확인 — 실험 수치는 인용 시 원문 재확인 필요.

## 관련 페이지
- [[온폴리시-증류]] — 학습≠추론 분포 문제의 증류판
- [[DanceOPD]] — on-policy distillation 클러스터
- [[Accelerating-RL-Post-Training]] — RL 사후학습 효율 계보
- [[Beyond-Scalar-Rewards]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2606.29526 (arXiv 2606.29526)
- 지표: 2026-07-06 HF 데일리 페이퍼 #1
- 신뢰도: ⭐⭐⭐⭐ (HF 초록·데일리 1위 실측 / 실험 수치는 원문 재확인)
