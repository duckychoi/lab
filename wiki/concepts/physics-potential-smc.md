---
title: "물리-potential SMC 생성 — 통계 prior × 물리 법칙 융합"
created: 2026-11-22
author: fryday
tags: [concept, diffusion, smc, particle-filter, physics-informed, world-model, video-generation, ledger-36]
ledger: 36
status: 판정-★진행(주력)—flow제안PF로재정의(2026-11-24)
---

# 물리-potential SMC 생성 (#36)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **★진행(주력) — flow 제안 PF로 재정의**
> 지킬 기여: 초반 관측으로 출발 상태·물성을 flow로 제안하고 물리 시뮬로 후보를 가중. 같은 정확도에 시뮬 호출 약 6.1배 절약(엄격 장부), 관문 10(PF 신념 계획) 같은 입자 계산량에서 84.9% vs 60.5%(+24.4%p) 통과. 관문 7·8(마찰 식별) 불통과 = 그 카메라·투척에서 마찰이 관측을 거의 안 움직이는 식별불가 무대. 다음: 경사면 블록(0단계에서 마찰 식별 무대 확인). EIG 탐침 고유 이득 없음, flow 학습 비용은 장부 밖.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

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

## GLM(Monday) 의견 — 융합 위상 분류·PhysDiff 차별화·비디오 확장 비판 (2026-11-22)

> 텔레그램 토의(#36과 같은 주제를 독립적으로 심화) 결과. 상호 검증: 볼트 #36 toy(1D 중력)와 내 분석이 결론 일치.

### 1. 융합 위상 3분해 — 이 노트는 **위상 B**
- **A: 물리 엔진=제안, 플로우=가중치**($\psi_t=\log\tilde p_t$) — 점근 목표 $p_{data}\cap p_{phys}$. 엔진이 탐색하고 통계가 골라냄.
- **B: 플로우=제안, 물리=가중치**($\exp(-\lambda E_{phys})$) — **#36이 B**. 베이즈 곱 정식화와 동일.
- **C: 잔차 공분산 융합** $v = w\,v_{flow}+(1-w)\,v_{phys}$, $w$=역분산 가중 — **[[super-twisting-stochastic-approximation]] #32 칼만 융합("모델+관측")의 재릴**. 물리 엔진=모델, 통계 월드모델=관측.
- 제안 확장 순서: **B(현재) → C(제안 수준 융합 — 엔진 호출 절약, 입자당 1회) → A(궤적 수준 — 비용 최대, 표현력 최대)**. 계산 등고선상 이 순서가 합리적.

### 2. PhysDiff = 위상 B의 결정론적 특수사례 (차별화 프레이밍)
PhysDiff(NVIDIA, ICCV 2023, 인용 ~640)는 매 디노이징 스텝을 시뮬레이터 사영으로 교정 — 그러나 **경직 제약·단일 입자·가중치 없음**. SMC 일반화의 판매 포인트 3개: 소프트 제약($\lambda$ 스케줄)·다입자·무편향 보정. 논문 프레이밍은 **"사영(projection)을 확률적 융합으로 일반화"** + ablation(사영 vs 가중치 vs 둘 다)로 PhysDiff와 정면 비교.

### 3. PF 정당화의 본체 = 접촉 다봉성
접촉 순간 궤적은 좌/우로 **갈라지는 다봉 사후분포**. 랑제방·ODE 단일 궤적은 모드를 평균한다(모션 뭉개짐의 정체). PF는 가지를 입자로 유지하다 통계 가중치가 판정. 서사: **랑제방의 백색잡음 탐색 → 물리 엔진의 구조화된 탐색(접촉 응답) 대체**. toy의 "다양성 보존(std 0.27~0.29)"이 이 주장의 1D 증거 — 다음 검증은 **2D 접촉 분기 모드 리콜**(물체 넘어짐 좌/우, 랑제방=모드평균 vs SMC=양쪽 보존)을 권한다.

### 4. sim2real = 명시적 가중치 항 (이론 신선도)
시뮬레이터 제안↔목표 궤적분포의 불일치가 SMC 가중치로 잡히면, **sim2real 갭이 "파인튜닝 문제"에서 "제안-목표 KL의 명시적 항"으로 재정식화**된다. Girsanov형 바운드가 이 프레임의 이론 기여 후보. 위상 A로 갈 때 특히 유효.

### 5. 비디오 확장($x_0$-예측 디코드 후 가중)에 대한 비판적 의견
디코드 시점 가중은 **입자당 1회 보정이라 조기 가중치 퇴화** 위험(중간에 못 고친다). 대안 3개: (i) 중간 시각 상태 추출 head(관절/깊이)로 **latent 내 물리 potential**, (ii) latent 리샘플+latent rejuv(#35 골격 재사용), (iii) **$\lambda$ 어닐링** — 초기 스텝=구도·구성(통계 우세) / 후기 스텝=역학·접촉(물리 우세). 물리는 "뒤쪽 스텝에 강하게"가 생성 의미론과도 일치.

### 6. toy 지표의 긴장 — E 단일 숫자는 함정
물리가이드(E=0.012) vs 물리-SMC(E=0.041): SMC가 E에서 지지만 다양성 보존. **E-다양성 파레토 보고** 권장. 또한 물리가이드(Langevin on E)는 λ→∞ 극한이라, 공정 비교는 **"같은 E 수준에서의 다양성"** 커브다.

### 7. 문헌 정합 상호검증 + 볼트 하우스키핑
- 내 독립 검색과 #35 노트(pf-generative-flow)의 gap 확정이 **일치**: FKC=조건부 전용, "Particle Filters and Flows" 정확 제목 부재(EnFF·DiffPF는 flow-in-PF로 반대방향) → 내가 걸었던 중복 의심 해제.
- PhyScene(CVPR24)은 제약 장면 생성(사영/최적화 계열)이라 겹침 낮음 판단. 잔여 확인 대상: PhysDiff 후속(2024~26) 중 SMC식 물리 가중 작업.
- ⚠️ **#35가 2노트 상태**([[pf-generative-flow]] + [[wasserstein-smc-generative-transport]]) — 동일 ledger 번호라 병합 권장. 내 노트의 W2 오차합성 정리·OT-리샘플·ESS-적응 스텝은 #36 비디오 확장 시 그대로 재사용 가능.

### 8. 연결 갱신
[[wasserstein-smc-generative-transport]] · [[super-twisting-stochastic-approximation]] #32 · [[phase-rope-flowmatching-motion-reward]] #34(위상·분포 언어) · 월드모델 로드맵("암묵 월드모델+생성기 융합" 커뮤니티 프레이밍 — 이 노트는 그 융합의 **대수적 해법** 포지션).
