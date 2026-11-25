---
title: "cc-switch-cli — 7종 AI CLI의 프로바이더 · MCP · 세션 전환 TUI"
type: source
domain: ai-news
tags: [ai-news, github, cli, tui, provider-switching, mcp, rust, sponsor-warning]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/SaladDay/cc-switch-cli]
reliability: medium
---

**레포**: SaladDay/cc-switch-cli · ★ **5,578**(수집기 11-25 = 볼트 API 일치) · Rust 일간 Trending(당일 +7) · MIT · 레포 ID 1102384337 · 생성 2025-11-23 · push 2026-11-25 · 최신 v5.11.4(2026-11-17)

## 핵심 인사이트
> [!insight] "전역 설정을 바꾸지 않고 해당 세션만" 다른 프로바이더로 — 설정 충돌 없는 세션 단위 스위칭
> 데스크톱 앱 farion1231/cc-switch의 **CLI 포크**(WebDAV 동기화 호환). 대상 앱 claude · codex · gemini · opencode · hermes · openclaw · pi. 기능: API 프로바이더 목록 · 전환 · 스트림 상태 점검, `cc-switch start claude <provider>`로 **전역 설정을 바꾸지 않고 해당 세션만** 다른 프로바이더로 실행, ChatGPT/Codex OAuth 계정 관리, 세션 목록 · 토큰/비용 사용량 가져오기, MCP 서버 일괄 동기화, 로컬 프록시 라우팅. 설치는 `curl | bash`(Linux는 정적 musl 빌드). 11-23 수집 때 "설정 전환 유틸"로 제외했던 레포 — 미보유 AI 후보 고갈로 11-25 포함.

> [!warning] README 상단 스폰서 8곳이 API 중계(relay) · 주거용 프록시 업체 광고
> 비공식 중계 사용은 각 AI 서비스 약관 확인 필요. 벤치 · 수치 없음(유틸리티).

## 도메인별 추출 (ai-news)
- **즉시 활용**: 여러 코딩 에이전트 CLI를 오가며 키 · MCP 설정을 손으로 맞추는 사람에겐 시간 절약 — 볼트 운영자처럼 claude · codex · gemini를 병행하는 환경에 정확히 겨냥됨. 단 볼트는 단일 CLI 축이라 당장 불필요.
- **대체 관계**: [[cli-agent-orchestrator]](다중 에이전트 오케스트레이션)와 인접 — 오케스트레이터는 "동시 실행", cc-switch는 "환경 전환".
- **액션**: 없음(관찰 — 필요 시 설치 1커맨드).

## 관련 페이지
- [[cli-agent-orchestrator]] · [[ai-news]]

## 원본
- 출처: https://github.com/SaladDay/cc-switch-cli
- 확인 범위: README(수집기 11-25) · GitHub API 재확인(볼트 11-25 — ★ · 라이선스 · 레포 ID · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐ (★5.5천 · 기능은 README 기준 · 스폰서 구성은 이용자 판단 필요)
