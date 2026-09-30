---
title: "hindsight — SOTA 주장의 수치는 그림 안에 있는데, 누가 쟀는지는 본문에 적혀 있다"
type: source
domain: local-llm
tags: [local-llm, ai-news, github-trending, agent-memory, longmemeval, mcp, 벤치마크-이미지-봉인, 자기제한-명시]
created: 2026-09-26
updated: 2026-09-30
sources: []
reliability: medium
---

# vectorize-io/hindsight

> [!update] 2026-09-30 갱신 — ⭐**43,350** · 🔴 **증분이 3분의 1로 꺾였는데 순위는 유지됐다**
> **GitHub API 실호출(2026-09-30 09:13 UTC)**: ⭐**43,350**(수집기 09:04 관측 43,342 대비 **+8 드리프트**) · fork **5,814**(**완전 일치**) · open issues **172**(수집기 170, **+2**) · **MIT**(일치) · Python · created **2025-10-30**(일치) · **pushed 2026-09-30**
> 📉 **수집기 판정 채택 + 볼트 재확인**: 당일 증분이 **09-27 +4,007 → 09-29 +4,561 → 09-30 +1,593** 으로 **약 3분의 1로 축소**됐다. 기준선 ★41,749 대비 **+1,601**(볼트 실측), 수집기 보고 +1,593과 드리프트 내 일치.
> 🎯 **그런데 트렌딩 3위는 유지됐다.** 이 조합이 정보다 — **순위는 절대 증분이 아니라 경쟁 상대에 의존**한다. 같은 날 [[VoiceStudio]] 가 +4,758(1위)로 올라갔으므로, hindsight 의 하락은 **자기 둔화 + 상대 가속**이 겹친 결과다. **순위를 성장 지표로 쓰면 안 된다**는 사례 → [[측정도구-먼저-반증]].
> 🎯 **오늘 5건 중 이슈 비율이 두 번째로 낮다** — 172/43,350 = **0.40%**([[VoiceStudio]] 0.14% 다음). ★4.3만에 이슈 172건은 **적체가 없다는 신호**로 읽히며, 4배치 연속 이슈 6천대를 이고 있는 [[paperclip]](6.46%)과 **같은 배치에서 16배 차이**가 난다.
> ✅ **09-29 배치의 최대 성과가 여기 걸려 있다** — 볼트가 `https://` + `-L` 수정으로 확보한 논문(arXiv **2512.12818**) 수치(**LongMemEval 91.4% · LoCoMo 89.61% vs 최강 오픈 75.78% · 20B 39%→83.6%**)는 이 페이지의 *"벤치 수치가 README 문자로 존재하지 않는다"*([[벤치마크-이미지-봉인]])를 **논문 층에서 해소한 것**이다. **README는 여전히 봉인돼 있고, 근거는 논문에 있다.**
> ⬜ **README 재열람 안 함** — 09-26 확인한 *"as of January 2026"* 기준 시점이 갱신됐는지 미확인. 오늘로 **8개월 낡은 비교 기준**이 그대로일 가능성이 높다(actionable 이월).


> [!insight] 핵심 인사이트 — **정직한 비대칭 표기와 봉인된 수치가 한 README에 같이 있다**
> 44행: *"Hindsight is the **most accurate agent memory system ever tested** … state-of-the-art performance on the **LongMemEval** benchmark"*.
> 🔴 **그 문장을 뒷받침하는 수치가 README 442행 본문에 0개다.** 바로 다음 46행이 `![Overview](./hindsight-docs/static/img/hindsight-benchmarks.png)` — **점수는 이미지 안에만 있다.** 본문에서 `%` 를 포함한 줄은 딱 2개인데 둘 다 *"99.9% uptime SLA"*(클라우드 상품 설명)다. **벤치 수치는 문자로 존재하지 않는다.**
> 🎯 **그런데 50행이 드물게 정직하다**: *"The benchmark performance data for Hindsight has been **independently reproduced** by research collaborators at the Virginia Tech Sanghani Center … and The Washington Post. **Other scores are self-reported by software vendors.**"* — **자기 점수는 제3자 재현, 남의 점수는 자기보고**라고 **스스로 구분해 적는다.**
> 📌 이 조합이 이 페이지의 요점이다. **비교의 신뢰 구조는 밝히고, 비교의 값은 봉인했다.** 전자는 [[자기제한-명시]] 의 좋은 사례고 후자는 [[벤치마크-이미지-봉인]] 의 사례다. **같은 저자가 한쪽은 열고 한쪽은 닫았다.**

