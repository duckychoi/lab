---
title: "NVIDIA/SkillEvaluator — 에이전트 스킬의 품질·중복·실효를 3단계로 평가"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, evaluation, nvidia, ci]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/NVIDIA/SkillEvaluator]
reliability: medium
---

**레포**: [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) · ★**2,083**(볼트 11-16 실측) · fork 285 · Python · Apache-2.0 · repo id 1278676884 · 생성 2026-06-24 · PyPI `skillevaluator` · arXiv 2608.20614(수집기).

## 핵심 인사이트
> [!insight] 스킬은 "있으면 좋다"가 아니라 有/無 비교로 재야 한다
> **Tier 1 검증**(안전성 · 형식 · 하네스 호환 — [[SkillSpector]] · Gitleaks 자동 설치, Semgrep 선택) → **Tier 2 중복 탐지**(임베딩으로 스킬 내 · 스킬 간 지침 중복) → **Tier 3 라이브 평가**(Harbor 로 Docker 샌드박스에서 스킬 有/無 에이전트 비교). 볼트가 반복 관찰한 "스킬 레포는 효과 수치가 없다"([[에이전트-스킬]])에 대한 측정 도구 쪽 답.

> [!warning] 정적 점수 ≠ 효과 (README 109 · 113 · 157행 · 볼트 확인)
> 키 없이 도는 `quality-check` 예제 점수 **86.2/100 (B)**(통과선 70)는 *static quality* 이고 *"publication evidence stays `INCOMPLETE`"*. 스캐너가 못 돌면 `INCOMPLETE` + 비정상 종료. Tier 3 autopilot 은 "커버리지 제한된 케이스 1개"만(수집기).

## 도메인별 추출 (ai-news)
- **신뢰도**: ★2,083 · NVIDIA · 논문 동반.
- **즉시 활용**: **YES** — 볼트 `~/.claude/skills/` 의 자작 스킬(wiki 등)에 Tier 1 · 2 를 키 없이 돌려 형식 · 중복 점검 가능. `skillevaluator ci init` 으로 PR 체크.
- **6개월 영향력**: 스킬 마켓 · 플러그인 배포가 늘면 "Verified Skills" 류 게이트가 배포 조건이 된다([[SkillSpector]] 와 같은 파이프라인).
- **대체 관계**: 수동 스킬 리뷰.
- **허와 실**: 정적 점수는 형식 점검일 뿐 — 실효는 Tier 3(Docker + 모델 키) 필요.
- **액션**: 자작 스킬 1개에 Tier 1 · 2 시험(actionable).

## 관련 페이지
- [[NVIDIA]] · [[SkillSpector]] · [[에이전트-스킬]] · [[elephant-goldfish-model]] · [[ffmpeg-skill]] · [[Claude-BugHunter]] · [[측정도구-먼저-반증]]

## 원본
- 출처: https://github.com/NVIDIA/SkillEvaluator
- 확인 범위: GitHub API 메타 · README 109 · 113 · 157행(볼트) · 🔴 3단계 구성 세부 · arXiv 번호는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (NVIDIA · 논문 · 측정 도구)
