---
title: Huihui-Qwen3.8-27B-abliterated-GGUF — 거부 제거 배포본이 월 219만 다운로드, 그런데 벤치마크가 하나도 없다
type: source
domain: local-llm
tags: [local-llm, ai-news, hf-model, gguf, abliteration, uncensored, qwen, quantization, unsloth]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: medium
---

# huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF

**HF**: https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF
**다운로드(최근 30일)**: **2,194,861** (2026-09-07 API 실측 · raw 표기와 **완전 일치**)
**좋아요 574 · 생성 2026-08-16 · 최종수정 2026-09-05 · `gated: False` · `private: False`**
**라이선스**: **apache-2.0** · **베이스**: [[Qwen3.8-27B]] · `pipeline_tag: image-text-to-text` · library `transformers`

> [!insight] 핵심 인사이트 — **이 배치 최대 다운로드가 "능력"이 아니라 "제거"를 파는 모델이다**
> 월 **219만 다운로드**는 이번 13건 중 최대이고, [[Tiel-Coder-35B-A3B-GGUF]](23.9만)의 **9.2배**, [[timesfm-3.0-pytorch]](14.4만)의 **15.2배**다.
> 그런데 이 모델이 파는 것은 **새 능력이 아니라 거부(refusal) 응답의 제거**다. 베이스 [[Qwen3.8-27B]] 에 **abliteration** 을 적용해 거부 방향을 걷어냈다.
> → 볼트가 [[에이전트-스킬]] 에서 08-28에 기록한 **"억제(inhibition) 축"** 이 **모델 가중치 층에서 재현**된다. 그때는 *스킬로 행동을 억제*하는 자산이었고, 여기서는 **가중치에서 억제를 제거**한다. **방향은 반대지만 축은 같다** — 모델의 "하지 않음"을 다루는 시장이 스킬 층과 가중치 층 양쪽에 있다.

> [!warning] 🔴 **모델 카드에 벤치마크 수치가 단 하나도 없다** — 219만 다운로드와의 격차
> 카드 원문을 끝까지 읽었으나 **성능 수치·비교표·평가 결과가 전무**하다. 있는 것은 **양자화 절차(llama-quantize 명령어)** 와 **ablate 레이어 범위**뿐이다.
> → **"abliteration이 원 모델 성능을 얼마나 훼손하는가"에 대한 저자 측 측정이 없다.** 카드 자체가 스스로를 *"a **crude, proof-of-concept** implementation"* 이라 부른다(원문).
> **월 219만 다운로드가 품질 근거가 아니라는 것을 저자가 먼저 인정한 셈이다.** 볼트 규칙(*"배지·지표를 근거로 쓰지 않는다"*)이 여기서는 **다운로드 수**에 적용된다 — 다운로드는 **수요의 크기**를 재지 **성능**을 재지 않는다.

> [!insight] 성능 보존을 위한 설계는 있다 — 측정이 없을 뿐
> 카드가 밝힌 **ablate 범위의 진화**(원문 실측):
> - **초기**: 앞 15개 레이어를 **보존**하고 나머지 ablate
> - **UD 계열**: unsloth GGUF 기반, **레이어 18~51만** ablate
> - **UD-DW 계열(최신)**: unsloth GGUF 기반, **레이어 23~51만** ablate
> → **ablate 범위가 점점 좁아진다.** 카드 원문: *"This helps **retain more of the original model's performance**."* 그리고 **`MTP and visual has not been modified`** — MTP와 비전 경로는 건드리지 않는다(raw 기재 정확, `pipeline_tag: image-text-to-text` 와 일치).
> **설계는 보존을 지향하는데 보존됐는지는 아무도 재지 않았다.** [[Tiel-Coder-35B-A3B-GGUF]](같은 배치)가 **자체 측정이나마 방법·표본·열세를 공개**한 것과 대비된다.

