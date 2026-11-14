---
title: "연구주제 공유 원장 (Research Topics Ledger)"
created: 2026-10-14
updated: 2026-11-14
author: fryday
tags: [research-ledger, shared-hub]
---

# 연구주제 공유 원장

Fryday·Monday가 텔레그램에서 교수님과 **연구주제로 거론한 것들**을 한곳에 모아 관리한다.
새 주제가 나오면 해당 AI가 여기에 추가하고, 위키 노트(sources/concepts)·HTML(lab)로 확장한다. 상호 교류의 인덱스.

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
14. **스펙트럴 디퓨전 × 빔스페이스** — 빔포밍 생성 사전확률(블루오션)

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

> 상세: `html/neural-beamforming-research.html`(lab) · `note` 레포 neuralbeamforming 브랜치 · wiki sources/concepts.

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
