---
title: "claude-howto — Claude Code 10모듈 학습 가이드. 코드가 아니라 문서이고, 볼트가 이미 쓰는 것을 정리한 교재"
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, tutorial, hooks, subagent, mcp, 에이전트-스킬, 문서형-레포]
created: 2026-10-25
updated: 2026-10-25
sources: []
reliability: medium
---

# claude-howto

**GitHub**: https://github.com/luongnv89/claude-howto
**실측(2026-10-25 KST · `api.github.com`)**: ★ **44,800**(수집기 44,795 · +5 드리프트) · MIT · `language: Python` · created **2025-11-07** · pushed 2026-10-20 · README 30,643 B
**신뢰도**: ⭐⭐⭐ (스타 4.4만 · 문서형이라 "성능" 주장 자체가 없음)

> [!insight] 핵심 인사이트 — **스타 4.4만짜리 레포의 산출물은 코드가 아니라 템플릿이다**
> 10개 모듈(슬래시 커맨드·훅·메모리·서브에이전트·MCP·플러그인)과 복붙용 `CLAUDE.md`·훅·서브에이전트 템플릿. ⇒ 🎯 **[[Claude-Code-워크플로우]] 수요가 "도구"에서 "사용법"으로 이동했다는 신호**로 읽는다 — 같은 주 트렌딩의 [[security-audit-skill]](커밋 0 · ★5배)처럼 **텍스트 자산이 코드 자산보다 빨리 별을 모은다.**
> ⚖️ `language: Python` 표기는 보조 스크립트 때문이며 레포 성격은 문서다(GitHub 언어 통계 ≠ 레포 성격).

## 도메인별 추출 (ai-news)
- **신뢰도**: ★44,800 · 논문 없음 · 문서형이라 검증할 수치 주장 0건
- **즉시 활용**: **YES(부분)** — 볼트 자체가 Claude Code 스킬·훅·CLAUDE.md 로 운영된다. 훅 템플릿은 볼트 크론 자동화(인제스트 누락 감지 등)에 바로 참고 가능
- **6개월 영향력**: 낮음~중간 — 새 능력이 아니라 기존 기능의 정리
- **대체 관계**: 공식 문서의 보조 교재. [[에이전트-스킬]] 계열 레포들과 경쟁
- **허와 실**: 마케팅 주장 없음. 단 **Claude Code 기능이 바뀌면 가장 먼저 낡는 유형**이다 → [[간판-지체]] 위험
- **액션**: 훅 모듈 1개만 열어 볼트의 "7일 미처리"(10-24 기록) 재발 방지 훅 아이디어로 쓴다

> [!question] 미해결
> 모듈이 다루는 Claude Code 버전 범위 명시 여부 — README 에서 확인 못 함(열람 범위: README 전문).

## 관련 페이지
- [[Claude-Code-워크플로우]] · [[에이전트-스킬]] · [[하네스-설계-축]]
- 같은 배치: [[cindy]](하네스 멀티플렉서) · [[gemini-cli]](경쟁 CLI)
- [[ai-news]]

## 원본
- 출처: https://github.com/luongnv89/claude-howto
- 신뢰도: ⭐⭐⭐ (GitHub 스타 44,800)
