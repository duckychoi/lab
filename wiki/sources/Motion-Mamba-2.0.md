---
title: "Motion Mamba 2.0 — 장기 휴머노이드 제어를 위한 자기회귀 확산 Mamba (arXiv 2611.29897)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, humanoid-control, diffusion, mamba, long-horizon, memory, robotics]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.29897]
reliability: medium
---

**논문**: arXiv 2611.29897 · 업보트 **88**(수집기 11-24, 1위) → **189**(볼트 API 11-25 — **이틀 만에 2.1배**) · 소속 Peking University · 저자 8명 · 코드 https://github.com/AIGeeksGroup/MotionMamba2.0 (★3)

## 핵심 인사이트
> [!insight] 먼 과거를 유지하는 열쇠는 컨텍스트가 아니라 "압축된 슬롯" — 지속 콘텐츠 메모리(PCM)
> 텍스트 · 공간 목표가 바뀌는 상황에서 실시간으로 동작을 이어 생성하는 루트-바디 확산 모델. Mamba 순환 상태 + 국소 어텐션 + **PCM(Persistent Content Memory: 압축된 과거 동작 · 상태 변화 · 텍스트 특징을 슬롯으로 만들어 어텐션이 참조)** 으로 먼 과거를 유지. 본체를 새로 설계한 사례 — [[동결-교정층]] 의 **대조군**(메모리 아키텍처로 본체를 바꾸는 방향).

> [!warning] "실시간"은 윈도 단위 300ms 수준 — 경쟁사 대비 4–8배 느리다
> 본문 표 1(HiPHI, 39.52s · 19윈도): 루트 위치 오차 **7.55cm**(전작 Motion Mamba 125.74 · 최강 비교 TACD 54.43), 명령 준수 46.05%. 표 7: CUDA Graph + 커널 융합으로 RTX 4090 윈도 지연 중앙값 1685.35 → **276.14ms**(6.138×, 출력 동일). **지는 행(본문 표)**: 최적화 후에도 윈도당 283.7ms — DartControl 34.7 · PCMDM 58.4 · DiP 73.6ms보다 **4–8배 느림**. BONES Seed 단기 명령 준수 86.92% < DreamControl 96.64 · MoLingo 97.50. HumanML3D 단기 R@3 84.29% < DreamControl 87.98.

## 도메인별 추출 (slam-3dgs)
- **실시간 가능성**: 불가 — 윈도당 ~280ms는 게임 캐릭터 · 로봇 데모 수준. 실제 제어 주파수에는 미달.
- **실기 검증**: 표 8 — Unitree G1 실기에서 동작 조합 18/20 · 키보드 제어 29/30 · 넘어짐 0. 시뮬레이션만이 아닌 점은 가점.
- **필수 레퍼런스**: 장기 명령 준수(46.05%) vs 단기 준수(경쟁사 90%+)의 **긴-짧 트레이드오프** 구조 — 장기 정확도가 필요한 과제와 아닌 과제를 구분할 때 참조.
- **액션**: 없음(관찰 — ★3 연구 코드 단계).

## 관련 페이지
- [[Embo-Harness]] · [[ACAP]] · [[동결-교정층]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.29897
- 확인 범위: HF papers API(볼트 11-25 — 업보트 189 · Peking University · githubRepo 일치) · 본문 표 1 · 7 · 8 및 지는 행(수집기 11-24 판독) · 실행 0
- 신뢰도: ⭐⭐ (실기 검증 있으나 ★3 레포 · 지연 수치 경쟁 대비 불리)
