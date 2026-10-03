---
title: Beyond Memory (PoS) — 이력 보존·압축 대신 "명시적 belief 상태"를 유지하는 장기 에이전트 프레임워크
type: source
domain: local-llm
tags: [ai-news, hf-paper, agent-memory, belief-state, long-horizon, inference-time, belief-trapping, alibaba]
created: 2026-10-03
updated: 2026-10-03
sources: []
reliability: high
---

# Beyond Memory / PoS (2610.01415)

> [!insight] 핵심 인사이트
> **문제 설정이 한 줄로 서술된다** — *"에이전트가 상호작용 이력을 메모리로 조직하는 방식이 **현재 세계에 대한 일관된 이해를 보장하지 않는다**."*
> 해법 **PoS**(추론시 프레임워크)는 **현재 세계 상태 추정 + 미해결 과제 요구**를 결합한 **belief** 를 결정 컨텍스트로 삼아 **지속적으로 구성·유지**한다. 각 belief 는 *"에이전트가 아직 무엇을 알아야 하고 무엇을 해내야 하는가"* 를 **명시적으로** 만든다.
> 🎯 **[[에이전트-메모리-레이어]] 와 정면 대립이 아니라 상위 전환이다** — 저자가 스스로 *"**beyond** history retention and compression"* 의 토대라고 위치시킨다.

## 핵심 기제 — 2단계

**① 일관성 검증(consistency validation)** — belief 가 신뢰할 수 있고 실행 가능하도록 정합성을 검사한다.
**② Belief Trapping 탐지** — 정의가 명확하다: *"에이전트가 **목표를 향한 의미 있는 진전 없이 계속 행동하는 상태**"*. 과제 진행을 모니터링해 탐지한다.
**③ 맞춤 복구** — *"Recovery is then tailored to both the **trapping pattern** and the **type of unresolved task requirement**."* ⇒ **덫의 패턴과 미해결 요구의 유형 2개 축으로 복구를 분기**한다.

> [!insight] 🎯 볼트 운영과 동형인 지점 — 그리고 볼트에 없는 것
> 볼트의 `log.md` 운영은 **원문 대신 판정을 남긴다**(10-02 기록). 그것은 PoS 의 ①(상태 추정)과 동형이다.
> 🔴 **그러나 볼트에 ②가 없다.** **Belief Trapping = "진전 없이 계속 행동하는 상태"** 는 볼트의 실제 증상에 이름을 준다:
> - **코드 실행 0건 — 14배치 연속**(10-02 기준)
> - **논문 PDF 0건 — 15배치 연속**(10-02 기준)
> - `open_issues` **PR 비중 미분해 4건** — 10-02 기록에 *"🔴 10-01 에 이 분해로 5배치치 결론이 뒤집혔는데 **알면서 반복했다**"*
> ⚖️ **"알면서 반복했다"가 Belief Trapping 의 정의와 문자 그대로 일치한다 — 행동은 계속되고 진전은 없다.**
> 🏆 **그래서 이 논문이 볼트에 주는 것은 모델 기법이 아니라 자기 진단 도구다.** 그리고 **오늘 그 덫 2개가 깨졌다** — PDF 2건 열람([[Sharpening-Tax]]·[[HC-DLM]])으로 15배치 연속이 종료됐다. ⇒ 📌 **덫 탈출의 계기가 "더 노력"이 아니라 "다른 요구 유형으로 전환"이었다**(초록 대조 → PDF 획득). **PoS 의 ③(요구 유형별 복구)과 같은 모양이다.**

## 도메인별 추출 (local-llm · 에이전트 메모리)

- **실용성 판단**: 🟡 **추론시(inference-time) 프레임워크라 재학습이 불필요하다** — 채택 문턱이 낮은 쪽이다. **구현체가 실제로 공개돼 있다**(아래 참조). 🔴 **단 수치가 초록에 0개**여서 효과 크기를 모른다.
- **메모리 아키텍처**: 🆕 **RAG/KV/압축/외부DB 어디에도 안 맞는다.** 🎯 **10-02 에 [[OneStreamer]] 로 신설한 5번째 분류(자기 생성 텍스트형)와도 다르다** — OneStreamer 는 기억을 *출력*으로 만들고(되감기 없음), PoS 는 기억을 *신념 상태*로 만들고 **일관성 검사와 진전 모니터링을 붙인다**. ⇒ 📌 **[[에이전트-메모리-레이어]] 6번째 분류 신설 후보: "검증되는 상태형"** — 유일하게 **메모리가 자기 정합성을 검사받는다.**
- **Hermes/ChinameBot 적용**: 🟡 **belief = 현재 상태 + 미해결 요구** 구조는 세션 요약에 바로 얹을 수 있다. 🔴 **그러나 ②·③(trapping 탐지와 분기 복구)이 효과의 핵심이고 그 구현 세부는 초록에 없다** — 구현체를 읽어야 한다.
- **트레이드오프**: 🔴 **추론시 프레임워크는 토큰을 더 쓴다.** belief 유지·검증·모니터링이 매 턴 비용이고 **초록이 그 비용을 적지 않는다.** 🎯 **같은 배치 [[caveman]] 이 반대 방향(출력 압축)이라 직교 쌍이다** → [[대립레시피-동시도착]].
- **허와 실**: ✅ **범위가 넓다** — *"four benchmarks spanning **execution and diagnosis**"* × **LLM 백본 3종** 전부에서 *"highest overall performance on **every** benchmark with **all three** backbones"*. ✅ **아블레이션으로 ①·③의 필요성 입증** + ✅ **컨텍스트 스케일링 실험으로 컨텍스트 증가에 대한 내구성(resilience)** 제시 — **장기 에이전트 논문이 당연히 받아야 할 질문을 스스로 받았다.**
- 🔴 **수치 0개 · 벤치마크 이름 0개**: 초록 **1,307자 전수 검색** 결과 성능 수치 **0개**이고 *"four benchmarks"* 의 **이름도 적지 않는다.** ⇒ **볼트 대조 불가.**