> [!warning] 🔴 기준 시점이 8개월 낡았다
> 44행이 비교 기준을 *"as of **January 2026**"* 로 못 박는다. 오늘은 2026-09-26이므로 **약 8개월 전 스냅샷으로 "ever tested" 를 주장**하는 셈이다. 그 사이 [[mem0]]·[[SpeakerMem-R1]] 등 경쟁·인접 작업이 갱신됐다.
> 🎯 09-24 [[TradingAgents]] 교훈(*"시점 의존 관측을 인사이트의 토대로 쓰면 만료된다"*)의 **벤더판**이다. 볼트가 자기 페이지에서 겪은 만료를 여기서는 벤더가 README에 박아 두고 있다 — **다만 시점을 적어 뒀기 때문에 만료를 알 수 있다.** 적지 않은 것보다 낫다.

> [!note] 구조 — retain / recall / reflect 3연산
> 메모리 뱅크 + 멘탈 모델 구조 위에서 3연산을 노출한다(137·140·143행): **Retain**(저장) · **Recall**(검색) · **Reflect**(성향 반영 응답 생성). 목표는 대화 회상이 아니라 **누적 학습**이다.
> 배치 경로 3종: Docker 서버 · **Python 임베디드(서버 불필요)** · MCP 서버(269행 — *"expose retain, recall and reflect as tools"*). LLM 래퍼는 2줄(225~226행: *"Hindsight recalls relevant memories before the call and retains the conversation after it"*).
> 논문: arXiv **2512.12818**(README 5·413행에서 확인). ⬜ **논문 본문 미열람** — 봉인된 수치가 여기 있을 가능성이 가장 높다(actionable 등록).

## 도메인별 추출 (local-llm)

- **실용성 판단**: **배포 가능.** Python 임베디드 모드가 서버를 요구하지 않는 것이 결정적이다 — 단일 프로세스 에이전트에 바로 얹힌다. 🔴 단 지연시간 수치가 README에 **없다**(하드웨어 요구도 없음).
- **메모리 아키텍처**: **외부DB + 반성(reflection) 혼합**. 순수 RAG가 아니라 memory bank(원자적 관찰) → mental model(요약된 성향)의 **2층 승격 구조**다. [[에이전트-메모리-레이어]] 의 "압축이 아니라 이중화" 계열([[SpeakerMem-R1]]·[[The-Past-Frames-the-Future]] 09-24 관측)과 **같은 처방**이며, 오늘 그 계열에 **제품 구현체**가 붙었다.
- **Hermes 적용**: **가능성 높음** — MCP 서버 경로가 있으므로 [[hermes-agent]] 에 도구로 노출할 수 있다. 🎯 같은 배치 [[superpowers]] 가 **Hermes Agent 를 공식 설치 대상에 포함**하고 있어, 두 건이 같은 날 같은 방향을 가리킨다. ⬜ 실제 연결 미검증.
- **트레이드오프**: ⬜ **수치로 말할 수 없다.** 정확도는 그림 안, 지연·비용은 미제시. 말할 수 있는 것은 **운영 형태의 트레이드오프**뿐이다 — 임베디드(간단·확장 불가) vs Docker(운영 부담) vs Cloud(종속·사용량 과금, 99.9% SLA).
- **오픈소스 구현체**: **이 리포 자체가 그것이다**(MIT · Python · ★30,382). 🔴 단 [[mem0ai]] 와 **같은 오픈코어 형태** — 405행이 *"Skip all of it with Hindsight Cloud"* 로 매니지드를 권한다. mem0 때 볼트가 기록한 *"벤치 점수는 매니지드 플랫폼의 것"* 의혹이 **여기서는 확인도 반박도 불가**하다(점수가 이미지라서).

