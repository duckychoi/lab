---
title: Darwin Family — 학습 없는 LLM 추론 스케일링 (진화적 모델 병합)
type: source
domain: ai-news
tags: [ai-news, llm, model-merging, test-time-scaling, reasoning, evolutionary, no-training]
created: 2026-05-17
updated: 2026-05-17
sources: []
reliability: medium
---

# Darwin Family (arXiv 2605.14386)

> [!insight] 핵심 인사이트
> **추가 학습 없이** MRI(Mutual Reliability Index) 신뢰도 가중 진화적 모델 병합으로 LLM 추론 성능을 스케일링. "Darwin"이라는 이름처럼 자연선택 원리를 모델 앙상블·병합에 적용. 파인튜닝 데이터나 RL 없이 기존 모델 조합만으로 추론 성능 향상이 가능하다면 LLM 개선의 진입 장벽을 대폭 낮춘다.

**arXiv**: https://huggingface.co/papers/2605.14386
**신뢰도**: ⭐⭐⭐

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF 논문 페이지 등재, 동료심사 전. "학습 없는 스케일링"은 검증 필요 클레임
- **즉시 활용**: 조건부 — 방법론이 공개된다면 기존 모델로 앙상블 실험 가능
- **6개월 영향력**: 모델 병합(merging)이 파인튜닝 대체재로 자리잡으면 소규모 팀도 SOTA급 모델 합성 가능. [[genericagent]](자기진화), [[evolver]](Genome Evolution) 같은 흐름과 수렴
- **대체 관계**: 전통적 파인튜닝·RL 대비 비용 0에 가까운 추론 성능 향상. [[how-to-fine-tune-reasoning-model]] 대비 훨씬 낮은 진입 장벽
- **핵심 기술**: MRI(Mutual Reliability Index)로 병합 가중치 산정, 진화 알고리즘으로 최적 조합 탐색
- **허와 실**: 기존 모델의 지식 범위를 넘을 수 없음 — 새 데이터 없이 성능 향상의 상한이 존재

> [!question] 미해결 질문
> MRI 신뢰도 가중치 계산 방법? 어떤 베이스 모델 조합에서 효과적? 성능 향상 상한은?

## 관련 페이지
- [[genericagent]] — 자기진화 에이전트
- [[evolver]] — Genome Evolution Protocol 에이전트 자기진화
- [[how-to-fine-tune-reasoning-model]] — 추론 파인튜닝 기법
- [[에이전트-메모리-레이어]] — 에이전트 성능 향상 인프라

## 원본
- 출처: https://huggingface.co/papers/2605.14386
- arXiv: 2605.14386
- 신뢰도: ⭐⭐⭐ (HF 논문, 동료심사 전)
