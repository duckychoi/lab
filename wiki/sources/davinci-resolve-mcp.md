---
title: "davinci-resolve-mcp — AI 어시스턴트가 DaVinci Resolve를 Scripting API로 조작하는 MCP 서버"
type: source
domain: video-saas
tags: [video-saas, ai-news, mcp, davinci-resolve, 편집자동화, claude-code, tool]
created: 2026-11-28
updated: 2026-11-28
sources: [https://github.com/samuelgursky/davinci-resolve-mcp]
reliability: medium
---

**레포**: https://github.com/samuelgursky/davinci-resolve-mcp · ★ **4,466**(수집기 11-28 = 볼트 GitHub API 일치) · Python · **MIT** · 생성 2025-03-18 · 최근 push 2026-11-28(금일 — 활성) · 트리거: 11-27 v5.7.0 · v5.7.1 연속 릴리스

## 핵심 인사이트
> [!insight] DCC(영상 제작 도구)를 에이전트의 손에 넣는 길이 MCP로 표준화되기 시작했다
> 공식 Scripting API를 MCP로 노출해 편집·미디어풀·렌더 설정·그레이딩·Fusion·Fairlight를 **API 100% 커버**(기본 37툴, 전체 390툴)하고, `npx davinci-resolve-mcp setup` 으로 Claude Code·Cursor·Codex CLI 설정을 자동화한다. [[carla]] actionable(Unreal MCP + Skills)과 같은 축 — **"전문 제작 소프트웨어 = 에이전트 작업 환경"** 패턴이 영상 편집 쪽에서도 성숙 단계(★4천+, 2년 레포)에 도달.

> [!warning] 채택 문턱이 버전과 에디션에 갈린다 — 무료판은 사실상 불가
> **Resolve 21.1부터 Python 스크립팅이 Studio 전용**으로 바뀌어(README 자인) **무료판은 21.0.x의 인앱 브리지 우회로만 동작하며 그 경로는 미확인 상태**다. "라이브 테스트 통과율 93.6%"도 README 배지 **자기신고**다. 즉 이 도구의 실용성은 *Studio 소유자*에게만 즉시 유효 — [[자기제한-명시]] 적용(제한을 스스로 명시)이지만 수치 검증은 미실시.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 편집·렌더·그레이딩·오디오(Fairlight)·합성(Fusion) 전 영역이 API 뒤에 있다는 것 자체가 의미 — 내 SaaS 워크플로우 설계에서 "NLE를 프로그래밍 인터페이스로 조작"하는 전제가 현실로 존재함.
- **크리에이터 인사이트**: 반복 편집(파일 정리 · 타임라인 조립 · 렌더 대기열)이 에이전트 자동화의 1순위 과제 — 크리에이터가 원하는 건 "편집을 대신"이 아니라 "기계적 반복을 대신".
- **워크플로우**: setup CLI가 에이전트별 설정 파일을 자동 생성 — 도구 채택 마찰을 설치 단계에서 제거하는 패턴([[Claude-Code-워크플로우]] 참고).
- **경쟁 우위 빈틈**: Studio 전용 의존이 역설적으로 기회 — 무료판 사용자의 자동화 수요는 이 도구로 충족 불가.
- **액션**: 없음(관찰 — Studio 환경 확보 시 [[carla]]와 함께 MCP-에이전트 실검 후보).

## 관련 페이지
- [[carla]] · [[Claude-Code-워크플로우]] · [[Coda-DaVinci]] · [[자기제한-명시]] · [[video-saas]]

## 원본
- 출처: https://github.com/samuelgursky/davinci-resolve-mcp
- 확인 범위: GitHub API(볼트 11-28 — ★4,466 · MIT · 생성·push 일치) · README 내용(수집기 11-28 판독 인용 — 툴 수 · 통과율 · 버전 제한 원문 재열람 미실시) · 실행 0
- 신뢰도: ⭐⭐⭐ (지표 실측 · 기능 커버·통과율·무료판 제한은 자기신고)
