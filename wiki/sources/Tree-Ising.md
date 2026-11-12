---
title: "Tree-Ising — LLM 가중치 '수리'를 BF16 비트 단위 Ising/QUBO 최적화로 (arXiv 2611.14210)"
type: source
domain: local-llm
tags: [local-llm, weight-editing, qubo, ising, model-repair, small-model]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/papers/2611.14210]
reliability: medium
---

**논문**: [arXiv 2611.14210](https://huggingface.co/papers/2611.14210) *Tree-Ising: Repairing Language Models with Bit-Level Ising Edits* · 업보트 **83** · 저자 2명 · 코드 github.com/TheQuantumGOAT/Tree-Ising ★5(수집기) (HF papers API 볼트 실측 — 초록 전문 대조, 수치 전건 일치)

## 핵심 인사이트
> [!insight] 에이전트가 158턴·8,970만 토큰으로 한 일을, 최적화기가 forward 4회·LLM 토큰 0·약 $0.90 로 더 잘 했다
> 비교 대상은 MIT(Takehi 외)의 "weight-space programming" — GPT-6 Astra 에이전트가 Qwen3.5-0.8B 의 **추론 루프**(같은 말 반복)를 가중치를 직접 읽고 고쳐 수리했다(158턴 · 89.7M 토큰 · forward 요청 50회). Tree-Ising 은 같은 수리를 **BF16 가중치의 부호 반전·지수 이동만 허용**하는 희소 이산 최적화로 바꾸고, 목적함수를 **출력 행별 독립 QUBO 로 정확히 분해**해 GPU 시뮬레이티드 어닐링/분기로 푼다.
> - 같은 두 층·같은 평가 프로토콜: MATH-500 **54.6%** vs 에이전트 편집 **51.7%** (분기 솔버 55.1%, 통계적으로 구분 불가)
> - 수학 벤치 5종 전부 에이전트 편집 상회 — **다중비교 보정 후 유의한 것은 MATH-500 · GSM8K 2개**
> - 수정 가중치 13~17% 적고 비트 플립 2.2~2.3배 적음 · forward 4회 · LLM 토큰 0 · 어닐링 약 $0.90
> - Qwen3.5-2B: greedy GSM8K **21.6% → 69.4%**(층·강도는 베이스 모델만으로 선택)
> ⇒ **"에이전트가 할 수 있다"와 "에이전트가 해야 한다"는 다르다** — 목적이 수식으로 쓰이면 고전적 최적화가 더 싸고 더 정확하다.

> [!warning] 한정어 보존
> - 원본 7.9% 는 **"as reported"** — 저자 재측정이 아니라 인용값이다(초록 원문). [[자기제한-명시]]
> - 대상은 0.8B/2B 소형 모델의 **추론 루프 수리**에 한정, 평가는 수학 벤치뿐.
> - 양자(IBM Heron QAOA)는 **8변수 부분문제 개념 증명**이다 — 제목·업보트가 "양자"로 읽히지 않게 주의.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 0.8B/2B 에서 수학 정확도를 크게 올린 "무학습 수리"는 온디바이스 소형 모델 운영자에게 직접 관련. 단 루프형 실패에만 검증됐다.
- **메모리 아키텍처**: 해당 없음(가중치 편집).
- **Hermes 적용**: 즉시 NO — 코드 ★5, 재현 정보 미확인.
- **트레이드오프**: 편집량 ↓ · 비용 ↓ · 정확도 ↑(MATH-500 +2.9%p vs 에이전트). 일반 능력 보존 여부는 초록에 없음.
- **오픈소스 구현체**: TheQuantumGOAT/Tree-Ising(★5).

## 관련 페이지
- [[Qwen]] · [[국소-수리-원리]] · [[자기제한-명시]] · [[리서치-2026년-온디바이스-AI엣지-추론모델-경량화-최신-동향]](같은 날 크론 노트 — 출처 0건, 이쪽이 측정치)

## 원본
- 출처: https://huggingface.co/papers/2611.14210
- 확인 범위: HF papers API 초록 전문 · 🔴 본문·코드 미열람
- 신뢰도: ⭐⭐ (업보트 83 · 코드 ★5)
