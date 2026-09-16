---
title: Atlas — 커밋을 그것을 만든 에이전트 세션에 역링크하는 소스 컨트롤
type: source
domain: ai-news
tags: [ai-news, github, source-control, rust, agent-provenance, checkpoint, shared-memory, mcp]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: medium
---

# GitHub: pacifio/atlas — ★4,761

**URL**: https://github.com/pacifio/atlas
**지표(2026-09-16 API 실측)**: ★ **4,761** (raw 4,759 · 드리프트 **+2**) · fork **286** · Rust
생성 **2026-05-14**(4개월) · 최종 push **2026-09-16** · 당일 **+91**
`description`: *"Source control for agents. Use multiple coding agents, track their changes and query them in one place"*

> [!insight] 핵심 인사이트 — **에이전트 시대의 `git blame` 문제를 정면으로 다룬다**
> 기존 git은 *"누가 이 줄을 바꿨나"* 에 **사람 이름**을 답한다. 에이전트가 코드를 쓰면 그 답은 **무의미해진다** — 전부 같은 사람 이름이 찍히고, 실제 원인(프롬프트·툴 호출·추론)은 **터미널 스크롤백과 함께 사라진다.**
>
> Atlas는 에이전트 실행마다 체크포인트를 남기고 **커밋 → 그 커밋을 만든 세션**으로 역링크한다. 🎯 **커밋의 출처를 사람이 아니라 과정으로 재정의한다.**
> 📌 이 배치에서 가장 **구조적으로 새로운** 항목이다. [[worktrunk]] 가 *공간*(작업 디렉터리)을 분리한다면 Atlas는 *시간*(무엇이 왜 바뀌었나)을 보존한다.

> [!insight] 공유 메모리 — 축이 하나 더 있다
> Claude Code · Codex · ACP 레지스트리 에이전트를 **같은 코드베이스에 병렬 투입하고 메모리를 공유**한다.
> 🔗 [[에이전트-메모리-레이어]] 와 직접 연결된다. 다만 볼트가 확인한 것은 **README·description 수준의 기능 서술**이며, **공유 메모리의 구현 방식(무엇을 얼마나 공유하는지)은 코드로 확인하지 않았다.**

> [!warning] ⚠️ 플랫폼 제약 — Linux 지원 별도 확인 필요
> 배포 배지에 **macOS·Windows만** 명시돼 있다. Rust로 작성돼 기술적으로 Linux 빌드가 가능할 수 있으나, **공식 배포 대상에 없다는 것이 확인된 사실**이고 **"Linux에서 된다/안 된다"는 볼트가 확인하지 않았다.**
> 🔗 [[메타데이터-부재-추론]] 적용: 배지에 없다 = **미지원이 아니라 미확인.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ medium. ★·fork·언어·날짜 실측 · **당일 +91로 이 배치 유일한 명확한 일간 급상승 지표 보유**(9router·worktrunk는 주간). 생성 4개월로 이력이 짧음
- **즉시 활용**: **조건부.** Linux 사용 시 빌드 확인 선행 필요. 에이전트 1개만 쓴다면 과잉 — **2개 이상 병렬 + 사후 추적 필요**할 때 가치가 나온다
- **대체 관계**: git을 **대체하지 않고 위에 얹는다.** 기존 히스토리를 버리지 않으므로 도입·철수 비용이 낮다
- **허와 실**: `description` 이 정확하다 — **과장 표현이 없다.** 이 배치에서 [[9router]] 와 정반대 극이다
- **6개월 영향력**: 🎯 **에이전트가 쓴 코드의 감사 추적**은 규제·팀 환경에서 곧 요구사항이 된다. 이 범주 자체가 커질 가능성이 높다

> [!action] 실행 항목
> **Linux 빌드 가능 여부부터 확인.** 가능하면 [[worktrunk]] 와 **함께** 시험할 것 — 공간 분리(worktrunk) + 출처 보존(atlas)은 **상보적**이며 같은 문제(병렬 에이전트)의 다른 면이다.

## 관련 페이지
- [[worktrunk]] — 상보 관계(공간 분리 ↔ 출처 보존), 같은 배치·같은 Rust
- [[pi-agent-harness]] — 에이전트 런타임
- [[에이전트-메모리-레이어]] — 공유 메모리 축
- [[메타데이터-부재-추론]] — 배지 부재 ≠ 미지원
- [[ai-news]]

## 원본
- 출처: https://github.com/pacifio/atlas
- 검증: GitHub API 실호출(2026-09-16). ★+2 · fork 286 · topics 15개 대조
- 신뢰도: ⭐⭐
