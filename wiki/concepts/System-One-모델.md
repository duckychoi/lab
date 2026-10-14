---
title: "System One 모델 — 생성에서 점수화로, 그리고 캐시 가능성을 1급 요건으로"
type: concept
domain: ai-news
tags: [concept, system-one, typed-decisions, scoring-head, caching, low-latency, agent]
created: 2026-10-14
updated: 2026-10-14
sources: [Jeva.md, VideoJev.md, SearchJev.md]
reliability: medium
---

# System One 모델

> [!insight] 한 줄
> **LLM/MLLM 에게 답을 "생성"시키지 않고 "점수화"시키는 설계 계열.** 에이전트가 **파싱 없이 바로 쓸 수 있는 저지연 결정**을 만드는 것이 목적이고, 2026-10-13 발행분에서 **캐시 가능성(cacheability)이 1급 설계 요건으로 올라왔다.**

## 왜 개념으로 세웠나 — 표본 근거

CLAUDE.md 규약(*"3개 이상 소스에서 등장한 개념은 반드시 concepts/ 독립 페이지 생성"*) 충족:

| 소스 | 유형 | 관계 |
|---|---|---|
| [[Jeva]] (2610.18773) | 논문 · 업보트 52 | *"System One Models **from First Principles**"* — 4요건 제시 |
| [[VideoJev]] (2610.18615) | 논문 · 업보트 54 | *"**System One Model** for Video Understanding"* — 영상 적용 |
| `autotrust/JEV-35B` | HF 모델 · 트렌딩스코어 439 | 태그 `system-one`·`typed-decisions`·`noul`·`choice`·`score` |
| [[SearchJev]] | 볼트 기보유 소스 | Jev 계열 · 🔴 **관계 미확인** |

🔴 **표본 한계를 명시한다**: 논문 2건은 **같은 날(2026-10-13) 발행분**이고, 모델 1건은 **다른 arXiv(`2609.14973`)를 인용한다.** ⇒ ⚖️ **"하나의 확립된 연구 계열"이라고 단정하지 않는다.** 금일 시점에서 확인된 것은 **용어와 출력 형식이 겹친다**는 사실까지다.

## 공통 구조 — 3가지가 겹친다

### ① 자기회귀 디코딩 제거 → 점수화 헤드
- [[VideoJev]]: *"replacing **autoregressive answer decoding** with a **shared head that scores** temporal intervals and textual options"*
- [[Jeva]]: *"recent practice of predicting an answer from **serialized text** does not … respect the structure of a decision problem"*

🎯 **같은 비판이다**: 텍스트로 답을 뽑는 것이 결정 문제에 맞지 않는다.

### ② 출력 타입이 고정된다 — Choice / Noul / Score
[[Jeva]] 가 *"unify **Choice**, **Noul**, and **Score** outputs"* 로 명시하고, `JEV-35B` 카드 태그가 **같은 3개 조어**를 쓴다(`choice`·`noul`·`score`).
- **Noul** = null 출력(답 부재) 전용 타입으로 보인다 — ⚖️ **조어의 정의가 초록에 없다**(🔴 미확인).
- 📌 **`Noul` 이라는 비표준 조어가 논문과 모델 카드에서 동시에 쓰인다**는 것이 두 쪽을 잇는 가장 강한 단서다.

### ③ 🏆 **캐시 가능성이 1급 요건으로 올라왔다 — 금일 최대 수확**
| 소스 | 표현 | 메커니즘 |
|---|---|---|
| [[Jeva]] | **4요건 중 (iv) `cacheable`** — *"Request-independent computation over recurring alternatives should be reusable across requests"* | 선택지를 **불변 메모리(immutable option memory)** 로 두고 **요청 상태만 정제** |
| [[VideoJev]] | **Cached inference** + **Joint inference** | 같은 영상 히스토리에 대한 **시각 연산 재사용** · 여러 쿼리를 **단일 forward** |

🎯 ⇒ **두 논문이 독립적으로 "반복되는 쪽을 고정하고 변하는 쪽만 계산한다"는 같은 비대칭을 택했다.**
📌 **이것이 저지연의 실제 출처다**: 모델을 작게 만든 것이 아니라 **재계산을 없앴다.** [[VideoJev]] 의 **100배 초과** 가속이 Joint inference 에서 나온다.

