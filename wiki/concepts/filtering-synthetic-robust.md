---
title: "필터링-기반 합성데이터 강건학습 — KF 예측·실데이터 보정 + 수축"
created: 2026-11-23
author: fryday
tags: [concept, kalman-filter, model-collapse, synthetic-data, contraction, dissipativity, robust-training, ledger-42]
ledger: 42
status: 판정-독립논문화보류(2026-11-24)
---

# 필터링-기반 합성데이터 강건학습 (#42)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **독립 논문화 보류**
> 칼만 갱신이 생성된 합성 표본을 실제로 쓰지 않음(합성 평균 = 자기 추정값 → 정보 0). 실측 이동평균만으로 최종 오차 0.1463·회복 7세대 재현. 즉 결과는 'KF가 이긴다'가 아니라 '자기 노이즈를 섞지 마라'. 재개: 같은 실측으로 합성 자료를 실제로 사용해 희소 모드 보존이 개선될 때.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 합성데이터 재귀학습을 **칼만필터**로 본다. 합성=노이즈 낀 예측, 실데이터=보정 관측, 칼만게인=적응신뢰, (1-K)<1=수축(#39)→붕괴 없음.

## 논제
AI 생성물이 웹을 채움 → **모델 붕괴**(자기생성 재귀학습 → 평균 drift + 분산/꼬리 소멸)가 현안. 기존 최강 완화책 **실데이터 혼합**은 *고정 비율*이라 비효율. 근접논문 **2512.00757**(Contraction-Conditioned Neural Filters)는 수축 패널티로 막지만 ①KF/PF 아님(게인·공분산·예측보정 없음) ②라벨을 **참값 오라클**로 만듦(실전 불가). → 그 오라클을 **실데이터 관측**으로 대체하고 필터의 **적응게인+공분산+수축**을 살림.

## KF 프레이밍
- 예측: 모델이 자기 믿음에서 합성 생성, $P^-=P+Q$ (새 정보 없음+불확실성↑).
- 보정: 소량 실데이터 $z$ 로 앵커 (오라클 대체), 게인 $K=\frac{P^-}{P^-+R}$.
- 수축: $(1-K)\in(0,1)$ = 소산성(#39) → 오차 유계 = **붕괴 없음 증명**.
- 적응 KF: 큰 혁신(innovation) 감지 → $Q$ 팽창 → 게인↑ → 분포이동 빠른 회복.

## toy (note:filtering-synthetic-robust)
재귀추정 θ*=2, σ_d=1, n_real=5, m=50, T=120, 300시드. **동일 real 예산.**
- Part1 평균붕괴 final|err|: naive **0.704**(붕괴22%) · mix 0.230 · **KF 0.146**(mix대비 37%↓) · adaptive 0.287.
- 수축인자 (1-K): naive **1.00**(발산) · mix 0.909 · **KF 0.730**(최강 수축=최타이트 유계).
- Part2 분산붕괴(/σ_d²): naive **0.12**(꼬리 소멸) vs mix 0.92 · KF 1.04(보존).
- Part3 분포이동 회복(gen50 +3.0): mix **35** vs KF **7** vs adaptive **3** 세대. (adaptive 최속 회복, 단 정상오차는 KF보다 약간↑ = 교환.)

## 차별점 / 가치
근접논문 오라클 약점 제거 + 적응게인·공분산·수축 복원. **동일 예산에서 고정혼합(최강 기존책)을 정량 능가** + 분포이동 강건 + 교정된 불확실성. 통합: #32(KF≈학습update)+#39(수축/소산성)+#33(큐레이션)+모델붕괴.

## 정직한 한계
R 추정·근사 선형가우시안 가정. 딥넷 확장은 KalmanNet식 학습게인+대각 공분산 필요(비용). mix-real이 더 단순 — 우리 이득은 **적응·붕괴보증·불확실성**이 커지는 레짐(제한된 real·분포이동).

## 연결 (🧭 나침반 — 샘플효율·안정·학계 toy)
원장 #42. [[dissipative-kf-worldmodel]] #39 · [[quantum-inspired-kf]] #41 · [[super-twisting-stochastic-approximation]] #32 · [[rl-self-curating-features]] #33 · [[research-synergy-map]] · [[research-topics-ledger]].
