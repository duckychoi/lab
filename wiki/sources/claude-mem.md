---
title: thedotmack/claude-mem — Claude Code 세션 간 컨텍스트 지속 플러그인
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, memory, context, session, plugin, llm-coding, workflow]
created: 2026-04-13
updated: 2026-04-17
sources: []
reliability: high
---

# thedotmack/claude-mem

> [!insight] 핵심 인사이트
> Claude Code 세션 종료 시 컨텍스트를 AI로 압축·저장하고, 다음 세션 시작 시 주입하는 플러그인. 스타 **60,473개(+1,897 today)**. "세션 간 기억 단절"이 Claude Code 실무 최대 불만 중 하나 — 이를 해결하는 도구가 이 정도 스타를 받는다는 건 **메모리 연속성**이 LLM 코딩의 핵심 UX 문제임을 입증.

## 핵심 인사이트

> [!action] 당장 할 것
> claude-mem 설치 후 실제 개발 세션에서 컨텍스트 연속성 확인. 특히 장기 프로젝트(wiki 시스템 등)에 유용할 수 있음.

> [!note] 배경 정보
> thedotmack 개발. AI 압축을 활용해 중요한 컨텍스트(파일 구조, 진행 상황, 결정 사항)를 요약 → 다음 세션 CLAUDE.md나 시스템 프롬프트에 자동 주입하는 방식으로 추정.

> [!question] 미해결 질문
> 압축 방식은? 어떤 AI를 압축에 사용? 주입 포인트가 CLAUDE.md인가 시스템 프롬프트인가?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — 스타 60,473개, 커뮤니티 대규모 검증
- **즉시 활용**: YES — Claude Code 설치 후 즉시 사용 가능 (플러그인 형태)
- **6개월 영향력**: 세션 간 기억이 해결되면 Claude Code로 수주/수개월 프로젝트 연속 진행 가능
- **대체 관계**: 수동 CLAUDE.md 관리 대체, 메모리 관련 CLAUDE.md 섹션 자동화
- **허와 실**: 압축 품질에 의존 — 중요 컨텍스트가 누락될 수 있음
- **액션**: 설치 후 wiki 작업 세션에 테스트

## 관련 페이지
- [[Claude-Code-워크플로우]]
- [[claude-code-best-practice]]
- [[andrej-karpathy-skills]]
- [[LLM-Wiki]]

## 원본
- 출처: https://github.com/thedotmack/claude-mem
- 신뢰도: ⭐⭐⭐ (스타 60,473)
