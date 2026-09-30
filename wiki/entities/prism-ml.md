---
title: prism-ml
type: entity
domain: local-llm
tags: [HuggingFace, 조직, 양자화, ternary, GGUF, on-device, 검사가능성]
created: 2026-09-29
updated: 2026-09-30
sources: [Ternary-Bonsai-2-27B.md]
reliability: medium
---

# prism-ml

> [!note] 정체
> [[Ternary-Bonsai-2-27B]] 를 배포하는 **HuggingFace 조직 계정**. 삼진(ternary) 양자화 계열 `Bonsai` 라인을 운영한다(모델 태그 `prismml`·`bonsai`).

## 볼트가 아는 것

- [[Ternary-Bonsai-2-27B]] — `prism-ml/Ternary-Bonsai-2-27B-gguf` · **DL 3,457,124**(30일 · 볼트 실측 2026-09-29) · ♥2,248 · **Apache-2.0** · created **2026-09-16** · `gated: False`
- **GGUF 전용 배포** — `safetensors` 없음, `gguf.total` **26,895,998,464**(볼트 실측)
- base_model: **[[Qwen3.8-27B]]** (`base_model:quantized:Qwen/Qwen3.8-27B` 태그로 확인)
- 태그가 실행 환경을 명시: `llama.cpp`·`cuda`·`metal`·`on-device`·`hybrid-attention`

## 🎯 볼트가 주목하는 것 — **검사 가능성을 의도적으로 공사한다**

🏆 **볼트가 09-26 에 [[검사가능성-공사]] 사례로 등록한 이유가 오늘도 유효하다.** 이 조직은 주장 옆에 **반증 재료를 같이 놓는다**:
- 비트폭을 **이상치(1.72비트)와 실측(1.75/2.13)을 나란히** 적음
- 실배포 **파일 크기**(5.95GB PTQ1_0 / 7.21GB PQ2_0)를 명시 — **누구나 받아서 확인 가능한 값**
- **tok/s 를 하드웨어와 함께**(M5 Max ~47)
- 백서 PDF + 데모 레포 공개

🎯 **그 결과 볼트가 오늘 불일치의 원인까지 좁힐 수 있었다** — 카드 표기 27.36B ↔ 실측 26.90B 의 **0.46B 차이가 카드 자신의 분해표(비전타워 0.46B)로 설명된다.** **분해해서 적어 둔 덕분에 대조가 가능했다** → [[단위-불일치]].
📌 **대비**: [[paperclipai]] 는 ★9.3만에 topics 0개, [[Lightricks]] 는 카드가 게이트 뒤. **prism-ml 은 작지만 가장 많이 열어 둔다.**

> [!warning] ⬜ 볼트가 확인하지 않은 것 · 🔴 미검증 3배치째
> - **조직의 다른 모델·소속·백서 PDF 를 조회하지 않았다.** 모델카드 본문도 미열람.
> - 🔴 카드 주장 *"14개 thinking 벤치 평균 84.78 = FP16 대비 98.2% 유지"* 는 **분모(FP16 기준선 86.3 추정)가 카드에 직접 제시되지 않아** 09-26 이후 **3배치 연속 미검증**이다. 14개 벤치 구성도 미확인.
> - ⬜ GGUF 파일 목록 미조회 — 비전타워 분리 배포 가설 검정 필요.

## 관련 페이지
- [[Ternary-Bonsai-2-27B]] · [[Qwen3.8-27B]] — base_model · [[검사가능성-공사]] · [[단위-불일치]] · [[지표-창길이]]
- [[Lightricks]]·[[paperclipai]] — 개방도 대비축 · [[local-llm]]

## 원본
- 출처: https://huggingface.co/prism-ml
- 볼트 실측: HF API `models/prism-ml/Ternary-Bonsai-2-27B-gguf` (2026-09-29 09:08 UTC)
- 신뢰도: ⭐⭐⭐ (모델 메타 실검증 · 조직 전반 미조회)

> [!update] 2026-09-30 — DL **3,581,027** · 🔴 **수집기 "다른 저장소" 판정을 볼트가 반박했다**
> 볼트 실측(09-30 09:13 · `prism-ml/Ternary-Bonsai-2-27B-gguf`): DL30 **3,581,027**(드리프트 0) · ♥**2,278**(완전 일치) · apache-2.0 · created **2026-09-16**(14일) · modified 2026-09-25 · **`gguf.total` 26,895,998,464**(완전 일치) · **`base_model: ["Qwen/Qwen3.8-27B"]`**
> 🔴 **수집기 정정**: *"볼트 기록(DL 3,457,124)은 비-gguf 본체이며 다른 저장소"* 라고 했으나 **이 19행이 그 값을 `prism-ml/Ternary-Bonsai-2-27B-gguf` 로 명시**하고 있었다. **같은 저장소이며 3,457,124→3,581,027 은 하루치 증분(+123,903)이다.**
> 🔴 **`prism-ml/Ternary-Bonsai-2-27B`(비-gguf)는 API 조회 불가**(`Invalid username or password.` 실측) — 수집기가 든 비교 저장소의 실재가 확인되지 않는다.
> 🏆 **볼트 09-29 가설이 근거를 얻었다**: 카드 27.36B − 비전타워 0.46B = **26.90B** = `gguf.total` 실측. 수집기가 카드에서 **비전타워 별도 Q8_0 mmproj 분리**를 확인해 왔다 → 가설 → **강한 가설**(파일목록 직접 대조는 여전히 미수행).
