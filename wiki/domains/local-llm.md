---
title: Local/Edge/Small LLM + 에이전트 메모리 누적 인사이트
type: domain
domain: local-llm
tags: [local-llm, edge-ai, slm, agent-memory, on-device]
created: 2026-04-09
updated: 2026-08-27
sources: [VoiceMem.md, Qwen3.8-27B-Uncensored-Aggressive-MTP-GGUF.md]
---

# Local/Edge LLM + 에이전트 메모리 누적 인사이트

목표: 경량 모델 실배포 + Hermes/에이전트에 메모리 심기

---

## 실용 배포 가능 모델 목록
_소스 ingest 시 자동 누적_

### Qwen3.8-27B 계열 — 실행 환경별 3분화 (2026-08-27 실측)
같은 베이스에서 갈라진 파생들이 **용도별로 분화**했고, 다운로드 규모가 그 수요 지도를 보여준다.

- **[[Qwen3.8-27B-GGUF]]** (로컬 실행·imatrix 양자화) — DL **7,638,591** · 좋아요 3,022 · **저변 1위**
- **[[Qwen3.8-27B]]** (원본 가중치·image-text-to-text) — DL **3,298,569** · 좋아요 **12,953**(볼트 최다·"인정" 신호는 원본에 집중)
- **[[Qwen3.8-27B-FP8]]** (서버 GPU 메모리 절감) — 별도 축
- **가드레일 제거 축** — [[Qwen3.8-27B-Uncensored-Aggressive-MTP-GGUF]] DL **911,795**(현 선두) · [[Qwen3.8-27B-OBLITERATED]] **468,746** · [[Qwen3.8-27B-Uncensored-GGUF]]

**구조**: 양자화 ≫ 원본 ≫ 가드레일 제거. 원본/GGUF 비율이 **0.402 → 0.432**로 2회 연속 상승해 격차는 축소 중.
> [!warning] 가드레일 제거 축은 전량 low
> 이 축 세 모델 모두 **제거 방식·능력 손실 벤치·명칭("Aggressive"·"MTP") 의미가 전량 미검증**이다. DL 91만은 수요의 크기이지 품질·안전성의 근거가 아니다. **실배포 후보가 아니라 생태계 관측 대상**으로만 추적한다.
> ⚠️ **HF 다운로드 수치는 격일 갱신**(4회 연속 확인) — 증분은 최소 2일 단위로 해석하고 좋아요 축을 교차 확인한다.

## 에이전트 메모리 아키텍처 패턴

### 이원 분리형 — VoiceMem (2026-08-27 추가)
[[VoiceMem]](HF 데일리 2위·업82)이 제시한 **정보(좌뇌) ∥ 감정(우뇌) 병렬 분리 + 스트리밍 I/O**.
- **핵심 수치**: **top-5 검색으로 Mem0의 top-200보다 약 30점 우위** — 후보를 **40배 적게** 가져오면서 더 정확
- **지연**: 검색 **134ms**로 표준 VAD 지연 안쪽 → **대화 지연 추가 없음**
- **페르소나**: 단·장기 정서 귀인 + 이중 노드 모델링, 벤치 3종 SOTA·종합 **+4.29점**
- **배포**: 메모리 백엔드 **교체형 분리 배포**

**설계 교훈**: 검색량을 늘리는 방향이 아니라 **무엇을 색인하고 어떻게 경로를 나눌 것인가**가 정확도를 만든다. [[MemTrapBench]](메모리 5종이 no-memory보다 못함)와 함께 읽으면 정식화는 이것 — **성패는 메모리 도입 여부가 아니라 경로 분리 방식에 달렸다.**
⚠️ 절대 점수·벤치 3종 이름·134ms 측정 조건 미기재. 코드 ★28로 재현 보고 부재.

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