> [!warning] 비표준 양자화 — **파일 크기 직관이 깨진다**
> 카드 원문: ablate 대상 텐서(**token_embd · output · ffn_down · ssm_out · attn_output**)를 Q2_K~Q6_K 에서 **Q8_0 으로 올리고** 파일명에 `_L` 을 붙인다. Q8_0 버전은 해당 텐서를 **BF16** 으로 올려 `Q8_0_L` 로 명명.
> 저자 경고 원문: *"This is **not a standard quantization**, so you might find that **Q2_K_L is larger than Q3_K and Q4_K**."*
> → **양자화 이름으로 크기·품질을 추론하면 틀린다.** raw 기재(*"Q2_K_L이 Q3_K보다 커질 수 있음"*)가 **정확**하며, 로컬 서빙 시 VRAM 계획에 직접 영향.
> 볼트 교차: [[Minima]] 가 *"496개 선형층 전부 NVFP4로 내려도 동등"* 을 보인 반면, 여기서는 **특정 텐서만 정밀도를 올려야 품질이 유지된다**고 본다. **어떤 텐서가 정밀도에 민감한가**는 두 소스가 다른 답을 시사한다 → 대조 관측 대상.

> [!note] 근거 구현체는 명시돼 있다
> 카드가 [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) 를 근거로 링크한다 — **TransformerLens 없이** refusal 방향을 제거하는 proof-of-concept. raw 기재가 정확하다. **방법의 출처가 추적 가능**한 것은 가점 요인.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **GGUF이므로 llama.cpp로 즉시 로컬 실행 가능.** 27B·Apache-2.0·gated 아님. ⚠️ **단 품질 손실 미측정**이므로 **베이스 [[Qwen3.8-27B]] 와 나란히 놓고 직접 비교하지 않으면 도입 판단 불가**.
- **메모리 아키텍처**: 해당 없음. **양자화·가중치 편집** 축.
- **Hermes 적용**: **권장하지 않음.** 볼트/ChinameBot의 병목은 거부 응답이 아니라 **정확성**이며, 이 모델은 정확성에 대해 **아무 주장도 하지 않는다**. 오히려 [[Tiel-Coder-35B-A3B-GGUF]] 처럼 **측정된 모델**이 우선순위가 높다.
- **트레이드오프**: **미측정.** 이것이 이 소스의 핵심 결함이다. abliteration이 거부만 제거하는지, 아니면 **판단 능력 일반을 함께 깎는지** 알 수 없다.
- **오픈소스 구현체**: **YES** — Sumandora/remove-refusals-with-transformers.

> [!warning] 볼트의 해석 규칙 적용 — 다운로드 219만을 어떻게 읽을 것인가
> 볼트는 09-03에 *"공개 직후 DL은 아직 없는 값"* 규칙을 세웠다. 이 모델은 **생성 2026-08-16(3주 경과)** 이므로 **그 예외에 해당하지 않는다** — 219만은 **실제 수요**로 읽어도 된다.
> 다만 **수요가 크다 ≠ 품질이 좋다**. 이 모델의 수요는 **다른 모델이 채우지 않는 공백**(거부 제거)에서 오며, 그 공백에서는 **대안이 적으므로 경쟁이 약하다.** 즉 **낮은 품질로도 높은 다운로드가 가능한 시장 구조**다.

> [!action] 당장 할 것
> **도입 전 반드시 자체 대조 1회.** 베이스 [[Qwen3.8-27B]] GGUF와 이 모델에 **같은 프롬프트 20개**(거부와 무관한 일반 추론·코딩)를 넣고 답 품질을 비교한다. 저자가 안 잰 것을 **쓰는 쪽이 재는 수밖에 없다.** 재지 않고 도입하면 볼트 규칙 위반.

> [!question] 미해결
> **UD-DW 계열의 레이어 23~51 범위는 어떻게 정해졌는가.** 카드에 근거가 없다. 경험적 탐색인지 측정 기반인지에 따라 *"성능 보존"* 주장의 무게가 완전히 달라진다.

## 관련 페이지
- [[Qwen3.8-27B]] · [[Qwen3.8-27B-GGUF]] · [[Alibaba]] · [[Minima]] · [[Tiel-Coder-35B-A3B-GGUF]] · [[Dont-Drop-Dropout]] · [[Random-Attention]] · [[에이전트-스킬]] · [[선택비용과-중복성]] · [[timesfm-3.0-pytorch]]

## 원본
- 출처: https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF
- 근거 구현: https://github.com/Sumandora/remove-refusals-with-transformers
- 수집: 2026-09-07 자동수집 (raw 도메인 ai-news → **local-llm 재분류**)
- 검증: HF 모델 API 실측 + 모델 카드 원문 대조 (2026-09-07 · DL 2,194,861 raw와 일치)
- 신뢰도: ⭐⭐⭐ (**벤치마크 전무 · 저자 자칭 proof-of-concept** — 다운로드 219만은 수요 근거이지 품질 근거가 아님)
