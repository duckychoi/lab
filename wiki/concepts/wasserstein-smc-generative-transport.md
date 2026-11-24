---
title: "Wasserstein-SMC 생성수송 — 연속성 방정식 전개를 예측-리샘플링 골격으로 대체"
created: 2026-11-21
author: fryday
tags: [concept, flow-matching, diffusion, particle-filter, sequential-monte-carlo, optimal-transport, wasserstein, ledger-35]
ledger: 35
status: 판정-종료(#35에포함)(2026-11-24)
---

# Wasserstein-SMC 생성수송 (W-SMC-Gen)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **종료(#35에 포함)**
> #35와 같은 판정: NFE 정직 집계 시 Heun 승, 오라클 밀도 의존. 정책판(FM 정책×e^{Q/β})도 재표집 고유 이득 없음, 학습된 Q_t는 CGQL-Linex·CEP가 선점.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 발상 경로: 텔레그램 대화. #32 에서 "칼만 ≈ RL 갱신식 = 예측-보정 골격"을 본 직후의 다음 질문 — **"FM·확산은 ODE/PDE(연속성 방정식)로 전개하는데, 그걸 입자필터(PF/SMC)로 대체하면 어떠냐"**. GS-PF(동적 3DGS 입자필터) 아이디어와 같은 골격의 생성모델 판.

## 1. 발상 — 현재 생성은 "보정 없는 입자 전개"다

- FM/확산의 수학적 본체: 연속성 방정식 $\partial_t p_t + \nabla\cdot(p_t v_t)=0$, $p_0=\mathcal N(0,I)\to p_1=p_{data}$.
- 실전 구현: 확률 플로우 ODE를 Euler/Heun로 풂 — $X_{k+1}=X_k+h_k v(X_k,t_k)$, $N$개 입자의 경험분포 $\hat\mu=\frac1N\sum\delta_{X^i}$.
- **관찰**: 이 골격은 #32 의 "새 추정 = 옛 추정 + 게인×(관측−예측)"에서 **보정항이 0인 특수상태**다. 예측(전파)만 K스텝 반복하고, 이산화 바이어스 + MC 표본 표류가 전부 누적된다. 칼만/TD에는 있던 "오차에 비례한 되돌림"이 생성 파이프라인에는 없다.
- **제안**: 시간축을 따라 **예측(전파) + 보정(가중치·리샘플링)** 을 도는 Feynman–Kac(SMC) 골격으로 교체. 입자가 살아가는 공간이 분포 공간 = **와서스타인 공간**이므로, 전파 오차와 보정 오차를 $W_2$ 메트릭으로 합성할 수 있다(KL은 삼각부등식이 없어 오차 합성에 못 쓴다 — W2를 고르는 이론적 이유).

## 2. 형식화

- Feynman–Kac 형식: $\gamma_k \propto \eta_k G_k$. 전파 커널 $M_k$ = Euler 스텝(학습 제안으로 대체 가능), 가중치 갱신 $w^i \propto w^i G_k(X^i)$, twist $G_k=\exp(\psi_{t_k})$.
- twist $\psi_t(x)\approx\log\tilde p_t(x)$ — **중간 주변분포 밀도 추정**. 학습은 TDS식 회귀(역방향 스냅샷 밀도비 회귀).
- 리샘플링: 다항/체계적/**OT-리샘플링**(와서스타인 바리센터 사영 — 분산 상수 최소).
- **ESS-적응 스텝**: $\mathrm{ESS}=1/\sum_i (w^i)^2 < \tau$ 일 때만 리샘플·세분화 → **NFE 절약이 골격의 부산물**로 나온다.

## 3. 정직한 역학 — 리샘플링은 무엇을 고치는가

- Euler 입자는 무가중치라 고전적 "가중치 퇴화"가 원래 없다. **리샘플링이 고치는 것은 twist $\psi_t$라는 중간분포 추정과 입자구름의 괴리(MC 표본 표류)다.**
- 따라서 twist 품질이 전부: $\psi$가 좋으면 굵은 스텝의 분포 표류를 중간분포 쪽으로 끌어당겨 교정하고, 나쁘면 편향을 주입한다. 조건부 생성(FKC 계열)에서는 관측 가능도가 twist을 공짜로 주지만, **무조건 생성에서는 $\psi_t$ 학습이 곧 연구 문제**다.
- 결론: 기여 본체 = (i) 무조건 생성용 twist 학습, (ii) W2 오차합성 정리, (iii) OT-리샘플·ESS-적응 스텝의 시스템화.

## 4. 🟢 열린 정리 (기여 타깃, 정직)

정리 스케치: $W_2(\hat\mu_K, p_1) \le \underbrace{C_1 L \sum_k h_k^{p+1}}_{\text{전파(경사 Lipschitz }L\text{)}} + \underbrace{C_2 \sum_k \mathrm{gap}_k}_{\text{twist 괴리 } \mathrm{gap}=\sup_x|\psi_t-\log\tilde p_t|} + \underbrace{C_3 K/\sqrt N}_{\text{리샘플 분산}}$

- Euler 전용은 첫 항만 있으나 계수가 나쁘다(보정 없음). **"조악한 스텝(소수 NFE) 레짐에서 SMC 항이 전파 항을 지배하는 경계조건"** 이 증명 타깃이다.
- 증명 의무 목록: (i) 전파 커널의 W2-Lipschitz(v의 Lipschitz 상수 L로 결합) (ii) 리샘플링 불편향 + 분산 바운드(표준 SMC; OT-리샘플은 분산 상수 개선) (iii) twist gap → 가중치 바이어스 bound (iv) 합성 = $W_2$ 삼각부등식.
- ⚠️ 정직: 무조건 생성도 N표본이라 MC 한계는 동일 — **SMC 이득은 "굵은 스텝 + 적응 스텝" 레짐에서만 나온다**는 조건을 실험과 정리 양쪽에 명시해야 한다.

## 5. 선행·차별화

- **Feynman–Kac Correctors**(Skreta, ICML 2025)·Discrete FKC·GFKC — 조건부/스티어링 SMC(무조건 수송 대체가 아님) · **TDS**(twist 조건부 표본) · **MCGdiff**·PF-latent-diffusion(역문제) · **PFGM/PFGM++**(포아송 장, 다른 기하) · "Particle Filters and Flows"(⚠️ **원문 확인 필수 — 제목이 정확히 겹친다**) · OT-리샘플링 문헌(Chopin 계열).
- 🟢 **빈 땅**: 무조건 생성에서 **ODE 적분기 자체를 ESS-적응 SMC로 교체 + W2 오차합성 정리 + OT-리샘플** 패키지.

## 6. 실험 설계

- **toy(1일, numpy)**: 1D/2D GMM 타깃, $K=4\sim8$ 굵은 스텝, Euler-N vs SMC-N marginal $W_2$ 비교 + ESS 곡선 + twist on/off. **"리샘플이 이기는 조건 경계"** 확인이 1차 관문.
- **본선**: CIFAR-10 / ImageNet-64. 베이스라인 Euler·Heun·FKC. 지표 FID@NFE·임베딩 공간 W2. ablation: 리샘플 방식(다항/OT) · twist on/off · 균일 vs ESS-적응 그리드.

## 7. 리스크

1. twist 학습 실패 시 편향 주입 → 가설 붕괴(가장 큰 리스크).
2. N개 입자 = 배치 N 샘플 상한과 결제 비용.
3. FKC 계열과의 델타 소진 — "무조건 + 이론 + 가속" 3축을 함께 잡아야 한다.
4. OT-리샘플 비용(싱크혼 사영).
5. "Particle Filters and Flows" 중복 가능성 — **원문 확인 전 실험 커밋 금지**(자기규약).

## 8. 연결

- [[research-topics-ledger]] #35.
- [[super-twisting-stochastic-approximation]] #32 — 같은 필터 골격의 RL판(게인 설계). 이 노트는 그 생성모델판(리샘플링=게인).
- [[phase-rope-flowmatching-motion-reward]] #34 — FM·연속성 방정식 사용 경험. §9 의 "$\sigma{=}0$이면 $W_2^2\lesssim B$"가 이 노트의 W2 선택 근거.
- 동적 3DGS-PF(slam-3dgs 도메인 토의) — 같은 골격의 제3응용. 여기서 확립한 SMC 골격의 역이식 후보.
- 칼만(TD)↔SMC 대응: 칼만의 K(계산된 게인) ↔ SMC의 가중치·리샘플 정책(계산된 게인) ↔ Euler의 "게인 0".

## 9. 다음 액션

- `note` 레포 toy: 2-모드 1D GMM 타깃, $K=4$, Euler-N vs SMC-N $W_2$ — 리샘플 우위 구간 존재 확인(twist는 1D라 비모수 KDE 사용 가능).
