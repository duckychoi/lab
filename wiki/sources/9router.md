---
title: 9Router — "Unlimited FREE"의 실제 의미가 무료 티어 라우팅인 LLM 게이트웨이
type: source
domain: ai-news
tags: [ai-news, github, llm-gateway, proxy, token-compression, routing, tos-grayzone, unverified-claim]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: low
---

# GitHub: decolua/9router — ★28,983

**URL**: https://github.com/decolua/9router
**지표(2026-09-16 API 실측)**: ★ **28,983** (raw 28,982 · 드리프트 **+1**) · fork **5,318** · JavaScript
생성 **2026-01-05**(8개월) · 최종 push **2026-09-10** ⚠️ **6일 전 — 이 배치 5건 중 유일하게 당일 push 아님**
⚠️ 증분 **주간 +986** — **당일 급상승 아님**

> [!warning] 🔴 헤드라인 주장 3건이 전부 검증 불가
> GitHub `description` 원문: *"**Unlimited FREE AI coding.** Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to **FREE** Claude/GPT/Gemini via 40+ providers."*
>
> **1. "Unlimited FREE" — 어휘 치환이다.**
> 무료인 것은 **모델이 아니라 라우팅 대상**이다. 9router는 **타사 무료 티어로 요청을 넘긴다.** 비용은 사라지지 않고 **프로바이더에게 이전된다.**
>
> **2. "Save 20-40% tokens" — 측정 방법론이 레포에 없다.**
> `tool_result` 본문 압축(RTK)은 실재 기능이나, **절감률 수치의 벤치마크·재현 스크립트·측정 조건이 없다.** 20%인지 40%인지, 어떤 워크로드에서인지 확인 불가.
>
> **3. 다계정 라운드로빈 = 약관 회색지대.**
> 구독 쿼터를 여러 계정으로 분산 소진시키는 기능은 **프로바이더 이용약관과 충돌할 수 있다.** 레포는 이 위험을 명시하지 않는다.

> [!insight] 🎯 이 배치의 대조 — **같은 "자기 한계", 정반대 처리**
> [[pi-agent-harness]] 는 권한 모델이 없다는 것을 **README 39~41행 전용 섹션**에 먼저 적었다.
> 9router는 **"Unlimited FREE"를 description 첫 단어로 적고** 그것이 무슨 뜻인지는 적지 않았다.
>
> 📌 **둘 다 "제품이 담당하지 않는 것"이 있다.** 차이는 **그것을 읽는 사람이 찾아야 하는가, 저자가 먼저 주는가**다.
> 🔗 [[한정어-탈락]] — 다만 이 건은 한정어가 *탈락*한 게 아니라 **처음부터 없다.** 저자가 한정어를 쓰지 않기로 선택한 경우다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⚠️ **low.** ★28,983은 실측이나 **핵심 주장 3건 전부 근거 부재** + **주간 집계** + **6일간 push 없음**
- **즉시 활용**: 🔴 **권장하지 않음.** 기능은 동작할 수 있으나 (a) 약관 위반 위험 (b) 절감률 미검증 (c) 요청이 제3자 프록시를 경유 — **코드가 프록시를 지난다**는 점이 보안상 결정적이다
- **대체 관계**: [[LibreChat]] 과 달리 **기존 CLI를 가로챈다**(Claude Code · Codex · Cursor · Cline). 대체가 아니라 **삽입**이다
- **허와 실**: 마케팅을 걷어내면 **"40+ 프로바이더 라우터 + 응답 압축 + 폴백"** 이다. 이것만으로도 유용하나, 그 설명으로는 ★29K가 안 모였을 것이다
- **6개월 영향력**: 게이트웨이 계층 자체는 남는다. **"무료" 프레이밍은 프로바이더 정책 변경 한 번에 사라진다**

> [!question] 미해결
> RTK 압축의 실제 절감률은 **직접 측정해야만** 알 수 있다. 레포가 주지 않는다.

## 관련 페이지
- [[LibreChat]] — 같은 멀티 프로바이더 축, 정직한 자기 규정 대비
- [[pi-agent-harness]] — 같은 배치, 자기 한계 처리 정반대
- [[한정어-탈락]] — 한정어가 처음부터 없는 변종
- [[ai-news]]

## 원본
- 출처: https://github.com/decolua/9router
- 검증: GitHub API 실호출(2026-09-16). ★+1 · **pushed_at 2026-09-10 확인(6일 정체)** · description 원문 대조
- 신뢰도: ⭐ (low)
