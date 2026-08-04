---
title: DecoEvo — Solver와 Rubric-Generator를 분리 공진화시키는 추론 개선
type: source
domain: ai-news
tags: [ai-news, hf-paper, rl, self-play, rubric, reasoning, co-evolution]
created: 2026-07-30
updated: 2026-07-30
sources: []
reliability: medium
---

# DecoEvo (논문 2607.25675)

> [!insight] 핵심 인사이트
> **Score-Decoupled Co-Evolution** — 문제해결 능력(**solver**)과 평가기준 생성(**rubric-generator**)을 **점수 결합에서 분리**해 서로 공진화(co-evolution)시키는 텍스트 공간 추론 개선 기법. raw 요약 기준, "푸는 쪽"과 "채점 기준을 만드는 쪽"을 한 점수에 묶지 않고 각각 진화시켜 보상 해킹·기준 붕괴를 피한다. [[Skill-Self-Play]](proposer·solver·skill controller 공진화)·[[AREX]]("비싼 탐색 vs 값싼 검증"의 비대칭 이중루프)와 같은 **"값싼 구조화 신호(rubric)로 비싼 역량을 키운다"** 계보. 같은 배치 [[CoRT]](토큰 단위 rubric-guided 정책 최적화)와 함께 **"rubric(채점기준) 중심 RL"** 이 한 날에 두 항으로 등장.

> [!action] rubric 분리 = 자기평가 신뢰도 개선 아이디어
> "채점 기준을 능력과 분리해 함께 진화"는 이 위키의 자동 리포트 자기검증에도 시사 — 산출물 품질 기준을 결과 점수와 분리해 별도 유지하면 [[LLM-Wiki]] lint의 기준 붕괴를 줄일 수 있는지 개념 검토.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — raw 한줄요약 기반. **미래형 arxiv ID(2607.25675)로 원문·수치 재현 미검증**. 벤치·개선폭 미확보.
- **즉시 활용**: 낮음(방법론) — RL 포스트트레이닝 아이디어라 직접 도입은 아니나, "능력↔평가기준 분리"는 자기평가 설계 원리로 참고.
- **6개월 영향력**: 자기개선 RL이 "solver 하나 키우기"에서 **"채점기준까지 함께 진화"** 로 정교화. 보상 해킹 완화의 구조적 접근.
- **대체 관계**: [[Skill-Self-Play]]·[[SEED]]·[[온폴리시-증류]]·[[CoRT]]와 **rubric·self-play 공진화** 계보. rubric을 "분리"한다는 점이 차별점.
- **허와 실**: "decoupled co-evolution"은 개념적으로 매력적이나, 실제 개선폭·붕괴 방지 효과는 원문 확인 전. 텍스트 공간 한정일 수 있음.
- **액션**: [[CoRT]]와 묶어 "rubric-guided RL" 미니 클러스터로 추적. 원문 공개 시 개선 수치 확인.

## 관련 페이지
- [[CoRT]]
- [[Skill-Self-Play]]
- [[AREX]]
- [[온폴리시-증류]]
- [[SEED]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.25675 (arXiv 2607.25675)
- 핵심(raw): solver ↔ rubric-generator 점수 분리 공진화로 텍스트 공간 추론 개선
- 신뢰도: ⭐⭐⭐ (raw 한줄요약 기반, 미래형 ID·원문 재현 미검증 medium)
