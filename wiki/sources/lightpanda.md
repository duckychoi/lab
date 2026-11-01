---
title: "lightpanda-io/browser — Zig 헤드리스 브라우저, 기본 텔레메트리 켜짐"
type: source
domain: ai-news
tags: [ai-news, browser, mcp, agent-web]
created: 2026-11-01
updated: 2026-11-01
sources: [https://github.com/lightpanda-io/browser]
reliability: medium
---

**GitHub**: https://github.com/lightpanda-io/browser · ★**39,489** · fork 1,924 · AGPL-3.0 · 생성 2023-02-07 · 푸시 2026-11-01T09:35Z

## 핵심 인사이트
> [!insight] 볼트의 추적 공백이 이미 쓰는 도구였다
> [[에이전트-웹접근]]은 09-08에 lightpanda를 "미채택 · 추적 공백"으로 적었다. 그런데 이 머신의 `~/.claude.json`에 이미 `lightpanda mcp`가 등록돼 있다. 소스 페이지가 사용 현황보다 뒤처졌던 셈이다.

> [!warning] 수집기 요약에 없는 두 가지
> - **텔레메트리가 기본 켜짐**이다. `LIGHTPANDA_DISABLE_TELEMETRY=true`로 끈다. 🔴 이 머신의 MCP 설정은 `env: {}`라 끄지 않은 상태다.
> - **벤치 조건**: AWS m5.xlarge · Go chromedp 크롤러 · Chrome 143 · 100페이지 · `smem` 기준의 제작사 측정이다. 123MB 대 2GB · 5초 대 46초는 이 조건의 값이고, JS가 무거운 사이트의 호환성은 말해 주지 않는다.

## 도메인별 추출
- **즉시 활용**: YES. 이미 등록돼 있다. `mcp` 서버(stdio · HTTP 세션 분리), `--dump markdown` 지원.
- **대체 관계**: 렌더링 충실도가 필요 없는 조회에서 Chromium을 대체한다. [[browser-use]] · [[chrome-devtools-mcp]]와 보완 관계이고 스크린샷 용도는 아니다.
- **허와 실**: AGPL이라 서비스 내장 시 소스 공개 조건을 검토해야 한다. 내부 도구로 쓰는 데는 문제가 작다(법률 판단 아님).

> [!action] 당장 할 것
> MCP 설정 env에 `LIGHTPANDA_DISABLE_TELEMETRY=true` 추가 여부 결정(사용자 설정 파일이라 볼트가 바꾸지 않았다).

## 관련 페이지
- [[에이전트-웹접근]] · [[browser-use]] · [[chrome-devtools-mcp]] · [[agent-governance-toolkit]]

## 원본
- 출처: https://github.com/lightpanda-io/browser
- 벤치: https://github.com/lightpanda-io/demo/blob/main/BENCHMARKS.md
- 확인 범위: GitHub API · README · BENCHMARKS.md · 🔴 벤치 재현 없음
- 신뢰도: ⭐⭐⭐ (★39,489 · 벤치 방법 공개 · 제작사 측정)
