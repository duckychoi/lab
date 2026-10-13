---
title: "Thinking Inertia — '생각하지 마'가 안 먹힌다. 그리고 답변 공간이 열릴수록 심해진다"
type: source
domain: ai-news
tags: [ai-news, hf-papers, 추론모드, no-thinking, 프록시지표, 임계-의존-성공률, 측정도구-먼저-반증, 복합지표-분해]
created: 2026-10-13
updated: 2026-10-13
sources: []
reliability: medium
---

# Thinking Inertia — 측정 방법을 먼저 부수고 들어간 논문

**HF Papers**: https://huggingface.co/papers/2610.11765
**업보트 42**(수집기 42 · **드리프트 0**) · 저자 **5명** · published **2026-10-08** · submittedOnDaily **2026-10-13**
✅ 볼트 독립 조회: HF API HTTP **200** · 3,621 B · 초록 전문 대조

> [!insight] 🏆🏆 핵심 인사이트 — **기존 측정 방식을 먼저 반증하고 시작한다**
> 원문: *"Prior work typically defines no-thinking through **proxies** such as a disabled thinking mode or the absence of long traces. **These proxies are unreliable**: disabled thinking modes **may still emit reasoning**, while long traces **may contain filler rather than genuine inference**."*
> 🎯 ⇒ **"thinking 끄기 = no-thinking" 이라는 등식을 깼다.** 스위치를 꺼도 추론이 나오고, 길다고 추론인 것도 아니다.
> 🏆 **이것은 [[측정도구-먼저-반증]] 의 교과서적 사례다** — 결과를 재기 전에 **자(尺)가 틀렸음을 먼저 증명**했다. 📌 볼트가 2026-09 부터 쌓아 온 이 개념의 **가장 명시적인 외부 확증**이다.
> 🆕 **그리고 [[메타데이터-부재-추론]] 와 직결된다**: *"long traces 가 없다 = 추론이 없다"* 는 **부재로부터의 추론**인데, 논문이 이것을 거짓으로 보였다.

> [!insight] 🏆 **대체 지표를 3층으로 쪼갰다 — 단일 지표를 믿지 않는 구조**
> 응답을 **pre-answer trace** 와 **final answer** 로 정규화한 뒤 3층 측정:
> | 층 | 지표 | 무엇을 잡나 |
> |---|---|---|
> | (i) | **Empty-Thinking Rate** | 정답만 출력하는 엄격 준수율 |
> | (ii) | **Question-Pre-answer Relevance** | 질문↔선행텍스트 유사도(지시 인식형) |
> | (iii) | **LLM-as-judge Explicit Inference Rate** | 가시적 명시 추론 비율 |
> 📌 **설계 의도가 명시돼 있다**: *"these metrics distinguish **answer-only output**, **relevant but non-inferential text**, and **explicit inference**"* — 🎯 **세 상태를 구분하려고 세 층을 만들었다.** 하나였으면 ②와 ③이 섞인다. → [[복합지표-분해]] 의 **설계 선행형** 사례(사후 분해가 아니라 처음부터 분해).

> [!insight] 🏆 **[[임계-의존-성공률]] 의 금일 최강 사례 — 답변 공간이 변수다**
> 원문: *"**Accuracy remains stable on Boolean and multiple-choice tasks**, whereas **open-ended tasks reveal a trade-off** between answer-only compliance and task accuracy."*
> 🎯 ⇒ **같은 개입, 같은 모델인데 과제 형식에 따라 결과의 부호가 갈린다.** Boolean·다중선택에서는 **대가 없음**, 개방형에서만 **준수↔정확도 트레이드오프**가 나타난다.
> 📌 **평균 1줄로 적으면 이 구조가 사라진다** — "no-think 개입 시 정확도 소폭 하락" 이라는 한 줄은 **대가가 특정 과제형식에만 집중된다는 사실**을 지운다.
> 🏆 **볼트 이력과 연결**: [[SimpleICL]](Easy +0.01 / Hard +0.26) · [[Reflex]](2.5m 65% / 5m 40%) 에 이어 **3번째 독립 재현**이고, 흔드는 변수가 **난이도 → 거리 → 🆕 답변 공간**으로 넓어졌다.
> 🆕 **추가 발견**: *"supplying candidate answers makes answer-only responses easier to produce"* ⇒ **같은 질문을 답변 공간만 바꿔 다시 쓰면 준수율이 올라간다** — 즉 **답변 공간은 교란변수가 아니라 조작 가능한 설계 변수**다.

