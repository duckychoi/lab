---
title: "nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB — Gemma-4-E4B 후학습 SLM 의 Q4_K_M (역할 · 지시 준수는 1위, 장문맥 · 도구 호출 8행은 Qwen3.5-4B 에 열세)"
type: source
domain: local-llm
tags: [local-llm, hf-model, slm, gguf, nvidia, tool-use, on-device]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB]
reliability: high
---

**HF**: dl30 195,916 · 누적 196,147(볼트 API 11-22 · 수집기 11-21 183,617) · 좋아요 693 · 생성 2026-10-05 · 내부 ID `6ac32703…` · license `other`(openmdw-1.1) · base_model `nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16`

## 핵심 인사이트
> [!insight] 양자화본의 열을 따로 낸 카드 — 그리고 지는 행을 숨기지 않았다
> google/gemma-4-E4B-it 를 [[NVIDIA]] 가 후학습한 SLM(총 8B · 유효 4B, 컨텍스트 64K). 이 레포는 BF16 원본의 Q4_K_M. 카드 벤치(자체 하네스 NeMo Gym)에 **Q4_K_M 열이 따로 있다** — 대부분의 GGUF 카드가 원본 수치를 그대로 옮기는 것([[배포출처-봉인]])과 대비되는 모범.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 4GB 급 · 로컬 음성/기기 비서 · 멀티턴 도구 사용 용도. OpenMDW-1.1(상업 사용 가능 명시 · 배포 지역 Global, 수집기 판독).
- **트레이드오프 (Q4_K_M 열 · 볼트가 카드 원문에서 13개 값 문자열 검출)**:
  - 이기는 쪽: MultiChallenge **55.60**(Gemma4 39.36 · Qwen3.5-4B 52.23) · RoleBench 71.21 · IHEval 82.40 · RelyToolBench 69.29 · GaRAGe 40.73 등.
  - 🔴 지는 쪽(상대 Qwen3.5-4B): Tau2-Bench 52.32 vs **61.74**(BF16 은 55.10 vs 75.06) · RULER 64K 85.76 vs **95.37** · LongBench v2 48.67 vs **58.28** · LongMemEval 69.92 vs **76.60** · BFCL-v3 67.31 vs **70.56** · ToolSandbox 74.13 vs 74.51 · IFBench 64.00 vs 66.67 · SysBench 67.22 vs 67.90. EQ-Bench v3 · When2Call 은 Gemma4 우세.
- **Hermes 적용**: 역할 유지 · 지시 준수 · 근거성이 강점이라 페르소나형 봇에 맞고, **장문맥 메모리(LongMemEval) · 함수 호출(BFCL · Tau2)이 핵심이면 Qwen3.5-4B 가 낫다**는 것을 카드 스스로 보여 준다.
- **메모리 아키텍처**: 해당 없음.
- **오픈소스 구현체**: GGUF → llama.cpp 계열.

> [!warning] 단서
> 측정 하네스가 NVIDIA 자체(NeMo Gym)다. 볼트 확인은 값의 **문자열 존재**까지이며 행 · 열 귀속은 수집기 판독이다. `유효 4B` 의 정의(임베딩 제외 등)는 미확인 → [[파라미터-다중표기]].

## 관련 페이지
- [[NVIDIA]] · [[Nemotron-3.5-Transcribe-30B-A4B]] (이름 유사 · 별개) · [[배포출처-봉인]] · [[파라미터-다중표기]] · [[SteerDistill]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
- 확인 범위: HF models API · 카드 README 원문(59,009B) 수치 13개 문자열 검출 · 🔴 표 열 귀속 미검증 · 실행 0
- 신뢰도: ⭐⭐⭐⭐
