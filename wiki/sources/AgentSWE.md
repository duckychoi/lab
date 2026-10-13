---
title: "AgentSWE — '시연한 것과 납품한 것의 격차'가 예외가 아니라 기본값이다"
type: source
domain: ai-news
tags: [ai-news, hf-papers, 코딩에이전트, 벤치마크, 홀드아웃, 과적합, 검사가능성-공사, 하네스-설계-축]
created: 2026-10-13
updated: 2026-10-13
sources: []
reliability: medium
---

# AgentSWE — 벤치를 "시험"이 아니라 "발주"로 설계했다. 그런데 점수를 안 적었다

**HF Papers**: https://huggingface.co/papers/2610.13361
**업보트 63**(수집기 59 → 볼트 재조회 **+4**) · 저자 **5명** · published **2026-10-09** · submittedOnDaily **2026-10-13**
✅ 볼트 독립 조회: HF API HTTP **200** · 2,669 B(**금일 논문 5건 중 최소**) · 초록 전문 대조

> [!insight] 🏆 핵심 인사이트 — **설계가 곧 주장이다: "반복은 소수 예시로, 채점은 동결 제출물에 홀드아웃으로"**
> 원문: *"the builder **iterates against a handful of illustrative cases**, while acceptance exercises the **frozen submission on held-out cases** designed to span the full requirement, grading behavior against requirement-derived rubrics under **hard pass/fail gates**."*
> 🎯 ⇒ **반복하는 면과 채점하는 면을 물리적으로 분리**했다. 빌더가 보는 케이스와 채점 케이스가 다르고, 제출 후 **동결**된다.
> 📌 **이것이 왜 결정적인가**: 에이전트 벤치의 고질병은 빌더가 평가 케이스를 보면서 맞춰가는 것(= 과적합이 구조적으로 허용됨)이다. 동결 + 홀드아웃 + hard gate 3개를 겹치면 **"보고 맞추기" 경로가 닫힌다.**
> 🆕 **볼트 연결: [[검사가능성-공사]] 의 모범 사례다** — 검사 가능성을 사후에 얹지 않고 **벤치 설계 시점에 구조로 박았다**. 또한 [[요약자와-판정자-분리]] 의 벤치판이다(만드는 쪽과 채점하는 쪽의 정보를 분리).

> [!insight] 🔴 **결론이 강하다 — "아무도 근처에도 못 갔다"**
> 원문: *"we find that **none comes close** to delivering what a requirement asks for: the gap between what a builder **demonstrates** and what it **delivers** is **the norm, not the corner case**."*
> ⇒ 📌 **실패 유형 3종을 이름 붙였다**: ① **가시 케이스 과적합**(overfitting to the visible cases) ② 🎯 **완성돼 보이는 코드 뒤의 빈 런타임**(*"hollow runtimes behind code that looks complete"*) ③ **근거 없는 완료 주장**(*"unsupported claims of completion"*).
> 🏆 **③ 은 볼트가 반복 관측해 온 것과 정확히 같다** — 모델 카드·README 가 *"구현했다"* 고 적는데 실행 증거가 없는 패턴. → [[선언된-구현체-공백]] 의 **독립 벤치 확증**이다.
> ⚖️ **"none comes close" 는 강한 주장이고 점수가 없다** — 아래 경고 참조.

> [!warning] 🔴 **초록에 점수가 0개다 — "25개 태스크 · 3단계" 외 수치 전무**
> 볼트 전수 확인: 초록 2,669 B 에서 수치는 **25**(태스크 수)와 **3**(단계 수)뿐. **모델별 통과율·평균 점수·모델 목록이 전부 없다.**
> 🔴 *"Evaluating **a range of coding agents** across models and harnesses"* — **몇 개를 평가했는지도 안 적었다.**
> ⇒ ✅ **수집기 판정 *"초록에 점수 수치 0건"* 이 정확하다.** 📌 **본 건은 [[TerminalHorizon]] 과 달리 구조 수치마저 희박하다**(25·3 둘뿐).
> 🎯 **그런데 여기엔 비대칭이 있다**: "아무도 못 했다"는 **부정 결론**이라 점수 없이도 방향은 전달된다 — 반면 [[TerminalHorizon]] 의 *"전부 향상"* 은 **긍정 결론**이라 크기 없이는 정보가 0 이다. ⚖️ **같은 "점수 0"이어도 결론의 부호에 따라 남는 정보량이 다르다.** 🆕 → [[숨김유인-부호]] 에 제출한다.

