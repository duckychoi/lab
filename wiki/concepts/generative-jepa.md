---
title: "생성형 JEPA — 시공간 latent에서 flow matching 조건부 미래예측"
created: 2026-11-22
author: fryday
tags: [concept, jepa, flow-matching, world-model, representation-learning, ledger-37]
ledger: 37
status: 판정-흡수(#38/#36비교군)(2026-11-24)
---

# 생성형 JEPA (#37)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **흡수(#38/#36 비교군)**
> 저차원에선 재표집이 이김(W1 0.173 vs 0.328), 선행 밀집.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 교수님 아이디어: JEPA(표현예측)에 동의하되, latent이 시공간에서 자유롭지 않아야 하고 **JEPA × flow matching 결합**.

## 논제
- **JEPA 약점**: 다음 latent를 하나로 예측(회귀) → 다봉 미래를 **평균내 뭉갬**(불확실성 소실).
- **해법**: flow matching을 **JEPA 예측기**로 → 조건부 미래 latent **분포** $p(z'|context)$ 생성 = 표현공간 생성(생성형 JEPA).
- **시공간 구조 보존**: 시간 RoPE/복소 SSM 위상(#28·#34)을 latent에 → latent이 시공간에서 "자유롭지 않게".

## toy (note:generative-jepa)
분기미래 $z=c\pm\Delta$. 결정론 JEPA(회귀)=전부 갭($\hat z\approx c$, 최근접모드 ~1.9=무효 붕괴). 생성형 JEPA(flow)=좌/우 모드 둘 다 복원(0.35/0.40, 갭 0.01). → 다봉 보존 실증 ✅.

## 선행/빈땅
Stochastic Latent Variable JEPA(2611.09302)=확률잠재 방향, **flow 버전 빈 땅**. LeJEPA/LeWM/V-JEPA=결정론. 참고 **Wan=DiT+Flow Matching**(픽셀 latent, 우린 표현 latent).

## 각도
① 시공간 RoPE latent+조건부 flow 예측기 ② 행동조건부 월드모델 $p(z'|z,a)$ 다봉→계획 ③ 접촉·분기 동역학 뭉갬 방지(#34).

## 연결
JEPA/월드모델 #25 · 스펙트럼 위상 #28 · [[phase-rope-flowmatching-motion-reward]] #34 · [[pf-generative-flow]] #35 · [[physics-potential-smc]] #36.
