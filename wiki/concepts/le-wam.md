---
title: "LeWAM — LeWorldModel + Action + Flow Matching + RoPE"
created: 2026-11-22
author: fryday
tags: [concept, world-model, jepa, flow-matching, rope, action-conditioned, ledger-38]
ledger: 38
status: 판정-종료—살아남은신호는#36으로합류(2026-11-24)
---

# LeWAM (#38)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **종료 — 살아남은 신호는 #36으로 합류**
> 물성 분포 계획: 베이즈−MAP ≈ 0(70.6% vs 71.7%). 남은 격차 중 물성 몫 +0.5%p, 가려진 마지막 '상태' 몫 +28.9%p → #36 관문 10으로. 물성이 정해지면 미래가 결정론적인 무대에선 점예측이 최적.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 교수님 아이디어: LeWM에 flow matching·RoPE가 들어갈 자리 분석.

## LeWM 구조 (arXiv 2603.19312)
인코더 ViT→**CLS 벡터 1개/프레임**. 예측기=인과 트랜스포머, **행동=AdaLN(zero-init)**, **결정론 MSE** `‖ẑ'−z'‖²` + **SIGReg**(임베딩→등방 가우시안 N(0,I), 붕괴방지). 위치인코딩=학습형. 계획=CEM/MPC. 한계: 결정론→다봉 평균, 롤아웃 오차누적→짧은 지평.

## 🟢 삽입점 분석
**① Flow = 예측기 MSE 헤드 교체** → 조건부 flow $v_\theta(z'^\tau,\tau|z,a)$, 행동은 기존 AdaLN 재사용.
- 💎 **SIGReg × flow 시너지**: SIGReg가 latent을 N(0,I)로 → **flow base가 공짜**. 궁합 최적.
- 이득: 행동조건부 다봉 미래 보존. 계획=CEM 샘플 롤아웃 기대비용.

**② RoPE = 예측기 시간축 PE 교체** → 상대시간·주기 + **지평 외삽**(LeWM 짧은지평 한계 직격). 변형: 패치토큰 latent+공간 RoPE("시공간 자유롭지 않은 latent").

## toy (note:le-wam)
행동분기 a=0 다봉/a=±1 단봉. 결정론 a=0→갭(붕괴), flow a=−1→좌0.82/a=+1→우0.81/a=0→양쪽. 행동이 분포 조절 실증 ✅.

## 두 기여
① 가우시안 정규화 latent=native flow base(SIGReg×flow) ② RoPE로 월드모델 지평 외삽.

## 연결
[[generative-jepa]] #37 · JEPA/WM #25 · [[pf-generative-flow]] #35 · [[physics-potential-smc]] #36 · 스펙트럼 위상 #28 · 모션 flow #34.
