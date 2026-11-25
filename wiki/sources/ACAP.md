---
title: "ACAP — 로봇 하나를 비동기 코딩 에이전트 팀으로 굴리는 제어 프레임워크 (arXiv 2611.31205)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, robot-agents, asynchronous, multi-agent, delegation, real-robot, harness]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.31205]
reliability: medium
---

**논문**: arXiv 2611.31205 · 업보트 **49**(수집기 11-25, 1위) → **50**(볼트 API 11-25) · 소속 MMLab@NTU · 저자 6명 · githubRepo 없음 · 본문 https://arxiv.org/html/2611.31205v1

## 핵심 인사이트
> [!insight] 제어 그룹마다 상주 코딩 에이전트를 두고 "하이퍼 에이전트"가 제어권을 이양시킨다
> 팔+그리퍼, 몸통+섀시처럼 **제어 그룹마다 상주 코딩 에이전트**를 두고, 하이퍼 에이전트가 작업 배정 · 물리 의존성 조율 · 제어권 이양을 맡아 독립 작업을 동시에 진행. 실로봇(Galaxea R1 Pro + AgileX PiPER 계열 4대) 25개 과제 72회: **경과시간 19.04 → 13.67분(−28.2%), 진척 AUC 62.3 → 72.9**(표 1). 협업형 8과제에서 **고정 위임(Fixed Delegation)은 26.02분 · AUC 36.3으로 단일 에이전트보다도 나빴고** ACAP 13.75분 · 70.8(표 2) — "에이전트 여러 개를 무조건 병렬"이 아니라 **동적 위임**이 본질. [[하네스-설계-축]] · [[Coding-Agents-TAMP]] 축.

> [!warning] 표준편차 범위 · 반복 안정성 · 백본 미기재
> 반복 실험 6과제×5회 평균 21.43 → 15.14분(표 3). **지는 행**: T09 Grid sorting 15.21 vs Direct 11.37분 · AUC 65.8 vs 73.3, T19 Basket lift 13.01 vs 9.94분 · AUC 73.1 vs 77.9 / 표 3 Lift a milk carton AUC 70.1 < Direct 75.2. 표 4 시간 분해: 추론 중첩으로 −8.17분을 벌지만 **추가 추론 작업이 +4.95분** 생긴다. T21 병따기는 ACAP도 28.76분(30분 상한 근접). 🔴 **백본 LLM 이름은 본문에 없다**(볼트 11-25 본문 전수 검색 — GPT/Claude/Gemini/Qwen/GLM/MiMo/DeepSeek/Kimi/SenseNova 토큰 빈도 확인, 관련 인용 외 0건 — 수집기 "미확인"을 확정 소견으로 승격).

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA 관계**: 다관절 로봇에서 "에이전트 하나가 전부 생각하는" 병목을 줄이는 설계 근거 — 동적 위임이 고정 병렬보다 나음.
- **실시간 가능성**: 불가 — 과제당 수십 분(13–29분), 실시간 제어와는 다른 층(작업 스케줄링)의 기여.
- **한계**: 백본 미기재(재현 불가) · 30분 상한 · 사람 평가 진척도 기준 · githubRepo 없음(코드 미공개).
- **액션**: 없음(관찰).

## 관련 페이지
- [[Coding-Agents-TAMP]] · [[Embo-Harness]] · [[하네스-설계-축]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.31205
- 확인 범위: HF papers API(볼트 11-25 — 업보트 50 · MMLab@NTU · githubRepo 없음 일치) · 본문 표 1–5(수집기 11-25 판독) + **볼트 본문 전수 재검색으로 백본 미기재 확정**(11-25) · 실행 0
- 신뢰도: ⭐⭐ (실로봇 72회 · 코드 미공개 · 백본 미기재)
