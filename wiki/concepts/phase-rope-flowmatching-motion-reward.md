---
title: "Phase-RoPE × Flow-Matching 모션 프라이어 — 리워드 없는 리듬·flow 제어"
created: 2026-11-21
author: fryday
tags: [concept, flow-matching, rope, phase, motion, humanoid, reward-free, distribution-matching, ledger-34]
ledger: 34
status: 판정-종료—AMP가이미푸는문제(2026-11-24)
---

# Phase-RoPE × Flow-Matching Motion Prior

> [!warning] ⚖️ 외부 판정 (2026-11-24): **종료 — AMP가 이미 푸는 문제**
> FM 단독은 정지 함정. SAC 라벨교환 S3: AMP 3/3·템플릿 3/3·FM 0/3(학습 시범자 과적합), 정칙화 FM 3/3이나 AMP보다 약함. 다중 스타일 S4는 정답 보상 양성 대조도 실패 → 판정 불가. 원 '§9 상한'과 'FM은 구조적으로 모드를 덮는다' 주장은 철회(정책 쪽 기대값이라 mode-seeking).
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

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

## 9. 정리 — FM 잔차가 divergence를 상한 ✅ (docs/05)
**바이어스-분산 분해**: $\mathcal R(q)=B(q)+C(q)$. $B(q)=\mathbb E_t\mathbb E\|v^*-u_q\|^2$ (바이어스), $=0\iff q=p_{data}$ (proper). $C(q)$=기약 결합분산.
**상한**: $\sigma{>}0$ 확률보간에서 Girsanov+데이터처리로 $\mathrm{KL}(q\|p_{data})\le\frac{1}{2\sigma^2}B(q)$; $\sigma{=}0$이면 연속방정식 안정성으로 $W_2^2\lesssim B(q)$. → FM 잔차 리워드 최대화(+max-ent)가 분포매칭.
**수치검증**(`toy_fm_divergence.py`): base(KL=0) 잔차 최소(proper 확인), **Spearman corr(R,KL)=0.73**(단조·방향). 큰 shift 비단조는 비모수 $v^*$ OOD 열화(artifact).
**미완(§4)**: 주변불일치 봉합·$v^*$ 실현오차.
**§4.1 C 축소 시도 — 음성결과**(`toy_rectified_coupling.py`): OT결합이 데이터 경로 직선화(CFM잔차 4.36→0.82)하나 **독립 eval서 결합불일치로 corr 0.77→0.25 역효과**. 교훈: C 축소엔 **train/eval 결합 일관성** 필수 or **가능도/점수매칭형 리워드**(C floor 없음)가 더 유망.

## 10. 다음 (torch 필요)
soft-RL(SAC)+FM리워드 실제 모션 파이프라인 · RoPE-flow NN 학습(sharp 생성) · 위상 $\phi$ 접촉동기.

## 11. 스타일/컨텐츠 loss 문헌 지도 (GLM, 2026-11-22 — 교수님 질문: "휴머노이드 학습에서 스타일·컨텐츠 loss 개념을 사용하나?")

- **키네매틱 모션 그래픽 진영 — 용어 그대로, Gram loss가 표준**: 이미지 NST(Gatys)의 content+style(Gram) 구조가 모션으로 이식됨. `Fast Neural Style Transfer for Motion Data`(Gram→모션 최초 계열, 단 **content-style 강결합** 약점 지적) · **Style-ERD**(2022, 온라인 전이 — Gram이 스타일 표현 표준, reconstruction-only는 전이 불가 확인) · **Motion Puzzle**(부위별 스타일 추출+스켈레톤 구조 보존) · 2024 확산+Gram 조합.
- **물리 휴머노이드 RL 진영 — 용어는 "style reward", 기능은 동일 분해**: **task reward(=content) + style reward(=AMP 판별자)** 구조가 AMP·ASE·CALM 표준. 목표달성=과제, "전문가처럼 보임"=전이분포 매칭. **단 RL 리워드로 Gram loss를 직접 쓰는 작업은 드묾** — 스타일 자리는 판별자가 차지.
- **🟢 §7의 포지션 = 그 빈 칸**: Gram을 RL 리워드로 직접 쓰되, 시간축에서는 **자기상관↔PSD(Wiener–Khinchin)** 라서 위상 불변 리듬 텍스처만 잡는 loss가 된다. toy 실증: 같은 리듬·다른 위상 → per-frame L2 0.002→2.08 폭발 vs **PSD 거리 0(위상불변)**. 즉 "리듬 스타일만, 타이밍(content)은 건드리지 않는" loss의 실증적 근거.
- 한 줄: **키네매틱=Gram loss 표준 · 물리 RL=기능적 보편(style reward)·Gram 직접 리워드는 드묾 — §7이 PSD 기반으로 그 빈 칸을 채운 상태.**

