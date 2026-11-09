---
title: "From Autonomous Agents to Cognitive Symbionts — \"기계가 혼자 얼마나 하나\" 대신 \"특정 사람을 얼마나 똑똑하게 만드나(AHI)\". 실험 0의 포지션 논문"
type: source
domain: local-llm
tags: [local-llm, agent-memory, hf-paper, position-paper, personal-ai, lifelong-memory, oxford]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/papers/2611.05376]
reliability: low
---

**논문**: [2611.05376](https://huggingface.co/papers/2611.05376) · University of Oxford · 업보트 **119**(볼트 11-09 09:04Z `api/papers` · 수집기 87 → +32) · 코드 없음 · 프로젝트 https://cognitive-symbiont.github.io/

## 핵심 인사이트
> [!insight] 목표 함수를 바꾼다: AGI(기계가 얼마나 똑똑한가) 옆에 AHI(특정 사람이 얼마나 똑똑해지는가)
> 핵심 개념은 **인지 격차** — 사람이 상황에 가져올 수 있었던 것과 작업기억에 담을 수 있는 것의 차이. 이를 메우는 **인지 공생체**: 평생·내장·실시간·프라이빗·저마찰·능동형 동반자. 설계 공간 = 감지 → 보관 → 이해 → 함께 생활 → 대신 실행·함께 생각 → 성장의 "공생 루프" + 개인 런타임·신뢰 계층.

> [!warning] 개념 논문 — 측정·모델·코드 0건
> 볼트 재검출: 초록에 정량 수치 없음(수집기 판독 일치). 위험(시험 중 은밀한 보조 · 모두가 도입해야 하는 사회적 압력)을 패러다임 일부로 다룬다는 점은 초록 원문 그대로.

## 도메인별 추출 (local-llm)
- **메모리 아키텍처**: "수년치 맥락 보관"을 요구 — [[에이전트-메모리-레이어]] 의 목표 사양서로 읽을 수 있음(구현 아님)
- **Hermes 적용**: 설계 체크리스트로만 — ChinameBot 메모리를 "사용자 인지 격차를 메우는가" 로 평가하는 관점
- **오픈소스 구현체**: 없음

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[EvoMemState]](11-08 — 구현 쪽) · [[리서치-LLM-장기기억에이전트-메모리-아키텍처-SOTA-2026-최신-동향]](같은 배치 크론)

## 원본
- 출처: https://huggingface.co/papers/2611.05376
- 확인 범위: HF papers API 초록(볼트 재조회 11-09)
- 신뢰도: ⭐ (개념 논문)
