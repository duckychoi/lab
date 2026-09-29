---
title: "TraceDance — 프런티어 9종이 26.7%에 그친다. 과제는 끝내는데 과정이 나쁘다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, 에이전트-벤치마크, 배포트레이스, RSI, decision-point, 벤치자동생성, 사람검증]
created: 2026-09-29
updated: 2026-09-29
sources: []
reliability: high
---

# TraceDance — Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces

> [!insight] 핵심 인사이트 — **벤치를 고르는 문제를 벤치를 만드는 문제로 바꿨다**
> 초록 축자: *"Developers need tests for the **specific behaviors encountered in deployment**, beyond fixed benchmark suites."*
> 🎯 **전제가 이동했다.** 기존은 *"어떤 공개 벤치가 내 에이전트를 잘 재나"* 였고, 여기서는 *"내 배포 로그에서 내가 싫어하는 행동만 골라 벤치를 찍어낸다"* 다. **벤치마크가 고정 자산에서 생성물로 바뀐다.**
> 핵심 기법 2개: **Anchor-and-Confirm**(프로그래머블 검색 + Flash LLM 후보 확인) · **Anchor Synthesis Loop**(커스텀 행동 명세 생성·수정). 평가 방식은 **decision-point continuation** — 기록된 결정 지점에서 **다음 한 턴만** 행동별 루브릭으로 채점하며, *"**without a reference answer or environment replay**"*.
> 📌 **정답도 환경 재생도 없이 채점한다**는 것이 비용 구조를 바꾼다. 환경 재현이 에이전트 벤치의 최대 비용인데 그걸 건너뛴다.

> [!insight] 🔴 **결론이 불편하다 — 프런티어 9종 평균 통과율 26.7%**
> 초록 축자: *"**Nine frontier LLMs achieve a mean pass rate of only 26.7%**, showing that they still struggle to respond appropriately at the evaluated decision points."*
> 🎯 **이 수치의 의미를 좁게 읽어야 한다.** 이건 *"과제 실패율 73%"* 가 아니다. 벤치의 정의상 **과제는 완료하면서 바람직하지 않은 행동을 보인 지점**을 모은 것이다 → **"끝내긴 하는데 과정이 나쁘다"** 구간이 프런티어급에서도 광범위하다는 뜻이다.
> 📌 볼트 관점: 이건 [[하네스-설계-축]]·[[에이전트축-분기]] 가 왜 성능축과 따로 놀아야 하는지에 대한 **정량 근거**다. 성능 벤치 상위 모델이 이 축에서 무너진다.

> [!note] 규모와 **자기 검증 장치** — 숫자가 제 발로 걸어 나온다
> - 소스: **252,557 세션**(코딩 + 일반 도구 사용 배포 로그)
> - 산출: **벤치 107개 · 4,125 인스턴스** · 요청 충족률 **95.3%**
> - 🎯 **품질 통제 2단**: ① *"human annotators confirm the requested behavior in **84%** of sampled instances"* ② *"the automated grader's agreement with human pass/fail judgments is **comparable to that between the annotators**"*
> - 📌 **②가 중요하다.** 자동 채점기를 사람과 비교한 게 아니라 **사람-사람 일치도를 상한선으로 놓고 거기 붙었다**고 보고했다. [[요약자와-판정자-분리]]·[[검사가능성-공사]] 의 좋은 실천 — **채점기의 한계를 채점기 자신의 지표로 제시**한다.

> [!warning] 🟡 마지막 한 문장은 톤이 다르다
> 초록 축자: *"TraceDance **could serve as a key component of the recursive self-improvement (RSI) loop**."*
> 📌 본문 전체가 측정치로 절제돼 있는데 **마지막 줄만 RSI 로 확장**한다. 조동사 *"could"* 가 붙어 있어 주장은 아니지만, **인용 시 이 문장만 떼면 논문 성격이 왜곡된다** → [[RSI-프레이밍]] 사례 추가. 🔴 수집기는 이 문장을 누락했다(과소보고 — 방향은 안전한 쪽).

## 도메인별 추출 (ai-news)

- **신뢰도**: HF 업보트 **51**(볼트 09-29 실측 · 수집기 50 → **+1**) · arXiv 2609.33295 · 게재 2026-09-27. 초록 무손상. 🔴 **252,557 세션의 출처(어느 제품 로그인지)가 초록에 없다** — 데이터 접근성·재현성 미확인.
- **즉시 활용**: 🟡 **원리는 YES, 도구는 미확인.** 볼트는 배포 트레이스를 갖고 있지 않다. **그러나 볼트 자신의 log.md 가 252,557 세션의 축소판**이다 — 배치마다 반복된 실패(예: [[한정어-탈락]] 3회, arXiv 조회 실패 3일 이월)를 **"바람직하지 않은 행동" 명세로 바꿔 자기 점검표를 만드는** 방식이 그대로 적용된다. 🎯 **오늘 볼트가 실제로 그 일을 했다** — [[무응답-오귀속]] 참조.
- **6개월 영향력**: 에이전트 평가가 **공개 리더보드 → 사내 자동생성 벤치**로 분화할 근거. 볼트가 추적하는 [[Benchmark-Radar]] 계열에 "생성형 벤치" 축이 생긴다.
- **대체 관계**: 고정 벤치 스위트를 **대체하지 않고 보완**한다(저자도 *"beyond fixed benchmark suites"* 라고만 씀).
- **허와 실**: 걷어내면 — **① 벤치 자동 생성 파이프라인은 수치로 뒷받침됨(95.3% · 84%) ② 26.7%는 실측이나 표본이 "나쁜 행동이 관측된 지점"으로 편향 설계됨(의도된 것, 속임수 아님) ③ RSI 는 전망일 뿐.**

> [!action] 당장 할 것
> 볼트 자체 적용: **log.md 에서 반복 실패 3종을 "명세"로 추출해 배치 점검표화**. 후보 — ① 한정어 없는 일반화 ② 도구 실패를 대상 부재로 귀속 ③ 수치 인용 시 조건절 탈락. 우선순위 **높음**(볼트가 이미 세 번 다 저질렀다).

## 관련 페이지
- [[RSI-프레이밍]] · [[요약자와-판정자-분리]] · [[검사가능성-공사]] · [[하네스-설계-축]] · [[에이전트축-분기]] · [[Benchmark-Radar]]
- [[무응답-오귀속]] · [[한정어-탈락]] · [[측정도구-먼저-반증]]
- 같은 배치: [[DN-MOPD]] · [[YuE2]] · [[HexaAnything]] · [[Post-Training-Behavioral-Shadows]] · [[hindsight]]

## 원본
- 출처: https://huggingface.co/papers/2609.33295 · arXiv **2609.33295**
- 실측(2026-09-29 09:08 UTC · HF papers API): 업보트 **51**(수집기 50 → +1) · 게재 **2026-09-27** · 초록 전문 정상
- 수집기 대조: **252,557 · 107 · 4,125 · 95.3% · 84% · 26.7% · 9종 전부 축자 일치** — 이 항목은 수집기 인용 정확도 **6/6**. 🎯 누락 1건: **마지막 RSI 문장**
- 확인 범위: 초록 전문. 🔴 본문·코드·벤치 데이터 미열람 · 🔴 미실행
- 신뢰도: ⭐⭐⭐⭐ **high** — API 실검증 + 사람 검증 지표 내장 + 자기 채점기 한계 명시
