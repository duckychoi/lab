---
title: "MAI-Thinking-1 / Rocket — Microsoft AI의 대규모 비동기 RL 레시피"
created: 2026-11-24
author: fryday
tags: [source, reinforcement-learning, grpo, llm-post-training, infrastructure, microsoft]
---

# MAI-Thinking-1 / Rocket (Microsoft AI)

- 원문: [MAI-Thinking-1 기술보고서(PDF, 109쪽)](https://microsoft.ai/pdf/mai-thinking-1.pdf) · [RL infrastructure at Microsoft AI](https://microsoft.ai/news/rl-infrastructure-at-microsoft-ai/) · 계기: Threads @choi.openai 요약
- 구현 정리·코드: note 레포 `mai-rocket-grpo` 브랜치 (`docs/METHOD.md`, `src/mai_grpo.py`, `docs/PREREG.md`)

## 요지
사내 RL 프레임워크 **Rocket**(컨트롤러·문제 워커·롤아웃 워커·SGLang 추론·YOLO 학습기)으로 수천 GPU에서 몇 주~몇 달 비동기 RL. 타사 모델 증류 없이 MAI Base 1→MAI-Thinking-1, 현재 MAI Base 2(3T) 후학습 중.

## 알고리즘
토큰 레벨 GRPO + (1) **엔트로피 적분제어로 움직이는 비대칭 상한 클립** r^tr=clip(r,1−ε,(1−ε)^{-1}+k), k←clip(k+δ·sign(H*−Ĥ),0,k_max) (ε=0.6, k_max 2.5, δ 0.25, H* 0.3) + (2) **외부 비율 클립** r_max=50. KL·엔트로피 보너스 없음. 보상 R_task + 0.5·언어일관성 − 0.25·(통과율×길이/ℓmax). early-exit(16개, 통과율 0.05–0.8) + 통과율 필터(0.1–0.8, G=128), top-p 0.97 마스크 재생, 길이 8k→128k, 5스텝/갱신·8갱신 staleness 상한, lr 1e-6(긴 길이 9e-7).

## 안정화가 진짜 핵심
학습–추론 로그확률 괴리는 RL이 진행될수록 커짐 → bf16·MoE 라우팅 재생·top-p 마스크 재생(MAI-T1), Rocket 2는 o_proj 복제·FP32 동일순서 전문가 합·공유 FA4·fake-quant로 **비트 단위 일치**. 붕괴 시 RL trace로 **자기증류 SFT 후 재개**(O(1M) 성공 trace, 후반 체크포인트 혼합). 학습기만 재시작(~5분, GPU시간 7%+ 절약).

## 주장 강도
공개 벤치(MAI-Thinking-1)는 경쟁권·선두 아님(저자 명시). "Opus 4.8 추월"은 사내 집계 벤치 자기보고, 수치 미공개.

## 우리 점검 (판정 아님)
numpy 레퍼런스 단위테스트 12/12. 표 toy에선 엔트로피 제어기 미개입(필터가 먼저 학습 중단, 또는 상한 미발동). 상한 발동 시 k↑가 엔트로피를 오히려 낮춤(0.469→0.446) — 상한 완화는 양의 어드밴티지 토큰을 키우므로 '대안 탐색' 효과는 저확률 토큰이 양의 어드밴티지를 받을 때만. LLM 규모 판정은 PREREG(튜닝된 DAPO clip-higher·엔트로피 보너스 기준선, 같은 계산량).
