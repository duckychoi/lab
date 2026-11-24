---
title: "Occupancy-Matching 모방학습 — 궤적 추적이 아니라 궤적 분포 매칭을 리워드로"
created: 2026-11-22
author: fryday
tags: [concept, imitation-learning, occupancy-measure, gail, amp, distribution-matching, ledger-39]
ledger: 39
status: 판정-#34로병합(→#34종료)(2026-11-24)
---

# Occupancy-Matching 모방학습 (IL×RL 융합)

> [!warning] ⚖️ 외부 판정 (2026-11-24): **#34로 병합(→ #34 종료)**
> 원장에서 인용한 상한은 본가에서 철회됨. #34가 'AMP가 이미 푸는 문제'로 정리됨.
> 정본: note:fm-reward-v2 `VERDICTS.md` · `review/post38_20261124/README.md`. 아래 본문의 toy 결과·'빈 땅' 주장은 판정 이전 기록이다.

> 발상 경로: 텔레그램 — "IL과 RL을 융합할 순 없을까? 궤적을 따라가게 하지 말고 **궤적의 분포**를 따라가게 하고, L2 loss 대신 **분포를 잘 따라가면 리워드**를 주는 방식".

## 1. 이 아이디어의 학술적 이름 = 점유분포(occupancy measure) 매칭

정확히 이 발상이 10년 된 활발한 계열이다:
- **GAIL**(Ho & Ermon 2016) — 판별자가 정책 궤적분포 vs 전문가 궤적분포를 구분, 판별 신호를 리워드로. 원조.
- **DICE 계열**(ValueDICE·IQ-Learn 2020·DemoDICE) — 판별자 없이 오프폴리시 분포비율 추정(primal-dual). **SMODICE** — f-divergence.
- **Distribution-Matching IL**(Cohen 2023) — **sliced-Wasserstein, 판별자 없는** 버전.
- **AMP**(Peng 2021) — 물리 휴머노이드에서 **상태 전이 분포 매칭을 스타일 리워드**로(모션 쪽 표준). task reward(=content)+style reward(=판별자) 분해.
- 2025~26 최신: 궤적 수준 비적대적 매칭(arXiv 2601.00452 — 지원집합 제약·취약 목적함수 문제 다룸) · **Imitation Learning as Return Distribution Matching**(Lazzati 2026, OpenReview — 리스크 감성 버전).

## 2. 두 축의 쉬운 해설 (GLM)

**AMP — "따라하지 말고 분위기가 비슷하면 점수"**: 전통 L2 추적은 (a)리깅하디 (b)복구 상황 실패 (c)리워드 손설계 지옥. AMP는 (s,s′) 전이쌍 판별자를 학습 → "전문가 것이라 착각할 확률"을 스타일 리워드로. 춤 비유: 프레임 카피(추적) vs 관객 판별(AMP). 약점 3: 적대적 불안정 · **리워드 해킹** · **모드 붕괴(스타일 평균 뭉개짐)**.

**리턴 분포 매칭 — "평균만 닮지 말고 운의 패턴까지"**: Abbeel–Ng(2004) "기대 리턴만 같으면 미지 리워드에서도 성과 비슷"의 맹점 — 평균이 같아도 분산·꼬리는 다르다(택시 기사: 평균 20만·나쁜 날 12만 vs 평균 20만·나쁜 날 5만). IL을 **리턴 분포 매칭**으로 정식화 + 리스크 감성 다이얼. = **distributional RL의 IL 이식** — "점 추정 대신 분포" 테마(#32 칼만→분포적 RL)의 IL판.

## 3. 볼트와의 관계 — #34가 이미 절반

- #34 §3 = 이 발상의 **비적대적 모션 스타일 특수사례**: AMP 판별자를 **FM 잔차 에너지**로 교체($r^{style}=-\mathbb E_{t,x_0}\|v_\theta(x_t,t;\phi)-(x-x_0)\|^2$).
- #34 §9 = 이미 이 리워드의 **이론 보유**: $\mathrm{KL}(q\|p_{data})\le B/2\sigma^2$(Girsanov), $\sigma{=}0$이면 $W_2^2\lesssim B$. → "잔차 최대화+max-ent ⟺ 분포 매칭" 증명済.
- ✅ toy: FM 잔차 corr(logp)=0.93·분산 0 vs AMP(덜학습 std 0.07 불안정). **soft/max-ent RL 필수**(argmax=모드붕괴).

## 4. 🟢 빈 땅 (정직)

1. **비적대·판별자 없는 전체 궤적 occupancy matching with FM-잔차 리워드**: 기존 비적대 계열(SMIL류)은 표본 간 거리(sliced-W). 플로우 잔차를 궤적 전체 단위 리워드로 쓰는 IL은 문헌 미확인 (⚠️ "score-as-reward" 이웃 계열 존재 — 커밋 전 1회 확인).
2. **이론 확장**: #34 §9 상한을 IL occupancy bound로 격상 — 판별자 분산(GAIL 만성 약점) 없는 수렴 보증.
3. **IL+RL 진짜 융합**: $r=r_{task}+\beta r^{FM}_{occ}$ — DemoDICE가 판별자 기반으로 한 조합을 비적대 생성모델 잔차로. 물리성·다양성 파레토(#36 프레임) 연결.
4. **리턴 분포 버전**: FM-잔차를 리턴 분포 매칭으로 — 위 1+2에 리스크 다이얼 얹기(앰비셔스, 후순위).

## 5. 실험 설계

- 베이스라인: GAIL·AMP·SMIL·DemoDICE. 환경: MuJoCo 로코모션 + 휴머노이드(#34 파이프라인 재사용).
- 지표: 태스크 성공률 + 물리성(#36) + **스타일 다양성·모드 커버리지**(AMP 모드붕괴 대비).
- toy(1일): 2-모드 전문가 분포에서 FM-잔차 리워드 + max-ent 정책 → 모드 커버리지 vs GAIL류. #34 toy 자산(C1~C3) 직접 재활용 가능.

## 6. 리스크

1. FM-잔차 리워드의 궤적 길이 확장(스타일 윈도우→전체 궤적) 시 밀도 추정 품질 저하.
2. "score-as-reward" 선행 발견 시 델타 재설계(가속: occupancy bound 이론만으로도 차별).
3. AMP와의 성능 판정은 물리성·다양성 파레토여야 한다(단일 FID류 지표 금지 — 볼트 규칙).

## 7. 연결

[[research-topics-ledger]] #39 · [[phase-rope-flowmatching-motion-reward]] #34(잔차 리워드·이론 본가) · [[super-twisting-stochastic-approximation]] #32(max-ent 업데이트 엔진) · [[physics-potential-smc]] #36(물리성 파레토) · AMP↔FM 교체는 #34 §3과 동일 명제의 IL 일반화.

## 8. 다음 액션

toy: 2-모드 GMM 전문가분포 + FM-잔차 리워드 + soft-RL → 모드 커버리지(AMP식 판별자 대비) — #34 C1~C3 코드 재활용, 1일.
