---
title: Worktrunk — 병렬 에이전트에게 각자의 파일시스템을 주는 git worktree CLI
type: source
domain: ai-news
tags: [ai-news, github, git-worktree, rust, parallel-agents, developer-tools, filesystem-layer]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: medium
---

# GitHub: max-sixty/worktrunk — ★7,876

**URL**: https://github.com/max-sixty/worktrunk
**지표(2026-09-16 API 실측)**: ★ **7,876** (raw 7,874 · 드리프트 **+2**) · fork **272** · Rust
생성 **2025-10-17** · 최종 push **2026-09-16** · topics: `agents`·`claude-code`·`codex`·`developer-tools`·`git`·`worktrees`
⚠️ 증분 **주간 +871** — 당일 급상승 아님

> [!insight] 핵심 인사이트 — **에이전트 병렬화의 병목은 모델이 아니라 작업 디렉터리였다**
> 에이전트 5~10개를 동시에 돌리면 **같은 워킹 트리를 놓고 충돌한다.** worktrunk는 각자에게 **독립 worktree**를 주고 핵심 명령 3개 + 훅으로 수명주기를 관리한다.
>
> 🎯 **이 배치 GitHub 5건 중 4건이 "모델 위 계층"이다** — [[pi-agent-harness]](런타임) · [[atlas-source-control]](버전관리) · [[LibreChat]](접근 UI) · worktrunk(파일시스템). **아무도 모델을 만들지 않는다.**
> 📌 에이전트 생태계의 경쟁축이 **모델 품질 → 모델을 둘러싼 계층**으로 이동한 정황이다. 다만 이는 **이 배치 5건 기준의 관찰**이며 전체 트렌드 주장이 아니다.

> [!insight] ★:fork = **29:1** — 이 배치 최고
> [[LibreChat]] 4.9:1 · [[9router]] 5.5:1 · [[pi-agent-harness]] 7.9:1 · [[atlas-source-control]] 16.6:1 · **worktrunk 29:1**
> 🎯 **fork가 거의 없다 = 아무도 고쳐 쓰지 않는다 = 설치해서 그대로 쓴다.** 명령 3개짜리 CLI의 정상적인 형태다. **★ 절대값만 보면 이 배치 4위지만, 사용 밀도는 가장 높을 수 있다.**

> [!warning] ⚠️ 저자 자평 — 근거 수치 없음
> README의 *"the most popular git worktree manager"* 는 **비교군·집계 시점·기준이 없는 자평**이다. ★7,876이 이 범주에서 1위라는 근거는 레포에 없다.
> 🔗 [[한정어-탈락]] 의 전형: 최상급을 쓰면서 **분모를 적지 않는다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ medium. ★·fork·언어·날짜 전건 실측. ⚠️ 주간 집계 · 최상급 자평 미검증
- **즉시 활용**: **YES — 이 배치에서 가장 즉시성이 높다.** 에이전트를 2개 이상 동시에 돌린다면 오늘 설치해서 효과를 확인할 수 있다. Rust 단일 바이너리 · 의존성 적음
- **대체 관계**: `git worktree` 수동 운용을 대체한다. 모델·에이전트는 **그대로 두고** 그 아래만 바꾼다 — **도입 리스크가 구조적으로 낮다**
- **허와 실**: 최상급 표현을 걷어내면 **"worktree 수명주기 자동화"** 다. 새로운 개념이 아니라 **기존 git 기능의 에이전트향 래핑**이며, 가치는 거기서 나온다
- **6개월 영향력**: 에이전트 동시 실행이 기본이 되면 이 층은 **표준 인프라**가 된다

> [!action] 실행 항목
> **설치 후 에이전트 2개 병렬 실행으로 실측할 것.** 명령 3개라 학습 비용이 낮고, 안 맞으면 버리면 된다 — **검증 비용이 가장 싼 후보다.**

## 관련 페이지
- [[atlas-source-control]] — 같은 배치, 같은 "에이전트 아래 계층", Rust, 인접 문제(버전관리)
- [[pi-agent-harness]] — 에이전트 런타임 계층
- [[firstmate]] — 볼트 기존 "모델 위 계층" 계열
- [[한정어-탈락]] — 분모 없는 최상급
- [[ai-news]]

## 원본
- 출처: https://github.com/max-sixty/worktrunk
- 검증: GitHub API 실호출(2026-09-16). ★+2 · fork 272 · topics 6개 대조
- 신뢰도: ⭐⭐
