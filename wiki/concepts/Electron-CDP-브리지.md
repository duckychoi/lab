---
title: Electron CDP 브리지 — API 없는 데스크톱 앱을 에이전트 도구로 (잠정)
type: concept
domain: ai-news
tags: [ai-news, concept, mcp, electron, cdp, 잠정, 신설]
created: 2026-09-19
updated: 2026-09-19
sources: [tradingview-mcp.md]
reliability: medium
---

# Electron CDP 브리지 *(잠정 · 표본 2)*

> [!insight] 한 줄
> **공식 API가 없는 Electron 데스크톱 앱을 Chrome DevTools Protocol 디버그 포트로 열어 MCP 도구로 감싼다.** [[tradingview-mcp]](TradingView Desktop, 포트 9222, 도구 84개) 가 설계도이고 [[After-Effects-MCP]] 가 같은 부류(앱 내부 스크립팅 경로 이용)다.

## 비용 (저자 명시 + 볼트)
- 🔴 **비공식 내부 API** — 앱 업데이트 시 예고 없이 파손(tradingview-mcp 저자 명시)
- 🔴 **약관 충돌** 가능성 · 계정 정지 위험은 사용자 부담
- 🔴 로컬 디버그 포트 노출(일반 지식, 레포에서 미검증)
- 🔴 유지보수: tradingview-mcp 는 열린 PR 195건 · 7주 무병합

## 완화
- 앱 버전 고정 · **압축 출력을 기본값**으로(80KB → 5~10KB 주장, 조건 미기재)

## 관련 페이지
- [[tradingview-mcp]] · [[After-Effects-MCP]] · [[자기제한-명시]]
