---
title: "backnotprop/plannotator — 에이전트의 plan · diff 에 브라우저에서 주석을 달아 다음 턴으로 돌려보내는 로컬 리뷰 도구"
type: source
domain: ai-news
tags: [ai-news, github-trending, human-in-the-loop, plan-review, code-review, claude-code, mcp]
created: 2026-11-14
updated: 2026-11-14
sources: [https://github.com/backnotprop/plannotator]
reliability: medium
---

**레포**: [backnotprop/plannotator](https://github.com/backnotprop/plannotator) · ★**10,603** · fork 792 · Apache-2.0 · TypeScript · repo id 1123956658 · created 2025-12-28 · pushed 2026-11-14T09:04Z · open_issues 213(이슈+PR) (GitHub API 볼트 실측 — 수집기 수치와 ±1)

## 핵심 인사이트
> [!insight] 에이전트가 계획을 내면 사람이 "글로 답하는" 대신 "문서 위에 표시한다"
> Claude Code · Codex · Copilot CLI · Gemini CLI · OpenCode · Kiro · Droid · Amp · Pi 등에 훅/플러그인으로 붙는다. 에이전트가 plan 을 만들면 로컬 브라우저 리뷰 화면이 열리고, 사용자가 문서 · HTML · diff 에 주석을 달아 **한 번에** 다음 턴으로 돌려보낸다. 로컬 변경 · GitHub PR · GitLab MR · GitButler · jj · Perforce 리뷰 지원.
> **Inbox**(README 100–106행): 여러 에이전트의 질문 · 파일 · 리뷰 요청을 한 창에 모은다. Claude Code · Pi · OpenCode 는 플러그인으로, 그 밖의 에이전트는 MCP(`plannotator inbox mcp`)로 연결.
> ⇒ [[하네스-설계-축]]에서 "사람의 개입 지점"을 텍스트 승인에서 구조화된 주석으로 바꾸는 층이다. [[open-code-review]] 가 리뷰 *판정*을 자동화한다면 이쪽은 리뷰 *입력 경로*를 다듬는다.

> [!note] 프라이버시 — README 172–182행 (볼트 직접 판독)
> *"does not collect usage telemetry or analytics. Plans, diffs, annotations … stay local by default."* 단, 각 화면이 열릴 때 GitHub 에 최신 릴리스를 조회한다(내용은 보내지 않음). 공유 포털 · Workspaces(별도 호스팅 제품)를 쓰면 로컬 저장 모델이 적용되지 않는다. → 한계를 스스로 적은 [[자기제한-명시]] 사례. 같은 날 [[modern-web-guidance-src]] 는 텔레메트리가 기본 켜짐이다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★10,603 · 11개월 차 · 성능 지표가 필요한 종류의 도구가 아니다.
- **즉시 활용**: 조건부 — 데스크톱에서 Claude Code plan mode 를 쓸 때는 YES. 볼트의 스케줄 작업(Telegram · 비대화형)에서는 브라우저를 열 수 없어 NO.
- **6개월 영향력**: 다중 에이전트를 돌릴 때 "사람 대기열"을 한 창으로 모으는 Inbox 형식이 퍼질 수 있다.
- **대체 관계**: 터미널에서 y/n 으로 답하던 plan 승인을 강화.
- **허와 실**: 과장 없음. 설치 시 GitHub Releases · npm 등 외부 접속이 있다(README 236행).
- **액션**: 대화형 세션에서 1회 시험(낮음).

## 관련 페이지
- [[Claude-Code-워크플로우]] · [[open-code-review]] · [[하네스-설계-축]] · [[자기제한-명시]] · [[modern-web-guidance-src]] · [[opencode]]

## 원본
- 출처: https://github.com/backnotprop/plannotator
- 확인 범위: GitHub API 메타 · README(31,360B) 42 · 68 · 100–106 · 172–182 · 236행 직접 판독 · 🔴 설치·실행 미확인
- 신뢰도: ⭐⭐ (★10,603 · 실행 미확인)
