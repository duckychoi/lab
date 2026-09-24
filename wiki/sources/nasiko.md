---
title: "Nasiko — A2A 에이전트 컨트롤 플레인 (에이전트에 진짜 API 키를 주지 않는다)"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-security, mcp-gateway, multi-agent, rust, a2a, observability, tool]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: high
---

# Nasiko-Labs/nasiko — A2A 에이전트 앞에 서는 단일 프로세스 프록시

**GitHub**: https://github.com/Nasiko-Labs/nasiko
**스타수**: ⭐**8,841** (2026-09-24 09:00 · 당일 **+288** · Rust 트렌딩) · forks 1,937 · open issues 58
**언어**: Rust · **created** 2026-02-12 · **pushed** 2026-09-14 · topics `agent-security` `mcp-gateway` `multi-agent` `llms`

> [!insight] 핵심 인사이트
> **에이전트에게 진짜 API 키를 주지 않는 것이 이 레포의 축이다.** 라우터가 에이전트에 `OPENAI_BASE_URL` + **단기 신원 토큰**만 건네고 provider·model·key는 서버에서 해석한다 — README 123행: *"No agent or log ever sees a real API key."* 🎯 볼트가 09-17에 관찰한 **"모델 위 계층 = 실행 통제"** 가 여기서 **자격증명 통제**까지 내려왔다. [[Octop]] 이 권한을 게이트했고 [[oh-my-hermes]] 가 증거를 게이트했다면, nasiko는 **키 자체를 에이전트 밖에 둔다.** 통제 대상이 *행동* 에서 *자격* 으로 이동한 첫 사례.

> [!note] 확인 범위 (볼트 실측)
> **README 742행 전문 열람** — 수집기는 상단 45행만 봤다. GitHub API `GET /repos/Nasiko-Labs/nasiko` 실측(★8,841 일치, 드리프트 0). LICENSE 파일 196행 전문 확인. 🔴 **코드 미실행** — Docker 스택(Postgres·Redis·S3/RustFS) 미구동.

## 능력 4개 — README 축자 대조

| 능력 | README 원문 위치 | 내용 |
|---|---|---|
| 3단 라우팅 | 120행 | 임베딩 유사도 shortlist → 대화맥락 rerank → **LLM 최종 선택**. *"Callers don't need to know your fleet."* |
| LLM Router | 123행 | 단기 신원 토큰 · provider/model/key 서버측 해석 |
| 전체 관측성 | 124행 | dispatch·프록시 홉마다 **실제 OTel 스팬** · 토큰/비용을 `gen_ai.*` 속성에서 자동 수집 |
| Flow guards | 125행 | **Redis 기반 cascade 제한** — depth · fan-out · 토큰예산 · 타임아웃 · 사이클 감지 |

✅ **수집기 요약 4/4 전문과 축자 일치.** 상단 45행만 보고 쓴 요약이 742행 전문 대조를 그대로 통과했다.

> [!warning] 🔴 볼트 정정 — 수집기의 라이선스 판정이 틀렸다 (그리고 볼트의 1차 판정도 틀렸다)
> 수집기: *"라이선스 **NOASSERTION**(SPDX 미식별 — 실제 조건 미확인)"*. → **틀렸다.**
> - README **738행**: *"**Apache-2.0** — see `LICENSE`"*
> - **LICENSE 파일 196행 전문**: Apache License 2.0 **원문 그대로** + 부록 고지에 `Copyright 2026 Nasiko Labs` 기입
> - GitHub API `/license`: `spdx_id: NOASSERTION`, `name: "Other"`
> 🎯 **라이선스는 Apache-2.0 이다. 탐지기가 못 읽었을 뿐이다** — 부록 고지를 채워 넣어 표준 템플릿 해시와 달라진 것이 원인으로 보인다(⬜ GitHub licensee 내부 동작 미확인).
> 📌 볼트 자신도 1차 판정에서 *"README는 Apache라는데 LICENSE가 미식별 → 표기 모순"* 으로 읽었다. **파일을 열고서야 모순이 아니라 탐지 실패임이 드러났다.** → [[메타데이터-부재-추론]] 신규 범주

