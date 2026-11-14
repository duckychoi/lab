---
title: "QwenLM/qwen-code — Gemini CLI 에서 갈라져 나온 다중 프로토콜 코딩 에이전트 (7개 버전 SWE-bench 76.40–77.80%)"
type: source
domain: ai-news
tags: [ai-news, github-trending, coding-agent, cli, qwen, harness]
created: 2026-11-14
updated: 2026-11-14
sources: [https://github.com/QwenLM/qwen-code]
reliability: high
---

**레포**: [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) · ★**30,134** · fork 3,418 · Apache-2.0 · TypeScript · repo id 1008713177 · created 2025-06-26 · pushed 2026-11-14T08:53Z · open_issues 2,274(이슈+PR) (GitHub API 볼트 실측). 수집기 11-13 ★30,037.

## 핵심 인사이트
> [!insight] 하네스를 22개 마이너 버전 동안 고쳤는데 점수는 1.4%p 안에서 움직였다
> README 201–203행: 같은 **Qwen 3.7 Max** 모델로 7개 버전을 SWE-bench Verified(500 과제 × 3회)에 돌린 평균 —
> `0.0.14` **77.80** · `0.1.0` 76.73 · `0.5.0` 76.60 · `0.10.0` 76.47 · `0.15.0` 77.67 · `0.19.0` 76.40 · `0.22.0` 77.33.
> **가장 오래된 버전이 최고점**이다. Auto-Memory · Auto-Skills · SubAgents · Agent Teams 가 그 사이에 붙었지만 이 벤치에서는 차이를 만들지 못했다. README 는 이를 "버전 간 안정성"으로 제시한다 — 다르게 읽으면 [[하네스-설계-축]]에서 **모델이 고정되면 하네스 기능 추가의 한계 이득이 이 벤치에서는 0에 가깝다**는 자료다(SWE-bench Verified 가 그 기능들을 요구하지 않는 과제일 수 있다는 단서와 함께).

> [!note] 계보
> Google [[gemini-cli]] v0.8.2 기반, v0.1 부터 업스트림 동기화를 끊고 독립 개발(README 234행). OpenAI · Anthropic · Gemini · Qwen API 와 Ollama/vLLM 로컬 모델을 런타임 전환. IDE 플러그인 · 데스크톱 · 웹 UI · Telegram/DingTalk/WeChat/Feishu 연동. Qoder 하네스를 합친 "1.0 Preview" 는 별도 태그(수집기 판독).

> [!warning] 주의
> 타 에이전트(Claude Code · Codex) 대비 수치는 없다 — 표는 자기 버전끼리의 비교다. 기본 인증 경로는 Qwen 유료 구독(수집기 판독).

## 도메인별 추출 (ai-news)
- **신뢰도**: ★30,134 · [[Qwen]] 공식 · 벤치 조건(모델·과제 수·반복) 명시.
- **즉시 활용**: 조건부 — 로컬 모델(vLLM/Ollama)을 코딩 에이전트에 붙이는 용도로는 후보. 볼트는 Claude Code 기반이라 전환 이유는 없다.
- **6개월 영향력**: 모델 벤더가 자사 CLI 를 "다중 프로토콜"로 여는 흐름([[opencode]] 와 같은 방향).
- **대체 관계**: [[gemini-cli]] 파생 · [[opencode]] · [[openai-codex]] 와 경쟁.
- **허와 실**: 기능 목록은 길고, 측정된 것은 "버전이 바뀌어도 점수가 안 변한다"뿐.
- **액션**: 없음(관찰).

## 관련 페이지
- [[Qwen]] · [[Alibaba]] · [[gemini-cli]] · [[opencode]] · [[openai-codex]] · [[하네스-설계-축]] · [[free-claude-code]]

## 원본
- 출처: https://github.com/QwenLM/qwen-code
- 확인 범위: GitHub API 메타 · README 201–203행 · 234행 직접 판독 · 🔴 기능 목록·인증 경로는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (★30,134 · 공식 · 조건 명시 벤치)
