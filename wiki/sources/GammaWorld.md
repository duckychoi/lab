---
title: Gamma-World — 2인 이상 다중 에이전트 생성적 세계 모델링 (NVIDIA)
type: source
domain: ai-news
tags: [ai-news, world-model, multi-agent, generative, NVIDIA, game-ai, simulation]
created: 2026-05-28
updated: 2026-05-28
sources: []
reliability: high
---

# Gamma-World — Generative Multi-Agent World Modeling Beyond Two Players

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 기존 2인(플레이어-환경) 프레임을 넘어 3인 이상 다중 에이전트 상호작용을 단일 생성 모델로 처리. NVIDIA 연구. 멀티에이전트 시스템이 실세계 사회적 복잡성을 모델링하는 방향. HF 업보트 46.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — HF 업보트 46, NVIDIA 공식 연구, arXiv 2605.28816
- **즉시 활용**: NO — 연구 단계. 게임 AI / 시뮬레이션 연구자 대상
- **6개월 영향력**: [[Foundation-Protocol]](다중 에이전트 협력 조율), [[recursive-multi-agent]], [[SkillsToTalent]]와 함께 멀티에이전트 사회 모델링 방향 심화. 자율 주행 시뮬레이션, 게임 NPC 행동 생성에 적용 가능
- **대체 관계**: 기존 Game-World([[gameworld]], [[WorldMark]])는 2인 구조 중심 — Gamma-World가 N인 확장
- **허와 실**: N명 에이전트 상태 추적 복잡도가 기하급수적으로 증가 — 실용적 에이전트 수 상한선 확인 필요

## 연구 핵심

- **문제**: 기존 세계 모델은 단일 에이전트 또는 2인 구조만 지원
- **방법**: 생성적 프레임워크로 임의의 수의 에이전트 행동과 상호작용을 동시 모델링
- **의의**: 사회적 AI 시뮬레이션, 복잡 게임 환경, 다중 로봇 협력 시나리오에 적용 가능

## 관련 페이지

- [[Foundation-Protocol]] — AI 에이전트 사회 협력 조율 프로토콜
- [[recursive-multi-agent]] — 재귀적 멀티에이전트 시스템
- [[SkillsToTalent]] — 이질적 에이전트 회사 구조 조직화
- [[gameworld]] — 게임 에이전트 평가 벤치마크
- [[WorldMark]] — 인터랙티브 비디오 월드 모델 벤치마크

## 원본

- 출처: https://huggingface.co/papers/2605.28816
- 업보트: 46 (2026-05-28)
- 기관: NVIDIA
- 신뢰도: ⭐⭐⭐⭐
