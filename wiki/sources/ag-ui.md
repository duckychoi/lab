---
title: "ag-ui-protocol/ag-ui — 에이전트↔프런트엔드 이벤트 프로토콜 (AG-UI)"
type: source
domain: ai-news
tags: [ai-news, github-trending, protocol, agent-ui, copilotkit, mcp]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/ag-ui-protocol/ag-ui]
reliability: high
---

**레포**: [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) · ★**18,230**(볼트 11-16 실측 · 수집기 ★17,489) · fork 1,881 · TypeScript · MIT · repo id 979392131 · 생성 2025-05-07. 볼트 첫 수록(그간 [[CopilotKit]] · [[CopilotKit-OpenBot]] 본문에 이름만 등장).

## 핵심 인사이트
> [!insight] MCP · A2A 다음의 세 번째 축 — "에이전트를 사용자 화면으로"
> README 의 자기 위치: MCP = 에이전트에 도구, A2A = 에이전트 간, **AG-UI = 에이전트 ↔ 사용자 UI**. 실행 중 백엔드가 *"~16 standard event types"*(46행)와 호환되는 이벤트를 내보내고, 전송은 SSE · WebSocket · 웹훅 무관. 스트리밍 채팅 · 양방향 상태 동기화 · 생성형 UI · 프런트엔드 도구 호출 · human-in-the-loop 를 한 스키마로 묶는다.

> [!warning] "표준"의 주도권과 빈칸
> - README 의 `docs.copilotkit.ai` 링크 **15건**(볼트 grep) — 표준을 표방하지만 문서 동선은 [[CopilotKit]] 으로 이어진다.
> - 지원 표에서 **OpenAI Agents SDK(126행) · AWS Bedrock Agents(115행) = "🛠️ In Progress"**. LangGraph · CrewAI · Microsoft Agent Framework · Google ADK · Mastra · Pydantic AI 등은 ✅. 가장 큰 상용 SDK 하나가 아직 빈칸이다.
> - 비-TS SDK(Kotlin · Go · Dart · Java · Rust · Ruby · C++ · .NET)는 모두 커뮤니티 표기(수집기 판독).

## 도메인별 추출 (ai-news)
- **신뢰도**: ★18,230 · 1.5년 차 · 다수 프레임워크 공식 통합 · 수록 사유는 누적(당일 +9).
- **즉시 활용**: YES(조건부) — 에이전트 UI 를 직접 만들 때 이벤트 스키마를 새로 설계하지 않아도 된다. 볼트 작업(CLI 위주)에는 당장 필요 없음.
- **6개월 영향력**: 에이전트 프레임워크 선택이 "AG-UI 를 내보내느냐"로 프런트 교체 비용을 좌우하게 된다. [[CopilotKit-OpenBot]] 이 외부 에이전트를 붙이는 경로가 바로 이것.
- **대체 관계**: 프레임워크별 자체 스트리밍 포맷(LangGraph stream events 등)을 상위에서 통일.
- **허와 실**: 프로토콜 자체는 MIT 로 열려 있고, 그 위의 상용 계층(CopilotKit Intelligence)은 별도 — [[파생표기-함정]] 과 같은 구조.
- **액션**: star 정도. 에이전트 웹 UI 를 만들 일이 생기면 첫 검토 대상.

## 관련 페이지
- [[CopilotKit]] · [[CopilotKit-OpenBot]] · [[AI-에이전트-프레임워크]] · [[에이전트-웹접근]] · [[파생표기-함정]] · [[OpenAI]] · [[Google]] · [[Microsoft]]

## 원본
- 출처: https://github.com/ag-ui-protocol/ag-ui
- 확인 범위: GitHub API 메타 · README 46 · 115 · 126행 · copilotkit 링크 계수(볼트) · 🔴 SDK 언어 목록 · 기능 목록은 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (★18,230 · 다수 공식 통합)
