---
title: AI 에이전트 프레임워크
type: concept
domain: ai-news
tags: [concept, agent-framework, tools, memory, multi-step, open-source, LLM-agent]
created: 2026-04-10
updated: 2026-04-11
sources: [hermes-agent.md, Archon.md, SkillClaw.md, superpowers.md, multica.md]
reliability: high
---

# AI 에이전트 프레임워크

LLM에 도구(Tools), 메모리(Memory), 멀티스텝 추론 루프를 더해 자율적으로 복잡한 작업을 수행하게 만드는 소프트웨어 구조.

> [!insight] 핵심 인사이트
> 2026-04-10~11 이틀 연속으로 에이전트 프레임워크 항목이 5개+ 트렌딩. hermes-agent 스타가 하루 만에 10,999 → 54,205로 5배 폭등. 에이전트 인프라 표준화 경쟁이 결정적 국면 — 2026년 4월이 분기점.

## 2026년 현황

5개 소스에서 공통 등장 (2일 연속 트렌딩):
- [[hermes-agent]] — NousResearch 오픈소스 에이전트 프레임워크 (스타 54,205, +5배 급등)
- [[Archon]] — AI 코딩 결정론화 하네스 (스타 12,392)
- [[SkillClaw]] — 집단 스킬 진화 프레임워크 (arXiv 2026-04-09)
- [[superpowers]] — Shell 기반 에이전트 스킬 프레임워크 (스타 146,198, **2026-04-11 신규**)
- [[multica]] — 오픈소스 매니지드 에이전트 플랫폼 (스타 6,713, **2026-04-11 신규**)
- [[rowboat]] — 지속 기억 기반 AI 동료 플랫폼 (스타 11,922, **2026-04-11 신규**)

→ [[ClawBench]] — 에이전트 벤치마크, 실용성 평가 기준선

## 핵심 구성 요소

```
에이전트 프레임워크
├── Tools        ← 외부 API, 코드 실행, 검색
├── Memory       ← 단기(컨텍스트) + 장기(DB/벡터)
├── Reasoning    ← ReAct, CoT, Tree-of-Thought
└── Orchestration ← 멀티 에이전트, 병렬 실행
```

## 비교

| 프레임워크 | 특징 | 신뢰도 | 스타 |
|---|---|---|---|
| superpowers | Shell 기반, 언어 독립, 초경량 | ⭐⭐⭐⭐ | 146,198 |
| hermes-agent | 확장 가능, 오픈소스, 메모리 통합 | ⭐⭐⭐⭐ | 54,205 |
| Archon | 결정론적·재현 가능 | ⭐⭐⭐ | 12,392 |
| multica | 매니지드, 팀 워크플로우 | ⭐⭐ | 6,713 |
| LangChain | 성숙도 높음, 무거움 | ⭐⭐⭐ | — |

## 관련 페이지

- [[NousResearch]]
- [[hermes-agent]]
- [[superpowers]]
- [[multica]]
- [[Archon]]
- [[SkillClaw]]
- [[Claude-Code-워크플로우]] — Claude Code 자체가 에이전트 프레임워크
- [[andrej-karpathy-skills]] — Claude Code 행동 최적화 지침
- [[local-llm]] — 로컬 배포 에이전트와 교차
