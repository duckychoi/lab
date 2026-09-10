---
title: "nvidia/Qwen3.8-Flash-Next-NVFP4 — 4비트 양자화가 9개 중 5개에서 FP8을 이겼다"
type: source
domain: local-llm
tags: [local-llm, hf-model, quantization, nvfp4, nvidia, qwen, moe, vision]
created: 2026-09-10
updated: 2026-09-10
sources: []
reliability: high
---

# Qwen3.8-Flash-Next-NVFP4

> [!insight] 핵심 인사이트
> Alibaba Qwen3.8-Flash-Next를 NVIDIA Model Optimizer로 **NVFP4(4비트)** 양자화한 가중치. 원본 구성은 **비전 인코더 + 하이브리드 어텐션(Gated DeltaNet + Qwen Sparse Attention) + MoE + 게이트 잔차 스트림 + n-gram 임베딩**.
> NVIDIA는 **자사 개발 모델이 아님을 명시**(third-party 고지). 라이선스도 **NVIDIA Open Model License + Qwen Community License 1.0 이중 적용**(API `license: other` 실측 확인).

> [!insight] 📊 FP8 → NVFP4: 무손실이 아니라 **절반 이상에서 상승**
> 9개 벤치마크 비교 결과 — **9개 중 5개에서 4비트가 8비트를 이긴다**:
> - SciCode 16.3 → **18.8** (**+2.5**)
> - AA-LCR 71.9 → **74.1** (**+2.2**)
> - MMMU Pro 77.1 → **78.3** (+1.2)
> - HLE 34.7 → **35.4** (+0.7)
> - IFBench 80.5 → **81.0** (+0.5)
>
> **하락 4개는 전부 1점 미만**:
> - GPQA Diamond 92.0 → 91.5 (−0.5) · τ²-Bench Telecom 90.8 → 90.1 (−0.7)
> - Omniscience 28.1 → 27.6 (−0.5) · Terminal-Bench 2.1 83.3 → 82.9 (−0.4)
> → **최대 상승 +2.5 / 최대 하락 −0.7.** 비대칭이 뚜렷하다. 상승은 양자화 노이즈의 정규화 효과이거나 **측정 분산**일 가능성이 높다 — 어느 쪽이든 **"4비트는 손해"라는 통념이 이 모델에서는 성립하지 않는다.**

> [!warning] 🎯 표기와 측정의 불일치 — 볼트 규칙 적용 대상
> 카드 표는 **FP8 행 전체를 볼드 처리**해 시각적으로 FP8 우위를 암시한다. 그러나 **실제 숫자는 절반 이상에서 NVFP4가 앞선다.**
> → 볼트 규칙 *"자기규정과 자기측정이 어긋나면 **측정을 채택**"* 정확한 적용 대상.
> → 이 배치 [[teamai-cli]] 건과 **같은 계열의 함정**: 거기서는 API의 파생 분류가, 여기서는 **표의 서식**이 원 수치를 가렸다. **둘 다 "숫자를 보기 전에 표시를 먼저 읽으면 틀린다".**

> [!warning] 날짜 불일치
> 카드 `Release Date` 는 **08/31/2026** 표기, HF API `createdAt` 은 **2026-09-02**(볼트 실측). 2일 차이.
> → 사소하나 **카드 자체 표기와 플랫폼 기록이 어긋난다**는 점은 기록해 둔다. 카드 수치를 인용할 때 "카드 기준"임을 명시할 근거.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **높음, 단 하드웨어 조건부.** NVFP4는 **Blackwell 세대(RTX 50xx·B100 등) 네이티브 지원**이 전제다. 구세대 GPU에서는 이점이 반감된다. 다운로드 **26,302**(♥185, 비율 142:1)는 **실사용 비율이 매우 높다** — [[MiniCPM5-2B]](2.9:1)와 정반대. **관심보다 실제로 쓰인다.**
- **메모리 아키텍처**: 양자화 자체가 메모리 전략. FP8→FP4로 **가중치 메모리 약 절반**. 하이브리드 어텐션(Gated DeltaNet + Sparse Attention)은 **KV 캐시 절감**에 유리한 구성.
- **Hermes 적용**: **VRAM이 병목이면 최우선 후보.** 정확도 손실이 −0.7 이내라면 4비트를 안 쓸 이유가 없다. 단 **비전 포함 모델**(`image-text-to-text` 실측)이라 텍스트 전용 용도면 오버스펙.
- **트레이드오프**: **이 모델에서는 트레이드오프가 사실상 없다.** 메모리 절반, 정확도 ±1점 내. 트레이드오프는 **하드웨어 세대**로 옮겨갔다.
- **오픈소스 구현체**: NVIDIA Model Optimizer(ModelOpt) 공개 툴체인. **같은 방식을 다른 모델에 적용 가능**하다는 게 이 항목의 진짜 값.

> [!action] 당장 할 것
> **내 GPU 세대부터 확인.** Blackwell이 아니면 이 가중치는 의미가 반감된다. Blackwell이면 → **ModelOpt로 내가 쓰는 모델을 직접 NVFP4 양자화**하는 경로 검토(이 레포는 결과물이자 **레시피 증명**).

> [!question] 미해결 질문
> "9개 중 5개 상승"이 **재현되는지**가 관건. 단일 실행 결과라면 ±1점은 측정 분산 범위일 수 있다. **분산·시드 정보가 카드에 없다.**

## 관련 페이지
- [[NVIDIA]]
- [[Alibaba]]
- [[MiniCPM5-2B]]
- [[Qwopus3.8-27B-Flash-GGUF]]
- [[측정도구-먼저-반증]]
- [[PI-Desktop]]

## 원본
- 출처: https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4
- 실측(2026-09-10): 다운로드 **26,302**(raw와 동일) · ♥**185**(동일) · **gated=False** · `license: other` · base `Qwen/Qwen3.8-Flash-Next` · created **2026-09-02** · modified 2026-09-05
- 실측 태그: `image-text-to-text` · `quantized` · `FP4` · `ModelOpt` — **비전 포함 확인**
- raw 대비 드리프트: **완전 일치**(다운로드·♥ 모두 고정)
- 신뢰도: ⭐⭐⭐ (양자화 전후 동일 조건 비교 · 9개 벤치 전량 공개 · 하락분도 숨기지 않음 · 실사용 비율 높음)
