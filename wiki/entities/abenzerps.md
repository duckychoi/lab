---
title: "abenzerps — 양자화 재배포자"
type: entity
domain: ai-news
tags: [entity, huggingface, quantization, gguf, comfyui, 원본-파생-역전]
created: 2026-10-02
updated: 2026-10-02
sources: [Qwen-Image-2.1-Uncensored-GGUF.md, Qwen-Image-2.1.md]
reliability: medium
---

# abenzerps

**HF**: https://huggingface.co/abenzerps

> [!insight] 🎯 핵심 — **베이스 제공자보다 많이 다운로드되는 재배포자**
> [[Qwen-Image-2.1-Uncensored-GGUF]] 의 제공자. 📌 **DL 1,303,476 으로 베이스 제공자 [[Qwen]] 의 원본(76,938)을 16.9배 앞선다** → [[원본-파생-역전]] 의 주요 사례.
> 🏆 **볼트가 주목하는 이유는 양자화 품질이 아니라 "동봉" 전략이다** — 가중치만 올리지 않고 **텍스트 인코더(qwen3vl_8b)와 VAE 까지 같은 레포에** 넣어 **ComfyUI 단독 구동**을 가능케 했다. **베이스 레포만으로는 바로 돌지 않는다.** ⇒ **DL 의 상당 부분이 "모델"이 아니라 "작동하는 세트"에 대한 수요로 보인다**(🔴 가설, 미검정).

> [!note] 확인된 것 (볼트 실측)
> - `base_model_relation` = **`quantized`** 로 베이스 관계를 **구조화 선언** → [[파생저장소-식별]] 최강 형태
> - 🎯 **재현 경로를 문자로 고정**: 소스 리비전 `b3179ad3…` · 변환 도구 `stable-diffusion.cpp` 커밋 `1330ceba…` · **SHA256SUMS 제공**. ⚖️ **볼트 수집 이력에서 이 정도로 명시된 파생 제공자는 드물다 — 신뢰도 가산.**
> - 12종 포맷 제공(GGUF·FP8·INT8 ConvRot·NVFP4·MLX 4/6/8bit) · **BF16 14.23GB ~ Q4_0 4.15GB**
> - 카드가 **"내장 안전 검사기·콘텐츠 필터 없음"** 을 명시(무검열 변종). **사실로만 기록한다.**

> [!warning] 🔴 미확인
> - 🔴 **09-22 에 이 레포가 307 리다이렉트로 DL 0 으로 읽혔다** — 당시 개명 이력이 있었고 **개명 전/후 관계 미정리**(actionable 410행)
> - *"Uncensored"* 가 **어떤 조작의 결과인지 카드가 설명하지 않는다**(가중치 변경인지 파이프라인 필터 제거인지 불명)
> - `license_link` **None** — `license_name: qwen-research` 만 선언하고 파일 미동봉 → [[메타데이터-부재-추론]]
> - 다른 보유 레포 · 신원 · 활동 이력 **미조회**

## 관련 페이지
- [[Qwen-Image-2.1-Uncensored-GGUF]] — 주 레포 · [[Qwen]] — 베이스 제공자 · [[Qwen-Image-2.1]]
- [[원본-파생-역전]] · [[파생저장소-식별]] · [[대체필드-대조]] · [[정규명-우선-중복검사]]
