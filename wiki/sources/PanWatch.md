---
title: "PanWatch(盯盘侠) — TradingAgents를 버튼 하나로 태우는 자체호스팅 래퍼"
type: source
domain: ai-news
tags: [ai-news, github-trending, 금융-AI, multi-agent, self-hosted, python, trading, observability]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: high
---

# TNT-Likely/PanWatch — 프레임워크가 아니라 배포된 제품

**GitHub**: https://github.com/TNT-Likely/PanWatch
**스타수**: ⭐**1,717** (2026-09-24 볼트 실측 · 수집기 1,711 → 드리프트 **+6** · 당일 **+95**) · forks 315 · open issues 64
**언어**: Python · MIT · **created** 2026-01-23 · **pushed** 2026-09-21 · topics `a-share` `akshare` `deepseek` `fintech`

> [!insight] 핵심 인사이트
> **볼트가 [[TradingAgents]] 페이지를 가진 뒤 처음 들어오는 실사용 래퍼다.** 본체 능력은 새 모델이 아니라 **TradingAgents 9-Agent 파이프라인을 보유 종목 화면에서 버튼 하나로 태우는 것**이다 — 4종 분석가(기술/심리/뉴스/펀더멘털) → 롱숏 토론 → 리스크 심사 → PM 결정서, **3~5분에 추론 체인 1건**, 결론을 Telegram/위챗/딩톡으로 직접 푸시.
> 🎯 볼트 [[금융-AI]] 축이 그동안 **프레임워크만**([[TradingAgents]]·[[ai-hedge-fund]]·[[Vibe-Trading]]) 모아 왔다. 이건 **그 프레임워크가 제품이 되면 어떤 모양인가**의 첫 데이터 포인트다.

> [!note] 확인 범위 (볼트 실측)
> **README 272행 전문 열람**(수집기는 상단 45행만). GitHub API 실측. **TradingAgents 본체 API 교차조회**(아래 정정의 근거). 🔴 **코드 미실행** — 배포·분석 1회도 돌리지 않았다. $0.05 주장 미검증.

## README 축자 대조 — 수집기 4/4 일치

| 주장 | README 원문 위치 | 결과 |
|---|---|---|
| TradingAgents 통합 | 3행 · 36행 · 38행 (TauricResearch/TradingAgents 링크) | ✅ |
| 9-Agent 투研팀 접력 분석 | 13행 *"TradingAgents 9-Agent 投研团队接力分析 → 看多看空辩论 → 风控审查 → PM 决策书"* | ✅ |
| 3~5분 완전 추론 체인 | 13행 · 41행 *"3-5 分钟输出完整推理链"* | ✅ |
| 기본 deepseek-chat · 1회 ~$0.05 | 42행 *"默认 deepseek-chat，单次 ~$0.05，月度预算可控"* | ✅ **저자 주장** (토큰 수·단가 근거 없음) |

## 🔴 볼트 정정 — PanWatch가 인용한 TradingAgents 별수가 3.2만 틀렸다 (그리고 볼트도 틀렸다)

- **PanWatch README 38행**: TradingAgents *"(**76k+ star**)"*
- **볼트 [[TradingAgents]] 페이지 15행**: ★**96,723** (2026-08-09 수집)
- **볼트 2026-09-24 실측**: ★**108,376** · forks 20,752 · Apache-2.0

🎯 **셋이 전부 다르고 전부 낮은 쪽으로 낡았다.** PanWatch는 −32,376, 볼트는 −11,653. **10만 돌파를 볼트가 놓쳤다.**
📌 교훈: **래퍼가 인용한 본체 지표는 래퍼의 작성 시점에 얼어 있다.** 래퍼를 통해 본체를 알면 안 된다 — 본체를 직접 조회해야 한다.

> [!warning] 🔴 볼트 낡은 주장 만료 — [[TradingAgents]] "5주 정체" 관측
> 볼트 [[TradingAgents]] 페이지 20~21행은 *"최종 푸시가 **2026-07-18로 5주 이상 정체**다… 트렌딩 5위에 오른 레포가 **5주간 커밋 0**이다"* 를 **"스타를 활성도 지표로 쓸 수 없다는 볼트 누적 관측의 가장 큰 사례"** 로 세워 뒀다.
> **2026-09-24 실측 `pushed_at`: `2026-09-24T07:51:55Z` — 오늘이다.** 개발이 재개됐다.
> → **일반 규칙(★≠활성도)은 유효하나, 그 규칙의 최대 근거로 쓰인 이 사례는 만료됐다.** 낡은 주장으로 표시하고 근거를 교체해야 한다. 이번 배치에서 [[agent-browser]](★둔화 +62 vs npm 월 532만)가 **더 강한 대체 근거**를 제공한다.

## 🎯 배치 패턴 — 5개 중 4개가 관측성을 내장한다

PanWatch README **204행**: *"内建一套自建可观测体系(结构化日志 `trace_id` 贯穿 / `agent_runs` 运行表 / **TradingAgents 节点级进度与成本**),开箱即用、无需任何外部组件"* — **노드별 진행률과 비용**을 자체 수집하고 외부 컴포넌트를 요구하지 않는다(210행: TradingAgents 노드 → 하위 span).

같은 배치 교차:
- [[nasiko]] — OTel 스팬 + `gen_ai.*` 속성에서 **토큰/비용 자동 수집**
- [[agent-desktop]] — `trace read/export`, 타임라인+스크린샷을 단일 HTML로
- [[agent-browser]] — `dashboard start`(포트 4848) 라이브 뷰포트 + 명령 피드
- **PanWatch** — `trace_id` 관통 + 노드별 비용

🔴 **4/5가 "에이전트가 무엇을 했고 얼마를 썼는지"를 1급 기능으로 넣었다.** 09-17 관찰(*모델 위 계층 = 실행 통제*)에 **계측(instrumentation)** 하위축이 붙는다 → [[검사가능성-공사]]

## 도메인별 추출 (ai-news · 교차 금융-AI)

- **신뢰도**: ⭐⭐⭐ — ★1,717(당일 +95) · MIT · README 272행이 배포 절차·AI 공급자 설정·관측성까지 구체적. high.
- **즉시 활용**: 🟡 **부분 YES** — 주식 모니터링 자체는 내 관심축이 아니다. 다만 **"멀티에이전트 파이프라인을 제품 UI에 붙이고 노드별 비용을 노출하는 방식"** 은 [[reat]] 파이프라인에 그대로 베낄 수 있는 패턴이다.
- **6개월 영향력**: 중간 — TradingAgents 채택이 계속 늘면 이런 래퍼가 더 나온다. **프레임워크 → 제품 전환의 관찰 창**으로 유용.
- **대체 관계**: TradingAgents를 대체하지 않고 **감싼다**. [[ai-hedge-fund]]·[[Vibe-Trading]] 과 같은 층이 아니라 한 층 위(배포).
- **허와 실**: 실 = 실제 배포 가능한 자체호스팅 스택, A주/홍콩/미국 실시간, PWA, 3채널 푸시. 허 = **$0.05/회 · 3~5분 전부 저자 주장이고 미실행**. 수익성 주장은 아예 없다(정직한 쪽).
- **액션**: TradingAgents 노드별 비용 수집 구현부 1개 파일 읽기(중간) — 코드 미독 해소 후보.

> [!warning] ⚠️ 유보 사항
> - 🔴 **$0.05/회 미검증** — 토큰 수·모델 단가 근거 없음. deepseek-chat 단가 변동 시 무효.
> - 🔴 **실거래 성과 주장은 README에 없다**(확인함) — 과적합 경고가 필요한 종류의 주장을 저자가 안 했다. 볼트 [[TradingAgents]] 의 *"수익 주장 미검증"* 경고가 여기선 해당 없음.
> - ⬜ TNT-Likely 법인/개인 여부 미확인.

## 관련 페이지
- [[TNT-Likely]] — 제작자
- [[TradingAgents]] — 감싸는 본체 (★108,376 실측 갱신)
- [[ai-hedge-fund]] · [[Vibe-Trading]] · [[금융-AI]]
- [[nasiko]] · [[agent-desktop]] · [[agent-browser]] — 같은 배치 관측성 내장 4/5
- [[검사가능성-공사]] · [[상대속도-가림]]
- [[ai-news]]

## 원본
- 출처: https://github.com/TNT-Likely/PanWatch
- 확인 범위: **README 272행 전문** · GitHub API 실측 · TradingAgents 본체 API 교차조회 · 코드 미독·미실행
- 신뢰도: ⭐⭐⭐ (★1,717 · MIT · 당일 +95)
