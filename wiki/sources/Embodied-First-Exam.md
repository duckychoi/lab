---
title: "Embodied First Exam — 코딩 에이전트가 제어 방식을 스스로 골라 로봇 47종을 다루는 평가 (arXiv 2611.12177)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, coding-agent, benchmark, embodied-ai, simulation]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/papers/2611.12177]
reliability: medium
---

**논문**: [arXiv 2611.12177](https://huggingface.co/papers/2611.12177) *Embodied First Exam* · 업보트 **26** · 저자 **30명** · 코드 github.com/mll-lab-nu/embodied-first-exam ★263(수집기) (HF papers API 볼트 실측 — 초록 수치 일치)

## 핵심 인사이트
> [!insight] 최강 코딩 에이전트도 "현실처럼" 제약하면 1/3 만 성공한다
> 에이전트가 **직접 제어 · 제어 코드 작성 · 정책 학습** 중 방식을 스스로 고른다. 로봇 **47종 · 35 스위트 · 1,156 과제**(신규 9 스위트: 공간 퍼즐 · 덱스터러스 조작 · 다중 로봇 · 동적 전신 제어 · sim-to-sim 엔지니어링). 설정 3종:
> - **Standard** — 센서 관측만, 기본적으로 **리셋 불가**(현실 모사)
> - **Realtime** — 추론하는 동안에도 환경이 진행
> - **Privileged** — 시뮬레이터 전체 상태 + 무제한 리셋(**근사 상한**)
> 핵심 456 과제에서 8개 에이전트 중 최고 **GPT-6 Astra(Codex) = Standard 34%**. ⇒ "LLM 은 고수준 계획자로 충분하다"는 같은 날 크론 휴머노이드 노트의 결론에 대한 **측정된 반례**. 특히 "리셋 불가"가 핵심 — 시뮬레이터에서 반복 시도로 얻은 성능은 현실 성능의 상한일 뿐이다([[천장-기준선]]).

> [!warning] 시뮬레이션 한정 · 수치 1개
> 전부 시뮬레이션, 실기 검증 없음. 초록 수치는 최고 에이전트 1개의 Standard 값뿐(나머지 7개 · Realtime · Privileged 는 본문). 실패 단계 라벨링 결과도 본문.

## 도메인별 추출 (slam-3dgs · 로봇)
- **현재 SOTA**: 코딩 에이전트 로봇 제어 Standard 34%(GPT-6 Astra · Codex).
- **실시간 가능성**: Realtime 설정이 바로 이 질문을 잰다 — 수치는 본문.
- **카메라 파이프라인**: 센서 관측 입력(종류는 본문).
- **응용 가능성**: 로봇 하네스를 만들 때 "리셋 가능/불가"를 평가 조건으로 분리하는 설계를 그대로 차용 가능.
- **필수 레퍼런스**: YES — 코드 ★263 · 저자 30명.

## 관련 페이지
- [[임바디드-AI]] · [[VLA]] · [[천장-기준선]] · [[OpenSandbox]] · [[리서치-2026년-휴머노이드-로봇-SLAMVLA로컬LLM-기반-제어-최신-동향]]

## 원본
- 출처: https://huggingface.co/papers/2611.12177
- 확인 범위: HF papers API 초록 전문 · 🔴 본문·코드 미열람
- 신뢰도: ⭐⭐ (업보트 26 · 코드 ★263 · 저자 30)
