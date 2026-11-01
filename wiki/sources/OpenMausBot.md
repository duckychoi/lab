---
title: "OpenMausBot — 로컬 CLI 에이전트를 채팅 연락처로 묶는 데스크톱 앱"
type: source
domain: ai-news
tags: [ai-news, agent, desktop-app, orchestration]
created: 2026-11-01
updated: 2026-11-01
sources: [https://github.com/milind-soni/OpenMausBot]
reliability: medium
---

**GitHub**: https://github.com/milind-soni/OpenMausBot · ★**9,989** · fork 1,385 · Apache-2.0 · 생성 2026-08-11 · 푸시 2026-11-01T09:08Z (GitHub API 2026-11-01)

## 핵심 인사이트
> [!insight] 새 에이전트가 아니라 기존 구독을 묶는 껍데기다
> 봇마다 로컬 `claude`·`codex`·`grok` CLI, 모델, 컴퓨터, 연결 앱을 따로 둔다. 기존 로그인을 그대로 쓰고 중간 프록시가 없다고 밝힌다. 구독료를 새로 내지 않고 Grok Bot 같은 형태를 흉내 내는 것이 판매 논리다.

> [!warning] 권한 범위와 요약 정정
> - 수집기 "Claude 또는 Codex"는 좁다. README는 **Grok CLI와 임의 CLI 바이너리**까지 적는다.
> - 봇에 **자기 컴퓨터 제어**를 줄 수 있고(macOS · Ubuntu Xorg 옵트인, Wayland는 #345로 비활성), Composio 앱 500개 이상이 붙는다. 승인 카드가 있어도 권한 면적은 넓다.
> - `boat.dev`는 README의 sponsors 자산 경로로 보아 후원사로 보인다. 클라우드 컴퓨터와의 관계는 볼트도 확인하지 못했다(추정).
> - 측정 수치는 README에 없다. 생성 약 3개월로 이력이 짧다.

## 도메인별 추출
- **즉시 활용**: 보류. [[Claude-Code-워크플로우]]를 이미 터미널로 쓰고 있어 얻는 것은 UI다.
- **대체 관계**: [[t3code]] · [[thinkrail]] · [[Orkas]]와 같은 "에이전트 GUI" 축이다.
- **액션**: 지금은 없음. 텔레그램으로 이미 같은 형태를 쓰고 있다면 우선순위가 낮다.

## 관련 페이지
- [[Orkas]] · [[t3code]] · [[Claude-Code-워크플로우]] · [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/milind-soni/OpenMausBot
- 확인 범위: GitHub API · README · 🔴 앱 미실행
- 신뢰도: ⭐⭐ (★9,989 · 이력 짧음 · 수치 없음)
