---
title: "NeoHorse-1 논문 — 하네스가 데이터 공장이다. 그리고 루프는 아직 한 바퀴다"
type: source
domain: ai-news
tags: [ai-news, local-llm, hf-paper, agent, harness, rsi, post-training, routing, curriculum, on-policy-distillation, tokenrhythm]
created: 2026-09-19
updated: 2026-09-19
sources: [NeoHorse-1-4B.md, NeoHorse-1-9B.md, TokenRhythm.md]
reliability: medium
---

# NeoHorse-1 논문 (arXiv 2609.08183)

> [!insight] 핵심 인사이트 — **배포 중인 라우팅 하네스가 이미 RSI에 필요한 관측 장치를 갖고 있다**
> 논문의 한 문장 주장: *"a deployed routing harness **already contains** such a mechanism"*.
> 라우터는 매 사용자 턴마다 **예측 능력수요(C0~C3) · 정책 조정 후 결정 · 실제 서빙 티어 · 그 뒤의 상호작용**을 남긴다. 이 **예측–행동–결과 분리 기록**이 곧 ① 학습 데이터(궤적) ② 난이도 신호(라우팅 점수) ③ 결손 신호(결과)가 된다.
> 🎯 **새로 만든 게 아니라 이미 돌던 서비스의 부산물을 학습 루프에 연결했다** — [[하네스-설계-축]] 4개 층 중 *"학습루프 내재화"* 층의 **설계도가 이 논문이다.**

> [!insight] 🎯 이 논문에서 가장 강한 증거는 벤치 표가 아니라 **표 3(데이터 출처 대조)** 이다
> ```
> 같은 Qwen3.5-4B · 같은 커리큘럼 · 같은 시드·옵티마이저·패킹 · "closely matched" 예산
>                          LCB    HE     IFBench  BFCL   τ²-Bench  Avg.
> 공개 데이터(Toucan)      49.14  87.80  56.33    54.77  73.54     64.32
> 라우팅 하네스 데이터      53.14  96.34  61.33    57.20  84.85     70.57
> 차이                     +4.00  +8.54  +5.00    +2.43  +11.31    +6.26
> ```
> 🎯 **레시피를 고정하고 데이터 출처만 바꿨더니 5축 전부 +** — "실제 배포 궤적 > 공개 합성 궤적"의 대조 실험이다.
> 🔴 **단 한정 두 개**: 예산은 *"closely matched"*(동일 아님) · *"sources differ in sequence composition"* 을 저자가 스스로 적었다. **데이터 *양*이 아니라 *구성* 차이까지 섞인 비교다.**
> 📌 반면 **데이터 양 스케일링은 약하다**: 중첩 부분집합으로 늘려도 5벤치 평균 **69.31 → 71.45 (+2.14)**, 그것도 로그축. → **출처(+6.26) > 양(+2.14)** — 이 논문 자체 수치로 본 서열.

> [!warning] 🔴🔴 볼트 정정 — **업보트 421은 재현되지 않는다. 오늘(09-19) 실측 170이다**
> ```
> 볼트 기록 (2026-09-18, [[선발창-누락]] · [[TokenRhythm]] · raw.md)  upvotes 421 · ★535
> 볼트 실측 (2026-09-19, HF papers API 동일 엔드포인트)            upvotes 170 · ★587(HF) / 599(GitHub API)
> ```
> 🔴 **업보트는 누적 지표라 하루에 251 줄어들 수 없다.** 가능한 설명: ① 09-18 기록이 다른 필드(모델 ♥ 등)를 옮긴 오기 ② HF 측 정정/중복표 제거. **볼트는 둘을 구분할 수 없다.**
> 🎯 **그래도 결론 방향은 유지된다**: 170은 [[Uno]] 19의 **8.9배**, 09-18 배치 1위 36의 **4.7배**(기존 기록 22배·11.7배에서 하향). **"놓쳤다"는 성립, "압도적으로 놓쳤다"는 과장이었다.**
> 📌 **이건 [[측정도구-먼저-반증]] 의 볼트 자기 사례다** — 수집기에 요구하던 기준을 볼트 자신의 측정에 적용하자 하루 만에 깨졌다.

> [!warning] 🔴 초록의 벤치 개수가 채널마다 다르다
> - arXiv abs 페이지 · HF papers API 초록: *"Across **eleven** benchmarks"*
> - 본문 HTML 초록 · 결론 · GitHub README: *"**ten** benchmarks"* / *"ten-benchmark protocol"*
> - 🎯 **표 1·2의 실제 열은 10개**(BFCL v4 · VitaBench · τ²-Bench · PinchBench · WorkBuddy · QwenClawBench · HumanEval · LCB v6 · IFBench · IFEval). **"eleven"이 오기다.** 볼트는 **10**으로 적는다.

## 방법 — 3단 구조

**① 데이터 (§3)** — 10⁵~10⁶ 개 하네스 궤적 + 공개 데이터 보강
- 단위가 3층: **궤적**(전체 실행) ⊃ **서브신**(같은 국소 목표를 공유하는 연속 턴 — 의미 라벨 단위) ⊃ **사용자 턴**(학습 직렬화 단위)
- 이전 턴의 추론은 버리고 현재 턴 추론만 유지(Qwen3.5 · DeepSeek-V3.2 관례)
- 품질 게이트 3단: 중복·오염 제거 → **규칙기반 구조 검증**(완결 / 부분복구 / 격리 3분기) → **6차원 의미 평가**(목표 달성 · 지시 준수 · 도구 사용 · 증거 일관성 · 오류 복구 · 종료)
- 🎯 **각 차원 판정값이 4개다: `PASS · WARN · FAIL · NOT_EVALUATED`** — 그리고 *"Missing evidence or an interrupted judge call is **never converted into a positive verdict**"*. 판정을 단일 점수로 압축하지 않고 커버리지를 별도 저장한다.
  → **볼트가 [[검사가능성-공사]] 에서 "✅/🔴 2값뿐이라 '확인되지 않음' 칸이 없다"고 적은 바로 그 칸이다.** 세 번째 독립 생태계의 수렴 증거.

**② 학습 (§4)** — Qwen3.5-4B/9B 기반
- **라우팅 점수 = C0~C3 티어 확률의 가중평균**(soft ordering) → SFT를 **3단 커리큘럼**으로 배열(저점수 일부를 후반에 남겨 끝이 고난도로만 쏠리지 않게). **손실 가중에는 쓰지 않는다.**
- 같은 진행을 **온폴리시 증류(OPD)** 에 확장: 기록된 컨텍스트에서 학생이 생성 → 고정 교사가 top-k+잔여 bin 분포로 역-KL 감독
- **능력 기반 배분(§3.5)**: 평가 결손 프로파일로 다음 학습 혼합을 옮긴다 = *"what the system learns to do shapes what it learns from next"*

**③ 평가 (§5)** — 볼트 기보유 수치와 **전건 일치** 확인([[NeoHorse-1-4B]] · [[NeoHorse-1-9B]])
- 4B: 58.94 → **64.87 (+5.93)** · **10축 전부 +**
- 9B: 65.60 → **69.04 (+3.44)** · LCB v6 65.14=65.14 · IFBench 66.33=66.33 · 🔴 **IFEval 89.46 → 89.09 (−0.37)**
- ✅ **저자가 하락을 본문에서 인정했다**: *"instruction-following benchmarks remains largely stable, with **one metric showing a minor decrease**"*. [[에이전트축-분기]] 의 볼트 해석(에이전트 이득 ↔ 지시수행 비용)과 **같은 방향의 저자 서술**: *"marginal benefits are concentrated more heavily on interactive execution than on relatively static instruction compliance."*
- 궤적 사례: 9B가 PinchBench에서 pandas 부재를 인지하고 표준 csv로 전환 → 4B 대비 **요청 −70.8% · 시간 −76.7% · 토큰 −83.6%** (🔴 단일 사례)

## 🔴 걷어낼 것 — 볼트가 본문에서 찾은 한계 6개

