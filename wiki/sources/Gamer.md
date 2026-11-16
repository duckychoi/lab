---
title: "Gamer — 키보드·마우스로 2D/3D 게임을 조작하는 범용 VLA 게임 에이전트 (실시간 평균 31.5 vs 범용 17.6)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, vla, game-agent, embodied, reinforcement-learning, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.18397]
reliability: medium
---

**논문**: arXiv 2611.18397 · HF Daily 11-16 **1위** · 업보트 **61**(볼트 · 수집기 59) · 코드 [RainBowLuoCS/Gamer](https://github.com/RainBowLuoCS/Gamer) ★124 · 프로젝트 mihoyo-gamer.github.io.

## 핵심 인사이트
> [!insight] "반복적인 키보드·마우스 궤적도 스케일하면 된다"
> 화면 픽셀 → 실제 키 · 마우스 입력. Qwen3.5/Qwen3-VL 기반, 수만 시간 장치 수준 조작 궤적으로 CPT(게임 85% + 일반 멀티모달 15%) → 희소 사고 SFT → 유한 컨텍스트 · 누적 오차 · 희소 보상을 다루는 다중 턴 RL → 클라우드–엣지 추론(Streaming-vLLM). 게임은 물리 · 디지털 성질을 함께 가진 환경이라 [[VLA]] 의 값싼 데이터원이다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA (arXiv HTML 표 5 · 볼트 확인)**: 4개 공개 게임 벤치 **실시간 평균** Gamer-8B-CPT **29.5** · Gamer-35B-A3B-CPT **31.5** vs 범용 최강 GPT-5.6-Sol **17.6** · Claude-Opus-5.0 **17.3**. 범용 모델은 일시정지 평가 대비 실시간에서 최대 **−34.5** 하락(GPT-5.6-Sol 평균 열).
- **붕괴:스타레일 사이드퀘스트(표 6)**: Gamer-RL 정확도 80.0% · 83.6% vs Gemini-3.8-Flash 16.7% · 45.5%.
- **실시간 가능성**: 클라우드–엣지 분리로 다수 환경 동시 서빙(지연 수치는 초록에 없음).
- **응용 가능성**: 로봇 원격조작 데이터 대신 게임 궤적으로 사전학습하는 경로.

> [!warning] 단서 (수집기 판독 + 볼트 표 대조)
> ① 초록 "숙련 플레이어에 필적(comparable to skilled players)"은 정성 표현 ② HSR 평가는 HSR 데이터로 별도 학습한 체크포인트 — [[분포내-우위]] ③ 퍼즐 유형은 RL 이 SFT 보다 낮음(22.2 → 11.1, 표 6 행 볼트 확인) ④ 실시간 하락 폭은 범용 모델이 실시간 조작용으로 설계되지 않은 탓도 있어 [[비매칭-비교]] 성격.

## 관련 페이지
- [[VLA]] · [[임바디드-AI]] · [[월드모델]] · [[Agentic-Robotics-Roadmap]](같은 날 · 하네스 쪽 반대 노선) · [[분포내-우위]] · [[비매칭-비교]] · [[Qwen]]

## 원본
- 출처: https://huggingface.co/papers/2611.18397 · https://arxiv.org/html/2611.18397
- 확인 범위: HF papers API 초록 · arXiv HTML 표 5 · 6 수치 문자열 대조(볼트) · 🔴 학습 데이터 규모 · 스케일링 연구는 수집기 판독
- 신뢰도: ⭐⭐⭐ (본문 표 · 코드 공개)
