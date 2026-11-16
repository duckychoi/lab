---
title: "google/elephant-goldfish-model (EGM) — 문맥 가진 작성자 + 문맥 없는 검토자로 설계 문서를 쓰고 리뷰하는 에이전트 플러그인"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, design-review, google, claude-code]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/google/elephant-goldfish-model]
reliability: medium
---

**레포**: [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) · ★**20,023**(볼트 11-16 실측) · fork 1,485 · Python · Apache-2.0 · repo id 1368596582 · 생성 2026-09-13 · 주간 트렌딩 +5,060(수집기). API description: *"Open-source plugin for designing and reviewing software with agents"*.

## 핵심 인사이트
> [!insight] "새 눈"을 구조로 만든다 — 작성자와 검토자의 문맥 분리
> **Elephant** 는 대화 문맥을 기억한 채 `/egm-brainstorm` → `concepts_brief.md` → `/egm-draft` → `design_draft.md` 를 섹션별로 쓰고, **Goldfish** 는 이전 대화 없이 문서와 참조 소스만 보고 숨은 가정 · 불명확 요구 · 구현 위험을 찾는다(`/egm-review` 5단계). README 16행 *"review documents with fresh eyes"*. 같은 모델이라도 **문맥을 공유하지 않는 검토자**가 작성자의 맹점을 보게 하는 설계 → [[요약자와-판정자-분리]] 의 실무 도구판. `/egm-drift-report` 는 `docs/designs/` 와 현재 코드의 괴리 보고.

> [!warning] 스스로 그은 선 (수집기 판독)
> Goldfish 리뷰는 **새 서브에이전트 컨텍스트 필수 — 못 만들면 리뷰 중단** · 리뷰는 테스트 · 사람 판단을 대체하지 않음 · Google 공식 지원 제품 아님. 정량 효과 수치 0 → [[자기제한-명시]].

## 도메인별 추출 (ai-news)
- **신뢰도**: ★2만 · 2개월 차 · Google 조직 레포(비공식 표기) · 측정 0.
- **즉시 활용**: **YES** — Claude Code 에 플러그인으로 설치(`/egm:` 접두, README 80행). 볼트 스키마 변경 · 수집기 프롬프트 수정 같은 "설계 문서" 작업을 Goldfish 로 검토시키기 좋다.
- **6개월 영향력**: 서브에이전트가 일반화되면서 "같은 모델 두 번 부르기"가 아니라 **문맥 격리**가 리뷰 품질의 변수가 된다.
- **대체 관계**: 사람 디자인 리뷰의 1차 필터. [[superpowers]] 류 브레인스토밍 스킬과 겹침.
- **허와 실**: 구조 아이디어는 견고, 효과는 미측정.
- **액션**: 설치 시험(actionable).

## 관련 페이지
- [[Google]] · [[에이전트-스킬]] · [[요약자와-판정자-분리]] · [[자기제한-명시]] · [[Claude-Code-워크플로우]] · [[superpowers]] · [[SkillEvaluator]](같은 배치 · 스킬 평가)

## 원본
- 출처: https://github.com/google/elephant-goldfish-model
- 확인 범위: GitHub API 메타 · README 16 · 66 · 80행(볼트) · 🔴 명령 흐름 · 한정 문구는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (★2만 · 측정 0)
