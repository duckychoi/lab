---
title: AgenticDataBench — 15개 도메인 344태스크·433 재사용 스킬 LLM 데이터 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, paper, hf-paper, agent-benchmark, data-agent, data-science, skill-based-eval, fine-grained]
created: 2026-07-03
updated: 2026-07-03
sources: []
reliability: medium
---

# AgenticDataBench: Fine-Grained Benchmark for LLM Data Agents

> [!insight] 핵심 인사이트
> HF 업보트 19. LLM 기반 데이터 에이전트(data science 워크플로 자동화)를 **다양한 시나리오 × 세분 granularity**로 평가하는 벤치마크. (1) 15개 vertical 도메인의 실데이터·태스크 수집(핀테크 선도사 실제 B2B 5건 포함), (2) 반복되는 data-centric 운영 패턴을 **data science skills**로 정의하고 벤치마크 커버리지를 포함 스킬 수로 정량화 — 대표 스킬은 Stack Overflow 대규모 태스크 해법에서 skill-aligned hierarchical clustering으로 추출, (3) 실 비즈니스 태스크는 스킬 구성 다양성 최대화로 선정, (4) 실 태스크 없는 도메인은 LLM 기반 태스크 생성으로 보강. 최종적으로 SOTA 데이터 에이전트를 태스크·**스킬 단위**로 세분 분석. 사용자 제공 요약의 "344 태스크 / 433 재사용 스킬" 규모. 에이전트 평가 계열([[EvoPolicyGym]], [[AgenticSTS]])과 인접.

## 도메인별 추출 (ai-news)
- **신뢰도**: HF 업보트 19, 원문 초록 검증 완료 (defuddle fetch 성공). "344 태스크 / 433 스킬" 구체 수치는 사용자 제공 요약 — 초록은 "15개 도메인 + 스킬 기반 커버리지"까지 확인, 정확 숫자는 본문 확인 필요.
- **즉시 활용**: MAYBE — 데이터 에이전트/AutoML·데이터 워크플로 자동화를 평가·비교하려는 팀에 직접 유용. open-sourced testbed 언급.
- **6개월 영향력**: 중간~큼. 데이터 사이언스 자동화 에이전트가 늘어나는 상황에서 "final accuracy가 아니라 스킬 단위 커버리지·성능"으로 진단하는 프레이밍은 벤치마크 표준화에 기여할 수 있음. 실 B2B 핀테크 케이스 포함은 실무 적합성 신호.
- **대체 관계**: 좁은 단일 데이터셋·최종 점수 중심 데이터 에이전트 평가를 도메인 다양성 + 스킬 단위 세분 분석으로 보강/대체.
- **허와 실**: 핵심 기여는 새 에이전트가 아니라 **벤치마크 구성 방법론**(실데이터 수집 + SO 기반 스킬 추출 + 스킬 커버리지 정량화 + LLM 태스크 생성). LLM 생성 태스크의 현실성·스킬 클러스터링 품질이 벤치 신뢰성의 전제.
- **액션**: 추적 — 데이터 에이전트 평가 필요 시 testbed 도입 검토.

> [!action] 당장 할 것
> 본문에서 정확한 태스크 수(요약 344)·스킬 수(요약 433)와 15개 도메인 목록·스킬 커버리지 지표 정의 확인. open-sourced testbed 접근성·라이선스 확인.

## 관련 페이지
- [[EvoPolicyGym]] — 궤적 단위 에이전트 진단 (에이전트 평가 계열, 상호 참조)
- [[AgenticSTS]] — 스킬 계층 효과 분리 (스킬 단위 분석 관점 공유)
- [[MulTaBench]] — 멀티태스크/테이블 데이터 에이전트 평가 인접
- [[Beyond-Static-Leaderboards]] — 정적 리더보드 넘어선 세분 평가 문제의식
- [[AI-에이전트-프레임워크]] — 에이전트 실행·평가 일반 개념
- [[From-Context-to-Skills]] — 컨텍스트→재사용 스킬 추출 관점 공유

## 원본
- 출처: https://huggingface.co/papers/2607.01647
- arXiv: 2607.01647
- HF 업보트: 19
- 신뢰도: 원문 초록 검증 완료 (fetch 성공). 태스크/스킬 정확 수치는 본문 미확인.
