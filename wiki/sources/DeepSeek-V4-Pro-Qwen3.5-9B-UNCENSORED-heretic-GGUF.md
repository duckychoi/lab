---
title: "mradermacher/…-UNCENSORED-heretic-GGUF — 원본보다 23배 많이 받는 정적 GGUF (평가 수치 0 · 원본 카드도 재측정 0)"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, quantization, uncensored, heretic, 파생저장소]
created: 2026-11-19
updated: 2026-11-19
sources: [https://huggingface.co/mradermacher/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF]
reliability: low
---

**HF**: 다운로드 **800,958**(30일 = 누적 · 생성 11-12) · ♥136(수집기 135) · trendingScore 52.5 · Apache-2.0 · base `xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic` · ID `6af60e24…` (볼트 API 11-19)

## 핵심 인사이트
> [!insight] 파생의 파생이 원본을 압도한다 — 측정은 두 단계 위에서 멈춰 있다
> 볼트 보유 [[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic]](xtools-at, ID `6ae46fa9…`)의 정적 GGUF. 원본 dl 35,450(수집기) 대비 **약 23배**([[원본-파생-역전]]). 그런데 원본 카드조차 벤치는 Jackrong 상위 원본 수치이고 직접 잰 것은 거부 3/100 · KL 0.0422 뿐이었다. 이 레포 카드(5,022B)는 양자화 목록뿐 — **`%` 0건 볼트 재확인.** ⇒ 80만 다운로드가 받는 파일은 **어느 단계에서도 직접 측정되지 않은 물건**이다(11-16 축 "측정된 것 ≠ 쓰이는 것"의 연장).

## 도메인별 추출 (local-llm)
- **실용성**: Q2_K 4.0GB ~ f16 18.5GB 12종 + 비전 mmproj(Q8_0 · f16) — 볼트가 카드에서 양자화 이름 검출. 컨텍스트 262,144(수집기).
- **트레이드오프**: 양자화 손실 미측정 + 검열 제거 손실 KL 1개 + 증류 원본 벤치는 외부 인용.
- **Hermes 적용**: NO(검열 제거판).
- **오픈소스 구현체**: GGUF 공개. imatrix 판은 별도 `-i1-GGUF`.

## 관련 페이지
- [[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic]] · [[heretic]] · [[DeepSeek-V4-Pro]] · [[원본-파생-역전]] · [[파생저장소-식별]] · [[gemma-4-31B-it-ARA-heretic-GGUF]] (같은 구조 · 11-16)

## 원본
- 출처: https://huggingface.co/mradermacher/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF
- 확인 범위: HF API(expand · 내부 ID · base_model) · 카드 raw 5,022B(`%` 0 · 양자화 목록) · 🔴 파일 크기 · 원본 dl 은 수집기 판독
- 신뢰도: ⭐ (dl 80만 · 평가 0 · 검열 제거 파생의 파생)
