---
title: "ModularRSI — 하네스를 5모듈로 쪼개 따로 진화시켰다. 그리고 벤치를 진화에서 뺐다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent, harness, rsi, self-evolution, terminal-bench, swe-bench, ablation, benchmark-disjoint]
created: 2026-09-19
updated: 2026-09-19
sources: [SoL-Pi.md, Harness-Design-Empirical.md, NeoHorse-1-Paper.md]
reliability: medium
---

# ModularRSI (arXiv 2609.14857)

> [!insight] 핵심 인사이트 — **"벤치에서 진화시키면 벤치에 맞춰진다"를 처음으로 통제 조건에서 수치로 보였다**
> 기존 하네스 RSI 방법(AHE · Meta-Harness)을 **같은 Terminus-2 출발점 · 같은 120개 진화 과제 · 같은 16 에폭 · 같은 DeepSeek-V4-Flash-0731** 로 재현하되 **진화 데이터만 벤치와 분리**하자, 둘 다 기준선 근처에 머물렀다(표 6, TerminalBench 2.0):
> ```
>                  Acc     Pass@3   Pass3
> Baseline        61.79    73.03    50.56
> Meta-Harness    62.92    74.16    50.56
> AHE             62.54    73.03    51.69
> ModularRSI      67.42    78.65    56.18
> ```
> 🎯 저자 서술: *"although existing RSI methods can achieve strong performance when evolving **directly on benchmark data**, their improvements are much more limited under our benchmark-disjoint protocol"* — **기존 방법의 보고 이득 중 일부가 벤치 적응이었을 가능성**을 가리킨다. (🔴 단 기존 방법의 원 보고치를 이 논문이 같은 표에 옮기지 않아 "얼마가 적응분인지"는 계산할 수 없다.)
> 📌 **이 논문의 진짜 기여는 방법보다 프로토콜이다** — 2,000개 벤치 분리 진화 과제를 **데이터셋으로 공개**했다(`IQuestLab/ModularRSI_2000_Instances`). [[측정도구-먼저-반증]] 형태: 개선을 주장하기 전에 "기존 측정이 적응과 일반화를 못 가른다"를 먼저 적었다.

> [!insight] 🎯 볼트 3번째 독립 분해 — 그런데 **컨텍스트 관리가 가장 약한 모듈로 나왔다**
> 단일 모듈 진화(표 5, TB2.0, 기준선 Acc 47.57 · StepNum 34.70) — **표 전행**:
> ```
> 모듈                     Acc     Pass@3   Pass3   StepNum
> Baseline                47.57    58.43    30.34    34.70
> Context Management      49.44    61.80    31.40    35.10
> Tool Use                50.19    62.92    30.34    41.28
> Agent Loop              50.56    64.04    34.83    40.40
> Observation Management  49.81    65.17    33.70    22.50   ← 스텝 −35%
> Task Completion Det.    49.44    65.17    31.40    31.06
> ModularRSI(통합)         52.43    65.17    35.96    35.57
> ```
> - 🎯 **[[SoL-Pi]] 와의 대응**: SoL-Pi에서 선택압을 통과한 "관측 처리"가 여기서도 **효율(스텝 34.70→22.50)** 을 가장 크게 바꾼 모듈이다. **효율 논문(SoL-Pi)과 효율 측면에서 같은 부품을 지목했다.**
> - 🔴 **[[Harness-Design-Empirical]] 과의 긴장**: 그쪽은 "컨텍스트 관리가 가장 중요"라고 했는데 여기서는 **Context Management가 Acc 최저(49.44, TCD와 동률)** 이다. 🎯 볼트 해석(추정): HDE 결론 ①은 *"윈도우 예산이 빠듯할 때만"* 이다 — 이 논문은 예산 제약을 변주하지 않았으므로 **모순이 아니라 조건 차이일 가능성이 크다.** 즉 세 논문은 **같은 부품 목록**에 도달했지만 **중요도 서열은 조건 의존**이다.
> - 📌 독립성: 이 논문(09-14)은 SoL-Pi(09-17)·HDE(09-17)보다 **먼저** 나왔고 둘을 인용하지 않는다(시간상 불가능). 분해 근거는 *"our analysis of existing harness implementations"* + Terminus-2 재구성. → **세 분해의 독립성은 이번엔 확인됐다**(인용 관계 없음).