> [!warning] 🔴 **초록에 값이 0개다 — 지표는 정의됐는데 수치가 없다**
> 볼트 전수 확인: 수치는 **6**(프롬프트 개입 수)과 **6**(모델 수)뿐. **Empty-Thinking Rate 도, 관련도도, 명시추론률도 값이 없다.**
> ⇒ ✅ **수집기 판정 *"초록에 수치 0건(지표는 정의됐으나 값이 없다)"* 이 정확하다** — 📌 **수집기가 "지표 정의"와 "지표 값"을 구분해 적은 것은 금일 보고 중 가장 정확한 표현이다.**
> 🔴 **그 결과 "신뢰성 있게 제거하지 못했다"의 강도를 모른다**: 명시추론률이 90%→70% 인지 90%→5% 인지에 따라 **결론이 완전히 달라진다**(전자는 실패, 후자는 거의 성공).
> 🆕 **6 모델 × 6 개입 = 36 조합**인데 **대표값 하나도 없다** — [[표-부분인용]] 의 역(逆) 상태: 표를 부분 인용한 게 아니라 **표 자체가 초록에 올라오지 않았다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF API 실측 통과(업보트 42 **드리프트 0** = 금일 5건 중 유일). **측정 설계는 정교하나 값이 0이라 효과 크기 미상.**
- **즉시 활용**: 🟡 **부분 YES.** 모델·코드는 없지만 **3층 지표 정의는 그대로 차용 가능**하다. 📌 특히 *"thinking 끄기 = 추론 없음"* 가정을 쓰고 있다면 **지금 당장 틀린 가정**이므로 점검이 필요하다.
- **6개월 영향력**: 🟢 **크다.** 추론 토큰 비용 절감 목적으로 no-think 모드를 쓰는 운영이 많은데, **이 논문은 그 절감이 실현되지 않을 수 있음을 보인다**(끈 줄 알았는데 계속 생각한다 = 토큰이 계속 나간다).
- **대체 관계**: 모델 설정(`thinking: off`)에 대한 **신뢰를 대체**한다 — 설정값 대신 **출력 측정**으로 판정하라는 요구.
- **허와 실**: ⚖️ 진단은 설득력 있고 방법론이 정직하다(프록시를 먼저 깼다). 🔴 **그러나 LLM-as-judge 를 3층 중 하나로 쓰면서 그 판정자의 신뢰도를 초록에서 다루지 않는다** — 측정 도구를 반증하며 시작한 논문이 **자기 측정 도구 하나는 검증 없이 쓴다.** 📌 이 비대칭을 적어 둔다. → [[요약자와-판정자-분리]]
- **액션**: 아래.

> [!action] 즉시 점검 항목 (내 워크플로우)
> no-think / reasoning_effort 류 설정을 쓰는 경로에서 **실제 출력에 pre-answer trace 가 남는지** 1회 측정한다. 설정값만 보고 "추론 없음"으로 적고 있었다면 **토큰 비용 추정이 틀렸을 수 있다.** 📌 [[Qwen3.8-27B]] 의 `reasoning_effort` 가 바로 이 대상이다.

> [!question] 미해결
> - **3층 지표의 실제 값** — 6모델 × 6개입 전부 부재.
> - **6개 모델이 무엇인지** 초록에 없음.
> - **LLM-as-judge 의 판정자 모델·일치율** 미상(자기 측정 도구 미검증).
> - 코드 공개 여부 — HF 레코드에 `githubRepo` **없음**(볼트 확인).

## 관련 페이지
- [[측정도구-먼저-반증]] — 🏆 **가장 명시적인 외부 확증**(프록시 불신뢰를 먼저 증명)
- [[임계-의존-성공률]] — 🏆 3번째 독립 재현 · 흔드는 변수 **답변 공간** 추가
- [[복합지표-분해]] — 설계 선행형 3층 분해
- [[메타데이터-부재-추론]] — *"긴 trace 없음 = 추론 없음"* 이 거짓
- [[표-부분인용]] — 🆕 역상태: 표 자체가 초록에 없음
- [[요약자와-판정자-분리]] — LLM-as-judge 자기 미검증
- [[Qwen3.8-27B]] — `reasoning_effort` 가 본 논문의 점검 대상
- [[SimpleICL]] · [[Reflex]] — 임계 의존의 선행 2사례
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.11765
- 수집: 2026-10-13 자동수집 (ai-news) · 인제스트 2026-10-13
- 검증: HF API HTTP 200(3,621 B) · 초록 전문 수치 전수 계수(**6 · 6 뿐**) · 업보트 드리프트 **0**(금일 5건 중 유일) · `githubRepo` 부재 확인
- raw 대비: ✅ 3층 지표 · 6모델 × 6개입 · Boolean/다중선택 안정 vs 개방형 트레이드오프 **전건 일치** · ✅ 수집기의 *"지표는 정의됐으나 값이 없다"* 표현 **정확함을 확인**
- 신뢰도: ⭐⭐
