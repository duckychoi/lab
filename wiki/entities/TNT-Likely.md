---
title: TNT-Likely
type: entity
domain: ai-news
tags: [ai-news, 개인개발자, python, 금융-AI, self-hosted]
created: 2026-09-24
updated: 2026-09-24
sources: [PanWatch.md]
reliability: medium
---

# TNT-Likely

[[PanWatch]](盯盘侠 · ★1,717 · Python · MIT) 제작. **[[TradingAgents]] 를 감싸 배포 가능한 제품으로 만든** 자체호스팅 AI 주식 모니터링 도구.

> [!insight] 🎯 볼트 [[금융-AI]] 축의 성격을 바꾸는 조직
> 볼트가 모아 온 금융 AI는 전부 **프레임워크**였다([[TradingAgents]]·[[ai-hedge-fund]]·[[Vibe-Trading]]). TNT-Likely는 **그 프레임워크를 제품으로 포장한 첫 사례**를 제공한다 — 보유 종목 화면의 🧠 아이콘 한 번에 9-Agent 파이프라인이 돌고 결론이 Telegram/위챗/딩톡으로 나간다.
> 📌 **프레임워크 → 제품 전환의 관찰 창.** 볼트가 [[mem0]] 에서 *"오픈코어 3경로"* 를 본 것과 달리, 여기선 **제3자가 남의 프레임워크로 제품을 만든다.**

> [!warning] 🔴 이 저자가 인용한 본체 지표가 3.2만 틀렸다 (볼트도 1.2만 틀렸다)
> PanWatch README 38행이 [[TradingAgents]] 를 *"(**76k+ star**)"* 라 소개한다. **볼트 2026-09-24 실측 ★108,376.** 볼트 자신의 기록은 96,723(08-09)이었다.
> → **래퍼가 인용한 본체 지표는 래퍼 작성 시점에 얼어 있다.** 래퍼를 통해 본체를 알면 안 된다. 볼트 규약: **본체는 직접 조회.**

## 확인된 것
- MIT 라이선스(API 실측) · Python · created 2026-01-23 · pushed 2026-09-21
- README 272행 전문 — 배포·AI 공급자 설정(OpenAI/智谱/DeepSeek/Ollama)·관측성까지
- 🎯 **자체 관측성 내장**(204·210행): `trace_id` 관통 · `agent_runs` 테이블 · **TradingAgents 노드별 진행률과 비용** · *"무외부 컴포넌트"*
- ✅ **수익 주장을 하지 않는다** — README 272행 전수에 실거래 성과·수익률 주장 없음. 볼트 [[TradingAgents]] 의 *"수익 주장 미검증"* 경고가 이 래퍼엔 해당 없음.

## ⬜ 미확인
- 개인/법인 여부·국적 미확인(중국어 README, A주 우선 지원으로 중국권 추정이나 **추정이다**).
- 다른 레포 미조회. 🔴 코드 미독·미실행 — `$0.05/회`·`3~5분` 전부 저자 주장.

## 관련 페이지
- [[PanWatch]] — 확인된 산출물
- [[TradingAgents]] — 감싸는 본체
- [[금융-AI]] · [[ai-hedge-fund]] · [[Vibe-Trading]]
- [[검사가능성-공사]] — 노드별 비용 계측
- [[ai-news]]
