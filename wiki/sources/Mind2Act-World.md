---
title: "Mind2Act World — 로봇 조작을 판단(Mind) · 실행(Act) · 합성(Mind2Act)으로 나눈 진단 벤치 (최강 에이전트 52.7 · 39.0 → 합성 12.0%)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, benchmark, robot-manipulation, vla, embodied, simulation]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.26444]
reliability: medium
---

**논문**: arXiv 2611.26444 · 업보트 51(볼트 11-22 · 수집기 47) · HF 조직 `Mind2Act-World` · 저자 43 · 코드 [Mind2Act/Mind2Act_World](https://github.com/Mind2Act/Mind2Act_World) ★32

## 핵심 인사이트
> [!insight] 단일 능력 점수의 곱보다도 합성 점수가 낮다
> 5개 도메인 시뮬레이션 조작 과제 30개 × 난이도 3 × 장면 2(Clean/Random) = 180 구성. 과제를 Mind(과거 관측 기반 판단) · Act(정밀 · 적시 실행) · Mind2Act(행동 결과가 다음 판단을 이끄는 폐루프)로 나눠 실패 원인을 귀속. **최강 에이전트도 Mind 52.7% · Act 39.0% 인데 Mind2Act 는 12.0%**(볼트 초록 대조 일치). 두 능력이 독립이라고 가정한 곱(약 20.6%, 볼트 산술)보다도 낮다 → 합성 자체가 별도의 병목이다.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 멀티모달 에이전트 · [[VLA]] · WAM 평가. 최강 에이전트는 과제 상태는 유지하나 지속 접촉에 약하고, end-to-end 정책은 반대.
- **실시간 가능성**: 해당 없음(벤치).
- **응용 가능성**: 로봇 정책을 고를 때 "판단형 과제 / 접촉형 과제 / 폐루프 과제" 중 어디에서 실패하는지 분리해 보는 틀. [[Game2Player]] 의 상태 기반 성공 판정과 같은 "실패를 귀속 가능하게" 계열.
- **필수 레퍼런스**: 본 논문 + 코드.

> [!warning] 단서
> 시뮬레이션 전용(실기 평가 언급 없음). 어떤 모델이 "최강 에이전트"인지는 초록에 없다.

## 관련 페이지
- [[VLA]] · [[임바디드-AI]] · [[Game2Player]] · [[Gamer]] · [[복합지표-분해]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.26444
- 확인 범위: HF papers API(초록 전문 · 업보트 · 조직 · githubRepo · 저자 수) · 🔴 본문 표 미열람 · 20.6% 는 볼트 산술(독립 가정)
- 신뢰도: ⭐⭐⭐