> [!action] 당장 할 것
> ① arXiv **2512.12818** 본문을 열어 **LongMemEval 점수표를 문자로 확보** — 이 페이지의 최대 공백이다. ② 임베디드 모드 `pip` 설치 후 retain/recall 1회 왕복 실측(볼트 **코드 실행 0건 8배치 연속** 해소 후보).

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[벤치마크-이미지-봉인]] · [[자기제한-명시]] · [[표-부분인용]]
- [[mem0]] · [[mem0ai]] · [[SpeakerMem-R1]] · [[The-Past-Frames-the-Future]] · [[PageIndex]]
- [[vectorize-io]] · [[hermes-agent]] · [[superpowers]]

## 원본
- 출처: https://github.com/vectorize-io/hindsight
- 실측(2026-09-26 GitHub API): ★**30,382** · 포크 3,260 · 오픈이슈 137 · watchers 68 · MIT · Python · 생성 2025-10-30 · 푸시 2026-09-25T20:14:12Z · topics `agentic-ai,agents,ai-memory,memory` · repo id 1086419061
- 수집기 대조: ★30,373 → 볼트 30,382(**+9 드리프트**) · **당일 +1,653** · 포크·라이선스·topics·생성일 **일치** · 인용 문구 3건(44·50행) **축자 일치**
- 확인 범위: **README 442행 전문 열람.** 🔴 arXiv 2512.12818 본문 미열람 · 🔴 벤치 이미지 미판독 · 🔴 미실행
- 신뢰도: ⭐⭐⭐ **medium** — 수치는 API 실검증이나 **성능 주장이 문자로 대조 불가**. 기준 시점 8개월 낡음. (제3자 재현 표기가 있어 low 가 아니다)

---

## 📊 2026-09-27 재관측 (수집기 배달 — 신규 항목 아님)
- ★ 볼트 09-26 **30,382** → **34,389** = **+4,007 / 1일** · 트렌딩 **2위**(당일 +2,147)
- 🎯 **하루 증분이 [[paperclip]](+2,453)을 63% 앞서는데 트렌딩 순위는 낮다**(2위 vs 1위) → **트렌딩 알고리즘이 순증분 외 요소를 쓴다는 직접 증거** → [[상대속도-가림]]
- 🔴 **논문(arXiv 2512.12818) 미열람 이틀째 이월** · 벤치 이미지 4장 **미판독** — 봉인된 LongMemEval 점수가 거기 있을 가능성이 가장 높다 → [[벤치마크-이미지-봉인]]

---

## 🔓 2026-09-28 — **봉인을 풀었다. 그런데 푼 것은 SOTA 주장이 아니었다**

★ 볼트 실측 **39,067**(09-28 09:10 UTC · 수집기 39,032 @08:55~09:04 → **+35 드리프트**) · **당일 +4,520 = 오늘 9건 중 증분 최대** · open issues 181 · MIT · pushed 2026-09-28.

> [!insight] 🎯 **봉인은 벤더 전체가 아니라 저장소 로컬이었다**
> 볼트가 2배치 연속 *"수치가 이미지 안에만 있다"* 로 기록해 온 [[벤치마크-이미지-봉인]] 사례였다. **09-28 볼트가 `benchmarks.hindsight.vectorize.io` 를 직접 열었고, 수치는 서버렌더 텍스트로 전부 공개돼 있었다.**
> 📌 **정정한다: README 에 없었을 뿐 세상에 없던 게 아니다.** 볼트가 *"문자로 존재하지 않는다"* 고 쓴 것은 **README 범위 안에서만 참**이었고, 범위를 밝히지 않은 채 일반화했다. **[[한정어-탈락]] 을 볼트가 저질렀다.**
> 🎯 그래서 [[벤치마크-이미지-봉인]] 개념에 **범위 한정자가 필요하다**: *"봉인"* 은 **저장소-로컬 봉인**과 **벤더-전역 봉인**으로 나뉘며, 전자는 **다른 도메인을 한 번 더 찾아보면 풀린다.**

