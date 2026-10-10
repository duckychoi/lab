---
title: "e2e — 자연어 목표를 에이전트가 실행하는 E2E 테스트 프레임워크"
type: source
domain: ai-news
tags: [ai-news, github-trending, testing, e2e, playwright, decision-model, 메타데이터부재]
created: 2026-10-10
updated: 2026-10-10
sources: []
reliability: medium
---

# e2e — 필드가 AI 를 숨기고 본문이 드러낸다

**GitHub**: https://github.com/tester-army/e2e
**★5,334** (당일 **+1,398 = 10-06 배치 최대 증분** · **트렌딩 1위**) · fork 229 · watchers 14
**open_issues 50 = 순수이슈 13 + PR 37** · Apache-2.0 · TypeScript · created 2026-07-22 · pushed 2026-10-06
**수집일**: 2026-10-06 (볼트 처리 2026-10-10 — **4일 지연 인제스트**)

> [!insight] 핵심 인사이트
> `agent.act('…')` 로 자연어 목표를 주면 에이전트가 앱을 조작하고 `agent.assert('…')` 로 의미 수준 검증을 하되, **같은 테스트 안에서 `screen.getByRole()` 류 결정론적 locator·assertion 과 병용하도록** 설계된 테스트 러너다.
> 🎯 즉 **의미 판정과 결정론 판정을 한 파일에 공존시킨다** — [[요약자와-판정자-분리]] 의 테스트 버전이다.

> [!warning] 🔴 [[메타데이터-부재-추론]] 역방향 사례 — 필드가 AI 를 숨긴다
> `description`·`topics` 에 **AI 표기가 없다.** topics 는 `e2e`·`playwright`·`mobile` 등 7개뿐이고 AI 성격은 **README 본문과 패키지 구성에서만 확인된다**:
> - `npx e2e init` 이 **model provider 를 묻는다**
> - 패키지 `@e2e-dev/decision` = *"Decision-model executors for bounded semantic actions and assertions"*
>
> 📌 10-05 [[LTX-2.5]] `pipeline_tag` 축소기술과 **같은 구조 · 반대 방향**이다. 같은 10-06 배치에서 [[t3code]] 는 **필드 자체가 비어 있고**(description `null` · topics 0), e2e 는 **필드가 있고 부정확하다** ⇒ **두 유형이 같은 배치에서 동시에 나왔다.**

> [!insight] 🏆 배치 내부 교차 — 같은 날 HF 논문 1위 [[SearchJev]] 와 설계가 겹친다
> 양쪽 다 *"짧은 판단은 생성형 LLM 이 아니라 **전용 결정 모델**에 맡긴다"* 이고, **e2e 는 제품으로 · [[SearchJev]] 는 논문으로** 같은 분리를 한다.
> ⇒ [[대립레시피-동시도착]] 이 아니라 **동일레시피 동시도착**이다. 📌 금일(10-10) [[laya]] 가 같은 레시피의 **4건째 도착**이다.

> [!warning] 1.0 미만 자체 명시 · 텔레메트리 기본 ON
> *"APIs and config can still change between minor releases"* 라고 적는다 → [[자기제한-명시]] 계열.
> ⚠️ **텔레메트리 기본 ON**(opt-out `E2E_TELEMETRY_DISABLED=1`). 전송 항목은 커맨드·엔진·실패 위치이고 테스트/앱 내용·크리덴셜은 제외라고 적는다 — **미검증**.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — API 실측 · Apache-2.0. 🔴 **성능·정확도 수치 0개** — 에이전트가 목표를 얼마나 달성하는지에 대한 측정이 README 에 없다.
- **즉시 활용**: **부분 YES** — 볼트 테스트 스택(Vitest/Playwright)과 직접 겹친다. **결정론 locator 와 의미 assertion 을 한 파일에 쓰는 패턴은 코드 없이도 이식 가능하다.** ⚠️ 단 1.0 미만 + 텔레메트리 ON 이므로 설치는 보류.
- **6개월 영향률**: E2E 테스트에서 "셀렉터 깨짐" 비용이 의미 판정으로 흡수되면 유지보수 구조가 바뀐다. 단 **의미 판정의 오탐률이 측정되지 않아** 현재는 교환비를 알 수 없다.
- **대체 관계**: Playwright 를 **대체하지 않고 감싼다**(topics 에 `playwright` 보유).
- **허와 실**: 🔴 **AI 성격을 메타데이터에서 숨긴 것이 의도인지 누락인지 미확정.** ⚖️ 단정하지 않는다 — 결과적으로 **"AI 테스트 도구"로 검색되지 않는다**는 사실만 적는다.
- **액션**: `@e2e-dev/decision` 패키지 설명만 읽고 **결정 모델 분리 경계**를 볼트 테스트 규약과 대조한다.

> [!question] 미해결
> - 의미 assertion 의 **오탐/미탐률** 미측정(README 에 없다).
> - 텔레메트리 전송 항목 주장 **미검증**.
> - PR 37 / 순수이슈 13 = **PR 비중 74%** 의 의미 미확정.

## 관련 페이지
- [[메타데이터-부재-추론]] — 역방향 사례(필드가 숨긴다)
- [[t3code]] — 같은 배치, 필드 자체가 비어 있는 유형
- [[SearchJev]] · [[laya]] — 동일레시피 동시도착
- [[요약자와-판정자-분리]] · [[자기제한-명시]] · [[대립레시피-동시도착]]
- [[LTX-2.5]] — `pipeline_tag` 축소기술과 반대 방향
- [[tester-army]] · [[ai-news]]

## 원본
- 출처: https://github.com/tester-army/e2e
- 수집: 2026-10-06 자동수집 (ai-news) · 인제스트 2026-10-10
- 검증: GitHub API 실측 · `open_issues` 분해 50=13+37 검산 통과
- 신뢰도: ⭐⭐⭐
