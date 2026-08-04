---
title: design.md — 코딩 에이전트용 비주얼 아이덴티티 명세
type: source
domain: ai-news
tags: [ai-news, github-trending, design-system, agent, google-labs, spec, frontend]
created: 2026-06-25
updated: 2026-06-27
sources: []
reliability: high
---

# design.md (google-labs-code/design.md)

> [!insight] 핵심 인사이트
> ⭐21,770 (2026-06-27, 당일 +2,407 — 급등 재가속; ⭐20,145→21,770). [[Google-Labs]]가 제안한, **코딩 에이전트가 디자인 시스템을 지속적으로 이해하도록 시각 아이덴티티를 기술하는 포맷 명세**. 핵심은 `CLAUDE.md`/`AGENTS.md`가 코드 컨벤션을 에이전트에 주입하듯, `design.md`가 **색·타이포·간격·컴포넌트 규칙을 에이전트의 영속 컨텍스트로** 만든다는 발상 — 이 위키의 [[LLM-Wiki]]·스키마 파일 철학과 정확히 같은 "에이전트용 설정 파일" 계보. 신뢰도는 Google Labs 발(發)이라 높음.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — Google Labs 공식 + ⭐17,801. 포맷 명세라 코드 안정성 이슈는 적고, 채택 여부가 관건.
- **즉시 활용**: YES — 내 [[tools-frontend]]·[[reat-layout]] 작업에서 에이전트가 일관된 디자인 토큰을 따르도록 `design.md`를 프로젝트에 두는 패턴 즉시 도입 가능. [[design.md]] = 프론트엔드판 `CLAUDE.md`.
- **6개월 영향력**: 에이전트 코딩의 "디자인 일관성" 문제(매번 색·간격이 흔들림)를 표준 파일로 해결하는 흐름. 보편화 시 모든 레포에 `design.md` 동반.
- **대체 관계**: Figma 토큰/스토리북을 *대체*하는 게 아니라, 그것들을 **에이전트가 읽는 단일 텍스트 명세**로 압축하는 보완재.
- **허와 실**: 명세 자체는 단순(마크다운 규약). 실효는 에이전트 하네스가 이 파일을 실제로 참조·준수하느냐에 달림 — 강제 메커니즘 없으면 권고에 그침.
- **액션**: 명세 포맷 정독 → 내 프론트엔드 프로젝트에 `design.md` 1개 작성·적용 실험.

> [!action] 당장 할 것
> `design.md` 명세를 읽고 [[reat-layout]] / [[tools-frontend]] 프로젝트 루트에 디자인 토큰 명세 파일을 작성, 에이전트가 레이아웃 생성 시 이를 참조하도록 연결.

> [!note] 배경 정보
> "에이전트용 설정 파일" 계보: 코드 → `CLAUDE.md`/`AGENTS.md`, 디자인 → `design.md`. 사람이 아니라 에이전트가 읽는 것을 1순위로 쓰는 문서 패턴이 도메인별로 분화 중.

## 관련 페이지

- [[Google-Labs]]
- [[LLM-Wiki]]
- [[Claude-Code-워크플로우]]
- [[tools-frontend]]
- [[reat-layout]]
- [[ai-website-cloner-template]]

## 원본
- 출처: https://github.com/google-labs-code/design.md
- 스타: ⭐21,770 (2026-06-27, 당일 +2,407) ← ⭐20,145 (06-26, +1,475) ← ⭐17,801 (06-25, +619)
- 신뢰도: ⭐⭐⭐⭐ (Google Labs 공식 명세, 2만 돌파·급등 가속 — 채택 확산 본격화)
