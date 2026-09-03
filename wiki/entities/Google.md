---
title: Google
type: entity
domain: ai-news
tags: [ai-news, organization, bigtech, ai-agent, gemini, google-cloud]
created: 2026-07-02
updated: 2026-09-03
sources: [agents-cli.md]
reliability: high
---

# Google

> [!update] 2026-09-03 — **TimesFM 3.0 공개** · 에이전트 일색 배치에서 유일한 비-LLM 축
> [[TimesFM]] GitHub ⭐**30,397**(포크 2,907 · 이슈 236 · Apache-2.0 · 트렌딩 **2위** · 푸시 2026-09-02), 신모델 **`google/timesfm-3.0-pytorch`**(생성 2026-08-24 · DL **46,862** · 좋아요 315 · **331M** · 라이선스 **`other`**) — 전량 API 실검증.
> ⚠️ **코드와 가중치의 라이선스가 다르다** — 레포는 Apache-2.0인데 모델은 `other`다. 볼트 09-02 규칙(*라이선스는 배지가 아니라 원문으로*)이 **한 프로젝트 안에서도 층이 갈릴 수 있음**을 보여준다.
> 📌 **331M**은 같은 배치 [[GLM-5.3]] 753B의 **2,275분의 1**이다. Google은 시계열에서 **스케일이 아닌 배포 가능성** 축으로 간다 → [[시계열-예측-파운데이션-모델]] 참조.
> ⚠️ **2.5가 3.0보다 다운로드가 많다**(55,036 vs 46,862) — 세대 교체 미완. 성능 벤치는 **미확인**.

> [!insight] 핵심 인사이트
> Gemini·Gemma 모델군과 Google Cloud를 축으로, **코딩 에이전트를 겨냥한 도구·명세를 잇따라 오픈소스로 배포**하는 전략이 뚜렷하다. 이 위키에는 [[agents-cli]](코딩 어시스턴트로 GCP 위 AI 에이전트 생성·평가·배포하는 CLI, ADK 기반)와 [[design-md]](Google Labs 코딩 에이전트용 디자인 명세)로 등장 — 둘 다 "Claude Code·Codex 같은 코딩 에이전트 안에서 불리도록" 설계돼, *에이전트 툴체인 표준을 GCP로 끌어오려는* 일관된 움직임. [[Gemma-4-12B]] 계열은 [[gemma-4-12B-coder-GGUF]]·[[gemma-4-12B-agentic-GGUF]]처럼 커뮤니티 로컬 파인튜닝의 베이스로도 확산 중.

## 관련 소스
- [[agents-cli]] — ADK 기반 GCP AI 에이전트 배포 CLI (Apache 2.0)
- [[design-md]] — Google Labs 코딩 에이전트용 비주얼 아이덴티티 명세

## 관련 페이지
- [[Google-Labs]]
- [[Gemma-4-12B]]
- [[gemma-4-12B-coder-GGUF]]
- [[Claude-Code-워크플로우]]
- [[ai-news]]

## 원본
- 조직: Google (Google Cloud · Google Labs · DeepMind)
- 관련 활동: Gemini·Gemma · Agent Development Kit(ADK) · 코딩 에이전트용 오픈 도구
- 신뢰도: ⭐⭐⭐ (공식 빅테크)
