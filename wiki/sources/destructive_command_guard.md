---
title: destructive_command_guard — AI 에이전트 위험 명령 사전 차단 가드 (Rust)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-safety, guardrail, rust, security, devsecops]
created: 2026-07-13
updated: 2026-07-16
sources: []
reliability: medium
---

# destructive_command_guard (Dicklesworthstone/destructive_command_guard)

> [!note] 2026-07-16 갱신
> GitHub ⭐**4,913 (당일 +471)** ← 3,447 (07-13). 사흘 새 +1.5K로 상승 지속 — 에이전트 셸 seatbelt 수요가 실재. 같은 배치서 [[openinterpreter]](로컬 저비용 코딩 에이전트) 재부상과 맞물려 "무인 로컬 실행 + 파괴 명령 차단" 조합 가치가 커짐.

> [!insight] 핵심 인사이트
> ⭐3,447 (2026-07-13, 당일 +444 — 신규 급상승). AI 에이전트가 실행하려는 **위험한 git·shell 명령을 실행 직전에 가로채 차단하는 Rust 가드**. `rm -rf`, `git reset --hard`, `git push --force`, 대량 삭제 같은 비가역 명령을 정적으로 판별해 막는다. 에이전트가 셸을 자유롭게 다루는 시대에 "실수 한 번이 레포·시스템을 날린다"는 실질 위험에 대한 **최소 안전장치(seatbelt) 레이어**. [[strix]]·[[VulnClaw]]가 *공격/취약점 탐지*라면 이건 *자기 파괴 방지*로, 에이전트 안전 스택의 반대편 축이다.

> [!action] 당장 할 것
> 로컬 코딩 에이전트가 셸 명령을 실행하는 환경(Claude Code·자동화 크론)에 pre-exec 훅으로 얹어 비가역 명령 게이트 실측. 오탐(false block)률과 우회 가능성 확인.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ⭐3.4K·당일 +444로 관심 급증이나 신생. 커버하는 명령 패턴의 완전성·우회 내성은 미검증. Rust라 통합 오버헤드는 낮음.
- **즉시 활용**: MAYBE → 이 위키를 갱신하는 것 같은 **자동화 크론·에이전트 셸 실행**에 안전장치로 유용. 다만 룰 기반이라 새 위험 패턴은 놓칠 수 있어 방어의 한 겹으로만.
- **6개월 영향력**: 에이전트 자율 실행이 늘수록 "가드레일"이 필수 인프라가 되는 흐름. 정책 기반 명령 필터가 에이전트 런타임 표준 컴포넌트로 편입될 가능성.
- **대체 관계**: [[CubeSandbox]]·격리 샌드박스가 "위험을 격리"라면 이건 "위험을 사전 차단" — 상보. [[strix]]·[[VulnClaw]]·[[SkillSpector]] 같은 공격/감사 도구와 다른 방어측.
- **허와 실**: 룰 기반 블록리스트는 우회에 취약. "완전 안전"이 아닌 "명백한 실수 방지" 수준으로 기대치 설정 필요.
- **액션**: star. 자동화 셸 실행 파이프라인에 실험 도입해 오탐률·차단 커버리지 실측.

## 관련 페이지
- [[strix]]
- [[VulnClaw]]
- [[SkillSpector]]
- [[CubeSandbox]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/Dicklesworthstone/destructive_command_guard
- 스타: ⭐3,447 (2026-07-13, 당일 +444, 신규 급상승)
- 신뢰도: ⭐⭐ (신생·급상승. 룰 커버리지·우회 내성 미검증 — 방어의 한 겹으로 활용)