> [!insight] ✅ 선언된 구현체가 실체가 있다 — 오늘 5건 중 **유일하게 쓸 수 있는 1건**
> HF API `githubRepo` = `https://github.com/luoyu100/PoS` · **볼트 독립 실측 ★21**(HF 보고 20 = **+1 드리프트**) · fork 0 · issues 0 · created **2026-09-14** · pushed **2026-10-02** · **라이선스 MIT**.
> 🏆 **실체 규모**: `GET /languages` = **Python 4,216,210B(4.2MB)** + HTML 22,544 + CSS 3,514 + Shell 3,185. 루트 **20항목** — `main.py` · `belief/` · `baselines/` · `benchmarks/` · `configs/` · `contexts/` · `prompts/` · `docs/` · `CITATION.cff` · `THIRD_PARTY_NOTICES.md` · `.env.example`.
> ⚖️ **오늘 논문 5건 중 "MIT + 실제 코드 + 벤치마크 포함" 조건을 만족하는 유일한 건이다.** 📌 `baselines/` 와 `benchmarks/` 가 함께 있어 **초록이 숨긴 벤치 이름과 수치를 코드로 복구할 수 있다.**
> 🔴 **단 `description` 이 프레임워크 설명이고 논문 수치는 아니다 — 복구는 미수행이다.**

> [!warning] 🔴 PoS 가 무엇의 약자인지 초록에 없다
> 초록 전문에 **약어 풀이가 없다**(*"We introduce PoS, an inference-time framework…"*). 프로젝트 페이지 URL 이 `luoyu100.github.io/projects/**progression-of-states**/project/` 이므로 **"Progression of States" 로 추정**된다. 🔴 **추정이고 1차 문서 확인은 아니다 — 사실로 적지 않는다.**

> [!action] 당장 할 것 (★최우선)
> `git clone https://github.com/luoyu100/PoS` 후 **`benchmarks/` 와 `baselines/` 를 먼저 읽는다.** 목표 2개:
> ① **초록이 숨긴 "four benchmarks" 의 이름과 수치 복구** — 코드/설정에 있을 가능성이 높다.
> ② **`belief/` 모듈에서 Belief Trapping 탐지 구현 확인** — 이것이 볼트 `log.md` 운영에 그대로 이식 가능한 유일한 부품이다.
> ✅ **MIT 이므로 사용 제약 없다**(같은 배치 [[Sharpening-Tax]] 는 CC BY-NC 로 상업 사용 금지).
> 🔴 **볼트 한계 직결**: 코드 실행 0건이 14배치 연속이다. 이 레포는 `main.py` + `.env.example` 로 실행 경로가 명시돼 있다.

> [!question] 미해결 질문
> - *"four benchmarks spanning execution and diagnosis"* 의 이름은? (→ 구현체로 복구 가능)
> - **belief 유지 비용**(추가 토큰/지연)은? 초록이 적지 않는다.
> - 🎯 **같은 배치 [[HC-DLM]] 과 구조적 동형인가?** 양쪽 다 *"지속되는 단일 상태"* 를 핵심에 둔다 — HC-DLM 은 **생성 과정의 연속 잠재**, PoS 는 **에이전트의 belief**. **서로 다른 층에서 같은 처방이 같은 날 나왔다.**

## 관련 페이지
- [[HC-DLM]] — 같은 배치 · **"지속되는 단일 상태"** 구조적 동형
- [[OneStreamer]] — [[에이전트-메모리-레이어]] 5번째 분류(자기 생성 텍스트형) · 같은 날짜 페이지의 다른 답
- [[Sharpening-Tax]] · [[On-Policy-or-Off-Policy-Distillation]] · [[Adaptive-Reward-Routing]] — 같은 배치
- [[caveman]] — 반대 방향(출력 압축) 직교 쌍
- [[에이전트-메모리-레이어]] · [[하네스-설계-축]] · [[선언된-구현체-공백]] · [[대립레시피-동시도착]]
- [[local-llm]] · [[Alibaba]]

## 원본
- 출처: https://huggingface.co/papers/2610.01415
- 제목(원문): *Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States*
- 구현체: https://github.com/luoyu100/PoS (★21 · **MIT** · **Python 4.2MB** · ✅ 실체 있음)
- 프로젝트: https://luoyu100.github.io/projects/progression-of-states/project/
- **볼트 독립 검증**: upvote **71** ✅(수집기 일치) · publishedAt **2026-10-01** ✅ · 저자 **12명** ✅ · 초록 **1,307자**
- 소속: **Alibaba** (HF API `organization` · 🔴 PDF 미열람이므로 공동 소속 유무 미확인 — 같은 배치 2건에서 `organization` 이 제1저자 소속만 반영함이 확인됐다)
- 10-02 게시분 **upvote 4위**
- 신뢰도: ⭐⭐⭐⭐ (4벤치×3백본 전부 최고 주장 + 아블레이션 + 컨텍스트 스케일링 + ✅ 실체 있는 MIT 구현체 / 🔴 수치 0개 · 벤치 이름 0개 · 비용 미공개)
