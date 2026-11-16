---
title: "Envisioning Agentic Robotics — Embodied System 2(파운데이션 모델 + 체화 하네스) 로드맵 (포지션 논문)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, agent-harness, position-paper, embodied, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.18359]
reliability: low
---

**논문**: arXiv 2611.18359 · HF Daily 11-16 2위 · 업보트 **58**(볼트 · 수집기 56) · 코드 없음 · 프로젝트 grid-robotics-official.github.io/agentic-robotics-roadmap. **실험 결과가 아닌 포지션/로드맵 논문.**

## 핵심 인사이트
> [!insight] 로봇 쪽에도 [[하네스-설계-축]] 이 넘어왔다
> 과제군마다 전용 정책을 학습하는 대신 파운데이션 모델 + **체화 하네스**가 관찰 → 의도 해석 → 추론 → 스킬 · 도구 호출 → 결과 검증 → 전략 수정 폐루프로 개방형 과제를 푼다. 의사결정 핵심을 **Embodied System 2** 로 규정. 핵심 난제: 반응 시간 · 기계 한계 · 환경 변화 · **되돌릴 수 없는 결과** 아래에서 일반 추론을 검증 가능한 행동으로 옮기기. 모델 능력과 폐루프 시스템 성능을 함께 재는 평가 틀, "프리미티브 수행 → 상시 역할 수행" 지속 자율성 로드맵 제시.

> [!warning] 근거 없는 첫 문장
> 초록 첫 문장 *"The release of GPT-6 Astra marks the emergence of a new paradigm … Within weeks, frontier models with agentic harnesses matched or exceeded task-specific policies on many embodied benchmarks"* — 초록에 수치 · 인용 0(볼트 원문 확인). 패러다임 선언의 근거가 특정 상용 모델 출시라는 점 → [[RSI-프레이밍]] 류 서사 주의.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 해당 없음(정의 · 로드맵).
- **응용 가능성**: 같은 날 1위 [[Gamer]](데이터 · 학습 노선)와 정반대 — 학습 대신 하네스. 두 노선의 비교 기준을 볼트가 잡는 데 유용.
- **필수 레퍼런스**: 평가 틀 부분만. [[Criteria-Exposure]] 가 지적한 "검증기 과적합"을 이 평가 틀이 어떻게 다루는지는 본문 미확인.

## 관련 페이지
- [[하네스-설계-축]] · [[임바디드-AI]] · [[VLA]] · [[Gamer]] · [[Criteria-Exposure]] · [[RSI-프레이밍]] · [[System-One-모델]]

## 원본
- 출처: https://huggingface.co/papers/2611.18359
- 확인 범위: HF papers API 초록 전문(볼트) · 🔴 본문 미열람
- 신뢰도: ⭐ low (포지션 논문 · 수치 0)
