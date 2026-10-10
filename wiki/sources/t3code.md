---
title: "t3code — 로컬 코딩 에이전트 6종을 모바일·웹에서 제어하는 하네스 제어면"
type: source
domain: ai-news
tags: [ai-news, github-trending, harness, control-plane, 자기제한, 메타데이터부재, mobile]
created: 2026-10-10
updated: 2026-10-10
sources: []
reliability: medium
---

# t3code — 자기를 "agent harness control surface"로 규정한다

**GitHub**: https://github.com/pingdotgg/t3code
**★25,745** (당일 +485 · **트렌딩 4위**) · fork 6,628 · watchers 68
**open_issues 2,499 = 순수이슈 1,162 + PR 1,337**(배치 최대) · MIT · TypeScript · created 2026-02-08 · pushed 2026-10-06
**수집일**: 2026-10-06 · 인제스트 2026-10-10

> [!insight] 핵심 인사이트
> 자신을 *"agent harness control surface"* 로 **직접 규정하고**, 사용자 머신에 이미 설치·인증된 **Claude Code · Codex · Cursor · Grok Build · OpenCode · Google Antigravity** 를 iOS/Android 앱·웹앱·Electron 데스크톱에서 원격 제어한다. **별도 모델 구독을 팔지 않고 기존 구독을 그대로 쓴다**고 명시한다.
> 🎯 **[[하네스-설계-축]] 에 "제어면"이라는 층 이름이 공급자 쪽에서 붙은 사례다.** 금일(10-10) [[knowledge-work-plugins]] 의 직무 묶음과 [[mattpocock-skills]] 의 스킬 단위 사이에 **이 층이 들어간다.**

> [!warning] 🔴 [[메타데이터-부재-추론]] 신규 유형 — 설명 필드 자체의 부재
> API `description` 이 **`null`** 이고 `topics` 가 **0개**다. 레포 성격은 **README 첫 문단에서만** 얻었다.
> 📌 같은 배치 [[e2e]] 는 **필드가 있고 부정확**했으나 t3code 는 **비어 있다** — **두 유형이 동시에 나왔다.** 금일 [[mattpocock-skills]] · [[knowledge-work-plugins]] 가 같은 유형으로 누적된다.

> [!warning] 🔴🔴 open_issues 2,499 가 ★의 9.7% 다
> **PR 1,337 이 순수이슈 1,162 보다 많다.**
> ⚖️ **해석을 단정하지 않는다**: 활발한 외부 기여일 수도, 미처리 적체일 수도 있으며 **PR 의 생성일 분포를 보지 않았다**(볼트 확인 필요).
> 📌 대조: 금일 [[open-code-review]] 는 `open_issues` 286 = ★의 **0.63%** = 본 레포의 **1/15**.

> [!insight] ✅ `open_issues_count` 분해 규약이 확립된 배치다
> 10-06 5개 레포 전부 `open_issues_count == 순수이슈 + PR` 검산 통과(50=13+37 · 86=25+61 · 35=0+35 · 2,499 · 213=97+116).
> ⇒ 🆕 **규약: `open_issues_count` 는 이슈+PR 합계이며 GitHub Search API `is:issue`/`is:pr` 로 분해 가능하다.** 볼트 4배치 연속 요청 항목이고 **금일(10-10)도 5/5 이행됐다.**

> [!insight] 자기제한 서술 보유
> *"우리가 잘못된 방향으로 가면 포크해서 원하는 에디터를 만들 수 있게 전부 공개한다"*
> ⇒ [[자기제한-명시]] **2번째 사례**(10-04 [[ponytail]] 에 이어). 금일 [[mattpocock-skills]] 가 3번째다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — API 실측 · MIT. 🔴 **성능 수치 0개.**
- **즉시 활용**: **조건부 — 볼트 운영과 직접 관련이 있다.** 볼트는 Telegram 경유로 에이전트를 돌리고 있고, t3code 는 **같은 문제(원격 제어면)를 앱·웹으로 푼다.** ⚠️ **설치가 파이프-투-셸이다**(`curl -fsSL https://t3.codes/install.sh | sh` · Windows `irm … | iex`) ⇒ 설치 보류, 설계만 참조.
- **6개월 영향력**: 코딩 에이전트의 **실행 위치와 제어 위치가 분리**되면 "어디서 돌리나"가 선택 축이 된다. 볼트의 Telegram 경로는 이미 이 축에 있다.
- **대체 관계**: 터미널 고정 사용을 대체한다. 모델 구독은 대체하지 않는다(명시).
- **허와 실**: 🏆 **"기존 구독을 쓴다"는 비즈니스 모델 서술이 정직하다** — 모델 마진을 취하지 않는다고 적는다. 🔴 단 **호스팅·동기화 비용 구조는 미확인.**
- **액션**: 10-06 [[claude-mem]] 이 `--ide t3code` 전용 경로를 가진 점과 교차해 **하네스 층 지도**를 그린다.

> [!insight] 🏆🏆 배치 내부 교차 — 같은 날 트렌딩 두 레포가 서로를 참조한다
> [[claude-mem]] 이 **t3code 전용 설치 경로를 명시한다**: `npx claude-mem install --ide t3code` · *"T3 Code 의 활성 provider 를 탐색해 각 provider 홈에 네이티브 플러그인 등록"*.
> ⇒ ⚖️ **하네스 생태계가 층으로 쌓이고 있다는 1차 증거**(t3code = 제어면 · claude-mem = 그 위 메모리층). 금일 [[knowledge-work-plugins]] 가 **3번째 층**으로 이 가설을 보강한다.

> [!question] 미해결
> - **PR 1,337 의 생성일 분포** 미확인 ⇒ 기여 활발 vs 적체 판정 불가.
> - 호스팅·동기화 **비용 구조** 미확인.
> - 제어 대상 6종 중 **실제 동작 검증** 0건.

## 관련 페이지
- [[하네스-설계-축]] — "제어면" 층 이름
- [[메타데이터-부재-추론]] — 신규 유형(필드 부재)
- [[자기제한-명시]] — 2번째 사례
- [[claude-mem]] — 상호 참조하는 상위 메모리층
- [[e2e]] — 같은 배치, 메타데이터 다른 유형
- [[knowledge-work-plugins]] · [[mattpocock-skills]] — 금일 층 지도
- [[지표-창길이]] · [[pingdotgg]] · [[ai-news]]

## 원본
- 출처: https://github.com/pingdotgg/t3code
- 수집: 2026-10-06 자동수집 (ai-news) · 인제스트 2026-10-10
- 검증: GitHub API 실측 · `open_issues` 분해 2,499 = 1,162 + 1,337
- 신뢰도: ⭐⭐⭐
