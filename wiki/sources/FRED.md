---
title: "FRED — 비디오 확산 기반 World Action Model 의 단일 디노이징 스텝 미래표현을 자기증류. 인간 영상에만 있는 과제 50.0% vs 경쟁 WAM 19.4%"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, world-action-model, video-diffusion, self-distillation, manipulation, human-to-robot, kaist, hf-paper]
created: 2026-10-25
updated: 2026-10-25
sources: [BadWAM.md]
reliability: medium
---

# Self-Distilling Future Video Representations for World Action Models (FRED)

**HF**: https://huggingface.co/papers/2610.30320 · KAIST AI · 코드 https://github.com/suhyeok-jang/FRED
**실측(2026-10-25 KST)**: upvote **37**(수집기 일치) · 저자 Huiwon Jang · Suhyeok Jang · Hyeonmo Kang 외
**도메인 재분류**: 수집기 `ai-news` → **`slam-3dgs`**(로봇 매니퓰레이션 · 카메라 입력 월드모델)
**신뢰도**: ⭐⭐⭐ (실세계 실험 · 코드 기재 · 초록 수치 1쌍)

> [!insight] 🏆 핵심 인사이트 — **같은 배치의 [[LaLa-World]] 와 정반대 노선이다 → [[대립레시피-동시도착]]**
> FRED = **픽셀 생성(비디오 확산) 쪽 월드모델**을 고쳐 쓴다(단일 스텝 표현 품질을 자기증류로 올림). LaLa-World = **생성하지 않는 잠재 예측(JEPA형)** 이 비디오 생성 베이스라인과 *"comparable … with 6× less training cost and 13.9× faster planning"* 이라고 주장한다.
> 🎯 **두 논문 모두 상대 노선을 직접 대조하지 않는다**(FRED 의 경쟁군은 다른 WAM · LaLa 의 대조군은 RAEv2 비디오생성). ⇒ [[JEPA-vs-Diffusion-월드모델]](07-12) 의 "수렴 지점" 질문에 **같은 날 양쪽 증거가 도착**했으나 판정은 불가.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 초록 기준 경쟁 WAM 대비 우세 · 특히 장기·도메인 외 과제. 정량 1쌍: *"reaching **50.0%** task success on tasks absent from robot training data and demonstrated only in human videos, compared with **19.4%** for the best competing WAM"* (2.58배)
- **실시간 가능성**: 🎯 **"단일 디노이징 스텝"이 설계 목표 자체** = 확산 월드모델의 추론 지연을 정면으로 다룸. 단 Hz 수치는 초록에 없음
- **카메라 파이프라인**: 과거 관측 조건화 + 미래 관측 표현 타깃(학습 시 정답 미래 프레임 사용)
- **응용 가능성**: 인간 시연 영상 → 로봇 전이는 데이터 수집 비용을 바꾼다
- **필수 레퍼런스**: [[BadWAM]](WAM 취약성) 과 같이 읽을 것

> [!question] 미해결
> 50.0% 의 과제 수·시도 수(분모) — 초록 없음. 과제 수가 작으면 50.0 vs 19.4 의 신뢰구간이 넓다. 본문 미열람.

## 관련 페이지
- [[LaLa-World]] · [[JEPA-vs-Diffusion-월드모델]] · [[대립레시피-동시도착]] · [[Diffusion-월드모델]] · [[월드모델]] · [[VLA]]
- [[BadWAM]] · [[Physical-RSI]] · [[임바디드-AI]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2610.30320
- 신뢰도: ⭐⭐⭐ (HF upvote 37 · KAIST · 코드 기재)
