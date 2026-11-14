---
title: "SO-Arena — System One 모델의 능력 범위와 결정 신뢰성 벤치 (성능 1위가 신뢰성 7위 · arXiv 2611.15777)"
type: source
domain: ai-news
tags: [ai-news, benchmark, system-one, decision-model, reliability, calibration]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.15777]
reliability: medium
---

**논문**: [arXiv 2611.15777](https://huggingface.co/papers/2611.15777) *SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models* · 업보트 **83**(수집기 11-13: 36) · 저자 5명(Lichen Li … **Xinchao Wang**) · 발행 2026-11-11 · 코드 holdrain/SO-Arena ★24 (HF papers API 볼트 실측)

## 핵심 인사이트
> [!insight] 정확도와 신뢰성은 다른 축이다 — 성능 1위 System One 모델이 신뢰성에서는 7위
> 긴 토큰 생성 없이 바로 결정하는 [[System-One-모델]]을 11개 도메인 · 5개 능력군으로 평가. 정확도 외에 두 가지 신뢰성 지표를 잰다:
> 1. **결정 안정성** — 선택지 집합을 통제해서 바꿨을 때 답이 유지되는가.
> 2. **답 부재 인식** — 유효한 선택지가 없을 때 "없다"를 고르는가.
>
> 21개 모델 평가에서 스케일과 추가 추론의 이득은 도메인마다 크게 달랐고, *"the best-performing System One model ranks only seventh in reliability"*.
> ⇒ 볼트가 10-14 에 [[System-One-모델]] 개념을 세울 때 적은 "이 계열의 공통 약점 = 검증 상태"에 처음으로 **외부 측정 축**이 생겼다. [[Jeva]] 의 `Noul`(답 부재 출력 타입)이 실제로 작동하는지를 재는 것이 ②번 지표다.

> [!warning] 초록에 모델명 · 점수 없음
> 어떤 모델이 1위이고 7위인지, 21개 모델 구성은 본문 확인 필요. 같은 배치 [[AutoTrust-JEV-27B]] 가 이 벤치에 포함됐는지도 미확인.

## 도메인별 추출 (ai-news)
- **신뢰도**: 업보트 83(11-13 데일리 1위) · 코드 공개 · 초록 수치는 순위 1건.
- **즉시 활용**: 간접 — 결정 모델을 라우터·판정기로 쓸 때 "정확도 표만 보지 말 것"이라는 선택 기준.
- **6개월 영향력**: 결정 모델 카드가 정확도 외에 선택지 변경 안정성·부재 인식을 보고하도록 압력을 줄 수 있다.
- **대체 관계**: [[AutoTrust-JEV-27B]] 가 쓰는 Decision Index(정확도·스킬 점수 중심)와 보완.
- **허와 실**: 문제 제기는 명확, 수치는 본문.
- **액션**: 본문 표에서 JEV 계열 순위 확인(낮음).

## 관련 페이지
- [[System-One-모델]] · [[Jeva]] · [[VideoJev]] · [[SearchJev]] · [[AutoTrust-JEV-27B]] · [[Actor-Judge-Teacher]] · [[캘리브레이션-붕괴]] · [[복합지표-분해]]

## 원본
- 출처: https://huggingface.co/papers/2611.15777
- 확인 범위: HF papers API 초록 전문 · 저자 · 업보트 · 🔴 본문 · 코드 미열람
- 신뢰도: ⭐⭐ (업보트 83 · 코드 공개 · 초록 수치 부족)
