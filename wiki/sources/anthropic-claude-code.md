---
title: anthropics/claude-code — Anthropic 공식 터미널 AI 코딩 에이전트
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, anthropic, coding-agent, terminal, CLI, agentic-coding]
created: 2026-06-01
updated: 2026-08-23
sources: []
reliability: high
---

# anthropics/claude-code — 공식 터미널 AI 코딩 에이전트

> [!update] 2026-08-23 갱신 — ⭐142,680 (**API 실검증**·50일 만 재측정) + **성격 재규정: 소스가 아니라 배포·이슈 채널**
> GitHub ⭐**142,680** (2026-08-23 **GitHub API 실호출 검증**) ← 135,978(07-04). **약 50일 +6,702**(일 평균 +134)로, 이번 배치 GitHub 5건 중 **당일 증가폭 최저(+127)**다. 부가 실측(API): 포크 **22,849**·오픈이슈 **15,113**·언어 **Python**·**라이선스 미명시**·생성 2025-02-22·최종 푸시 **2026-08-23**(당일·활성).
> **이번 배치에서 [[openai-codex]]가 처음 편입되며 이 레포의 성격이 대비로 드러났다.** codex는 ⭐114,383으로 스타는 여기보다 적지만 **Apache-2.0·Rust로 에이전트 본체 소스를 공개**한다. 반면 이 레포는 **라이선스 미명시 + 오픈이슈 15,113건**으로, **구현체 저장소가 아니라 배포·이슈 트래킹 채널**에 가깝다. 즉 스타 142,680은 *"Claude Code 제품의 인지도"*를 반영하는 것이지 *"읽을 수 있는 코드베이스의 가치"*가 아니다 — **소스 학습 목적이라면 여기가 아니라 codex를 봐야 한다.**
> ⚠️**본문 하단 "에코시스템 현황"의 스타 수치는 07-04 시점 값으로 전부 낡았다** — 실제로 [[mattpocock-skills]]는 ⭐85K가 아니라 **232,854**(2.7배), [[superpowers]] **276,399**, [[ECC]] **242,304**로 **파생 생태계가 원천 레포(142,680)를 스타에서 크게 추월했다.** 07-04에 "이 레포가 생태계 중심축"이라 적었으나, 지금은 **중심축은 제품이되 GitHub 스타 중력은 스킬·하네스 레이어로 이동**한 상태가 정확한 서술이다.
> reliability high 유지(벤더 공식·당일 푸시 활성·수치 API 실검증).

> [!insight] 핵심 인사이트
> Anthropic 공식 Claude Code CLI — 코드베이스를 이해하고 자연어로 코딩·리팩토링·git 작업 수행. GitHub ⭐**135,978 (+221 당일, 2026-07-04)** ← 129,171(06-01), 약 한 달 +6.8K. [[everything-claude-code]](⭐199K), [[mattpocock-skills]](⭐85K) 등 파생 에코시스템의 원천. 이 레포 자체가 AI 에이전트 생태계 중심축 — 경쟁사 OpenAI마저 이 CLI용 브리지 [[codex-plugin-cc]]를 직접 배포할 만큼 사실상 허브로 굳음.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — Anthropic 공식, ⭐129K, 프로덕션 사용 대규모 검증
- **즉시 활용**: YES — npm install -g @anthropic-ai/claude-code
- **6개월 영향력**: AI 코딩 에이전트의 사실상 표준. 이 레포 중심으로 스킬·플러그인·메모리 레이어 생태계가 계속 성장
- **대체 관계**: Cursor, GitHub Copilot, Gemini CLI 경쟁. 코드베이스 전체 이해·복잡 작업 처리에서 우위. 이제 [[codex-plugin-cc]]로 OpenAI Codex를 서브에이전트/리뷰어로 흡수하는 멀티벤더 조합까지 가능
- **허와 실**: 토큰 비용 높음. 긴 세션에서 컨텍스트 관리 필요 ([[claude-mem]], [[context-mode]] 등 보조 도구 필요)
- **액션**: 현재 사용 중. [[Claude-Code-워크플로우]] 최적화 지속

> [!note] 에코시스템 현황
> 파생 프로젝트만 수십만 스타: [[everything-claude-code]](⭐199K), [[mattpocock-skills]](⭐85K), [[awesome-agent-skills]](⭐17K), [[claude-code-best-practice]](⭐39K), [[academic-research-skills]](⭐14K), [[tech-leads-agent-skills]](⭐4K)

## 관련 페이지

- [[Claude-Code-워크플로우]] — .claude/ 설정, 스킬, 워크플로우 최적화
- [[everything-claude-code]] — 통합 최적화 하네스 (⭐199K)
- [[claude-mem]] — 세션 간 컨텍스트 메모리
- [[andrej-karpathy-skills]] — Karpathy CLAUDE.md 최적화 패턴
- [[openai-codex]] — OpenAI 공식 경쟁 CLI(⭐114,383·Apache-2.0·Rust 본체 공개). 스타는 열세, 소스 개방성은 우위
- [[ECC]] — Claude Code 우선 지원 하네스(⭐242,304·파생이 원천을 스타에서 추월한 사례)
- [[AI-에이전트-프레임워크]] — 에이전트 생태계 현황

## 원본

- 출처: https://github.com/anthropics/claude-code
- 스타: ⭐**142,680** (2026-08-23 **GitHub API 실호출 검증**·당일 +127·raw 표기 142,678과 +2 드리프트) ← ⭐135,978 (2026-07-04, +221 당일) ← ⭐129,171 (2026-06-01)
- 부가 실측(2026-08-23 API): 포크 22,849 · 오픈이슈 **15,113** · 언어 Python · **라이선스 미명시** · 생성 2025-02-22 · 최종 푸시 2026-08-23(당일)
- 성격: 에이전트 본체 소스가 아닌 **배포·이슈 트래킹 채널** — 소스 참조용으로는 [[openai-codex]](Apache-2.0·Rust 본체 공개)가 대체 경로
- 신뢰도: ⭐⭐⭐⭐⭐ (벤더 공식·당일 푸시 활성·수치 API 실검증 — 단 라이선스 미명시·코드 본체 비공개로 **소스 학습 가치는 제한적**)
