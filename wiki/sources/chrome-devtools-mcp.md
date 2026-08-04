---
title: ChromeDevTools/chrome-devtools-mcp
type: source
domain: ai-news
tags: [ai-news, mcp, chrome, devtools, browser-automation, debug]
created: 2026-04-18
updated: 2026-07-31
sources: []
reliability: high
---

# ChromeDevTools/chrome-devtools-mcp

> [!update] 2026-07-31 갱신 — ⭐48,211 (WebFetch "48.2k"·Apache-2.0 실확인)
> GitHub 스타 **48,211**(2026-07-31 자동수집, 당일 +80) ← 45,886(07-05). 약 4주간 +2.3k 완만 성장으로 공식 MCP의 표준 지위 굳힘. **WebFetch 재확인: 48.2k·TypeScript·Apache-2.0**(기존 페이지에 라이선스 미표기였음 — 이번에 확정), CDP를 MCP로 노출해 코딩 에이전트가 라이브 Chrome을 제어·검사한다는 성격 동일. 내 lightpanda 브라우저 자동화와 같은 축의 공식 레퍼런스.

> [!insight] 핵심 인사이트
> Chrome DevTools 공식팀이 직접 MCP 서버를 만들었다 — 브라우저 디버깅이 LLM 에이전트의 1급 도구로 편입되는 시점. Claude Code 등 코딩 에이전트가 브라우저를 직접 열어 콘솔 오류 확인·DOM 조작·네트워크 탭 분석까지 수행 가능.

## 도메인별 추출

**즉시 활용**: YES — [[Claude-Code-워크플로우]]에서 웹 디버깅 자동화에 바로 통합 가능
**신뢰도**: ⭐⭐⭐⭐⭐ (Chrome DevTools 공식 레포, ⭐45,886 / +304/일, 2026-07-05) ← ⭐35,992 (2026-04-18)
**6개월 영향력**: 코딩 에이전트가 "실행-디버그-수정" 루프를 브라우저 수준에서 닫을 수 있게 됨 → 수동 브라우저 디버깅 감소
**대체 관계**: Playwright MCP, Puppeteer 대비 DevTools 프로토콜 직접 접근으로 더 낮은 레벨 제어

## 주요 기능

- MCP 서버로 Chrome DevTools Protocol 노출
- 코딩 에이전트가 자연어로 브라우저 제어·디버깅 수행
- 콘솔 오류, 네트워크 요청, DOM 상태를 LLM이 직접 읽고 수정
- 공식 Chrome DevTools 팀 개발 → 장기 지원 기대

> [!action] 당장 할 것
> 설치 후 Claude Code + chrome-devtools-mcp 연결 테스트. 프론트엔드 디버깅 워크플로우에 통합.

## 관련 페이지

- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]
- [[superpowers]]

## 원본

- 출처: https://github.com/ChromeDevTools/chrome-devtools-mcp
- 스타: ⭐**48,211** (2026-07-31, 당일 +80, WebFetch "48.2k"·Apache-2.0 실확인) ← ⭐45,886 (2026-07-05, +304/일) ← ⭐35,992 (2026-04-18)
- 라이선스: Apache-2.0 / TypeScript
- 신뢰도: ⭐⭐⭐⭐⭐
