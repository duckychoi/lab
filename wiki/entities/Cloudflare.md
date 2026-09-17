---
title: Cloudflare
type: entity
domain: ai-news
tags: [entity, cloudflare, infrastructure, security, agent-skills]
created: 2026-09-17
updated: 2026-09-17
sources: [security-audit-skill.md]
reliability: high
---

# Cloudflare

엣지 네트워크·보안 인프라 기업. AI 축에서는 **모델을 만들지 않고 에이전트의 판정 절차를 만든다.**

> [!insight] 🎯 볼트가 이 조직에서 배운 것 — "심각도를 붙일 수 없는 칸"
> [[security-audit-skill]](★8,529 · MIT)은 모델이 아니라 **`SKILL.md` + 14개 공격분류 문서 + 의존성 0인 JS 검증기 2개**다. 핵심 발명은 판정 3분류를 **스키마로 강제**하는 것:
> > *"`confirmed` has a complete source trace and bounded observed result, `needs_validation` has **an exact unresolved fact and no severity**, and `rejected` records a disproved candidate."*
>
> 🎯 **확인되지 않은 후보에 "낮은 심각도"를 주지 않고 심각도 필드 자체를 비운다** — 등급이 아니라 **범주**로 갈랐다.
> ✅ **자기 실행 조건의 실패 모드까지 적었다**(README 90행): OS 강제 샌드박스가 없으면 *"the workflow keeps the lead as `needs_validation` **instead of executing target code**"* → [[자기제한-명시]].
> 🔗 같은 배치 [[oh-my-hermes]] 가 **다른 생태계에서 같은 것을 발명**했다(`Code · reported done` vs `Test · verified`) → [[검사가능성-공사]] 수렴 증거.

> [!warning] 🔴 검증 불가 영역
> **탐지율·재현율 수치가 레포에 없다.** Cloudflare 블로그(`build-your-own-vulnerability-harness`) 링크만 있고 **볼트도 읽지 않았다.**
> ⚠️ `topics` **0개** — ★8,529 레포가 메타데이터를 비워 뒀다 → [[메타데이터-부재-추론]].

## 관련 페이지
- [[security-audit-skill]] — 제작물 · [[oh-my-hermes]] — 같은 발명의 타 생태계 판본
- [[검사가능성-공사]] · [[자기제한-명시]] · [[요약자와-판정자-분리]] · [[agent-skills]] · [[ai-news]]
