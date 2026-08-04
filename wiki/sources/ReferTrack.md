---
title: ReferTrack — 참조 후 추적(Referring Then Tracking) 임보디드 비주얼 트래킹
type: source
domain: slam-3dgs
tags: [ai-news, hf-paper, embodied-ai, visual-tracking, vla, robotics, referring, sim2real]
created: 2026-07-25
updated: 2026-07-25
sources: []
reliability: medium
---

# ReferTrack (Referring Then Tracking for Embodied Visual Tracking)

> [!insight] 핵심 인사이트
> HF Daily ↑47. 임보디드 비주얼 트래킹(EVT) — 이동 에이전트가 **자연어로 지시된 대상**을 온보드 비전만으로 추적 — 에서 기존 [[VLA]] 정책의 약점(추상적 공간에서 CoT 추론 → 실제 이미지 검출과 약결합)을 지적하고, **2단계**로 접지한다: ①**Referring** — 전방 카메라에서 검출된 바운딩박스 집합 중 대상을 고르는 **제약된 객관식**으로 식별을 이미지 공간에 접지, ②**Tracking** — "Refer-CoT" 토큰으로 확정된 대상에 조건화해 추적 웨이포인트 디코딩. 슬라이딩 윈도우 bbox 큐(TVBI 토큰)로 시간적 모션 단서 유지. **RL 없이 단일표적 추적 89.4% 성공**, 단일 전방카메라가 다중카메라 베이스라인을 능가, 4족·휴머노이드 실로봇 sim-to-real 확인.

> [!note] 배경 정보
> "추론을 추상 공간이 아니라 **명시적 이미지 검출(bbox)에 접지**"하는 방향은 [[BadWAM]]("예측은 맞고 행동은 틀림", 예측≠행동 접지)과 같은 문제의식 — [[임바디드-AI]]에서 반복되는 "월드모델/CoT를 실제 관측에 어떻게 묶을 것인가". 카메라·추적이라 slam-3dgs 도메인으로 분류하되 [[월드모델]]·VLA와 교차.

## 도메인별 추출 (slam-3dgs / 임바디드 교차)

- **현재 SOTA 관점**: RL 없이 89.4%(단일표적)·단일 전방카메라로 다중카메라 능가 주장 — 트래킹을 "객관식 접지"로 단순화한 게 강점.
- **실시간 가능성**: 온보드 비전·웨이포인트 디코딩 구조라 실시간 지향이나 구체 FPS 미명시(원문 확인 필요).
- **카메라 파이프라인**: 전방 카메라 검출 bbox 인덱싱 → 참조(객관식) → Refer-CoT → 추적 웨이포인트. TVBI 토큰으로 시간축 bbox 히스토리 주입.
- **응용 가능성**: "자연어로 대상 지정 후 추적"은 로봇·드론 팔로우캠뿐 아니라, [[down-analysis]] 같은 영상 이해에서 "지시된 객체를 프레임 간 추적"으로 응용 여지.
- **필수 레퍼런스**: [[BadWAM]](행동 접지), VLA 정책 일반.

> [!warning] 미래형 ID·원문 미검증
> 초록은 WebFetch 실확인(2단계 접지·89.4%·sim2real). 단 2607.20061 미래형 ID·원문·재현 미검증으로 medium. 89.4%의 벤치 조건(데이터셋·난이도)·실시간성은 원문 확인 대상.

## 관련 페이지
- [[BadWAM]]
- [[임바디드-AI]]
- [[월드모델]]
- [[slam-3dgs]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.20061
- HF Daily Papers: ↑47
- 핵심: 참조(bbox 객관식) → Refer-CoT → 추적 웨이포인트, TVBI 토큰, RL 없이 89.4% 단일표적, 4족·휴머노이드 sim2real
- 신뢰도: ⭐⭐ (초록 WebFetch 실확인, 미래형 ID·원문·재현 미검증 medium)
