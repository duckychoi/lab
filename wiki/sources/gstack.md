---
title: "gstack — YC CEO Garry Tan의 Claude Code 세팅을 역할 슬래시 커맨드 23+8개로 공개. ★13.8만의 근거는 저자 본인의 '810×' 생산성 자기측정이고, 인용한 OpenClaw 스타 수는 이미 낡았다"
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, agent-skills, slash-commands, role-prompting, openclaw, self-reported, auto-update]
created: 2026-10-26
updated: 2026-10-26
sources: [https://github.com/garrytan/gstack]
reliability: medium
---

# garrytan/gstack — ★137,768 · TypeScript · MIT · Bun

> [!insight] 핵심 인사이트 — **"역할 = 슬래시 커맨드"가 1인 개발 하네스의 사실상 표준 포맷이 되는 중이고, 그 확산 동력은 성능이 아니라 저자의 권위다**
> gstack은 Claude Code를 가상 팀으로 만든다: `/office-hours`(제품 심문) → `/plan-ceo-review`(범위 재검토) → `/review`(프로덕션 버그) → `/qa`(실브라우저) → `/ship`(PR), 그 밖에 `/cso`(OWASP+STRIDE) 등. README 기준 **"Twenty-three specialists and eight power tools, all slash commands, all Markdown"**. 즉 실체는 Markdown 스킬 묶음 + Bun으로 빌드한 헤드리스 브라우저 바이너리(`/browse`)다 → [[에이전트-스킬]]·[[Claude-Code-워크플로우]].
> ★137,768 · fork 20,424는 배치 최대이나, README의 근거는 전부 **저자 자기측정**: *"my 2026 run rate is ~810× my 2013 pace (11,417 vs 14 logical lines/day)"*, 40개 본인 레포 기준. 저자 스스로 LOC 논란을 인정하고 방법론 문서를 따로 둔 점은 [[자기제한-명시]]로 평가할 만하나, 도구 효과의 제3자 측정은 아니다 → [[스타-근거-비동행]].

> [!warning] 검증 / 교정
> - 🟡 **낡은 인용 수치**: README *"Peter Steinberger built OpenClaw — 247K GitHub stars"* ↔ 볼트 실측 [[openclaw]] **★393,100**(2026-10-26T09:07Z). README 안의 타 레포 수치가 작성 시점에 고정됨 → [[캐시된-지표-신선도]].
> - 수집기 "role slash commands"는 맞으나 규모 한정어가 빠짐: 23 전문가 + 8 power tools, Claude 외 `--host codex` 등 다중 에이전트 설치 지원.
> - **OpenClaw 통합** 확인: OpenClaw가 ACP로 Claude Code 세션을 띄울 때 gstack 스킬 사용 + ClawHub 네이티브 스킬 4종(office-hours·ceo-review·investigate·retro). Peter Steinberger 언급은 README 문장, 볼트 [[OpenClaw-Foundation]] 소유 구조와는 별개.
> - **설치 프롬프트가 CLAUDE.md를 수정**: *"never use mcp__claude-in-chrome__* tools"* 문구를 넣도록 지시 — 다른 브라우저 도구를 배제하는 정책이 사용자 설정에 주입됨.
> - **Team mode 자동 업데이트**: 모든 Claude Code 세션 시작 시 1시간 간격 업데이트 체크, `required` 모드는 훅으로 미설치 팀원 스킬 차단 → 1인 소유 레포에 대한 공급망 의존. 텔레메트리는 **opt-in(기본 off)**, 업데이트 체크는 기본 on.
> - Bun v1.4.2+ (1.3.3 미만은 `.env` 노출 위험으로 거부) — 수집기 "Bun" 확인.

## 도메인별 추출 (ai-news)

- **신뢰도**: ★137,768(수집기 일치) · fork 20,424 · open issues 155 · created 2026-03-11(7.5개월) · pushed 2026-10-26T09:05Z(실측 2분 전, 매우 활발) · 논문·제3자 벤치 없음.
- **즉시 활용**: **부분 YES** — 통째 설치(CLAUDE.md 주입·자동 업데이트)는 NO. `/review`·`/qa`·`/office-hours`의 SKILL.md를 **읽고 패턴만 차용**하는 것은 YES: "계획 단계에서 강제 질문(forcing questions)으로 범위를 깎는" 구조는 볼트 인제스트 판정에도 이식 가능.
- **6개월 영향력**: 높음 — 저자 영향력으로 "CEO/EM/QA/릴리스 역할 분할"이 Claude Code 사용 관행의 기본 템플릿이 될 가능성. [[claude-seo]]가 같은 구조를 SEO에 적용한 사례.
- **대체 관계**: [[everything-claude-code]]·[[claude-howto]]와 같은 "하네스 설정 묶음" 층에서 최대 규모. [[cindy]]·[[openclaw]]는 그 위에서 세션을 띄우는 오케스트레이터 층 → [[하네스-설계-축]].
- **허와 실**: 실 = 잘 다듬은 역할 프롬프트 + 실브라우저 QA 바이너리 + 다중 호스트 렌더링(글로벌 설치 632→63 SKILL.md 정리 같은 운영 세부). 허 = "한 명이 20명처럼"은 저자 개인 생산성 서사이며 도구 기여분 분리 불가. [[Andrej Karpathy]] 인용으로 시작하는 권위 프레이밍.
- **액션**: star + `review/`·`qa/`·`office-hours/` SKILL.md 열람(실행 없이). Team mode 금지.

## 관련 페이지
- [[에이전트-스킬]] · [[Claude-Code-워크플로우]] · [[하네스-설계-축]] · [[자기제한-명시]] · [[스타-근거-비동행]] · [[캐시된-지표-신선도]]
- [[openclaw]] · [[OpenClaw-Foundation]] · [[Andrej Karpathy]] · [[Anthropic]]
- 유사: [[everything-claude-code]] · [[claude-howto]] · [[cindy]]
- 같은 배치: [[experiential]] · [[sandbox-runtime]] · [[claude-seo]] · [[infinite-canvas]]
- [[ai-news]]

## 원본
- 출처: https://github.com/garrytan/gstack · README raw 90,120 B
- 볼트 실측(GitHub API, 2026-10-26T09:07Z): ★137,768(수집기 일치) · fork 20,424 · open issues 155 · MIT · TypeScript · created 2026-03-11 · pushed 2026-10-26T09:05Z · 루트 항목 111개
- 비교 실측: openclaw/openclaw ★393,100 (README 인용 247K)
- 신뢰도: ⭐⭐ (★ 최대급이나 효과 근거는 저자 자기측정)
