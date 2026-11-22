---
title: "rtk-ai/rtk — 에이전트가 읽는 셸 출력을 압축하는 Rust CLI 프록시 (★87k · \"출력 90% 절감 ≠ 비용 90% 절감\"을 README 가 명시)"
type: source
domain: ai-news
tags: [ai-news, github-trending, token-saving, claude-code, rust, cli, hook]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/rtk-ai/rtk]
reliability: high
---

**GitHub**: ★87,448(볼트 API 11-22 · 수집기 11-21 87,335) · Rust · Apache-2.0(CLI) + BUSL-1.1(`engine/`, README 14행 배지 볼트 확인) · 생성 2026-01-22

## 핵심 인사이트
> [!insight] 절감률의 분모를 스스로 밝힌 드문 토큰 절약 도구
> 훅으로 `git status` → `rtk git status` 처럼 셸 명령을 바꿔치기해 테스트는 실패만, diff · log · lint 는 요약만 에이전트에 전달(100+ 명령, 명령당 25ms 미만 자칭). 필터 실패 시 원본 출력 · 종료코드 유지, `rtk bypass` 우회, `rtk gain` 으로 로컬 절감량 집계. **README 가 "명령 출력 90% 절감 ≠ 비용 90% 절감"(명령 출력은 입력 토큰의 일부) · 토큰 수는 `bytes/4` 추정치라고 명시**(수집기 판독) → [[자기제한-명시]].

> [!warning] 수치의 출처
> - "파이프라인"(큰 파일 읽기를 저가 모델에 위임 등)의 최고 사례 **총비용 −20.2% 는 작성자 자체 벤치마크**(README 55행 "author's benchmark", 볼트 확인).
> - 기본 훅은 Read/Grep/Glob 같은 내장 도구는 건드리지 않는다 → 절감 폭은 세션의 셸 출력 비중에 좌우.
> - `engine/` 은 BUSL-1.1, 유료 RTK Pro(전사 게이트웨이) 유도 포함.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐⭐ — ★87k · 한계 자기 명시 · 독립 측정은 없음.
- **즉시 활용**: ✅ YES — Claude Code 에 `rtk init -g` 한 줄. 효과는 `rtk gain` 으로 **내 세션에서 직접** 잰다.
- **6개월 영향력**: 컨텍스트 절약이 모델 쪽([[SparseRead]] 의 노출 예산)과 도구 출력 쪽(rtk · [[context-mode]])에서 동시에 진행.
- **대체 관계**: [[context-mode]] (도구 출력 샌드박스)와 목적이 겹친다. [[OmniRoute]] 는 rtk 를 구성요소로 언급.
- **허와 실**: 90% 는 셸 출력 한정. 총비용 기준 최고 사례가 −20.2%(자체 측정).
- **액션**: 설치 시험 → `rtk gain` 1주 기록(actionable 등록).

## 관련 페이지
- [[context-mode]] · [[SparseRead]] · [[OmniRoute]] · [[Claude-Code-워크플로우]] · [[자기제한-명시]]

## 원본
- 출처: https://github.com/rtk-ai/rtk
- 확인 범위: GitHub API · README 14행(라이선스 배지) · 55행(20.2% author's benchmark) 볼트 판독 · 🔴 "≠ 비용" 문장 · bytes/4 는 수집기 판독(볼트 grep 은 이미지 alt 텍스트만 적중) · 실행 0
- 신뢰도: ⭐⭐⭐⭐