## 방법 요약
- **출발 하네스**: Harbor의 **Terminus-2** 를 5모듈(Agent Loop · Observation Mgmt · Tool Use · Context Mgmt · Task Completion Detection)로 재구성. 인프라(샌드박스·병렬·LLM 통신)는 진화 대상에서 제외.
- **대조 궤적**: 과제당 K회 롤아웃 → 전원 성공(Positive) / 혼재(Contrastive) / 전원 실패(Negative). 실패 전원이면 **과거 에폭의 성공 궤적**을 Trajectory Memory에서 꺼내 짝짓는다. 실측 분포(부록 D.1): 혼재 **732(40.67%)** · 과거 성공과 재짝 150(8.33%) · 성공 이력 없는 전원 실패 262(14.56%) · 전원 성공 648(36.00%).
- **수정 선택**: 여러 과제가 지지하는 진단일수록 표가 많다(교차 과제 투표) → 단일 사례 과적합 억제.
- **검증 게이트 3단**: AST·import 등 정적 검사 → **Diff Review**(수정이 과제 특화 해법을 인코딩했는지 에이전트가 검토, 걸리면 롤백) → 무작위 2과제 실행 검증.
- **통합**: 모듈별 독립 진화 후 **교차 모듈 통합 에폭 1회**로 중복·충돌 제거 → 동결 후 평가.
- 🎯 **진화시키는 주체가 진화 대상 자신이다**: *"The agent under evolution itself serves as the Code-Modify Agent"*.

## 🔴 루프는 몇 바퀴 돌았나 — [[RSI-프레이밍]] 기준 대조
- **모듈당 3 에폭 × 5모듈(병렬) + 통합 1 에폭** = 저자 환산 **16 에폭 상당**(표 6에서 AHE·Meta-Harness를 16 에폭으로 맞춘 근거).
- 부록 D 사례에 **generation 14** 까지 등장한다 — 하네스가 **불변 세대(immutable generation)** 로 여러 번 교체됐다.
- 부록 F: *"largely monotonic improvement"* 를 **세대별 곡선**으로 보고 — 🔴 **그림 수치는 HTML 본문에 없어 볼트가 옮기지 못했다.** 곡선 보조지표는 **Opus-4.8 LLM 판정 점수**다.
- 🎯 **판정: [[NeoHorse-1-Paper]] 의 "single pass"와 달리 이 논문은 루프를 여러 회 돌렸고 세대별 성능을 기록했다.** 볼트가 [[RSI-프레이밍]] 에 세운 최소 조건(*"루프 2회 이상 + 각 회차 성능 기록"*)을 **형식상 처음 충족한 사례**다. 🔴 단 개선되는 것은 **모델이 아니라 하네스 코드**다(가중치 불변).

## 🔴 걷어낼 것 — 본문에서 찾은 한계 6개
1. **이득 크기가 작고 분산 보고가 없다.** TB2.0은 **89과제 × 3롤아웃 = 267궤적**이다. 47.57→52.43은 **127→140궤적(+13)**, Pass3 30.34→35.96은 **27→32과제(+5)**. 표준편차·신뢰구간·반복 실행이 **본문 0건**(`standard deviation|variance|confidence` 0히트). → **"consistent improvements"는 방향은 일관되지만 크기는 수 과제 단위**다.
2. **교차 도메인 이전의 한 칸은 0이다.** SWE 진화 → TB2.0 평가에서 **Pass3 30.34 → 30.34(불변)**, Acc +1.83. 초록의 *"consistent improvements on unseen … cross-domain tasks"* 는 Acc·Pass@3 기준으로만 성립한다 → [[표-부분인용]].
3. **표 4(모듈형 vs 비모듈형·전모듈 동시 진화)는 예산이 맞지 않는다.** §5.3: *"all evolution processes, including single-module evolution and joint-module evolution, are conducted for **3 epochs**"* — ModularRSI는 모듈 5개 × 3 에폭 + 통합이다. 🎯 **"모듈형이 압도적으로 낫다"(비모듈 46.44, 동시 44.19 vs 52.43)의 일부는 5배 많은 진화 예산일 수 있다.** 예산을 맞춘 비교는 **표 6(타 방법 대비)뿐**이다. (볼트 추론 — 저자는 표 5 설명에서 단일 모듈 변형이 *"larger aggregate trajectory budget"* 없이도 개선됨을 보였다고 적었다.)
4. **대조 분석 절제가 없다** — 저자 한계 절 원문: *"we do **not** conduct a dedicated ablation that isolates the contribution of contrastive trajectory analysis"*. 제목 3요소(benchmark-disjoint · contrastive · modular) 중 **contrastive는 사례·비율 곡선으로만 뒷받침**된다. [[NeoHorse-1-Paper]] 의 "커리큘럼 절제 없음"과 같은 구조.
5. **2,000개 중 240개만 썼다** — TB 120 + SWE 120. 저자 인정: *"our main evolution experiments use only a subset of the 2,000 curated evolution instances"*.
6. **기준선 수치가 표마다 다르다** — 표 2~5는 DeepSeek-V4-Flash-**Preview**(Acc 47.57), 표 6은 V4-Flash-**0731**(Acc 61.79). 같은 "Baseline"이라는 이름으로 **14점 차이**가 난다. 두 표를 섞어 인용하면 안 된다.

