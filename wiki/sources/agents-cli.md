---
title: google/agents-cli — 코딩 어시스턴트로 Google Cloud AI 에이전트를 만드는 CLI
type: source
domain: ai-news
tags: [ai-news, github-trending, ai-agent, google-cloud, adk, cli, deployment]
created: 2026-07-02
updated: 2026-07-02
sources: []
reliability: high
---

# agents-cli (google/agents-cli)

> [!insight] 핵심 인사이트
> ⭐4,609 (2026-07-02, 당일 **+586** — 스타 대비 유입 속도가 매우 빠름). [[Google]] 공식 오픈소스로, **코딩 어시스턴트([[Claude-Code-워크플로우]]·Codex 등)가 Google Cloud 위에서 AI 에이전트를 생성·평가·배포하도록 돕는 CLI**. Agent Development Kit(ADK) 프레임워크 기반으로 에이전트 프로젝트 스캐폴딩 → 평가(메트릭·데이터셋·멀티턴 합성) → 배포(Cloud Run·GKE·Agent Runtime) → Gemini Enterprise 게시까지 **40+ 명령**을 제공한다. **Apache 2.0**. 핵심 포인트는 "코딩 에이전트가 *다른* 에이전트를 만드는 메타 도구"라는 점 — [[Claude-Code-워크플로우]] 안에서 스킬처럼 호출되도록 설계됐다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — Google 공식 + Apache 2.0 + 당일 +586(스타 4.6K 대비 고속 유입). ADK 생태계 공식 진입점.
- **즉시 활용**: MAYBE — 배포 타깃이 **Google Cloud(Cloud Run/GKE/Agent Runtime)** 로 고정돼, GCP를 안 쓰면 로컬 개발·평가 부분(스캐폴딩·eval 합성)만 부분 활용. GCP 사용 시 에이전트 배포 자동화로 강력.
- **6개월 영향력**: 높음(GCP 진영) — [[Claude-Code-워크플로우]]·Codex가 "에이전트 배포 파이프라인"을 CLI로 표준화하는 흐름. 벤더별 에이전트 배포 CLI 경쟁(OpenAI·AWS 대비)의 Google 카드.
- **대체 관계**: 수동 GCP 콘솔 배포 + 자체 eval 스크립트를 대체. [[agency-agents]]가 "에이전트 팀 구성"이라면 이건 "에이전트 배포·운영 인프라".
- **허와 실**: "40+ 명령"의 상당수는 GCP 인프라 프로비저닝. 실체는 *ADK + gcloud를 코딩 에이전트가 부리기 쉽게 래핑*한 것. GCP 락인 주의.
- **액션**: GCP 프로젝트가 있을 때 `create → eval` 로컬 흐름만 먼저 시험 → 멀티턴 eval 합성이 내 에이전트 품질 측정에 쓸 만한지 확인.

> [!note] 배경 정보
> "코딩 어시스턴트가 지원하는" 표현은 Claude Code·Codex 같은 도구 안에서 skill/command로 불리도록 명세를 제공한다는 뜻. [[design-md]](Google Labs 디자인 명세)와 함께 "코딩 에이전트를 겨냥해 도구를 배포"하는 Google의 일관된 전략.

## 관련 페이지
- [[Google]]
- [[Claude-Code-워크플로우]]
- [[agency-agents]]
- [[design-md]]
- [[ai-news]]

## 원본
- 출처: https://github.com/google/agents-cli
- 스타: ⭐4,609 (2026-07-02, 당일 +586)
- 프레임워크: Agent Development Kit(ADK) · 배포: Cloud Run/GKE/Agent Runtime/Gemini Enterprise · Apache 2.0
- 신뢰도: ⭐⭐⭐ (Google 공식, 고속 유입 — GCP 종속)
