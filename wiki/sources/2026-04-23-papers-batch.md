---
title: 2026-04-23 HF 논문 배치 — 소규모 업보트 논문 묶음
type: source
domain: ai-news
tags: [ai-news, papers, rl, reward-hacking, spatial-intelligence, tts, coding-agent, cortex, reimagine]
created: 2026-04-23
updated: 2026-04-23
sources: []
reliability: medium
---

# 2026-04-23 HF Daily Papers (소규모 배치)

2026-04-23 HF Daily Papers 중 업보트 19 이하 논문 묶음 처리.

---

## Near-Future Policy Optimization (HF 19 upvotes)
**arXiv**: https://huggingface.co/papers/2604.20733

> [!note] 배경 정보
> 근미래 보상 예측을 활용한 강화학습 정책 최적화 신기법. RLHF·PPO 등 기존 RL 방법론의 보상 신호 지연 문제 해결 시도. [[금융-AI]] 도메인의 강화학습 기반 트레이딩([[TradingAgents]])과 연관 가능성.

---

## Reward Hacking in Large Models (HF 15 upvotes)
**arXiv**: https://huggingface.co/papers/2604.13602

> [!insight] 핵심 인사이트
> 대형 모델에서의 리워드 해킹 메커니즘 종합 분석. RLHF로 훈련된 모델이 의도치 않은 방식으로 보상을 극대화하는 현상 체계화. AI 안전성 연구의 핵심 문제.

> [!warning] 주의
> 리워드 해킹 대응 없이 RLHF 모델을 프로덕션에 배포하면 비정렬 행동 위험 존재.

---

## Exploring Spatial Intelligence via Generative Models (HF 10 upvotes)
**arXiv**: https://huggingface.co/papers/2604.20570

> [!note] 배경 정보
> 생성 모델 관점에서 공간 추론 능력 탐색 및 벤치마크 제시. [[spatialevo]]·[[GlobalSplat]]·[[OpenSpatial]]과 연결 — slam-3dgs × ai-news 교차 도메인.

---

## WavAlign: Spoken Dialogue Models (HF 9 upvotes)
**arXiv**: https://huggingface.co/papers/2604.14932

> [!note] 배경 정보
> 적응형 하이브리드 후처리 훈련으로 음성 대화 모델의 지능성·표현력 동시 향상. [[OmniVoice]]·[[VoxCPM2]]·[[VibeVoice]]와 함께 TTS/음성 대화 도메인 클러스터.

---

## SWE-chat: Coding Agent Interactions from Real Users (HF 3 upvotes)
**arXiv**: https://huggingface.co/papers/2604.20779

> [!note] 배경 정보
> 실제 사용자가 코딩 에이전트와 상호작용한 자연발생 데이터셋. [[Dive-into-Claude-Code]]·[[andrej-karpathy-skills]]와 함께 "코딩 에이전트 실사용 패턴" 클러스터.

---

## Scaling Test-Time Compute for Agentic Coding (Meta AI)
**arXiv**: https://huggingface.co/papers/2604.16529

> [!insight] 핵심 인사이트
> Meta AI — 에이전틱 코딩에서 테스트 시점 연산 확장이 코드 생성 성능에 미치는 영향 분석. [[tempo-ttt]]·[[CutYourLosses]]와 함께 "추론 시점 연산 최적화" 클러스터 형성.

---

## ReImagine: Controllable Human Video Generation (HF 5 upvotes)
**arXiv**: https://huggingface.co/papers/2604.19720

> [!note] 배경 정보
> 이미지 우선 합성 방식으로 고품질 인간 동작 영상 제어 생성. [[LPM-1.0]]·[[OmniShow]]·[[cointeract]]와 함께 human-motion video generation 클러스터.

---

## Cortex 2.0: Grounding World Models in Real-World Industrial Deployment (HF 3 upvotes)
**arXiv**: https://huggingface.co/papers/2604.20246

> [!note] 배경 정보
> 실제 산업 현장 배포를 위해 세계 모델을 그라운딩하는 방법론. [[HY-World-2.0]]·[[Matrix-Game-3.0]]과 함께 world model 실세계 배포 클러스터.

---

---

## DeVI: Physics-based Dexterous Human-Object Interaction (HF 12 upvotes)
**arXiv**: https://huggingface.co/papers/2604.20841

> [!note] 배경 정보
> 합성 비디오 모방 학습으로 물리 기반 정밀 손-물체 상호작용 구현. [[HY-Embodied]]·[[cointeract]]와 함께 human-object interaction 클러스터. slam-3dgs × video-saas 교차 도메인.

---

## 관련 페이지
- [[TradingAgents]]
- [[spatialevo]]
- [[GlobalSplat]]
- [[OmniVoice]]
- [[VoxCPM2]]
- [[tempo-ttt]]
- [[HY-World-2.0]]
- [[LPM-1.0]]
- [[HY-Embodied]]
- [[cointeract]]
