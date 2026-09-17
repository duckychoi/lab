---
title: cline/cline — 볼트 관측 사상 첫 ★ 음수 드리프트
type: source
domain: ai-news
tags: [ai-news, github, coding-agent, ide-extension, cli, headless, infrastructure]
created: 2026-09-17
updated: 2026-09-17
sources: []
reliability: medium
---

# GitHub: cline/cline — ★68,506

**URL**: https://github.com/cline/cline
**지표(2026-09-17 볼트 API 실측)**: ★ **68,506** · fork **7,401** · Apache-2.0 · 생성 **2024-07-06** / 푸시 **2026-09-17** · `topics` **0개**
**드리프트**: raw ★68,507 → 볼트 **68,506 = 🔴 −1**
🏗️ **상시 인프라 (신규 릴리스 아님)** — 2년 2개월차 · 당일 +112 = **상대속도 0.16%**

> [!insight] 🔴 **볼트 관측 사상 첫 음수 드리프트 — 그리고 그게 [[상대속도-가림]] 의 실증이다**
> 볼트는 09-16까지 드리프트를 *"전부 상승 또는 동일"* 로 기록해 왔다. **이 항목이 처음으로 −1 을 냈다.**
> 🎯 **크기가 문제다.** 수집기 측정 후 볼트 재호출까지 **★가 1개 줄었다** = 누군가 star를 해제했다.
> - 수집기 보고 당일 증가량: **+112** (상대속도 **0.16%**)
> - 볼트 재측정 변화: **−1**
> - 📌 **즉 이 레포의 "일간 신호"는 언스타 노이즈와 같은 자릿수 안에 있다.** +112 중 몇이 순증이고 몇이 교체인지 **일간 스냅샷으로는 분리 불가**하다.
>
> 🔗 대조군(같은 배치): [[security-audit-skill]] +23 · [[Octop]] +6 · [[oh-my-hermes]] +4 · [[wshobson-agents]] +1 — **전부 양수**. 상대속도 10.90%인 항목은 같은 시간에 **+23**을 냈다.
> 🎯 **[[상대속도-가림]] 규칙에 측정론적 근거가 추가됐다**: 상대속도가 0.2% 미만이면 **증가량 자체가 노이즈와 구분되지 않는다.** "기저 유입"이라 부르는 것이 실은 **측정 한계** 일 수 있다.

> [!insight] README가 내세우는 신규 능력 — 헤드리스 (수집기 인용 문자 일치, 47~48행)
> > *"Interactive chat or fully headless for CI/CD and scripting."*
>
> 🔴 **볼트 추가 — 수집기가 놓친 전용 섹션이 219행에 있다** ([[oh-my-hermes]] 와 동일한 누락 패턴):
> > **`## Headless CLI for CI/CD`** — *"Run Cline with zero interaction for scripting and automation. **Pipe input, get JSON output, chain commands**, integrate into CI/CD pipelines."*
>
> 🎯 **`JSON output` 이 실체다.** 대화형 에이전트를 **파이프 가능한 유닉스 도구로 만든 것** — 이것이 IDE 확장에서 SDK·CLI·데스크톱으로 배포면을 넓힌 이유다.
> 배포면(README 128행 표 확인): `apps/cli/` 가 독립 CHANGELOG를 갖는 **별도 제품**이다.

> [!warning] 🔴 능력 수치가 README 235행 전체에 없다 — 확인 불가
> SWE-bench 등 **정량 벤치마크 일절 없음**(볼트 README 235행 전수 확인). 별도 문서(`docs.cline.bot`) 확인 필요 — **볼트도 읽지 않았다.**
> ⚠️ `topics` **0개** — ★68.5k 레포가 topics를 비워 뒀다. [[메타데이터-부재-추론]] 포화도 사례 추가.
> 📌 **이 페이지의 값은 능력이 아니라 경쟁 축의 바닥면**이다 — 볼트에 [[anthropic-claude-code]]·[[openai-codex]] 가 이미 있고, 이 셋이 **같은 자리를 다르게 배포**한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ medium. Apache-2.0 · ★68,506 · 2년 운영 이력은 강하나 **자체 성능 주장·수치가 README에 전무** → 검증할 것이 없어 high로 올릴 근거가 없다
- **즉시 활용**: 🎯 **YES — 단 "에이전트"로서가 아니라 "CI 단계"로서.** `JSON output` + 파이프가 되면 기존 워크플로에 **셸 한 줄로 꽂힌다**
- **6개월 영향력**: 중간. 🔴 **상대속도 0.16%는 성장이 아니라 유지다.** 판도를 바꾸는 쪽이 아니라 **바닥이 되는 쪽**
- **대체 관계**: [[anthropic-claude-code]]·[[openai-codex]] 와 **동일 자리 경쟁**. 차별점은 모델 비종속 + IDE 출신 + Apache-2.0
- **허와 실**: 🎯 **허가 적다 — 주장을 거의 안 한다.** 벤치 없고 SOTA 문구 없다. 반면 실을 확인할 수단도 없다
- **액션**: `cline --headless` JSON 출력을 **볼트 파이프라인 후보로 실험** (수집→검증 단계 자동화)

## 관련 페이지
- [[상대속도-가림]] — 🔴 **첫 음수 드리프트 = 측정론적 근거**
- [[oh-my-hermes]] — 같은 배치 동일 독해 누락(전용 섹션을 60행 제한이 가렸다)
- [[anthropic-claude-code]] · [[openai-codex]] · [[wshobson-agents]] — 경쟁·배급 축
- [[메타데이터-부재-추론]] · [[ai-news]]

## 원본
- 출처: https://github.com/cline/cline
- 검증: GitHub API 실호출(2026-09-17) · **README 235행 전수 확인** — 수집기 인용(47~48행) **문자 일치** · 볼트 추가 인용(219·128행) · 🔴 **★ −1 드리프트 실측**
- 신뢰도: ⭐⭐
