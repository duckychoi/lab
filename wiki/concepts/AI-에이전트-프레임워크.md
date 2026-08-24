---
title: AI 에이전트 프레임워크
type: concept
domain: ai-news
tags: [concept, agent-framework, tools, memory, multi-step, open-source, LLM-agent]
created: 2026-04-10
updated: 2026-08-24
sources: [hermes-agent.md, Archon.md, SkillClaw.md, superpowers.md, multica.md, OpenManus.md, Graph-Engineering.md, apache-maka.md]
reliability: high
---

# AI 에이전트 프레임워크

LLM에 도구(Tools), 메모리(Memory), 멀티스텝 추론 루프를 더해 자율적으로 복잡한 작업을 수행하게 만드는 소프트웨어 구조.

> [!insight] 2026-08-24 — 에이전트 최적화 패러다임의 4단계 계보 확보 ([[Graph-Engineering]])
> 볼트가 그동안 개별 소스로 흩어 기록해 온 에이전트 기법들을 **하나의 축 위에 정렬할 어휘**가 들어왔다. [[Graph-Engineering]](HF 데일리 신규 3위·업21·저자 35인·**초록 원문 실검증**·동반 레포 실재 확인)이 정리한 계보는 다음 4단계다.
>
> 1. **Prompt Engineering** — 모델 능력을 끌어내기
> 2. **Context Engineering** — 정보 접근 관리 → 볼트의 [[에이전트-메모리-레이어]] 축이 여기 대응
> 3. **Harness Engineering** — 외부 도구·자원 조직 → [[에이전트-스킬]]·하네스 소스군이 여기 대응
> 4. **Loop Engineering** — 지속적 반성·자기개선 → [[SkillEvo]]가 여기 대응
>
> 저자들의 논지는 이 4단계가 **개별 지능(individual intelligence)의 구조적 한계**에 부딪힌다는 것이다. 한계 조건 다섯: **이질적 전문성 · 상호의존적 서브태스크 · 병렬 실행 · 독립 검증 · 지속 상태**. 이들은 *한 에이전트의 능력이나 컨텍스트를 키워서 풀리는 문제가 아니라 구조적 불일치* 이므로, 지능이 **전문화된 에이전트들에 분산되고 시스템 수준에서 조직**돼야 한다 — 이를 **시스템 지능(System Intelligence)** 이라 부른다. 제안된 **Graph Engineering**은 태스크·에이전트·시스템 상태를 **명시적이고 동적으로 진화하는 그래프**로 구성하는 패러다임이다.
>
> **이 계보를 본 개념 페이지의 분류축으로 채택한다** — 이번 배치에서 가장 즉시적인 수확이며, 앞으로 에이전트 소스를 인제스트할 때 "몇 층에 해당하는가"를 먼저 묻는다.
> ⚠️**단, 포지션·서베이 논문으로 자체 실험·신규 벤치 수치가 전혀 없다** — *"Graph Engineering이 더 낫다"* 는 성능 주장은 인용 불가. 동반 레포도 ⭐29·생성 4일차로 커뮤니티 검증 이전이다. **분류 어휘로서 채택하는 것이지 방법의 우수성을 채택하는 것이 아니다.**
> **구현 대응 관계**: 볼트에는 이미 이 패러다임의 **선행 정량 구현체**가 있다 — [[Repo0]]의 **Dual-DAG**(요구사항 DAG + 컴포넌트 DAG + 정렬)가 RPG 대비 **Functionality Coverage +20.08%p · Pass Rate +29.74%p**를 냈다. 즉 *추상적 제안 ↔ 검증된 구현*의 짝이 성립한다. 반대편에는 [[apache-maka]]가 지속 상태를 **그래프가 아니라 append-only 이벤트 로그**로 다루는 **경쟁 표현 형식**으로 서 있으며, **두 형식의 비교 실험은 아직 존재하지 않는다.**

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

### 오케스트레이션·자율 실행 하네스 (2026-07 확장)
- [[deer-flow]] ([[ByteDance]], ⭐76,695) — 서브에이전트·메모리·샌드박스 슈퍼에이전트 하네스
- [[agentscope]] (⭐27,749) — 관측·권한·샌드박스 갖춘 프로덕션 멀티에이전트 프레임워크
- [[OpenManus]] ([[MCP]] FoundationAgents, ⭐57,200, **2026-07-12 신규**) — 초대코드 없는 **범용 자율 에이전트** 오픈 구현(계획→도구호출→다단계 실행 + Playwright 브라우저 + MCP + 비전). 상용 Manus의 오픈 대항마
- [[herdr]] · [[orca]] — 병렬 에이전트 플릿 오케스트레이션

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
- [[OpenManus]]
- [[agentscope]]
- [[deer-flow]]
- [[Claude-Code-워크플로우]] — Claude Code 자체가 에이전트 프레임워크
- [[andrej-karpathy-skills]] — Claude Code 행동 최적화 지침
- [[local-llm]] — 로컬 배포 에이전트와 교차
