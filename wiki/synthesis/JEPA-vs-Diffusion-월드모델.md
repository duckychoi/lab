---
title: JEPA vs Diffusion 월드모델 — 두 패러다임의 대비와 수렴
type: synthesis
domain: ai-news
tags: [ai-news, synthesis, world-model, jepa, diffusion, comparison]
created: 2026-07-12
updated: 2026-10-25
sources: [JEPA-월드모델-서베이-2026.md, Flow-JEPA-연구아이디어.md, C-JEPA.md, LaLa-World.md, FRED.md]
reliability: high
---

# JEPA vs Diffusion 월드모델 — 대비와 수렴

> [!insight] 핵심 인사이트
> [[월드모델]]은 "미래를 어떻게 표현하느냐"로 두 축이 갈린다. **[[JEPA]] = 잠재 예측(비생성)**, **[[Diffusion-월드모델]] = 픽셀 생성.** 그런데 이 둘은 경쟁이 아니라 **상보적**이며, 2026년 흐름은 *수렴*이다 — 같은 [[Meta]]팀이 [[JEPA]]와 디퓨전(NWM)을 모두 만들고, 하이브리드([[Flow-JEPA-연구아이디어]])가 그 사이를 메운다.

## 대비

- **예측 대상**: JEPA는 미래의 *잠재 임베딩*, Diffusion은 *다음 프레임 전체 분포(픽셀)*.
- **디테일 처리**: JEPA는 예측 불가능한 디테일을 **버림**(효율·추상화), Diffusion은 디테일이 **자산**("Visual Details Matter" — DIAMOND).
- **불확실성**: JEPA는 결정론 predictor라 다봉 미래를 뭉갬(mode-averaging) → latent z 필요. Diffusion은 분포를 샘플링해 다봉 자연스러움.
- **비용**: JEPA는 렌더링 없이 가벼움. Diffusion은 무겁고 느린 롤아웃·오차 누적(→ Diffusion Forcing·consistency로 완화).
- **용도**: JEPA=샘플효율 RL·계획·견고 표현 / Diffusion=인터랙티브 시뮬·데이터 생성·자율주행 시나리오.

## 수렴 지점 (2026)

- **NWM** — [[Meta]] LeCun팀이 만든 *디퓨전* 월드모델(CDiT). JEPA와 같은 팀이 두 축을 병행.
- **잠재 디퓨전 WM** — GAIA-2가 픽셀이 아닌 잠재에서 디퓨전(중간 지점).
- **Flow × JEPA** — [[Flow-JEPA-연구아이디어]]: 표현공간에서 조건부 flow → JEPA의 추상화 + 디퓨전의 확률성. 브릿지(Stochastic Interpolant)로 "현재→미래"를 직접 잇는 방향이 가장 신선.

> [!action] 실행 관점
> 로봇/계획·샘플효율 → JEPA 계열. 인터랙티브·데이터 생성·자율주행 → Diffusion 계열. **둘 다 필요하면 하이브리드**(잠재 flow/bridge)를 노려라.

## 관련 페이지
- [[JEPA]] · [[Diffusion-월드모델]] · [[월드모델]]
- [[C-JEPA]] · [[Flow-JEPA-연구아이디어]] · [[JEPA-월드모델-서베이-2026]]
- [[임바디드-AI]] · [[Yann-LeCun]] · [[Meta]] · [[NVIDIA]]
- [[ai-news]]

## 원본
- 근거 소스: [[JEPA-월드모델-서베이-2026]] · [[Flow-JEPA-연구아이디어]] · [[C-JEPA]]
- 신뢰도: ⭐⭐⭐⭐ (다수 1차 소스 교차 종합)

## 🔄 2026-10-25 — 3개월 만의 갱신: 정합 비교 1건 · 같은 날 반대편 1건
> [!insight] [[LaLa-World]] 가 이 페이지의 "수렴 지점" 질문에 처음으로 **정합(matched) 비교** 를 줬다
> *"In a matched comparison with an RAEv2-based video generation model baseline, LaLa-World reaches **comparable** planning performance with **6× less training cost and 13.9× faster planning**"* ⇒ 🎯 **JEPA 쪽 이점은 성능이 아니라 비용**(동등 성능). 07-12 대비표의 "효율" 행에 첫 정량 근거.
> 🎯 **수렴의 방향도 보인다**: LaLa 는 비디오 생성 모델의 **언어 조건 인터페이스를 차용**했다(*"adopting the language-conditioned interface of video generation models"*) — JEPA 가 Diffusion 쪽 인터페이스를 흡수.

> [!warning] 반대편 — [[FRED]](같은 날)
> 확산 WAM 의 약점(추론 지연)을 **단일 디노이징 스텝**으로 공략. 인간 영상 전용 과제 50.0% vs 경쟁 WAM 19.4%. 🔴 **두 논문 모두 상대 노선과 직접 비교하지 않는다** → [[대립레시피-동시도착]]. ⇒ 비용 축은 JEPA 우위 근거 1건, 일반화 축은 확산 개선 근거 1건 — **같은 축 비교가 아니므로 승패 판정 불가.**

### 관련 페이지 추가
- [[LaLa-World]] · [[FRED]] · [[대립레시피-동시도착]] · [[JEPA효율화-로컬추론]] · [[NAVER]]
