---
title: C-JEPA — 객체 단위 잠재 개입으로 배우는 월드모델
type: source
domain: ai-news
tags: [ai-news, source, jepa, world-model, object-centric, causal, lecun]
created: 2026-07-12
updated: 2026-07-12
sources: [C-JEPA.md]
reliability: high
---

# C-JEPA — Causal-JEPA: Learning World Models through Object-Level Latent Interventions

> [!insight] 핵심 인사이트
> **[[JEPA]]의 마스킹을 "이미지 패치"에서 "객체(object) 단위"로 끌어올려 상호작용·인과 추론을 강제한 월드모델.** 객체 하나를 가리고 나머지 객체들로부터 추론하게 만들어 "만약 이 객체가 없었다면?"에 가까운 **latent intervention(잠재 개입)** 효과를 낸다 → shortcut을 막고 인과 학습을 강제. [[Yann-LeCun]] 공저(2026).

## 도메인별 추출 (ai-news)

- **신뢰도**: arXiv 2602.11389 · GitHub 205★ · [[Yann-LeCun]]·Randall Balestriero·Heejeong Nam(Brown) 등 공저 → ⭐⭐⭐⭐
- **즉시 활용**: NO(연구 단계) — 다만 "객체 단위 마스킹" 아이디어는 [[임바디드-AI]] 추론·영상 이해에 이식 가능.
- **6개월 영향력**: 인과 JEPA는 [[월드모델]] 계보의 최신 꼭짓점(공간→시간→행동→**객체/인과**). 다음은 개입형·다물체 인과로 갈 가능성.
- **허와 실**: 벤치 강함(반사실 +20%, 패치 대비 1% 특징으로 8× 빠른 플래닝)이나 CLEVRER/Push-T 등 통제 환경 위주 — 실세계 복잡 상호작용은 future work.

## 핵심 수치

- **CLEVRER VQA**: 전체 83.88% / 반사실 60.19% — SlotFormer·OCVP-Seq 상회, 반사실 추론 **+20%**(동일 구조 대비)
- **Push-T 제어**: 88.67%(6×128 토큰 ≈ 패치의 1%) vs DINO-WM 91.33%(196×384) — 근접 성능 + **8× 빠른 플래닝**
- **구현**: VideoSAUR/SAVi 슬롯 인코더 + 객체 슬롯 마스킹(7슬롯 중 0~4개), L2 잠재 예측, Stable-WorldModel/Pretraining 기반

## 관련 페이지
- [[JEPA]] · [[월드모델]] · [[Yann-LeCun]] — 상위 개념·저자
- [[JEPA-월드모델-서베이-2026]] — 이 논문이 포함된 서베이
- [[Flow-JEPA-연구아이디어]] — 파생 연구 아이디어
- [[임바디드-AI]] · [[Meta]]
- [[ai-news]]

## 원본
- 출처: arXiv 2602.11389 · github.com/galilai-group/cjepa · hazel-heejeong-nam.github.io/cjepa
- 신뢰도: ⭐⭐⭐⭐ (LeCun 공저, GitHub·프로젝트페이지 공개)
