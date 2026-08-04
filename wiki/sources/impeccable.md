---
title: impeccable — AI 하네스 디자인 언어 (pbakaus)
type: source
domain: ai-news
tags: [ai-news, github-trending, design-system, ai-harness, frontend, claude-code, agent-skills, design-tokens]
created: 2026-07-27
updated: 2026-07-27
sources: []
reliability: high
---

# impeccable (pbakaus/impeccable, ⭐51,000)

**GitHub**: https://github.com/pbakaus/impeccable
**스타수**: ⭐51,000 (2026-07-27, 당일 +413) / JavaScript·TypeScript / Apache 2.0

> [!insight] 핵심 인사이트
> "AI 하네스를 디자인에 더 능숙하게 만드는 **디자인 언어**." AI 코딩 에이전트가 만들어내는 프런트엔드의 고질적 약점(밋밋한 UI·안티패턴)을 **프롬프트가 아니라 검증 가능한 룰셋**으로 잡는다. 핵심은 두 축: ①`/impeccable audit`·`/impeccable polish`·`/impeccable critique` 등 **23개 슬래시 커맨드**(스킬), ②**60개 결정론적(deterministic) 디텍터 룰**로 흔한 디자인 안티패턴을 API 키 없이 파일·URL 스캔으로 잡아냄. [[Google-Labs]]의 [[design.md]]가 "에이전트에 주입하는 디자인 명세"였다면, impeccable은 거기에 **결정론 검출기 + 라이브 브라우저 이터레이션**을 붙여 "명세→자동 감사→수정" 루프로 발전시킨 형태 — 즉 [[SWE-Pruner-Pro]]·[[open-code-review]]가 코드에서 한 "LLM 판단을 결정론 룰로 보강" 패턴의 **디자인판**.

## 핵심 인사이트

> [!note] 구조 (README 실측)
> - **23개 커맨드**: audit(감사)·polish(다듬기)·critique(비평) 등 — [[agent-skills]] 형태로 하네스에 설치
> - **60개 결정론 디텍터 룰**: 대비 부족·간격 불일치·타이포 위계 붕괴 등 안티패턴을 규칙으로 검출 (LLM 호출 없이 확정적)
> - **CLI**: API 키 불필요, 로컬 파일·라이브 URL 스캔
> - **멀티 플랫폼**: 여러 AI 코딩 도구(Claude Code·기타 하네스) 지원, 라이브 브라우저 이터레이션 포함

> [!action] tools-frontend / reat 계열에 직접 참고
> 내 [[tools-frontend]]·[[reat-layout]]·[[reat-analyze]]가 "AI로 프런트/레이아웃 생성"을 하는데, 결과물 디자인 품질은 항상 약점. impeccable의 **60개 결정론 룰 + audit 커맨드 구조**를 참고해, 생성된 레이아웃/슬라이드에 "결정론 디자인 게이트"를 붙이는 실험 가치 큼. Apache 2.0이라 룰셋 차용 가능.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐51,000(당일 +413), Apache 2.0. GitHub API 실검증. "디자인 완성도 향상" 효과 주장은 산출물 재현으로 확인 필요하나 룰셋·CLI 존재는 확정.
- **즉시 활용**: YES — CLI가 API 키 없이 파일·URL 스캔이라 즉시 시험 가능. 내 프런트 산출물에 audit 돌려 안티패턴 목록만 뽑아도 가치.
- **6개월 영향력**: "에이전트에 디자인 감각을 코드로 주입" 흐름의 대표 사례. [[design.md]]·[[Impeccable]]류가 표준화되면 AI 생성 UI의 하한선이 올라감 — 순수 프롬프트로 디자인 품질을 올리려던 접근을 **결정론 룰 게이트**가 대체·보강.
- **대체 관계**: 디자인 시스템 문서(피그마·스토리북)를 대체하진 않지만, **AI 산출물 품질 게이트**로서 수작업 디자인 리뷰의 1차 필터를 대체.
- **허와 실**: "디자인을 잘하게 만든다"는 결국 룰 커버리지에 달림 — 60개 룰이 잡는 건 안티패턴 회피이지 창의적 디자인은 아님. 하한선 상승 도구로 이해.
- **액션**: CLI 설치 → 내 프런트 산출물(reat 슬라이드·tools-frontend)에 audit 실행, 결정론 룰 60개 중 이식 가능 항목 추출.

## 관련 페이지
- [[design.md]] — 에이전트용 디자인 명세 (impeccable의 선행 계보)
- [[Google-Labs]] — design.md 배포처
- [[agent-skills]] — 23개 커맨드의 배포 단위
- [[open-code-review]] — 코드판 "결정론 룰 + LLM" 하이브리드
- [[SWE-Pruner-Pro]] — "모델 판단을 결정론 신호로 보강" 계보
- [[tools-frontend]] — 내 프런트 개발 오버레이 (적용 대상)
- [[reat-analyze]] — 내 디자인 토큰 추출 스킬 (연결점)

## 원본
- 출처: https://github.com/pbakaus/impeccable
- GitHub: ⭐51,000 (2026-07-27, 당일 +413), JavaScript·TypeScript, Apache 2.0
- 구성: 23 커맨드 + 60 결정론 디텍터 룰 + 키 불필요 CLI + 라이브 브라우저 이터레이션
- 신뢰도: ⭐⭐⭐⭐⭐ (GitHub API 실검증, 대규모 스타·명확한 구조. 디자인 향상 "효과"는 산출물 재현 전 잠정)
