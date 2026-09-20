---
title: "mem0 — 볼트가 8개월간 페이지 없이 '베이스라인'으로만 써 온 본체"
type: source
domain: local-llm
tags: [local-llm, agent-memory, github, ai-news, 본체-누락, 표-부분인용, 스킬-배급]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# mem0

> [!insight] 🎯 핵심 인사이트 — **볼트는 이 레포를 자(尺)로 써 왔고, 자를 잰 적이 없다**
> 볼트의 mem0 언급은 지금까지 **전부 남의 논문 속 베이스라인**이었다:
> - [[VoiceMem]]: *"top-5 검색으로 **Mem0의 top-200** 보다 약 30점 높다"* — 볼트 [[에이전트-메모리-레이어]] 의 대표 수치
> - [[TencentDB-Agent-Memory]]: *"mem0·cognee·claude-mem류 메모리 레이어와 경쟁"*
>
> 🔴 **즉 ★65,688 · 3년 3개월 된 이 축의 기준점에 볼트 페이지가 없었다.** [[에이전트-메모리-레이어]] 프론트매터의 `sources:` 7건(cognee·claude-mem·openai-agents-python·Agent-Native-Memory-System·OpenViking·apache-maka·Recuris) 어디에도 없다.
> 📌 **[[browser-use]](파생 2건을 먼저 잡고 본체를 10개월 놓침) · [[HuggingFace]](1,043소스 쌓는 동안 페이지 없음) 에 이은 세 번째 본체 누락**이고, 이번 것이 가장 비싸다 — **앞의 둘은 "없었다"로 끝나지만 이건 볼트가 그 위에 수치를 올려 뒀다.**

> [!warning] 🔴 그래서 볼트가 실제로 대가를 치렀다 — **VoiceMem 30점 우위의 분모가 둘이다**
> README 47~54행 원문:
> > *"Single-pass retrieval (one call, no agentic loops) at a **top_200 retrieval budget**. ... **Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK**; open-source users should expect directionally similar gains but **not identical numbers**."*
>
> ✅ **좋은 소식**: `top_200` 은 **Mem0 자신이 공표한 운용점**이다 — [[VoiceMem]] 이 top-200을 비교 조건으로 고른 것은 **자의적 불리 설정이 아니었다.** 볼트가 확인 못 했던 것이 확인됐다.
> 🔴 **나쁜 소식**: 그 점수는 **매니지드 플랫폼**의 것이다. VoiceMem이 OSS SDK를 돌렸다면 **더 약한 Mem0를 이긴 것**이고, 플랫폼을 썼다면 강한 쪽을 이긴 것이다. **볼트는 어느 쪽인지 모르는 채 "약 30점 우위"를 8개월간 인용해 왔다.**
> → **[[VoiceMem]] 과 [[에이전트-메모리-레이어]] 에 이 조건부를 병기해야 한다.**

> [!warning] 🔴 수집기 [[표-부분인용]] — **4행 표에서 2행만 왔고, 빠진 행이 유일한 하락 신호다**
> README 벤치 표는 **4행**이다:
> | Benchmark | Old | New | Tokens | Latency p50 |
> | LoCoMo | 71.4 | **92.5** | 7.0K | 0.88s |
> | LongMemEval | 67.8 | **94.4** | 6.8K | 1.09s |
> | BEAM (1M) | — | **64.1** | 6.7K | 1.00s |
> | BEAM (10M) | — | **48.6** | 6.9K | 1.05s |
>
> 수집기는 **LoCoMo·BEAM(1M) 2행**만 옮겼다. 빠진 둘 중:
> - **LongMemEval 67.8→94.4(+27)** 는 LoCoMo보다 **더 큰 개선**이다 — 유리한 쪽인데도 누락됐다.
> - 🎯 **BEAM 1M 64.1 → 10M 48.6 = −15.5.** **규모가 10배가 되면 15.5점이 무너진다.** 표 안에서 **유일하게 방향이 아래인 행**이고, 이것만이 *"이 방법이 어디서 깨지는가"* 를 말한다.
> 📌 [[표-부분인용]] 의 정의 그대로다 — *"몇 점을 읽는가가 결론의 정확도가 아니라 **종류**를 바꾼다."* 2행만 보면 "메모리 레이어가 해결됐다", 4행을 보면 "**1M까지는 되고 10M에서 진다**".

> [!note] 🎯 검사 가능한 것과 주장된 것이 서로 다른 물건이다
> README 63행: *"The **evaluation framework** is open-sourced so anyone can **reproduce the numbers**."*(github.com/mem0ai/memory-benchmarks)
> 🔴 그런데 54행이 말하듯 **점수의 주체는 비공개 매니지드 플랫폼**이다.
> → **공개된 것은 자(harness)이고, 재현 불가능한 것은 피측정물(system under test)이다.** *"anyone can reproduce"* 는 **하네스에 대해서만 참**이다.
> 📌 [[검사가능성-공사]] 의 변종 — 칸은 만들었는데 **칸 안의 물건이 닫혀 있다.**

