---
title: "Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It — 깊이를 안 쓰는 트랜스포머와 rank-8 한 장"
type: source
domain: ai-news
tags: [ai-news, hf-papers, lora, in-context-reasoning, mechanistic-interpretability, frozen-weights, measurement-critique, qwen3, looped-transformer]
created: 2026-10-04
updated: 2026-10-04
sources: []
reliability: high
---

# Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It (arXiv 2609.36585)

> [!insight] 🏆 핵심 인사이트 — **능력을 더한 논문이 아니라 "기본 응답이 능력을 가린다"는 측정 비판이다**
> 초록의 결론 문장이 이 논문의 성격을 정한다: **"Default answers therefore understate the computation accessible through a tiny edit."**
> ⇒ 📌 **모델의 기본 출력으로 측정한 능력치는 그 모델이 할 수 있는 계산의 하한이다.** 가중치를 **전부 동결**한 채 **이른 층 한 곳에 rank-8 LoRA** 를 붙이는 것만으로 Qwen3-8B 가 24행 체인에서 **15.5% → 99%** 로 간다. **새 지식을 넣은 것이 아니라 이미 있던 깊이를 쓰게 한 것이다.**
> 🎯 **볼트 축과 직결**: 이것은 [[측정도구-먼저-반증]] 의 모델 내부 버전이다 — 벤치 점수가 모델의 한계가 아니라 **디코딩/기본 구성의 한계**를 재고 있었다는 주장이다. 같은 배치 [[DMM]] 이 *"에이전트별 분포가 올바르게 학습됐어도 최종 샘플링 기제에서 실패한다"* 고 적어 **같은 분리(모델 품질 ≠ 산출 품질)를 다중에이전트 층에서 반복**한다.

## 수치 (초록 원문 기준)

- **베이스 모델 13종이 문맥 내 참조를 안정적으로 따라가는 범위 = 1.4~3.6행**. 추가 사전학습 루프는 거의 보태지 않는다.
- **Qwen3-8B**: 24행 체인 exact accuracy **15.5% → 99%** (rank-8 LoRA · **이른 층 1곳** · **전 가중치 동결**)
- 더 길게 학습한 LoRA: **50행**
- **Ouro-1.4B**(루프형): 4루프에서 **60행** · 8루프에서 **최소 160행**
- 실제 과제 전이: **MuSiQue 개선**(과제별 LoRA)

> [!note] 메커니즘까지 적는다 — "릴레이(relay)"
> LoRA 가 릴레이를 **시작**하고, 프로그램 행들이 **중간층의 짧은 구간**을 통해 자기 체인 식별자를 넘긴다. 동결된 헤드들이 체인을 **점점 더 위로** 읽어 올라간다.
> 🏆 **개입 실험이 있다: 부모 행에 대한 어텐션을 제거하면 릴레이가 멈춘다.** ⇒ 상관이 아니라 **인과 주장**이다.
> ✅ **동결 모델 측정만으로 "마지막으로 유효한 개입 층"을 held-out 4종 중 3종에서 허용 오차 내로 특정**한다 — 즉 **어디에 붙여야 하는지를 미리 계산할 수 있다**는 주장이다.

## 🔬 선언된 구현체 3단 층 — **오늘 배치에서 ③까지 통과한 2건 중 하나**

[[선언된-구현체-공백]] 의 3단 판별을 볼트가 실행했다(2026-10-04T09:12Z, GitHub API 실호출):

| 층 | 판정 | 실측 |
|---|---|---|
| ① 선언이 있는가 | ✅ | API `githubRepo` = `Lunamos/stop-thinking-too-early` · `githubStars` 3 |
| ② **코드가 있는가** | ✅ | `GET /languages` = **Python 534,805B + Shell 2,132B** · size **1,387KB** |
| ③ **쓸 수 있는가** | ✅ | **Apache-2.0** (상업 사용 가능) |

- 레포 실측: ★**3** · fork **0** · created **2026-09-29T01:55:25Z** · pushed **2026-09-30T21:00:10Z**
- `projectPage` = `https://lunamos.github.io/stop-thinking-too-early/` (인터랙티브 데모 명시)

> [!warning] 🔴 수집기 표현 1건 정정 — "두 경로가 일치"가 아니다
> 수집기 메모: *"초록에도 링크가 있어 두 경로가 일치하는 드문 건."*
> ⚖️ **볼트 확인: 초록이 주는 링크는 `projectPage` 하나다** — 원문 *"Code and an interactive demo are available at **https://lunamos.github.io/stop-thinking-too-early/**"*. **`githubRepo` URL 은 초록에 없고 HF API 필드에만 있다.**
> ⇒ 📌 **즉 초록만 읽으면 프로젝트 페이지까지만 가고 레포는 못 찾는다. 10-03 에 확립한 "API 필드를 먼저 읽는다" 규칙이 이 건에서도 여전히 필요하다** — 규칙의 반례가 아니라 **약한 형태의 사례**다.

