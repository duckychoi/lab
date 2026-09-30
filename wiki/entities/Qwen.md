---
title: Qwen
type: entity
domain: local-llm
tags: [HuggingFace, 조직, Alibaba, 오픈웨이트, VLM, 파생생태계, apache-2.0]
created: 2026-09-29
updated: 2026-09-30
sources: [Qwen3.8-27B.md, DN-MOPD.md, Ternary-Bonsai-2-27B.md]
reliability: medium
---

# Qwen

> [!note] 정체
> [[Qwen3.8-27B]] 등 Qwen 계열 오픈웨이트 모델을 배포하는 **HuggingFace 조직 계정**. 볼트에 **파생본이 먼저 쌓이고 본체는 09-29 에야 처음 배달**된 특이 사례다.

## 볼트가 아는 것

- [[Qwen3.8-27B]] — `Qwen/Qwen3.8-27B` · **DL 6,844,348**(30일 · 볼트 실측 2026-09-29 · 배치 내 1위) · ♥16,521 · **Apache-2.0** · `gated: False` · created 2026-08-05 · **`safetensors.total` 27,781,427,952** · pipeline **`image-text-to-text`**(VLM)
- 볼트 보유 파생본: [[Qwen3.8-27B-FP8]](`Qwen/Qwen3.8-27B-FP8` · 자체 파생) · [[Qwen3.8-27B-GGUF]](`unsloth/...` · 제3자) · [[Ternary-Bonsai-2-27B]](`prism-ml/...` · 제3자 삼진 양자화)
- 연구 사용: 같은 배치 [[DN-MOPD]] 가 **Qwen3.5 계열 3개 크기**로 실험, [[Post-Training-Behavioral-Shadows]] 가 **Qwen2.5-1.5B** 사용

## 🎯 볼트가 주목하는 것

🏆 **이 조직의 실질 영향력은 자기 다운로드가 아니라 파생 생태계다.** 오늘 배치 HF 모델 3건 중 **2건이 Qwen 계열**이다 — 본체([[Qwen3.8-27B]] DL 684만) + 삼진 양자화본([[Ternary-Bonsai-2-27B]] DL 346만, `base_model` 태그로 확인). **합치면 배치 DL 의 압도적 다수.**
🎯 **연구 벤치 백본으로도 기본값이 됐다** — 오늘 논문 5건 중 **2건이 Qwen 을 학생/백본으로** 쓴다. **Apache-2.0 + 가중치 공개가 만든 위치**다([[Lightricks]] 의 `gated`·`other` 와 정반대).

📌 **그러나 [[원본-파생-역전]] 이 볼트 등록 순서에서 일어났다** — 파생본 3종이 먼저 들어오는 동안 **본체 URL 은 생성 후 55일(08-05 → 09-29) 동안 배달되지 않았다** → [[선발창-누락]].

> [!warning] ⬜ 볼트가 확인하지 않은 것
> - **조직 전반(모델 수·Qwen3.5/3.6/3.7 라인·기업 소속)을 조회하지 않았다.** Alibaba 계열로 알려져 있으나 **볼트가 확인한 사실이 아니다** — 미검증 표기 유지.
> - 🔴 [[Qwen3.8-27B]] 모델카드의 벤치 표(OSWorld 84.3 등)는 **전부 벤더 자기보고**이며 볼트 미열람.
> - ✅ **제3자 수치는 1건 있다** — 09-28 [[hindsight]] Retain 리더보드에서 **7위 · 지연 30.7s · 233 tok/s**(DL 1위 모델이 그 과제에선 최하위권) → [[상대속도-가림]].

## 관련 페이지
- [[Qwen3.8-27B]] · [[Qwen3.8-27B-FP8]] · [[Qwen3.8-27B-GGUF]] · [[Ternary-Bonsai-2-27B]] · [[prism-ml]]
- [[DN-MOPD]] · [[Post-Training-Behavioral-Shadows]] · [[hindsight]]
- [[원본-파생-역전]] · [[선발창-누락]] · [[상대속도-가림]] · [[파생저장소-식별]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/Qwen
- 볼트 실측: HF API `models/Qwen/Qwen3.8-27B` (2026-09-29 09:08 UTC)
- 신뢰도: ⭐⭐⭐ (모델 1건 메타 실검증 · 조직 전반·소속 미조회)

> [!update] 2026-09-30 — [[Qwen3.8-27B]] DL **7,020,239**(트렌딩 내 1위) · 🎯 **47일 정지 상태로 하루 +17.6만**
> 볼트 실측(09-30 09:13): DL30 **7,020,239**(드리프트 0) · allTime **11,744,215**(완전 일치) · ♥**16,590** · apache-2.0 · created 2026-08-05 · **lastModified 2026-08-14(47일 정지)** · `safetensors.total` **27,781,427,952**(완전 일치)
> 🏆 **파생 계보를 API 로 직접 검증**: [[Ternary-Bonsai-2-27B]] 응답에 `base_model: ["Qwen/Qwen3.8-27B"]` · 태그 `base_model:quantized:…` **실측**.
> 🎯 **파생/본체 비율이 고정이다**: 50.5%(09-29: 3,457,124/6,844,348) → **51.0%**(09-30: 3,581,027/7,020,239). 하루 사이 본체 +175,891 · 파생 +123,903 — **함께 움직인다**. → [[원본-파생-역전]] 에 **"역전이 아니라 연동"** 추가.
> 📌 **47일 정지 + 하루 17만 DL** 조합이 [[Omni-IO-Skills]] 의 *"모델 갱신 없이 하네스로 능력 확장"* 과 같은 날 같은 방향을 가리킨다 — **모델은 멈춰도 위층은 움직인다.**
> 🔴 사내 벤치 문제 미해소(SWEBench 79.0 각주 *"In-house"*) — 오늘 [[Omni-IO-Skills]] 의 **UniM-90 출처 미확인**과 같은 계열.