1. **루프는 한 바퀴만 돌았다** — *"The results also reflect a **single pass** of the evaluation–selection–update loop"*. **RSI의 "재귀"는 이 논문에서 측정되지 않았다.** [[RSI-프레이밍]] 캔버스에 적어 둔 "RSI 최소조건 = 루프 2회, 아직 1회"가 **저자 서술로 확정**됐다.
2. **커리큘럼·OPD 절제실험이 없다**(본문 `ablat` 0히트). 표 3은 **데이터 출처**만 바꿨다 → **라우팅 커리큘럼 자체의 기여는 미측정.** 논문 제목의 핵심 부품이 분리 검증되지 않았다.
3. **OPD 교사 모델이 비공개** — *"a fixed teacher"* 로만 표기.
4. **홈 하네스 평가** — 학습 궤적을 만든 하네스에 **OpenSquilla** 가 포함되고, QwenClawBench·PinchBench **평가도 OpenSquilla**로 했다. 🎯 **반대 증거도 있다**: 공식 네이티브 하네스로 잰 WorkBuddy에서 4B +9.79로 오히려 가장 크게 올랐다. → **홈 이점만으로 설명되지 않지만, 두 벤치의 이득은 할인해서 읽는다.**
5. **측정 회차 혼재** — PinchBench·VitaBench 1회, QwenClaw·WorkBuddy·τ² 3회 평균. VitaBench는 원래 권장 모델이 없어져 **[[DeepSeek-V4-Flash]] 가 사용자 시뮬레이터 겸 판정자**.
6. **재현 불가** — GitHub `TokenRhythm/NeoHorse` **★599는 코드 레포가 아니다**: 파일 10개 = README · 기술보고서 PDF · 이미지 3 · **추론 예제 2개(`chat.py`·`tool_call.py`)**. 학습 코드·데이터 파이프라인·데이터셋(HF 연결 0) **전무**. 🔴 볼트가 09-18에 "코드 ★535"라고 적은 것은 **"코드 공개"로 읽히면 오해다.**

## 도메인별 추출

### ai-news
- **신뢰도**: HF 업보트 **170**(09-19) · 공개 2026-09-08 · 저자 **37명**(Core 18 + Contributors 18 + "NeoHorse Team") · GitHub ★599 / 이슈 0 · 연결 모델 4(4B 22,666 DL / 9B 10,746 / GGUF 2종) · 연결 Space 3. 🎯 **자기한정 서술이 매우 정직**(단일 패스·"initial attempt… rather than a definitive demonstration"·하락 인정)하지만 **재현 수단이 없고 핵심 부품 절제가 없다** → reliability **medium**.
- **즉시 활용**: 🎯 **YES — 모델이 아니라 품질 게이트 설계를.** `PASS/WARN/FAIL/NOT_EVALUATED` 4값 + "증거 결손은 절대 양성 판정으로 바꾸지 않는다" 규칙은 볼트의 ✅/🔴 2값 체계에 **그대로 이식 가능**하다.
- **6개월 영향력**: **중간~높음.** "배포 트래픽 = 학습 데이터 + 난이도 라벨 + 결손 신호" 공식은 **라우팅 제품을 가진 모든 회사**가 따라 할 수 있다. 🔴 단 **루프 2회차 결과(NeoHorse-2?)가 나와야 RSI 주장이 검증**된다.
- **대체 관계**: 공개 합성 에이전트 데이터(Toucan 류)를 **자체 배포 궤적**이 대체한다는 주장 — 트래픽이 없는 팀에게는 해당 없음.
- **허와 실**: ✅ 실: 동일 레시피 데이터 대조(+6.26) · 4B 10축 전부 개선. ❌ 허: "RSI"(1회전) · "코드 공개"(추론 예제뿐) · 초록 "eleven"(10개).
- **액션**: ✅ 인제스트 완료(본 페이지). 🎯 **다음 버전(루프 2회차) 공개 추적** + 볼트 판정 체계에 `NOT_EVALUATED` 칸 도입 검토.

### local-llm
- **실용성 판단**: 4B·9B BF16, SGLang v0.5.17 배포, 컨텍스트 262,144(README: 최대 1,010,000 확장). 4B가 **Qwen3.5-9B 베이스를 여러 벤치에서 따라잡는다**(평균 64.87 vs 65.60) → 로컬 에이전트용 4B 후보.
- **메모리 아키텍처**: 해당 없음(외부 메모리 아님). 🎯 다만 **"이전 턴 추론 제거 · 현재 턴 추론만 유지"** 컨텍스트 정책은 긴 에이전트 세션의 컨텍스트 절약 규칙으로 참고 가능.
- **Hermes 적용**: 🎯 **데이터 쪽이 적용 대상** — ChinameBot 대화 로그를 *사용자 턴 단위*로 자르고 *6차원 판정*으로 걸러 학습/평가셋을 만드는 구조가 그대로 참고된다. 모델 교체는 **9B 지시수행 −0.37** 을 감안해 지시 준수가 중요한 봇이면 보류.
- **트레이드오프**: 에이전트 축 +(VitaBench 9B +11.00) ↔ 지시수행 정체/소폭 하락(9B).
- **오픈소스 구현체**: 가중치만(apache-2.0). **파이프라인 코드 없음.**

