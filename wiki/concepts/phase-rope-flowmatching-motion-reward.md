---
title: "Phase-RoPE × Flow-Matching 모션 프라이어 — 리워드 없는 리듬·flow 제어"
created: 2026-11-21
author: fryday
tags: [concept, flow-matching, rope, phase, motion, humanoid, reward-free, distribution-matching, ledger-34]
ledger: 34
status: research-program (toy 검증 완료)
---

# Phase-RoPE × Flow-Matching Motion Prior

> 교수님 발상: 모션 리워드의 두 키워드 = **위상 + 분포**. **RoPE(=회전 위상)** 로 리듬을, **flow matching(=분포 생성)** 으로 flow/스타일을 잡고, 스칼라 리워드를 설계하지 말자.

## 1. 두 키워드 1:1 매핑
- **RoPE = 위상.** 위치 $t$를 다중주파수로 회전 $\theta_i=t\omega_i$ ($\omega_i=10000^{-2i/d}$) = $e^{i\omega_i t}$ → **다중주파수 푸리에 위상 임베딩** = 리듬/주기 기저.
- **Flow matching = 분포.** 속도장 $v_\theta(x,t)$로 노이즈→모션분포 연속수송. 조건부 FM 손실:
$$\mathcal L_{CFM}=\mathbb E_{t\sim U[0,1],x_1\sim p_{data},x_0\sim\mathcal N}\|v_\theta(x_t,t)-(x_1-x_0)\|^2,\quad x_t=(1-t)x_0+tx_1$$
  "motion=연속 flow"라는 의미까지 일치.

## 2. 선행 (조각은 SOTA, 특정 융합은 빈 땅)
- Flow 정책: **Flow Policy Gradients**(arXiv 2602.02481, 휴머노이드+sim2real) · VITA(2507.13231) · CoLA-Flow(2601.23087) · Riemannian FM Policy(2412.10855) · Let the Dynamics Flow(2606.03834) · π0 VLA.
- RoPE×FM×모션: **RoPECraft**(2505.13344, RoPE=위상+FM 목적함수에 위상제약) · **MotionHiFlow**(CVPR2026, Joint RoPE, 단 골격용) · AV-Link(ICCV2025, 시간정렬 RoPE 박자동기).
- 🟢 **빈 땅**: RoPE를 "상대위치/골격"이 아니라 **"리듬 위상"** 으로 + FM을 **물리제어용 모션 프라이어**로 → 리듬·flow가 **리워드 없이 emergent**한 **physics-based** 휴머노이드 제어. 현재 RoPE+FM 모션은 전부 kinematic 생성(텍스트/영상)이지 closed-loop 제어가 아님.

## 3. 심화 — (b) Flow-Matching 프라이어 = 스타일 리워드

핵심: **AMP 판별자(적대적)를 flow-matching 잔차(수송기반)로 교체.**

### 3.1 FM이 정의하는 밀도
학습된 $v_\theta$는 CNF를 정의, 연속방정식 $\partial_t p_t+\nabla\!\cdot(p_t v_t)=0$. 순간변수변환:
$$\log p_1^\theta(x_1)=\log p_0(x_0)-\int_0^1 \nabla\!\cdot v_\theta(x_t,t)\,dt$$
→ 원칙적으로 $r^{style}=\log p_1^\theta(x)$ 가능. 단 divergence(Hutchinson) 비쌈.

### 3.2 실용 대리 = FM 잔차 에너지
모션 윈도우 $x$가 **학습된 flow 위에 있나**를 1-샘플로 측정:
$$\boxed{\,r^{style}(x)=-\,\mathbb E_{t\sim U[0,1],\,x_0\sim\mathcal N}\big\|v_\theta(x_t,t)-(x-x_0)\big\|^2,\quad x_t=(1-t)x_0+tx\,}$$
잔차 작음 = in-distribution = 자연스러운 모션 → 높은 리워드. **AMP 스코어의 생성형 대체.**

**AMP 대비 이점:**
- **비적대적**: flow는 데이터로 1회 학습한 **고정 목표** → GAN minimax 불안정·판별자 exploit 없음.
- **멀티모달 보존**: 평균포즈 collapse 방지(flow가 모드 유지).
- (score/diffusion-as-reward 계열의 FM판, 직선경로라 노이즈스케줄 불필요.)

### 3.3 위상조건 = 리듬 강제
flow를 위상 $\phi$로 조건화(모션 윈도우 토큰에 RoPE로 $\phi$ 주입): $v_\theta(x_t,t;\phi)$. 리워드가 위상인식:
$$r^{style}(x,\phi)=-\,\mathbb E_{t,x_0}\|v_\theta(x_t,t;\phi)-(x-x_0)\|^2$$
→ **"올바른 위상에서 in-distribution"** 을 보상 = 박자 리워드를 손으로 안 짜고 리듬/타이밍 강제. 다중주파수 RoPE = 스펙트럴 리듬 기저.

