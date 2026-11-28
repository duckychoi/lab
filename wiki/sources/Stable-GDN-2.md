---
title: "Stable Gated DeltaNet-2 — 순환 상태 발산을 '비정규 소거 연산자'로 규명하고 대칭화로 묶은 선형 어텐션 (arXiv 2611.34051)"
type: source
domain: ai-news
tags: [ai-news, paper, linear-attention, recurrent-state, stability, long-context, gdn, ruler]
created: 2026-11-28
updated: 2026-11-28
sources: [https://huggingface.co/papers/2611.34051]
reliability: medium
---

**논문**: arXiv 2611.34051 · 업보트 **130**(수집기 11-28) → **131**(볼트 API 11-28 · 11-27 페이지 1위) · MemTensor · 코드 레포 없음(HF papers API githubRepo None)

## 핵심 인사이트
> [!insight] 발산의 원인을 "수정 없이도 상태가 커진다"로 특정 — 학습률 튜닝이 아니라 연산자 구조의 문제
> GDN-2가 장문맥 학습 중 발산하는 이유를 **읽기/수정 방향 비대칭 → 비정규(non-normal) 소거 연산자 → 쓰기 없이도 순환 상태가 지수적으로 증가**로 규명하고, **대칭 소거 + 감쇠 조절 잔차 쓰기**로 상태 증가를 **O(T) 상한**으로 묶는다(청크 병렬 유지 — 실용성 유지). 이론 진단 → 구조 수정이라는 순서가 명확한 논문.

> [!warning] 이득이 지표에 따라 양분된다 — 평균만 보면 놓친다([[복합지표-분해]])
> ~1.6B에서 **128K RULER 평균 +6.80(순환형)** — 큰 이득. 그러나 **하이브리드형은 9개 다운스트림 평균 +0.62%p**로 미미. 본문 ablation: 잔차 쓰기(RW) 제거 시 단문 평균 50.39→49.43%, RULER 25.43→22.22 — RW가 실제 기여. **검증 규모는 1.6B까지** — 스케일 이월 미확인.

## 도메인별 추출 (ai-news)
- **신뢰도**: 이론 규명 + ablation까지 갖춤(수치 4종). 단 코드 레포 미공개(HF API 확인) — 재현 경로 없음.
- **즉시 활용**: NO — 학습 인프라가 필요한 아키텍처 변경이고 레포가 없다.
- **6개월 영향력**: 선형 어텐션 계열(GDN · DeltaNet · Mamba2 계열)의 안정화 표준 기법이 될 가능성 — [[Loom-Attention]] · [[Morphing-Hybrid-Attention]] 같은 어텐션 재설계 축과 같은 시장.
- **허와 실**: "128K +6.80"은 순환형 한정 — 하이브리드(실배포 주류 구성)에서는 +0.62%p.
- **액션**: 없음(관찰 — 선형 어텐션 모델 학습 시 재검토).

## 관련 페이지
- [[복합지표-분해]] · [[Loom-Attention]] · [[Morphing-Hybrid-Attention]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.34051
- 확인 범위: HF papers API(볼트 11-28 — 업보트 131 · 코드 없음 확인) · 본문 수치(ablation · RULER · 다운스트림 — 수집기 11-28 판독 인용) · 실행 0
- 신뢰도: ⭐⭐⭐ (이론+ablation 구성 · 스케일 한계 명시 · 레포 미공개)
