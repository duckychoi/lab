---
title: MaP-WAM (Memory as Plans) — 장기기억 로봇 조작 정책
type: source
domain: ai-news
tags: [ai-news, hf-daily-paper, robotics, agent-memory, manipulation, planning]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [arXiv:2609.11561]
---

# MaP-WAM — Memory as Plans: World-Action Modeling with Memory-Grounded Planning

**HF**: https://huggingface.co/papers/2609.11561 · **arXiv**: 2609.11561
**지표(2026-09-13 API 실호출)**: 업보트 **35** · 저자 **8인** · **발행 2026-09-10**
**드리프트**: 업보트·저자 수 **완전 일치**. 🔴 **발행일 정정** — raw는 *"09-11 발행분"* 이라 적었으나 API `publishedAt` 은 **2026-09-10**이다(09-11은 데일리 **게재일**).

> [!insight] 핵심 인사이트 — **기억을 "되돌아볼 기록"이 아니라 "다음 계획"으로 바꾼다**
> 초록의 문제 설정이 정확하다: 로봇 정책은 보통 마르코프 가정을 쓰는데 *"many complex real-world manipulation tasks are inherently **non-Markovian**"* 이다. 기존 해법(언어 요약 / 커지는 시각 윈도 / 혼합)은 **미세한 시각 증거를 잃거나, 히스토리 범위와 실행 효율이 상충**한다.
> MaP-WAM의 선택: 히스토리를 **실행기에 계속 물리지 않는다.** 완료된 구간을 *"언어 지시 + **희소** 시각 맥락"* 기록으로 압축하고, 그것을 **계획 시점에만** 증거로 쓴다. 계획은 *"다음 구간의 언어 계획 + 대응 시각 가이드"* 라는 **압축된 형태**로 나온다.
> 🎯 **핵심 효과는 성공률이 아니라 상수성이다** — *"keeps the executor context length **fixed**"*. 그래서 *"maintaining approximately **constant** executor inference latency as task history grows."* **긴 작업에서 느려지지 않는다.** 이게 이 논문이 파는 것이다.

> [!note] WAP 모델 — 구간 전환을 스스로 보정한다
> World-Action-Progress 모델이 **행동 청크와 실행 진행도를 동시 예측**하고, 예측된 진행도를 *plan-observation alignment* 로 보정해 **적응적 구간 전환**과 폐루프 맥락 갱신을 수행한다. 각 계획의 실행 길이가 **미리 정해지지 않는다**(*over an unknown duration*)는 점이 설계의 요점 — 고정 길이 세그먼트가 아니다.
> 구조화된 어텐션으로 **계획·실행 양쪽에서 KV 캐싱**이 가능하다.

> [!warning] 두 수치를 반드시 같이 적는다
> - **RMBench 성공률 83.3%**(SOTA 주장)
> - **실로봇 78.0%**
>
> **격차 5.3%p.** 그리고 SOTA 주장의 범위는 원문상 *"state-of-the-art performance **on RMBench**"* 로 **한정**된다. 실로봇 78.0%에 대한 비교군은 초록에 없다.

## 도메인별 추출 (ai-news + 에이전트 메모리)

- **신뢰도**: 업보트 35(미인제스트 중 최상위) · 저자 8인 · 수치 2개 명시 → **high**
- **즉시 활용**: 로봇은 아니지만 **구조는 이식 가능하다.** 볼트의 [[에이전트-메모리-레이어]] 문제와 동형: *"전체 히스토리를 매번 물리지 않고, 완료분은 압축해 계획 시점에만 쓴다"*.
- **메모리 아키텍처**: RAG도 KV도 외부DB도 아니다 — **"완료 구간 기록 → 다음 계획" 변환**이다. 검색이 아니라 **요약 후 재계획**.
- **트레이드오프**: 압축하므로 미세 증거 손실 위험이 있고, 논문은 *희소 시각 맥락*으로 그걸 완화한다고 주장한다. 손실량 자체는 초록에 없다.
- **6개월 영향력**: 긴 에이전트 작업에서 **지연이 히스토리 길이와 무관해지는** 설계는 볼트 인제스트 루프에도 직접 해당한다.

> [!question] 미해결
> *"희소 시각 맥락"* 의 희소도(몇 프레임/무슨 기준)가 초록에 없다. 압축률과 성공률의 트레이드오프 곡선이 본문에 있는지 확인 필요.

## 관련 페이지
- [[에이전트-메모리-레이어]] — 같은 문제의 텍스트 도메인 판본
- [[임바디드-AI]] · [[월드모델]] · [[국소-수리-원리]]
- [[World-in-World]] — 같은 배치. **양쪽 다 "추가 학습 없이 맥락을 어떻게 넣을까"를 다룬다**

## 원본
- 출처: https://huggingface.co/papers/2609.11561
- 신뢰도: ⭐⭐⭐ (HF API 실호출 + 초록 원문 전문 대조)
