---
title: "LaLa-World — 행동과 시각 변화를 전부 자연어로 기술해 시뮬·로봇·일반 영상을 JEPA형 잠재 월드모델 하나로. 비디오생성 대비 학습 1/6 · 계획 13.9배"
type: source
domain: slam-3dgs
tags: [slam-3dgs, world-model, jepa, latent-world-model, language-action, mpc, naver, robotics, hf-paper]
created: 2026-10-25
updated: 2026-10-25
sources: []
reliability: medium
---

# LaLa-World: Scaling Latent World Models with Natural Language Actions

**HF**: https://huggingface.co/papers/2610.27851 · [[NAVER]] AI Lab · published 2026-10-21 · 코드 https://github.com/junha1125/LaLa-World
**실측(2026-10-25 KST)**: upvote **37**(수집기 일치) · 저자 Junha Song · Geonmo Gu · Jeongeun Park 외
**도메인 재분류**: 수집기 `ai-news` → **`slam-3dgs`**(로봇 계획·정책)
**신뢰도**: ⭐⭐⭐ (정합 비교 명시 · 코드 기재 · 공개 벤치 LIBERO·RoboCasa)

> [!insight] 🏆 핵심 인사이트 — **이종 데이터 결합의 접착제가 "행동을 언어로 쓰기"다**
> 초록: *"we describe both numerical actions and visual changes in language, enabling joint training of a single future predictor across heterogeneous datasets"* + 예측기를 LM 위에 구축.
> 🎯 로봇마다 다른 행동 공간(관절 수·좌표계)을 **언어라는 공통 인터페이스로 평탄화** ⇒ 시뮬·로봇·일반 이미지/비디오를 한 모델에. [[JEPA]] 계열이 그동안 약했던 "스케일링 데이터원" 문제에 대한 답.
> ✅ **정합 비교를 명시한다**: *"In a **matched comparison** with an RAEv2-based video generation model baseline, LaLa-World reaches **comparable** planning performance with **6× less training cost and 13.9× faster planning**"* ⇒ 성능 우위가 아니라 **동등 성능의 비용 우위** 주장이다(과장 없이 읽으면 이렇다).

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 도메인별 개별 LWM 대비 MPC 평균 계획 성능 우위 · LaLa-Policy 는 LIBERO·RoboCasa 에서 Cosmos Policy 와 *"competitively"*(=대등) · 추론 *"up to 5.5×"* 빠름(최대치)
- **실시간 가능성**: 계획 속도 13.9배가 핵심 — 비디오 생성 기반 상상(imagination) 계획의 병목 제거
- **카메라 파이프라인**: 시각 변화도 언어로 기술 → 잠재 공간 예측(픽셀 생성 없음)
- **응용 가능성**: 🎯 **[[JEPA효율화-로컬추론]](볼트 synthesis) 의 실측 근거 추가** — "생성하지 않으면 싸다"가 정합 비교로 나왔다
- **필수 레퍼런스**: [[FRED]](반대 노선, 같은 날)

> [!warning] 한정어
> "5.5×" 는 *"up to"*, LIBERO·RoboCasa 는 *"competitively"* — 우위가 아니라 대등. 볼트는 이 한정어를 유지한다 → [[한정어-탈락]].

## 관련 페이지
- [[FRED]] · [[JEPA]] · [[JEPA-vs-Diffusion-월드모델]] · [[JEPA효율화-로컬추론]] · [[대립레시피-동시도착]] · [[월드모델]] · [[Yann-LeCun]]
- [[NAVER]] · [[Physical-RSI]] · [[VLA]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2610.27851
- 신뢰도: ⭐⭐⭐ (HF upvote 37 · NAVER AI Lab · 코드 기재)
