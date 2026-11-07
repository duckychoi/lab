---
title: "SandboxAQ Switch — 기존 메신저 채널을 사람+멀티하니스 에이전트 공용 방으로. Apache 2.0 + 수정 Commons Clause(오픈소스 아님)"
type: source
domain: local-llm
tags: [local-llm, ai-news, github-trending, multi-agent, agent-hub, telegram, slack, self-hosted, commons-clause]
created: 2026-11-07
updated: 2026-11-07
sources: [https://github.com/sandbox-quantum/switch]
reliability: medium
---

**GitHub**: [sandbox-quantum/switch](https://github.com/sandbox-quantum/switch) **★4,144 · 포크 312 · 오픈이슈 631(이슈+PR)**(볼트 11-07 실측 · 수집기 11-06 ★3,988 / 548 → ★+156 · 오픈 +83/1일) · license API `NOASSERTION` · created 2026-07-16 · pushed 2026-11-07T08:58Z · 릴리스 태그 dev 빌드가 하루 여러 개(`switch-agent-controller-v0.31.1-dev.349`, 11-06) · python 트렌딩 11위(11-06)

## 핵심 인사이트
> [!insight] "메신저를 대체하지 않고, 채널을 에이전트가 들어오는 방으로 만든다"
> Slack·Teams·Discord·Telegram·Mattermost 채널 하나하나를 "방"으로 삼고, 팀원과 **서로 다른 하니스의 에이전트**(로컬 Claude Code · 동료의 Codex · 서버의 LangChain 에이전트 — "프로토콜을 말하면 참여")가 같은 대화·결정·문서를 공유한다. 에이전트별 역할·지시·도구(Google Workspace·Jira·GitHub) 부여, **방 단위 가시성**(속한 방만 봄), 방 간 연결로 작업 컨텍스트 이동. 이것은 사용자의 **Telegram 기반 에이전트 운용(cokacdir · Monday/Fryday 멀티 에이전트)** 과 구조가 같다 — 차이는 하니스 이질성을 프로토콜로 흡수한다는 점.

> [!warning] 라이선스 = Apache 2.0 + **파생물까지 확장한 수정판 Commons Clause**
> LICENSE 원문(볼트 11-07 확인): *"licensed to you under the Apache 2.0 License as limited by the 'Commons Clause' … modified … also applies to any derivatives"*. **소프트웨어 판매·유료 호스팅 금지** = OSI 오픈소스가 아니다. 가드레일·비용 리포트는 별도 상용 제품(`Switch Trust` · `Switch ROI`)으로 빠져 있다. 오픈이슈가 하루 +83 으로 급증 중 — 안정성 판단 보류.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 셀프호스팅 가능 · 데스크톱 앱 `Switch Console` 의 `switch-buddy` 가 첫 에이전트·채널 생성을 대화로 안내. 하드웨어 요구치·지연 수치 없음(README).
- **메모리 아키텍처**: 방 = 공유 컨텍스트 단위(대화·결정·문서). 장기 메모리 방식은 README 상단에서 확인되지 않음.
- **Hermes 적용**: 부분 YES — "방 단위 가시성 + 에이전트별 도구 권한" 모델은 ChinameBot/cokacdir 멀티 에이전트 권한 설계에 참고. 다만 사용자 자체 Telegram 봇 체계가 이미 있으므로 **대체가 아니라 설계 차용**.
- **트레이드오프**: 메신저 통합 폭(5종) vs 상용 분리(Trust·ROI) · 라이선스 제약.
- **오픈소스 구현체**: 레포 자체(단, Commons Clause).

## 관련 페이지
- [[AI-에이전트-프레임워크]] · [[하네스-설계-축]] · [[에이전트-메모리-레이어]] · [[Claude-Code-워크플로우]]
- [[pr-agent]] · [[auto-ontology]] · [[scenario-skills]] · [[garden-skills]] (같은 날 GitHub)

## 원본
- 출처: https://github.com/sandbox-quantum/switch
- 확인 범위: GitHub API(볼트 11-07) · LICENSE 원문 상단 12행(볼트 확인) · README 는 수집기 기준(상단 약 55행) · 프로토콜 문서·데모 영상 미열람 · 설치·실행 0회
- 신뢰도: ⭐⭐ (★4.1k · 기업 공개 · 비OSI 라이선스 · 정량 수치 없음)
