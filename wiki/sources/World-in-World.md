---
title: World in World — 학습 없는 비디오 월드모델 제어 인터페이스
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-daily-paper, world-model, video-generation, training-free, no-results]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: medium
identifiers: [arXiv:2609.11548]
---

# World in World — Explore the World with World Models

**HF**: https://huggingface.co/papers/2609.11548 · **arXiv**: 2609.11548
**지표(2026-09-13 API 실호출)**: 업보트 **28** · 저자 **3인** · **발행 2026-09-10**
**드리프트**: 업보트·저자 수 **완전 일치**. 🔴 발행일 raw *"09-11"* → 실제 **09-10**
**도메인 재판정**: raw `ai-news` → **`slam-3dgs`** 이관. 카메라 제어 재렌더링·기하 렌더링·시점 변화가 주제다.

> [!insight] 핵심 인사이트 — **모델을 건드리지 않고 "읽을 것"의 형식만 바꾼다**
> 문제: 자기회귀 비디오 월드모델로 원본 영상을 **새 시점에서 탐색**하려면 네 가지를 동시에 만족해야 한다 — 기록된 사건과 **동기 유지** · 관측 내용을 **요청된 시점에 배치** · 새로 드러난 영역을 **그럴듯하게 채움** · 재방문 시 **이전에 생성한 외형을 복원**. 기존 해법은 *"task-specific modules or additional training"* 이었다.
> World in World의 선택: **학습을 전혀 하지 않는다**(*training-free inference-time interface*). 대신 이질적인 제어 증거를 **"카메라·시간 라벨이 붙은 깨끗한 시각 상태"** 로 변환해서, **동결된 인과적 비디오 모델의 네이티브 셀프어텐션이 그냥 읽게** 만든다.
> 🎯 **어댑터를 붙이지 않고 입력 형식을 모델의 모국어로 번역한 것이다.** 증거는 4종: 원본 관측 · 목표시점 장면 투영 · 새로 드러난 영역 완성을 유도하는 **기하 렌더링** · 롤링 캐시 **밖에서 검색된 생성 상태**. 각 증거가 **토큰 단위 지원 범위와 자체 가용 스케줄**을 갖는다.

> [!note] 두 부품 — 라우터와 EWA
> - **correspondence router**: *"persistent point identities"* 와 기하를 결합해 토큰 대응을 세우고, 지원되는 쿼리를 **매칭되는 원본 영상 토큰 쪽으로 유도**한다
> - **Evidence-wise attention CFG (EWA)**: 각 보조 채널의 추가 기여도를 **같은 디노이징 forward pass의 어텐션 응답으로** 독립 조절한다 → 채널별 가중치를 **사람이 튜닝하지 않는다**
>
> 같은 동결 백본으로 **카메라 재렌더 · 장기 재방문 · 사람 동작 전이** 셋을 처리한다는 것이 인터페이스 주장의 근거다.

> [!warning] 🔴 **초록이 평가 결과를 보고하지 않는다 — 성능 우위 인용 금지**
> 마지막 문장(원문): *"We **evaluate** World in World on camera-controlled video rerendering under diverse viewpoint changes, **assessing** perceptual quality, temporal consistency, and camera-following accuracy."*
> **무엇을 재는지만 적고 얼마가 나왔는지는 없다.** 비교군도 없다.
> → 이 페이지에서 주장 가능한 것은 **구조와 성질**(training-free · frozen backbone · 한 인터페이스로 3과제)이지 **우위가 아니다.**
> 📌 이 배치는 결손이 **3단계**로 늘어섰다: [[FreeFlow]](수치 있음·대조군 없음) → [[RCWM]](수치 없음) → **World in World(결과 자체를 안 적음)**. 업보트는 각각 32·28·28로 **결손 정도와 무관하다** — 볼트가 반복 확인해 온 명제의 또 한 사례.

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: **판단 불가.** 결과 미보고.
- **실시간 가능성**: 낮다. 디노이징 기반 + 캐시 밖 검색 + 기하 렌더링 전처리가 겹친다. 다만 **학습 비용이 0**이라 실험 반복은 싸다.
- **카메라 파이프라인**: 🎯 여기가 실익이다. **목표시점 투영 + 기하 렌더링을 "증거"로 넣는다** — 즉 기존 3D 파이프라인 산출물을 **비디오 모델 입력으로 재사용**하는 경로를 연다. SLAM/3DGS 결과물의 하류 소비처가 하나 생긴 셈.
- **응용 가능성**: 동결 모델 + 입력 번역이라 **백본 교체가 쉽다.** 더 좋은 비디오 모델이 나오면 그대로 얹는다.
- **필수 레퍼런스**: 비교 대상이 될 *task-specific module / 추가 학습* 계열 확인 필요.

> [!question] 미해결
> ① 실제 점수 ② 어떤 동결 백본을 썼는가 ③ *"retrieved generated states beyond the rolling cache"* 의 검색 비용. **전부 초록 밖.**

## 관련 페이지
- [[RCWM]] — 같은 배치·같은 "월드 모델"이나 **정반대 접근**(명시적 코드 재구성 vs 동결 모델 제어)
- [[MaP-WAM]] — 같은 배치. **둘 다 "추가 학습 없이 맥락을 어떻게 넣을까"** 를 다룬다
- [[월드모델]] · [[Diffusion-월드모델]] · [[AI-영상-생성-2026]]
- [[측정도구-먼저-반증]]

## 원본
- 출처: https://huggingface.co/papers/2609.11548
- 신뢰도: ⭐⭐ (HF API 실호출 + 초록 원문 대조. **결과 미보고로 medium**)
