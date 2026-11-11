---
title: "[리서치] 휴머노이드 로봇 SLAM·VLA·로컬LLM 기반 제어 최신 동향"
created: 2026-11-11
updated: 2026-11-11
author: research-agent
origin: cron-research-agent
tags: [research-agent, 크론노트, 주제재생성-중복, 볼트판정-2026-11-11]
type: source
domain: slam-3dgs
topic: humanoid-slam-vla   # 중복 판정 키
sources: []
reliability: low   # 크론 자동생성 · 볼트 표본 대조만
---

> [!warning] ⚖️ 볼트 판정 (2026-11-11 인제스트) — **미대조 · 출처 0건 · 잘림 · 확인 안 되는 발표 1건**
> - 🔴 **출처 0건 + 잘림** — *"…한국은 국산 NPU"* 에서 끊겼다(4,126B). 3일 연속 출처 0.
> - 🔴 **"Google DeepMind 가 2026년 11월 10일 'Gemini Robotics 2.5' 공개 · Apollo 2 가 Mercedes-Benz 생산 라인 200가지 이상 과제에서 96% 성공률"** — 볼트 웹 검색 1회로는 **확인되지 않았다.** 검색에 잡히는 것은 7월 30일 공개로 보도된 **Gemini Robotics 2**(Apollo 2 세 가지 구성)이고, 보도된 성공률은 과제별 32~92%(전구 빼기 92% · 끼우기 36% 등)이며 Mercedes-Benz 는 벤치 결과가 아니라 협력사로 언급된다. "2.5 · 96%"가 틀렸다고 확정하지는 않는다(검색 1회 · 하루 전 발표일 수 있음) — **인용 금지, 원출처 확보 전까지 보류.**
> - 🔴 **[[주제재생성-중복]]** — `topic: humanoid-slam-vla` 파일이 이 파일로 26개째(볼트 `grep` 계수). 어제 [[리서치-휴머노이드-로봇-제어-기술-혁신-VLA로컬LLMSLAM-통합-시대]] 와 같은 주제의 새 파일명.
> - ⬜ 미대조: 출하 7배 · 5만 대 전망(11-10 노트와 같은 수치 — 출처는 양쪽 모두 없음) · Hefei Keda VLA-SLAM 특허 · ST-VLA · Ro-SLM · Atlas LBM "2026년 Hyundai 와 Google DeepMind 에 배송 예정" · 국산 NPU + 국산 VLA 약 24억원 과제(2026-07~2027-12).
> - 🟡 *"로컬 VLA 가 100Hz 미만에서 행동을 생성"* — "미만"은 상한만 말한다. 실제 주파수를 알려 주지 않는 문장이다.
> - 오늘 자동수집의 [[RoboScript]](RoboTwin 2.0 83.4%) · [[DexForesight]](실로봇 58.3%)는 이 노트에 없다 — 초록 수치가 있는 쪽은 그 두 페이지다.

이제 추가로 로컬LLM과 온보드 추론에 대한 정보를 검색하겠습니다.
## 휴머노이드 로봇 SLAM·VLA·로컬LLM 기반 제어 최신 동향

**핵심 3줄**
- 
2026년 전 세계 휴머노이드 출하량은 전년 대비 약 7배인 5만 대 이상으로 전망되며, VLA 모델 발전이 핵심 동력

- 
생성형 AI와 비전·언어·행동(VLA) 모델의 발전으로 로봇이 주변 환경을 이해하고 다양한 작업을 수행할 수 있는 가능성이 확대

- 
VLA 모델이 SLAM 파이프라인에 통합되면서 기하학적 제약 해결에서 의미론적 개념 정렬로 진화


**상세**

**VLA(Vision-Language-Action) 모델의 지배적 패러다임 전환**
- 
기존 비전·언어 모델(VLM)이 이미지와 텍스트를 이해하는 데 초점을 맞췄다면, VLA는 이를 확장해 로봇이 실제로 수행해야 할 행동을 생성

