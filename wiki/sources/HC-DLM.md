---
title: Hierarchical Continuous Diffusion Language Models (HC-DLM) — 연속 잠재를 "유일한 지속 생성 상태"로 두는 구조
type: source
domain: local-llm
tags: [ai-news, hf-paper, diffusion-lm, discrete-diffusion, continuous-diffusion, sudoku, countdown, lm1b, uiuc, amazon, pdf-verified]
created: 2026-10-03
updated: 2026-10-03
sources: []
reliability: high
---

# HC-DLM (2610.02193)

> [!insight] 핵심 인사이트
> **문제 진단이 양쪽 진영을 동시에 깎는다.**
> **이산** 디퓨전 LM: 병렬 디코딩 시 **각 토큰이 자기 marginal 에서 독립 샘플링돼 함께 디코딩되는 토큰 간 통계적 의존성이 끊긴다.**
> **연속** 디퓨전 LM: 공유 연속 상태를 디노이징해 이를 피하지만 **디노이저가 그 상태만 보므로 최종 디코딩 전까지 유효한 토큰 구성에 묶이는 것이 아무것도 없다.**
> **HC-DLM** 은 이산 토큰 생성과 연속 잠재 궤적을 **단일 디노이징 과정**으로 결합하고, 학습 목표를 **토큰 우도의 변분 하한**에서 유도한다.
> 🎯 **최근 유사 연구와의 차이를 스스로 명시**: 자기완결적 이산 체인에 연속 컨텍스트를 *붙이는* 방식과 달리 **잠재를 유일한 지속 생성 상태로 만든다** — 매 스텝 잠재에서 토큰을 읽어내고 그것이 다음 잠재 업데이트의 **scaffold** 로 되먹임된다.

> [!insight] 🏆 볼트 PDF 열람 — 초록이 "수치 0개"였던 논문의 표 3개를 전부 확보했다
> `https://arxiv.org/pdf/2610.02193` → **HTTP 200 · 617,457B · PDF 1.7 · 24페이지** · `pypdf` 추출 **78,992자**.
> ⚖️ **초록에는 성능 수치가 1개도 없었다. 본문에는 3개 표가 있다.** 아래는 전부 PDF 실측이다.

## 🏆 PDF 실측 — 표 3개

**Table 1 · Sudoku 정확도(%↑) — 9×9 격자 · L=81 · K=10 · 81칸 전부 일치해야 정답**
(Easy = Shah et al. 2024 표준 split, **7가지 고정 논리 전략으로 풀리는 퍼즐** / Hard = 그 전략 집합 밖 · Kim et al. 2025 프로토콜)

| 방식 | #Params | Easy | Hard |
|---|---|---|---|
| ARM (순서학습 없음) | 42M | 9.73 | – |
| ARM (순서학습 있음) | 42M | 87.18 | 32.57 |
| MDM (vanilla) | 6M | 6.88 | 3.62 |
| MDM (top-prob.) | 6M | 18.51 | 9.44 |
| MDM (top-prob. margin) | 6M | 89.49 | 49.88 |
| **CCDD** (하이브리드) | 6M | **94.65** | 70.73 |
| **HC-DLM (ours)** | 6M | 94.21 | **72.41** |

**Table 2 · Countdown 정확도(%↑)** — 표 캡션: *"Best overall result per subtask in **bold**; best result at the **6M** parameter scale underlined"*

| 방식 | #Params | CD4 | CD5 |
|---|---|---|---|
| GPT-2 Scratch | 6M / 85M / 303M | 31.9 / 45.8 / 41.3 | 4.3 / 5.1 / 4.5 |
| Stream-of-Search | 250M | 54.2 | – |
| LLaMA | 7B / 13B | 41.1 / 51.1 | 6.7 / 7.4 |
| VDM | 85M | 73.4 | 16.3 |
| D3PM | 85M | 83.1 | 27.6 |
| **RDM** | 85M | **87.0** | **45.8** |
| MDM (top-prob. margin) | 6M | 50.8 | 21.3 |
| CCDD | 6M | 81.18 | 25.35 |
| **HC-DLM (ours)** | 6M | 84.41 | 37.52 |

**Table 3 · LM1B 무조건 생성 Gen. PPL(↓ 낮을수록 좋음)** — 베이스라인은 LangFlow 저자 재학습분

| 방식 | #Params | Gen. PPL |
|---|---|---|
| **Transformer (자기회귀)** | 108M | **66.7** |
| MDM | 116M | 103.9 |
| SEDD | 116M | 115.9 |
| Duo | 116M | 97.6 |
| Plaid | 109M | 77.3 |
| LangFlow | 117M | 92.2 |
| **HC-DLM (ours)** | 118M | 75.5 |
| *Ground truth* | – | *40.4* |

