---
title: "ConceptCountry/qwen-concept-27b — 학습 없이 down-proj 9개 재작성으로 사고 토큰 −27~54% (랜덤 편집 대조군 포함)"
type: source
domain: local-llm
tags: [local-llm, weight-editing, qwen, reasoning, gguf, control-experiment]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/ConceptCountry/qwen-concept-27b]
reliability: medium
---

**모델**: [ConceptCountry/qwen-concept-27b](https://huggingface.co/ConceptCountry/qwen-concept-27b) · 다운로드 63,964 · 좋아요 276 · apache-2.0 · base [[Qwen3.8-27B]] · 생성 2026-11-08 · 논문은 자사 사이트(concept.country/research/weight-space-programming) — arXiv 아님.

## 핵심 인사이트
> [!insight] 기여는 편집이 아니라 대조군 (README 20행 · 볼트 확인)
> *"The contribution is the control, not the edit."* 경사 하강 · 학습 데이터 없이 모델 자신의 활성값에서 편집 방향을 도출해 **down-projection 9개 행렬 재작성**('weight-space programming'). 같은 층 · 같은 크기의 **노름 맞춤 랜덤 편집은 모든 벤치에서 CI 가 0 을 걸침** — "방향이 의미 있다"를 "아무 섭동이나 도움된다"와 분리. 볼트가 반복 요구해 온 [[측정도구-먼저-반증]] · 음성 대조군이 카드 안에 있다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 사전 등록 기준 **GPQA Diamond +4.3 [95% CI +1.8, +7.1]** · **LiveCodeBench v6 +13.0** · 사고 토큰 **27–54% 감소**(17–18행 · 볼트 확인). 형식 bf16 ~52GB · FP8 ~30GB · NVFP4A16 ~20GB · **GGUF Q8_0 ~27GB(벤치가 실제 돈 파일)** · Q4_K_M ~16GB.
- **트레이드오프**: 사고 토큰 감소 = 로컬 추론 지연 · 비용 직접 감소. 단 상태 "실험적 · 평가 중".
- **Hermes 적용**: Qwen3.8-27B 를 로컬에서 쓰는 경우 Q8_0 로 A/B 해볼 가치. Q4_K_M 은 효과 미보장.
- **오픈소스 구현체**: 가중치 공개 · 편집 도구 공개 여부 미확인.

> [!warning] 측정은 Q8_0, 4비트는 미측정 · LCB 에 CI 없음
> 카드 40행 *"…claims a 4-bit conversion preserves the effect — that needs its own evaluation"* 의 부정형(볼트 확인: 주장하지 않는다). LiveCodeBench +13.0 에는 CI 미표기(수집기) — GPQA 만 CI. 같은 배치 축(측정된 것 ≠ 쓰이는 것)의 정직한 쪽 사례.

## 관련 페이지
- [[Qwen3.8-27B]] · [[Qwen]] · [[측정도구-먼저-반증]] · [[gemma-4-31B-it-ARA-heretic-GGUF]](같은 "원본 측정 · 양자화 배포" 구조) · [[heretic]](같은 가중치 편집 계열 · 목적 다름) · [[local-llm]]

## 원본
- 출처: https://huggingface.co/ConceptCountry/qwen-concept-27b
- 확인 범위: HF models API 메타 · README 17–20 · 40행(볼트) · 🔴 형식별 크기 · 상태 표기는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (사전 등록 · 랜덤 대조군 · CI)