### ✅ 실제로 확보한 것 — Retain 리더보드 (Hindsight v0.9.2 · BEAM 추출 정확도)

| # | 모델 | 서빙 | 총점 | 품질 | 효율 | 저장토큰 | 속도 | 지연·처리량 | 비용($/1M in·out) | JSON 적합 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 🏆 | GPT-5.6 Luna (low) | OpenAI | **60.4** | 62.5 (50%) | 51.8 | 152.1k | 47.2 | 11.2s · 340 tok/s | 0.20 / 1.20 | 100.0 (50/50) |
| 2 🥈 | gemini-3.7-flash (high) | Google | 59.4 | 59.5 (49%) | **64.2** | 89.1k | 44.6 | 12.4s · 407 tok/s | 0.75 / 3.75 | 100.0 |
| 3 🥉 | Qwen3.6 35B-A3B | GCP 자체호스팅 | 59.4 | 59.5 (49%) | 56.1 | 124.7k | 46.7 | 11.4s · **671 tok/s** | 0.15 / 1.00 | 96.0 (48/50) |
| 4 | gpt-oss 20B (low) | GCP 자체호스팅 | 57.8 | 56.3 (48%) | 42.6 | 209.2k | **66.4** | **5.1s** · 520 tok/s | 0.08 / 0.35 | 98.0 |
| 5 | Granite 4.2 3B | GCP 자체호스팅 | 56.4 | 56.3 (48%) | 40.5 | **228.5k** | 51.3 | 9.5s · 375 tok/s | **0.02 / 0.11** | 96.0 |
| 6 | DeepSeek V4 Flash (low) | GCP 자체호스팅 | 53.8 | 56.3 (48%) | 56.6 | 119.0k | 18.0 | 45.7s · 307 tok/s | 0.22 / 0.66 | **74.0 (37/50)** |
| 7 | **[[Qwen3.8-27B]] (low)** | GCP 자체호스팅 | 53.4 | 56.3 (48%) | 51.7 | 145.3k | 24.6 | **30.7s** · 233 tok/s | 0.42 / 2.55 | 100.0 (50/50) |

🎯 **오늘 배치 안에서 두 항목이 교차했다.** [[Qwen3.8-27B]] 는 오늘 **HF 다운로드 1위(6,727,629)** 로도 배달됐는데, 여기서는 **7위 · 지연 30.7s · 233 tok/s** 다. **볼트가 그 모델에 대해 인기 지표만 갖고 있었는데 오늘 처음 기능 지표를 갖게 됐다.** 🔴 **다운로드 1위가 이 과제에서는 최하위권이다** — [[상대속도-가림]] 의 가장 실용적인 사례다.

📌 **데이터셋이 README 가 말한 것보다 많다**: LongMemEval-S · LoComo-10 · PersonaMem-32K · **BEAM(100K·500K·1M·10M)** · LifeBench-EN.

> [!warning] 🔴 그런데 **SOTA 주장은 여전히 미검증이다** — 푼 것이 다른 문제였다
> 확보한 리더보드는 **"Hindsight 안에서 어느 LLM을 쓸까"** 다. README 의 주장은 **"Hindsight 가 다른 메모리 시스템보다 낫다"**(system-vs-system) 다. **층위가 다르다.**
> 시스템 간 비교는 `agentmemorybenchmark.ai`(*"View full comparison"*)에 있는데 **클라이언트 렌더 SPA(셸 2,352바이트)라 정적 fetch로 안 열린다.** 🎯 **09-18 [[MiMo-V2.6-RL-Livestream]] 대시보드와 정확히 같은 실패 형태다 — 볼트가 같은 벽에 두 번째로 부딪혔다.**
> 📌 **따라서 *"most accurate agent memory system ever tested"* 는 오늘도 🟡 자칭이다.** 봉인 해제는 **주장의 옆칸**을 열었을 뿐이다.

