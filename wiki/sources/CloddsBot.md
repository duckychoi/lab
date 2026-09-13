---
title: CloddsBot — 예측시장·크립토 트레이딩 에이전트
type: source
domain: ai-news
tags: [ai-news, github-trending, trading, crypto, agent, 이해상충, 단위-불일치]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: medium
identifiers: [alsk1992/CloddsBot]
---

# CloddsBot — 예측시장·크립토 트레이딩 에이전트

**GitHub**: https://github.com/alsk1992/CloddsBot · `alsk1992/CloddsBot`
**지표(2026-09-13 API 실호출)**: ⭐**2,613**(raw와 **완전 일치**) · fork **317** · 이슈 **28** · **TypeScript** · **MIT** · 생성 **2026-01-26** · 푸시 **2026-09-12**
**증가율**: 당일 **+376 · 16.8%** — 이 배치 최고

> [!warning] 🔴 이해상충 — **스타 수를 기술 신호로 읽으면 안 된다**
> README **12행**에 **자체 토큰 주소**가 박혀 있다(실측):
> `Clodds CA: 2puc76ehVHyPXhZmDprtP2phDSFE4kzZKDT4JgAWpump` — `pump` 접미어는 **pump.fun** 발행이다.
> → **레포 인기가 토큰 가치에 직접 연결되는 구조**다. 당일 +376(16.8%)이라는 이 배치 최고 증가율을 **순수 기술 평가로 해석할 수 없다.**

> [!insight] 🎯 볼트 추가 실측 — 토큰은 **세 층 중 하나일 뿐이다**
> raw는 토큰 하나만 신고했다. README를 끝까지 읽으면 **수익화 층이 셋**이다:
> 1. **토큰**(12행) — pump.fun CA
> 2. **에이전트 마켓플레이스**(501행) — USDC 에스크로, *"Escrow releases (**95% seller, 5% platform fee**)"* → **플랫폼이 거래마다 5%를 가져간다**
> 3. **에이전트 전용 포럼**(460행) — *"only **verified Clodds instances** can register agents"* → 인간은 읽기만, **등록 권한이 이 레포에 종속**
>
> 🎯 즉 이건 "트레이딩 봇 오픈소스"가 아니라 **자체 토큰 + 수수료 + 폐쇄 등록을 갖춘 플랫폼**이다. MIT 라이선스는 코드에만 적용되고, **세 층은 코드 복제로 우회되지 않는다.** 오픈소스 표기와 실제 사업 구조가 어긋나는 사례로 기록한다.

> [!warning] 🔴 단위 불일치 — 세는 대상이 셋 다 다르다
> - 배지(20행): `skills-121+`
> - 산문(46·151행): *"**118+** trading **strategies**"*
> - GitHub description: *"1000+ **markets**"*
> - 실제 명시된 전략(315행): *"Built-in strategies: Mean Reversion, Momentum, Arbitrage, Market Making"* — **4개뿐**
>
> **스킬 ≠ 전략 ≠ 시장**이고, 레포 내 실카운트로 검증된 것은 **아무것도 없다**. [[단위-불일치]] 전형.
> 대조: 같은 배치 [[Claude-Red]] 는 배지 78/23이 실물과 정확히 일치했다.

> [!warning] 자기 스크린샷을 근거로 쓰는 배지
> 배지 `clones/14d-10.7k`(23행)의 근거는 **본인 스크린샷**(`assets/screenshots/clones-14d.jpeg`, 28행)이다.
> GitHub clone 통계는 **소유자 전용 API**라 외부 검증이 원리적으로 불가능하다. → **검증 불가 항목임을 표기하고 인용하지 않는다.**

> [!note] 마케팅 문구 제외
> 레포 설명의 *"operates autonomously ... **while you sleep**"* 은 요약에서 제외한다. 실제 구조는 **대화형 터미널 + 스케줄러**다. 메신저 21종 연동, 실행 엔진은 `ANTHROPIC_API_KEY` 필요.
> 생성 2026-01-26 · README 48행 *"Developed in **12 days**"*(Colosseum 해커톤, Solana).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐2,613이나 **토큰 이해상충 + 단위 불일치 3종 + 자기보고 배지** → **medium**. 별도 검증 없이 수치 인용 금지.
- **즉시 활용**: **NO.** 실거래 자금이 걸리고, 전략 118+는 미검증이며, 12일 개발 해커톤 산출물이다.
- **허와 실**: 걷어내면 남는 것은 **다수 거래소 어댑터 + 메신저 연동 + 스케줄러**. 이 부분은 실재한다.
- **액션**: **관찰만.** 3개월 뒤 스타 추이와 토큰 가격의 상관을 보면 [[출처표시-무력화]] 계열 데이터가 된다.

## 관련 페이지
- [[단위-불일치]] · [[출처표시-무력화]] · [[한정어-탈락]]
- [[Claude-Red]] — 같은 배치, 실카운트가 **일치한** 대조군
- [[금융-AI]]

## 원본
- 출처: https://github.com/alsk1992/CloddsBot
- 신뢰도: ⭐⭐ (API 실호출 + README 647행 전문 대조. **토큰 이해상충으로 medium 강등**)
