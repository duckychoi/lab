---
title: "CoworkOS — 전략은 모델, 실행 관리는 런타임: 장기 작업용 코워크 하네스 (12벤치 중 1위 6개, 평균 격차는 대부분 1점 이내)"
type: source
domain: ai-news
tags: [ai-news, agent-harness, cowork, long-horizon, subagent, semantic-memory, rsi, glm-5.3]
created: 2026-11-03
updated: 2026-11-03
sources: [https://huggingface.co/papers/2611.03178]
reliability: medium
---

**HF**: published 2026-11-02 · upvote **51** · Jiajie Jin 외 39인(**40명** · "CoworkOS Team") · HF 조직 **Renmin University of China** · 교신 RUC·Fudan · arXiv 2611.03178 · 코드 [RUC-NLPIR/CoworkOS](https://github.com/RUC-NLPIR/CoworkOS) **★51 · MIT** · 레포 생성 **2026-11-03**(논문 공개 다음 날) · Electron 데스크톱 앱 구조(`desktop/`·`src/`·`web/`·`e2e/`) · 실행 0회

## 핵심 인사이트
> [!insight] 모델은 "무엇을·누구에게·언제 수락할지"만 정하고, 상태와 증거는 런타임이 들고 있다
> 3계층 구조다. Main이 직접 실행하거나 서브에이전트에 동기/비동기로 위임한다. 공유 앱 계층에서는 사람과 에이전트가 **같은 문서·PPT·CAD·Blender 씬을 직접 고친다**. 그래서 사람의 개입이 대화창뿐 아니라 산출물 수정으로도 들어온다. 계층형 워크스페이스와 영속 시맨틱 메모리로 장기 Job 로그를 중단 후에도 재개할 수 있게 한다. → [[에이전트-메모리-레이어]] · [[하네스-설계-축]]

> [!warning] "competitive"의 실제 모습 — 본문 Table 1 (백본 GLM-5.3 High · 256K · 출력 64K 동일)
> | 도메인 | 벤치 | OpenHands | Codex | DSH | **CoworkOS** |
> |---|---|---|---|---|---|
> | Tool Use | SkillsBench | 63.30 | 53.48 | 56.75 | **64.34** |
> | | τ³-Bench Banking | 40.20 | 46.39 | **55.67** | 49.48 |
> | | AutomationBench | 50.50 | 30.33 | **53.50** | 51.83 |
> | | 평균 | 51.33 | 43.40 | **55.31** | 55.22 |
> | Productivity | JobBench | 55.02 | 23.42 | 56.15 | **59.88** |
> | | Harvey LAB | **23.75** | 12.70 | 22.30 | 22.74 |
> | | GDPVal (Elo) | 1122 | 925 | 1157 | **1164** |
> | | OfficeQA Pro | 66.20 | **66.30** | 62.30 | 65.90 |
> | | WorkspaceBench-Lite | 64.54 | 58.81 | **68.76** | 67.14 |
> | | 평균 | 55.27 | 40.11 | 56.13 | **57.54** |
> | Search | WideSearch | 81.43 | 82.05 | 72.48 | **82.47** |
> | | BrowseComp | **83.00** | 75.50 | 80.80 | 81.80 |
> | | 평균 | **82.22** | 78.78 | 76.64 | 82.14 |
> | ML Coding | MLE-Bench-Lite | 60.40 | 67.28 | 76.70 | **76.90** |
> | | MLS-Bench | 28.91 | 29.05 | 35.57 | **35.62** |
> | | 평균 | 44.66 | 48.17 | 56.14 | **56.26** |
>
> - 12벤치 중 1위는 **6개**(SkillsBench·JobBench·GDPVal·WideSearch·MLE-Lite·MLS)다. 나머지 **6개에서는 진다**. 최대 열세는 τ³ Banking **−6.19**(DSH 대비)다.
> - 도메인 평균은 **2/4 승**이다. Tool Use는 DSH에 **−0.09**, Search는 OpenHands에 **−0.08** 뒤진다. ML Coding 우위는 DSH 대비 **+0.20 / +0.05**로 사실상 동률이다.
> - 🔴 **반복 실행·분산 보고가 없다**(본문 grep `variance|std|runs` 무관 결과만). 그래서 1점 이내 격차들은 순위로 읽을 수 없다. → [[유의성-자기제한]]
> - 표현 수위가 문서 안에서 다르다. 초록은 "highly competitive", 서론은 "competitive", §4.1.2는 **"the strongest overall performance among the four"**라고 썼다. 그런데 4도메인 종합 평균은 표에 없다. 볼트가 계산한 등가중 평균은 CoworkOS **62.79** · DSH 61.06 · OpenHands 58.37 · Codex 52.62로, 저자 문장과 같은 방향이다. 이 값은 *볼트 계산값*이다.
> - 그림 2(c) 캡션은 "**10** benchmarks in four domains", 본문·초록은 **12**다. → [[문서내-값충돌]]

> [!warning] 자동 후학습 사례 (Table 2) — 기준선은 자기 SFT, 개입은 동시다발
> GLM-5.3이 컨트롤러·데이터 교사를 맡고, Qwen3.6-35B-A3B를 5라운드 후학습했다. 8벤치 평균은 **33.19 → 42.95(+9.76)**다.
> - 벤치별 R0→R5: Automation **11.00→44.15(+33.15)** · SkillsBench +14.91 · τ³ +8.25 · Harvey **3.33→11.08** · BFCL v4 +7.35(R1~R4 내내 기준선 아래였고 R5에 +9.07) · OfficeQA +6.47 · GDPVal +2.34 · **JobBench −2.13**(유일한 하락).
> - 평균은 단조 증가가 아니다. **R1 36.94 → R2 35.90**으로 떨어졌다. 원인 분석에 따르면 42개 궤적이 지도 토큰의 84.2%를 차지했다.
> - 저자 스스로 "**concurrent interventions rather than isolated causal effects**"라고 적었다. 라운드별 기여는 분리되지 않는다. 비교 대상은 R0(자기 seed SFT)뿐이다. 사람 연구자나 다른 하네스가 같은 예산으로 같은 일을 했을 때의 기준선은 없다. → [[RSI-프레이밍]] · [[인간-기준선-조건]]

## 도메인별 추출 (ai-news)
- **신뢰도**: 논문 + MIT 코드(★51, 생성 하루) + 40인 팀. 비교 하네스 4종에 백본을 고정한 점은 좋다([[비매칭-비교]] 기준 통과). 단일 실행이라 미세 격차는 판정할 수 없다.
- **즉시 활용**: **NO(관망)**. 데스크톱 Electron 앱이고 백본은 GLM-5.3 기준이다. 지금 쓰는 Claude Code 하네스를 대체할 근거가 표에 없다. 우위가 있는 곳은 JobBench(+3.73)와 SkillsBench(+1.04) 정도다.
- **6개월 영향력**: "사람이 산출물을 직접 고치는 공유 앱 계층"이 실질적인 차별점이다. 벤치 점수가 아니라 이 UX가 코워크 도구의 경쟁축이 될 수 있다. 24개 사례(웹·게임·PPT·시각화·CAD·Blender)는 정성 비교뿐이다.
- **대체 관계**: [[OpenHands]] · Codex · DSH([[DeepSeek-V4.1-Flash]] 계열 하네스)와 같은 층이다. [[t3code]]처럼 여러 하네스를 묶는 제어면과는 층이 다르다.
- **허와 실**: "최고 성능"은 등가중 평균으로는 맞다. 벤치 단위로 보면 반반이다. 후학습 +9.76은 *하네스가 실험 운영을 끝까지 수행했다*는 증거다. *하네스가 사람보다 낫다*는 증거는 아니다.
- **액션**: 공유 앱 계층 설계(산출물 상태를 사람·에이전트가 같이 쓰는 방식)를 문서로만 읽어 둔다. 설치·실행은 보류한다.

## 관련 페이지
- [[하네스-설계-축]] · [[하네스형-에이전틱-RL]] · [[에이전트-메모리-레이어]] · [[에이전트-스킬]] · [[LongHorizon-Harness]]
- [[OpenHands]] · [[DeepSeek-V4.1-Flash]] · [[GLM-5.3]] · [[Zhipu-AI]] · [[DeepSeek]] · [[Qwen]]
- [[RSI-프레이밍]] · [[RSIHub]] · [[유의성-자기제한]] · [[문서내-값충돌]] · [[한정어-탈락]]
- [[CUA-Master]] · [[uni-robot-agent]] · [[Video-Generation-Agent-Harness]] (같은 날 하네스 논문 3건 동시 도착)

## 원본
- 출처: https://huggingface.co/papers/2611.03178 · https://arxiv.org/html/2611.03178
- 확인 범위: HF `api/papers/2611.03178` · arXiv HTML 본문 §4.1(Table 1 전체)·§4.3(Table 2 전체)·초록·서론 · GitHub API(메타·루트 목록) · 🔴 §4.2 실사용 6범주 정성평가·부록 A.1 벤치별 실행 한도 상세 미확인 · 코드 실행 0회
- 신뢰도: ⭐⭐ (코드 MIT ★51 · 백본 고정 비교 · 단일 실행 · 승패 6:6)
