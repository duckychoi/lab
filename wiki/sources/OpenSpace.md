---
title: OpenSpace — AI 에이전트를 위한 스킬 관리 레이어 (품질평가·자가진화)
type: source
domain: ai-news
tags: [ai-news, skill-management, agent-harness, self-evolving, claude-code, terminal-bench]
created: 2026-07-29
updated: 2026-07-29
sources: []
reliability: high
---

# OpenSpace (HKUDS/OpenSpace · GitHub ⭐7.2k)

> [!insight] 핵심 인사이트
> 홍콩대 [[HKUDS]]의 **"AI 에이전트를 위한 스킬 관리 레이어"** — 에이전트가 스킬을 **검색·평가·진화**시키게 한다. 결정적 차별점은 **"설명이 아닌 실제 실행 결과로 스킬 품질을 측정"**: 스킬이 선택됐는지·적용됐는지·완료됐는지·폴백으로 대체됐는지를 추적한다. 진화는 세 메커니즘 — **FIX(고장 수리)·DERIVED(특화 버전 생성)·CAPTURED(재사용 서브워크플로 저장)**. Local-First(로컬 실행·관리 + 선택적 클라우드 공유), 복구 가능 세션·권한 인지 도구 실행. **Terminal-Bench 2.1에서 콜드런 65.2% → 웜런 78.7%**(자가진화 스킬 라이브러리 효과)를 제시. [[book-to-skill]](문서→스킬)·[[Skill-Self-Play]](스킬 self-play RL)·[[impeccable]]과 함께 **"스킬을 만들고→쓰고→증거로 개선한다"** 스킬 라이프사이클의 관리 레이어. MIT.

> [!action] 이 위키 스킬 운용과 직접 동형
> OpenSpace의 **"실행 결과로 스킬 품질 측정(선택/적용/완료/폴백)"**은 내가 wiki·reat·pptx 등 다수 스킬을 운용하는 방식에 그대로 적용된다. 스킬별 **성공/폴백 로그를 남겨 품질 증거화 → FIX/DERIVED/CAPTURED로 개선**하는 루프를 log.md 확장으로 실험 가능.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 스타 7.2k·MIT·기능 WebFetch 실확인. Terminal-Bench 65.2→78.7% 개선은 **자체 벤치**로 독립 재현 전.
- **즉시 활용**: YES(개념) — 내 스킬 운용에 **품질 증거 로깅 + 자가진화 3메커니즘**을 부분 이식. [[Claude Code]]·OpenClaw·nanobot 통합 지원이라 하네스 호환.
- **6개월 영향력**: "스킬"이 정적 프롬프트에서 **실행 증거로 진화하는 관리 대상**으로 격상. [[ECC]] 하네스의 스킬 레이어와 수렴.
- **대체 관계**: [[ECC]] 번들의 스킬 관리 부분을 전용화한 것. [[book-to-skill]](생성)·[[Skill-Self-Play]](학습)와 라이프사이클 분업.
- **허와 실**: 65.2→78.7%는 자체 벤치 — "자가진화가 성능을 올린다"의 방향은 타당하나 절대 수치는 검증 전.
- **액션**: FIX/DERIVED/CAPTURED 세 연산의 실제 트리거 조건을 코드로 확인 → wiki 스킬 log.md에 "선택/적용/완료/폴백" 필드 추가 실험.

## 관련 페이지
- [[HKUDS]]
- [[ECC]]
- [[book-to-skill]]
- [[Skill-Self-Play]]
- [[impeccable]]
- [[에이전트-메모리-레이어]]
- [[AI-에이전트-프레임워크]]
- [[Claude Code]]
- [[ai-news]]

## 원본
- 출처: https://github.com/HKUDS/OpenSpace
- 스타: ⭐7.2k (2026-07-29, 당일 +58 — raw 7,161과 일치), MIT
- 기능: 실행결과 기반 스킬 품질평가(선택/적용/완료/폴백)·자가진화 3메커니즘(FIX/DERIVED/CAPTURED)·Local-First·복구세션·권한인지 실행·Claude Code/OpenClaw/nanobot 통합
- 벤치(자체): Terminal-Bench 2.1 콜드 65.2% → 웜 78.7%
- 신뢰도: ⭐⭐⭐ (스타·라이선스·기능 WebFetch 실확인, 벤치 자체·재현 전 medium)