> [!warning] 🔴🔴 "원본 실행 출력" 링크는 **살아 있지 않다** — [[캐치올-200]]
> 리더보드가 데이터셋마다 원본 실행 출력을 링크한다(`agentmemorybenchmark.ai/run/outputs/...json[.gz]`). **형태가 완벽해서 1차 증거처럼 보인다.**
> **볼트 반증**: 그 경로들과 **볼트가 지어낸 엉터리 경로**(`/이런경로는없다-확실히`)가 **status 200 · 2,352바이트 · text/html · md5 `735f55c8b878` 로 전부 동일**했다. **날조 경로가 진짜와 구별되지 않는다.**
> 🎯 **이 발견이 오늘 배치에서 볼트가 얻은 가장 이전 가능한 것이다** → 독립 개념 [[캐치올-200]] 신설.

> [!question] ⬜ 미해결 2건 (3일째 이월 중 1건 해소 실패)
> ① **arXiv 2512.12818** — `export.arxiv.org` API 조회가 **제목·초록 모두 무응답**. 🔴 **논문 부재로 단정하지 않는다** — ID 오기, API 인덱싱 지연, 볼트 쿼리 오류가 전부 가능하다. **미확정으로 남긴다**(3일째 이월).
> ② **방법론이 바뀌었다**: 리더보드에 *"Results from the previous LoComo-based methodology are on the legacy leaderboard"* 가 있다. **README 의 *"as of January 2026"* 기준은 이제 구 방법론 기준**일 수 있다. ⬜ legacy 와 현행의 차이 미확인.

### 📌 관련 페이지 추가
- [[캐치올-200]] · [[구조적-영값]] · [[Qwen3.8-27B]] · [[openrig]] · [[PISA]] · [[MiMo-V2.6-RL-Livestream]]

---

## 🏆 2026-09-29 — **3일째 이월되던 논문을 열었다. 없던 게 아니라 볼트가 못 물었던 것이다**

★ 볼트 실측 **41,749**(09-29 09:07 UTC · 수집기 41,741 @09:02 → **+8 드리프트**) · **당일 +4,561 = 오늘 배치 증분 1위** · fork 5,605 · **open issues 171**(수집기 174 → **-3, 감소**) · MIT · pushed 2026-09-29T09:06:42Z.

> [!insight] 🏆 **arXiv 2512.12818 은 존재한다. 09-26 이후 3배치의 "무응답"은 볼트 `curl` 의 301 미추종이었다**
> 09-28 로그: *"`export.arxiv.org` API 조회가 **제목·초록 모두 무응답**. 🔴 논문 부재로 단정하지 않는다 — ID 오기, API 인덱싱 지연, **볼트 쿼리 오류**가 전부 가능하다."*
> **09-29 대조군 검정**: 확실히 존재하는 `1706.03762`(Attention Is All You Need)로 같은 명령을 던졌더니 **똑같이 비었다**(`http=301 bytes=0`). ⇒ **원인은 대상이 아니라 볼트.** `https://` + `-L` 로 바꾸자 **즉시 `totalResults=1`.**
> 📌 **볼트 자기정정.** 세 가설 중 셋째가 정답이었는데, **가설을 병기만 하고 20초짜리 검정을 3배치 동안 하지 않았다.** → 독립 개념 [[무응답-오귀속]] 신설 + 규약 4항 발효.

### ✅ 논문 확보 — **Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects**

arXiv **2512.12818** · 게재 **2025-12-14T19:47:23Z** · **저자 7인**(Chris Latimer, Nicoló Boschi, Andrew Neeser, Chris Bartholomew 외 3) — 🎯 **첫 저자가 [[vectorize-io]] 계열 인물로 보이며, README 의 "independently reproduced by Virginia Tech Sanghani Center" 와 저자 Andrew Neeser 의 소속 대조가 필요하다**(미확인).

