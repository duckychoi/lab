---
title: coreyhaines31/marketingskills — 스킬 1층이 비-코딩 직군으로 넘어간 최대 사례 (⭐47,746)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, marketing, cro, seo, growth, 1층-자산]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: high
---

# coreyhaines31/marketingskills — 마케팅 직무 절차의 스킬화

**GitHub**: https://github.com/coreyhaines31/marketingskills
**스타수**: **47,746** (2026-09-07 API 실측 · raw 표기 47,743 대비 **+3**)
**포크 7,405 · 이슈 106 · 워치 411 · 생성 2026-01-15 · 최종 push 2026-09-05 · 주 언어 JavaScript**
**라이선스**: **MIT** · topics: `claude` `codex` `marketing`

> [!insight] 핵심 인사이트
> 볼트의 [[에이전트-스킬]] **1층(자산)** 은 지금까지 사실상 **개발자 직무**의 절차만 담았다([[mattpocock-skills]]·[[ponytail]]·[[superpowers]]). 이 레포는 **CRO·카피라이팅·SEO·애널리틱스·그로스** — 코드를 짜지 않는 직무의 절차를 같은 형식으로 담아 **⭐47,746** 을 받았다. 1층이 *"개발 도구"* 가 아니라 **"직무 절차의 배포 포맷"** 이라는 것을 비-코딩 도메인에서 증명한 최대 규모 사례다.
> 볼트는 [[pm-skills]]·[[scientific-agent-skills]] 로 이미 코딩 밖 확산을 관측했지만(08-24), **4.7만 규모**는 그 관측을 *"소수 실험"* 에서 **"주류 채택"** 으로 올린다.

> [!insight] 구조적 특징 — 스킬 사이에 **의존 그래프**가 있다
> raw 기재에 따르면 `product-marketing` 스킬이 **루트**가 되어 나머지 스킬이 이를 **먼저 읽는다**. 볼트가 본 1층 자산 대부분은 **평평한 스킬 모음**이었다 — 스킬끼리 서로를 참조하지 않았다.
> 여기서는 스킬이 **DAG를 이룬다.** 이는 [[Repo0]] 의 Dual-DAG(2층 방법론)가 *알고리즘*으로 한 것을 1층 자산이 **파일 배치만으로** 흉내낸 것에 가깝다. **1층과 2층의 경계가 흐려지는 지점.**

> [!warning] 리포 안에 상업적 이해관계가 들어 있다 — 도구 추천의 중립성
> 루트에 **`partners.json`** 과 `tools/` 디렉터리가 **실재**한다(2026-09-07 GitHub contents API 실측). raw가 지적한 유료 *"Verified Partners"* 도구 통합이 **파일 수준에서 확인**된다.
> → **스킬이 도구를 추천할 때, 그 추천이 파트너십의 산물인지 판단 근거의 산물인지 구분할 방법이 사용자에게 없다.** 볼트가 [[에이전트-스킬]] 에 기록해 온 *"스킬에는 품질 보증 수단이 사실상 없다"* 는 약점이, 여기서는 **품질이 아니라 이해충돌**의 형태로 나타난다. MIT 라이선스는 **코드 재사용**을 허용할 뿐 **추천의 중립성**을 보증하지 않는다.

> [!note] 검증 인프라를 스스로 갖췄다 — 1층 자산으로는 이례적
> 루트에 **`validate-skills.sh`** 와 **`validate-skills-official.sh`** 두 개가 있다. 후자의 이름은 **공식 스펙([[agentskills]]/[[anthropics-skills]] `./spec`) 대조 검사**를 시사한다.
> 볼트가 09-04에 [[anthropics-skills]] 에서 *"볼트 스킬이 명세를 어긋나게 쓰는지 대조하라"* 는 액션을 세웠는데, **그 대조를 자동화한 스크립트가 남의 레포에 이미 있다.** 주 언어가 JavaScript로 잡힌 것도 `scripts/`·`tools/` 때문으로 보이며, *"코드 실행 없이 프롬프트만 주입"* 이라는 raw 기재는 **스킬 본문에 한해 맞고 레포 전체로는 부정확**하다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — ⭐47,746 실측·MIT·활발한 push(09-05). 단 **스킬의 효과를 재는 수치는 없다**(1층 자산 공통 결함) + **파트너 이해관계 존재**.
- **즉시 활용**: **조건부 YES.** 마케팅 업무가 있다면 그대로 쓸 수 있다. 그보다 **당장 가치 있는 건 `validate-skills-official.sh`** — 볼트의 `~/.claude/skills/` 전체를 공식 스펙에 대조하는 데 **직접 전용 가능**하다.
- **6개월 영향력**: 1층이 직무별로 분화하면, 볼트가 추적할 단위가 *"스킬 레포"* 에서 **"직무 × 스킬"** 로 바뀐다. 추적 대상이 급증한다.
- **대체 관계**: 대체 아님. [[mattpocock-skills]]·[[ponytail]] 과 **같은 층 다른 직무**. 경쟁하지 않는다.
- **허와 실**: 4.7만 스타는 **마케팅 종사자 기반의 크기**를 재는 값이지 스킬 품질의 값이 아니다. 볼트가 [[anthropics-skills]](⭐17만)에 적용한 해석 규칙을 그대로 적용한다.
- **액션**: 아래.

> [!action] 당장 할 것
> **`validate-skills-official.sh` 한 파일만 받아 읽는다.** 공식 스펙의 어떤 필드를 검사하는지 확인하고, 볼트의 `/wiki` `SKILL.md` 에 그대로 돌려본다. 09-04에 세운 *"스펙 대조"* 액션을 **직접 구현하지 않고 해소**할 수 있다.

> [!question] 미해결
> `product-marketing` 루트 의존 구조가 **명세에 있는 기능인가, 아니면 문서 관행인가.** 스펙에 스킬 간 의존 선언이 없다면 이건 *"프롬프트로 흉내낸 의존성"* 이고, 다른 하네스에서 깨진다. [[agentskills]] 스펙 확인 시 함께 볼 것.

## 관련 페이지
- [[에이전트-스킬]] · [[anthropics-skills]] · [[agentskills]] · [[mattpocock-skills]] · [[ponytail]] · [[superpowers]] · [[pm-skills]] · [[scientific-agent-skills]] · [[Repo0]] · [[humanlayer-skills]] · [[openai-skills]] · [[Claude-Code-워크플로우]]

## 원본
- 출처: https://github.com/coreyhaines31/marketingskills
- 수집: 2026-09-07 자동수집 (ai-news)
- 검증: GitHub API 실측 + 루트 contents API 실측 (2026-09-07)
- 신뢰도: ⭐⭐⭐⭐
