---
title: "Post-Training Leaves Behavioral Shadows — 프롬프트당 단어 하나로 능력이 건너간다 (초록 손상은 HF 탓이 아니었다)"
type: source
domain: ai-news
tags: [ai-news, local-llm, hf-paper, subliminal-learning, 증류, ATD, HumanEval, 초록손상, 수집기-정정, 포맷-불일치-오염]
created: 2026-09-29
updated: 2026-09-29
sources: []
reliability: medium
---

# Post-Training Leaves Behavioral Shadows on Unrelated Decisions

> [!insight] 핵심 인사이트 — **로짓도 파라미터도 과제 예시도 없이, 무관한 단어 하나로 능력이 전이된다**
> 초록 축자: *"We introduce **Active Taskless Distillation (ATD)**, which achieves capability transfer using **only a single word from the teacher per prompt**."*
> 🎯 **설계가 영리하다**: *"selecting prompts where the teacher and student's **shared public ancestor is nearly indifferent between two ordinary words**."* → 공통 조상이 두 평범한 단어 사이에서 **거의 무차별한 지점**만 골라, 교사가 어느 쪽을 택하는지를 신호로 쓴다. **무차별점이 곧 사후훈련의 그림자가 드러나는 자리**다.
> 학생은 *"without target-task examples, teacher logits, or teacher parameters"* — **과제 데이터 없이 과제 능력을 얻는다.**
> 📌 보안 함의가 크다: **모델 출력에서 단어 하나씩만 수집해도 사후훈련 결과가 새어 나간다.** 기존 subliminal learning 연구가 *"traits or preferences using extensive teacher outputs"* 였던 것에서 **비용이 극단적으로 낮아졌다.**

> [!warning] 🔴🔴 **수집기 정정 — 초록 손상은 "HF API가 반환한" 것이 아니다. 원문이 그렇다**
> 수집기 표기: *"**HF API 가 반환한 초록 본문이 부분 손상돼 있다**"* → **귀속이 틀렸다.**
> **볼트 반증**: 09-29 볼트가 **arXiv 원문(`export.arxiv.org` API)** 을 직접 조회한 결과, **동일 위치에 동일 손상**이 나타났다.
> ```
> HF papers API   : "...Qwen2.5-1.5B, 5,664nses yield a 5.34 pp gain on HumanEval+
>                    over an exact nuisance-matched control thadisrupts prompt-resperiments
>                    showtransfer in scientific knowledge..."
> arXiv API (원문) : "...Qwen2.5-1.5B, 5,664nses yield a 5.34 pp gain on HumanEval+
>                    over an exact nuisance-matched control thadisrupts prompt-resperiments
>                    showtransfer in scientific knowledge..."   ← 축자 동일
> ```
> 📌 **두 경로가 글자 단위로 같다 ⇒ 손상은 전송 계층이 아니라 저자 제출본에 있다.** HF 를 의심할 이유가 없었다. → [[포맷-불일치-오염]] 사례 추가, **원인 귀속은 대조 경로 확보 후에만** 하라는 규칙의 재확인.
> 🎯 **이 대조가 가능했던 것은 오늘 볼트가 arXiv 조회 자체를 고쳤기 때문이다** → [[무응답-오귀속]]

> [!insight] ✅ **판독 가능 범위가 수집기 판정보다 넓다 — 대조군 정의는 읽힌다**
> 수집기: *"+5.34pp 와 HumanEval+ 는 판독되나 **표본 수(5,664?)와 대조군 정의는 원문 대조 전까지 인용 금지**"*
> 볼트 판정: **대조군 정의는 손상 이전에 완결돼 있다** — *"over **an exact nuisance-matched control**"* 는 문법적으로 온전한 구다. 손상은 그 **뒤**(`thadisrupts...`)부터 시작한다.
> ✅ **인용 가능**: `ATD` · 단어 1개/프롬프트 · 무차별점 선택 · 로짓·파라미터·과제예시 불요 · Qwen2.5-1.5B · **HumanEval+ +5.34 pp** · **exact nuisance-matched control 대비** · 전이 영역 3종(scientific knowledge · commonsense reasoning · reading comprehension) · *"across additional model generations, sizes, and families"* · *"strength tracks the teacher's update strength"*
> 🔴 **인용 금지 유지**: **5,664 의 단위**(`5,664nses` → *responses* 로 추정되나 확정 불가) · 대조군이 무엇을 *disrupt* 하는지 · 조합가능성(*"the learned sid composable"* → *signal is composable* 추정) — **추정은 추정으로 표기한다.**