### 3.4 알고리즘 스케치
```
# 사전학습: 위상조건 flow v_θ 를 모션 데이터셋에 CFM 손실로 학습 (RoPE phase 토큰)
# RL 루프:
for each step:
    정책 π 가 모션/전이 윈도우 x 생성, 현재 위상 φ
    t ~ U(0,1); x0 ~ N(0,I); x_t = (1-t)x0 + t·x
    r_style = -|| v_θ(x_t, t; φ) - (x - x0) ||^2        # MC 1-샘플
    r = r_task + β(n)·r_style                            # β 어닐링(AMP처럼)
    π 업데이트 (PPO 또는 STSA-SA)
```

## 4. 🟢 열린 정리 (기여 타깃, 정직)
1. **리워드 타당성**: $-r^{style}$ 잔차 최소화 ⟺ 정책유도분포 $p_\pi$ 가 $p_{data}$ 로 수렴? GAIL의 occupancy matching처럼 **FM 잔차 기대값이 어떤 divergence의 상한/대리**임을 증명해야. (잔차는 정확한 $\log p$ 아님 = ELBO/에너지 대리 → gap 특성화 필요.)
2. **위상 정합**: $\phi$를 접촉/보행에 동기 or 학습 — 아니면 RoPE가 그냥 시간인덱스.
3. **closed-loop/물리실현성**: FM은 open-loop 생성 → task RL과 결합 필수. 소수스텝(consistency/shortcut) flow로 실시간화.
4. **리워드 해킹**: 저잔차 영역 악용 → 다중 $t$ 샘플/gradient penalty 유사항.

## 5. 연결
- [[research-topics-ledger]] #34.
- **RoPE $e^{i\omega_i t}$ = [[스펙트럼 기억]] #28 의 복소SSM $e^{(-\alpha+j\omega)t}$ 의 어텐션판** — 네 위상기억 아이디어를 모션 위치인코딩에 적용.
- [[super-twisting-stochastic-approximation]] #32 — FM 잔차 리워드는 노이즈·비정상 → STSA가 정책 업데이트 강인엔진.
- [[rl-self-curating-features]] #33 — 모션 피처의 위상 큐레이션.
- 휴머노이드 파쿠르 SOTA(Terrain-Indexed AMP 2611.08056 / Motion Matching 2602.15827): AMP·tracking을 **FM 프라이어로 대체**하는 포지션.

## 6. 검증 결과 (toy, numpy, `note:spectral-credit-stsa`)
증명 스케치 핵심: **고정 에너지 리워드최대화는 $q$에 선형→모드붕괴. max-ent(soft) RL 필수** ($q^*\propto\exp(r/\alpha)$, $r=\log p$, $\alpha=1$ → $q^*=p_{data}$).
3-모드 GMM toy(`src/toy_fm_vs_amp.py`):
- **C1**: argmax=단일점 붕괴. soft α 0.05→1모드, α=1→목표가중 [0.6,0.3,0.1] 복원(H 0.82). 이론 확인.
- **C2**: 비모수 FM 잔차 에너지 corr(logp)=**0.93**, 에너지 순서=가중치 순서 → 유효 밀도점수.
- **C3**: 완전수렴 AMP corr 0.61 / 덜학습 AMP corr 0.54·std **0.07(불안정)** vs **FM 0.93·분산0** → FM 더 정확·안정.
설계 함의: **PPO 리워드최대화 ✗ → soft/max-ent RL ✓**.

## 7. Style/Content Loss 접목 (교수님 질문: 도움 되나 → 됨)
- CONTENT = 위상 민감 목표(과제 추종) / STYLE = 시간축 피처 **Gram = 자기상관 ↔(Wiener–Khinchin) 파워스펙트럼(PSD)** = 위상 불변 리듬 텍스처.
- 세 분포매칭 축 상보: **AMP(적대·불안정) / FM(생성·안정) / Gram-PSD(모멘트·싸고 비적대·타이밍불변)**. Gram은 2차 통계라 고차는 FM 병용.
- 리워드: $r=r_{task}(\text{content})+\beta\,r^{FM}_{style}-\gamma\|\text{PSD}_\pi-\text{PSD}_{data}\|$.
- → **CONTENT=위상(RoPE) / STYLE=PSD(Gram) / 분포=FM** 로 리듬·flow를 스펙트럴 분해. [[스펙트럼 기억]] #28과 같은 언어.

## 8. 추가 검증 ✅ (note:spectral-credit-stsa)
- **PSD 스타일 toy**(`toy_psd_style.py`): 같은 리듬·다른 위상 → per-frame L2 0.002→2.08 폭발, **PSD거리 0 유지**(위상불변); PSD가 리듬 판별; content는 per-frame만. **Wiener–Khinchin 수치확인 오차 2.84e-14**(Gram=PSD 쌍).
- **RoPE 위상조건 flow 생성 toy**(`toy_rope_phase_flow.py`): 링(순환 위상)에서 비모수 조건 flow. **무조건 κ=0 각도오차 1.63rad(명령 무시) → RoPE조건 κ=8 0.33rad(추종)**, 반경 2.07(링 위). RoPE 위상조건이 생성 리듬 위상 제어 실증(비모수라 coarse, NN이면 sharp).

## 9. 다음 (미완)
FM 잔차→f-divergence 상한 엄밀 증명 · 위상 $\phi$ 접촉동기 · soft-RL(SAC)+FM리워드 실제 모션 파이프라인 · torch로 RoPE-flow NN 학습(sharp 생성).
