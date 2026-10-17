---
title: "연구주제 공유 원장 (Research Topics Ledger)"
created: 2026-10-14
updated: 2026-10-17
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
