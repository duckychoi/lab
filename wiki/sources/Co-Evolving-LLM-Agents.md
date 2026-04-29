---
title: Co-Evolving LLM Agents
type: source
domain: ai-news
tags: [ai-news, agent-framework, skill-bank, co-evolution, long-horizon-tasks, reinforcement-learning]
created: 2026-04-25
updated: 2026-04-25
sources: []
reliability: medium
---

# Co-Evolving LLM Agents

> [!insight] 핵심 인사이트
> **LLM 의사결정 에이전트와 스킬 뱅크(Skill Bank)가 공진화(co-evolution)**하는 프레임워크. 에이전트가 태스크를 수행하며 스킬을 자동 학습·등록하고, 스킬 뱅크가 커질수록 에이전트 장기 태스크 성능이 향상되는 자기강화 루프.

**arXiv**: https://huggingface.co/papers/2604.20987

## 도메인별 추출

**신뢰도**: arXiv 논문. 중간 신뢰도. 실험 재현 가능성 확인 필요.

**즉시 활용**: 조건부 YES — [[AI-에이전트-프레임워크]] 설계 시 스킬 뱅크 공진화 패턴 참조. [[SkillClaw]](집단 진화)과 비교 검토 가치 있음.

**6개월 영향력**: 에이전트가 사용할수록 더 강해지는 "사용→학습→재사용" 루프는 장기 에이전트 인프라의 핵심 패턴. [[hermes-agent]], [[superpowers]] 같은 스킬 기반 에이전트와 직접 연결.

**Hermes 적용**: hermes-agent의 스킬 뱅크에 공진화 방식 통합 시 에이전트 자율성 향상 가능. 장기 태스크(긴 대화, 멀티스텝 프로젝트)에서 효과 예상.

**대체 관계**: [[SkillClaw]](집단 진화) + [[genericagent]](스킬트리 자동 성장) 대비 공진화의 독자적 메커니즘 구분 필요.

> [!question] 미해결 질문
> - 공진화 루프의 실제 수렴 속도와 안정성?
> - 스킬 뱅크 크기와 성능의 상관관계 수치?

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[에이전트-메모리-레이어]]
- [[SkillClaw]]
- [[hermes-agent]]
- [[genericagent]]

## 원본
- 출처: https://huggingface.co/papers/2604.20987
- 신뢰도: ⭐⭐ (arXiv 논문, 신규)
