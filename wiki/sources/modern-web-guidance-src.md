---
title: "GoogleChrome/modern-web-guidance-src — 코딩 에이전트에 최신 웹 표준을 주입하는 스킬 (자체 eval: 무가이드 52–60% → 가이드 82–96%)"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, frontend, web-platform, eval, google]
created: 2026-11-14
updated: 2026-11-14
sources: [https://github.com/GoogleChrome/modern-web-guidance-src]
reliability: high
---

**레포**: [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) · ★**5,174** · fork 283 · Apache-2.0(코드) + CC-BY 4.0(`guides/`) · TypeScript · repo id 1143633223 · created 2026-01-27 · pushed 2026-11-14T02:08Z (GitHub API 볼트 실측 11-14 09:04Z). 수집기 11-13 ★3,849 → 하루 남짓 **+1,325**.

## 핵심 인사이트
> [!insight] "모델이 이미 아는 것은 지운다" — 가이드의 존재 이유를 eval 로 정한 스킬
> 배포 레포 `GoogleChrome/modern-web-guidance` 의 원본(가이드 작성·보정·평가 코드). View Transitions · Anchor Positioning · Popover · container queries · `scheduler.yield` 등 최근 수년의 웹 플랫폼 기능을 가이드로 만들어 에이전트 컨텍스트에 주입한다. 스킬 팩 자체는 **약 205 토큰**(`modern-web-guidance`) · 175 토큰(`chrome-extensions`)이고 본문은 CLI 검색으로 필요할 때만 불러온다. README 는 Chrome · Edge · Firefox · MDN 팀 공동 관리라고 적는다.
> 핵심은 선별 기준이다 — *opportunity*(100% − 무가이드 통과율)와 *uplift*(가이드 − 무가이드)를 재서, 모델이 가이드 없이도 통과하는 내용은 **잘라낸다**. [[에이전트-스킬]]이 "많이 넣을수록 좋다"가 아니라 "모델이 모르는 것만 넣는다"로 설계된 드문 사례다.

> [!warning] 수집기 "README 본문에 eval 수치 없음" — 볼트 실측과 다르다
> README 593–610행 `### Recent eval results snapshot`(자동 주입 구간)에 표가 있다. 11-08 행:
> | 에이전트 + 모델 | 과제 / 체크 | 무가이드 → 가이드 |
> |---|---|---|
> | antigravity_cli (gemini-4-argon) | 214 / 1,673 | 58% → 94% (**+36pp**) |
> | claude_code (opus-5-5) | 215 / 1,801 | 57% → 88% (**+31pp**) |
> | codex_cli (gpt-6.1-sol) | 215 / 1,795 | 54% → 82% (**+28pp**) |
>
> 표 10행 전체 범위: 무가이드 52–60% · uplift +27~+36pp. → [[메타데이터-부재-추론]]("없다"는 판정은 원문 끝까지 읽은 뒤에만 — 108KB README 의 570행 이후에 있었다).

> [!warning] 이 수치를 읽는 법
> 1. **과제가 가이드에서 생성된다** — 파이프라인이 "전문가 가이드·데모 → 과제 생성 → 채점기 보정 → 에이전트 평가" 순서다. 채점기는 "가이드의 구현 요구사항을 따랐는가"를 본다. 즉 측정한 것은 *가이드가 있을 때 가이드대로 하는가*이고, 임의의 프런트엔드 작업 품질 향상이 아니다 → [[분포내-우위]].
> 2. 자체 측정 · 기반 앱 2종(`daily-grind` · `devtools-times`).
> 3. **텔레메트리 기본 켜짐** — 설치 수 · 호출 에이전트명 · 가이드 ID · **에이전트가 만든 CLI 검색어**를 Google 이 수집(원문 프롬프트는 미수집이라고 명시). 끄기: `DISABLE_TELEMETRY=1`.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★5,174 · 하루 +1,325 · Google 공식 · 자체 eval 표 공개(자동 갱신).
- **즉시 활용**: YES — 볼트 사용자의 영상 SaaS 프런트엔드(Next.js) 작업을 에이전트에 맡길 때 `npx modern-web-guidance@latest install`(대화형 마법사) 한 번. 단 텔레메트리를 끄고 시작.
- **6개월 영향력**: 플랫폼 벤더가 "에이전트용 문서"를 eval 과 함께 배포하는 형식이 표준이 될 수 있다. 무가이드 통과율 52–60% 는 프런티어 모델도 최신 웹 API 절반 가까이를 놓친다는 벤더 측 수치다.
- **대체 관계**: 프로젝트별 CLAUDE.md 에 손으로 적던 "구식 패턴 쓰지 마" 규칙을 대체. [[chrome-devtools-mcp]](실행·디버그)와는 보완.
- **허와 실**: uplift 는 크지만 과제가 가이드 유래. 무가이드 기준선이 높아질수록 가이드는 줄어드는 구조라 수치는 시점 의존.
- **액션**: 설치 시험(아래).

> [!action] 당장 할 것
> 프런트엔드 레포 1개에서 `DISABLE_TELEMETRY=1` 설정 후 설치 → `legacy-scan` 으로 레거시 패턴 수를 한 번 센다. 설치 전후 같은 작업 1건의 diff 를 비교.

## 관련 페이지
- [[에이전트-스킬]] · [[분포내-우위]] · [[메타데이터-부재-추론]] · [[Google]] · [[chrome-devtools-mcp]] · [[anthropics-skills]] · [[하네스-설계-축]]

## 원본
- 출처: https://github.com/GoogleChrome/modern-web-guidance-src
- 확인 범위: GitHub API 메타 · README 전문 내려받아 eval 절(570–610행) · 텔레메트리 절 · 라이선스 절 판독 · 🔴 Eval Dashboard 미열람 · 설치·실행 미확인
- 신뢰도: ⭐⭐⭐ (Google 공식 · 자체 eval 표)