> [!note] 📌 교차 모델 이전(표 3, TB2.0, 동결 하네스) — 전행
> ```
> 모델              Baseline Acc/P@3/Pass3      ModularRSI Acc/P@3/Pass3
> GLM-5.2           59.55 / 70.79 / 46.07       61.80 / 74.16 / 49.44
> MiniMax-2.5       41.57 / 56.18 / 24.72       44.94 / 57.30 / 30.34
> DeepSeek-V4-Flash 47.57 / 58.43 / 30.34       52.43 / 65.17 / 35.96
> ```
> ✅ 3모델 × 3지표 **전부 +**. 🔴 다만 이득이 가장 큰 건 **진화에 쓴 모델 자신**(+4.86)이고 타 모델은 +2.25~+3.37 — **이전은 되지만 감쇠한다.**

## 도메인별 추출 (ai-news)
- **신뢰도**: HF 업보트 **171** · 저자 **14명**(Beihang · Manchester · **IQuest Research** · M-A-P · Langboat · Hohai) · GitHub `IQuestLab/ModularRSI` **★28** · 진화 데이터셋 HF 공개(DL 477). 🎯 **코드·데이터·평가 궤적(`trajectories/`)을 전부 공개**했다 — 볼트가 본 하네스 논문 중 [[검사가능성-공사]] 가 가장 완결된 편. 🔴 감점: 분산 없음 · 표 4 예산 불일치 · 대조 절제 없음. → reliability **medium**.
- **즉시 활용**: 🎯 **부분 YES — 방법이 아니라 두 가지 부품.** ① **Diff Review 게이트**(수정이 "이 과제 전용 해법"을 담았는지 따로 검토해 롤백) — 볼트가 규칙을 추가할 때 "특정 배치 전용 규칙인가?"를 묻는 절차로 그대로 옮길 수 있다. ② **혼재 궤적 우선**(같은 과제에서 성공·실패가 섞인 경우가 가장 정보량이 크다) — 볼트의 정정 사례 수집에도 적용 가능.
- **6개월 영향력**: **중간~높음.** "벤치 분리 진화"가 하네스 RSI 논문의 **심사 기준**이 되면, 벤치에서 진화시킨 기존 결과(AHE·Meta-Harness 등)의 보고치가 재해석된다.
- **대체 관계**: [[harness-sdk]]·[[pi-agent-harness]] 류 구현을 대체하지 않는다. **자동 진화 절차**를 얹는 쪽이며, 출발점은 Harbor/Terminus-2다.
- **허와 실**: ✅ 실: 예산 맞춘 타 방법 대비 +4.5~4.9 Acc(표 6) · 코드/데이터 공개 · 한계 절 정직. ❌ 허: *"substantially outperforms joint or non-modular evolution"*(예산 5배 차) · *"consistent"*(Pass3 교차 도메인 0) · 초록의 수치 부재가 가린 **이득 크기 = 수 과제**.
- **액션**: 🎯 **데이터셋 카드 확인 + `trajectories/mergefinal` 의 평가 궤적 표본 읽기.** 모듈별 진화 결과물(`generations/merged_active`)에 **Observation Mgmt가 무엇을 잘라냈는지** 보면 [[Harness-Design-Empirical]] 결론 ②(규칙기반 생략 우선)와 같은지 판정할 수 있다.

