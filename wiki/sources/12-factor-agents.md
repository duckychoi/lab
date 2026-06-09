---
title: 12-factor-agents — 프로덕션 수준 LLM 에이전트 구축 12원칙
type: source
domain: ai-news
tags: [ai-news, agent, best-practice, production, llm, agent-design, humanlayer]
created: 2026-05-19
updated: 2026-05-19
sources: []
reliability: high
---

# 12-factor-agents — 프로덕션 수준 LLM 에이전트 구축 12원칙

## 핵심 인사이트

> [!insight] 핵심 인사이트
> Heroku의 유명한 "12 Factor App" 방법론을 LLM 에이전트에 적용한 설계 지침. 프로덕션에 실제로 배포 가능한 에이전트를 만들기 위한 12가지 원칙 — 에이전트의 신뢰성·관측 가능성·확장성 문제를 체계화. 에이전트를 처음 설계하거나 기존 에이전트를 프로덕션화할 때 참조 필수 레포.

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub ⭐20,892 (+399 당일, 2026-05-19), humanlayer(AI 에이전트 안전·승인 레이어 전문). 20K 스타는 커뮤니티 검증 완료 수준
- **즉시 활용**: YES — 새 에이전트 설계 시 즉시 체크리스트로 활용. 코드가 아닌 지침서
- **6개월 영향력**: [[andrej-karpathy-skills]]·[[claude-code-best-practice]]가 "Claude Code 설정 최적화"라면, 12-factor-agents는 **에이전트 아키텍처 설계 원칙**. 에이전트 인프라가 성숙할수록 이 원칙의 중요성 ↑
- **대체 관계**: [[Dive-into-Claude-Code]](Claude Code 내부 설계 분석)·[[agentspex]](에이전트 명세 언어) 보완 — 실무 설계 원칙 측면
- **허와 실**: "12 Factor"는 마케팅 프레이밍일 수 있음. 원칙 각각의 실제 적용 가능성 직접 검토 필요
- **액션**: 현재 에이전트 워크플로우([[Claude-Code-워크플로우]])가 12원칙을 얼마나 준수하는지 체크리스트 검토

## 관련 페이지

- [[AI-에이전트-프레임워크]] — 에이전트 설계 전체 지형도
- [[Claude-Code-워크플로우]] — Claude Code 설정·워크플로우
- [[andrej-karpathy-skills]] — 실무 에이전트 스킬 모음
- [[Dive-into-Claude-Code]] — Claude Code 에이전트 아키텍처 분석
- [[agentspex]] — 에이전트 행동 형식 명세 언어

## 원본

- 출처: https://github.com/humanlayer/12-factor-agents
- 신뢰도: ⭐⭐⭐ (⭐20,892, +399 당일, humanlayer 전문 기관)
