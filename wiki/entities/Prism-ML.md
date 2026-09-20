---
title: Prism ML
type: entity
domain: ai-news
tags: [quantization, ternary, gguf, local-llm, llama-cpp, mlx]
created: 2026-09-20
updated: 2026-09-20
sources: [Ternary-Bonsai-2-27B.md, Bonsai-27B.md]
reliability: medium
---

# Prism ML

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
