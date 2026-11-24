---
title: "Reliability-Gated Filtering — raw 관측 품질 → 게인 + 수축 증명"
created: 2026-11-23
author: fryday
tags: [concept, kalman-filter, robust-filtering, observation-quality, contraction, variational, ledger-63]
ledger: 63
status: research-program (toy 검증)
---

# Reliability-Gated Filtering (#63)

> 칼만/PF 게인은 "예측 vs 관측" 한 축뿐. "이 관측이 유독 좋으니 더 가중"을 하려면 raw 관측에서 측정 가능한 품질 $q(z)$ 가 게인에 수식적으로 들어가고, 발산 안 함이 증명되어야 한다.

## robust/VB KF에 있나 (정직한 분해)
1. raw goodness 측정 — ✅ 정규화 혁신 $\nu^\top S^{-1}\nu$, 단 **모델 잔차**(관측 고유 품질 아님).
2. 게인 기여 — ✅ Student-t 변분 KF $\lambda\to R/\lambda\to K$.
3. 증명 — △ 추론수렴(ELBO)만, **적응게인 균일 수축**은 전면에 없음.
→ 공백: **(A) 순환성**(자신만만 틀린 필터가 '맞지만 놀라운' 좋은 관측을 이상치로 버림) · **(B) 균일 수축 증명**.

## 아이디어
- 품질 $q(z)$: SNR·선명도·교차뷰/교차태스크 일관성(#43)·confidence — **잔차와 독립**. $R_{\text{eff}}=h_\theta(q)$, 클램프 $[R_{\min},R_{\max}]$.
- 게인: $K(q)=P^-H^\top(HP^-H^\top+R_{\text{eff}}(q))^{-1}$, $q\uparrow\Rightarrow K\uparrow$.
- **명제**: $H$ 가역·$R_{\text{eff}}\succeq R_{\min}\succ0$ → $A_{cl}=I-K(q)H$ 가 $\|A_{cl}\|\le\rho<1$ 균일(의사역 도달 불가) & $\|K\|\le\kappa$(주입 유계) = **robust+stable 동시**. (#39 소산성 결.)
- PF 버전: 템퍼드 가능도 $p(z|x)^{\lambda(q)}$ (일반화 베이즈).

## toy (note:reliability-gated-filtering)
1D 추적, 이질 노이즈(품질 covariate $c$) + 이상치 + 점프(순환성), 200시드. A 고정R / B 잔차게이트(robust/VB) / C 품질게이트(ours) / D 결합.
- 정상 RMSE: A 1.126 · **B 2.035**(고정R보다 나쁨) · **C 0.498** · D 0.497.
- 순환성(점프후 회복) ★: A 3.101 · **B 4.604(최악)** · **C 1.376** · D 1.382.
- 이상치 최대오차 평균: A 3.74 · B 4.26 · C 1.75 · **D 1.55**.
- 전 방법 $K<1$ 균일 $(1-K)>0$ 수축; 품질게이트 $K\le0.95$(고신뢰)이나 클램프 유계.

## toy#2 — 학습형 게이트 (오라클 제거, note:reliability-gated-filtering)
맵 $h(c)$ 를 데이터 학습: $E[\nu^2-P^-|c]=E[r|c]$ (현재 잔차 안 씀→순환성 회피), 보정/테스트 분리.
- **정직한 반복**: 최소제곱 적합 실패(이상치·점프 거대 $\nu^2$ 지배→계수폭발/포화, E가 A보다 나쁨) → **c-빈 median 로버스트** 모멘트매칭으로 교체 성공.
- ρ=0.8: 학습맵 c=0.1→2.41/c=0.9→0.09 로 $E[r|c]$ 복원. 정상 RMSE **E 0.563** vs A 1.148·B 2.043, 천장 C* 0.481 근접. 순환성 E 1.72 vs B 4.60.
- 안전성(ρ 스윕): ρ 1.0→0.0 에서 E 0.58→1.12≈A — 무정보면 고정R화, **A보다 나빠지지 않음**. B는 ρ 무관 2.04.

## 차별점 / 한계
있는 것=마할라노비스 게이팅·Student-t VB·적응R·Huber(전부 잔차기반). 빈 땅=①raw/일관성 품질→순환성 해소 ②클램프 균일 수축 증명(robust+stable 동시) ③#42/#43 샘플신뢰 이식(2512.00757 오라클 가중의 엄밀화). 한계: C는 품질→노이즈 보정맵 교정/학습 가정, 품질신호 오류 시 D(품질+잔차백업)가 안전.

## 연결 (🧭 나침반)
원장 #63. [[filtering-synthetic-robust]] #42(샘플신뢰) · [[selfcorrecting-studio-engine]] #43(일관성=품질) · [[dissipative-kf-worldmodel]] #39(수축) · [[quantum-inspired-kf]] #41 · [[research-topics-ledger]] · [[research-synergy-map]].