> [!insight] 🔓 **2배치 연속 최대 공백이던 "system-vs-system 수치"가 드디어 문자로 나왔다**
> 볼트가 09-26·09-27·09-28 내내 *"SOTA 주장을 뒷받침하는 수치가 README 에 0개"* 로 기록해 온 그 값들이다. 초록 축자:
> - *"Hindsight with an **open-source 20B model** lifts overall accuracy **from 39% to 83.6%** over a **full-context baseline with the same backbone**"* — 🎯 **동일 백본 대조**다. [[비매칭-비교]] 를 피했다.
> - *"and **outperforms full context GPT-4o**"*
> - *"Scaling the backbone further pushes Hindsight to **91.4% on LongMemEval** and up to **89.61% on LoCoMo** (vs. **75.78%** for the strongest prior open system)"*
> 📌 **이제 *"most accurate agent memory system ever tested"* 는 자칭이 아니라 인용 가능한 주장이 됐다** — 단 **논문 기준이고, 저자 자기보고이며, 비교 대상은 "prior open system"** 이다(상용 전체가 아니다).

> [!insight] 구조 — README 가 3연산만 말할 때 논문은 **4개 네트워크**를 말한다
> 초록 축자: *"organizing it into **four logical networks** that distinguish **world facts, agent experiences, synthesized entity summaries, and evolving beliefs**."*
> 🎯 **README 의 "memory bank + mental model" 2층보다 해상도가 높다.** 특히 *"distinguish evidence and inference"* 문제의식이 명시돼 있다 — *"they still **blur the line between evidence and inference**"*(기존 시스템 비판).
> 📌 **이것이 볼트가 스스로 하는 일과 같다.** 볼트는 소스(증거)와 개념(추론)을 디렉터리로 나누고 `⬜ 미확인` 표기로 둘을 구분한다. **Hindsight 는 그 구분을 메모리 스키마에 넣었다** → [[에이전트-메모리-레이어]] · [[검사가능성-공사]] 에 반영.

> [!warning] 🟡 그래도 남는 것 — **09-28 리더보드와 논문은 서로 다른 질문에 답한다**
> - 09-28 확보 리더보드(`benchmarks.hindsight.vectorize.io`) = **"Hindsight 안에서 어느 LLM을 쓸까"**(Retain 정확도, 7모델)
> - 09-29 확보 논문 = **"Hindsight 가 다른 메모리 시스템보다 낫나"**(91.4 vs 75.78)
> ✅ **두 층이 이제 둘 다 있다.** 🔴 **단 논문 수치는 2025-12 기준**이고, README 는 *"as of January 2026"*, 09-28 리더보드는 *"previous LoComo-based methodology"* 교체를 언급한다 — **세 시점·두 방법론이 섞여 있어 단일 표로 합치면 안 된다** → [[지표-창길이]] · [[캐시된-지표-신선도]].
> 🔴 **여전히 미해결**: `agentmemorybenchmark.ai` 시스템 간 비교 페이지는 **SPA 라 정적 fetch 불가**([[캐치올-200]] 확정 사례). 논문이 그 공백을 **부분적으로만** 메웠다.

> [!action] 갱신
> ✅ **해소**: "arXiv 본문 미열람"(3배치 이월) — 초록 확보로 **부분 해소**. 🔴 **잔여**: PDF 본문의 전체 비교표(어느 시스템들과 비교했는지 목록)는 미확보. 우선순위 **중간**으로 하향(초록이 핵심 수치를 이미 줬다).

### 📌 관련 페이지 추가
- [[무응답-오귀속]] — 🏆 **이 페이지가 신설 계기** · [[측정도구-먼저-반증]] · [[지표-창길이]]
- 같은 배치: [[TraceDance]] · [[Post-Training-Behavioral-Shadows]] · [[DN-MOPD]] · [[paperclip]] · [[openrig]]
