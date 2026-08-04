---
title: DanceOPD — On-Policy Generative Field Distillation
type: source
domain: ai-news
tags: [ai-news, hf-papers, distillation, generative-model, on-policy, diffusion]
created: 2026-06-26
updated: 2026-06-28
sources: []
reliability: medium
---

# DanceOPD: On-Policy Generative Field Distillation

> [!insight] 핵심 인사이트
> HF 데일리 페이퍼 당일 1위(업보트 66, 2026-06-28 재확인 — 3일 연속 최상위, ↑40→59→66). **온폴리시(on-policy) 방식의 생성형 필드 디스틸레이션** 기법 — 디스틸레이션이 학습 분포(off-policy 데이터)에 갇혀 생기는 분포 불일치를, 학생 모델 자신이 만든 샘플을 따라가며(on-policy) 교정하는 계보. [[OPID]](에이전트 스킬 디스틸레이션)와 같은 사이클에 동시 등장 — "온폴리시 디스틸레이션"이 이번 HF 데일리의 공통 키워드로, 생성·에이전트 양쪽에서 동시에 부상.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF 데일리 1위(업보트 40)로 연구 관심도는 높음. 단, 코드·벤치마크 재현은 미확인.
- **즉시 활용**: NO — 생성 모델 학습 기법으로, 모델을 직접 학습하지 않는 한 즉시 적용 대상 아님.
- **6개월 영향력**: 온폴리시 디스틸레이션이 확산/생성 모델 경량화의 표준 레시피가 되면, 빠른 추론용 소형 생성 모델 품질이 향상 → 로컬 이미지/영상 생성에 간접 수혜.
- **대체 관계**: 기존 off-policy 디스틸레이션(분포 불일치 한계)을 보강/대체하는 학습 기법.
- **허와 실**: "필드 디스틸레이션" 네이밍은 학술 추상화. 실측 속도·품질 트레이드오프 수치 확인 필요.
- **액션**: 관찰 — 코드 공개 시 경량 생성 모델 적용 사례 추적.

> [!question] 미해결 질문
> "필드(field)"의 구체적 정의는? 어떤 생성 모델(확산/플로우)에 적용되며 속도-품질 수치는?

## 관련 페이지

- [[OPID]]
- [[Improved-LLDM]]
- [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/papers/2606.27377
- HF 업보트: 66 (2026-06-28, 데일리 1위 — 3일 연속) ← 59 (06-27) ← 40 (06-26)
- 신뢰도: ⭐⭐⭐ (데일리 1위, 재현·코드 미확인)
