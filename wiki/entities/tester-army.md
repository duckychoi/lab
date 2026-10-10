---
title: "tester-army — 자연어 E2E 테스트 프레임워크 제공자"
type: entity
domain: ai-news
tags: [entity, github, testing, e2e, decision-model, 메타데이터부재]
created: 2026-10-10
updated: 2026-10-10
sources: [e2e.md]
reliability: medium
---

# tester-army

**GitHub**: https://github.com/tester-army

> [!insight] 핵심
> [[e2e]] 의 제공 조직. `agent.act('…')` / `agent.assert('…')` 로 **자연어 목표와 의미 수준 검증**을 주면서, **같은 테스트 안에서 `screen.getByRole()` 류 결정론적 locator 와 병용**하도록 설계한다.
> 🎯 즉 **의미 판정과 결정론 판정을 한 파일에 공존시킨다** → [[요약자와-판정자-분리]] 의 테스트 구현체.

> [!insight] 🏆 "짧은 판단은 전용 결정 모델에" — 동일레시피 계보의 제품 쪽
> 패키지 `@e2e-dev/decision` = *"Decision-model executors for bounded semantic actions and assertions"*
> ⇒ 같은 2026-10-06 배치 [[SearchJev]](논문)와 **같은 분리**이고, 2026-10-10 [[laya]](제품·수치 보유)가 **4건째 도착**이다.

> [!warning] 🔴 메타데이터가 AI 성격을 숨긴다 — [[메타데이터-부재-추론]] 역방향
> `description`·`topics` 에 **AI 표기가 없다**(topics 는 `e2e`·`playwright`·`mobile` 등 7개).
> AI 성격은 **README 본문과 패키지 구성에서만** 확인된다(`npx e2e init` 이 **model provider 를 묻는다**).
> ⇒ 📌 결과적으로 **"AI 테스트 도구"로 검색되지 않는다.** 의도인지 누락인지는 **단정하지 않는다.**

> [!note] 확인된 것
> - [[e2e]]: ★**5,334** · 당일 **+1,398 = 2026-10-06 배치 최대 증분 · 트렌딩 1위** · fork 229 · Apache-2.0 · TypeScript · created **2026-07-22**
> - `open_issues` 50 = 순수이슈 13 + PR 37(PR 비중 74%)
> - ⚠️ **1.0 미만 자체 명시**: *"APIs and config can still change between minor releases"* → [[자기제한-명시]] 계열
> - ⚠️ **텔레메트리 기본 ON**(opt-out `E2E_TELEMETRY_DISABLED=1`) — 전송 항목 주장은 **미검증**

> [!warning] 🔴 미확인
> 조직 실체(기업/팀/개인) · 구성원 · 자금 출처 **전부 미조회.** GitHub org 페이지 **미열람.**
> 🔴 **성능·정확도 수치 0개** — 에이전트가 목표를 얼마나 달성하는지 측정이 README 에 없다.

## 관련 페이지
- [[e2e]] — 주 저장소
- [[메타데이터-부재-추론]] — 역방향 사례
- [[SearchJev]] · [[laya]] — 동일레시피 계보
- [[요약자와-판정자-분리]] · [[자기제한-명시]] · [[ai-news]]

## 원본
- 대표 산출물: [[e2e]] (GitHub ★5,334 · 트렌딩 1위)
- 신뢰도: ⭐⭐⭐ (저장소 메타 실측 · 조직 실체 미확인)
