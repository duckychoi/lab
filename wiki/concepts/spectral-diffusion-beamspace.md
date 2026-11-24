---
title: "스펙트럴 디퓨전 × 빔스페이스 — 빔포밍 생성 사전확률"
created: 2026-11-21
author: fryday
tags: [concept, beamforming, diffusion, generative-prior, beamspace, spectral, ledger-14]
ledger: 14
status: 판정-보류(2026-11-24)
---

# 스펙트럴 디퓨전 × 빔스페이스 (#14)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **보류**
> 데이터가 1-모수 다양체라 모수(각도) 적합이 정답(−12.0 dB=진리), 가우시안 사전 −7.7·영채움 −5.4. 재개 조건: 기존 방법이 실패하는 현상을 먼저 찾을 때.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 빔패턴 $P(\theta)=|w^H a(\theta)|^2$ = 각도영역(DFT dual)=beam-space=스펙트럴. "좋은 빔포머 분포" 생성 사전으로 ill-posed 설계·복구.

## toy (note:spectral-diffusion-beamspace, ULA N=16)
- 매니폴드 유효차원 10/16 → beam-space 저차원(스펙트럴).
- **(A) 게인제약만 ill-posed → 선형-가우시안 사전 실패**(MAP −7dB < 매칭필터 −13dB): 전방향 데이터라 μ≈0, 전역 2차통계가 방향 위상 비선형 못 담음.
- **(B) inpainting(소자 고장 복구) → 사전 유효**: k=8 사전 −8.6 vs 영채움 −5.8dB(진리 −12). 사전이 역문제 복구를 일관 개선.

## 결론
사전은 유효하나 **선형은 방향 비선형성에 약함 → 비선형·조건부 생성사전="스펙트럴 디퓨전"이 필요**. 선형 프록시 한계=디퓨전 당위.

## 🟢 각도
① beam-space 조건부 디퓨전(저사이드로브·널 제약) ② sparse 각도 도메인 디퓨전 ③ 생성형 빔 설계(시나리오 조건부 샘플→per-scenario 최적화 대체).

## 연결
원장 #14. 빔포밍 메인(#1~11) · [[neural-superposition-comms]] #30 · [[spectral-memory-creativity]] #28 · diffusion=spectral autoregression #13.