> [!warning] ⚠️ 주력 과제가 합성이다
> 체인 추적(reference following)은 **합성 과제**이고 1.4~3.6행 · 24행 · 160행 같은 수치가 전부 그 축 위에 있다. **실제 과제 증거는 MuSiQue 1건**이다.
> ⇒ ⚖️ **"깊이를 안 쓴다"는 진단은 합성 과제에서 선명하게 입증됐고, 그것이 실무 성능으로 번역되는 폭은 1건으로만 지지된다.** 🔴 MuSiQue 개선 **수치가 초록에 없다** → [[표-부분인용]] 경계 · PDF 열람 필요.
> 🔴 **13종 모델 목록이 초록에 없다** — "Thirteen base models" 만 적혀 있고 어떤 모델인지 모른다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ high — upvote **62(배치 최고)** · **코드 실재 + Apache-2.0** · 개입 실험(어텐션 제거)과 held-out 검증이 있다. 🔴 단 합성 과제 편중.
- **즉시 활용**: **조건부 YES** — rank-8 LoRA 1장은 **볼트 하드웨어에서 학습 가능한 규모**다(전 가중치 동결이므로 메모리 요구가 낮다). 🎯 **긴 문맥에서 참조를 놓치는 증상이 있는 로컬 모델에 바로 시험할 수 있다** → [[local-llm]] 교차.
- **6개월 영향력**: 큼. **"모델을 바꾸지 않고 기본 구성만 바꿔 능력을 꺼낸다"** 는 축이 선다. 📌 [[에이전트-스킬]] 이 *문맥에* 얹는 층이고 이 논문은 *가중치에* 최소 편집을 넣는 층이다 — 같은 배치 [[X-Tree]] 가 바로 그 대비를 주장한다.
- **대체 관계**: 대체가 아니라 **진단 도구**다. 기존 벤치 점수를 **하한으로 재해석**하게 만든다.
- **허와 실**: 실은 **"15.5%→99%"가 합성 체인 과제 수치**라는 것. 프런티어 벤치 점수가 저렇게 움직인다는 주장이 아니다.
- **액션**: ① 레포 clone + 인터랙티브 데모 열기(싸다) ② 체인 추적 평가를 볼트 로컬 모델에 돌려 1.4~3.6행 범위를 **재현**해 보기 — 🏆 **볼트의 15배치 연속 "코드 실행 0건" 을 깰 가장 싼 후보다**(Apache-2.0 · Python 534KB · 전 가중치 동결).

> [!question] 미해결 질문
> - **13종 모델 목록**과 각 모델의 행 수 → PDF
> - **MuSiQue 개선 폭** 수치 → PDF
> - 과제별 LoRA 가 필요한가, 아니면 **한 장이 여러 과제에 전이**되나? (초록은 *"Task-specific LoRAs"* 라고 적는다 ⇒ **전이는 주장되지 않았다**)
> - "이른 층 한 곳"의 **층 번호 선택 규칙** — held-out 3/4 특정이 실용 가능한 수준인가?
> - Ouro-1.4B 의 **"최소 160행"** 이 상한 미측정인지 포화인지

## 관련 페이지
- [[선언된-구현체-공백]] — 3단 층 ③까지 통과(오늘 2건 중 1건)
- [[측정도구-먼저-반증]] — "기본 응답이 능력을 과소평가한다"는 측정 비판
- [[DMM]] — 같은 배치, **모델 품질 ≠ 산출 품질** 분리를 다중에이전트 층에서 반복
- [[X-Tree]] — 같은 배치, **"문맥이 아니라 가중치에"** 라는 같은 방향 주장
- [[게시일-이중화]] — publishedAt 09-29 ↔ HF daily 10-02 ↔ 수집 10-04 **3중 날짜**
- [[Qwen]] · [[Qwen3.8-27B]] — 측정 대상 계열
- [[ai-news]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2609.36585
- 저자: Zehao Jin · Ruixuan Deng · Junran Wang (3명)
- 구현체: https://github.com/Lunamos/stop-thinking-too-early (★3 · Apache-2.0 · Python 534,805B)
- 데모: https://lunamos.github.io/stop-thinking-too-early/
- 지표: upvote **62** · publishedAt **2026-09-29** · submittedOnDailyAt **2026-10-02**
- 검증: **2026-10-04T09:12:13Z** HF 논문 API + GitHub API/languages 실호출 (볼트)
- 신뢰도: ⭐⭐⭐⭐ (코드 실재 + Apache-2.0 + 인과 개입 실험 / 🔴 합성 과제 편중 · 실과제 1건)
