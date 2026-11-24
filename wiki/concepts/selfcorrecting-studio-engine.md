---
title: "자기교정 디지털‑스튜디오 데이터 엔진 — 멀티태스크 일관성=공짜 관측 + 소량 실 보정"
created: 2026-11-23
author: fryday
tags: [concept, data-engine, synthetic-data, multi-task, consistency, kalman-filter, 3d-vision, gaussian-splatting, ledger-43]
ledger: 43
status: 판정-★주력질문(재정의:능동실측선택)(2026-11-24)
---

# 자기교정 디지털‑스튜디오 데이터 엔진 (#43)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **★주력 질문(재정의: 능동 실측 선택)**
> 원 toy 12회 실측 2.451→0.990이지만 최종 오차>1 비율 46%. 실영상(Middlebury 15쌍) 실측점 선택은 균등 대비 8.37%/6.95%로 10% 관문 미달, 새 13장면 '보정할지' 규칙은 3% 문턱보다 1.73% 나쁨. 새 질문: 값싼 관측을 먼저 읽고 실측의 종류·위치·중단 시점을 골라 같은 비용으로 물리 오차를 더 줄이기. 점수 ΔP=PHᵀ(HPHᵀ+R)⁻¹HP 자체는 고전 실험설계 — 신규 후보는 편향·오대응 하에서 예상 개선과 실제 개선의 차이를 교정하는 규칙(근접: Dexheimer CVPR'23 깊이 공분산 능동측정, Park CVPR'24).
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 디지털 스튜디오가 합성 멀티태스크 데이터(뎁스·포즈·모캡·3DGS)를 GT 공짜로 뽑되, **태스크 간 기하 일관성(reprojection)을 공짜 관측 + 소량 실촬영을 보정**으로 칼만 루프에 묶어 붕괴를 막고 실데이터를 절감. = **#42를 멀티태스크 3D 비전으로 스케일.**

## 동기
교수님의 AI 영상제작 툴 = 조명·카메라·3D 제어하는 **합성데이터 공장**. 합성만 학습하면 sim-to-real 갭 + 재귀생성 붕괴(스튜디오 편향 상속·증폭). 기존 최강책 '소량 실 혼합'([2512.13411])은 고정비율 비효율. 빈 땅 = **멀티태스크 상호 일관성을 자기교정 관측으로** 쓰는 필터 루프.

## 아이디어 (필터)
- 예측 = 스튜디오 합성 생성(편향 b) → 공분산↑.
- **일관성 관측(공짜)** = reprojection 잔차(GT 불필요) → 오차의 '비일관' 방향 n̂ 소거.
- **실 관측(비쌈·희소)** = 일관성이 못 보는 **게이지 방향 ĝ**(일관되지만 틀린 스케일 drift) 보정.
- 칼만게인=적응신뢰, (1-K)<1=수축(#39)=붕괴 없음.
- 통찰: **gauge ambiguity**(bundle adjustment 구조) — 일관성이 부분공간을 공짜로 죽이니 비싼 실은 게이지 한 축만 → 조금으로 충분.

## toy (note:selfcorrecting-studio-engine)
2D 오차공간, 편향 b=0.06·n̂+0.025·ĝ, 4법(naive/cons/mix/ours), T=120, 300시드.
- Part1 동일예산(실 12회): naive **7.80**(붕괴100%) · 일관성만 3.01 · 실혼합만 2.45 · **ours 0.99**(실혼합 2.5×↓). reprojection 잔차 ours 0.27 vs 실혼합만 2.26.
- Part2 궤적: naive 선형발산(7.80) vs ours 유계수렴(0.99).
- Part3 샘플효율: **ours 실 3회=1.88 > mix 실 12회=2.45** → 4× 적게 쓰고 우위.

## 차별점 / 가치
조각들(스플랫-포즈 [2412.00138]·few-real+synth [2512.13411]·월드모델 데이터엔진 [GigaWorld-0/Mirage2Matter])은 존재 → 신규 = **필터‑지배 자기교정 + 멀티태스크 상호일관성 관측 루프 + 수축 붕괴보증**. 제품엔 즉효 데이터전략, 논문엔 "일관성이 실데이터 예산을 접는다" 정량주장.

## 정직한 한계
일관성 단독은 게이지 drift 못 막음(실 앵커 필수). toy 선형·방향 기지 가정 → 실제 reprojection 비선형, EKF/KalmanNet식 학습게인 필요. 학습된 뷰모델서 생성 시 그 오차 상속(garbage-in) → 실관측 보정이 차단기.

## 대표 수혜 태스크
metric depth(Apple Depth Pro 계열: 픽셀별 카메라시선 z) · camera pose · mocap/skeleton · 3DGS/4DGS · optical flow — 전부 "GT 공짜 렌더 + 큰 sim2real 갭" → #42/#43 루프의 수혜 1순위.

## 연결 (🧭 나침반 정중앙)
원장 #43. [[filtering-synthetic-robust]] #42(본가) · [[dissipative-kf-worldmodel]] #39(수축) · [[quantum-inspired-kf]] #41 · [[rl-self-curating-features]] #33(큐레이션) · [[research-synergy-map]] · [[research-topics-ledger]].
