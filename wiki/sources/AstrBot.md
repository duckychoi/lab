---
title: AstrBot — 다중 메신저 통합 AI 에이전트 챗봇 플랫폼
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-framework, chatbot, multi-platform, mcp, plugin]
created: 2026-07-20
updated: 2026-07-22
sources: []
reliability: high
---

# AstrBot (AstrBotDevs/AstrBot)

> [!update] 2026-07-22 갱신 — 소폭 성장·어댑터 실확인
> ⭐**37,700**(당일 +416) ← 07-20 36,836. 이틀 새 +864로 완만한 성장 지속. WebFetch 재확인: 공식 유지 어댑터 **14+**(QQ·WeChat Work·Feishu·DingTalk·WeChat 공식계정·Telegram·Slack·Discord·LINE·Satori 등) + 커뮤니티(Matrix·Rocket.Chat 등). 07-20의 "텔레그램/Slack/Discord 어댑터 성숙도 확인" 과제는 여전히 실사용 검증 대상. reliability high 유지.

> [!insight] 핵심 인사이트
> ⭐**36,836 (2026-07-20, 당일 +83)**. **15개+ 메신저 플랫폼(QQ·WeChat Work·Feishu·DingTalk·Telegram·Slack·Discord·LINE 등)에 LLM 에이전트를 붙이는 올인원 챗봇 플랫폼**. OpenAI·[[Anthropic]]·[[Google]] Gemini·DeepSeek·Ollama 등 다중 LLM 백엔드 + [[MCP]] 통합 + **1000개+ 커뮤니티 플러그인** 원클릭 설치 + 에이전트 샌드박스(격리 코드 실행) + 지식베이스·페르소나. 이 위키의 에이전트 축에서 **"IM 채널 배포 레이어"** 를 담당 — [[lobehub]]가 GUI 오케스트레이션, [[OpenManus]]·[[deer-flow]]가 코드형 하네스라면, AstrBot은 **"이미 사람들이 쓰는 메신저 안으로 에이전트를 배달"** 하는 마지막 1마일.

> [!note] 배경 정보
> 내 관심사(ChinameBot류 텔레그램/메신저 봇)와 가장 직접 맞닿는 소스. Hermes/GLM 백엔드를 붙여 여러 메신저에 동시 서빙하는 골격을 이미 제공 — 플랫폼 어댑터·플러그인·페르소나·MCP를 직접 구현하지 않고 재사용 가능. "다중 IM 어댑터 + 플러그인 마켓"이라는, 개인이 만들기엔 비용 큰 부분을 오픈소스로 흡수.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐3.68만 대형 활성 프로젝트. 다중 플랫폼·1000+ 플러그인 주장은 WebFetch로 확인(README 기재). 개별 플랫폼 어댑터 안정성·한국어 대응은 실사용 검증 필요. raw 수치(당일 +83)는 ⭐36.8k와 일치.
- **즉시 활용**: YES(후보) — 텔레그램/메신저에 LLM 봇을 붙이는 작업을 밑바닥부터 짜는 대신 AstrBot 어댑터+플러그인으로 대체 가능. 특히 **다중 채널 동시 서빙 + MCP 도구 연결**이 바로 필요한 골격.
- **6개월 영향력**: "에이전트 프레임워크"가 개발툴(코드 하네스)에서 **엔드유저 배포 채널(메신저 봇)** 로 확산되는 흐름. LLM을 붙일 곳이 웹챗 → IM 플랫폼으로 넓어짐.
- **대체 관계**: 직접 짠 텔레그램 봇 + 개별 LLM SDK 연결을 통합 플랫폼으로 대체. [[lobehub]](GUI 오케스트레이션)와는 배포 대상(IM vs 웹)에서 차별.
- **허와 실**: 중국 IM(QQ·WeChat·Feishu) 중심 생태계라 플러그인 상당수가 중화권 서비스 특화일 수 있음 — 텔레그램/Slack/Discord 어댑터 성숙도를 별도 확인해야 오판 방지.
- **액션**: star + Telegram 어댑터로 최소 봇 1개 구동 → Hermes/GLM 백엔드 + MCP 도구 붙여 ChinameBot류 골격 이식 가치 스팟체크.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[lobehub]]
- [[OpenManus]]
- [[deer-flow]]
- [[Anthropic]]
- [[ai-news]]

## 원본
- 출처: https://github.com/AstrBotDevs/AstrBot
- GitHub: ⭐37,700 (2026-07-22, 당일 +416) — WebFetch 실확인 / cf. ⭐36,836(07-20)
- 어댑터: 공식 14+(QQ·WeChat Work·Feishu·DingTalk·Telegram·Slack·Discord·LINE·Satori 등) + 커뮤니티(Matrix·Rocket.Chat)
- 신뢰도: ⭐⭐⭐ (대형 활성 프로젝트, 실재 확고 / 개별 어댑터·한국어 성숙도 미검증)
