---
title: "TOME-Math — 대학 수학 교과서 2,118권을 구조 보존 증명 지도 데이터 38만 건으로 (arXiv 2610.40394)"
type: source
domain: ai-news
tags: [ai-news, math, dataset, curriculum-learning, proof]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/papers/2610.40394]
reliability: low
---

**논문**: [arXiv 2610.40394](https://huggingface.co/papers/2610.40394) *Scaling Mathematical Proof Supervision from Structured Textbooks* · 업보트 **26** · 저자 10명 · **공개 코드·데이터 없음**("will release") (HF papers API 볼트 실측)

## 핵심 인사이트
> [!insight] 데이터를 "문제-풀이 쌍"으로 평탄화하면 교과서의 구조(장 순서 · 명제-증명 연결 · 의존 참조)를 버린다
> 2,118권 → 약 **380K** 구조화 레코드(장 순서 · 명제-증명 링크 · 의존 참조 · 출처 보존). 이 구조로 커리큘럼 학습과 데이터량·출처 폭 스케일링을 분석. 전체 규모 파인튜닝 시 **비가중 평균 +16.7%p**(베이스 대비), 공개 지시 데이터 3종을 **종합 점수에서** 상회.

> [!warning] +16.7%p 의 분모
> 평균에 **자체 홀드아웃이 섞여 있다**(*"across our held-out evaluations and established public benchmarks"*). 공개 벤치만의 향상 폭 · 베이스 모델명 · 벤치 목록은 초록에 없다 → [[복합지표-분해]]. 코퍼스는 **미공개** → [[선언된-구현체-공백]].

## 도메인별 추출 (ai-news)
- **신뢰도**: low — 업보트 26 · 코드·데이터 없음.
- **즉시 활용**: NO.
- **6개월 영향력**: 공개되면 수학 추론 SFT 데이터의 "출처·구조 보존" 기준점. 이 볼트의 "원본 링크 유지" 원칙과 같은 방향([[WikiTrace]]).
- **액션**: 공개 시 재판정.

## 관련 페이지
- [[복합지표-분해]] · [[선언된-구현체-공백]] · [[WikiTrace]]

## 원본
- 출처: https://huggingface.co/papers/2610.40394
- 확인 범위: HF papers API 초록 전문
- 신뢰도: ⭐ (업보트 26 · 미공개)
