---
title: Prism ML
type: entity
domain: ai-news
tags: [quantization, ternary, gguf, local-llm, llama-cpp, mlx]
created: 2026-09-20
updated: 2026-10-04
sources: [Ternary-Bonsai-2-27B.md, Bonsai-27B.md]
reliability: medium
---

# Prism ML

> [!warning] 🔴 2026-10-04 **중복 엔티티 발견 — 같은 조직에 페이지가 두 개다**
> `wiki/entities/` 에 **`Prism-ML.md`(이 페이지 · created 2026-09-20 · 참조 10건)** 과 **`prism-ml.md`(created 2026-09-29 · 참조 4건)** 이 공존한다. **같은 조직**(HF `prism-ml` · GitHub `PrismML-Eng`)이고 **sources 도 겹친다**([[Ternary-Bonsai-2-27B]]).
> ⇒ 📌 **[[정규명-우선-중복검사]] 가 다루는 바로 그 실패이고, 볼트 자기 볼트에서 발생했다.** 🔴 **통합하지 않고 남긴다** — 양쪽이 참조되고 있어 삭제하면 링크가 끊긴다. ⚖️ **통합은 별도 작업으로 actionable 등록**(정본 = 참조 많은 `Prism-ML`, 대소문자 정규화 규칙 필요).

> [!update] 2026-10-04 갱신 — 🏆 **[[Ternary-Bonsai-2-27B]] 카드 전문 열람으로 이 벤더의 측정 성향이 확정됐다**
> **볼트 실측(2026-10-04T09:12:38Z)**: `prism-ml/Ternary-Bonsai-2-27B-gguf` DL **3,969,867**(09-29 실측 3,457,124 → **+512,743 / 5일 · 일평균 ≈102,549**) · likes **2,400** · trendingScore **222** · `gguf.total` **26,895,998,464** · `base_model` **Qwen/Qwen3.8-27B**.
> 🏆 **측정 성향 — 이 벤더는 자기에게 불리한 것을 적는다(부분적으로)**:
> - ✅ **벤치 14종을 이름까지 공개**(MMLU-Redux · MuSR · GSM8K · MATH-500 · AIME25 · AIME26 · HumanEval+ · MBPP+ · LiveCodeBench · IFEval · IFBench · BFCL v3 · MMMU-Pro · OCR Bench v2) + **카테고리별 표** + **분모 공개**(FP16 평균 **86.32** → Bonsai **84.78** = **98.2%**)
> - ✅ **1.72bit 가 이상값이고 출하물은 1.75/2.13 임을 카드가 명시**(`5.8 GB ideal at 1.72 bits/weight` ↔ 실제 **5.95GB / 7.21GB**)
> - ✅ **집계 평균이 실패 방식을 가린다고 스스로 적는다** — 경쟁 빌드 IQ2_XXS 의 선택적 붕괴를 수치로 보인다(**AIME26 57.5 · LiveCodeBench 56.4** ↔ **MMLU-Redux 88.93**) + *"which is why **casual testing misses the collapse**"* ⇒ [[측정도구-먼저-반증]] 벤더 자발 실행
> - ✅ **2번째 모델 계열로 일반화 근거 제시**(Gemma-4-31B · *"the collapse is a property of the **methods** rather than of one base model"*)
> - ✅ **효율 지표 자체 제시**(점수/GB: Bonsai **0.457** ↔ IQ2_XXS **0.257**)
> 🔴 **그러나 방향이 한쪽이다** — 경쟁자 수치는 분해하고 **자기 수치의 분산은 접는다**: *"98.2% 유지"* 뒤에서 **14종 중 3칸은 양자화본이 FP16 보다 높다**(LiveCodeBench 90.07>90.05 · IFBench 74.00>71.00 · 코딩 89.42>89.07). 🔴 **그리고 tok/s 가 두 개다** — 수집기가 전한 **47 tok/s** 는 **M5 Max** 수치이고, 카드에는 *"standard laptop at **~28 tok/s**"* 도 있다([[한정어-탈락]] 주의).
> 🏆 **볼트 발견 — 이 벤더의 `gguf.total` 은 비전 타워를 집계하지 않는다**: 카드 성분(24.35B 백본 + 2.54B 임베딩/LM헤드 + **0.46B 비전 타워** = 27.36B) 중 **앞 둘의 합 26.89B 가 `gguf.total` 26.896B 와 일치**한다. ⇒ 📌 **베이스 대비 −3.187% 편차의 절반 이상이 양자화 손실이 아니라 집계 범위 차이다** → [[대체필드-대조]] 결론 수정.
> - 🔴 **미열람**: 화이트페이퍼 `PrismML-Eng/Bonsai-demo/bonsai-2-27b-whitepaper.pdf` · GGUF 파일 목록(mmproj 분리 여부) · **제3자 재현 0건**(전부 벤더 자체 측정)
> - ⬆️ **[[Ternary-Bonsai-2-27B]] 신뢰도 medium → high 상향**(카드 공개 범위 근거)

