---
title: DeskcommCRM — WhatsApp 영업 에이전트 내장 자가호스팅 CRM (포르투갈어권)
type: source
domain: ai-news
tags: [ai-news, github-trending, crm, whatsapp, sales-agent, self-hosted, mcp, multi-tenant, localization]
created: 2026-09-12
updated: 2026-09-12
sources: []
reliability: medium
---

# DeskcommCRM (melgarafael/DeskcommCRM)

> [!insight] 핵심 인사이트 — **fork/star 비율이 이 레포의 정체를 말한다**
> ⭐**1,509**(2026-09-12 API 실호출 · raw 1,506 대비 **+3**) · fork **513** · TypeScript · **MIT** · created **2026-04-28** · pushed 2026-09-12(당일) · 이슈 **95**.
> 자기규정(README 원문): *"o Sistema Operacional de Vendas com IA, open source, pro WhatsApp"* — **AI 영업 운영체제**. 에이전트가 WhatsApp(WAHA 경유)에서 **응대·리드 검증·판매**까지 수행하고, 그 전부가 자기 서버에서 돈다. MCP 지원, 멀티테넌트, LGPD(브라질 개인정보보호법) 대응.
> 🎯 **fork 513 / star 1,509 = 1:2.94.** raw가 짚은 대로 이례적으로 높다. 볼트 비교값: 같은 배치 [[hyperresearch]] 1:10.5 · [[OpenResearch]] 1:14.0 · [[MathModelAgent]] 1:12.6 · [[WeKnora]] 1:6.96.
> → **배치 5건 중 압도적 1위**다. 스타는 "관심"이고 fork는 "내 서버에 올리려고 복제"다. 자가호스팅 CRM에서 이 비율은 **실배포 의도의 직접 신호**로 읽는 편이 타당하다.
> → 다만 반대 해석도 열어 둔다: **fork는 기여 워크플로의 부산물**일 수도 있다. 이슈 **95건**(배치 최다)이 함께 있다는 점은 *"실제로 돌리다가 막힌 사람이 많다"* 쪽을 지지한다.

> [!warning] 국내 적용 시 현지화 비용이 선행한다 — raw 판정 실측 확인
> **볼트 실측**: 루트 `README.md` 가 **포르투갈어 원본**이고(1행 `🇧🇷 Português · [🇺🇸 English](README.en.md) · [🇪🇸 Español](README.es.md)`), 영어·스페인어는 **번역본으로 분리**돼 있다. 포르투갈어 특수문자(ç/ã/õ) 포함 행 **129개**.
> → 즉 **영어가 1차 언어가 아니다.** 제품 UI·문서·프롬프트가 브라질 시장(LGPD·Nuvemshop 연동)에 맞춰져 있다.
> → raw 판정(*"문서·UI가 포르투갈어 중심이라 국내 적용 시 현지화 비용 발생"*) **정확**.

> [!note] 배경 — 이 레포가 대체하겠다고 지목한 대상
> description 원문: *"Open alternative to **Kommo, Octadesk & Intercom** for any business that sells by chat."*
> **채팅으로 파는 사업**이라는 세그먼트를 명시적으로 겨눈다. 국내로 옮기면 WhatsApp → 카카오톡 채널이고, 그 층은 이미 국내 사업자들이 점유하고 있다 — **아키텍처는 이식 가능해도 채널이 다르다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — 수치·라이선스·언어 구성 API/원문 실측. 다만 **성능·전환율 등 효과 데이터가 전무**하고, 이슈 95건의 성격(버그 vs 기대 불일치)은 **미확인**이다 → **medium**.
- **즉시 활용**: **NO.** 내 도메인(영상 SaaS·로컬 LLM·지식베이스)과 접점이 없고, 채널(WhatsApp)·법제(LGPD)·언어가 전부 다르다. 코드 재사용 가치보다 **패턴 관찰 가치**가 크다.
- **6개월 영향력**: 의미 있는 신호는 CRM이 아니라 **"에이전트가 SaaS의 기능이 아니라 SaaS 자체가 되는 형태"** 다. 기존 CRM에 AI를 붙인 게 아니라 *AI 영업 OS* 를 표방하고, 그것을 **자가호스팅 오픈소스로 배포**한다. 이 조합(에이전트 + 셀프호스팅 + 멀티테넌트)이 늘면 SaaS 구독 모델과 직접 충돌한다.
- **대체 관계**: 내 스택에서 대체하는 것 없음. 같은 배치 [[WeKnora]] 와는 **"기업용 자가호스팅 AI 제품"** 이라는 같은 범주.
- **허와 실**: *"Sistema Operacional"*(운영체제)은 마케팅이다 — 실체는 **CRM + 에이전트 런타임 + WhatsApp 게이트웨이**다. 반면 MCP 지원·멀티테넌트·LGPD는 확인 가능한 기능 항목이다.
- **액션**: 없음(관찰만). fork/star 비율을 **자가호스팅 제품의 실배포 지표**로 쓰는 관측 규칙만 볼트에 남긴다.

## 관련 페이지
- [[WeKnora]]
- [[hyperresearch]]
- [[선택비용과-중복성]]
- [[ai-news]]

## 원본
- 출처: https://github.com/melgarafael/DeskcommCRM
- GitHub API 실호출(2026-09-12): ⭐**1,509** · fork **513** · TypeScript · **MIT** · created 2026-04-28 · pushed 2026-09-12(당일) · open_issues **95** · topics `ai, ai-agents, chatbot, crm, customer-support, ecommerce, lgpd, mcp, multi-tenant, nextjs, nuvemshop, open-source`
- README 원문 실측: **32,518B**, 1행 언어 스위처 확인, 포르투갈어 특수문자 포함 행 **129개**
- raw 대비: 스타 **+3** · fork **0 드리프트**, 언어·비율 판정 **일치**
- 신뢰도: ⭐⭐ (메타 실측 / 효과 데이터 부재)
