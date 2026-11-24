---
title: "bendlang/bend — 'AI가 짠 코드를 증명으로 막는' 의존 타입 병렬 언어 Bend 2 (LAWS.bend · PROOF.bend)"
type: source
domain: ai-news
tags: [ai-news, github, programming-language, dependent-types, gpu-parallelism, agent-verification, proof-gate]
created: 2026-11-24
updated: 2026-11-24
sources: [https://github.com/bendlang/bend]
reliability: medium
---

**GitHub**: ★25,832(볼트 API 11-24 · 수집기 11-23 25,790) · 당일 +53(TypeScript Trending) · TypeScript(컴파일러) · Apache-2.0 · 생성 2023-08-29 · HEAD `0e2f38f759`(수집기 11-18) · open issues 265

## 핵심 인사이트
> [!insight] 법칙을 선언하면 컴파일러가 증명을 요구한다 — "증명으로 뒷받침되는 AGENTS.md"
> Bend 2 = Python형 문법 + 의존 타입 + 선형(affine) 값 언어. CPU 단일 코어는 C 수준 · GPU 수천 코어 자동 병렬화 목표(분할정복 재귀를 `!` 로 GPU 실행). 핵심 신기능 `LAWS.bend`: 앱이 깨면 안 되는 규칙("잔액 합은 0", "벽 통과 불가")을 **법칙으로 선언**하면 코드 수정 때마다 컴파일러가 수학적 증명(`PROOF.bend`)을 요구하고, 증명이 안 되면 커밋이 막힌다. 사용법은 AGENTS.md 에 `bend guide` · `bend PROOF.bend` 실행 지시를 넣고 코딩 에이전트에게 맡기는 방식 — [[에이전트-스킬]] 형식과 정확히 같은 결이다.

> [!warning] 속도 · 증명 속도 주장은 이미지 차트뿐
> "C만큼 빠름", "다른 증명기보다 수 자릿수 빠름" 수치는 README 이미지 차트로만 제시 — 텍스트 수치 없음(bench/ 미열람, [[벤치마크-이미지-봉인]] 유형). README 가 스스로 적은 한계: Bend 1 · HVM 코드 비호환, **타입 추론 없음(전부 주석 → 장황)**, 타입클래스 · 트레이트 · 매크로 없음, **전술(tactic) · 증명 탐색 없음 → 증명 작성 부담이 사람 몫**, 클로저 · 배열 공유 불가, 재귀는 종료해야 함. 논문 2편(BendTT · BendRT PDF) + Lean 형식화 커널 동봉.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★25.8k · Apache-2.0 · Lean 형식화 커널 동봉. 단 2023-08 생성 레포의 대규모 리라이트(Bend 1 비호환)이고 실사용 보고는 아직 없음.
- **즉시 활용**: NO — 신생 언어라 기존 프로젝트 적용 어려움. 법칙을 정확히 쓰는 일 자체가 남는다.
- **6개월 영향력**: "에이전트 출력 검증" 수요가 커지면 언어 수준 증명 게이트가 하나의 답이 된다. [[검사가능성-공사]] 의 빌드 단계 버전: 미검증 코드가 저장소에 들어가지 못하게 **컴파일러가 게이트를 쥔다**.
- **허와 실**: 차트 수치(속도 · 증명 속도)는 미검증. 반대로 한계를 README 에 항목으로 나열한 것은 [[자기제한-명시]].
- **액션**: 없음(관찰 대상).

## 관련 페이지
- [[에이전트-스킬]] · [[검사가능성-공사]] · [[Claude-Code-워크플로우]] · [[ai-news]]

## 원본
- 출처: https://github.com/bendlang/bend
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 · 생성일 — 볼트 11-24) · README 내용은 수집기 11-23 판독(수치 이미지 병기 확인) · bench/ · 논문 PDF 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐
