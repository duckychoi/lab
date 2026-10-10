---
title: "pingdotgg — 하네스 제어면 제공 조직"
type: entity
domain: ai-news
tags: [entity, github, harness, control-plane, mobile, 자기제한]
created: 2026-10-10
updated: 2026-10-10
sources: [t3code.md]
reliability: medium
---

# pingdotgg

**GitHub**: https://github.com/pingdotgg

> [!insight] 핵심
> [[t3code]] 의 제공 조직. 자신을 *"**agent harness control surface**"* 로 직접 규정하고, 사용자 머신에 이미 설치·인증된 **코딩 에이전트 6종**(Claude Code · Codex · Cursor · Grok Build · OpenCode · Google Antigravity)을 iOS/Android·웹·Electron 에서 원격 제어한다.
> 🎯 **볼트 [[하네스-설계-축]] 에 "제어면"이라는 층 이름이 공급자 쪽에서 붙은 사례다.**

> [!insight] 🏆 모델 마진을 취하지 않는다고 명시한다
> **별도 모델 구독을 팔지 않고 기존 구독을 그대로 쓴다**고 적는다.
> 🏆 자기제한 서술도 보유: *"우리가 잘못된 방향으로 가면 포크해서 원하는 에디터를 만들 수 있게 전부 공개한다"* → [[자기제한-명시]] **2번째 사례**(10-04 [[ponytail]] 에 이어).

> [!warning] 🔴 메타데이터가 비어 있다 — [[메타데이터-부재-추론]] 신규 유형
> API `description` 이 **`null`** 이고 `topics` 가 **0개**다. 레포 성격은 **README 첫 문단에서만** 얻었다.
> 📌 같은 배치 [[e2e]] 는 **필드가 있고 부정확**했고 이쪽은 **비어 있다** ⇒ **두 유형이 동시 관측됐다.**

> [!warning] 🔴🔴 open_issues 2,499 가 ★의 9.7% 다
> **PR 1,337 > 순수이슈 1,162.**
> ⚖️ **해석을 단정하지 않는다** — 활발한 외부 기여일 수도, 미처리 적체일 수도 있고 **PR 생성일 분포를 보지 않았다.**
> 📌 대조: [[open-code-review]] 는 `open_issues` 가 ★의 **0.63%** = 본 레포의 1/15.

> [!insight] 🏆 생태계 층 구조의 1차 증거
> 같은 날 트렌딩 2위 [[claude-mem]] 이 **t3code 전용 설치 경로를 명시한다**: `npx claude-mem install --ide t3code`.
> ⇒ ⚖️ **t3code = 제어면 · claude-mem = 그 위 메모리층 · [[knowledge-work-plugins]] = 직무 묶음** ⇒ **3개 층이 2배치에 걸쳐 관측됐다.**

> [!note] 확인된 것
> - [[t3code]]: ★**25,745** · 당일 +485 · fork 6,628 · MIT · TypeScript · created **2026-02-08** · pushed 2026-10-06
> - ⚠️ **설치가 파이프-투-셸이다**: `curl -fsSL https://t3.codes/install.sh | sh` · Windows `irm … | iex`

> [!warning] 🔴 미확인
> 조직 실체·구성원·자금 출처 **미조회**(GitHub org 페이지 미열람). 호스팅·동기화 **비용 구조 미확인.**
> 🔴 **성능 수치 0개** · 제어 대상 6종 **동작 검증 0건.**

## 관련 페이지
- [[t3code]] — 주 저장소
- [[하네스-설계-축]] — "제어면" 층
- [[claude-mem]] — 상호 참조하는 상위 층
- [[자기제한-명시]] · [[메타데이터-부재-추론]]
- [[knowledge-work-plugins]] · [[e2e]] · [[ai-news]]

## 원본
- 대표 산출물: [[t3code]] (GitHub ★25,745)
- 신뢰도: ⭐⭐⭐ (저장소 메타 실측 · 조직 실체 미확인)