> [!warning] 🔴 초록의 3개 주장 중 1개가 과대다 — 그리고 **본문이 그것을 스스로 정정한다**
> 초록: *"HC-DLM improves over discrete and continuous diffusion baselines at matched model size, **in puzzle accuracy on Sudoku and Countdown** and in generative perplexity on LM1B."*
> ① **Countdown**: ✅ **정확**. 6M 급에서 CCDD 81.18→84.41(**+3.23**) · 25.35→37.52(**+12.17**). 🔴 단 **전체 최고는 RDM 85M(87.0/45.8)** 이고 표의 bold 가 거기 가 있다 — **"matched model size" 한정이 정확히 그 때문에 붙어 있다.**
> ② **LM1B**: ✅ **정확**. 디퓨전 중 최저 PPL 75.5. 🔴 단 **자기회귀 Transformer 66.7 이 더 좋다**. 저자 서술이 정확히 한정한다 — *"best generative perplexity **among the evaluated diffusion models**"*.
> ③ **Sudoku**: 🔴 **부정확.** Easy split 에서 **CCDD 94.65 > HC-DLM 94.21 (−0.44%p 패배)** 다. 승리는 Hard split(+1.68%p)뿐이다.
> ✅ **그런데 본문은 숨기지 않는다**: *"the matched CCDD implementation attains comparable and **marginally higher** accuracy (**94.65 vs. 94.21**)"* — **수치까지 적어 자기 패배를 명시한다.**
> ⚖️ **그래서 이건 "저자가 숨겼다"가 아니라 "초록이라는 매체가 뭉갠다"다.** 📌 [[자기제한-명시]] 는 **본문에서 실행됐고 초록에서 실행되지 않았다** ⇒ 🆕 **[[표-부분인용]] 에 "같은 논문 내 초록↔본문 정직성 격차" 유형 추가. 그리고 이것은 [[벤치마크-이미지-봉인]] 과 같은 축이다 — 분야 관행이 아니라 매체의 속성이다.**
> 🔴 **파급**: **초록만 읽는 볼트의 15배치 관행이 바로 이 지점에서 틀린다.** 초록 대조는 *"수집기가 옳게 인용했는가"* 를 검증하는데, **수집기는 초록을 옳게 인용했고 초록이 과대했다.** ⇒ ⚖️ **"수집기 인용 검증 통과"가 "주장 검증 통과"가 아니라는 것을 처음으로 실물로 확인했다.**

## 도메인별 추출 (local-llm · 디퓨전 LM)

- **실용성 판단**: 🔴 **현 시점 실배포 불가.** 전부 **6M~118M 규모 연구용**이고 LM1B·Sudoku·Countdown 은 실서비스 과제가 아니다. 🟡 **다만 구조 아이디어는 즉시 이해 가치가 있다** — *"잠재를 유일한 지속 생성 상태로"* 는 토큰 병렬 생성 품질 문제의 명확한 진단이다.
- **메모리/상태 아키텍처**: 🎯 **같은 배치 [[Beyond-Memory-PoS]] 와 구조적 동형이다.** 양쪽 다 *"지속적으로 유지되는 단일 상태"* 를 핵심에 둔다 — HC-DLM 은 **생성 과정의 잠재**, PoS 는 **에이전트의 belief**. 📌 **서로 다른 층(디코딩 ↔ 에이전트 루프)에서 같은 처방이 같은 날 나왔다** → [[대립레시피-동시도착]] · [[에이전트-메모리-레이어]].
- **효율 주장**: *"At large batch sizes, HC-DLM also maintains lower wall-clock sampling time, suggesting favorable efficiency for batched parallel generation"* (Fig. 4) · 엔트로피가 **NFE 완화와 CFG 스윕 전반에서 안정**(Table 7·Fig. 5). 🔴 **둘 다 수치가 그림/부록에 있어 봉인** → [[벤치마크-이미지-봉인]] **그림매장형**.
- ✅ **[[비매칭-비교]] 모범 사례**: CCDD 를 *"**matched 6M-parameter scale** under the **same protocol** with its **original backbone replaced by our own** for fair comparison"* 로 **재현**했다. 그리고 *"Parameter counts refer to **sampling-time generative parameters, excluding token embeddings**"* 로 **파라미터 정의까지 명시**(Appendix B.4). ⇒ 🏆 **오늘 배치 최고의 비교 설계다.**
- **아블레이션**: *"Both the continuous latent and the token feedback are needed"* — **두 부품이 전부 필요하다**고 Sudoku 등에서 보인다(본문 86행).

