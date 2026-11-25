---
title: "Loom Attention — 토큰마다 헤드 간 회로를 다시 배선하는 이중 스트림 Transformer (arXiv 2611.30634)"
type: source
domain: ai-news
tags: [ai-news, paper, architecture, attention, head-circuits, pretraining, throughput, loomformer]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.30634]
reliability: medium
---

**논문**: arXiv 2611.30634 · 업보트 **36**(수집기 11-25) → **38**(볼트 API 11-25) · 소속 표기 없음 · 저자 4명 · 코드 https://github.com/Caiyun-AI/LoomFormer (★1 · Apache-2.0)

## 핵심 인사이트
> [!insight] 헤드끼리 서로 본다 — 수직 어텐션(토큰 방향)에 가로 어텐션(헤드 방향)을 얹은 이중 스트림
> 각 헤드가 이전 헤드 출력들에 대한 **"세로 어텐션"**(정규화 · 게이트 선형 어텐션, 토큰별 행렬 메모리 = 두 번째 잔차 스트림)으로 Q/K/V를 얻어 토큰 방향 어텐션과 엮는 LoomFormer. 초록: 3배 이상 연산한 Transformer, 1.7–2.8배 연산한 HC/mHC · MUDDFormer · AttnRes와 동급 — [[cmHC]] · [[SimpleHC]] · [[xHC]] 의 mHC 계열과 직접 비교된 확장. [[동결-교정층]] 의 대조군 — **본체(어텐션 구조) 자체를 재설계**하는 방향.

> [!warning] 이론 FLOPs +2%지만 실측 처리량은 8–16% 느리다
> 표 2(300B 토큰, Pythia 계열): LoomPythia-2.8B 평균 0-shot **59.9**(Pythia-12B 59.9와 동률, mHC-2.8B 58.8) · 5-shot 61.6(12B 60.8 상회), Pile ppl 6.02(12B 6.01). **지는 행**: 0-shot PIQA 74.7 < 12B 76.0, HellaSwag 49.1 < 12B 50.3, BoolQ 65.8 < mHC 66.9 · 12B 67.4, 5-shot ARC-C 35.1 < mHC 35.5 · 12B 36.5. **속도 비용(표 3 · 9)**: 이론 FLOPs는 +1.95–3.70%뿐인데 실측 처리량은 Transformer 대비 학습 89.2–92.4% · A800 프리필 83.8–90.5% · 디코드 84.6–92.3% — **이론과 실측의 갭이 8–16%**. 절제(표 4): 동적 읽기 · 쓰기를 모두 고정하면 이득의 56%만 남음. 실험 최대 규모 2.8B.

## 도메인별 추출 (ai-news)
- **허와 실**: "FLOPs 거의 안 늘어나는 성능 12B"는 이론값 — 실측 처리량 8–16% 감소가 실 배포 비용. 이론-실측 갭을 표로 공개한 점은 가점.
- **6개월 영향력**: 사전학습 아키텍처 연구 — 2.8B까지 검증이라 대규모 검증 전 당장 쓸 일 없음. mHC 계열 관찰(볼트 cmHC · SimpleHC · xHC)의 후속 추적 대상.
- **액션**: 없음(관찰).

## 관련 페이지
- [[cmHC]] · [[SimpleHC]] · [[xHC]] · [[동결-교정층]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.30634
- 확인 범위: HF papers API(볼트 11-25 — 업보트 38 · githubRepo 일치) · 본문 표 2 · 3 · 4 · 9 및 지는 행(수집기 11-25 판독) · 실행 0
- 신뢰도: ⭐⭐ (2.8B까지 · 소속 미표기 · ★1 레포)
