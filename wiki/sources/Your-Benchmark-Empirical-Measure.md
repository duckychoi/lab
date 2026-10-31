---
title: "Your Benchmark Is an Empirical Measure Over Difficulty — 벤치의 난이도 편중·공백 진단"
type: source
domain: ai-news
tags: [ai-news, benchmark, evaluation, irt]
created: 2026-10-31
updated: 2026-10-31
sources: [https://huggingface.co/papers/2610.29927]
reliability: medium
---

**HF**: published 2026-10-21 · upvote 143 · 저자 5(Yifan Sun · Huan Zhang 외, UIUC·UCSD·NYU) · arXiv 2610.29927

## 핵심 인사이트
> [!insight] 볼트가 매일 하는 "벤치 점수 판정"에 쓸 수 있는 정량 잣대
> 평균 점수는 난이도 분포에 대한 가중 평균일 뿐이다. 25개 벤치 중 **10개가 DDM ≥ 0.10**(편중) · **8개가 MaxGap ≥ 0.10** · **9개가 Top-5 Sum ≥ 0.30**(구간 공백). 공백 구간에서 일어난 진짜 진전은 합계 점수에 거의 안 잡힌다 → 학습 실행을 일찍 버리게 만든다.

> [!warning] 한정 조건
> ① 난이도는 IRT 추정치라 응답 모델 집합에 좌우된다. ② 기준 분포는 "사전 정보 없을 때의" 균등 분포이고, 저자도 *비균등 자체는 문제가 아니며 평가 목적과 맞으면 괜찮다*고 적는다. ③ 프레임워크는 사후 진단(post-hoc)이다. ④ BenchFill의 21.09~38.88% 감소는 **벤치당 3문항 삽입 후 상위 3개 공백 합**에 대한 값이지 점수 왜곡 전체의 감소가 아니다. 삽입 문항은 GPT-5.4 자동 판정 후 사람 감사를 거쳤다.

## 도메인별 추출
- **즉시 활용**: 부분 YES — 코드로 관심 벤치의 공백을 계산하면 [[벤치-개조-재평가]] · [[벤치마크-외부축]] 판정에 수치 근거가 생긴다. 🔴 응답 행렬이 있어야 하고 볼트 미실행.
- **6개월 영향력**: "1점 차 1위" 판정마다 *그 벤치가 어떤 난이도에서 변별력이 있는가*를 묻게 된다.
- **액션**: star + AIME24/25 사례(저자가 공백 예시로 든 Fig. 3) 1회 정독.

## 관련 페이지
- [[벤치-개조-재평가]] · [[벤치마크-외부축]] · [[천장-기준선]] · [[A-RSI]] · [[Youtu-Parsing-Omni]]

## 원본
- 출처: https://huggingface.co/papers/2610.29927 · 코드 https://github.com/ASTRAL-Group/benchmark-difficulty-measure (★42 · 라이선스 필드 없음 · 볼트 실측)
- 확인 범위: HF `api/papers` · arXiv HTML 본문 열람(2026-10-31) · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐ (저자 자기 측정 · 볼트 재현 없음)
