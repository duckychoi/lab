---
title: Local/Edge/Small LLM + 에이전트 메모리 누적 인사이트
type: domain
domain: local-llm
tags: [local-llm, edge-ai, slm, agent-memory, on-device]
created: 2026-04-09
updated: 2026-04-09
sources: []
---

# Local/Edge LLM + 에이전트 메모리 누적 인사이트

목표: 경량 모델 실배포 + Hermes/에이전트에 메모리 심기

---

## 실용 배포 가능 모델 목록
_소스 ingest 시 자동 누적_

## 에이전트 메모리 아키텍처 패턴
_소스 ingest 시 자동 누적_

## Hermes/ChinameBot 직접 적용 가능한 것
_소스 ingest 시 자동 누적_

## 성능·속도·비용 트레이드오프
_소스 ingest 시 자동 누적_

## 당장 쓸 수 있는 오픈소스 구현체
_소스 ingest 시 자동 누적_

## 관련 페이지

## JEPA × 경량화 교차 (2026-07-12)
- [[Flow-JEPA-연구아이디어]]에서 도출: "예측 가능한 건 버린다"는 [[JEPA]] 철학을 2025~2026 LLM 경량화와 접목한 교차 연구 후보.
  - **Latent CoT-JEPA**: 잠재공간 추론 롤아웃으로 CoT 토큰 45~80%↓
  - **Predictive KV Cache** ([[LMCache]]·FlashKDA): 예측가능 KV는 저장 안 하고 복원 → KV 75%↓와 결합
  - **Predictability-Guided Sparse Attention** ([[Linear-Attention-Architectures]]): surprise(예측오차)로 어텐션 예산 배분
  - **State-Space JEPA WM** ([[Mamba4]]/SSM): 롤아웃 horizon 선형화
  - **Ternary/VQ Latent WM** (BitNet): 3진 가중치 온디바이스 월드모델
> [!note] 검증 필요
> 위는 검증 안 된 연구 아이디어(reliability medium) — data2vec·MC-JEPA·REPA 등 선행연구와 중첩 여부 확인 필요.

> [!insight] synthesis (2026-07-12)
> [[JEPA효율화-로컬추론]] — 로컬 추론 4대 효율화 축(어텐션 sparsity·KV 압축·양자화·CoT 압축)이 [[JEPA]]의 "예측 가능한 건 버린다" 철학의 서로 다른 구현임을 통합. 스택하면 온디바이스 [[월드모델]] → [[slam-3dgs]] 엣지 로보틱스로 연결.