> [!insight] 🎯 그 판정이 다른 페이지를 구했다 — 그리고 다른 페이지는 못 구했다
> 같은 `NOASSERTION` 을 [[treg]]([[superdesigndev]])에서도 봤고 볼트는 *"재배포 조건 불명"* 으로 기록했다. **treg LICENSE 첫 3행을 열어 보니 `tools-registry License / Copyright (c) 2026 Superdesign` — 진짜 커스텀 라이선스다.**
> → **`NOASSERTION` 은 서로 다른 두 상태를 한 값으로 접는다**: ① 커스텀·독점(treg — 조건 불명이 맞다) ② 표준 라이선스 탐지 실패(nasiko — 오경보). **파일을 열지 않으면 구분 불가.** treg 판정은 살았고 nasiko 판정은 죽었다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ★8,841(당일 +288, Rust 트렌딩) · README 742행이 실행 가능한 Docker 절차·환경변수·트러블슈팅까지 갖췄고 라이선스가 Apache-2.0으로 확정됐다. high.
- **즉시 활용**: 🟡 **조건부 YES** — 단일 에이전트에는 과하다. Postgres+Redis+S3 를 요구하므로 [[ChinameBot]] 급 단일 프로세스에는 부담. 다만 **`gen_ai.*` 속성 기반 토큰/비용 자동 수집** 패턴은 스택 없이도 베낄 수 있다.
- **6개월 영향력**: 중간~높음 — 에이전트가 여러 개로 늘면 "키를 누가 쥐는가"가 반드시 문제가 된다. 그때 이 레포의 **단기 신원 토큰** 패턴이 기본형이 될 가능성.
- **대체 관계**: MCP 게이트웨이·에이전트 프록시 축. [[Octop]](권한 게이트) 보완재이고 대체재는 아니다 — Octop은 *무엇을 할 수 있는가*, nasiko는 *무엇으로 할 수 있는가* 를 막는다.
- **허와 실**: 실 = 4대 능력 전부 README에 구체적으로 적혀 있고 아키텍처 다이어그램(149~202행)이 컴포넌트를 명시한다. 허 = **성능·지연 수치가 전문 742행에 0개**. 프록시를 한 홉 더 넣는 비용을 저자가 재지 않았다.
- **액션**: `gen_ai.*` 비용 수집 패턴만 발췌해 내 파이프라인에 적용 검토(중간). 전체 스택 도입은 에이전트 3개+ 시점까지 보류.

> [!warning] ⚠️ 유보 사항
> - **pushed 09-14 = 10일 미갱신**인데 당일 +288. [[상대속도-가림]] 패턴([[TradingAgents]]·[[mattpocock-skills]])의 재현 후보 — 단 10일은 5주와 달라 아직 "정체"라 부를 근거가 약하다.
> - **성능 오버헤드 수치 0개** — 프록시 홉 추가 지연을 저자가 보고하지 않았다(README 742행 전수 확인).
> - ⬜ Nasiko Labs 법인 실체·소속 미확인.

## 관련 페이지
- [[Nasiko-Labs]] — 제작 조직
- [[Octop]] — 권한 게이트(보완 관계)
- [[oh-my-hermes]] — 증거 게이트
- [[agent-desktop]] · [[agent-browser]] — 같은 배치 Rust 3종
- [[메타데이터-부재-추론]] — NOASSERTION 양의성
- [[treg]] — 같은 NOASSERTION, 다른 실체
- [[에이전트-웹접근]] · [[AI-에이전트-프레임워크]]
- [[ai-news]]

## 원본
- 출처: https://github.com/Nasiko-Labs/nasiko
- 확인 범위: **README 742행 전문** · GitHub API `/repos` 및 `/license` 실측 · **LICENSE 196행 전문**
- 신뢰도: ⭐⭐⭐ (★8,841 · 당일 +288 · Apache-2.0 확정)
