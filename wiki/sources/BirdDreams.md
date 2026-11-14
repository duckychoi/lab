---
title: "BirdDreams — 카메라 영상과 BEV 영상을 함께 생성하는 주행 월드모델 (arXiv 2611.14815)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, world-model, driving, bev, video-diffusion, camera]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.14815]
reliability: medium
---

**논문**: [arXiv 2611.14815](https://huggingface.co/papers/2611.14815) *BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model* · 업보트 **49**(수집기: 36) · 저자 6명(Junyoung Seo · Jaewoo Seo · Seungryong Kim · Laura Leal-Taixé … Seung Wook Kim) · 발행 2026-11-10 · 코드 링크 없음 (HF papers API 볼트 실측). 수집기 `ai-news` → 볼트 재분류 `slam-3dgs`(카메라 · 주행).

## 핵심 인사이트
> [!insight] 레이아웃을 "입력"에서 "예측 대상"으로 옮겼다
> 기존 주행 월드모델은 주변 차량의 미래 궤적을 레이아웃으로 **입력받아** 영상을 만든다 — 제어는 되지만 미래를 이미 알아야 한다. BirdDreams 는 카메라 영상과 도식형 BEV(조감도) 영상을 **두 개의 비디오 DiT 가 공동 어텐션으로 함께 생성**해, 장면 레이아웃을 예측되는 미래의 일부로 만든다.
> - BEV: 도로와 차량을 고정 미터 스케일의 단순 도형으로 — 가림이 적고 위치·운동이 분명.
> - 카메라 영상: BEV 가 버리는 신호등 · 외형을 유지.
> - **ego 제어의 기하 인터페이스**: 예측된 BEV 의 최신 프레임을 입력 ego 궤적대로 이동·회전시켜 "ego 만 움직였다면 장면이 어떻게 보일지"를 소프트 조건으로 준다.
> - 추론 입력은 **단일 카메라 이미지** — HD 맵 · 차량 상태 불필요.

> [!warning] 정량 수치 0
> PhysicalAI-AV · nuScenes 에서 "기존 주행 월드모델보다 ego 궤적 추종이 충실", 사람 평가에서 "perspective-only 기준선보다 주변 차량 거동이 현실적" — 초록에 수치가 없다. 코드도 없다. BEV 는 학습 시 장면 주석에서 렌더링하므로 주석 데이터가 전제다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 주장만 있고 수치는 본문.
- **실시간 가능성**: 미상(자기회귀 비디오 DiT 2개 — 초록에 속도 언급 없음).
- **카메라 파이프라인**: 입력 단일 전방 카메라 이미지 → 출력 카메라 영상 + BEV 영상. BEV 가 "가림 없는 중간 표현" 역할.
- **응용 가능성**: 기하 표현(BEV)을 영상 생성과 같이 예측시키는 구조는 로봇 실내 주행에도 옮길 수 있는 아이디어.
- **필수 레퍼런스**: 코드 공개 전까지는 초록.

## 관련 페이지
- [[월드모델]] · [[Diffusion-월드모델]] · [[Cosmos-3]] · [[Duo]](같은 날 "월드모델"을 다른 뜻으로 쓴 사례) · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.14815
- 확인 범위: HF papers API 초록 전문 · 저자 · 🔴 본문 미열람 · 코드 없음
- 신뢰도: ⭐⭐ (업보트 49 · 수치·코드 없음)
