---
title: n8n — Self-hosted AI 워크플로우 자동화 플랫폼 (⭐190,304)
type: source
domain: ai-news
tags: [ai-news, github-trending, workflow-automation, self-hosted, LLM-pipeline, n8n, no-code, agentic]
created: 2026-05-30
updated: 2026-06-04
sources: []
reliability: high
---

# n8n — Self-hosted AI 워크플로우 자동화 플랫폼

## 핵심 인사이트

> [!insight] 핵심 인사이트
> ⭐190,304 (+159/day). 400+ 서비스 연동 + 네이티브 AI 노드로 LLM 파이프라인을 노코드로 오케스트레이션. Zapier 대비 self-hosted + 코드 커스터마이징 가능. GitHub에서 가장 많이 스타받은 워크플로우 자동화 도구.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — GitHub ⭐190,304, 성숙한 오픈소스 프로젝트, 활발한 커뮤니티
- **즉시 활용**: YES — Docker 한 줄로 배포, 비주얼 에디터로 LLM 파이프라인 구성 가능
- **6개월 영향력**: AI 에이전트 워크플로우의 "접착제" 레이어로 자리잡을 가능성 높음. 코드 작성 없이 LLM 호출 → 데이터 처리 → 알림 파이프라인 구성
- **대체 관계**: Zapier/Make 대체 (self-hosted), LangChain/LlamaIndex의 UI 레이어 역할 가능
- **허와 실**: 복잡한 로직은 여전히 코드 필요. 엔터프라이즈 기능은 유료. 하지만 오픈소스 코어는 충분히 강력
- **액션**: Docker로 로컬 설치 후 Claude/OpenAI API 연동 LLM 워크플로우 실험

> [!action] 당장 할 것
> `docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n` 로 즉시 설치. AI 노드(OpenAI, Anthropic) + HTTP Request + Webhook 조합으로 자동화 파이프라인 테스트.

## 주요 기능

- **네이티브 AI 노드**: OpenAI, Anthropic, Ollama 등 LLM 직접 연동
- **400+ 통합**: Slack, Google, GitHub, DB, HTTP 등 포괄적 커버리지
- **에이전트 오케스트레이션**: AI 에이전트 체인 구성, 루프·조건 분기 지원
- **Self-hosted**: 데이터가 서버 외부로 나가지 않음 → 기업 보안 요건 충족
- **JavaScript 커스터마이징**: 내장 코드 노드로 복잡한 로직 처리 가능
- **n8n-mcp**: MCP 서버 통합 지원으로 Claude Code와 직접 연결 가능 ([[n8n-mcp]] 참조)

## 관련 페이지

- [[n8n-mcp]] — n8n MCP 서버 통합 (Claude Code 연동)
- [[AI-에이전트-프레임워크]] — 에이전트 오케스트레이션 도구 비교
- [[에이전트-메모리-레이어]] — n8n + 메모리 레이어 조합 패턴
- [[Claude-Code-워크플로우]] — n8n을 Claude Code 자동화에 활용

## 원본

- 출처: https://github.com/n8n-io/n8n
- 스타: ⭐190,304 (+159, 2026-05-30 기준)
- 신뢰도: ⭐⭐⭐⭐⭐
