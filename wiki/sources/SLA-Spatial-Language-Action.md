---
title: "SLA — π0.5 에 3D 공간 정렬을 연속 사전학습부터 넣은 VLA. 수치 4종은 절대값뿐, 베이스라인 대비는 미확인"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, vla, pi0.5, 3d-perception, continual-pretraining, hf-paper, hkust-gz]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/papers/2611.08373]
reliability: medium
---

**논문**: arXiv 2611.08373 · HF papers 업보트 **83**(볼트 11-08 09:05Z API) — 🔴 수집기 11-07 보고 **150**(*"11-06 데일리 1위"*) 와 불일치 → [[계수기-배수]] · HKUST(GZ) · 코드 없음 · [프로젝트 페이지](https://embodiedsla.github.io/)

## 핵심 인사이트
> [!insight] "공간 감독을 언제 넣느냐"가 VLA 일반화의 변수
> 기존 [[VLA]] 는 2D VLM 표현을 물려받고 3D 감독은 태스크 적응 때만 넣는다. SLA 는 사전학습된 π0.5 에서 출발해 **행동 예측 + 중간 시각 임베딩 ↔ 동결된 3D 인식 모델 표현 정렬**을 *연속 사전학습과 후학습 둘 다*에 적용한다. 보조 모듈(feature-dependent gate · depth/카메라 보정의 부분 활용 · 확률적 state dropout)은 **학습 때만** 쓰여 추론 구조·가중치가 그대로 재사용된다 — 배포 비용 0 의 개선이라는 점이 실용적.

> [!warning] 절대값만 있다
> 프로젝트 페이지(볼트 grep 4/4 검출): LIBERO-Plus 7축 가중 성공률 **87.4%** · RoboTwin 2.0 Clean2Random 50태스크 **72.3%** · RoboCasa-Panda 24태스크 **68.4%** · RoboDojo-Real 실물 3종 **33.9%**. **π0.5 원본 대비 증분은 볼트도 수집기도 미확인** — 개선폭을 말할 수 없다. 실물 33.9% 는 시뮬레이션 수치와 2배 이상 격차.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 3D 인식 모델을 "교사"로 쓰는 암묵적 공간 정렬 — 명시적 SLAM/점군 입력 없이 공간성을 가중치에 넣는 계열.
- **실시간 가능성**: 추론 구조 불변 ⇒ π0.5 와 동일 지연.
- **카메라 파이프라인**: RGB(+부분적 depth·캘리브레이션, 학습 시만).
- **응용 가능성**: 로봇 조작 정책 연구라면 "3D 교사 정렬 손실" 아이디어만 차용 가능. 코드 미공개라 재현 불가.
- **필수 레퍼런스**: 베이스라인 표가 공개되면 재평가.

## 관련 페이지
- [[VLA]] · [[계수기-배수]]
- 같은 날 크론: [[리서치-2026년-휴머노이드-로봇의-AI로봇공학-융합-시대-도래]](VLA 동향)

## 원본
- 출처: https://huggingface.co/papers/2611.08373
- 확인 범위: HF papers API 초록(볼트 11-08) · 프로젝트 페이지 HTML grep · 본문 표 미열람
- 신뢰도: ⭐⭐ (논문 · 코드 없음 · 비교 수치 미확인)