> [!insight] 🆕 볼트 관측 — **[[local-llm]] 메모리 분류에 빈 칸이 있다**
> 볼트 CLAUDE.md 의 local-llm 템플릿은 메모리 아키텍처를 **RAG / KV / 압축 / 외부DB** 로 묻는다.
> 🔴 **System One 의 캐시는 이 넷 중 어디에도 정확히 안 들어간다**: 문서를 검색하는 것(RAG)도, 생성 토큰의 KV 를 재사용하는 것(KV 캐시)도 아니다. **입력 측 "선택지 집합"의 표현을 고정해 두는 것**이다.
> ⇒ 🆕 **새 칸 제안: "후보 측 캐시(option-side cache)"** — 요청이 아니라 **선택지가 반복될 때** 효과가 나는 유형. 📌 **표본 2이고 조기 신설이므로 분류 제안으로만 적고 독립 개념으로 올리지 않는다**(10-10 *"n=1 조기 신설"* 자기지적 적용).

## 🔴 검증 상태 — 이 계열의 공통 약점

| 주장 | [[Jeva]] | [[VideoJev]] |
|---|---|---|
| 벤치마크 **이름** | 🔴 **0개** | ✅ 7벤치(그라운딩 3 + QA 4) |
| 품질 **수치** | 🔴 비정량(*"strong"*) | ✅ +6.7p / +10.8p |
| 지연 **수치** | 🔴 비정량(*"substantially"*) | ✅ 2.8~3.1배 / 100배 초과 |
| 코드·가중치 | 🔴 언급 없음 | 🔴 언급 없음 |

🎯 ⇒ **패러다임을 선언한 쪽([[Jeva]])이 수치가 없고, 적용한 쪽([[VideoJev]])이 수치를 가졌다.**
📌 **따라서 "System One 이 빠르다"의 근거는 현재 [[VideoJev]] 단독이다.** ⚖️ 일반 주장으로 쓰면 표본 1이다.
🔴 **구현체 경고**: `JEV-35B` 를 [[Jeva]] 의 구현체로 적으면 **틀린다**(인용 arXiv 가 `2609.14973` 로 다름). 또한 그 카드의 Decision Index 59.73 은 **저자 자체 채점**이고 리더보드 등재값이 아니다. → [[분포내-우위]]

> [!question] 미해결
> - **`Noul` 의 정의** — 두 소스가 같은 조어를 쓰는데 뜻이 초록에 없다.
> - [[Jeva]] ↔ [[VideoJev]] ↔ `2609.14973` ↔ `JEV-35B` 의 **저자·기관 관계** 미확인. 📌 해소 경로: arXiv 저자 목록 대조. **금일 미시도.**
> - [[SearchJev]] 와의 관계 — 볼트가 이미 가진 Jev 계열 소스인데 **연결을 확인하지 않았다.**
> - **단발 질의에서의 이득** — 캐시 전제가 깨지면 가속이 사라질 가능성. 두 초록 모두 경계를 적지 않았다.

## 관련 페이지
- [[Jeva]] — 4요건 원전
- [[VideoJev]] — 수치를 가진 유일한 적용 사례
- [[SearchJev]] — 관계 미확인
- [[Urbex]] — 🆕 **같은 배치의 평행 사례**: System One 을 자칭하지 않으나 **"생성 → 능동 탐색/점수화"라는 같은 방향**이다
- [[분포내-우위]] — 자체 채점 경고
- [[임계-의존-성공률]] — 두 축 가속 배수
- [[local-llm]] · [[ai-news]]

## 원본
- 생성: 2026-10-14 (인제스트 2026-10-14)
- 근거: HF Papers API 초록 전문 2건(2610.18773 · 2610.18615) + HF 모델 목록 API(`JEV-35B` 트렌딩스코어 439) — 전건 볼트 직접 수신
- 신뢰도: ⭐⭐ (용어·출력형식·캐시요건 **겹침은 확인** / 🔴 **연구 계열 동일성 미확인 · 표본 3 · 논문 2건이 같은 날 발행**)