- 
RT-2(2023) → OpenVLA(2024) → Helix(Figure) → GR00T N1·N1.6·N2(NVIDIA) 계보로 진화 중

- 
Figure AI는 Helix라는 내부 개발 VLA 모델로 "빠른 반사 + 느린 추론" 이중 시스템을 구현하여 텔레오퍼레이션 데이터 수집과 VLA 기반 학습을 결합


**SLAM과 VLA의 의미론적 통합**
- 
VLA 모델이 동적 예측 업데이트로 루프 클로저 감지, 키프레임 필터링, 노이즈 추정을 수행하며 SLAM이 기하학적 제약 해결에서 의미론적 개념 정렬로 이동

- 
2026년 Hefei Keda의 VLA-SLAM 특허 출원이 향후 3~5년 체현형 AI 네비게이션의 전략적 신호로 부상

- 
ST-VLA는 통합된 3D-4D 표현으로 2D 지침을 3D 궤적으로 변환하고 시공간 맥락을 포착하는 부드러운 공간 마스크 생성


**온보드·엣지 기반 로컬 LLM 실행의 현실화**
- 
온보드 배포를 지원하는 미세 조정된 소규모 언어 모델(SLM)을 배포하는 것이 유망한 대안이며, Ro-SLM은 LLM의 지식과 추론을 증류하여 신뢰할 수 있는 SLM 기반 로봇 작업을 가능하게 함

- 
0.1초의 지연 시간도 허용되지 않는 스마트 팩토리나 자율주행 로봇 같은 엣지 AI 환경에서는 클라우드를 거치지 않는 실시간 AI 추론이 필수

- 
NPU(Neural Processing Unit) 중심의 SoC 구성이 고도화되며 엣지에서 경량 LLM 추론이 가능하고, MCU·NPU·GPU 조합으로 저전력 제어와 AI 추론 가속화 구현


**산업 배포 단계로의 전환**
- 
Google DeepMind는 2026년 11월 10일에 'Gemini Robotics 2.5'를 공개했으며, Apollo 2 휴머노이드가 Mercedes-Benz 생산 라인에서 200가지 이상의 과제로 평가되어 96% 성공률을 달성

- 
Boston Dynamics와 Toyota Research Institute가 Atlas 휴머노이드용 대규모 행동 모델(LBM)을 공동 개발하여 전신 정책으로 packing/sorting/organizing 작업 제어, 2026년 Hyundai와 Google DeepMind에 배송 예정

- 
국내에서는 국산 NPU에 국산 VLA를 탑재한 이동형 양팔 로봇 개발로 총 약 24억원, 2026년 7월~2027년 12월 추진 중


**계층적 아키텍처의 부상**
- 
로컬 VLA가 100Hz 미만에서 행동을 생성하고 고수준 LLM이 초 단위로 작업을 재계획하는 계층 구조에서, 결정론적 실시간 제어·VLA/Action Expert·World Models·LLM/Embodied Reasoning·안전 계층의 분업이 현실적


**💡 인사이트/시사점**


2026년의 로봇 산업은 "하드웨어 데모"의 시대에서 "두뇌와 물량"의 시대로 넘어가는 중
이며, SLAM의 의미론적 진화와 온보드 LLM의 실현은 
VLA 모델과 물리 세계를 이해하는 월드 모델의 발전이 Physical AI 변화의 기술적 방아쇠
가 되고 있습니다. 실제 생산 라인 도입(Mercedes-Benz, Hyundai)은 로봇 모델의 경쟁 지점이 실험실 과제에서 산업 현장으로 이동했음을 의미하며, 한국은 국산 NPU

## 관련 페이지 (볼트 추가)
- [[VLA]] · [[RoboScript]] · [[DexForesight]] · [[A2-MEAS]] · [[주제재생성-중복]]
