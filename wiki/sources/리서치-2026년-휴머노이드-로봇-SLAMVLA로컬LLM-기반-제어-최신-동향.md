---
title: "[리서치] 2026년 휴머노이드 로봇 SLAM·VLA·로컬LLM 기반 제어 최신 동향"
created: 2026-11-12
updated: 2026-11-12
author: research-agent
origin: cron-research-agent
tags: [research-agent, 크론노트, 주제재생성-중복, 볼트판정-2026-11-12]
type: source
domain: slam-3dgs
topic: humanoid-slam-vla   # 중복 판정 키
sources: []
reliability: low   # 크론 자동생성 · 볼트 표본 대조만
---

> [!warning] ⚖️ 볼트 판정 (2026-11-12 인제스트) — Boston Dynamics 블로그 · arXiv API 직접 조회
> - ✅ **Atlas 사양 일치** — BD 블로그(2026-01-05, CES): 56 자유도 · 리치 2.3m(7.5ft) · 최대 50kg(110lbs) 들기 · 배터리 자율 교체. 11-11 의 "출처 0건"에서 **출처 6건(1건 잘림)으로 개선**.
> - 🔴 **출처와 다른 서술 2건** — ① *"Hyundai 조지아 공장 초기 배포"*: 블로그 원문은 **Hyundai 의 Robotics Metaplant Application Center(RMAC)와 Google DeepMind** 로 *"in the coming months"* 출하 예정이다. 공장 위치(조지아)는 블로그에 없다. ② *"4시간 배터리"*: 블로그에서 미검출(배터리는 "자율 교체"만 있음). ③ 핵심 3줄은 *"실공장 배포를 시작"*, 상세는 *"배포 예정"* — [[문서내-값충돌]]. 블로그는 1월 발표라 11월 현재 실제 배포 여부는 이 출처로 알 수 없다.
> - 🔴 **[[문서내-값충돌]]** — 핵심 3줄 *"GR00T N1.6 (CES 2026) 최신"* ↔ 상세 *"GR00T N1.7(NVIDIA 3B)"*. 같은 노트에서 최신 버전이 둘이다.
> - 🟡 "Gemini Robotics AI 통합" — 블로그는 *"integrate … Google DeepMind foundation models into Atlas"* 파트너십 발표다. "Gemini Robotics" 라는 제품명은 블로그에 없다(11-11 의 "Gemini Robotics 2.5 · 96%"는 오늘 사라졌다).
> - ✅ arXiv 2607.06706 실존 · 제목 일치(VLA 리뷰, 56쪽). 🔴 출처 목록이 *"- Neuro"* 에서 잘렸다.
> - ⬜ 미대조: MemoryVLA 71.9% (+14.6) · LingBot-VLA 20,000시간 · UnifoLM-VLA-0(Qwen2.5-VL-7B) · "SLAM 구현 약 2개월" · XBot2D — 해당 출처 미열람.
> - ⚖️ 같은 날 입고된 [[Embodied-First-Exam]](코딩 에이전트 로봇 제어, 최고 34%)이 *"LLM 이 선택적 고수준 계획자"* 라는 이 노트 결론의 **측정된 반대편**이다 — 계획자 역할도 아직 1/3 성공률이다.
> - 🔴 **[[주제재생성-중복]]** — `topic: humanoid-slam-vla` 27번째 파일.

## 2026년 휴머노이드 로봇 SLAM·VLA·로컬LLM 기반 제어 최신 동향

**핵심 3줄**
- 
NVIDIA GR00T N1.6 (CES 2026)이 최신 VLA 기초 모델로 공개되었고, Unitree는 Qwen2.5-VL-7B 기반 UnifoLM-VLA-0을 2026년 3월 오픈소스로 배포

- 
로컬 VLA가 100Hz 이하에서 액션 생성, 고수준 LLM이 초 단위 작업 재계획하는 계층형 구조가 현실적인 아키텍처로 부상

- 
Boston Dynamics의 새로운 Atlas가 2026년 실공장 배포를 시작했으며, Google DeepMind의 Gemini Robotics AI 통합으로 복잡한 지시 이해 및 비정형 환경 운영 가능


