---
title: "elementalsouls/Claude-BugHunter — 버그바운티·레드팀용 Claude Code 스킬 번들 (83 스킬 · 15 명령)"
type: source
domain: ai-news
tags: [ai-news, github-trending, security, bug-bounty, agent-skill, claude-code]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/elementalsouls/Claude-BugHunter]
reliability: medium
---

**레포**: [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) · ★**6,880**(볼트 11-16 실측) · fork 1,054 · Python · MIT · repo id 1229774092 · 생성 2026-05-05.

## 핵심 인사이트
> [!insight] 공개 리포트를 "출처 인용 가능한 스킬"로 — 그리고 그 비율을 스스로 밝힌다
> README 5행: **83 skills** · 15 slash commands · **681 disclosed-report patterns (433 now individually cited & auditable)**. 즉 패턴의 **64%** 만 개별 출처 추적 가능. 구성: 24개 취약점 클래스 `hunt-*` 58개(탐지 패턴 · 페이로드 · 우회 표 · 체인 템플릿) + 방법론 + 엔터프라이즈 경계 체인(M365/Entra · Okta · vCenter · SSL-VPN 등 2024–2026 CVE) + 보고 단계(`triage-validation` 7문항 게이트 · VRT 심각도 · PII 마스킹).

> [!warning] 사용 범위 · 수치
> 공격 도구 성격 — **허가된 스코프(바운티 프로그램 · 계약 레드팀)에서만**. 정확도 · 성공률 수치 0(README 예시 출력은 연출 데모 — 수집기). 🟡 API description 은 "82 skills", README 는 "83" — 사소한 불일치. [[Claude-Red]](SnailSploit)와 같은 공격 보안 스킬 계열.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★6,880 · 6개월 차 · 측정 0.
- **즉시 활용**: NO(볼트 용도 무관). 보안 점검을 하는 경우 `triage-validation` 게이트(오탐 보고 방지)만 참고 가치.
- **6개월 영향력**: 스킬 자동 로드(주제 기반) + 공격 지식 번들 → 바운티 플랫폼의 AI 생성 저품질 리포트 문제를 키울 수도, 7문항 게이트로 줄일 수도.
- **허와 실**: 지식베이스로는 실재, 효과는 미측정. 출처 인용률 64% 는 스스로 공개한 정직성 지표.
- **액션**: 없음.

## 관련 페이지
- [[Claude-Red]] · [[에이전트-스킬]] · [[SkillEvaluator]](스킬 품질 측정) · [[Claude-Code-워크플로우]]

## 원본
- 출처: https://github.com/elementalsouls/Claude-BugHunter
- 확인 범위: GitHub API 메타 · README 5 · 36행(볼트) · 🔴 스킬 구성 세부는 수집기 판독 · 실행하지 않음(의도)
- 신뢰도: ⭐⭐ (★6,880 · 측정 0)