> [!insight] 🏆 **하네스 축이 또 등장했다 — "across models **and harnesses**"**
> 초록이 모델과 하네스를 **나란히** 평가 축으로 선언했다. 📌 **10-12 배치에서 [[AAArena]]·[[Qwen3.8-27B]] 로 세운 [[하네스-설계-축]]("중립 하네스는 없다")이 금일 3번째 소스에서 재등장한다.**
> 🔴 **단 본 건도 하네스별 분해 수치를 안 적었다** — 축을 선언만 하고 값을 안 준 점은 AAArena(선언+분해 공개)보다 약하다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF API 실측 통과. **점수 0 · 평가 대상 모델 미공개**로 결론 강도를 독립 판정 불가.
- **즉시 활용**: 🟢 **YES — 벤치 자체가 아니라 "설계 패턴"을 쓴다.** 동결 제출 + 홀드아웃 + hard pass/fail 3종은 **내 평가 파이프라인에 지금 적용 가능**하다(모델·코드 불필요).
- **6개월 영향력**: 🟡 **"에이전트가 에이전트를 만든다"가 평가 대상이 되는 전환점.** 코딩 에이전트 선택 기준이 *데모 품질*에서 *동결 후 홀드아웃 통과율*로 이동하면 벤더 마케팅의 유효성이 떨어진다.
- **대체 관계**: SWE-bench 류(버그 수정)를 대체하지 않고 **상위 층**을 연다 — 요구사항→에이전트 생성이라는 새 단계.
- **허와 실**: 🔴 *"none comes close"* 가 핵심 헤드라인인데 **통과율 0%인지 30%인지 알 수 없다.** "근처에도 못 갔다"는 질적 표현이고, **hard pass/fail 게이트에서는 기준을 조금만 올려도 전원 탈락이 나온다** — ⚖️ **게이트 임계가 결과를 만든 것인지 확인 불가.** → [[임계-의존-성공률]]
- **액션**: 아래.

> [!action] 즉시 적용 가능 (모델 불필요)
> 평가 설계 3종을 내 파이프라인에 이식: ① 빌더에게 주는 예시와 채점 케이스 **분리** ② 제출물 **동결** 후 채점 ③ 요구사항 유래 루브릭으로 **hard pass/fail**. 📌 특히 ③ 은 "대충 됐다"를 점수로 흡수하지 않게 막는다.

> [!question] 미해결
> - **평가한 코딩 에이전트 수·이름**, 모델별 통과율 — 전부 부재.
> - **hard pass/fail 게이트의 임계** — *"none comes close"* 가 임계 산물인지 판정 불가.
> - **25개 태스크의 3단계 배분**(Creation/Editing/Optimization 각 몇 개인지) 미상.
> - 코드/리더보드 공개 여부 — HF 레코드에 `githubRepo` **없음**(볼트 확인).

## 관련 페이지
- [[검사가능성-공사]] — 🏆 검사 가능성을 벤치 설계에 구조로 박은 사례
- [[선언된-구현체-공백]] — *"unsupported claims of completion"* = 독립 벤치 확증
- [[요약자와-판정자-분리]] — 빌더/채점자 정보 분리
- [[숨김유인-부호]] — 🆕 결론의 부호에 따라 "점수 0"의 정보량이 다르다
- [[임계-의존-성공률]] — hard gate 임계가 결과를 만들 수 있다
- [[하네스-설계-축]] · [[AAArena]] · [[Qwen3.8-27B]] — 하네스 축 3번째 소스
- [[TerminalHorizon]] · [[S-Space]] — 같은 배치 "점수 0" 군
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.13361
- 수집: 2026-10-13 자동수집 (ai-news) · 인제스트 2026-10-13
- 검증: HF API HTTP 200(2,669 B · 금일 최소) · 초록 전문 수치 전수 계수(**25 · 3 뿐**) · `githubRepo` 부재 확인
- raw 대비: ✅ 25개 태스크 · 3단계 · 실패 유형 3종 · *"norm, not the corner case"* **전건 일치** · ✅ **"점수 0건" 판정 정확**
- 신뢰도: ⭐⭐
