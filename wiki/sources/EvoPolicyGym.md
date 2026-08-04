---
title: EvoPolicyGym — 실행형 정책 반복 개선(Autonomous Policy Evolution) 벤치마크
type: source
domain: ai-news
tags: [ai-news, paper, hf-paper, agent-benchmark, policy-evolution, rl-environment, trajectory-diagnostics]
created: 2026-07-03
updated: 2026-07-03
sources: []
reliability: medium
---

# EvoPolicyGym: Autonomous Policy Evolution

> [!insight] 핵심 인사이트
> HF 업보트 29. 에이전트가 **고정 상호작용 예산(fixed interaction budget)** 안에서 실행형 정책(executable policy, Python 코드)을 환경 피드백을 받아 반복 편집·개선하는 능력을 측정하는 벤치마크. 기존 평가가 이 과정을 "최종 점수 하나"로 뭉개거나 open-ended SWE 진척과 혼동하는 문제를 지적하고, compact interactive RL 환경 16개로 **궤적 단위 진단(trajectory-level diagnostics)** 제공 — 예산 배분, 피드백을 parametric tuning으로 전환하는 방식을 분리 측정. GPT-5.5가 종합 랭크 1위 및 16개 환경 전부 top-two. 에이전트 평가 계열([[AgenticDataBench]], [[AgenticSTS]])과 인접.

## 도메인별 추출 (ai-news)
- **신뢰도**: HF 업보트 29, 원문 초록 검증 완료 (defuddle fetch 성공). GPT-5.5 리더보드 결과 명시.
- **즉시 활용**: MAYBE — 자체 코딩 에이전트의 "반복 개선 능력"을 최종 점수가 아니라 궤적 관점으로 진단하려는 팀에 유용. 벤치마크 코드 공개 여부 확인 필요.
- **6개월 영향력**: 중간~큼. "final score → trajectory diagnostics"로의 평가 축 이동은 에이전트 벤치마크 설계 트렌드와 부합. budget-constrained refinement라는 프레이밍이 재사용될 가능성.
- **대체 관계**: 최종 점수·리더보드 중심 에이전트 평가를 보강(대체 아님). open-ended SWE 벤치와 정책 진화 능력을 분리.
- **허와 실**: 핵심 기여는 "새 SOTA 에이전트"가 아니라 **평가 방법론(controlled setting + 예산 제약 + 궤적 진단)**. compact RL 환경이라 실제 대규모 태스크로의 외삽은 별개 문제.
- **액션**: 추적 — 벤치마크 공개 시 자체 에이전트를 예산 제약 하 정책 개선 궤적으로 프로파일링.

> [!action] 당장 할 것
> EvoPolicyGym 16개 환경 구성과 예산/궤적 지표 정의 확인. 자사 코딩 에이전트에 "고정 예산 하 반복 개선" 진단 지표(예산 소진 패턴) 적용 가능성 검토.

## 관련 페이지
- [[AgenticDataBench]] — LLM 데이터 에이전트 태스크·스킬 단위 세분 평가 (에이전트 벤치마크 인접)
- [[AgenticSTS]] — 장기 에이전트 메모리/스킬 계층 효과 분리 (평가 궤적 관점 공유)
- [[AI-에이전트-프레임워크]] — 에이전트 실행·평가 일반 개념
- [[에이전트-메모리-레이어]] — 반복 개선 시 컨텍스트/기억 관리와 연결
- [[Beyond-Static-Leaderboards]] — 리더보드 넘어선 평가 문제의식 공유

## 원본
- 출처: https://huggingface.co/papers/2607.02440
- arXiv: 2607.02440
- HF 업보트: 29
- 신뢰도: 원문 초록 검증 완료 (fetch 성공)