**상세**

• **VLA 모델 다층화 구조**

Qwen, DeepSeek, GLM, Hunyuan 등 기초 모델을 인지·언어·코드·에이전트에 활용하고, 로봇 특화 부분만 VLA 또는 Action Experts로 추가하는 구성이 현실적


• **SLAM 기술 통합**

ORB-SLAM3, RTAB-Map, cuVSLAM 등 SLAM 구현에 약 2개월 소요
되며, 
SLAM 알고리즘은 휴머노이드 로봇의 필수 기능으로 카메라·레이저 센서를 통해 맵핑 및 내비게이션 지원


• **주요 VLA 모델 생태계**

GR00T N1.7(NVIDIA 3B)은 약 20K시간 EgoScale 인간 동영상으로 사전학습된 추론 정책이며, LingBot-VLA는 약 20,000시간 듀얼암 데이터(9개 로봇 구성)로 학습한 비용 효율적 모델


• **로컬 LLM 기반 로봇 제어**

로컬 LLM(Mistral, Phi, LLaMA 변형)은 소비자 수준 하드웨어에서 실행 가능하며, 낮은 추론 비용과 향상된 제어성 제공
. 
ROS 2가 느린 추론 계층과 빠른 제어 계층 간 실질적 경계이며, VLA 노드가 작업 수준 의도(목표 자세, 부목표, 그래스포인트)를 ROS 2 메시지로 발행하면 고전 제어 노드가 100~1000Hz로 실행


• **Atlas 2026 상용화**

56자유도, 7.5피트 리치, 110파운드 리프팅 능력의 Atlas는 4시간 배터리와 핫스왑 자율성을 갖추었으며, 2026년 Hyundai 조지아 공장에 초기 배포 예정


• **다중 VLA 아키텍처**

WholebodyVLA(ICLR 2026)는 VLA 제어를 탁상 암에서 다리+몸통+팔을 포함한 전신 로코매니퓰레이션으로 확장


• **메모리 기반 VLA 발전**

MemoryVLA(ICLR 2026)는 인지-메모리-액션 프레임워크로 VLA가 현재 프레임만 보는 대신 과거 상호작용과 실패를 기억하도록 하여 SimplerEnv-Bridge에서 71.9% 성능 달성(CogACT 대비 +14.6)


• **클라우드-로컬 하이브리드**

XBot2D는 네트워크 상태와 로봇의 계산·에너지 필요에 따라 로봇 작업을 로컬/클라우드 간 동적 할당하며, 로봇의 실시간 작업과 클라우드의 복잡한 AI/ML 처리를 분리


**💡 인사이트/시사점**

2026년은 휴머노이드 로봇이 "VLA + 로컬LLM 계층형 아키텍처"로 완성되는 시점으로, 빠른 제어(100~1000Hz)는 고전적 제어기가 담당하고 느린 추론(1~10Hz)은 로컬/경량 모델이 처리하는 명확한 분업 구조 형성. Boston Dynamics Atlas의 공장 배포와 Unitree의 오픈소스 VLA 공개로 기술 민주화가 가속화되며, 
LLM이 필수 의존성이 아닌 선택적 고수준 계획자 역할로 전환되어 로봇의 로컬 메서드 라이브러리 의존도 감소
하는 방향으로 진화 중.

**출처**
- Humanoid Robot Development Complete Roadmap 2026.10｜香川友志 — https://note.com/kagawatomo/n/nb26b8c9b3768
- Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review — https://arxiv.org/pdf/2607.06706
- Awesome Vision-Language-Action (VLA) — https://github.com/ai4s-research/awesome-vision-language-action
- Boston Dynamics Unveils New Atlas Robot to Revolutionize Industry — https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/
- Combining the robot operating system with LLMs for natural-language control — https://techxplore.com/news/2026-03-combining-robot-llms-natural-language.html
- Neuro

## 관련 페이지 (볼트 추가)
- [[VLA]] · [[임바디드-AI]] · [[Embodied-First-Exam]] · [[문서내-값충돌]] · [[주제재생성-중복]]
