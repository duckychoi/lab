---
title: ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF — 배치 유일의 제3자 대조 벤치마크 보유 양자화
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, quantization, mixed-precision, gsq, rco, benchmark]
created: 2026-09-06
updated: 2026-09-06
sources: []
reliability: high
---

# ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF

**HF 모델**: https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
**지표(2026-09-06 API 실측)**: 다운로드 **348,389** · 좋아요 **433** · `gated=False` · 생성 2026-08-28 · 최종수정 2026-09-02 · **Apache-2.0** · pipeline **image-text-to-text**
**raw 수집값(09-05)**: DL 206,575 · 좋아요 327 → **DL +141,814(+68.6%)** — ⚠️**배치 내 증가율 1위**
**기법**: GSQ(arXiv 2604.18556) · RCO(arXiv 2605.00649) 기반 **비균일 혼합정밀 양자화**

> [!insight] 핵심 인사이트 — **이 배치에서 유일하게 근거를 카드 안에 넣었다**
> 09-05·09-06 배치의 HF 모델 6건 중 **자체 벤치마크 표를 카드에 실은 것은 이것뿐**이다. 나머지는 전부 *"외부 문서 링크"*([[Qwen3.8-27B-GGUF]]·[[Qwen3.8-Flash-Next-GGUF]]), *"벤더 자체 표"*([[Qwen3.8-27B]]·[[DeepSeek-V4-Flash-Vision-Exp]]), 또는 *"표 없음"*([[MiniMax-H3]])이다.
> 게다가 **제3자 대조**다 — 경쟁 양자화본을 **동일 파일 크기(8.4GB)** 조건에서 직접 비교했다:
> - **AIME25 +10.00** · **GPQA-D +8.59** · **LiveCodeBench +4.57** (vs Unsloth UD-IQ2_S)
>
> [[Repo-To-Skill]]이 세운 기준(*변수 하나만 남기고 나머지를 고정*)을 **모델 카드가 충족한 첫 사례**다. 파일 크기를 고정하고 양자화 기법만 바꿨다.

> [!insight] IQ3_S가 **4.6배 축소에도 BF16과 동률**
> **IQ3_S (3.50bpw · 11.8GB)** 기준:
> - **AIME25 100.00** — BF16과 **동일**
> - **LiveCodeBench v6 85.71** — BF16과 **동일**
> - **GPQA-D 89.39** vs BF16 89.90 — **-0.51만 뒤짐**
>
> 27B를 **11.8GB**로 내리고도 3개 벤치 중 2개가 손실 0이다. [[Minima]]가 NVFP4로 **17.5 GiB**를 보고한 것과 나란히 놓으면, **같은 모델에 대해 두 경로가 각각 11.8GB(GGUF·범용)와 17.5GB(NVFP4·NVIDIA 전용)** 를 제시하는 셈이다.
> ⚠️ 단 **AIME25 100.00은 그 자체로 경계 신호**다 — 만점은 문제 수가 적거나(AIME는 30문항) 포화됐다는 뜻이고, **만점 구간에서는 열화가 보이지 않는다.** *"BF16과 동일"* 은 **이 벤치가 더 이상 변별하지 못한다**는 해석과 구분되지 않는다.

> [!insight] DL **+68.6%/6일** — 배치 최고 증가율
> 좋아요도 327→433(**+32.4%**). 볼트의 기존 규칙 *"좋아요는 누적되고 다운로드는 이동한다"* 에 비춰, **다운로드가 좋아요보다 2배 빠르게 늘고 있다** = 관심이 아니라 **실사용이 유입 중**이라는 신호다.
> 대비: [[Qwen3.8-Flash-Next-GGUF]] +17.3%, [[DeepSeek-V4-Flash-Vision-Exp]] +57.3%.

> [!warning] ⚠️ 유보 사항
> - 벤치 **3종(AIME25·GPQA-D·LCB)** 뿐이다. MMLU-Pro·장문맥·검색은 없다 — **추론 편중 평가.**
> - 대조군이 **Unsloth UD-IQ2_S 하나**다. 다른 기법 대비는 없다.
> - **Apache-2.0**은 확실한 강점(원본 [[Qwen3.8-27B]]와 동일, [[Qwen3.8-Flash-Next-GGUF]]의 `other`와 대비).

## 도메인별 추출 (local-llm)

- **실용성 판단**: **YES — 이 배치 로컬 배포 1순위.** IQ3_S **11.8GB**면 12GB VRAM급에서도 사정권이고, 손실 근거가 카드에 있다. `gated=False`·Apache-2.0으로 마찰 없음.
- **메모리 아키텍처**: 해당 없음(양자화 축).
- **Hermes 적용**: **직접 적용 후보 1순위.** 27B급 추론 성능을 11.8GB로 확보하면 봇 백본 선택이 실질적으로 바뀐다.
- **트레이드오프**: 용량 **4.6배 축소** ↔ 정확도 **GPQA-D만 -0.51**, 나머지 2종 손실 0. **이 배치에서 가장 유리한 거래.**
- **오픈소스 구현체**: 이것 자체. GGUF이므로 llama.cpp 즉시 사용.

> [!question] 미해결 질문
> - **AIME25 100.00의 포화 여부** — 다른 벤치(MMLU-Pro·RULER)에서도 동률인지 확인해야 *"손실 없음"* 이 성립한다.
> - **11.8GB(IQ3_S)의 실제 tok/s** — 용량은 알지만 속도 미확인.
> - **[[Minima]]의 NVFP4 경로와 직접 비교** — 같은 모델, 다른 경로. 대조하면 볼트 최초의 양자화 경로 비교가 된다.

## 관련 페이지
- [[Qwen3.8-27B]] — **원본 모델**(Apache-2.0)
- [[Minima]] — **같은 모델의 NVFP4 W4A4 경로**(원인 분석)
- [[Qwen3.8-27B-GGUF]] · [[Qwen3.8-Flash-Next-GGUF]] — **반박 대상인 Unsloth 계열**
- [[Qwen3.8-27B-FP8]] — 같은 모델 양자화 계열
- [[Repo-To-Skill]] — 변수 고정 대조 설계 기준
- [[검사가능성-공사]] — 근거를 검증 가능한 형태로 두는 축

## 원본
- 출처: https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
- 신뢰도: ⭐⭐⭐⭐ (HF API 2026-09-06 실측 · **카드 내 제3자 대조 벤치마크 표 보유**)
