---
title: "hindsight — SOTA 주장의 수치는 그림 안에 있는데, 누가 쟀는지는 본문에 적혀 있다"
type: source
domain: local-llm
tags: [local-llm, ai-news, github-trending, agent-memory, longmemeval, mcp, 벤치마크-이미지-봉인, 자기제한-명시]
created: 2026-09-26
updated: 2026-09-27
sources: []
reliability: medium
---

# vectorize-io/hindsight

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
