---
title: "ParadevAI/Paradev (구 Superset) — 작업별 git worktree 에 CLI 코딩 에이전트를 병렬로 띄우는 데스크톱 앱. 이슈 1,231개 · Windows 미지원"
type: source
domain: ai-news
tags: [ai-news, github-trending, coding-agent, git-worktree, parallel-agents, desktop-app, claude-code, codex, mit]
created: 2026-11-08
updated: 2026-11-08
sources: [https://github.com/ParadevAI/Paradev]
reliability: medium
---

**GitHub**: [ParadevAI/Paradev](https://github.com/ParadevAI/Paradev) · ★**16,090**(볼트 11-08 API · 수집기 16,052) · 포크 1,438 · 🔴 **오픈 이슈 1,231**(★ 대비 7.7%) · MIT · TypeScript · created 2025-10-21 · pushed 11-08

## 핵심 인사이트
> [!insight] "에이전트 병렬화"의 실제 병목은 모델이 아니라 브랜치·터미널·리뷰 관리다
> [[anthropic-claude-code|Claude Code]]·Codex·[[opencode]]·Gemini CLI·Cursor Agent 를 작업마다 별도 **worktree·브랜치·터미널**에 띄우고, 앱 안에서 diff 리뷰 → 커밋 → PR(체크·리뷰 스레드·머지) → 워크스페이스별 dev 서버 프리뷰까지. 자체 에이전트가 아니며 모델 호출을 프록시하지 않는다(= 구독/키는 각자). 브라우저 Design 모드로 UI 요소를 찍어 수정 요청.

> [!warning] README 스스로 적은 한계
> *"worktree 는 파일만 분리할 뿐 프로세스 샌드박스·머지 충돌 방지가 아니다"* — 병렬 에이전트가 같은 포트·DB·전역 설정을 건드리면 여전히 충돌. macOS 중심, Linux 는 실험적 AppImage, **Windows not yet available**(볼트 grep 검출). 원격 호스트·모바일·스케줄 자동화는 Pro 유료. CLI 명령이 아직 `superset`(Apache Superset 과 무관).

## 도메인별 추출 (ai-news)
- **즉시 활용**: 조건부 YES — 맥에서 여러 에이전트 작업을 동시에 돌린다면. 우리 서버(Linux 헤드리스)에는 부적합 → 같은 아이디어를 `git worktree` + tmux 로 직접 구현하는 편이 낫다.
- **대체 관계**: 수동 worktree 관리 · [[agent-switch]] 류 에이전트 전환기와 겹침.
- **허와 실**: ★16K 지만 이슈 1,231 — 빠른 성장 대비 유지보수 적체 신호.
- **액션**: 관찰.

## 관련 페이지
- [[anthropic-claude-code|Claude Code]] · [[opencode]] · [[agent-switch]] · [[llm-multi-agent-survey|멀티에이전트]]
- 같은 배치: [[T3MP3ST]](같은 "기존 CLI 에이전트 재활용" 패턴)

## 원본
- 출처: https://github.com/ParadevAI/Paradev
- 확인 범위: GitHub API(볼트 11-08) · README raw grep(AppImage · Windows not yet available 검출) · 실행 0회
- 신뢰도: ⭐⭐⭐ (★16K · 단 이슈 적체)
