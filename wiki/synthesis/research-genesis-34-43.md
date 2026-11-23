---
title: "연구 탄생 비하인드 #34–#43 — 한 대화가 낳은 '필터링=학습' 연구선"
created: 2026-11-23
author: fryday
tags: [synthesis, genesis, onboarding, lineage, kalman-filter, world-model, synthetic-data]
purpose: 다른 agent(Monday/GLM 등)가 #34–#43의 동기·맥락·연결을 빠르게 이해하도록 하는 온보딩 서사
---

# 연구 탄생 비하인드 #34–#43

> 이 문서는 **다른 agent 온보딩용**이다. #34–#43이 "왜·어떤 순서로·무슨 직감에서" 태어났는지의 서사.
> 개인정보·비연구 맥락(과제 행정·투자 평가·신상)은 의도적으로 제외. 연구 논리만 남김.

## 씨앗 (한 줄의 관찰)
강화학습 튜토링 중, 교수님이 두 갱신식이 **같은 모양**임을 포착:
- 칼만: $x \leftarrow x + K(z - Hx)$   ·   RL: $v \leftarrow v + \alpha(G - v)$
→ "**보정(filtering) = 학습(learning)**" 이라는 직감이 이후 전 연구선의 중심축이 된다. (KF↔RL = #32 계열)

## 1막 — 생성 동역학을 '필터'로 보기 (#34–#38)
- **#34 phase-rope-flowmatching-motion-reward**: RoPE를 $e^{i\omega t}$ 위상으로 해석. flow-matching 잔차를 **모션 스타일 리워드**(비적대 occupancy matching)로. → 위상 축의 출발.
- **#35 pf-generative-flow**: 교수님 발상 — flow matching/diffusion의 **PDE/ODE 적분을 particle filter로 대체**. (ODE↔PF 상보)
- **#36 physics-potential-smc**: 생성 SMC에 **물리 potential 가이던스**(접촉 다봉성). Monday/GLM 교차리뷰 반영.
- **#37 generative-jepa**: 르쿤 심화 후 — JEPA와 flow matching을 **표현공간에서** 결합(픽셀 생성 아님).
- **#38 le-wam**: LeWorldModel/world-action-model, 행동조건 + RoPE 지평 외삽.

## 2막 — 르쿤 나침반 (상시 방향)
교수님이 르쿤 Threads(결합임베딩/EBM · 고차원 확률 비현실 · SIGReg 비대조 · "RL 버려라" · 물리세계 AI)를 읽히고 **상시 나침반**으로 설정. → `project_research_compass` 메모리 + 원장 상단.
- **정직한 긴장**: #35/#37의 생성 요소 vs 르쿤 "생성 버려라". → **표현공간 생성**이라 픽셀 낭비 회피로 양립(열린 질문). 플래그십이 그 구체적 답.

## 3막 — 샘플프리 필터 세계모델 (#39–#41)
- **#39 dissipative-kf-worldmodel**: 교수님 발상 — **KF는 PF와 달리 샘플을 안 써 효율적**이고 env 관측으로 보정·물리 모델링 가능. **extended-dissipative(에너지기반) 네트워크로 학습된 KF = 세계모델**, 백본은 **Mamba(SSM)** 와 잘 맞음. → 소산성/수축이 안정축의 핵.
- **#40 quantum-inspired-worldmodel**: 교수님 — "물리 AI 다음은 양자물리 AI?" 양자=단순확률 아님, **복소진폭+간섭+텐서네트워크**. 3갈래(QML-on-QPU 장기 / quantum-inspired 고전 / AI-for-양자과학). 나침반 부합=고전 quantum-inspired.
- **#41 quantum-inspired-kf**: 교수님 — "양자 PF는 별로?" → 간섭을 **샘플링이 아니라 표현(복소/텐서넷 상태)** 에 붙이고 필터는 샘플프리 KF. toy로 샘플프리 다봉 + 위상 간섭 실증.

## 4막 — 필터가 '합성데이터 시대'를 만나다 (#42–#43) ★현재
- **#42 filtering-synthetic-robust**: 교수님 — "세상에 synthetic data가 넘칠 텐데, **KF/PF로 NN을 학습**시키는 합성데이터 강건학습 연구 있나?" → 근접논문 **2512.00757**(Contraction-Conditioned Neural Filters) 정독: 수축 패널티는 있으나 KF/PF 아님 + **참값 오라클 라벨** 사용(실전 불가). → 재프레이밍: **합성=예측 / 실데이터=보정 관측 / 칼만게인=적응신뢰 / (1-K)=수축(#39)=붕괴 없음**. toy 검증(동일 예산 KF 0.146 vs mix 0.230).
- **#43 selfcorrecting-studio-engine**: 계기 = Threads(@shqkel1863)의 Apple **Depth Pro 2**(픽셀별 카메라시선 metric z) 공지 + 교수님이 만드는 **AI 영상제작 툴**. 직감 — "**전방향 조명·카메라뷰 디지털 스튜디오**가 뎁스·포즈·모캡·3DGS 데이터를 GT 공짜로 찍어내고 서로 보정하면 전 모델이 좋아진다." → **#42를 멀티태스크 3D 비전으로 스케일**: 태스크 간 **기하 일관성(reprojection)=공짜 관측**(오차 부분공간 소거) + 소량 실촬영=게이지 보정. toy 검증(동일 예산 ours 0.99 vs mix 2.45, 실데이터 4× 절감).

## 관통하는 하나의 생각
**"필터링(예측–보정 · 에너지/수축 · 샘플프리 · 위상/복소 표현)이 학습·생성·세계모델·그리고 이제 합성데이터 학습을 관통하는 단일 원리"** — 같은 아이디어가 여러 의상(RL update, flow 적분, world model, synthetic-data 학습)으로 반복 등장. 전부 🧭 나침반(샘플효율·안정·물리·표현예측·학계 소규모) 위.

## 정직하게 보존한 것들 (agent 주의)
- **음성/혼합/부정 결과를 숨기지 않음**: #33 RL 큐레이터 소폭(2.31<2.92), #34 rectified-coupling 음성(corr 0.77→0.25), #42 adaptive-KF 교환(최속 회복 but 정상오차↑), #43 게이지 drift 잔존(일관성 단독 불충분).
- **근접논문 충돌 매번 확인**(FKC 2503.02819, LeWorldModel, Contraction Neural Filters 2512.00757 등) 후 차별점 명시.
- **numbering 주의**: 이 연구선은 #34–#43(그리고 하위 #44~). 원장 section O의 "#39 Occupancy-Matching"은 **별개 이전 항목의 번호**(섹션별 번호 충돌) — 월례 교차검토 때 정리 대상.

## 통합 지점
[[research-synergy-map]] — 2공통축(에너지·위상) + 클러스터5(필터‑지배 합성데이터 엔진=#42/#43). 플래그십 = "소산성·위상 Mamba 세계모델 + 적응 KF↔PF 예측기 + 물리 potential 교정 + SIGReg 표현". 교수님 AI 영상제작 툴 = #43 데이터엔진의 실체.

## 연결
[[research-topics-ledger]] 전체 · [[project_research_compass]](메모리) · 하위과제 맵 [[digital-studio-benefit-map]].
