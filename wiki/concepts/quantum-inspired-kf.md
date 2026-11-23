---
title: "Quantum-inspired KF — 복소/텐서넷 상태 샘플프리 세계모델 필터"
created: 2026-11-23
author: fryday
tags: [concept, kalman-filter, complex, tensor-network, quantum-inspired, sample-free, world-model, ledger-41]
ledger: 41
status: research-program (toy 검증)
---

# Quantum-inspired KF (#41)

> "양자 PF"는 양자를 샘플링(줄여야 할 부분)에 붙인 미스매치. 같은 직감을 **표현(복소/텐서넷 상태)** 에 붙이고 필터는 **샘플프리 KF/SSM**(#39)로.

## 논제
- PF 다봉성을 **샘플 없이**: 복소 진폭 상태 $|\psi|^2$ 가 다봉 사후를 단일 복소벡터로. 실수 KF(단일 가우시안)=갭 붕괴.
- **위상 간섭** $|a+b|^2$ cross term $2|a||b|\cos\Delta\phi$ = 고전 확률 합이 못 하는 표현력(#28·#40).

## toy (note:quantum-inspired-kf)
- Part1(샘플프리 다봉): 모호관측 $y=\cos x$. **복소/그리드 모드질량 0.97** vs 실수KF μ=0(갭)·0.25.
- Part2(위상 간섭): 겹침질량 복소 Δφ=0 **0.782**/π **0.494** vs 고전 **0.714 고정**. 간섭=추가 표현력.

## 설계
상태=복소 진폭(저차원 그리드) or **텐서네트워크 MPS(고차원, #40)**. 갱신=복소 KF 예측–보정(샘플프리 #39)+소산성 안정(#39·#32). 참고: 복소 KF(I/Q)·텐서넷 KF 실증 존재.

## 왜 양자 PF가 아니라 이것
양자 PF=간섭을 샘플링(무거운 가지)에 붙임+고전 사후는 비음(간섭 자리 없음)→미스매치. 간섭은 **표현**에서 이득 → 샘플프리 필터 상태표현에 붙임. (양자 PF 적합=추정대상이 진짜 양자상태=#40 C.)

## 연결 (🧭 나침반 정중앙)
[[dissipative-kf-worldmodel]] #39 · [[quantum-inspired-worldmodel]] #40 · [[spectral-memory-creativity]] #28 · [[research-synergy-map]](위상 축) · PF↔KF 상보 #35.
