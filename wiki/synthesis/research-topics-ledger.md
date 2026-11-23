---
title: "연구주제 공유 원장 (Research Topics Ledger)"
created: 2026-10-14
updated: 2026-11-21
author: fryday
tags: [research-ledger, shared-hub]
---

# 연구주제 공유 원장

Fryday·Monday가 텔레그램에서 교수님과 **연구주제로 거론한 것들**을 한곳에 모아 관리한다.
새 주제가 나오면 해당 AI가 여기에 추가하고, 위키 노트(sources/concepts)·HTML(lab)로 확장한다. 상호 교류의 인덱스.

---

## 🧭 연구 나침반 (상시 방향, 2026-11-23 설정)
교수님 지침: **얀 르쿤(AMI Labs) 방향**을 기본 나침반으로 — ①생성형·확률·샘플비효율 RL 과신 지양 ②**JEPA(결합임베딩)+에너지기반** 중심 ③"인간수준 AI엔 LLM 스케일 경쟁 말라"(수천 GPU=학계 불가) ④**물리세계 이해·행동결과 예측·계층적 계획**에 집중(소규모 컴퓨팅·numpy toy로 기여 가능).
- 적용: 새 주제·toy는 (a)표현공간(픽셀X) (b)물리/행동예측 (c)계층계획 (d)샘플효율·소규모 검증 쪽으로.
- ⚠️ 열린 긴장: #37·#38은 JEPA에 **flow(생성·확률)** 를 붙임 → 르쿤 "생성 버려라"와 충돌. 단 **표현공간 생성**이라 픽셀 낭비 우려는 회피. "표현공간 생성이 르쿤 노선과 양립하나"를 상시 열린 질문으로.
- 정합: #25(JEPA/월드모델)·#34~#40 전부 이 나침반 위. 상충 시 "표현공간·물리·계획·샘플효율" 우선.
- 📌 통합 지도: [[research-synergy-map]] — 2공통축(에너지·위상)+4 시너지 클러스터+플래그십("소산성·위상 Mamba 세계모델 + 적응적 KF↔PF + 물리 potential + SIGReg").

---

## 🅰 Fryday 쪽 (텔레그램 대화에서 거론)

### A. Neural Beamforming (메인 스레드)
1. AI-native 빔포밍 재발명 — 6단계 사다리(①솔버교체~⑥AI 알고리즘 발견)
2. Neural Beamforming Transformer (NBT, 2026)
3. CAT-MoEformer — MoE 빔선택/빔예측
4. 멀티빔 동시 조준타격(multi-target)
5. Volumetric Beam Focusing — 근거리장 3D 점집속
6. **VF-MoNBT** — NBT+MoE+멀티빔+볼륨집속 융합 (플래그십 A)
7. 슈퍼트위스팅/슬라이딩모드 × 빔포밍
8. **공간 슈퍼트위스팅 개구** — 1-bit 메타표면 양자화로브 셰이핑(ΔΣ=1차, STW=2차 슬라이딩) (플래그십 B)
9. Sliding-mode-as-optimization (슬라이딩 변수 s=∇J)
10. 물리적 꼬인/미끄러지는 빔 — OAM 보텍스, Airy 자동집속, FDA
11. Super-twisting × OAM (twist×twist 결혼)

### B. 생성모델·디퓨전·스펙트럴
12. 스펙트럴 편향(F-principle)·Fourier features
13. Diffusion = spectral autoregression / 주파수영역 디퓨전(DCTdiff·blurring)
14. **스펙트럴 디퓨전 × 빔스페이스** — 빔포밍 생성 사전확률(블루오션) → [[spectral-diffusion-beamspace]]
    - ✅ toy(note:spectral-diffusion-beamspace): 매니폴드 유효차원 10/16. **(A) 게인제약 ill-posed→선형사전 실패**(-7 vs 매칭 -13dB, 방향 위상 비선형). **(B) inpainting→사전 유효**(k=8 -8.6 vs 영채움 -5.8dB). 결론: **선형 한계=비선형 스펙트럴 디퓨전 당위**.

### C. Neural Operators
15. Neural operators (FNO, DeepONet) — ViT/연산자 릴스 연계

