---
title: Pi Agent Harness — 권한 모델 부재를 README에 먼저 적는 코딩 에이전트 하네스
type: source
domain: ai-news
tags: [ai-news, github, agent-harness, typescript, monorepo, permissions, sandbox, self-limiting]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: high
---

# GitHub: earendil-works/pi — ★106,058

**URL**: https://github.com/earendil-works/pi
**지표(2026-09-16 API 실측)**: ★ **106,058** (raw 기록 106,048 · 드리프트 **+10**) · fork **13,340** · TypeScript
생성 **2025-08-09** · 최종 push **2026-09-16** · `description`: *"AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI"*
🔴 **`topics` = 0개** (빈 배열)

> [!insight] 핵심 인사이트 — **성립 조건을 제품 README에 먼저 적은 사례**
> 볼트 원문 대조 결과, README **39행에 `## Permissions & Containerization` 전용 섹션**이 있고 **41행**이 수집기 인용과 **문자 그대로 일치**한다:
> > *"Pi does not include a built-in permission system for restricting filesystem, process, network, or credential access. By default, it runs with the permissions of the user and process that launched it."*
>
> 🎯 **이것은 결함 고백이 아니라 경계 명시다.** 43~47행은 곧바로 세 가지 격리 패턴(Plain Docker · OpenShell · 별도 문서)을 제시한다 — **"우리는 이 층을 담당하지 않는다, 담당자는 당신이고 방법은 이것이다"** 를 순서대로 적는다.
> 🔗 [[자기제한-명시]] 의 강한 사례다. [[vxcontrol]] 이 `Current Capability Boundaries` 절을 두고도 **같은 README 63행에서 "Fully Autonomous"** 를 유지한 것과 대비된다 — pi는 **헤드라인과 경계가 모순되지 않는다.**

> [!insight] 🔴 **볼트 발견 — 이 배치는 `topics` 필드의 양극단을 동시에 담고 있다**
> - **pi**: `topics` **0개** · `description` 에 *"AI agent toolkit"* 명시 → **채택됨**
> - **[[omniget-재판정]]**: `topics` **20개 만석(상한)** · 어디에도 AI 없음 · README 본문엔 AI 카테고리 6개 존재 → **누락 위험**
>
> 🎯 **같은 배치, 같은 필드, 정반대 밀도, 둘 다 기능 명세가 아니었다.**
> 09-15 [[gods-eye-view]] 는 *"필드가 비어서 놓쳤다"* 는 사례였다. 이번 배치는 여기에 **"필드가 가득 차도 못 믿는다"** 를 더한다 — **밀도는 신뢰도와 무관하다.** → [[메타데이터-부재-추론]] 에 확장 등재.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ ★106,058 실측 · 1년 1개월 운영 · 당일 push 활성. **README가 자기 한계를 먼저 적는다** → high
- **즉시 활용**: **조건부 YES.** 6패키지 모노레포(통합 LLM API · 에이전트 루프 · TUI · 코딩 CLI)라 **부분 차용**이 가능하다. 단 **권한 격리를 직접 구성해야 한다** — 컨테이너 없이 로컬에서 돌리면 실행 사용자 권한 전체를 갖는다.
- **대체 관계**: 모델을 만들지 않고 **모델 위 계층**만 만든다. [[worktrunk]]·[[atlas-source-control]] 과 같은 축이나, 이쪽은 **런타임 자체**를 제공한다.
- **허와 실**: ⚠️ 신규 기여자 이슈·PR **기본 자동 종료** 정책이 명문화돼 있다 — 스타 10만 규모지만 **커뮤니티 개방형 프로젝트가 아니다.** fork 13,340 대비 기여 경로가 좁다.
- **6개월 영향력**: 에이전트 하네스가 **권한 층을 외부화**하는 방향이 굳어지면, 격리는 OS/컨테이너 책임이 된다.

> [!warning] 성립 조건
> 볼트가 확인한 것은 **README 115행 전체 + 권한 섹션 원문**이다. **코드로 권한 경계를 검증하지 않았다.** "권한 시스템이 없다"는 것은 **저자 진술이며 볼트 실측이 아니다.**

## 관련 페이지
- [[자기제한-명시]] — 경계를 헤드라인과 모순 없이 적은 사례
- [[메타데이터-부재-추론]] — `topics` 0개 극단
- [[omniget-재판정]] — `topics` 20개 만석 극단 (같은 배치 반대 사례)
- [[worktrunk]] · [[atlas-source-control]] · [[LibreChat]] — 같은 배치 "모델 위 계층"
- [[vxcontrol]] — 경계를 적고도 헤드라인이 모순된 대비 사례
- [[ai-news]]

## 원본
- 출처: https://github.com/earendil-works/pi
- 검증: GitHub API 실호출(2026-09-16) + README 115행 원문 대조. **41행 인용 문자 일치**
- 신뢰도: ⭐⭐⭐
