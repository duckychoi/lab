---
title: "awslabs/cli-agent-orchestrator — 여러 코딩 CLI를 tmux 세션으로 묶는 감독자-작업자 오케스트레이터(CAO)"
type: source
domain: ai-news
tags: [ai-news, github, agent-orchestration, tmux, multi-agent, aws, mcp]
created: 2026-11-24
updated: 2026-11-24
sources: [https://github.com/awslabs/cli-agent-orchestrator]
reliability: medium
---

**GitHub**: ★1,660(볼트 API 11-24 · 수집기 11-23 1,638) · 당일 +12(Python Trending) · Python · Apache-2.0 · 생성 2025-07-29 · HEAD `2f7c19dc50`(수집기 11-23) · open issues 203(수집기 187 — PR 포함 합산 기준 차이 가능)

## 핵심 인사이트
> [!insight] 래퍼가 아니라 완전한 프로세스 — 각 CLI의 자체 인증 · 기능을 그대로 쓴다
> 로컬 `cao-server` 가 13종 제공사 CLI(Kiro 기본 · Claude Code · Codex · Antigravity · Hermes · Kimi · Qwen Code · MiniMax Code · Copilot · OpenCode · OMP · Cursor · Grok Build)를 **격리된 tmux 세션**에서 띄우고, 감독자 에이전트가 작업자에게 병렬/순차 위임. 웹 UI(`localhost:9889`) · 운영용 MCP 서버 · 스케줄 flows · 스킬 · 세션 간 메모리 · 옵트인 자기학습 루프 · 도구 제한(역할 allowlist) · EKS 배포 예시 · 원격 EC2 운용 문서. 요구: Python 3.11+ · tmux 3.3+ · uv · 인증된 CLI 1개 이상.

> [!warning] 성능 수치 0 · 통과 기준이 별
> README 에 성능 · 성공률 수치는 없다. ★1,660 은 기준선(1,000)을 겨우 넘는 수준이고 당일 증분도 +12 — 급상승이 아니라 **AWS 공식 조직(awslabs)이라는 신뢰도로 통과**한 선발(수집기 스스로 밝힘, [[스타-근거-비동행]] 방향).

## 도메인별 추출 (ai-news)
- **실용성**: Claude Code + Codex 를 한 감독자 아래 병렬로 돌리는 구성을 리눅스에서 바로 시험 가능. tmux 기반이라 서버 운용 · 크론 작업과 궁합이 좋다 — 볼트의 [[Claude-Code-워크플로우]] 와 직접 겹친다.
- **설계 포인트**: 에이전트를 API 래퍼로 감싸지 않고 **완전한 프로세스로 남긴다** — CLI 업데이트를 따라가는 유지비용을 프로세스 경계로 격리. [[LoopForge]](코딩 에이전트 CLI 10종 위에 역할 · SOP · human gate)와 같은 "기존 CLI 위에 얹는다" 축의 2번째 표본.
- **허와 실**: 오케스트레이션 효과의 정량 근거 0. 감독자 에이전트의 위임 품질이 사실상 전부.
- **액션**: 설치 시험 후보(actionable 등재).

## 관련 페이지
- [[LoopForge]] · [[Claude-Code-워크플로우]] · [[에이전트-스킬]] · [[mini-swe-agent]] · [[ai-news]]

## 원본
- 출처: https://github.com/awslabs/cli-agent-orchestrator
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 · 생성일 — 볼트 11-24) · README 내용은 수집기 11-23 판독 · 실행 0
- 신뢰도: ⭐⭐⭐
