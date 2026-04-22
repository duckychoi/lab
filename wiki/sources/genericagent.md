---
title: lsdefine/GenericAgent (자기진화 에이전트)
type: source
domain: ai-news
tags: [ai-news, agent, self-evolving, skill-tree, token-efficiency, local-llm]
created: 2026-04-16
updated: 2026-04-18
sources: []
reliability: medium
---

# GenericAgent

> [!insight] 핵심 인사이트
> 3.3K 줄 시드 코드에서 스킬 트리를 자체 성장시켜 시스템 전체 제어 달성하는 자기진화 에이전트. ⭐3,883(당일 +831). 토큰 소비 6배 절감 클레임 — [[SkillClaw]] 개념의 실용 구현체.

## 핵심 인사이트

**스펙:**
- GitHub ⭐3,883 (당일 +831, 2026-04-18 업데이트)
- 핵심: 시드 코드 → 자동 스킬 트리 성장 → 복잡 태스크 처리
- 주장: 토큰 소비 6배 절감

> [!note] 배경 정보
> [[SkillClaw]](집단 진화 에이전트 스킬)의 구현체에 가까운 실용 레포. 차이점: GenericAgent는 단일 에이전트의 자기진화에 집중, SkillClaw는 집단 진화 이론.

**자기진화 메커니즘:**
1. 시드 스킬(3.3K 줄)에서 시작
2. 태스크 수행 중 새 스킬 자동 추출·저장
3. 다음 태스크에서 기존 스킬 재활용 → 토큰 절감

> [!warning] 주의 / 신뢰도 낮음
> "6배 절감" 클레임은 마케팅성 수치일 수 있음. 독립 검증 필요.

> [!action] 당장 할 것
> SkillClaw 이론과 대조해서 읽고 실제 벤치마크 재현 시도

## 관련 페이지

- [[SkillClaw]]
- [[AI-에이전트-프레임워크]]
- [[hermes-agent]]

## 원본

- 출처: https://github.com/lsdefine/GenericAgent
- 신뢰도: ⭐⭐ (⭐3,883, 신규 — 6배 절감 클레임 독립 검증 필요)