> [!note] 서지 실측
> arXiv **2609.29233** · 게재 **2026-09-24T08:39:27Z** · **저자 6인**(Ziyang Zhang, Yubin Jing, Yuanhao Zeng, Yuyao Li 외 2) · HF 업보트 **47**(수집기 46 → +1)

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ **medium** — API 2경로 실검증이나 **초록 자체가 훼손**돼 핵심 표본 수를 못 읽는다. 🔴 **+5.34 pp 단일 수치 · 단일 과제 · 1.5B 단일 모델**이 주 결과이고, 확장 실험은 *"experiments show"* 수준으로 수치 없음.
- **즉시 활용**: 🔴 **NO(능력 획득 용도로는).** 그러나 **위협 모델로는 즉시 유효** — 볼트/에이전트가 외부 모델 출력을 대량 수집해 학습에 쓰는 경로가 있다면, **의도치 않은 능력·성향 전이가 단어 단위에서도 성립**한다는 것을 전제해야 한다.
- **6개월 영향력**: 모델 출력 이용약관·증류 방어 논의의 근거가 된다. [[온폴리시-증류]] 가 "협조적 증류"라면 이쪽은 **비협조적 증류의 하한선**을 낮췄다.
- **대체 관계**: 없음(방법론 연구).
- **허와 실**: 🟡 **걷어낼 마케팅은 적으나 근거도 얇다.** 주장은 크고(*"capabilities transfer through task-unrelated text"*) 보고된 증거는 **+5.34 pp 1건**이다. 🔴 훼손된 초록이 **확장 실험 수치를 정확히 가리고 있어** 주장-증거 간극을 볼트가 메울 수 없다.

> [!question] ⬜ 미해결
> 초록 훼손으로 막힌 3항목(표본 단위 · 대조군 disrupt 대상 · 조합가능성)은 **PDF 본문으로만 해소 가능**하다. 오늘 확보한 arXiv 경로(`https://arxiv.org/abs/2609.29233`)가 열려 있으므로 **다음 배치에서 우선 해소 가능** — 09-28 까지와 달리 **더 이상 도구 문제가 아니다.**

> [!action] 당장 할 것
> arXiv **2609.29233** PDF 본문에서 `5,664` 단위와 대조군 정의 확보. 우선순위 **중간**.

## 관련 페이지
- [[포맷-불일치-오염]] · [[무응답-오귀속]] · [[한정어-탈락]] · [[측정도구-먼저-반증]] · [[자기제한-명시]]
- [[온폴리시-증류]] · [[DN-MOPD]] — 🎯 **같은 배치 증류 논문 2건. 이쪽은 비협조·단어단위, 저쪽은 협조·분산정규화**
- 같은 배치: [[TraceDance]] · [[YuE2]] · [[HexaAnything]]

## 원본
- 출처: https://huggingface.co/papers/2609.29233 · arXiv **2609.29233**
- 실측(2026-09-29 09:09 UTC): HF papers API + **arXiv API 2경로 교차 조회** · 업보트 **47** · 게재일·저자 6인 확인 · **양 경로 초록 축자 동일(손상 포함)**
- 수집기 대조: 🔴 **정정 1건**(손상 귀속 = HF API → **원문**) · 🟡 **완화 1건**(대조군 정의는 판독 가능) · 수치 `+5.34pp`·`HumanEval+` **일치**
- 확인 범위: 초록 2경로. 🔴 PDF 본문 미열람 · 🔴 미실행
- 신뢰도: ⭐⭐⭐ **medium**
