---
title: "unsloth/Inkling-2-Mini-GGUF — Thinking Machines 26.4B(활성 3.4B · 루프 실효 5.4B) 멀티모달 모델의 GGUF (dl 원본의 약 30배 · 비환각률은 비교군 중 약함)"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, moe, looped-layers, multimodal, coding-agent, unsloth]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/unsloth/Inkling-2-Mini-GGUF]
reliability: high
---

**HF**: dl 238,152 · 좋아요 712(볼트 API 11-22 · 수집기 일치) · 생성 2026-11-20 · 내부 ID `6b00469c…` · apache-2.0 · base_model `thinkingmachines/Inkling-2-Mini`(dl 7,944 · 좋아요 3,417 · 생성 2026-11-17 · 내부 ID `6afb9f51…`)

## 핵심 인사이트
> [!insight] 좋아요는 원본에, 다운로드는 파생에 — 이틀 만에 약 30배
> 원본은 [[Thinking-Machines-Lab]] 의 텍스트 + 이미지 → 텍스트 모델(Apache-2.0 · 별도 AUP). 24층 디코더 중 가운데 12층을 가중치 공유로 3회 반복(48층 연산), **26.4B · 활성 3.4B · 루프 포함 실효 5.4B**, 컨텍스트 1M → [[파라미터-다중표기]]. [[unsloth]] GGUF 가 dl 238,152 로 원본 7,944 의 **약 30배**(볼트 산술), 좋아요는 반대로 원본 3,417 vs 712 → [[원본-파생-역전]].

## 도메인별 추출 (local-llm)
- **실용성 판단**: 원본 체크포인트 약 20GB(NVFP4/MXFP8) · 32GB 이상 권장. GGUF 는 7.76GB(UD-IQ1_S · top token 일치 89.4%) ~ 22.87GB(UD-Q8_K_XL), **UD-Q4_K_M 16.61GB 에서 일치 97.9%** — 양자화 손실을 "원본과의 다음 토큰 일치율"로 낸 점은 모범(볼트가 GGUF 카드에서 4개 값 검출).
- **트레이드오프 (원본 카드 자체 표 · 볼트 10개 값 문자열 검출)**:
  - 이기는 쪽: SWE-bench Verified(bash only) 79.2% · SWE-Bench Pro v2 Hard 77.9% · BrowseComp 79.0% · MCP Atlas 82.7% · LongBench v2 66.9% · OmniDocBench 92.8%.
  - 🔴 지는 쪽(주로 [[Qwen3.8-27B]] 대비): Terminal Bench v2.1 71.6 vs 73.0 · AutomationBench-AA 41.8 vs 48.2 · GDPVal-AA 1319 vs 1427 · AA-Briefcase 1263 vs 1391 · EnterpriseOps-Gym 42.0 vs 44.2 · MMMU Pro 74.9 vs 76.3 · BVB 68.4 vs 70.7 · ARC-AGI v1 84.5 vs 87.5 · **AA-Omniscience 비환각률 63.4% vs 71.4%(Nemotron 69.5%)**. Terminal Bench v4.0 은 5.6% 로 전 모델 바닥.
- **Hermes 적용**: 🟡 코딩 · 검색 에이전트로는 상위 후보이나, **비환각률이 비교군 중 약하다** — 사실 확인이 중요한 볼트 수집기 · 요약 용도에는 불리한 신호.
- **메모리 아키텍처**: 해당 없음(1M 컨텍스트).
- **오픈소스 구현체**: GGUF → llama.cpp 계열(루프형 구조 지원 버전 요구 여부 미확인).

> [!warning] 단서
> - 벤치는 전부 **원본 기준**이다. GGUF 는 토큰 일치율만 쟀고 벤치를 다시 돌리지 않았다([[배포출처-봉인]] — 다만 일치율이라는 대리 지표가 있다는 점에서 통상의 GGUF 카드보다 낫다).
> - SWE 계열은 [[mini-swe-agent]] 하네스(bash only) 측정 — 하네스가 다른 타 카드 수치와 직접 비교하지 말 것.
> - 볼트 확인은 값의 문자열 존재까지, 행 · 열 귀속은 수집기 판독.

## 관련 페이지
- [[Thinking-Machines-Lab]] · [[Inkling]] (07-18 · 같은 조직의 975B) · [[unsloth]] · [[원본-파생-역전]] · [[파라미터-다중표기]] · [[SenseNova-Loop-9B-GGUF]] (같은 날 · 루프형) · [[mini-swe-agent]] · [[Qwen3.8-27B]] · [[배포출처-봉인]]

## 원본
- 출처: https://huggingface.co/unsloth/Inkling-2-Mini-GGUF · https://huggingface.co/thinkingmachines/Inkling-2-Mini
- 확인 범위: HF models API 2건(dl · 좋아요 · 내부 ID · base_model) · 카드 README 2종 원문 수치 14개 문자열 검출 · 🔴 AUP 본문 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐⭐
