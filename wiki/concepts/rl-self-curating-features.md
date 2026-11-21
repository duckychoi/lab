---
title: "RL 자기개선 피처 큐레이션 — 스트리밍 raw data에서 능동 획득·정렬·변환"
created: 2026-11-21
author: fryday
tags: [concept, reinforcement-learning, active-feature-acquisition, feature-selection, feature-transformation, streaming, representation-learning, ledger-33]
ledger: 33
status: research-program
---

# RL 자기개선 피처 큐레이션 (Self-Curating Feature RL)

> 교수님 아이디어: 큐에 아무 raw data나 넣으면 → 피처 추출 → **능동으로 자기에게 도움되는 피처를 획득·정렬·조정하며** RL로 학습하는 시스템.

## 1. 분해 → 기존 분야 매핑 (조각은 다 존재)
- **"능동 획득"** = Active Feature Acquisition (AFA). 비용 vs 성능으로 어느 피처를 살지 순차 결정.
  - Towards Cost Sensitive Decision Making, AISTATS 2025 (Active-Acquisition POMDP + CS-HPPO 계층정책)
  - Survey on AFA Strategies 2025 (arXiv 2502.11067)
- **"조정/구성"** = RL Feature Transformation/Generation.
  - Group-wise Reinforcement Feature Generation (arXiv 2501.10555)
  - Collaborative Multi-Agent RL Feature Transformation (arXiv 2504.17355)
  - Heterogeneous MARL + Attention (arXiv 2511.21934)
- **"정렬/선택"** = RL Feature Selection (MDP: 상태=피처집합, 행동=추가/제거, 보상=검증성능−비용).
- **"큐/스트리밍"** = Online/Streaming Feature Selection (OSFS 계열).

## 2. 통합 gap (= 기여 지점)
현재 논문은 **한 조각만** 푼다(획득만/변환만/선택만). 비어 있는 것:
> **임의 raw data 스트림 → 피처 추출 → 단일 RL 에이전트가 [획득 + 정렬 + 변환]을 동시에, 자기 다운스트림 학습 개선을 보상으로 self-improving** 하는 end-to-end 시스템.

## 3. 아키텍처 설계 (제안)
```
[Queue: raw data 스트림]
      │
      ▼
[Feature Extractor fθ]  ── 후보 피처 풀 Φ_t 생성
      │
      ▼
[RL Policy π]  (계층/MoE)   세 행동 헤드:
   ├─ ACQUIRE : 어느 후보 피처를 (비용 c 내고) 가져올지        (AFA)
   ├─ RANK    : 보유 피처 정렬/선택 (top-k, 중요도)            (selection)
   └─ TRANSFORM: 피처 변환·결합 연산 적용 (±,×,log,group-op)   (feature gen)
      │
      ▼
[Downstream Learner g]  ── 예측/제어 수행
      │
      ▼  보상 r_t = ΔPerf(g) − λ·cost − μ·redundancy
[Credit Assignment] ── 어느 피처가 도움됐나 (feature-level)
      └───(정책 업데이트, STSA로 비정상 강인)───┘
```

### 보상 설계
$$r_t = \underbrace{[\mathcal L_{t-1}-\mathcal L_t]}_{\text{다운스트림 개선}} - \lambda\underbrace{c(\text{acquire})}_{\text{획득비용}} - \mu\underbrace{\text{redund}(\Phi_t)}_{\text{중복 페널티}}$$
- 느리고 노이즈 많은 보상 → **피처 수준 신용할당**(RUDDER/HCA를 피처축으로) 필요.

### 행동공간
획득×정렬×변환 = 조합폭발 → **계층 RL(상위: 무엇을/하위: 어떻게)** 또는 **MoE 라우팅**(#30 CAT-MoEformer식).

## 4. 난제 (정직)
1. **보상 지연·노이즈** → 신용할당 난제. (앞선 신용할당 스레드와 직결)
2. **행동공간 폭발** → 계층/MoE 필요.
3. **스트리밍 비정상성** → 분포 변동. 여기에 **STSA(강인 확률근사, #32)** 가 업데이트 엔진으로 들어감.
4. **평가**: "self-improving"이 실제로 베이스라인(고정 피처/AutoML)을 이기는지 공정 비교 설계.

## 5. 연결
- [[research-topics-ledger]] #33.
- [[feature-map-encryption]] #31 — 피처 큐레이션 ↔ 피처 보호(쓸까/숨길까)의 쌍.
- [[super-twisting-stochastic-approximation]] #32 — 비정상 스트리밍 강인 업데이트 엔진.
- [[neural-superposition-comms]] #30 — MoE 라우팅(획득·변환 조합 선택).
- 신용할당 스레드(RUDDER/HCA) — "어느 피처가 도움됐나" = feature-level credit.
- 온디바이스 경량화(#20-22) — 비용항 c = 연산/메모리 예산.

## 6. 상태 / 다음
- 상태: **개념(research program)**, 코드·실험 없음.
- 다음 후보: ① AFA survey·group-wise·multi-agent transform 원문 정독해 state/action/reward 설계 정교화 ② toy 프로토타입(스트리밍 피처에서 RL 선택+변환) 구현 ③ 피처 수준 신용할당 + STSA 결합 정식화.
