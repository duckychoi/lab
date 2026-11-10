---
title: "google-deepmind/mujoco 4.0.0 — 터널링 방지 speculative contact·탄소성 추가, 대신 기존 모델의 시뮬 결과가 달라질 수 있는 메이저 판"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, simulator, github-trending, breaking-change, deepmind]
created: 2026-11-10
updated: 2026-11-10
sources: [https://github.com/google-deepmind/mujoco]
reliability: high
---

**GitHub**: https://github.com/google-deepmind/mujoco · ★**17,112** · fork 2,028 · open issues 322 · Apache-2.0 · C++ · 생성 2021-08-27 · 푸시 2026-11-10T01:29Z (GitHub API 2026-11-10 09:06Z · 수집기 17,108 대비 +4 드리프트) · **4.0.0 릴리스 2026-11-06T15:39Z** · 직전 3.17.0 = 10-22

## 핵심 인사이트
> [!insight] 새 기능보다 "같은 모델이 다른 결과를 낸다"가 먼저 읽어야 할 줄이다
> 4.0 은 ① `speculative` 플래그(빠른 볼록 물체가 한 타임스텝 안에 얇은 장애물을 뚫는 터널링 방지) ② 탄소성(`mjData.plastic` 에 상태 저장) ③ 파이썬 패키지 분리(`mujoco-core`·`mujoco-studio`·`mujoco`)를 넣었다. 동시에 sidesite 텐던 감김 규칙 변경 · RK4 가 ball/free 관절 방향까지 4차 정확도로 바뀜 · `cable` 플러그인과 `composite` 요소 제거가 들어가 **기존 학습 환경의 궤적 재현성이 깨질 수 있다.** 정책을 3.x 에서 학습했다면 4.0 평가 수치는 같은 실험이 아니다.

> [!note] 볼트 대조 범위
> 릴리스 API 본문 앞부분에서 speculative · elasto-plasticity(`mjSTATE_PLASTIC`) 2항과 3.17.0 batch API("bit-identical to a plain loop at any thread count") 를 직접 확인했다. 호환성 깨짐 3항(sidesite · RK4 · cable/composite)과 pip 재설치 안내는 **수집기 판독 기준이며 볼트는 해당 구절을 재검출하지 않았다.** 발표문(discussions/3773)은 수집기·볼트 모두 미열람.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 로봇·강화학습 표준 물리 시뮬레이터. 성능 수치는 릴리스 노트 앞부분에 없음.
- **실시간 가능성**: 3.17.0 batch API 가 스레드풀 병렬 스텝을 제공(결과는 단순 루프와 비트 동일이라고 명시).
- **응용 가능성**: [[VLA]] · [[임바디드-AI]] 정책 학습 환경의 바닥층. 오늘 배치의 [[A2-MEAS]](RoboTwin 2.0 · BEHAVIOR) 같은 시뮬 벤치 수치를 읽을 때 "어느 시뮬 버전인가"가 조건 열이 된다.
- **액션**: 직접 쓰는 환경이 없으면 없음. 쓴다면 업그레이드 전 sidesite · RK4 · cable 사용 여부 점검.

## 관련 페이지
- [[A2-MEAS]] · [[VLA]] · [[임바디드-AI]] · [[월드모델]] · [[Google]]

## 원본
- 출처: https://github.com/google-deepmind/mujoco
- 확인 범위: GitHub API(메타 · releases 2건 본문 앞부분) · 🔴 코드 미실행 · 발표문 미열람
- 신뢰도: ⭐⭐⭐ (★17,112 · Apache-2.0 · 5년 이력)
