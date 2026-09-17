---
title: wshobson/agents — 하네스별 "관용적 산출물"을 원칙으로 못 박은 마켓플레이스
type: source
domain: ai-news
tags: [ai-news, github, agent-skills, marketplace, multi-harness, distribution, infrastructure]
created: 2026-09-17
updated: 2026-09-17
sources: []
reliability: medium
---

# GitHub: wshobson/agents — ★39,749

**URL**: https://github.com/wshobson/agents
**지표(2026-09-17 볼트 API 실측)**: ★ **39,749** · fork **4,235** · MIT · 생성 **2025-07-24** / 푸시 **2026-09-14** · 🔴 `topics` **20개 = 만석**
**드리프트**: raw ★39,748 → 볼트 **39,749 (+1)** · fork **4,235 완전일치**
🏗️ **상시 인프라 (신규 릴리스 아님)** — 1년 2개월차 · 당일 +41 = **상대속도 0.10%**

> [!insight] 🎯 **실제 능력은 개수가 아니라 변환 방식이다** (README 10~11행 문자 일치)
> 배지 주장(README 3~4행 볼트 실측): **94 plugins · 202 agents · 183 skills · 105 commands**
> 그런데 원칙은 개수가 아니라 이 문장이다:
> > *"One source-of-truth (`plugins/`), six target harnesses. Each harness gets **idiomatic, harness-native artifacts — not lowest-common-denominator translations**."*
>
> 🎯 **"최소공통분모 번역을 하지 않는다"** 가 설계 선언이다. 6개 하네스(Claude Code·Codex·Cursor·OpenCode·Antigravity·Copilot·Pi)로 **각각 다른 형태로** 내보낸다. 98행이 같은 문구를 반복해 원칙임을 확인시킨다.
> 📌 하네스별 능력차를 숨기지 않고 `docs/harnesses.md` **매트릭스로 노출**한다 — 능력 차이를 **문서화한 것 자체가 [[자기제한-명시]]** 형태다.

> [!insight] 🔴 **`topics` 20개 만석 — 09-16 [[omniget-재판정]] 패턴의 두 번째 확증**
> 09-16 볼트는 omniget README 주석에서 저자 진술을 찾았다: *"**GitHub allows 20 topics. The repository uses exactly these 20**"* → **AI가 없어서 topics에 AI가 없는 게 아니라 자리가 없어서 없다.**
> 🎯 **이 레포는 `topics` 가 정확히 20개다** — 볼트 API 실측. 즉 **만석 상태**이며, topics에 무엇이 빠졌든 **부재를 신호로 읽을 수 없다.**
> 📌 [[메타데이터-부재-추론]] 의 포화도 축에 **세 번째 데이터점**: 0개([[cline]]·[[security-audit-skill]]) · 7개([[Octop]]) · 9개([[oh-my-hermes]]) · **20개 만석(이 레포)**. **같은 배치 안에 전 구간이 있다.**

> [!insight] 🏗️ 상대속도가 다시 [[상대속도-가림]] 을 실증한다
> 당일 **+41 = 0.10%**. **당일 증가량 기준으로는 슬레이트 5위이지만 절대값은 1위([[security-audit-skill]] +927)의 4.4%** 다.
> 🔗 같은 배치 [[Octop]] 12.61% 과 **126배 차이**. 🎯 **★39,749라는 크기가 성장률을 분모에서 지워 버린다** — 큰 레포는 절대 증가량으로는 트렌딩에 남지만 **성장하고 있지 않다.**

> [!warning] 설치 경로가 하네스마다 다르다 — 실사용 마찰
> native registry 방식과 `clone + make generate` 방식이 갈린다. 🔴 **Antigravity·OpenCode·Pi 는 생성 트리가 gitignore** 되어 있어 **clone 후 `make generate` 필수**다.
> ⚠️ **배지 실카운트 미대조**: 94/202/183/105 를 git tree로 세지 않았다. 볼트는 [[vercel-skills]]·[[SnailSploit]] 에서 배지 대조를 해 왔으나 **이번엔 하지 않았다** — 다음 배치 숙제.
> 🔴 **성능·품질 수치 없음.** 202개 에이전트의 품질을 잴 수단이 레포에 없다 — **개수는 검증 가능하고 품질은 불가**하다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ medium. MIT · ★39,749 · 1년 2개월 운영. **감점**: 배지 실카운트 미대조 · 품질 지표 전무
- **즉시 활용**: **YES.** Claude Code는 native registry로 즉시 설치. 🎯 다만 **202개 중 무엇이 좋은지 고를 근거가 레포에 없다** → [[선택비용과-중복성]] 의 배포 층 판본
- **6개월 영향력**: 중간. 🎯 **의미는 배급 구조에 있다** — [[Vercel]] 이 스킬 패키지 매니저를 가져간 것과 **같은 자리 경쟁**이며, 이쪽은 **다중 하네스 변환**으로 차별화
- **대체 관계**: [[vercel-skills]] 와 직접 경쟁. [[agent-skills]]·[[superpowers]] 같은 개별 스킬 묶음의 **상위 유통층**
- **허와 실**: 허는 없다(개수는 사실). 🎯 **실의 한계는 "개수가 품질을 말하지 않는다"** — 202개가 20개보다 나은지 판단할 데이터가 없다
- **액션**: `docs/harnesses.md` 능력 매트릭스를 읽어 **볼트가 쓰는 하네스의 제약 확인** · 배지 실카운트 대조(다음 배치)

## 관련 페이지
- [[omniget-재판정]] — 🔴 **topics 20개 만석 패턴의 두 번째 사례**
- [[메타데이터-부재-추론]] — 포화도 전 구간(0·7·9·20)이 같은 배치에 · [[상대속도-가림]] — 126배 차이
- [[vercel-skills]] · [[agent-skills]] · [[superpowers]] · [[ECC]] · [[security-audit-skill]] — 스킬 생태
- [[Vercel]] · [[선택비용과-중복성]] · [[ai-news]]

## 원본
- 출처: https://github.com/wshobson/agents
- 검증: GitHub API 실호출(2026-09-17) · **README 191행 확인** — 수집기 인용(10~11행·3~4행 개수) **문자 일치** · 🔴 **`topics` 20개 만석 API 실측**
- 신뢰도: ⭐⭐
