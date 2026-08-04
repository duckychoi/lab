---
title: AgenticSTS — 타입별 검색으로 프롬프트를 재조립하는 bounded-contract 장기 에이전트 메모리
type: source
domain: ai-news
tags: [ai-news, paper, hf-paper, agent-memory, long-horizon, typed-retrieval, bounded-contract, slay-the-spire]
created: 2026-07-03
updated: 2026-07-03
sources: []
reliability: medium
---

# AgenticSTS: Bounded-Contract Memory for Long-Horizon LLM Agents

> [!insight] 핵심 인사이트
> HF 업보트 29. 장기 에이전트 메모리를 "각 미래 결정이 무엇을 볼 수 있는가에 대한 계약(contract)"으로 정의. 과거 관찰·툴콜·reflection을 매 프롬프트에 통째로 append하는 단순 계약은 접근은 쉽지만 개별 메모리 요소의 효과를 분리 불가능한 "뒤죽박죽 혼합물"로 만든다는 문제를 지적. 대안으로 **bounded contract** — 매 결정을 **타입별 검색(typed retrieval)** 으로 조립한 fresh user message에서 내림, raw cross-decision transcript는 붙이지 않음. 프롬프트가 실행 길이와 무관하게 bounded하게 유지되고 어떤 계층도 단독 ablation 가능. **Slay the Spire 2**(closed-rule 확률적 덱빌딩, 런당 수백 결정)에서 실험 — 298개 완료 궤적으로 메모리 계층별 효과를 분리 측정. [[에이전트-메모리-레이어]]와 강하게 연결되는 핵심 소스.

## 도메인별 추출 (ai-news)
- **신뢰도**: HF 업보트 29, 원문 초록 검증 완료 (defuddle fetch 성공). 298 궤적 + condition tag + frozen 메모리/스킬 스냅샷 + 분석 스크립트 공개(reproducible testbed) 명시.
- **즉시 활용**: MAYBE~YES — "transcript append 대신 typed retrieval로 프롬프트 조립" 패턴은 장기 에이전트 설계에 즉시 참고 가능. 다만 게임 도메인 특화 harness라 이식은 재설계 필요.
- **6개월 영향력**: 큼. 무한히 늘어나는 컨텍스트 append의 한계가 실전에서 커지는 상황에서 "bounded prompt + typed retrieval + 계층별 ablation" 방법론은 에이전트 메모리 설계의 참조 틀이 될 수 있음.
- **대체 관계**: accumulating-context(전 기록 append) 방식을 대체. 계층별 효과 분리가 불가능하던 기존 메모리 평가를 ablation 가능한 구조로 전환.
- **허와 실**: 승률 효과는 directional 수준 — no-store baseline 3/10 vs 스킬 계층 추가 6/10이나 표본이 작아 Fisher exact p≈0.37로 통계적 결정력은 약함(저자도 인정). 공개 프론티어 LLM 벤치는 최저 난이도에서 zero win(인간 승률 16%)이라 태스크는 어렵지만 saturated는 아님. 핵심 기여는 "승률 SOTA"가 아니라 **검증된 재사용 방법론 + 재현 testbed**.
- **액션**: 읽기 + 실험 — typed retrieval 계약을 자체 에이전트 메모리에 프로토타입.

> [!action] 당장 할 것
> 자체 장기 에이전트에서 "raw transcript append"를 typed retrieval 기반 fresh-prompt 조립으로 바꿔 프롬프트 길이 상한/계층별 ablation 가능성 검증. 298 궤적 testbed·분석 스크립트 확보.

## 관련 페이지
- [[에이전트-메모리-레이어]] — 핵심 연결. bounded-contract·typed retrieval은 메모리 계층 설계의 구체 사례
- [[Agent-Native-Memory-System]] — 에이전트 네이티브 메모리 구조 비교
- [[EvoPolicyGym]] — 장기 결정·궤적 진단 관점 공유 (에이전트 평가 계열)
- [[AgenticDataBench]] — 스킬 단위 분석 관점 공유
- [[AI-에이전트-프레임워크]] — 에이전트 실행·메모리 일반 개념
- [[stale-llm-memory]] — 장기 메모리 오염/노후화 문제와 대비

## 원본
- 출처: https://huggingface.co/papers/2607.02255
- arXiv: 2607.02255
- HF 업보트: 29
- 신뢰도: 원문 초록 검증 완료 (fetch 성공)
