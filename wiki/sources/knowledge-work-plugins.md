---
title: "knowledge-work-plugins — Anthropic이 직접 공개한 직무별 플러그인 11종"
type: source
domain: ai-news
tags: [ai-news, github-trending, anthropic, agent-skills, plugin, connector, cowork]
created: 2026-10-10
updated: 2026-10-10
sources: []
reliability: high
---

# knowledge-work-plugins — "스킬 → 플러그인 → 직무"로 한 층 더 묶인다

**GitHub**: https://github.com/anthropics/knowledge-work-plugins
**★28,497** (당일 +709 · 트렌딩 **6위**) · fork 3,258 · watchers 186
**open_issues 140 = 순수이슈 79 + PR 61**(PR 비중 **43.6%**) · Apache-2.0 · Python · created 2026-01-23 · pushed 2026-10-10
**제공**: [[Anthropic]] (공식 조직 레포)

> [!insight] 핵심 인사이트
> **묶음 계층이 공식 공급자 쪽에서 나왔다.** 스킬·커넥터·슬래시커맨드·서브에이전트를 **직무 단위로 묶은 플러그인 11종**(productivity · sales · customer-support · product-management · marketing 등)을 Claude Cowork 용으로 공개하고 Claude Code 호환도 명시한다.
> 📌 **금일 교차의 상층**: [[mattpocock-skills]] · [[diagram-design]] 는 **스킬 단위**, 10-06 [[t3code]] 는 **하네스 제어면**, 본 레포는 **직무 묶음**.
> ⇒ ⚖️ **같은 날 3개 층이 동시에 관측된다** — 10-06 *"하네스 생태계가 층으로 쌓인다"* 가설의 **보강 증거이고 반증이 아니다.** → [[하네스-설계-축]]

> [!warning] 측정 수치 0개 · 외부 실행 문턱이 높다
> **플러그인이 업무 품질·시간을 얼마나 바꾸는지 측정이 전혀 없다.**
> ⚠️ **커넥터 의존이 크다** — 실행에 외부 SaaS 계정이 필요하다(Slack · Notion · Asana · Linear · Jira · HubSpot · Intercom · Figma · Amplitude · Microsoft 365 등을 표로 열거).
> ⇒ 📌 **금일 최저 실행 문턱은 [[laya]]**(`pip install laya`)이고 본 레포는 그 반대편 극단이다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 공식 조직 레포 · Apache-2.0 · 커넥터 목록 명시. 능력 측정은 0.
- **즉시 활용**: **부분 YES** — Claude Code 호환을 명시하므로 **플러그인 구조(스킬+커맨드+서브에이전트 묶음)를 볼트 스킬 조직화의 참조 설계로 읽을 수 있다.** 🔴 **다만 실행은 커넥터 계정에 묶여 있어 볼트 환경(Gmail·Drive·Calendar **미인증**)에서는 대부분 돌지 않는다.**
- **6개월 영향력**: 스킬의 단위가 "기능"에서 "직무"로 올라가면 **볼트의 스킬 디렉터리도 묶음 계층이 필요해진다**(현재 볼트는 평면 스킬 40여 종).
- **대체 관계**: 개별 스킬 수집·설치를 **직무 단위 묶음**이 대체한다. [[mattpocock-skills]] 의 *"작게 쪼개라"* 와 **방향이 반대다** ⇒ ⚖️ **같은 날 두 반대 처방이 도착했다** → [[대립레시피-동시도착]] 후보.
- **허와 실**: 🔴 `topics` **0개** · `description` **1줄** ⇒ [[메타데이터-부재-추론]] 누적(금일 2건: 본 레포 · [[mattpocock-skills]]). 📌 *"11개를 오픈소스로 공개한다"* 는 **개수 선언**이고 **각 플러그인 내부 스킬 수는 미집계**다(볼트가 확인 가능).
- **액션**: 플러그인 1종의 디렉터리 구조만 읽어 **볼트 스킬 묶음 설계**와 대조한다.

> [!question] 미해결
> - 각 플러그인 **내부 스킬 수** 미집계.
> - Claude Code 호환의 **실제 범위**(커넥터 없이 되는 플러그인이 몇 개인지) 미확인.
> - [[Anthropic]] 공식 조직 레포가 **볼트 수집에 처음 들어왔는지** 미확정 — 엔티티 페이지는 존재한다.

## 관련 페이지
- [[하네스-설계-축]] — 3개 층 동시 관측의 최상층
- [[대립레시피-동시도착]] — [[mattpocock-skills]] 의 "작게 쪼개라"와 반대 방향
- [[메타데이터-부재-추론]] · [[에이전트-스킬]]
- [[t3code]] — 하네스 제어면 층
- [[laya]] — 실행 문턱의 반대 극단
- [[Anthropic]] · [[ai-news]]

## 원본
- 출처: https://github.com/anthropics/knowledge-work-plugins
- 수집: 2026-10-10 자동수집 (ai-news)
- 검증: GitHub API 실측 · `open_issues` 분해 140=79+61 검산 통과 · **금일 5/5 전건 검산 통과**(136=97+39 · 163=149+14 · 81=20+61 · 286=116+170 · 140=79+61)
- 신뢰도: ⭐⭐⭐⭐
