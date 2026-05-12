---
title: context-mode — AI 코딩 에이전트 컨텍스트 윈도우 최적화
type: source
domain: ai-news
tags: [ai-news, context-window, token, optimization, coding-agent, sandbox]
created: 2026-05-07
updated: 2026-05-07
sources: []
reliability: high
---

# mksglu/context-mode

> [!insight] 핵심 인사이트
> 툴 출력을 샌드박스 처리하여 컨텍스트 윈도우 토큰을 98% 절감. Claude Code · Cursor · Gemini CLI 등 14개 플랫폼 지원. 에이전트 비용의 핵심 병목인 "툴 출력 토큰 팽창"을 직접 해결.

**GitHub**: https://github.com/mksglu/context-mode  
**스타**: ⭐13,388 (2026-05-06 기준)  
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출

- **신뢰도**: 13K 스타 — 빠른 성장, 검증 중. 98% 절감 클레임은 실측 필요
- **즉시 활용**: YES — Claude Code 사용 시 장기 대화에서 컨텍스트 초과로 인한 오류·비용 급증 문제 직접 해결
- **6개월 영향력**: 에이전트 컨텍스트 관리가 표준 미들웨어로 자리잡으면 장시간 코딩 세션 가능. [[claude-mem]] · [[beads]]와 유사 문제 다른 접근
- **대체 관계**: [[claude-mem]](세션 간 기억), [[beads]](메모리 레이어) 대비 실시간 토큰 압축에 집중
- **허와 실**: 98% 절감은 최적 케이스. 실제 코딩 작업 중 툴 출력 특성에 따라 달라짐. 샌드박스 방식이 일부 정보 누락 가능성
- **액션**: Claude Code 세션에 설치 후 실제 토큰 절감률 측정

> [!action] 당장 할 것
> context-mode 설치 → Claude Code 장시간 작업 세션에서 토큰 사용량 before/after 비교.

> [!warning] 주의
> 98% 절감 클레임은 검증 필요. 툴 출력 샌드박스가 에이전트 판단에 필요한 정보를 가리는 경우 없는지 확인.

## 관련 페이지
- [[Claude-Code-워크플로우]]
- [[claude-mem]]
- [[beads]]
- [[에이전트-메모리-레이어]]
- [[Terminal-Agent-Context-Compression]]

## 원본
- 출처: https://github.com/mksglu/context-mode
- 신뢰도: ⭐⭐⭐⭐ (13K 스타, 클레임 검증 필요)
