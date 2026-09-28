---
title: "paperclipai/paperclip — 에이전트 관리 계층이 '회사'로 모델링되기 시작했다"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-orchestration, multi-agent, governance, budget, org-chart, 계측]
created: 2026-09-26
updated: 2026-09-27
sources: []
reliability: high
---

# paperclipai/paperclip

> [!insight] 핵심 인사이트 — 관리 계층의 은유가 파이프라인에서 **법인**으로 넘어갔다
> README 33행이 자기를 이렇게 정의한다: *"**If OpenClaw is an _employee_, Paperclip is the _company_.**"* 35행은 *"orchestrates a team of AI agents **to run a business**"*, 37행은 *"Under the hood: **org charts, budgets, governance, goal alignment**, and agent coordination"*.
> 🎯 **볼트 축의 다음 칸이다.** 09-17 *"모델 위 계층 = 실행 통제"* → 09-24 *"계측(먼저 보이게, 그다음 막기)"* → 오늘 **조직화**. 순서가 일관된다: 보이게 만들고 → 막고 → **직제를 준다.**
> 사용 예시가 은유를 끝까지 민다 — 목표는 *"Build the #1 AI note-taking app to **$1M MRR**"*, 2단계는 *"**Hire the team**: CEO, CTO, engineers, designers, marketers — any bot, any provider"*(README 43~45행). **PR이 아니라 사업 목표를 관리한다**(*"Manage business goals, not pull requests"*).

> [!note] 실행하지 않고 위임한다
> Node.js 서버 + React UI이며 에이전트를 직접 구동하지 않는다 — *"**Bring your own agents**"*(35행). 지원 표기: [[OpenClaw]] · Claude Code · Codex · Cursor(53~55·71행). 편입 조건이 느슨하다: *"Any agent, any runtime, one org chart. **If it can receive a heartbeat, it's hired.**"*(105행).
> 예산은 하드 스톱이다 — *"Monthly budgets per agent. **When they hit the limit, they stop.** No runaway costs."*(119행). 09-24 배치의 [[PanWatch]] 노드별 비용·[[nasiko]] OTel 토큰 수집이 *관측*이었다면 이쪽은 **집행**이다.

> [!warning] 🔴 조정 품질·비용 절감의 정량 근거가 없다
> README 544행 전문에서 성능·절감·조정 정확도 수치 **0개**. 표는 3단계 사용 흐름(01 목표 정의 · 02 팀 고용 · 03 승인·실행)과 기능 카탈로그뿐이다.
> 🎯 **그리고 이 판정 과정에서 볼트가 도구 함정을 하나 더 찾았다** — `grep -cE "[0-9]+%"` 가 **5건을 반환**했는데 전부 HTML 표 속성(`width="33%"` 3건 · `width="50%"` 2건)이었다. **데이터는 0건이다.**
> 📌 09-24에 볼트는 *"어휘 grep은 `<img alt=>` 속성을 통과한다"*(거짓 음성)를 배웠다. 오늘은 **같은 원인(HTML 속성)이 거짓 양성을 만든다.** → [[메타데이터-부재-추론]] 에 양방향 기록.

> [!warning] 🔴 오픈이슈 5,712 — 볼트 관측 사상 최다
> 기존 최다였던 [[claude-plugins-official]] 1,035 의 **5.5배**다(오늘 동시 실측). ★85,666 대비 **watchers 421**(0.49%) — 스타 대비 구독이 극히 낮다.
> ⬜ **이슈 내용 미확인.** [[claude-plugins-official]] 때처럼 *"등록 큐"* 성격일 수 있으나 이쪽은 레지스트리가 아니라 실행 소프트웨어라 같은 해석을 적용할 수 없다. **7개월 된 레포(생성 2026-03-02)에 5,712건은 유입 규모이거나 적체이거나 둘 중 하나이고, 열어 보지 않으면 모른다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — ★85,666(GitHub API 실검증 2026-09-26) · 포크 15,285 · MIT · TypeScript · **당일 +2,109 = 트렌딩 데일리 1위** · 푸시 2026-09-26(당일). 수치 신뢰도이지 성능 신뢰도가 아니다(위 경고 참조).
- **즉시 활용**: **조건부 YES** — 셀프호스트 Node.js 서버이고 기존 에이전트를 그대로 붙인다. 🎯 사용자 상황과 맞는 조건을 README가 직접 적는다: *"You have **20 simultaneous Claude Code terminals** open and lose track of what everyone is doing"*(72행). 다만 `topics` **0개**이고 벤치가 없어 **도입 전 소규모 검증 필수**.
- **6개월 영향력**: 높음 — 다중 에이전트를 *동시 실행*이 아니라 **직제·예산으로** 다루는 형태가 표준이 되면 [[AI-에이전트-프레임워크]] 4층 분류(자산/방법론/레지스트리/진화)에 **5번째 층(조직 운영)** 이 필요해진다.
- **대체 관계**: [[superpowers]](방법론)·[[oh-my-hermes]](증거 게이트)와 경쟁이 아니라 **상위 감싸기**. superpowers가 *한 에이전트가 어떻게 일하는가*라면 paperclip은 *여러 에이전트를 누가 어떤 예산으로 부리는가*다.
- **허와 실**: 🔴 마케팅을 걷어내면 **검증된 것은 "대시보드와 예산 한도가 존재한다"까지**다. *"goal alignment"·"governance"* 가 실제로 무엇을 강제하는지는 코드 미독. **$1M MRR 예시는 기능이 아니라 서사다.**
- **액션**: ⬜ 이슈 5,712건의 성격 1차 표본 확인(등록/버그/스팸 구분) · ⬜ 예산 하드스톱이 실제로 중단시키는지 1회 실측.

