---
title: "STSA — 초격자(슈퍼트위스팅) 확률근사: 칼만·RL 통일 오차보정 골격의 2차 일반화"
created: 2026-11-18
author: fryday
tags: [concept, reinforcement-learning, kalman, super-twisting, sliding-mode, stochastic-approximation, convergence, ledger-32]
ledger: 32
status: research-program
---

# STSA — Super-Twisting Stochastic Approximation (STW-TD)

> 발단(교수님 관찰): 칼만 갱신 $x\leftarrow x+K(z-Hx)$ 과 RL 갱신 $V\leftarrow V+\alpha(G-V)$ 가 "너무 비슷"하다.

## 1. 통일 골격 — 오차보정(error-driven) 업데이트
$$\text{새 추정} = \text{옛 추정} + (\text{게인})\times(\text{관측} - \text{예측})$$
- 칼만: $x\leftarrow x+K(z-Hx)$, innovation $=z-Hx$, 게인 $K$.
- TD(0): $V\leftarrow V+\alpha(r+\gamma V'-V)$, innovation $=\delta$(TD 오차), 게인 $\alpha$.
- 대응: 상태 $x\leftrightarrow V$, 측정 $z\leftrightarrow G_t$(또는 $r+\gamma V'$), innovation $z-Hx\leftrightarrow\delta$, $K\leftrightarrow\alpha$.
- 공통 뿌리: **1차 확률근사(Robbins–Monro)**. 칼만·TD·SGD·미러하강·자연경사는 전부 특수경우/기하 재표현.

### 결정적 차이 = 게인을 "계산" vs "정함"
- 칼만: $K=PH^\top(HPH^\top+R)^{-1}$, 공분산 전파 $P\leftarrow FPF^\top+Q$ → 불확실성으로 자동 조절. 모델 앎.
- RL: $\alpha$ 는 하이퍼파라미터(또는 $1/N$). 불확실성 추적 X. 모델 모름.
- 간극 메우기 = **KTD**(아래).

## 2. 선행: 칼만 기반 RL (KTD 라인)
- KTD — Geist & Pietquin, JAIR 2010 (arXiv 1406.3270).
- Managing Uncertainty within KTD — ADPRL 2011 (KTDQ, 능동학습).
- MM-KTD 2020 (arXiv 2006.00195) · KTD×Successor Rep 2019 (arXiv 1910.02532) · Adaptive KTD 멀티에이전트 2022 · Generalized Kalman-filter TD 2026 (arXiv 2607.20010).
- 요지: 불확실성 추적 → 적응 학습률·탐험(UCB/Thompson) 연결. 딥넷에선 공분산 $P$(파라미터²) 전파가 비현실적 → 앙상블이 "가난한 칼만".

## 3. 제안: STSA (Super-Twisting Stochastic Approximation)
통일 골격의 암묵 가정 3개 — (i) 가산적(유클리드) (ii) 1차·무기억 (iii) 점추정 — 중 **(ii)를 깸**: 혁신 $\delta_t$ 를 **분수차 비선형 + 적분 기억**으로.

$$\theta_{t+1} = \theta_t + \alpha\big(-k_1|\delta_t|^{1/2}\mathrm{sign}(\delta_t) + u_t\big)$$
$$u_{t+1} = u_t - \alpha\,k_2\,\mathrm{sign}(\delta_t)$$

$\delta_t$ = TD 오차(혁신). 구조적 신규성 = ① 분수차 맵 $|\delta|^{1/2}\mathrm{sign}$, ② **적분 상태 $u$**(혁신 2차 기억) → "증강 2차 골격".

### 왜 더 강한가 (결정론에서 증명된 성질)
1. **유한시간 수렴**(점근 아님).
2. **유계 교란 완전 상쇄**(적분항 $u$ 가 bounded bias 제거 → 강인성). 1차 가산식 불가.
3. **분수차**: 멀면 빠르게·가까우면 미세하게(채터링 없는 연속판).

### 엄밀성 — 결정론 백본 (이미 증명됨)
Moreno–Osorio 엄격 Lyapunov:
$$V=\zeta^\top P\zeta,\quad \zeta=[\,|\delta|^{1/2}\mathrm{sign}(\delta),\,u\,]^\top,\quad \dot V\le-\kappa V^{1/2}\ \Rightarrow\ \text{유한시간}$$
결정론·유계노이즈 STW에서 엄밀 증명 존재 (Moreno-Osorio; Automatica 2013; constrained-opt via SMC arXiv 2604.27587).

## 4. 🟢 빈 땅 (검색 확인: STW×확률근사 유한시간 증명 없음) = 기여 지점
- 난관: ① RL 노이즈 = 제로평균 마팅게일 차분(STW의 유계·Lipschitz 교란 가정 깨짐) ② $\mathrm{sign}$ 불연속 + 노이즈 → 노이즈 볼 채터링.
- 증명 전략: $\alpha_t\to0,\ \sum\alpha_t=\infty,\ \sum\alpha_t^2<\infty$ + 확률 Lyapunov(초마팅게일) + ODE 방법(극한 ODE가 비평활·유한시간 안정). $\mathrm{sign}$ 은 Filippov 해 + 확률평균화.
- 기대 정리: "정확한 유한시간"이 아니라 **"유한시간에 노이즈 볼 도달 + 가속 수렴률"**. ← 이게 증명 타깃.
- ⚠️ 정직: 아직 증명된 정리 아님. 결정론 백본은 엄밀, 확률 확장은 **출판가능 연구 프로그램**.

## 5. 대안 골격 (더 야심, 일부 기지)
측도수송(Wasserstein 자연경사) — 점추정 대신 분포 수송. 분포 RL 벨만 수축(Wasserstein contraction)은 증명됨, "수송맵=업데이트 골격"은 부분적만 알려짐.

## 6. 연결
- [[research-topics-ledger]] #32.
- #7 슈퍼트위스팅×빔포밍 · #9 sliding-as-optimization(s=∇J) 를 **학습 업데이트 골격**으로 정식화.
- #8 공간 슈퍼트위스팅 개구(물리 STW) ↔ STSA(학습 STW) = twist의 물리/학습 쌍.
- 불확실성 인식 탐험(KTD) ↔ 앞선 탐험·활용·신용할당 스레드.

## 7. 다음 단계
- 확률 STW 유한시간 Lyapunov 증명 스케치 심화(가정·보조정리).
- STW-TD 1D 수치 시뮬: TD(0) vs STW-TD 수렴속도·강인성.