> [!warning] 🔴 선언된 구현체가 비어 있다 — ★52 인데 코드가 0이다
> HF API `githubRepo` = `https://github.com/rhfeiyang/HC-DLM` · 설명 *"**Official implementation** of 'Hierarchical Continuous Diffusion Language Models'"* · **볼트 독립 실측 ★52**(HF 보고 52 = 드리프트 0) · fork 1 · issues 1 · created **2026-09-29** · pushed **2026-10-02**.
> 🔴 **그런데 `GET /repos/.../contents/` 루트 항목이 3개다**: `.gitignore` · `README.md` · `assets` 뿐이고 **`GET /languages` = `{}` (완전히 비어 있다)**.
> ⚖️ **"Official implementation" 이라 선언하고 ★52 를 받았는데 코드가 없다.** ⇒ 🆕 **[[선언된-구현체-공백]] 의 새 하위유형 — "활력형 공백".**
> 📌 **볼트 누적 3사례가 서로 다른 모양이다**: 10-01 [[RIDE]] ★**1** · 10-02 [[CorrGRPO]] ★**0**·description `None` · 🆕 10-03 **HC-DLM ★52 · description 있음 · pushed 어제 · 코드 0**.
> ⚖️ **그래서 10-02 결론 *"★0 은 품질 신호가 아니라 시간 신호"* 를 보강해야 한다: ★는 시간 신호도 아니다. ★52 는 "코드가 있다"의 증거가 아니라 "논문에 관심이 있다"의 증거다.** 구현체 존재는 **★이 아니라 `languages`/`contents` 로 판정한다.**

> [!insight] 🏆 프로젝트 페이지가 같은 배치 [[impeccable]] 의 진단을 실증했다
> `https://hc-dlm.github.io/` 열람(**HTTP 200 · 34,296B**) — 🔴 **github/code 링크 0개**(프로젝트 페이지는 있으나 코드로 가는 경로가 없다).
> 🎯 **부수 발견**: 외부 폰트 로드가 **`family=Inter`(+Fira Code) 단 하나**다. 같은 배치 [[impeccable]] 의 문제 설정이 *"모든 모델이 같은 SaaS 템플릿으로 학습돼 매 프로젝트에 같은 흔적(**전부 Inter 폰트** 등)이 나온다"* 였다. ⇒ **진단과 증거가 같은 배치 안에서 만났다.** 🔴 **단 n=1 이고 이 페이지가 AI 생성이라는 증거는 없다 — 상관일 뿐이다.**

> [!question] 미해결 질문
> - CCDD 가 Easy 에서 이기고 Hard 에서 지는 **이유**가 무엇인가(저자는 *"out-of-distribution Hard split"* 이라고만 적는다 — 일반화 우위라는 뜻인가?).
> - 🎯 **같은 배치 [[On-Policy-or-Off-Policy-Distillation]] 과 Countdown 을 공유한다.** 저쪽은 *"Countdown 더 어려운 변형의 일반화"* 를 본다. **같은 과제의 난이도 축을 두 논문이 각자 쓰는데 설정이 호환되는지 미확인.**
> - `assets/` 에 무엇이 있는가(코드 없는 레포의 유일한 디렉터리).

## 관련 페이지
- [[Beyond-Memory-PoS]] — 같은 배치 · **"지속되는 단일 상태"** 구조적 동형
- [[On-Policy-or-Off-Policy-Distillation]] — 같은 배치 · Countdown 공유
- [[Sharpening-Tax]] · [[Adaptive-Reward-Routing]] — 같은 배치
- [[impeccable]] — 이 논문 프로젝트 페이지가 impeccable 진단을 실증
- [[선언된-구현체-공백]] · [[표-부분인용]] · [[비매칭-비교]] · [[벤치마크-이미지-봉인]] · [[자기제한-명시]]
- [[local-llm]] · [[UIUC]] · [[Amazon]]

## 원본
- 출처: https://huggingface.co/papers/2610.02193
- PDF: https://arxiv.org/pdf/2610.02193 (**볼트 열람 완료** · 617KB · 24p)
- 구현체: https://github.com/rhfeiyang/HC-DLM (★52 · 🔴 **코드 0 · `languages` 비어 있음**)
- 프로젝트: https://hc-dlm.github.io/ (HTTP 200 · 34,296B · 🔴 코드 링크 0개)
- **볼트 독립 검증**: upvote **70** ✅(수집기 일치) · publishedAt **2026-10-01** ✅ · 저자 **5명** ✅ · 초록 **1,434자**
- 🏆 **저자 소속이 API 보고보다 많다**: HF `organization` = **UIUC-CS** 단일이나 PDF 실측은 **University of Illinois Urbana-Champaign + Amazon.com, Inc. 2개 기관**. 저자 **Hui Ren · Zihan Li · Chang Liu(UIUC) · Huidong Liu(Amazon) · Alexander Schwing(UIUC)**. ⇒ 📌 `organization` 은 제1저자 소속만 반영한다(같은 배치 [[Sharpening-Tax]] 에서 2번째 확증).
- 10-02 게시분 **upvote 5위**
- 신뢰도: ⭐⭐⭐⭐ (PDF 실측 표 3개 · 모범적 비교 설계 / 🔴 초록 1개 주장 과대 · 구현체 공백 · 연구 규모)
