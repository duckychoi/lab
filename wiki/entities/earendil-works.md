---
title: earendil-works — 권한 모델 부재를 README에 먼저 적는 에이전트 하네스 조직
type: entity
domain: ai-news
tags: [entity, github, agent-harness, typescript, open-source, self-limiting]
created: 2026-09-16
updated: 2026-09-16
sources: [pi-agent-harness.md]
reliability: medium
---

# earendil-works

**대표 산출물**: [[pi-agent-harness]] (★**106,058** · TypeScript · 2025-08-09 생성 · fork 13,340)

> [!insight] 이 조직의 서명
> 🎯 **자기 제품이 담당하지 않는 것을 README 전용 섹션으로 먼저 적는다.**
> `## Permissions & Containerization`(39행) → *"Pi does not include a built-in permission system..."*(41행) → **격리 패턴 3개 제시**(43~47행).
> **경계 → 이유 → 대안**을 순서대로 놓는다. 볼트가 [[자기제한-명시]] 로 추적해 온 행동의 강한 사례다.

> [!note] 볼트 내 대비군
> - [[vxcontrol]] — 경계 절을 두지만 **같은 README에서 "Fully Autonomous"** 유지 (경계와 헤드라인이 모순)
> - [[pascalorg]] — 런타임에 스키마를 선조회해 **없으면 좁은 결과를 보고** (실행 중 자기제한)
> - **earendil-works** — 🎯 **헤드라인 자체에 과장이 없다.** `description`이 *"AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI"* 로 **기능 나열에 그친다**

> [!warning] 확인되지 않은 것
> **조직 실체(법인·구성원·자금)를 확인하지 않았다.** GitHub 조직 계정과 레포 메타데이터·README까지가 볼트 확인 범위다.
> ⚠️ 신규 기여자 이슈·PR **기본 자동 종료** 정책이 명문화돼 있다 — ★10만 규모지만 **개방형 커뮤니티 운영이 아니다.**

> [!note] `topics` 0개
> 이 조직은 pi 레포에 **topics를 하나도 달지 않았다.** AI 기능을 `description` 에만 적었다.
> 🔗 [[메타데이터-부재-추론]] — 같은 배치 [[omniget-재판정]](topics 20개 만석)과 **정반대 극**이며 **둘 다 topics가 기능을 말하지 않는다.**

## 관련 페이지
- [[pi-agent-harness]] · [[자기제한-명시]] · [[메타데이터-부재-추론]]
- [[vxcontrol]] · [[pascalorg]] — 자기제한 계열 대비군
- [[ai-news]]

---

## 🔄 2026-10-02 갱신 — **볼트 기준선 대비 드리프트 3건**

[[pi-agent-harness]] 실측: ★**111,489**(수집기 111,483 → +6) · fork **14,149** · open_issues **253** · MIT · TypeScript · **당일 푸시** · 랭크 10위

| 항목 | 볼트 기준선 | 10-02 | 차이 |
|---|---|---|---|
| ★ | 106,058 | **111,489** | **+5,431** |
| fork | 13,340 | **14,149** | **+809** |
| 패키지 | "6패키지" | **README 표 7행** | **+1**(🔴 어느 것인지 미확인) |

🔴 **수집기가 이 레포를 "신규"로 오판했다가 자기정정했다**(슬래시 grep → 볼트는 하이픈 정규명 보유) → [[정규명-우선-중복검사]].
🎯 **그 오판이 재검사를 강제하고, 재검사가 기준선 대조를 만들었다** ⇒ 📌 **[[동일대상-분리오판]] 의 비용은 중복 페이지만이 아니라 "시계열의 소실"이다.**

🏆 **운영 특징 2건**:
1. ✅ **공급망 경화 10항목 명문화** — 버전 핀 · **`min-release-age=2`**(당일 릴리스 회피) · `--ignore-scripts` · 라이프사이클 스크립트 허용목록 · `npm audit signatures`. 🎯 **[[OpenShell]] 이 런타임에서 막는 것과 대비 — 이쪽은 설치 시점에서 막는다.**
2. 🔴 ***"신규 기여자의 이슈·PR 기본 자동 닫힘"*** 정책 명시 ⇒ **`open_issues_count` 253 이 다른 레포와 같은 의미가 아니다**(분자가 정책적으로 억제됨) → [[복합지표-분해]] **유입 필터 변종**.

🎯 **권한 시스템을 의도적으로 내장하지 않고** 외부 샌드박스 3패턴(Gondolin · Docker · **[[OpenShell]]**)을 문서로 안내한다 ⇒ **같은 날 트렌딩 3위·10위가 의존 관계로 연결** → [[하네스-설계-축]].

🔴 **topics 0개**(★111,489) — 같은 날 [[ponytail]] topics 10개와 대비 → [[메타데이터-부재-추론]].
🔴 **볼트 설치·실행 0건** — 14배치 연속. **볼트가 Claude Code 기반이고 이것이 코딩 CLI 하네스인데 미실행.**

### 관련 페이지 추가
- [[pi-agent-harness]] · [[OpenShell]] — 문서가 지목 · [[ponytail]] — topics 대비
- [[정규명-우선-중복검사]] · [[복합지표-분해]] · [[하네스-설계-축]] · [[선발창-누락]]
