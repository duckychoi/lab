---
title: WeaveBench — Microsoft 하이브리드 인터페이스 컴퓨터 사용 에이전트 장기 벤치마크
type: source
domain: ai-news
tags: [ai-news, benchmark, computer-use, agent, Microsoft, long-horizon, hybrid-interface, evaluation]
created: 2026-06-13
updated: 2026-06-14
sources: []
reliability: high
---

# WeaveBench: Long-Horizon Benchmark for Computer-Use Agents

> [!insight] 핵심 인사이트
> Microsoft 연구팀이 제안하는 **하이브리드 인터페이스 환경**에서 컴퓨터 사용(computer-use) 에이전트를 평가하는 장기(long-horizon) 벤치마크. 업보트 50. 단순 클릭/입력을 넘어 GUI + CLI + 파일시스템 + API를 혼합 사용하는 복잡한 실제 컴퓨터 작업을 평가 — 에이전트가 "진짜 컴퓨터 사용자"처럼 작동할 수 있는지 측정.

## 핵심 인사이트

> [!note] 배경 정보
> [[UI-TARS-desktop]], [[ClawGUI]] 등 GUI 에이전트 연구가 급증 중이지만 대부분 단기(short-horizon) 태스크 평가. WeaveBench는 장기 목표를 달성하기 위해 여러 인터페이스를 넘나드는 태스크를 설계. "컴퓨터 사용" 에이전트의 현실적 능력 측정 공백을 메운다.

> [!question] 미해결 질문
> 하이브리드 인터페이스의 구체적 조합은? 태스크 도메인(업무/개발/창작)? 현재 SOTA 에이전트들의 성능은?

> [!action] 당장 할 것
> arXiv 2606.09426 읽기. Monday AI 스킬이 GUI + CLI 혼합 태스크에서 어떻게 수행하는지 WeaveBench 기준으로 분류해보기.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — Microsoft Research 소속, arXiv 2606.09426, HF 업보트 50
- **즉시 활용**: 에이전트 평가 기준으로 활용. 현재 Claude Code 스킬이 어떤 WeaveBench 카테고리를 커버하는지 자가 평가 가능
- **6개월 영향력**: 컴퓨터 사용 에이전트의 산업 표준 벤치마크로 자리잡을 가능성 높음 (Microsoft 브랜드)
- **대체 관계**: OSWorld, WebArena 대비 하이브리드 인터페이스 + 장기 태스크 특화
- **허와 실**: Microsoft 자체 에이전트 제품 홍보용 벤치마크일 가능성 배제 불가 — 태스크 선정 편향 주의
- **액션**: arXiv 읽기 → 태스크 카테고리 파악 → 내 에이전트 커버리지 자가 진단

## 관련 페이지

- [[UI-TARS-desktop]]
- [[ClawGUI]]
- [[Agentic-Environment-Engineering]]
- [[EvoArena]]
- [[SpatialClaw]]

## 원본

- 출처: https://huggingface.co/papers/2606.09426
- arXiv: 2606.09426
- 소속: Microsoft Research
- HF 업보트: 50 (2026-06-12)
- 신뢰도: ⭐⭐⭐⭐
