---
title: DexJoCo — MuJoCo 기반 작업 지향 손재주 조작 벤치마크
type: source
domain: ai-news
tags: [ai-news, robotics, mujoco, dexterous-manipulation, benchmark, slam-3dgs]
created: 2026-05-19
updated: 2026-05-19
sources: []
reliability: medium
---

# DexJoCo — MuJoCo 기반 작업 지향 손재주 조작 벤치마크

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 로봇 손(덱스터러스 핸드) 제어 연구를 위한 MuJoCo 기반 표준화 벤치마크·툴킷. "작업 지향" 설계로 단순 포즈 달성이 아닌 실제 작업 완수 중심 평가. 재현 가능한 로봇 손 제어 연구 인프라 표준화 시도.

## 도메인별 추출 (ai-news / slam-3dgs 교차)

- **신뢰도**: HF 업보트 39 (2026-05-18), arXiv 2605.16257, 학술 벤치마크 논문
- **즉시 활용**: PARTIAL — MuJoCo 환경 사용하는 로봇 제어 연구자에게 즉시 유용. 일반 개발자에겐 간접 참조
- **6개월 영향력**: [[ClawGym]](로봇 클로 Gym 표준화)과 함께 로봇 손 제어 평가 표준 클러스터 형성. 물리 시뮬레이션 기반 로봇 AI 재현성 향상에 기여
- **대체 관계**: IsaacGym·Brax 등 기존 로봇 시뮬레이션 환경 대비 작업 지향성 강조
- **허와 실**: MuJoCo 시뮬레이션 ↔ 실제 로봇 전이 성능은 별개 문제. 시뮬-to-real 갭 검증 필요
- **액션**: slam-3dgs 도메인 로봇 제어 연구 방향 추적 시 참조

## 관련 페이지

- [[ClawGym]] — 로봇 클로 에이전트 Gym 스타일 표준화
- [[HY-Embodied]] — 실세계 로봇용 소형 임베디드 모델
- [[HiVLA]] — 계층적 시각 기반 로봇 조작 시스템
- [[ExoActor]] — 3인칭 영상 기반 휴머노이드 행동 제어

## 원본

- 출처: https://huggingface.co/papers/2605.16257
- 신뢰도: ⭐⭐ (업보트 39, arXiv 2605.16257, 2026-05-18)
