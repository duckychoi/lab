---
title: "AtomicChat DeepSeek-V4.1-Flash-1017 Uncensored GSQ-RCO — ISTA 2bit 양자화본에 거부 방향 제거. JailbreakBench 거부율 85.2% → 0%"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, abliteration, uncensored, deepseek, ista-daslab, strata, quantization, 파생저장소]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/AtomicChat/DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF, DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF.md]
reliability: low
---

**HF**: [AtomicChat/DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF](https://huggingface.co/AtomicChat/DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF) · 다운로드 **108,162(30일 = 누적)**(볼트 11-07 · 수집기 11-06 92,333 → +15,829/1일) · ♥359 · trendingScore 266 · MIT · base `ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF` + `deepseek-ai/DeepSeek-V4.1-Flash-1017` · created 10-28 · sha `4f1d2f73`(lastModified 10-31) · IQ1_M · IQ2_XS · IQ2_XXS 각 4샤드

## 핵심 인사이트
> [!insight] 전문가 384개는 바이트 그대로, dense 텐서 3종만 교체 — "최소 편집 파생"
> 볼트 [[DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF]](ISTA 리비전 `cb02422c900d` — 볼트 카드 grep 1건 확인)의 샤드에서 **잔차에 쓰는 dense 텐서 3종**(`attn_output_b` · `ffn_down_shexp` · `engram_wkv`)만 교체하고 **라우팅 전문가 384개는 원본 바이트 유지**. 교체 텐서에 **거부 방향 1개를 강도 2.0 으로 투영 제거**한 편집 = abliteration([[heretic]] 계열 기법). 763B MoE 를 다시 양자화하지 않고 수 GB 단위 텐서만 바꿔 배포하는 방식이라, **파생 레포가 원본의 신뢰(ISTA 양자화 품질)를 그대로 빌려온다** → [[파생저장소-식별]] · [[원본-파생-역전]].

> [!warning] 표는 "거부가 사라졌다"를 보여준다 — 안전 모델이 아니다 (카드 수치 볼트 grep 전건 검출)
> | 지표 (Strata · `IQ2_XXS` 2.0 bpw · 249 GB) | stock → 편집 |
> |---|---|
> | `JailbreakBench (EN)` | **85.2% → 0.0%** (= 해로운 요청 **거부율**) |
> | `XSTest (safe refused)` | 7.6% → 0.0% |
> | `Thinking high (30)` | 27/30 → 0/30 |
> | `MMLU (500)` | 82.8% (p=0.27 · stock 값 표에 없음) |
> | `KL to stock` | 0.0225 (top-64 하한 추정) |
> | `GPQA-Diamond (198 q)` · `AIME25 (30 q)` | 83.3 → 83.3 · 76.7 → 80.0 (n=30 노이즈 범위라 카드 자인) |
> - 카드 자기신고: *"Not every rung cleared every gate"* · 거부 분류기가 답 앞부분만 읽어 **후반부 소프트 거부를 놓칠 수 있다**.
> - **llama.cpp 미지원(Strata 전용)**. 12 GB GPU + 시스템 메모리 + SSD 스트리밍 Engram(110 GB, 미재배포) 구성을 주장하나 속도·RAM 수치 0건(수집기 grep).

## 도메인별 추출 (local-llm)
- **실용성 판단**: 249 GB(IQ2_XXS) + Strata 런타임 전용 — 개인 장비 실배포 난이도 높음.
- **트레이드오프**: 추론 능력 보존(GPQA 동일) vs 안전 거부 전면 제거. KL 0.0225 는 작지만 하한 추정.
- **Hermes 적용**: NO — 에이전트 운용에 안전 거부 제거 모델을 쓸 이유 없음. 도구 실행 권한이 있는 에이전트에 붙이면 프롬프트 인젝션 방어선이 사라진다.
- **오픈소스 구현체**: 가중치만(MIT). 편집 스크립트·metrics 데이터셋은 볼트 미열람.

## 관련 페이지
- [[DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF]] (원본 양자화) · [[DeepSeek-V4.1-Flash-1017]] · [[ISTA-DASLab]] · [[DeepSeek]]
- [[heretic]] · [[Qwen3.6-40B-Deckard-Heretic]] · [[Huihui-Qwen3.8-27B-abliterated-GGUF]] (abliteration 계열)
- [[파생저장소-식별]] · [[원본-파생-역전]] · [[천장-기준선]]
- 같은 날 모델: [[Qwen3.5-4B-3D-Coder]] · [[LFM3-1.7B]]

## 원본
- 출처: https://huggingface.co/AtomicChat/DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF
- 확인 범위: HF API expand(볼트 11-07) · 카드 raw 109행 grep(표 수치 11개 · `cb02422c` · "Not every rung" 전부 검출) · metrics 데이터셋·Strata 레포 미열람 · 실행 0회
- 신뢰도: ⭐ (안전 제거 파생 · 전용 런타임 · 자기측정)
