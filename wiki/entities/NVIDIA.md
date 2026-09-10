---
title: NVIDIA
type: entity
domain: local-llm
tags: [ai-news, nvidia, quantization, nvfp4, hardware, inference, entity]
created: 2026-07-04
updated: 2026-09-10
sources: [Qwen3.6-27B-NVFP4.md, LocateAnything-3B.md]
reliability: high
---

# NVIDIA

> [!insight] 핵심
> GPU·AI 하드웨어·추론 스택(TensorRT-LLM 등) 공급사. 위키 맥락의 주목점은 두 축 — ①**자사 4비트 포맷 NVFP4로 인기 오픈모델을 직접 재양자화·배포**([[Qwen3.6-27B-NVFP4]]·[[Qwen3.6-35B-A3B-NVFP4]]), GGUF 중심 지형에 벤더 네이티브 포맷을 경쟁 축으로 투입. ②**공식 VLM 배포**([[LocateAnything-3B]] HF DL 1.42M로 급증) — visual grounding("어디에 있는가") 수요를 자사 모델로 흡수. 로컬 추론·비전을 자사 하드웨어에 묶는 전략. 앞서 Newton 물리엔진(로봇 훈련 70x)도 이 회사 협업.


> [!insight] 2026-09-10 — [[Qwen3.8-Flash-Next-NVFP4]]: **4비트가 9개 중 5개에서 FP8을 이겼다**
> Alibaba Qwen3.8-Flash-Next를 자사 Model Optimizer로 **NVFP4** 양자화. **9개 벤치 중 5개 상승** — SciCode 16.3→**18.8**(+2.5) · AA-LCR 71.9→**74.1**(+2.2) · MMMU Pro +1.2 · HLE +0.7 · IFBench +0.5. **하락 4개는 전부 1점 미만**(최대 −0.7).
> → **"4비트는 손해"라는 통념이 이 모델에서는 성립하지 않는다.** 트레이드오프가 정확도에서 **하드웨어 세대**(Blackwell 네이티브)로 옮겨갔다.
> **NVIDIA 노선 일관**: 자사 모델이 아닌 오픈 모델을 **직접 양자화해 배포**(third-party 고지 명시). 앞선 Qwen3.6-27B NVFP4 건과 같은 패턴 — **ModelOpt 툴체인의 레시피 증명**이 실제 산출물이다.
> 🎯 **볼트 규칙 적용 대상**: 카드 표는 **FP8 행 전체를 볼드 처리**해 시각적으로 FP8 우위를 암시하지만 **실제 숫자는 절반 이상 NVFP4가 앞선다** → *"자기규정과 자기측정이 어긋나면 측정을 채택"* → [[파생표기-함정]]
> ⚠️ 날짜 불일치(카드 08/31/2026 vs API createdAt 2026-09-02) · 분산·시드 정보 없음(±1점은 측정 분산 범위일 수 있음) · 라이선스 이중 적용(NVIDIA Open Model + Qwen Community 1.0).

## 관련 페이지
- [[Qwen3.8-Flash-Next-NVFP4]] — NVFP4 4비트, 9개 중 5개 FP8 상회 *(2026-09-10 신규)*
- [[Qwen3.6-27B-NVFP4]] — NVFP4 4비트 양자화 배포판
- [[Qwen3.6-35B-A3B-NVFP4]] — 35B NVFP4 배포판
- [[LocateAnything-3B]] — NVIDIA 공식 visual grounding VLM
- [[Qwen3.6-27B-GGUF]]
- [[local-llm]]
- [[vllm]]

## 원본
- 대표 배포: https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4
- 신뢰도: ⭐⭐⭐⭐⭐ (AI 하드웨어·추론 인프라 표준)