> [!warning] 수집기 대조
> - ✅ 원문 대조 일치: 업보트 171 · githubStars 27(HF 필드; GitHub API 실측 ★28) · 저자 14 · 공개 09-14 · 3대 실패원인 · 5모듈 · 2,000과제 · TB2.0/SWE-Bench Verified · 모델 간 이전 주장 · 초록 성능 수치 0개.
> - 🔴 정정/보강: 수집기의 *"세 논문이 독립적으로 비슷한 분해에 도달했는지는 본문 확인 필요"* → **본문 확인 결과 독립이다**(이 논문이 먼저 나왔고 인용 없음). 단 **중요도 서열은 일치하지 않는다**(컨텍스트 관리 최저).
> - 📌 수집기가 비운 org 필드: HF papers API `organization: None`. 본문 소속은 IQuest Research 외 5기관.

> [!action] 당장 할 것
> 1. **볼트 규칙 추가 절차에 "Diff Review" 질문 1개 도입** — *"이 규칙은 이번 배치 사례에만 맞춘 것인가?"* 를 규칙 신설 전에 묻는다. (볼트 규칙이 원 맥락에 결박되지 않은 채 허가증이 되는 문제 — [[MiniMax-H3]] 페이지 09-06 교훈과 같은 축)
> 2. **[[RSI-프레이밍]] 에 "루프 2회+세대별 기록을 충족한 첫 사례"로 등재** 제안(오케스트레이터 통합 대상).
> 3. `IQuestLab/ModularRSI_2000_Instances` 카드와 라이선스 확인(코드는 Harbor 유래 Apache-2.0 + 연구 기여분 **CC BY-NC 4.0 비상업**).

> [!question] 미해결 질문
> - 부록 F 세대별 곡선의 실제 값 — 몇 세대부터 포화하는가? (그림만 있고 본문 수치 없음)
> - 표 4를 **같은 총 예산(16 에폭)** 으로 다시 돌리면 모듈형 우위가 남는가?
> - 컨텍스트 관리 모듈의 약한 기여는 DeepSeek-V4-Flash의 **긴 컨텍스트** 때문인가? 윈도우를 줄이면 서열이 바뀌는가? → [[Harness-Design-Empirical]] 결론 ①의 직접 검증 경로
> - 기존 방법의 **벤치 위 진화 보고치**와 이 논문의 **벤치 분리 재현치**를 한 표에 놓으면 "적응분"이 얼마인가?

## 관련 페이지
- [[RSI-프레이밍]]
- [[하네스-설계-축]]
- [[SoL-Pi]]
- [[Harness-Design-Empirical]]
- [[NeoHorse-1-Paper]]
- [[RSIAgent]] — 같은 날(09-14) 공개된 다른 "RSI"(메모리 축적, 가중치·코드 불변)
- [[Dream-RSI]] — arXiv 번호 인접(2609.14858), 같은 날 공개, 탐색 정책만 개선
- [[DeepSeek-V4-Flash]]
- [[측정도구-먼저-반증]]
- [[검사가능성-공사]]
- [[표-부분인용]]
- [[자기제한-명시]]
- [[harness-sdk]]
- [[pi-agent-harness]]

## 원본
- 출처: https://huggingface.co/papers/2609.14857 · 본문 https://arxiv.org/html/2609.14857
- 코드: https://github.com/IQuestLab/ModularRSI · 데이터: https://huggingface.co/datasets/IQuestLab/ModularRSI_2000_Instances
- 볼트 실측(2026-09-19): HF papers API `upvotes` 171 · `githubStars` 27 · `authors` 14 · `organization` None · `publishedAt` 2026-09-14 / GitHub API `stargazers_count` 28 · `forks_count` 1 · `open_issues_count` 2 · `created_at` 2026-08-28 · `pushed_at` 2026-08-31 · license Apache-2.0(+ LICENSE-MODULARRSI CC BY-NC 4.0) · 파일 4,587개(Harbor 기반, `terminus_2_modular`·`self_evo`·`trajectories` 포함) / HF datasets API `downloads` 477 · `likes` 2 · `createdAt` 2026-08-28 / arXiv HTML 본문 전문 읽음(표 1~7, 9, 11, 한계 절, 참고문헌 — **2609.08183(NeoHorse) 인용 없음**)
- 신뢰도: ⭐⭐ (코드·데이터·궤적 공개 · 예산 맞춘 비교 1건 · 🔴 분산 없음 · 이득 수 과제 단위 · 대조 절제 없음 · 표 4 예산 불일치)