> [!question] 미해결 질문
> *"If it can receive a heartbeat, it's hired"* 의 편입 인터페이스가 무엇인가? 웹훅·폴링·MCP 중 어느 것인지 README 544행에서 확정하지 못했다(기능 카탈로그 서술만).

## 관련 페이지
- [[AI-에이전트-프레임워크]] · [[에이전트-스킬]]
- [[superpowers]] · [[oh-my-hermes]] · [[PanWatch]] · [[nasiko]]
- [[paperclipai]] · [[검사가능성-공사]] · [[메타데이터-부재-추론]]

## 원본
- 출처: https://github.com/paperclipai/paperclip
- 실측(2026-09-26 GitHub API): ★**85,666** · 포크 15,285 · 오픈이슈 **5,712** · watchers 421 · MIT · TypeScript · 생성 2026-03-02 · 푸시 2026-09-26T09:03:39Z · topics **0개** · repo id 1170821064
- 수집기 대조: ★85,658 → 볼트 85,666(**+8 드리프트**, 시점 차) · 그 외 포크·라이선스·언어·생성일 **일치**
- 확인 범위: **README 544행 전문 열람.** 🔴 코드 미독 · 🔴 이슈 목록 미열람 · 🔴 미실행
- 신뢰도: ⭐⭐⭐⭐ (수치 API 실검증 · README 축자 대조 — 단 성능·절감 수치는 리포에 없음)

---

## 📊 2026-09-27 재관측 (수집기 배달 — 신규 항목 아님)
- ★ 볼트 09-26 **85,666** → **88,119** = **+2,453 / 1일** · 트렌딩 **1위**(당일 +2,608)
- 오픈이슈 **5,792** (09-26 기록 5,712 → **+80**)
- 🔴 **오픈이슈 5,712건 미열람이 이틀째 이월**이다 — 볼트 관측 사상 최다인데 성격을 모른다. 이슈비율 6.6%.
- 🎯 **트렌딩 1위인데 하루 증분은 [[hindsight]](+4,007)보다 작다** — 트렌딩 랭킹이 순증분과 일치하지 않는 반례 → [[상대속도-가림]]

---

## 📊 2026-09-28 재관측 — **이슈가 3일째 자란다**

볼트 독립 실측: **★91,180** @ 09-28 09:10 UTC (수집기 91,164 → **+16 드리프트**) · **당일 +2,401 · 트렌딩 1위** · MIT · TypeScript · created 2026-03-02 · pushed 2026-09-28.

| 관측일 | ★ | open issues | 증분 |
|---|---|---|---|
| 2026-09-26 | — | **5,792** | — |
| 2026-09-27 | — | — | +2,453 |
| **2026-09-28** | **91,180** | **5,895** | **+2,401** |

🔴 **open issues 5,792 → 5,895 = +103(2일).** 🔴 **성격은 여전히 미확인 — 볼트 한계 5번이 3일째 이월이다.** 버그인지 기능요청인지 지원질문인지 구분하지 않은 채 숫자만 3번 적었다.
📌 **판정 가능한 대조군이 오늘 생겼다**: 같은 배치 [[VoiceStudio]] 가 **★41,201 에 open issues 27**, [[openrig]] 가 **★1,256 에 51** 이다. paperclip 은 **★당 이슈 비율이 압도적으로 높다**(5,895/91,180 ≈ **6.5/1000★**, VoiceStudio ≈ **0.7/1000★** = **9.3배 차이**).

> [!question] ⬜ 이 비율 차이가 무엇의 신호인지 볼트는 모른다
> 가설 3개 — ① paperclip 이 실제로 불안정하다 ② VoiceStudio 가 이슈를 닫거나 억제한다 ③ 사용자층이 달라 보고 성향이 다르다. **셋 다 라벨 조회 한 번이면 좁혀진다.**
> 🔴 **볼트는 이 조회를 3배치 연속 미룬다.** [[캐치올-200]] 검증은 오늘 해냈는데 이건 안 했다 — **어려워서가 아니라 등록만 하고 집행하지 않았기 때문**이다.

🎯 **[[openrig]] 과 정면 경쟁 구도가 오늘 확인됐다**(같은 문제, 다른 형태: 서버+웹UI vs CLI+tmux). **★ 72배 차이가 품질 차이는 아니다** — 이슈 비율은 openrig 쪽이 낫다.

### 📌 관련 페이지 추가
- [[openrig]] · [[VoiceStudio]] · [[캐치올-200]] · [[상대속도-가림]]
