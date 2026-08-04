---
title: OpenSpec — AI 코딩 어시스턴트용 스펙 주도 개발(SDD) 프레임워크
type: source
domain: ai-news
tags: [ai-news, github-trending, spec-driven-development, claude-code, agent-workflow, vibe-coding]
created: 2026-06-28
updated: 2026-06-28
sources: []
reliability: high
---

# OpenSpec (Fission-AI/OpenSpec)

> [!insight] 핵심 인사이트
> GitHub ⭐57,292 — 코드를 짜기 **전에** 사람과 AI가 "무엇을 만들지" 명세(spec)에 먼저 합의시키는 경량 **스펙 주도 개발(SDD, Spec-Driven Development)** 프레임워크. AI 코딩의 고질병인 "막연한 프롬프트 → 예측 불가한 결과"를, 의도와 코드 생성 사이에 *구조화된 스펙 레이어*를 끼워 해결한다. 이것은 [[바이브코딩]]의 안티테제가 아니라 **상위 호환** — "느낌으로 짜기"의 무계획성을 "합의된 명세로 짜기"로 길들이는 흐름이다. [[design-md]]([[Google-Labs]])가 *디자인*을 에이전트가 읽는 설정 파일로 만들었다면, OpenSpec은 *요구사항/태스크*를 그 자리에 올린 같은 계보.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐57,292의 대형 레포. npm 공식 배포(`@fission-ai/openspec`), Claude·Copilot 등 25개+ 코딩 도구 연동. 채택 규모로 신뢰도 높음.
- **즉시 활용**: YES — `/opsx:explore`(코드베이스 탐색·아키텍처 검토) → `/opsx:propose <기능>`(proposal·spec·design·태스크 체크리스트 생성) → `/opsx:apply`(구현)의 3단계 슬래시 커맨드 워크플로. Claude Opus 같은 고추론 모델과 결합 시 효과 극대화. 내 [[Claude-Code-워크플로우]]에 바로 얹을 수 있다.
- **6개월 영향력**: "프롬프트→코드" 직접 생성에서 "스펙 합의→코드 생성"으로 코딩 에이전트 사용 패턴이 이동. 변경마다 proposal/spec/design/checklist 폴더가 남아 **brownfield(기존 코드베이스) 작업의 추적성**이 크게 개선됨.
- **대체 관계**: 수동 CLAUDE.md/이슈 작성·즉흥 프롬프팅을 대체·구조화. [[design-md]]가 디자인 토큰을 맡는다면 OpenSpec은 기능 명세를 맡아 상호 보완.
- **허와 실**: "fluid not rigid / iterative not waterfall"을 표방 — 워터폴 회귀가 아니라 언제든 산출물을 갱신할 수 있는 반복형. 다만 소규모 일회성 작업에는 오히려 오버헤드. 가치는 *반복·협업·장기 코드베이스*에서 나온다.
- **액션**: 한 개 실제 기능을 OpenSpec 워크플로로 시범 적용 → proposal/spec 산출물 품질과 구현 일관성을 즉흥 프롬프팅과 대조.

> [!action] 당장 할 것
> `npm install -g @fission-ai/openspec@latest` (Node 20.19+) → 기존 프로젝트에서 `openspec init` → 다음 기능 1건을 `/opsx:propose`로 명세화해보고 결과 일관성 체감.

## 관련 페이지
- [[바이브코딩]]
- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[design-md]]
- [[OpenMontage]]
- [[ai-news]]

## 원본
- 출처: https://github.com/Fission-AI/OpenSpec
- GitHub 스타: ⭐57,292 (2026-06-28)
- 설치: `npm install -g @fission-ai/openspec@latest` (Node.js 20.19.0+)
- 신뢰도: ⭐⭐⭐ (대형 레포, npm 공식 배포, 25개+ 코딩 도구 연동)