## 🆕 조직 정보 — [[TokenRhythm]] 의 "소속 불명"이 풀렸다

본문 부록 A(Affiliations):
```
1 TokenRhythm Technologies   2 Infinigence AI   3 Tsinghua University
4 Peking University          5 The Chinese University of Hong Kong
6 Visionplus Capital         7 WX Capital       8 Alibaba Group
교신저자(*): Yu Wang(3 칭화대) · Yunhe Wang(1 TokenRhythm)
```
- 저자 37명 중 **소속 1(TokenRhythm) 표기가 다수** — 회사 실체는 TokenRhythm Technologies(홈페이지 `tokenrhythm.ai`, README 배지)
- OpenSquilla 하네스 X 계정이 README에 함께 링크됨 → **하네스 제품과 모델 팀이 같은 조직권**으로 보인다(🔴 볼트 추정, 명시 문장 없음)
- 🔴 **국적은 본문에 명시되지 않았다.** 중국 속담 인용 · 중국어 보고서 과제 · 공저 기관 구성은 정황일 뿐 볼트는 단정하지 않는다.
- 📌 **[[Alibaba]] 소속 공저자 2명** — 베이스 모델(Qwen3.5) 제작사 인원이 파생 사후학습 논문에 참여한 구조.

> [!action] 당장 할 것
> 1. **볼트 판정 체계에 `NOT_EVALUATED`(확인되지 않음) 값 도입 검토** — 이 논문이 [[security-audit-skill]]·[[oh-my-hermes]] 에 이은 **세 번째 독립 수렴 사례** → [[검사가능성-공사]]
> 2. **[[선발창-누락]] 수치 정정 반영**(421→170) — 완료(본 인제스트)
> 3. **NeoHorse 루프 2회차 공개 추적** — RSI 주장의 유일한 검증 경로

> [!question] 미해결 질문
> - 09-18의 421은 어디서 왔나? — 볼트 측 오기인지 HF 측 정정인지 구분 불가
> - 라우팅 커리큘럼을 끄면 이득이 얼마나 남나? (절제 없음)
> - 9B IFEval −0.37은 커리큘럼이 고티어(C2·C3) 에이전트 예제로 쏠린 결과인가? 저자는 원인을 분석하지 않았다
> - OPD 교사는 무엇인가? 풀 안의 C3 모델인가?

## 관련 페이지
- [[TokenRhythm]]
- [[NeoHorse-1-4B]]
- [[NeoHorse-1-9B]]
- [[RSI-프레이밍]]
- [[선발창-누락]]
- [[하네스-설계-축]]
- [[에이전트축-분기]]
- [[검사가능성-공사]]
- [[측정도구-먼저-반증]]
- [[자기제한-명시]]
- [[SoL-Pi]]
- [[Dream-RSI]]
- [[Harness-Design-Empirical]]
- [[DeepSeek-V4-Flash]]
- [[Alibaba]]
- [[Uno]]

## 원본
- 출처: https://huggingface.co/papers/2609.08183 · https://arxiv.org/abs/2609.08183 · 본문 https://arxiv.org/html/2609.08183
- 코드/자료: https://github.com/TokenRhythm/NeoHorse (README · PDF · 추론 예제 2개)
- 볼트 실측(2026-09-19): HF papers API(업보트 170 · githubStars 587 · 저자 37) · GitHub API(★599 · fork 9 · open issues 0 · 생성 09-04 · 최종 push 09-16 · 파일 트리 10개) · arXiv HTML 본문 전문 읽음(표 1·2·3, 부록 A 소속)
- 신뢰도: ⭐⭐ (본문 전문 확인·자기한정 정직 · 🔴 학습 코드/데이터 비공개 · 커리큘럼 절제 없음 · 교사 비공개 · 루프 1회)