> [!insight] 📌 부수 발견 — **메모리 회사가 스킬을 배급한다**
> README 189·192행: `npx skills add https://github.com/mem0ai/mem0 --skill mem0-oss-to-platform` · `/mem0-integrate` · `/mem0-test-integration` · `/mem0-oss-to-platform`
> 🎯 **스킬 하나가 문자 그대로 "오픈소스 → 유료 플랫폼 이전"이다.** [[Vercel]](vercel-skills ★31,337 배급층) · [[higgsfield-repo]](skills ★1,069) · [[SnailSploit]](Claude-Red) 에 이어 **스킬 배급 축의 네 번째 사례**이자, **상용 퍼널을 에이전트 스킬로 출하한 첫 사례**다.

> [!note] 📌 볼트 실측 (2026-09-20, GitHub API)
> ★**65,688**(raw **완전일치**) · fork **7,713** · **Apache-2.0** · Python · created **2023-06-20**(3년 3개월) · pushed 2026-09-19 · archived false
> **open issues 759** — 수집기 분해(이슈 322 / PR 437) **합계 정확히 일치**. **PR:이슈 = 1.36:1 = 병합 병목형**([[TensorRT-LLM]] 1.52:1 과 동형, [[docling]] 0.16:1 과 반대).
> `topics` 14개 · **fork:★ = 1:8.5** — 프레임워크 대역([[FastVideo]] 1:9.6과 유사).

## 도메인별 추출 (local-llm)

- **실용성 판단**: 배포 3경로(`pip install mem0ai` OSS · `docker compose up` 셀프호스트 · 매니지드). 🔴 **셀프호스트는 기본 인증 ON**(`ADMIN_API_KEY` 필요) — 로컬 실험에도 설정이 든다.
- **메모리 아키텍처**: 볼트 4분류(RAG / KV / 압축 / 외부DB) 중 **외부DB + 엔티티 링킹**. README 59행: *"entities are extracted, embedded, and **linked across memories** for retrieval boosting"* — 순수 벡터 검색이 아니라 **그래프 성분**이 있다.
- **Hermes 적용**: 🔴 **지금 당장은 NO.** 근거가 나왔다 — **BEAM 10M에서 48.6**. [[Hermes]] 장기 세션이 노리는 지점이 정확히 롱스케일이고, **이 레포의 자체 표가 거기서 15.5점을 잃는다고 적고 있다.**
- **트레이드오프**: 토큰 6.7~7.0K · p50 지연 0.88~1.09s — **표가 정확도·토큰·지연을 한 줄에 같이 준다.** 🎯 이건 칭찬할 점이다: 볼트가 다른 소스에서 늘 없다고 적는 세 번째 열(지연)이 여기 있다.
- **오픈소스 구현체**: 본체 + `mem0ai/memory-benchmarks`(평가 하네스) 분리 공개.

> [!action] 당장 할 것
> 1. **[[VoiceMem]]·[[에이전트-메모리-레이어]] 에 "Mem0 top-200은 매니지드 플랫폼 수치" 조건부를 단다** — 이미 반영했다(아래 관련 페이지 참조).
> 2. `mem0ai/memory-benchmarks` 로 **OSS SDK를 직접 돌려 LoCoMo를 재는 것**이 8개월 묵은 애매함을 끝내는 유일한 방법이다. 하네스가 공개돼 있으므로 **가능하다.**

> [!question] 미해결 질문
> OSS SDK와 매니지드 플랫폼의 **점수 차가 얼마인가** — README는 *"directionally similar but not identical"* 라고만 한다. **숫자가 없다.** 이 값이 나오기 전까지 볼트의 모든 "vs Mem0" 비교는 **±미상**이다.

## 관련 페이지
- [[에이전트-메모리-레이어]]
- [[VoiceMem]]
- [[TencentDB-Agent-Memory]]
- [[표-부분인용]]
- [[검사가능성-공사]]
- [[browser-use]]
- [[HuggingFace]]
- [[docling]]
- [[PageIndex]]
- [[Hermes]]
- [[local-llm]]

## 원본
- 출처: https://github.com/mem0ai/mem0
- 볼트 실측(2026-09-20, GitHub API): ★**65,688**(raw 완전일치) · fork 7,713 · **Apache-2.0** · Python · open issues **759**(이슈 322/PR 437 합계 일치) · created 2023-06-20T08:58:36Z · pushed 2026-09-19T01:14:39Z · topics 14 · homepage mem0.ai
- 수치 출처: README 47~54행 표(4행) · 63행 평가 하네스 · 189·192행 스킬 — **전부 README 원문 실열람**
- raw 대비: 볼트 추가 = **본체 누락 3번째 사례 + 그 대가(VoiceMem 분모 미상)** · **4행 중 2행만 인용됨을 적발, 누락행이 유일한 하락 신호(BEAM 10M 48.6)** · **하네스는 공개·피측정물은 비공개** · **스킬 배급 축 4번째 + 상용 퍼널 스킬 첫 사례**
- 신뢰도: ⭐⭐ (지표 완전일치·README 자기한정 명시는 높은 점수 / **핵심 수치가 비공개 플랫폼 소산이고 OSS 격차 미공개**)
