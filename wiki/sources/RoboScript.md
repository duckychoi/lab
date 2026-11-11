---
title: "RoboScript (WICL) — 가중치 대신 컨텍스트에 배운다: 시연 1개 + 시뮬 리허설로 RoboTwin 2.0 50과제 평균 83.4% (그래디언트 업데이트 0)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-paper, robotics, in-context-learning, manipulation, simulation]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/papers/2611.12885]
reliability: medium
---

**논문**: [2611.12885](https://huggingface.co/papers/2611.12885) *World In-Context Learning for Agentic Robot Manipulation* · ArcheOne-AI · 업보트 **27** · 코드 [ArcheOne-AI/RoboScript](https://github.com/ArcheOne-AI/RoboScript) ★**39**(GitHub API 볼트 실측 · HF 캐시 값은 36) · Apache-2.0 · created 2026-11-05

## 핵심 인사이트
> [!insight] 문맥에서 배우는 것은 겉모습이 아니라 절차다
> 고정(frozen) 모델이 시연 1개에서 출발해 **시뮬레이터에서 과제를 리허설하고 피드백을 가중치가 아닌 컨텍스트(Task Memory)에 적는다.** 그 메모리를 얼린 채 새 장면에 배포한다. 저자 관찰: 문맥 학습이 기록하는 것은 과제 단계·물체 역할 같은 의미 정보라 다른 세계로 옮겨진다. RoboTwin 2.0 **50개 과제 전체 평균 성공률 83.4%**(clean+randomized · 과제당 시연 1개 · 업데이트 0)로 가장 강한 학습형 정책보다 **20점 이상** 높다(초록 전문 일치).

> [!warning] 읽을 때 붙일 조건
> - "20점 이상"의 비교 대상 정책 이름과 그 정책의 학습 데이터 양은 초록에 없다. 시연 1개 vs 대량 학습의 비교인지 확인 필요.
> - **같은 과제를 시뮬레이터에서 리허설할 수 있다는 것이 전제**다. 시뮬 자산이 없는 과제에는 그대로 못 쓴다.
> - 실물 양팔 로봇 전이는 "된다"는 서술뿐, 성공률 수치는 초록에 없다.
> - 레포는 생성 6일째 · ★39.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 저자 주장 기준 RoboTwin 2.0 에서 학습형 정책 대비 +20점 이상. 볼트 독립 확인은 초록까지.
- **실시간 가능성**: 초록에 추론 지연·호출 횟수 없음. 파운데이션 모델을 매 스텝 부르는 구조라면 느릴 수 있다(추정).
- **카메라 파이프라인**: 배포 입력은 "실로봇에서 얻을 수 있는 것만" 쓰도록 데이터 격리(초록).
- **응용 가능성**: 재학습 없이 과제를 추가하는 경로 — 전날의 [[A2-MEAS]](동결 가중치 + 런타임 교정 코드)와 같은 방향. 학습 대신 문맥·코드로 적응하는 로봇 연구가 이틀 연속 입고됐다.
- **필수 레퍼런스**: RoboTwin 2.0 · 본 논문 코드.

## 관련 페이지
- [[VLA]] · [[A2-MEAS]] · [[DexForesight]] · [[리서치-휴머노이드-로봇-SLAMVLA로컬LLM-기반-제어-최신-동향]]

## 원본
- 출처: https://huggingface.co/papers/2611.12885
- 확인 범위: HF papers API 초록 전문 · GitHub API 메타 · 🔴 본문 · 코드 미열람
- 신뢰도: ⭐⭐ (업보트 27 · ★39)
