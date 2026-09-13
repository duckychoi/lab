---
title: FreeFlow — 귀납편향 없는 옵티컬 플로우 트랜스포머
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-daily-paper, optical-flow, transformer, vision, scaling]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [arXiv:2609.11486]
---

# FreeFlow — A Bias-free Hierarchical Transformer for Optical Flow Estimation

**HF**: https://huggingface.co/papers/2609.11486 · **arXiv**: 2609.11486
**지표(2026-09-13 API 실호출)**: 업보트 **32** · 저자 **4인** · **발행 2026-09-10**
**드리프트**: 업보트·저자 수 **완전 일치**. 🔴 발행일 raw *"09-11"* → 실제 **09-10**
**도메인 재판정**: raw는 `ai-news` 로 분류했으나 **`slam-3dgs` 로 이관**한다. 옵티컬 플로우는 볼트 도메인3(카메라·비전 파이프라인)의 핵심 구성요소이며, 09-11/09-12에 적용한 *"주제가 도메인을 정한다"* 기준의 일관 적용이다.

> [!insight] 핵심 인사이트 — **전용 부품을 빼는 것이 주장이다**
> 옵티컬 플로우는 **상관 볼륨(correlation volume) · 특징 워핑 · 반복 정제**라는 전용 부품 3종이 사실상 표준이었다. 초록의 문제 제기: *"such biases **constrain the model to predefined heuristics**, which can limit its expressivity and lead to more complex pipelines and additional computational cost."*
> FreeFlow는 이 셋을 **전부 빼고** 어텐션 3종만 남긴다 — **윈도 어텐션**(국소) + **시프트윈도 어텐션**(윈도 간 교환) + **저해상도 전역 어텐션**. 단일 피드포워드 인코더-디코더다.
> 🎯 그리고 그 대가로 얻은 것이 스케일링이다: *"The resulting architecture **scales naturally with model capacity**, enabling a consistent accuracy gain from small to large variants."* **전용 부품이 있으면 키워도 안 오르는데, 빼니까 오른다** — 이게 진짜 주장이다. 성능 수치는 그 주장의 부산물이다.

## 수치 (초록 원문 실측)

- **Sintel**: **0.68 / 1.48 EPE**(Clean / Final)
- **KITTI-2015**: **3.23 Fl-all**
- **Spring**: **3.192 1px**
- **1080p 추론에서 메모리 효율 유지**(*while remaining memory efficient at 1080p inference*)

> [!warning] 🔴 비교 대상이 초록에 없다
> *"achieves **state-of-the-art** results on major benchmarks"* 라고 하는데 **대조군 모델명이 하나도 없다.** 어떤 SOTA를 넘었는지 초록만으로는 알 수 없다.
> → **"SOTA다"를 인용하지 않는다.** 인용 가능한 것은 **절대 수치 4개**뿐이다. 본문에서 비교표 확인 필요.

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: 자칭 SOTA이나 **대조군 미기재**. Sintel 0.68/1.48은 절대값으로는 최상위권 수준이다.
- **실시간 가능성**: 초록에 **FPS·지연 수치가 없다.** *"memory efficient at 1080p"* 는 메모리 이야기이지 속도 이야기가 아니다. → **실시간 판단 불가.**
- **카메라 파이프라인**: 입력은 프레임 쌍. 반복 정제가 없으므로 **단일 패스**라 지연 특성이 예측 가능할 가능성이 높다(미확인).
- **응용 가능성**: SLAM 프론트엔드의 플로우 추정을 단순 트랜스포머로 대체 가능 → **파이프라인 부품 수 감소**가 실익.
- **필수 레퍼런스**: 반복 정제 계열(RAFT 계보)과의 지연·정확도 비교가 본문에 있어야 실용 판단이 선다.

> [!question] 미해결
> ① 대조군 ② 추론 속도(FPS) ③ 모델 크기별 정확도 곡선의 실제 기울기. **셋 다 초록 밖이다.**

## 관련 페이지
- [[측정도구-먼저-반증]] — "SOTA인데 대조군이 없다" 유형
- [[RCWM]] — 같은 배치. **RCWM은 수치조차 없고, 이쪽은 수치는 있으나 대조군이 없다** (결손의 두 단계)
- [[임바디드-AI]]

## 원본
- 출처: https://huggingface.co/papers/2609.11486
- 신뢰도: ⭐⭐⭐ (HF API 실호출 + 초록 원문 전문 대조)
