---
title: "Edge0/Edge0-145B-NVFP4 — Qwen3.8-Flash-Next 의 expert 층을 latent MoE 로 재구성한 145B (활성 10.12B · 24GB VRAM 에서 98.3 tok/s, 단 호스트 RAM 38GiB 동반)"
type: source
domain: local-llm
tags: [local-llm, hf-model, moe, latent-moe, nvfp4, edge-inference, license]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/Edge0/Edge0-145B-NVFP4]
reliability: medium
---

**HF**: dl30 88,713(볼트 API 11-22 · 수집기 11-21 85,400) · 좋아요 700(수집기 605) · 생성 2026-11-11 · 내부 ID `6af3fbab…` · license `other`(edge0-community-model-1.0) · base_model `Qwen/Qwen3.8-Flash-Next`

## 핵심 인사이트
> [!insight] "24GB 에서 145B" 의 실제 청구서는 VRAM 23GiB + RAM 38GiB + 전용 엔진이다
> [[Edge0]] 의 두 번째 공개물. 카드 주장: 재양자화가 아니라 48개 층의 routed expert 를 latent 폭 1792 로 교체한 뒤 4비트 네이티브 후학습([[latent-MoE]]). 145B · 토큰당 활성 10.12B, 층당 512 experts 중 10개, 256K 컨텍스트. **전용 엔진 `edge0-infer`(Strata 확장) 필요** — 일반 llama.cpp/vLLM 으로 바로 못 돌린다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: RTX 5090 D 24GB NVFP4 에서 agent decode **98.3 tok/s** · 16K prefill 3165.7 tok/s — 이때 **VRAM 23.25GiB + 호스트 RAM 38.27GiB**. 같은 16GiB + 20GiB 예산에서 decode 36.8 vs Qwen 18.5 tok/s(2.0배).
- **트레이드오프**: 🔴 가장 나쁜 행 — 12GiB VRAM + 20GiB RAM(Q3_K · SSD 스트리밍)에서 chat 22.4 · agent 23.5 tok/s · prefill 221–222 tok/s. 24GB 카드에 예산 상한을 건 시험이며 카드가 "최소 사양이 아니다"라고 명시.
- **품질**: terminal-bench 2.1 86.5 vs Qwen 83.3 · deepswe 1.1 64.6 vs 58.7 · 나머지는 "level" — 수치는 이미지 차트([[벤치마크-이미지-봉인]]).
- **Hermes 적용**: NO — 전용 엔진 의존 + 아래 라이선스.
- **오픈소스 구현체**: `edge0-infer`(vLLM 은 서드파티 플러그인).

> [!warning] 라이선스 · 측정
> - Edge0 Community Model License 1.0 + Qwen Community License 동시 적용: 개인 · 연구 · 내부 사용 · 산출물 상업 이용 허용, **모델 판매 · 상업 모델 서비스 · 독립 코딩/오피스 어시스턴트 제공은 별도 서면 라이선스**. LICENSE(236행)의 "excluded" 3건(110 · 129 · 205행)은 예외 범위 서술 — 지역 조항 아님(수집기 판독).
> - 속도 · 품질 전부 카드 자체 측정. 볼트는 카드 원문(44,959B)에서 14개 값의 문자열 존재만 확인.
> - 카드 태그는 `quantized`, 본문은 "재양자화가 아니다" → [[파생표기-함정]].

## 관련 페이지
- [[Edge0]] · [[Edge0-35B-A3B-preview]] · [[Qwen3.8-Flash-Next]] · [[latent-MoE]] · [[파라미터-다중표기]] · [[Tideway]] · [[파생표기-함정]] · [[벤치마크-이미지-봉인]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/Edge0/Edge0-145B-NVFP4
- 확인 범위: HF models API · 카드 README 원문 수치 14개 문자열 검출 · 🔴 LICENSE 본문 · 이미지 차트 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐
