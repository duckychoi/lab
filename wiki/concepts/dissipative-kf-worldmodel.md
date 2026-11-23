---
title: "소산성 신경 KF 세계모델 — extended dissipativity로 학습된 샘플프리 world model"
created: 2026-11-23
author: fryday
tags: [concept, kalman-filter, world-model, dissipativity, energy-based, mamba, ssm, ledger-39]
ledger: 39
status: research-program (아이디어+toy)
---

# 소산성 신경 KF 세계모델 (#39)

> 교수님 아이디어: KF는 PF와 달리 **샘플 없이 예측–보정** → 효율적 세계모델. **extended dissipative performance**(에너지 지표)로 학습해 소산적=안정 필터를, Mamba/Transformer로.

## 선행 vs 빈땅
- 실재: **KalmanNet**(칼만게인 NN 학습)·DynaNet·DL-KF(2026)·KalmanTNet / **KalMamba**(Mamba latent SSM→KF+스무딩, POMDP 세계모델)·Mamba-2+EKF. → "샘플프리 신경 KF 세계모델"+"Mamba 궁합"은 검증·일부 구현.
- 🟢 **빈땅**: **extended dissipativity(H∞·L2-L∞·passivity 통합)를 학습 목적으로** 쓴 신경 KF/SSM 세계모델은 없음 = novel.

## 왜 소산성
세계모델은 계획 위해 **관측 없이 상상 rollout** → 불안정(ρ>1)이면 발산(LeWM #38 롤아웃 드리프트의 근본 원인). 소산성=에너지 발산 안 함=Lyapunov 안정 → 장기 rollout 유계.

## toy (note:dissipative-kf-worldmodel)
노이즈 짧은 궤적 선형 SSM 적합(sample-free). plain vs dissipative(ρ≤0.98 투영).
plain: 불안정 11%·발산 1%·최대norm 16.0 / dissip: 0%·0%·최대 0.5. → 소산성이 상상 안정성 보장.

## 설계
Mamba(선택적 SSM=학습 상태전이) + 칼만 보정 헤드(게인/공분산) + **extended dissipativity LMI를 미분가능 패널티/구조적 만족**. 안정·강인(H∞/passivity) 보장 세계모델 → MPC/latent 계획 신뢰↑.

## 연결 (🧭 나침반 전적 부합)
[[super-twisting-stochastic-approximation]] #32(칼만≈RL·강인) · [[le-wam]] #38(rollout 안정화) · [[pf-generative-flow]] #35(PF=샘플·다봉 ↔ KF=샘플프리·단봉, 상보) · 에너지기반·샘플효율·물리·학계 소규모 전적 부합.
