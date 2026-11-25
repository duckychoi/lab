---
title: "ViDecide — 영상 확산 모델에 단계별 추론 · 계획 학습 (arXiv 2611.26389)"
type: source
domain: video-saas
tags: [video-saas, paper, video-diffusion, planning, causal-prediction, corrective-finetuning, world-model]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.26389]
reliability: medium
---

**논문**: arXiv 2611.26389 · 업보트 **30**(수집기 단건 API 11-24) → **43**(볼트 API 11-25) · 소속 MMLab@NTU · 저자 7명 · 코드 https://github.com/Kevin-thu/ViDecide (★5)

## 핵심 인사이트
> [!insight] 영상 모델이 물리 · 논리를 어기는 원인은 "해답을 고정 길이 클립으로 학습"하기 때문 — 멈출 시점까지 학습시킨다
> 영상 모델의 퍼즐 · 계획 과제 실패의 원인을 **고정 길이 클립 학습**에서 찾고, 상태 전이를 인과적으로 하나씩 예측하며 **멈출 시점도 스스로 결정**하게 학습(Wan2.2-5B 파인튜닝 + DiT-B 처음부터). 실패한 결정의 노이즈를 모델 자신의 성공 연속으로 매핑하는 **Corrective Fine-tuning(CFT)** 은 정책 경사 없이 개선. 영상 생성 모델을 "시각 계획기"로 쓰는 방향의 정량 근거 — [[NoPeWorld]] 와 같은 "영상 모델의 세계 이해" 축.

> [!warning] 퍼즐 크기는 일반화되지만 로봇 배치 변화엔 취약
> 본문 표 1: 제로샷 Seedance 2.5 · Veo 3.1은 FlowFree 0.0%, 최강 기존법 S2PD FlowFree 68.1 · Sokoban 75.7 vs ViDecide(K=1) 77.9 · 83.0. 표 5 CFT 후 84.4 · 90.8(VBVR-MultiStep 82.2 · RoboTwin-Plan 78.0). 초록 평균 83.8% vs 표준 파인튜닝 23.3 · 기존 최강 67.8. **지는 행**: RoboTwin Blocks World Row 75.0 < HDR 86.0, Triangle 50.7 < HDR 56.7. 표 7 분포 밖(OOD): K=1 모델은 Blocks 2×2 4.0% · Hanoi 2×2 2.0%로 양방향 기준선(14.0 · 16.0)보다 나쁨. DiT-B FlowFree Hard는 CFT 27.2 < 단순 연속 SFT 34.4.

## 도메인별 추출 (video-saas)
- **경쟁 우위 빈틈**: 상용 영상 모델(Seedance 2.5 · Veo 3.1)이 계획 과제에서 **0%** — 영상 품질 경쟁과 물리적 일관성 경쟁이 분리되어 있다는 것. 내 SaaS가 "영상을 이해·계획"해야 한다면 생성 품질 SOTA를 써도 안 된다는 근거.
- **프롬프트 패턴**: 클립 길이 고정 학습의 한계 → 단계별 인과 생성 + 종료 토큰. 영상 생성 파라미터 설계(세그먼트 구성)에 참고.
- **액션**: 없음(연구 코드 ★5 단계).

## 관련 페이지
- [[NoPeWorld]] · [[Plan4D]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.26389
- 확인 범위: HF papers API(볼트 11-25 — 업보트 43 · MMLab@NTU · githubRepo 일치) · 본문 표 1 · 5 · 7 및 지는 행(수집기 11-24 판독) · 실행 0
- 신뢰도: ⭐⭐ (평가가 자체 벤치 중심 · ★5 레포)
