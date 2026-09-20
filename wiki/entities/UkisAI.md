---
title: UkisAI
type: entity
domain: local-llm
tags: [efficient-thinking, gguf, quantization, lora, 상용-라이선스]
created: 2026-09-20
updated: 2026-09-20
sources: [Swift-Qwen3.8-27B-GGUF.md]
reliability: medium
---

# UkisAI

HF `ukisai` · ukisai.com. **"생각 토큰을 줄이는" 파생 모델(Swift) 제작사.**

> [!insight] 자리의 성격 — **능력을 늘리지 않고 추론 길이를 줄인다**
> `Swift-Qwen3.8-27b` = [[Qwen3.8-27B]] 에 **LoRA 어댑터**를 붙인 파생(원본 레포 `lora` 태그 · 카드 본문 *"the Swift **adapter**"*). 점수를 거의 유지하면서 사고 토큰을 줄이는 것이 상품이다.
> 🎯 **볼트 개입 깊이 축에서 새 칸이다**: 재포장([[Comfy-Org]]) · 양자화([[DavidAU]]·[[Prism-ML]]) · 사후학습([[TokenRhythm]]) 에 더해 **"추론 예산 재조정"** — 가중치를 바꾸되 능력이 아니라 **길이**를 바꾼다.

> [!note] ✅ 측정 품질이 GGUF 배포자 중 상급이다
> 카드에 **표 3개**: BF16 9행(정확도+토큰) · 양자화 평가 · **GGUF 24 tier × KLD/Top-p**. 재현 조건(시드 0–4 · Terminal-Bench 5시행 · 벤치별 출력 상한)까지 적었다.
> ✅ **미완 칸을 비워 두고 이유를 썼다** — *new tier* 의 32k 열은 `—`, *"their 32k columns will be filled as those runs complete"*. → [[검사가능성-공사]]. 🎯 같은 배치 [[Prism-ML]] 의 [[검사가능성-후퇴]] 와 **정확히 반대 행동**이다.
> ✅ 실사용 함정도 적었다 — LM Studio/koboldcpp/Jan AI 기본 4,096 컨텍스트가 *"looks like an endless loop"*.

> [!warning] 🔴 그러나 헤드라인 2건이 자기 표와 어긋난다
> - *"near-identical performance (**<1% loss**)"* → **9행 중 4행이 1% 초과**(IFBench −1.73 · AIME −4.67 · HMMT −3.33 · ERQA −1.15)
> - *"**58.3% fewer** thinking tokens"* → **18개 셀 중 최댓값**(평균감소 9개의 평균은 약 **37.2%**)
> - *"**x1.95 speed-up** on several tasks"* → **근거표 없음**
> 🎯 **표는 정직하고 요약이 과하다.** 볼트 [[DavidAU]] 09-17 사례(*"단계별 표 4개를 정직하게 다 적었는데 볼트가 못 읽었다"*)와 **원인이 반대**다 — 여기선 **벤더 자신의 요약이 자기 표를 넘어간다.**
> 🔴 **라이선스**: `swift-open-license-1.0` 독자 라이선스. 카드는 *"distributed through **gated access**"* 라 하는데 **HF API 는 두 레포 모두 `gated: false`** — 불일치 미해소. 상용은 별도 Enterprise 문의.

## 모델
- [[Swift-Qwen3.8-27B-GGUF]] — DL(30일) **136,668** · 좋아요 321 · `base_model_relation: quantized` ✅ · mmproj 동봉 · MTP 내장 *(2026-09-11)*
- `ukisai/Swift-Qwen3.8-27b`(**원본, 볼트 미보유**) — DL **10,962** · 좋아요 **497** · LoRA · *(2026-09-08)* → 🔴 [[원본-파생-역전]] 로 선발되지 않는다. **backlog 요청 대상.**

## 관련 페이지
- [[Swift-Qwen3.8-27B-GGUF]] · [[원본-파생-역전]] · [[표-부분인용]] · [[검사가능성-공사]] · [[Prism-ML]] · [[DavidAU]] · [[Qwen3.8-27B]] · [[local-llm]]
