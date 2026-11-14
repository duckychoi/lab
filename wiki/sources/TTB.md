---
title: "TTB (Test-time Baking) — 교차 시점 어텐션을 경량 MLP 에 구워 디코더 전용 시점 합성을 최대 23배 가속 (arXiv 2611.17331)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, novel-view-synthesis, lvsm, test-time-training, rendering-speed, nvidia]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.17331]
reliability: medium
---

**논문**: [arXiv 2611.17331](https://huggingface.co/papers/2611.17331) *TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models* · 업보트 **21** · 저자 9명(Chin-Yang Lin · Ryo Hachiuma · Jaesung Choe · Min-Hung Chen … Cheng Sun) · 발행 2026-11-12 · 코드 NVlabs/DVSM ★35 · 프로젝트 test-time-baking.github.io (HF papers API 볼트 실측 — 수집기와 일치). 수집기 `ai-news` → 볼트 재분류 `slam-3dgs`.

## 핵심 인사이트
> [!insight] 어텐션을 "대체"하지 말고 어텐션의 입출력을 "외우게" 하라
> 3D 기하를 재구성하지 않고 신경망으로 새 시점을 회귀하는 디코더 전용 LVSM(KV-cache)은 품질이 SOTA 지만 느리다. TTT(Test-Time Training) 층은 빠르지만 품질을 잃는다. TTB 의 두 열쇠:
> 1. TTT 의 fast-weight MLP 를 어텐션의 **대체물**로 쓰지 않고, **교차 시점 어텐션의 입출력 쌍을 명시적으로 학습**시킨다 → TTT 와 같은 렌더링 효율 · 훨씬 높은 품질.
> 2. **모달리티 불일치 해소** — 컨텍스트 토큰을 "카메라 전용 렌더링 토큰"(TTB 입력)과 "이미지 포함 정답 토큰"(매핑 타깃)으로 분리해, 구운 MLP 가 컨텍스트 ↔ 새 시점 사이의 일반화 부담을 지지 않게 한다.
>
> 결과: *"up to **23x** rendering speedup with quality on par with the state-of-the-art across several benchmarks."*
> ⇒ [[3DGS]] 개념 페이지의 패턴 — **"무거운 계산은 장면당 1회, 결과는 가벼운 표현에 굽는다"** — 이 명시적 3D 표현 없이 신경망 내부에서 재현된 것이다. 가우시안 대신 MLP 가중치가 "구운 장면"이다.

> [!warning] "최대" · 굽는 비용
> 23배는 "up to". 벤치별 PSNR · 절대 FPS · **굽는 데 걸리는 시간**(장면당 테스트 시점 학습 비용)은 초록에 없다. 굽는 비용이 크면 시점 몇 개만 뽑는 용도에서는 이득이 사라진다 → [[배수-조건분산]].

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 품질은 LVSM 급 "on par"(수치 본문).
- **실시간 가능성**: 23배의 기준 FPS 가 없어 30fps 여부는 미상.
- **카메라 파이프라인**: 포즈가 있는 다시점 이미지 → 장면별 MLP 굽기 → 카메라 토큰만으로 새 시점 디코딩.
- **응용 가능성**: 3DGS 를 쓰지 않는 시점 합성 경로의 속도 문턱이 내려간다 — 영상 SaaS 의 카메라 이동 생성에 연결 가능.
- **필수 레퍼런스**: NVlabs/DVSM · 프로젝트 페이지.

## 관련 페이지
- [[3DGS]] · [[NVIDIA]] · [[배수-조건분산]] · [[한정어-탈락]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.17331
- 확인 범위: HF papers API 초록 전문 · 저자 · 🔴 본문 · 코드 미열람
- 신뢰도: ⭐⭐ (업보트 21 · NVlabs 코드)