HF `prism-ml` · GitHub `PrismML-Eng` · prismml.com. **삼진(ternary) 양자화 전문 벤더.**

> [!insight] 🎯 자리의 성격 — **양자화하는 데서 멈추지 않고 런타임을 포크한다**
> 볼트 [[DavidAU]] 가 *"커뮤니티 양자화·탈검열 재배포자"* 라면 Prism ML 은 **포맷과 커널을 같이 낸다**:
> - **llama.cpp 포크**(`PrismML-Eng/llama.cpp`, CUDA + Metal) — `PTQ1_0`·`PQ2_0` 커스텀 타입과 **하다마드 활성 런타임**
> - **MLX 포크** · **mlx-swift 포크**(iOS/macOS) · MLX 배포판 별도(`Ternary-Bonsai-2-27B-mlx-2bit`)
> - **Bonsai-demo** 레포 = *"the **source of truth** for running these models"*(카드가 자기 README보다 그쪽이 맞다고 선언)
> 🎯 **[[Comfy-Org]]=재포장 < [[DavidAU]]=양자화 < [[TokenRhythm]]=사후학습** 이라는 볼트의 개입 깊이 축에서, **Prism ML은 양자화이되 런타임까지 내려가 있다** — 같은 칸이 아니다.

> [!insight] 🎯 **포맷이 오용을 거부하도록 설계했다**
> *"the packed model **declares its rotation as metadata**, so a runtime either applies the matching transform **or refuses to load the file**."*
> 그리고 실패 모드를 직접 적는다: *"Stock llama.cpp ... **loads `Q2_0` without any warning and produces garbage**"* — 🎯 **자기 옛 파일이 다른 런타임에서 조용히 틀린다는 사실을 자기가 공개했다.** [[자기제한-명시]] 의 강한 사례다.

> [!warning] 🔴 그런데 **증거는 반대로 갔다**
> v1(`Ternary-Bonsai-27B-gguf`)에는 `.eval_results/` 3종과 `eval-results` 태그가 있었고, **v2(`Ternary-Bonsai-2-27B-gguf`)에는 없다.** 점수 주장은 올라갔다. → [[검사가능성-후퇴]] 사례 1.
> 🔴 **모든 성능 수치가 자사 화이트페이퍼 PDF 단일 출처**이며 arXiv 논문이 아니다. 제3자 재현 **확인되지 않음**.
> 🔴 **법인 실체·국적·규모 전부 미확인.** 확인된 것은 도메인(prismml.com) · HF 조직 · GitHub 조직 · Discord.

## 모델
- [[Ternary-Bonsai-2-27B]] — Qwen3.8-27B 기반, DL(30일) **1,908,396** · 좋아요 1,315 · Apache-2.0 *(2026-09-16)*
- [[Bonsai-27B]] — Qwen3.6-27B 기반 v1, DL **662,554** · 좋아요 **1,370** · Apache-2.0 *(2026-07-04)*
- 🎯 **v1이 좋아요에서 아직 앞선다**(1,370 > 1,315).

## 관련 페이지
- [[Ternary-Bonsai-2-27B]] · [[Bonsai-27B]] · [[검사가능성-후퇴]] · [[DavidAU]] · [[Comfy-Org]] · [[단위-불일치]] · [[Qwen3.8-27B]] · [[ai-news]]
