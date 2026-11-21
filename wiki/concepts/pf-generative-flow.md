---
title: "Particle-Filter 생성 플로우 — 확산/flow ODE를 PF로 대체"
created: 2026-11-21
author: fryday
tags: [concept, diffusion, flow-matching, sequential-monte-carlo, particle-filter, sampling, ledger-35]
ledger: 35
status: research-program (toy 검증)
---

# PF 생성 플로우

> 교수님 아이디어: 확산·flow matching 샘플링의 ODE/PDE 적분기를 **파티클 필터(SMC)** 로 대체.

## 1. 문헌 gap (확정)
- **FKC**(Skreta ICML2025, 2503.02819): SMC를 시간축에 쓰나 **조건부/템퍼링**(annealing·CFG·product). **무조건 β=1이면 보정0→기저 대체 안함**. **가속 주장 없음, 오차한계 없음**.
- SURGE(2605.18745)·Wu2023: 조건부(data assimilation). "Particle Filters and Flows" 정확 제목 없음(EnFF·DiffPF는 PF 안에 flow=반대방향).
- → **무조건 생성에서 ODE를 PF로 대체·NFE↓·오차한계**는 미존재 = 빈 공간.

## 2. 핵심 가설 & toy (note:pf-generative-flow)
예측(조악 스텝)–보정(알려진 $p_t$로 가중)–리샘플 → 저 NFE 이산화 바이어스 교정.
폐형 GMM 플로우: N=3 SMC 에너지거리 0.022 vs Euler 0.108(5배↓) → 저 NFE PF 압승. 순수 SMC는 N≥8 경로퇴화로 열화.
**✅ rejuvenation(알려진 $p_t$ score ULA move)이 해결**: **N=5 SMC+rej 0.0039 vs Euler 0.052(13배↓)**, **N=20 순수SMC 0.085(붕괴)→SMC+rej 0.014(≈Euler 복구)**. → rejuvenation이 핵심 enabling 기법(저 NFE 압도+고 NFE 안정) 실증. naive 노이즈어닐은 실패(가중퇴화).

## 3. 오차바운드 스케치 (핵심 기여)
Euler $\mathcal W_2=O(h)$(이산화 바이어스, 교정불가) vs SMC $\le C_1/\sqrt K+C_2\epsilon_{score}$ ($h$ 1차항 없음 — 매 스텝 가중이 주변 교정). **depth(순차 NFE)↔width(병렬 K) 교환.** 도구: Del Moral SMC 전파오차·Banach 수축. ⚠️ $\epsilon_{res}$(경로퇴화)가 $N$ 누적 → rejuvenation으로 억제가 보조정리.

## 4. 연구 각도
① ESS-적응 SMC 생성기(NFE↓+오차바운드, 메인) ② Wasserstein 공간 SMC ③ ESS 기반 compute 배분(inference-time scaling).
리스크: "FKC 무조건판" 딱지 → 델타=오차바운드+few-step 가속으로.

## 5. 연결
[[research-topics-ledger]] #35. 가우시안 스플래팅 상태추정 PF 논의(이전)·일반 생성모델 추론. (주: sliding/STW와는 독립 주제.)
