---
title: orca — 병렬 코딩 에이전트 개발환경(ADE)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent, ade, worktree, typescript]
created: 2026-07-09
updated: 2026-07-09
sources: []
reliability: high
---

# stablyai/orca (GitHub ⭐14,538)

**GitHub**: https://github.com/stablyai/orca
**스타수**: 14,538 (2026-07-09 기준) · **제작**: stablyai
**라이선스**: MIT · **스택**: TypeScript 96.7%

> [!insight] 핵심 인사이트
> **여러 AI 코딩 에이전트를 병렬로 오케스트레이션하는 ADE(Agent Dev Environment).** WebFetch 실측: [[anthropic-claude-code|Claude Code]]·Codex·OpenCode 등 임의 에이전트를 **격리된 git worktree에서 동시 실행**하고 결과를 비교. ①iOS/Android **모바일 컴패니언 앱**, ②WebGL 렌더링 터미널 스플릿, ③**GitHub·Linear 네이티브 연동**, ④SSH 원격 worktree, ⑤CLI 스크립팅, ⑥브라우저 디자인 모드. "사용자의 자체 구독으로 아무 에이전트나 데스크톱·모바일에서 돌린다"가 핵심 — **벤더 중립 멀티에이전트 IDE**. [[herdr]](터미널 멀티플렉서)와 같은 날 트렌딩해 "**병렬 에이전트 플릿 관리**"가 확립된 카테고리임을 증명. [[codex-plugin-cc]]가 벤더 간 브리지를 깔았다면, orca는 그 위의 **동시 실행·비교 UX 레이어**.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (⭐14,538, README WebFetch 실측 — worktree 병렬·모바일 앱·GitHub/Linear 연동 확인, MIT)
- **즉시 활용**: 후보(중간) — worktree 격리로 에이전트 2~3개에 같은 태스크를 던져 best-of-N 하는 워크플로가 내 작업에 유효. 모바일 관제는 스케줄 태스크 모니터링에 매력.
- **6개월 영향력**: 단일 에이전트 → **여러 에이전트 병렬 후 비교·선택**이 표준 개발 UX로. "어느 모델이 이 태스크에 나은가"를 실행 중 판단.
- **대체 관계**: Cursor·Windsurf 등 단일 에이전트 IDE를 멀티에이전트로 확장·대체. [[herdr]](CLI)와 데스크톱 GUI 축에서 경쟁.
- **허와 실**: 기능 목록은 화려하나 "임의 에이전트 병렬 + 모바일 + 원격"의 실제 안정성은 검증 필요. MIT라 자체 호스팅·확장 가능은 강점.
- **액션**: orca로 [[herdr]]와 동일 태스크(에이전트 2개 병렬 worktree)를 돌려 결과 비교 UX·리소스 점유·모바일 관제 실효 평가.

## 관련 페이지
- [[herdr]] — 같은 날 병렬 에이전트 (CLI 축 경쟁)
- [[codex-plugin-cc]] — 벤더 간 에이전트 브리지 (하부)
- [[CodexBar]] — 멀티벤더 사용량 관제
- [[anthropic-claude-code]] · [[OpenAI]] — 오케스트레이션 대상 에이전트
- [[ai-news]]

## 원본
- 출처: https://github.com/stablyai/orca
- GitHub: ⭐14,538 (2026-07-09), MIT, TypeScript 96.7%
- 기능: 격리 worktree 병렬 / 모바일 앱(iOS·Android) / GitHub·Linear 연동 / SSH worktree / WebGL 터미널
- 신뢰도: ⭐⭐⭐ (라이브 스타·README WebFetch 실측)
