---
title: "edgeever — Cloudflare 무료 구간에서 돌리는 셀프호스팅 노트 앱(AI 사이드바 · MCP · ACP 내장)"
type: source
domain: ai-news
tags: [ai-news, github, self-hosted, notes-app, mcp, acp, cloudflare, byok]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/tianma-if/edgeever]
reliability: medium
---

**레포**: tianma-if/edgeever · ★ **3,531**(수집기 11-24) → **3,551**(볼트 API 11-25) · TypeScript 일간 Trending(당일 +27) · AGPL-3.0 · 생성 2026-06-26 · push 2026-11-25

## 핵심 인사이트
> [!insight] "AI 에이전트에 붙여넣을 배포 프롬프트"를 설치 방법 1순위로 제시하는 노트 앱
> Evernote식 3단(트리 · 목록 · 편집기) 노트 앱을 [[Cloudflare]] Workers + D1 + R2(또는 Docker)로 셀프호스팅. 웹 · 데스크톱 3종 · 모바일 2종 클라이언트와 웹 클리퍼(20+ 플랫폼 전용 파서) 제공. 배포 문서가 사람용 설치 가이드보다 **에이전트용 프롬프트를 먼저** 주는 문서 순서는 "설치를 에이전트가 하게 만드는" 시대의 흐름을 보여준다.

> [!note] AI 기능 4종(README 기능표 기준)
> ① 사이드바 AI(요약 · 교정 · 번역 · 이어쓰기 — OpenAI · Anthropic · Gemini · 커스텀 BYOK) ② 노트북 단위 읽기/쓰기 권한이 있는 **Remote MCP 서버 내장** ③ 데스크톱 ACP로 Codex · Claude Code 같은 로컬 에이전트 구동 ④ OpenAI 호환 음성 모델 오디오 · 영상 전사. 그 밖에 "프롬프트로 데이터베이스 생성".

## 도메인별 추출 (ai-news)
- **실용성**: AI는 부가 기능이고 본체는 노트 앱. 성능 · 동기화 지연 수치 없음.
- **대체 관계**: 볼트(Obsidian)를 MCP로 에이전트에 노출하는 현재 구성의 **대안 후보** 정도 — 갈아탈 이유는 현재 없음.
- **액션**: 없음(관찰).

## 관련 페이지
- [[Cloudflare]] · [[ai-news]]

## 원본
- 출처: https://github.com/tianma-if/edgeever
- 확인 범위: README(수집기 11-24) · GitHub API 재확인(볼트 11-25 — ★ · 언어 · 라이선스 · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐⭐ (★3.5천 · 신규 레포라 장기 유지보수 여부 미확인)
