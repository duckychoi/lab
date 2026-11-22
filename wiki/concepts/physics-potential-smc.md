---
title: "물리-potential SMC 생성 — 통계 prior × 물리 법칙 융합"
created: 2026-11-22
author: fryday
tags: [concept, diffusion, smc, particle-filter, physics-informed, world-model, video-generation, ledger-36]
ledger: 36
status: research-program (toy 검증)
---

# 물리-potential SMC 생성 (#36)

> 교수님 아이디어: 생성모델의 "통계적 암묵 물리"에 **물리를 prior로 주입** — PF로 통계+물리 융합.

## 정식화 (베이즈 곱)
$$p(\text{궤적})\propto p_\theta(\text{궤적})\times\exp(-\lambda E_{phys}),$$
생성=제안(proposal), 물리=가중치(potential), 리샘플+물리 rejuvenation=곱 강제. = **#35 PF머신 + 물리 potential**(#35는 potential이 "알려진 주변", 여기선 물리 에너지).

## toy (note:physics-smc-generation, 1D 중력운동)
$E_{phys}=\|Sy+g\|^2$(2차차분=−g ⟺ 물리). prior=물리궤적+잡음.
- raw prior E=**6.45** → 물리가이드(Langevin on E) **0.012** / 물리-SMC(리샘플+rejuv) **0.041** (참물리≈0).
- **다양성 보존**: 초기속도 std 0.27~0.29(참 0.257). 한 궤적 붕괴 아님.
- → **재학습 없이 추론때 통계+물리 융합**(통계=다양성·그럴듯함, 물리=법칙). 실증 ✅.

## 두 노선
(A) 샘플링 가이드($-\eta\nabla E$, energy guidance) · (B) 물리-SMC(reweight $\exp(-\lambda E)$+리샘플+rejuv, 분포 교정).

## 🟢 각도/난관
비디오 확장: 노이즈 latent엔 물리 적용 불가 → $x_0$-예측 디코드 후 $E_{phys}$ 가중. 물리 potential 설계(광류·운동량·강체·접촉, 미분가능). 비용·경로퇴화→#35 rejuvenation. vs 르쿤 JEPA(생성X)=다른 노선, 이건 생성 유지+물리 교정.

## 연결
[[pf-generative-flow]] #35 · 모션 flow #34 · JEPA/월드모델 #25 · 비디오생성 튜토리얼(`html/video-gen-tutorial.html`).
