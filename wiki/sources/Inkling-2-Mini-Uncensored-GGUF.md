---
title: "AtomicChat/Inkling-2-Mini-Uncensored-GGUF — Inkling-2-Mini 거부 방향 제거판: rank-1 LoRA 49지점 최소 편집 (MMLU −1.5%p 자인)"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, uncensored, rank-1-lora, refusal-direction, thinking-machines]
created: 2026-11-24
updated: 2026-11-24
sources: [https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF]
reliability: medium
---

**HF**: dl30 329,497(볼트 API 11-24 · 수집기 11-23 129,693 — 트렌딩 급등 구간, 하루 +200k) · 좋아요 690(수집기 547) · 생성 2026-11-20 · 내부 ID `40886ab6…`(수집기 `6b00b0af…` — 🔴 볼트 API 재확인값) · base_model `thinkingmachines/Inkling-2-Mini`

## 핵심 인사이트
> [!insight] 49곳에 rank-1 LoRA 한 줄씩 — 검열 해제를 "재학습"이 아니라 "편집"으로 한다
> [[Inkling]] 원본(26.4B MoE · 활성 3.4B · looped core, 텍스트 + 이미지 입력, Apache-2.0 — [[Inkling-2-Mini-GGUF]] · [[Thinking-Machines-Lab]])의 검열 해제판. 방식: 24개 층의 attention 출력 · routed expert 와 토큰 임베딩, 총 **49곳의 잔차 기록 지점에 rank-1 LoRA** 로 층별 거부 방향(유해 vs 무해 프롬프트 평균 활성 차이, 영 · 러)을 제거 — 12개 looped 층은 3회 반복을 가중치 공유하므로 한 번의 편집이 **48패스에 적용**. [[동결-교정층]] 의 4번째 표본(가중치를 갈아끼우지 않고 얇은 편집층만).

> [!warning] 카드가 스스로 실패 게이트 2개를 밝혔다
> **카드 자체 측정**: 유해 프롬프트 거부 영어 100% → 0 · 러시아어 91% → 0, XSTest 안전 프롬프트 과잉 거부 4.0% → 0, 도구 호출 18/20 → 20/20. 🔴 **실패 게이트 2개(자인)**: MMLU 80.65% → **79.15%(−1.5%p, p=0.006 유의)** · 무해 프롬프트 첫 토큰 KL 0.94(게이트 0.10, 랜덤 편집 0.014) 미달 · 누출 프로브 0.11(게이트 0.001) 미달. 일부 답변은 경고 한 줄 후 답함. 파일: AD-Q4_K 16.53GB(KLD 0.0115 · top-1 95.6%) · IQ3_S 13.34GB · IQ2_M 8.67GB · LoRA 단독 0.04GB(기본 레포의 어떤 GGUF 에도 적용) · mmproj. llama.cpp b12600+(PR #32694 병합 구조) 필요, 구 PR #32695 레이아웃과 혼용 금지.

## 도메인별 추출 (local-llm)
- **[[원본-파생-역전]] 3번째**: 볼트 API 11-24 기준 원본 `thinkingmachines/Inkling-2-Mini` dl 41,888(수집기 11-23 23,543 — 급등 구간) · 좋아요 5,590 vs 파생 GGUF dl 329,497 · 좋아요 690 — **다운로드는 파생 7.9배, 좋아요는 원본 8.1배**. 11-22 관찰(다운로드는 파생 30배 · 좋아요는 원본) 재현.
- **품질 대가의 정량화**: 검열 해제판의 지능 손실을 카드가 p값까지 공개한 것은 드물다 — 파생 모델 카드에서 "무엇을 잃었는가"의 기록 표본([[자기제한-명시]] 방향).
- **활용 조건**: Apache-2.0 원본의 파생이지만 무해 프롬프트 KL · 누출 프로브 게이트 미달이 카드에 명시 — 프로덕션 조건은 스스로 판단해야 한다. 볼트 활용은 "검열 해제 편집 기법 기록"이 목적이며 모델 채택 의도는 없음.
- **액션**: 없음(관찰).

## 관련 페이지
- [[Inkling]] · [[Inkling-2-Mini-GGUF]] · [[Thinking-Machines-Lab]] · [[원본-파생-역전]] · [[동결-교정층]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF
- 확인 범위: HF models API(파생 + 원본 — 볼트 11-24: dl · 좋아요 · 생성일 · 내부 SHA) · 카드 수치는 수집기 11-23 판독(볼트 문자열 검증 미실시) · 실행 0
- 신뢰도: ⭐⭐⭐
