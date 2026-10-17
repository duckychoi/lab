---
title: FDE-Gym — 요구사항이 명시되지 않은 납품 과제 벤치마크 (정보를 다 얻어도 못 한다)
type: source
domain: ai-news
tags: [ai-news, benchmark, agent, delivery, requirements, stakeholder, 정보수집한계, 납품]
created: 2026-10-17
updated: 2026-10-17
sources: []
reliability: high
---

# FDE-Gym: The Last Mile of AI Delivery

**arXiv**: 2610.22350 · **HF**: https://huggingface.co/papers/2610.22350
**upvote**: **281** (2026-10-17 실측 · 수집기 280 대비 +1 · HF 데일리페이퍼 10-16 목록 5위)
**저자**: **26인** · published 2026-10-15
**코드**: https://github.com/deeplethe/fde-gym · **프로젝트**: https://fde-gym.com/paper
**신뢰도**: ⭐⭐⭐

> [!insight] 🏆🏆 핵심 인사이트 — **기존 에이전트 벤치마크는 "문제가 주어진 상태"를 재고 있었다**
> 저자 진단: 기존 벤치마크는 *"well-specified tasks defined by issue reports, specifications, or task tickets"* 를 푼다. 실제 고객 납품은 다르다 — FDE(forward-deployed engineer)는 **모호한 요구를 명확화하고, 살아 있는 시스템에서 일하고, 적히지 않은 제약을 캐내야** 한다.
> ⇒ 🎯 **문제 정의 자체가 과제의 일부인 벤치마크다.** 95개 납품 과제 · 20개 고객 시나리오 · **18개 산업** · 각 과제를 **업계 전문가가 실제 납품 프로젝트에서 각색**했다.
> ⇒ 채점이 특이하다: **고객 자신의 성공 지표 개선분**을 0(무변화)~1(레퍼런스 해법)로 정규화하고, **이해관계자 상호작용(메시지·시행·대기시간)에 감점**을 준다 ⇒ **"물어보면 깎인다"** — 현실의 비용 구조를 넣었다.

## 측정 (초록 전문 교차검증 완료)

7개 제공사 **13개 모델 구성** 평가. 현실 설정(적히지 않은 제약을 스스로 발견해야 하는 조건):

- **최고 구성 평균 FDE-Gym 점수 0.56**
- 🔴 **95건 중 14건만 해결**(0.8 이상 + 무사고)
- 주 병목: *"Discovering unstated constraints is the primary bottleneck"* — 명시적 안내 없이 캐내야 하면 성능이 급락

> [!warning] 🏆🏆🏆 저자가 "정보수집 부족" 설명을 스스로 기각했다 — 이게 이 논문의 핵심 수치다
> *"Yet **information discovery alone does not account for the gap**: even on the **23 tasks where the best configuration obtains every key fact from stakeholders**, it reaches a normalized business uplift of 0.8 or above on only **10**."*
> ⇒ 🔴 **핵심 사실을 전부 얻은 23건에서도 성공은 10건(43.5%)** 이다.
> ⇒ ⚖️ **따라서 병목은 "묻지 않아서"가 아니다.** 정보를 다 가진 상태에서도 **56.5%가 실패**한다 ⇒ 남은 결손은 **정보 → 작동하는 해법으로의 변환** 단계에 있다.
> 🎯 **이것이 이 논문이 다른 벤치마크와 갈리는 지점이다**: 대부분의 벤치마크는 실패를 하나의 수치로 남기는데, 이 논문은 **실패를 "못 물어봄"과 "묻고도 못 함"으로 분해**하고 후자가 더 크다는 걸 보였다 → [[복합지표-분해]] 벤더 자발 실행 사례.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — upvote 281 · **저자 26인**(금일 수집 논문 중 최다) · githubRepo + projectPage 실존 · 업계 전문가 각색 · **인간 연습 플랫폼 동시 운영**(*"An online platform lets humans practice FDE skills under the same grading criteria"*) ⇒ 🏆 **인간 기준선을 수집할 설계가 들어 있다**(단 초록에 인간 점수는 **없다**).
- **즉시 활용**: **NO(직접) / YES(간접)** — 벤치마크 자체를 돌릴 일은 없다. 🏆 **그러나 채점 설계가 그대로 쓰인다**: "요구를 캐묻는 행위에 감점" + "고객 자신의 지표로 채점"은 **내가 에이전트에 일을 맡길 때의 평가 기준**으로 이전 가능하다.
- **6개월 영향력**: 에이전트 평가의 축을 **"명세된 과제 해결률"에서 "명세되지 않은 과제 납품률"로** 옮긴다. 최고가 0.56 / 95건 중 14건이면 **현재 모델은 이 축에서 초기 단계**다 ⇒ 에이전트 자동화 기대치를 교정하는 수치다.
- **대체 관계**: SWE-bench 류(이슈가 주어짐) 를 **대체가 아니라 보완**한다 — 같은 모델이 전자에서 높고 후자에서 0.56 이면 **두 수치가 다른 것을 재는 것**이다.
- **허와 실**: 🏆 **과장이 없다** — 자기 벤치마크의 최고 점수가 낮다는 것을 헤드라인으로 적었다(*"The Last Mile"*). 🔴 **실**: 시뮬레이션 환경 + **스크립트된 이해관계자**이므로 실제 고객의 비일관성·정치는 재지 않는다(저자도 *"simulated"* 로 명시).
- **액션**: 읽기 전용 — **23→10 분해 수치**를 에이전트 위임 판단 기준으로 메모. 우선순위 중간.

> [!question] 미해결
> ① **인간 FDE 점수 미공시** — 플랫폼은 있는데 초록에 인간 기준선이 없다. 0.56 이 높은지 낮은지 판정 불가.
> ② 13개 구성 / 7개 제공사 **명단 미공시**(초록).
> ③ *"with no incident"* 의 incident 정의 미확인.

## 관련 페이지
- [[복합지표-분해]] ← 실패를 2축으로 분해한 벤더 자발 사례
- [[벤치마크-외부축]]
- [[에이전트-평가-벤치마크]]
- [[OpenGCUA]] ← 같은 10-16 목록 · 벤치마크 밖 축을 저자가 직접 적은 동형 사례
- [[하네스-설계-경험칙]]

## 원본
- 출처: https://huggingface.co/papers/2610.22350 (arXiv 2610.22350)
- 열어 본 것: HF papers API(초록 전문 · upvote 281 · 저자 26 · githubRepo · projectPage). arXiv API 빈 응답 → HF API 대체.
- 관측: 2026-10-17T09:12Z (18:12 KST)
- 신뢰도: ⭐⭐⭐