### D. 로보틱스·SLAM·임바디드
16. VLA 모델 (π0, OpenVLA, RT-2, X-VLA, GR00T N1)
17. Masked Trajectory Models / RoboTTT (test-time training)
18. Colorized LiDAR SLAM (Livox Mid-360 + 카메라, Scan Context++)
19. 로컬LLM 휴머노이드 SLAM + 캠핑 (NRF 제안서 주제, Mac Studio M5 Ultra 백팩)

### E. 온디바이스 AI·경량화
20. 온디바이스 AI / 이미지 클러스터링 (본인 연구분야)
21. 양자화·경량화: GPTQ, AWQ, SpinQuant, QAT
22. DINOv3 (비전 백본)

### F. LLM 메모리·ICL·에이전트
23. LLM 장기기억·에이전트 메모리 SOTA 10 (Titans, Mem0, Letta, Zep, MAGMA, HippoRAG2 …)
24. ICL / emergence / gradient descent (in-context learning)

### G. 기타 AI 개념
25. JEPA / world models
26. Jev / "System One Model" (typed AI)
27. ViT (vision transformer)

### H. 스펙트럼 기억·창의력 (신규 2026-10)
28. **"창의력 = 아주 긴 기억력" — 푸리에 중첩 기반 기억장치** (교수님 발상)
    - 르장드르 vs 푸리에 기저: **르장드르=충실한 장기저장**(비주기·무한지평 LegS), **푸리에/복소=재조합·위상**(binding)
    - HiPPO / LMU / **FRU(푸리에 기저, 유한주기)** / HiPPO-LegS(무한지평·척도불변)
    - **HRR/FHRR** 홀로그래픽 기억 — 순환합성곱=푸리에 곱, **위상결합·중첩**(= CDMA/FDMA 원리)
    - **복소/위상 기억** = 대각 복소 SSM(S4D·S5·LRU): 감쇠 복소진동자 $e^{(-\alpha+j\omega)t}$ — 크기=기억길이, 위상=주파수
    - 🟢 **빈 땅**: 복소SSM(무한지평) + FHRR 위상결합 → **"생성형 홀로그래픽 기억"**, 창의=위상 보강간섭(constructive interference)
    - ⚠️ 함정: 중첩 용량·누화 천장(무한주기≠무한용량), 순수 푸리에 시간국소성 약함(웨이블릿/Gabor 대안), 창의력 미조작화
    - 연결: [[스펙트럴 디퓨전 × 빔스페이스]](#14) · 빔포밍 위상/CDMA · 슈퍼트위스팅 강인성
    - ✅ **toy 조작화**(note:spectral-memory-fhrr) → [[spectral-memory-creativity]]: T1 용량천장(N150→0.85), **T2 창의=위상재조합(ID인덱싱) L≤30 완벽→L150 0.28**, **T3 복소SSM α=0.04→lag25 완벽('긴 기억' 정량)**. 논제 "창의=긴기억+위상보강간섭" 수치분해. 빈땅: 생성형 홀로그래픽 기억·천장상향·위상=창의손잡이.

### I. 온디바이스 에이전트·모델 (신규 2026-10)
29. **메타 Muse 패밀리 — 온디바이스 에이전트·액티브 메모리**
    - Spark(프런티어 LLM, 1M) / **Glimmer(30B 오픈·온디바이스)** / **Wonder(최고성능, 2026.10.12)**
    - Glimmer 원리(공개): **logit distillation(Spark→30B) + on-policy distillation+RL + 4bit 양자화 + perception encoder + 제로샷 툴콜**
    - Wonder: **Active Memory / Active Focus**(기능만 공개, 메커니즘·논문 비공개) · "컨텍스트 길이보다 정보활용"
    - 연결: [[LLM 장기기억·에이전트 메모리 SOTA]](#23) · 온디바이스 경량화(#20-22)

### J. 비직교·합승 통신 × 딥러닝 (신규 2026-11)
30. **뉴럴 "합승통신" End-to-End 공동최적화** (교수님 발상: 타다 공유택시 ↔ 통신)
    - 비유: 같은 목적지 신호 **묶기**(네트워크코딩 XOR·MPLS 라벨·광 그루밍·WiFi A-MPDU) vs **포개기**(NOMA+SIC / RSMA / SDMA·MU-MIMO)
    - **RSMA** = 메시지를 공통+개별로 분할 → NOMA(완전디코딩)·SDMA(완전잡음처리)를 특수경우로 포함하는 **상위 프레임**
    - 수신 분리 난이도: SDMA < RSMA < NOMA(SIC 부담). 핵심변수 = SIC순서·전력/빔 배분
    - SOTA(2024–2026): 딥언폴딩 [[UWMMSE]]·**RS-BNN**(2407.06530) / GNN **NOMANet**(2502.05592)·**RS-GNN**(2607.11740)·gradient-GNN(2503.06077) / 오토인코더+**SICNet**(2603.12289)·super-constellation(2503.07509) / DRL mmW-NOMA(2205.06814) / 메타러닝 RSMA(2307.08822)
    - 🟢 **빈 땅**: **클러스터링(이산·Gumbel-Softmax) + 빔·전력(연속·GNN/언폴딩) + 수신분리(SICNet)** 를 **하나의 미분가능 신경망**으로 end-to-end. 대부분 논문이 유저 페어링을 고정해 회피 중.
    - 연결: [[CAT-MoEformer]](#3)(MoE=합승조합 선택) · [[VF-MoNBT]](#6) · 멀티빔 동시타격(#4) · 스펙트럴 빔스페이스(#14)

### K. 프라이버시·보안 × 온디바이스 (신규 2026-11)
31. **딥러닝 피처맵 보호·학습형 암호화** (교수님 질문: 피처맵 암호화 AI?)
    - 동기: **분할추론(split inference)** 의 중간 피처맵에서 원본을 복원하는 **model/feature inversion 공격** 방어
    - 암호연산형: **HE**(CryptoNets·CKKS) / **MPC**(Gazelle·Delphi·Cheetah) / **TEE**(Slalom) — 증명가능 보안이나 느림·고비용
    - 학습형(AI다움): **학습형 암호화**(Kiya 블록셔플·채널순열, 암호도메인 학습) / **정보병목·적대적 난독화**(NoPeek=dCor($x,z$) 최소화·Shredder·Cloak·DISCO·DPFE) / InstaHide(⚠️ Carlini 등에 복원 공격으로 깨짐)
    - 삼각 트레이드오프: 정확도 ↔ 보안강도 ↔ 연산/통신비용
    - 🟢 **빈 땅**: ① **"양자화=피처맵 보호" 공동학습**(4bit 압축이 inversion도 차단) ② **물리계층 피처암호**(랜덤 빔/위상으로 피처맵 전송 = 학습형 난독화 × 물리계층 보안 PLS)
    - 연결: 온디바이스 경량화(#20-22) · 양자화(#21) · [[공간 슈퍼트위스팅 개구]](#8)·위상결합 기억(#28)(물리계층 보안) · 뉴럴 합승통신(#30, 전송계층)

### L. 학습 동역학·오차보정 골격 (신규 2026-11)
32. **STSA — 초격자(슈퍼트위스팅) 확률근사** (교수님 관찰: 칼만 ≈ RL 갱신식) → [[super-twisting-stochastic-approximation]]
    - 통일 골격: **새 추정 = 옛 추정 + 게인×(관측−예측)** = 1차 확률근사(Robbins–Monro). 칼만 $x{+}K(z{-}Hx)$ ↔ TD $V{+}\alpha\delta$. 칼만·TD·SGD·미러하강·자연경사 모두 특수경우.
    - 차이: 게인을 **계산**(칼만 $K=PH^\top(HPH^\top{+}R)^{-1}$, 공분산 전파) vs **정함**(RL $\alpha$). 간극 메움 = **KTD**(Geist-Pietquin 2010·MM-KTD·Gen-KF-TD 2026).
    - PPO/SAC 이후 실주류 강자: **DreamerV3·TD-MPC2·MuZero/EfficientZero**(모델기반), LLM은 **GRPO/DPO**. 칼만식은 미개척(앙상블=가난한 칼만).
    - 🟢 **제안**: 1차·무기억 가정을 깨 **분수차+적분기억** 2차 골격 — $\theta{+}\alpha(-k_1|\delta|^{1/2}\mathrm{sign}\delta + u),\ u{-}\alpha k_2\mathrm{sign}\delta$. 유한시간·유계교란 상쇄. 결정론 Lyapunov(Moreno-Osorio) 증명 존재, **STW×확률근사 유한시간 증명은 미존재**(검색 확인) = 기여 지점(노이즈볼 도달+가속 수렴률).
    - ⚠️ 정직: 결정론 백본만 엄밀, 확률 확장은 출판가능 연구 프로그램(증명 미완).
    - 연결: [[슈퍼트위스팅/슬라이딩모드 × 빔포밍]](#7) · sliding-as-optimization(#9) · 물리STW 개구(#8)=물리/학습 twist 쌍 · 탐험·활용·신용할당 스레드

35. **Wasserstein-SMC 생성수송** (텔레그램: FM·확산의 ODE/PDE 전개를 입자필터로 대체 제안) → [[wasserstein-smc-generative-transport]]
    - 관찰: ODE 전개 = **보정항이 0인 예측 전용 골격** — #32 골격("새 추정 = 옛 추정 + 게인×오차")의 오차항 결손. 제안: 시간축 Feynman–Kac(SMC)로 전파+보정(가중치·리샘플).
    - 형식화: twist $\psi_t\approx\log\tilde p_t$(중간 주변분포 학습) · ESS-적응 스텝(NFE 절약) · **OT-리샘플**(와서스타인 바리센터).
    - 이론 타깃: $W_2(\hat\mu_K,p_1)\le$ 전파항+twist괴리항+리샘플분산 — **W2 삼각부등식으로 오차 합성**(KL은 metric 아님 → 합성 불가가 W2 선택 근거). 조악한 스텝 레짐에서 SMC 항이 지배하는 경계조건이 증명 본체.
    - 선행: FKC(ICML25)·TDS·MCGdiff — 전부 조건부/스티어링. 🟢 **빈 땅: 무조건 생성의 ODE 적분기 교체 + W2 오차 정리 + OT-리샘플**. ⚠️ "Particle Filters and Flows" 원문 확인 필수(제목 정면 충돌 의심).
    - 연결: [[STSA]](#32)(같은 필터골격 RL판) · [[phase-rope-flowmatching-motion-reward]](#34)(W2 bound 근거) · 동적 3DGS-PF 아이디어(제3응용, 역이식 후보)

### M. 표현학습·자기개선 피처 (신규 2026-11)
33. **RL 자기개선 피처 큐레이션** (교수님 아이디어: 큐에 raw data → 능동 획득·정렬·변환) → [[rl-self-curating-features]]
    - 분해 매핑: **능동획득=AFA**(AISTATS2025 CS-HPPO·survey 2502.11067) · **조정=RL 피처변환/생성**(group-wise 2501.10555·MARL 2504.17355·2511.21934) · **정렬=RL 피처선택** · **큐=스트리밍/OSFS**
    - 🟢 **빈 땅**: 조각은 다 있으나 **[획득+정렬+변환]을 단일 RL 정책으로 + 스트리밍 + 자기 다운스트림 개선 보상**으로 묶은 self-improving end-to-end는 미존재.
    - 설계: Queue→추출→정책(3헤드 acquire/rank/transform, 계층·MoE)→다운스트림→보상 $r=\Delta$Perf$-\lambda$cost$-\mu$redund→피처수준 신용할당.
    - 난제: 보상 지연·노이즈(신용할당) · 행동공간 폭발(계층/MoE) · 스트리밍 비정상성(→STSA).
    - ✅ toy(note:rl-feature-curation): 스트리밍 비정상 회귀. **RL-curated MSE 2.31 < all 2.92 < fixed 3.03**(oracle 0.72), recall 0.39. 큐레이션이 전부/고정 이김(modest 양성). 크루스=피처 신용할당(discovery $|x\cdot e|$↔retention $|W|$ 딜레마), 하이브리드 credit이 to-do.
    - 연결: [[피처맵 보호]](#31)(큐레이션↔보호 쌍) · [[STSA]](#32)(비정상 강인 엔진) · 합승통신 MoE(#30) · 신용할당 스레드(피처축 RUDDER/HCA) · 온디바이스 비용항(#20-22)

### N. 모션 리워드·위상-분포 (신규 2026-11)
34. **Phase-RoPE × Flow-Matching 모션 프라이어** (교수님: 모션=위상+분포 → 리워드 설계 말고) → [[phase-rope-flowmatching-motion-reward]]
    - 매핑: **RoPE=회전 위상**($e^{i\omega_i t}$, 다중주파수=리듬 기저) · **flow matching=모션 분포 생성**(속도장 $v_\theta$). 두 키워드 1:1.
    - 선행: Flow Policy Gradients(2602.02481,휴머노이드+sim2real)·VITA·CoLA-Flow·π0 / RoPECraft(2505.13344 RoPE위상+FM)·MotionHiFlow(CVPR26 Joint RoPE)·AV-Link(박자동기). 🟢 **빈 땅**: RoPE를 리듬위상으로+FM을 물리제어 프라이어로=리워드없는 emergent 리듬·flow(현 RoPE+FM은 전부 kinematic 생성).
    - **심화(b) FM 프라이어=스타일 리워드**: $r^{style}(x,\phi)=-\mathbb E_{t,x_0}\|v_\theta(x_t,t;\phi)-(x-x_0)\|^2$. AMP 판별자의 **비적대적·멀티모달 보존** 대체(고정 목표, GAN 불안정 없음). 위상조건으로 박자 강제.
    - 열린 정리: FM 잔차 최소화 ⟺ $p_\pi\to p_{data}$ 수렴(GAIL식 divergence 상한) 증명 · 위상정합 · closed-loop RL 결합 · 리워드해킹.
    - ✅ **toy 검증**(note:spectral-credit-stsa): C1 리워드최대화=붕괴/α=1 soft=분포복원, C2 FM잔차 에너지 corr(logp)=0.93, C3 FM(분산0)이 AMP(덜학습 std 0.07)보다 정확·안정. **설계: soft/max-ent RL 필수**. + PSD 스타일(위상불변 리듬, Wiener-Khinchin 2.8e-14) + RoPE 위상조건 생성(각도오차 1.63→0.33rad).
    - ✅ **정리**(docs/05): 잔차 $\mathcal R=B(q)+C(q)$, $B{=}0\!\iff\!q{=}p_{data}$(proper), **KL$\le B/2\sigma^2$**(Girsanov)·$\sigma{=}0$이면 $W_2^2\lesssim B$. 수치: base=잔차최소, corr(R,KL)=0.73. 미완: $C(q)$ 상수화·주변불일치·실현오차.
    - **style/content 접목**: CONTENT=위상(RoPE)/STYLE=Gram=자기상관↔PSD(Wiener-Khinchin, 위상불변 리듬)/분포=FM → 리듬·flow 스펙트럴 3분해.
    - 연결: [[스펙트럼 기억]](#28)(RoPE=복소SSM $e^{(-\alpha+j\omega)t}$ 어텐션판 · Gram=PSD) · [[STSA]](#32)(강인 업데이트) · 파쿠르 SOTA(AMP/tracking을 FM으로 대체)

### O. 생성모델 샘플링·추론 (신규 2026-11)
35. **Particle-Filter 생성 플로우 — 확산/flow ODE를 PF로 대체** (교수님 아이디어) → [[pf-generative-flow]]
    - gap 확정: FKC(2503.02819)·SURGE·Wu2023 전부 **조건부/템퍼링**, 무조건 ODE 대체·NFE가속·오차한계는 미존재.
    - ✅ toy(note:pf-generative-flow): 예측–보정(알려진 $p_t$ 가중)–리샘플. **N=3 에너지거리 0.022 vs Euler 0.108(5배↓)** 저 NFE 압승. 순수 SMC는 N≥8 경로퇴화 열화 → **✅ rejuvenation(ULA move)이 봉합: N=5 0.0039 vs 0.052(13배↓), N=20 0.085→0.014 복구**. naive 어닐 실패.
    - 오차바운드: Euler $W_2{=}O(h)$ vs SMC $\le C_1/\sqrt K{+}C_2\epsilon_{score}$(h 1차항 없음). depth↔width 교환. rejuvenation으로 $\epsilon_{res}$ 억제가 핵심.
    - 각도: ESS-적응 SMC 생성기(메인)·Wasserstein SMC·compute 배분. (주: sliding/STW와 독립.)
36. **물리-potential SMC 생성 — 통계 prior × 물리 법칙 융합** (교수님 아이디어) → [[physics-potential-smc]]
    - 사후 ∝ $p_\theta$(생성=통계)×$\exp(-\lambda E_{phys})$(물리). 생성=제안, 물리=가중치, 리샘플=곱강제. = #35 PF머신+물리 potential.
    - ✅ toy(note:physics-smc-generation, 1D 중력): raw prior E=6.45 → 물리가이드 0.012/물리-SMC 0.041(참≈0), **다양성 보존**(std 0.27~0.29). 재학습 없이 추론때 통계+물리 융합 실증.
    - 각도: 비디오 확장($x_0$-예측 디코드 후 물리가중)·물리 potential 설계·#35 rejuvenation. vs 르쿤 JEPA(생성X)=다른 노선. 튜토리얼: `html/video-gen-tutorial.html`.
37. **생성형 JEPA — 시공간 latent에서 flow matching 조건부 미래예측** (교수님 아이디어) → [[generative-jepa]]
    - JEPA 약점=다음 latent 하나로 예측→다봉 미래 평균붕괴. 해법=flow matching 예측기로 조건부 미래 **분포** 생성(표현공간 생성). latent에 시공간 RoPE/복소SSM 위상(#28·#34) 보존.
    - ✅ toy(note:generative-jepa): 분기미래 $z=c\pm2$. 결정론 JEPA=전부 갭(무효 붕괴), 생성형 flow=좌/우 모드 복원(0.35/0.40, 갭 0.01). 다봉 보존 실증.
    - 선행 Stochastic Latent Variable JEPA(2611.09302)=확률잠재, **flow 버전 빈땅**. 참고 Wan=DiT+Flow Matching. 연결 #25·#28·#34·#35·#36.
38. **LeWAM — LeWorldModel + Action + Flow Matching + RoPE** (교수님 아이디어) → [[le-wam]]
    - LeWM(2603.19312) 분석: 인코더 CLS벡터, 예측기=인과트랜스포머+행동 AdaLN, **결정론 MSE + SIGReg(latent→N(0,I))**, 학습형 PE, CEM 계획. 한계=다봉 평균·짧은 지평.
    - 🟢 삽입점: **①Flow=예측기 MSE 헤드 교체**(조건부 flow, 행동 AdaLN 재사용) — 💎 **SIGReg가 latent을 N(0,I)로 만들어 flow base 공짜(궁합 최적)**. **②RoPE=시간축 PE 교체** → 지평 외삽(짧은지평 한계 직격).
    - ✅ toy(note:le-wam): 행동조건부 분기. 결정론 a=0→갭붕괴, flow a=−1→좌0.82/a=+1→우0.81/a=0→양쪽. 행동이 미래 분포 조절 실증.
    - 기여: ①가우시안 latent=native flow base ②RoPE 월드모델 지평 외삽.
39. **소산성 신경 KF 세계모델 — extended dissipativity로 학습** (교수님 아이디어) → [[dissipative-kf-worldmodel]]
    - KF=PF와 달리 샘플프리 예측–보정 → 효율 세계모델. **extended dissipativity(H∞·L2-L∞·passivity 통합 에너지지표)로 학습** = 소산적·안정 필터. 백본 Mamba(선택적 SSM=학습 상태전이)+칼만 보정 헤드.
    - 선행: KalmanNet·DynaNet·DL-KF / **KalMamba**(Mamba+KF 세계모델). 🟢 **빈땅=dissipativity를 학습목적으로** 쓴 신경 KF 세계모델 없음.
    - ✅ toy(note:dissipative-kf-worldmodel): 샘플프리 SSM 적합. plain 불안정 11%·rollout발산 최대norm 16.0 vs **dissip 0%·최대 0.5**. 세계모델 '관측없는 상상 rollout' 안정성을 소산성이 보장(=#38 롤아웃 드리프트 근본해결).
    - 🧭 나침반(에너지기반·샘플효율·물리·학계 소규모) 전적 부합. 연결 #32(칼만≈RL)·#38·#35(PF↔KF 상보).
40. **Quantum-inspired 세계모델 — 복소·간섭·텐서네트워크** (교수님 발상: 물리AI 다음은 양자물리AI?) → [[quantum-inspired-worldmodel]]
    - 양자=단순확률 아님, **복소진폭+간섭+얽힘**. #28 복소SSM·FHRR·#34 RoPE가 이미 quantum-inspired(위상 간섭).
    - 3갈래 분리: (A)QML on 양자컴(하이프·장기) (B)**quantum-inspired 고전컴**(텐서넷·복소NN·FHRR) (C)AI for 양자과학(고전, 실용). "0/1컴에 참 양자알고리즘=무의미(맞음), quantum-inspired 수학=고전서 유의미".
    - 🧭 판정: **(B)(C) 고전=나침반 부합(근미래·학계·numpy toy 가능)**, QML-on-QPU=나침반 벗어남(장기 관찰). 다리: MPS 상태표현·복소SSM·NQS. 연결 #28·#34·#39.
    - 🆕 **GLM(Monday) 의견 반영(11-22)**: 융합 위상 3분해(노트=위상 B · C=STSA 칼만융합 재릴 · A=궤적수준) · PhysDiff=B의 결정론 특수사례(사영→확률융합 일반화 프레이밍) · PF 정당화=접촉 다봉성(랑제방 백색잡음→엔진 구조화 탐색 대체) · sim2real=제안-목표 KL 명시항 · 비디오 확장 디코드시점 가중의 조기퇴화 비판+λ어닐링 대안 · E-다양성 파레토 보고 권장 · #35 이중노트 병합 권장.

> 상세: `html/neural-beamforming-research.html`(lab) · `note` 레포 neuralbeamforming 브랜치 · wiki sources/concepts.
> 코드·검증: `note` 레포 **spectral-credit-stsa**(#28·#32·#34) · **pf-generative-flow**(#35) 브랜치 — #28 스펙트럴 신용할당(설계형 FIR Hann > TD(λ), AUC 0.170 vs 0.202) + #32 STSA(고정 STW 외란불변≈0.164, 적응게인 STW 양축 지배 A 0.051/D 0.132). proof-of-concept, 수렴정리 미완.

### O. 모방학습·분포 매칭 (신규 2026-11)
39. **Occupancy-Matching 모방학습 — 궤적 추적 → 궤적 분포 매칭 리워드** (텔레그램: IL×RL 융합 제안) → [[occupancy-matching-imitation]]
    - 발상의 이름 = 점유분포 매칭: GAIL(2016)→DICE/IQ-Learn→SMODICE→DM-IL(sliced-W 2023)→AMP(2021 전이분포 스타일 리워드)→2026 궤적수준 비적대·**리턴 분포 매칭**(리스크 감성, distributional RL의 IL 이식).
    - #34가 이미 절반: FM 잔차 리워드=비적대 occupancy matching의 모션 스타일 특수사례 · §9 이론(KL≤B/2σ²·W2²≲B) 보유 · toy 완료(corr 0.93 vs AMP 불안정).
    - 🟢 빈 땅: 비적대·판별자 없는 **전체 궤적** FM-잔차 occupancy matching + §9 상한의 occupancy bound 격상 + $r_{task}+\beta r^{FM}_{occ}$ 융합(물리성·다양성 파레토). ⚠️ "score-as-reward" 이웃 계열 확인 필요.
    - 연결: #34(잔차 리워드 본가) · [[STSA]](#32)(max-ent 엔진) · #36(물리성 파레토) — "점 추정 대신 분포" 테마(IL판)의 세 번째 얼굴.

---

## 🅱 Monday 쪽 (텔레그램에서 거론 — Monday가 채워 넣기)

Monday(GLM-5.3): 네가 교수님과 텔레그램에서 **연구주제로 얘기한 것들**을 Fryday처럼 여기에 정리해 줘.
- 각 주제를 이 섹션에 목록화
- 필요하면 `wiki/sources/`·`concepts/` 에 노트, `html/` 에 정리본(→lab)
- 중복 주제는 🅰 와 교차링크(`[[...]]`)로 연결

(채워지기 전 — 비어 있음)

---

## 📌 관리 규칙
- 새 주제 거론 시 → 담당 AI가 이 원장에 추가(1줄) + 깊이 생기면 위키 노트/HTML로 확장.
- 월 1회 Fryday·Monday가 🅰🅱 교차검토해 중복 병합·상호링크.
