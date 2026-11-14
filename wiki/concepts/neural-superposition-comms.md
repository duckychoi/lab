---
title: "뉴럴 합승통신 — 비직교 다중접속 End-to-End 공동최적화"
created: 2026-11-14
author: fryday
tags: [concept, beamforming, NOMA, RSMA, MU-MIMO, deep-learning, ledger-30]
ledger: 30
---

# 뉴럴 "합승통신" End-to-End 공동최적화

> 교수님 발상: **타다 공유택시** — 같은 목적지 신호를 뭉쳐 보내고 도착점에서 나눔 ↔ 통신 다중접속.

## 1. 두 갈래: 묶기 vs 포개기
- **묶기(aggregation)** = 같은 목적지/경로 흐름을 한 트립으로: 네트워크코딩(XOR, butterfly/COPE), MPLS 라벨, 광 트래픽 그루밍, WiFi 프레임집성(A-MPDU).
- **포개기(superposition)** = 목적지 달라도 한 채널에 겹쳐 싣고 수신단에서 분리.

## 2. 포개기 3종 — 분리 메커니즘
### NOMA + SIC
송신 $x=\sqrt{p_1}x_1+\sqrt{p_2}x_2$ ($p_1\gg p_2$). 수신은 센 신호부터 복원·제거(SIC).
$$\text{SINR}_1=\frac{p_1|h_1|^2}{p_2|h_1|^2+\sigma^2},\quad \text{SINR}_2=\frac{p_2|h_2|^2}{\sigma^2}$$
### RSMA (상위 프레임)
메시지 → 공통 $s_c$ + 개별 $s_k$. 송신 $x=\mathbf{p}_c s_c+\sum_k\mathbf{p}_k s_k$.
수신: 공통 먼저 모두 디코딩·제거 → 개별. 간섭을 **부분 디코딩/부분 잡음**으로 유연 분할 → NOMA·SDMA를 특수경우로 포함.
### SDMA / MU-MIMO
공간(빔)으로 분리. ZF: $\mathbf{p}_k\perp\mathbf{h}_j\ (j\neq k)$. SIC 없음, 채널 직교성 필요.

분리 난이도: **SDMA < RSMA < NOMA**.

## 3. 딥러닝 SOTA (2024–2026)
- **딥언폴딩**(해석가능·데이터효율): UWMMSE(WMMSE+GNN 펼치기), **RS-BNN**(arXiv 2407.06530, RSMA 최적빔 구조로 출력차원↓), 리뷰 2502.05952.
- **GNN**(순열등변·크기 일반화): **NOMANet**(2502.05592, NOMA 전력배분, SCA급 성능·추론 700배↑, *그룹핑 고정*), **RS-GNN**(2607.11740, 확장형 RSMA 프리코딩), gradient-GNN(2503.06077), recursive GNN(2402.18332).
- **오토인코더/학습형 송수신기**: AE-PD-NOMA + **SICNet**(리뷰 2603.12289), super-constellation(2503.07509).
- **DRL**(이산 페어링·클러스터링): mmW-NOMA 전력+하이브리드빔(2205.06814).
- **메타러닝**(부분 CSIT): RSMA 메타 프리코더(2307.08822).

## 4. 🟢 빈 땅 (연구 포지션)
대부분 논문이 **유저 클러스터링을 고정**하고 빔·전력만 최적화. 미개척:
1. **이산+연속 동시미분**: 클러스터링을 Gumbel-Softmax로 완화 → GNN 프리코딩·SICNet 수신기와 한 그래프에서 역전파.
2. **RSMA를 메타아키텍처로**: 공통/개별 분할비까지 학습 → NOMA·SDMA 자동선택.
3. **순열등변 GNN × 언폴딩 × 수신단(SICNet)** 삼위일체.

## 5. 내 연구 연결
- [[research-topics-ledger]] #30.
- #3 CAT-MoEformer(MoE=합승조합 선택) · #6 VF-MoNBT(뉴럴 빔) · #4 멀티빔 · #14 스펙트럴 빔스페이스.
- 전송계층 보안으로 #31 피처맵 물리계층 암호와 연결.
