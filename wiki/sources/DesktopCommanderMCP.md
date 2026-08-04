---
title: DesktopCommanderMCP — Claude에 터미널·파일시스템·프로세스 제어를 주는 MCP 서버
type: source
domain: ai-news
tags: [ai-news, mcp, claude-code, terminal, filesystem, agent-coding, local-llm]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: high
---

# wonderwhy-er/DesktopCommanderMCP

> [!insight] 핵심 인사이트
> Claude Desktop에 **터미널 실행·파일시스템 검색·diff 기반 파일 편집·프로세스 관리**를 통째로 붙이는 MCP 서버. ⭐7,572 (당일 **+328**, 급상승). 별도 API 토큰 없이 **호스트 클라이언트 구독을 그대로 사용**(vLLM/API 과금 없음)하는 점이 핵심 — "Claude Desktop을 IDE·터미널 에이전트로 승격"시킨다. Python/Node/R **인메모리 코드 실행**과 Excel/PDF/DOCX 네이티브 처리까지 포함.

**GitHub**: https://github.com/wonderwhy-er/DesktopCommanderMCP  
**스타**: ⭐7,572 (당일 +328)  
**신뢰도**: ⭐⭐⭐ (7.6K 스타·MIT, 급상승 중)

## 도메인별 추출

- **신뢰도**: MIT 라이선스·955 forks·활성 Discord. 당일 +328 급상승 = 데스크톱 에이전트 수요 실증
- **즉시 활용**: YES — Claude Desktop/Cursor/VS Code에서 **로컬 파일·터미널을 바로 조작**. npx·bash·Smithery·Docker(샌드박스) 다중 설치. surgical text replace + full rewrite 지원으로 코드 패칭에 유용
- **6개월 영향력**: [[Claude-Code-워크플로우]]를 데스크톱 GUI로 확장. "IDE 없이 Claude Desktop만으로 개발"이 현실화되면 [[anthropic-claude-code]] CLI와 GUI가 상보
- **대체 관계**: 파일시스템 MCP 서버 사양을 확장 — 기본 filesystem-mcp 상위 호환. [[DesktopCommanderMCP]] = 터미널+프로세스+코드실행까지 묶은 풀 세트
- **허와 실**: 터미널 무제한 실행은 강력하지만 **보안 리스크** — symlink traversal 방지·command blocklist를 제공하나, 임의 명령 실행 권한은 신중히. 스케줄/무인 실행엔 command blocklist 필수
- **액션**: Docker 격리 모드로 설치 후 위키 자동수집(파일 정리·crawl 결과 파싱)에 붙이는 실험

> [!action] 당장 할 것
> Docker 샌드박스 모드로 DesktopCommanderMCP를 설치하고, command blocklist를 건 상태에서 로컬 파일 정리·diff 편집 워크플로우를 검증한다.

> [!warning] 신뢰도·보안
> 터미널·프로세스 무제한 접근은 프롬프트 인젝션 시 위험. 무인 스케줄 실행에는 blocklist·격리 컨테이너 필수, 신뢰 소스만.

## 관련 페이지
- [[Claude-Code-워크플로우]]
- [[anthropic-claude-code]]
- [[claude-code-templates]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/wonderwhy-er/DesktopCommanderMCP
- 신뢰도: ⭐⭐⭐ (7.6K 스타·MIT)
