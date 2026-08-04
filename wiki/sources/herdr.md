---
title: herdr — 터미널 에이전트 멀티플렉서
type: source
domain: ai-news
tags: [ai-news, github-trending, agent, terminal, multiplexer, rust]
created: 2026-07-09
updated: 2026-07-09
sources: []
reliability: high
---

# ogulcancelik/herdr (GitHub ⭐14,553)

**GitHub**: https://github.com/ogulcancelik/herdr
**스타수**: 14,553 (2026-07-09 기준) · **최신 릴리스**: v0.7.3 (2026-07-07)
**라이선스**: AGPLv3+ / 상용 듀얼 · **스택**: Rust 85.1%

> [!insight] 핵심 인사이트
> **"에이전트를 위한 tmux"** — 여러 코딩 에이전트를 한 터미널에서 동시에 띄우고 전환·관제하는 멀티플렉서. WebFetch 실측 핵심: ①**detach 후에도 에이전트가 계속 실행**되고 어느 터미널에서든 재attach, ②에이전트가 **pane을 spawn하고 소켓 API로 상호 협조**, ③**플러그인 마켓플레이스**, ④**Electron 없는 단일 Rust 바이너리**. [[stablyai/orca|orca]]가 데스크톱 GUI/모바일 앱으로 병렬 에이전트를 다룬다면, herdr는 **터미널 네이티브·경량·소켓 오케스트레이션**으로 같은 문제를 푼다. "병렬 에이전트 플릿 관리"가 2026년 여름 트렌딩의 뚜렷한 축임을 [[orca]]와 나란히 증명.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (⭐14,553, README·릴리스 WebFetch 실측 — v0.7.3/2026-07-07·1,071 커밋 확인, AGPL/상용 듀얼)
- **즉시 활용**: 후보 — 여러 에이전트를 백그라운드로 계속 돌리며 관제하는 워크플로에 유용. 단 AGPL 라이선스라 상용 임베드 시 주의.
- **6개월 영향력**: 단일 에이전트 세션 → **병렬 에이전트 플릿**으로 사용 패턴 이동. 터미널 사용자에게 tmux 대체가 아니라 "에이전트 오케스트레이터"가 새 카테고리.
- **대체 관계**: tmux/zellij의 에이전트 특화판. [[orca]](GUI ADE)와 UX 축에서 경쟁하되 CLI 우선 사용자층 겨냥.
- **허와 실**: 소켓 협조·마켓플레이스는 매력적이나 실사용 안정성·플러그인 생태계 성숙도는 검증 필요. "no Electron"은 성능 셀링포인트.
- **액션**: herdr로 [[orca]]와 동일 태스크(에이전트 2개 병렬 worktree)를 돌려 관제 UX·리소스 점유 비교.

## 관련 페이지
- [[orca]] — 같은 날 병렬 에이전트 ADE (GUI 축 경쟁)
- [[CodexBar]] — 멀티벤더 에이전트 사용량 관제층
- [[herdr]] 관련 흐름: [[claude-skills]]·[[awesome-claude-code]] 에이전트 도구 생태계
- [[ai-news]]

## 원본
- 출처: https://github.com/ogulcancelik/herdr
- GitHub: ⭐14,553 (2026-07-09), v0.7.3 (2026-07-07), 1,071 커밋
- 스택: Rust 85.1% / 단일 바이너리 / 소켓 API / 플러그인 마켓플레이스 / AGPLv3+·상용 듀얼
- 신뢰도: ⭐⭐⭐ (라이브 스타·README·릴리스 WebFetch 실측)
