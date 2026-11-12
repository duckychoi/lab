---
title: "One Table Benchmark — 표 데이터 생성·결측 대체·예측을 같은 분할로 묶은 벤치마크 (arXiv 2611.13001)"
type: source
domain: ai-news
tags: [ai-news, tabular, benchmark, imputation, synthetic-data]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/papers/2611.13001]
reliability: low
---

**논문**: [arXiv 2611.13001](https://huggingface.co/papers/2611.13001) *One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction* · 업보트 **36** · 저자 7명 · 코드 github.com/limix-ldm-ai/OTBench ★0(수집기) (HF papers API 볼트 실측)

## 핵심 인사이트
> [!insight] "유용성"과 "충실도"는 다른 순위를 낸다 — 하나의 점수로 표 모델을 고르면 안 된다
> 데이터셋 56 · 등록 방법 46 · 능력 축 20 · 정렬된 분할. 결과(초록): 대체↔예측은 수치 복원·의존성 보존으로, 생성은 예측 유용성으로 연결되지만 **분포 충실도 순위는 다르거나 반대**. 가장 큰 이득은 **해당 과제 자신의 목적함수를 넣을 때**이고 목적함수 이득은 **가산적이지 않다**. 일부 범용 모델이 유용성에선 전문 모델 조합을 넘지만 **충실도는 전문 모델 우세**. → [[복합지표-분해]] 의 표 데이터판.

> [!warning] 규모·이해관계
> 목적함수 개입 실험은 **5 데이터셋 × 3 시드 × 5 백본**. 초록에 절대 수치 없음. 결론이 "통합 표 모델" 동기 부여라 저자 측 방향성 감안. 코드 ★0.

## 도메인별 추출 (ai-news)
- **신뢰도**: low~medium — 업보트 36 · 벤치 설계는 넓으나 수치 미공개(초록).
- **즉시 활용**: NO — 이 볼트 워크플로에 표 생성/대체 과제 없음.
- **6개월 영향력**: 표 파운데이션 모델 평가가 "예측 정확도 하나"에서 다축으로 이동하는 계기.
- **허와 실**: "범용 모델이 전문 조합을 넘는다"는 **유용성 축에서만**이다.
- **액션**: 없음(기록용).

## 관련 페이지
- [[복합지표-분해]] · [[시계열-예측-파운데이션-모델]] · [[금융-AI]]

## 원본
- 출처: https://huggingface.co/papers/2611.13001
- 확인 범위: HF papers API 초록 전문 · 🔴 본문 미열람
- 신뢰도: ⭐ (업보트 36 · 코드 ★0)
