---
title: "Open-HumanScale — 1인칭 영상 5만 시간으로 로봇 월드-액션 모델 사전학습. 84.60% SOTA 는 사람+로봇 혼합 모델 몫, 사람 영상만은 68.88%"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, hf-paper, vla, world-action-model, egocentric-video, scaling-law, open-data, pku]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/papers/2611.06817]
reliability: medium
---

**논문**: [2611.06817](https://huggingface.co/papers/2611.06817) · DAGroup-PKU · 업보트 **34**(볼트 11-09 `api/papers` · 수집기 31) · 프로젝트 https://dagroup-pku.github.io/open-humanwam/ · 코퍼스·파이프라인·체크포인트·평가 스위트 공개(초록 기준 · 저장소 링크 API 에 없음)

## 핵심 인사이트
> [!insight] 사람 1인칭 영상 시간 ↔ 로봇 성공률의 로그-선형 스케일링
> Open-HumanScale-50K(손 모션·언어 밀집 주석)로 폐루프 시뮬 평가에서 **데이터 시간과 로봇 성공률의 로그-선형 관계**를 보고. 사람 영상은 로봇 텔레옵보다 훨씬 싸게 늘릴 수 있으므로, 이 법칙이 성립하면 [[VLA]] 사전학습 데이터 전략이 바뀐다.

> [!warning] 두 모델의 데이터가 다르다 — 헤드라인 SOTA 를 "사람 영상만의 성과"로 읽지 말 것
> HumanWAM-**Vanilla**(사람 영상만): Clean2Clean 92.08% / **Clean2Random 68.88%** / RoboDojo 14.17%·진척 19.00.
> HumanWAM-**Goal**(사람+로봇 혼합 + 시각 목표 조건): 92.70% / **84.60%**(SOTA).
> Clean2Random 의 +15.7%p 는 **로봇 데이터 혼합과 목표 조건이 함께 바뀐 비교**다([[비매칭-비교]]). RoboDojo 14.17% 는 Goal 쪽 값이 초록에 없다. 수치는 볼트 초록 재검출 전건 일치.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: RoboTwin 2.0 Clean2Random 84.60%(초록 자기 주장)
- **실시간 가능성**: 미기재
- **응용 가능성**: 공개 50K 코퍼스는 휴머노이드/로봇팔 사전학습 데이터로 바로 재사용 후보. in-context 적응(파라미터 업데이트 없이 새 시각 목표 추종)은 실기 관찰 — 정량 없음
- **필수 레퍼런스**: YES — 공개 범위가 넓음(데이터+레시피+체크포인트)

## 관련 페이지
- [[VLA]] · [[월드모델]] · [[비매칭-비교]] · [[SLA-Spatial-Language-Action]](11-08 VLA) · [[리서치-휴머노이드-로봇-VLA로컬LLMSLAM-기반-제어의-2026-최신-동향]](같은 배치 크론)

## 원본
- 출처: https://huggingface.co/papers/2611.06817
- 확인 범위: HF papers API 초록(볼트 재조회 · 수치 7종 검출)
- 신뢰도: ⭐⭐ (전면 공개 주장 · 저장소 미확인)
