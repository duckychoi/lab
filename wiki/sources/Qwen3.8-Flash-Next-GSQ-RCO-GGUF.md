---
title: "ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF — 27B 카드를 '미러'했는데 대조군과 라이선스가 따라오지 않았다"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, quantization, mixed-precision, gsq, rco, moe, qwen4exp, llama.cpp, 단위-불일치, 파생저장소-식별]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF

> [!insight] 🎯 핵심 인사이트 — **카드 주석 *"Mirrors the Qwen3.8-27B card"* 가 정확히 무엇을 복사했고 무엇을 빠뜨렸는지가 이 항목의 발견이다**
> 볼트 [[Qwen3.8-27B-GSQ-RCO-GGUF]] 가 *"배치 유일의 제3자 대조 벤치"* 로 high를 받은 이유는 **Unsloth UD 양자화본과 동일 크기 대조**였다. 27B README(볼트 09-22 재열람) 원문: *"evaluated against the BF16 base model **and the Unsloth Dynamic (UD) quantizations**"* + perplexity 3종.
> 🔴 **Flash-Next 카드는 BF16 대비만 있다** — Unsloth 대조 없음, perplexity 없음. 볼트 [[Qwen3.8-Flash-Next-GGUF]](Unsloth)가 *"GSQ-RCO의 반박과 대조해야 한다"* 고 기다리던 **그 대조가 이 모델에선 오지 않았다.**
> 🔴 그리고 **라이선스가 틀린 채로 복사됐다**(아래). 🎯 **템플릿 미러링은 미덕(표 구조)과 오류(메타데이터)를 함께 옮긴다.**

> [!warning] 🔴 **라이선스 자기모순 — 메타는 Apache-2.0, 본문은 "원본 라이선스 상속" = `qwen-community-1.0`**
> YAML·HF API: `license: apache-2.0`. README 225행 원문: *"These quantized weights **inherit the license of the base model** (Qwen3.8-Flash-Next)."*
> 원본 `Qwen/Qwen3.8-Flash-Next` API 실측: `license: other` · `license_name: **qwen-community-1.0**`(볼트 [[Qwen3.8-Flash-Next]] 09-03 기록과 일치).
> 🎯 27B 카드에선 두 문장이 일치했다(원본 [[Qwen3.8-27B]] 가 Apache-2.0). **Flash-Next로 미러하면서 YAML만 그대로 두어 모순이 생겼다**(볼트 추정 — 경위는 미확인). 수집기는 메타의 Apache-2.0을 그대로 옮겼다. → **상용 판단은 본문(qwen-community-1.0) 기준으로 한다.**

> [!note] ✅ 수집기 수치 전부 일치 + 볼트 재계산
> | 빌드 | bpw* | 샤드1(상주) | 샤드2(n-gram) | 합계 | AIME25 | GPQA-D | LCB v6 | Task avg |
> |---|---|---|---|---|---|---|---|---|
> | BF16 | 16 | — | — | 354 GB | 100.00 | 91.92 | 87.43 | 93.12 |
> | Q2_0 | 2.40 | 37.6 | 28.8 | 66.4 | 96.67 | 89.39 | 81.14 | 89.07 |
> | IQ2_XS | 2.50 | 39.2 | 28.8 | 68.0 | 96.67 | 87.37 | 83.43 | 89.16 |
> | **IQ3_XXS** | 3.00 | 47.0 | 28.8 | 75.8 | **100.00** | 91.41 | 86.29 | **92.57** |
> 볼트 재계산: Task avg는 3개 벤치 산술평균과 소수 둘째 자리까지 일치 · 92.57/93.12 = **99.4%** ✅ · 354/75.8 = 4.67배 ✅ · 속도 367.49/108.19 = **3.40배**(카드 "3.4x") · 지연 12.68/6.70 = **1.89배**(카드 "1.9x") · 디코드 93.79/70.30 = 1.33배.
> ✅ 한정어 2종 원문 확인: 제로샷 평균 100.3~101.4%는 *"within roughly one standard error and should be read as **parity rather than improvement**"* · *"primarily optimized for **xhigh reasoning effort** … At lower reasoning-effort levels, quantization-induced degradation **can be larger**."* 📌 번들 chat template도 `reasoning_effort` 기본값이 **xhigh**이고 `high` 를 xhigh로 강제 매핑한다(선택지는 xhigh/medium/low).
> ✅ **하드웨어는 카드 228행 전문 어디에도 없다** — 수집기 *"발췌분에 미기재"* → **전문에도 없음**. *"Measured with `llama.cpp` over 55 prompts spanning eleven categories"* 가 전부다. GPU·백엔드·빌드 버전 미상.

> [!warning] ⚠️ **bpw 2.40 은 파일 비트수가 아니다** — [[단위-불일치]]
> 카드 원문: *"the bit-width column is the average **over the transformer weights**"*. n-gram 테이블(`per_layer_token_embd`, **51.2B 파라미터**)은 **IQ4_NL 4.5bpw 고정, 탐색 제외**(51.2B×4.5/8 = 28.8 GB ✅).
> 볼트 계산(GGUF 메타 총 파라미터 176,943,899,520 기준): **파일 전체 평균 = Q2_0 ≈3.00 · IQ2_XS ≈3.07 · IQ3_XXS ≈3.43 bpw.**
> ✅ 카드는 정직하게 밝혔다. 🔴 수집기 헤드라인 *"2.4~3.0bpw"* 는 그 한정어를 떨어뜨렸다. 📌 [[Ternary-Bonsai-2-27B]] 가 경쟁사에 건 비판(*"'2-bit' build … is really 2.8 bits/weight"*)이 **정의를 밝힌 경우에도** 헤드라인 층에서 재발하는 구조다.
> ⚠️ 사소한 라벨 모순: IQ2_XS 비고 *"Smallest at equal quality"* — 그런데 **Q2_0이 1.6GB 더 작고** task avg 차는 0.09다.

> [!note] 🎯 **수집기 미확인 2건 해소 — 포크 불필요, Q2_0은 업스트림 표준 타입**
> **① `-lm mmap --lazy-mode on` 은 stock llama.cpp에 있다.** `ggml-org/llama.cpp` master `common/arg.cpp` 실열람: `-lm, --load-mode`(mmap/mlock/dio 통합, 2026-07-23 #20834) · `-lzm, --lazy-mode`(*"on-demand reading of certain tensors, for example **per-layer embeddings**"*, 08-27 `TENSOR_READ_LAZY` #27794 → 08-30 개명 #27969). 아키텍처 `qwen4exp` 도 업스트림(08-27 #27742 *"model: add Qwen3.8-Flash-Next"*). 카드는 커스텀 빌드 링크 없이 *"standard GGUF and run unmodified in llama.cpp, Ollama, and LM Studio"* 라고 적는다.
> 🔴 **단 최소 버전이 카드에 없다** — 위 커밋들로 보면 **2026-08-30 이후 빌드**가 필요하다(볼트 추정). Ollama·LM Studio가 `--lazy-mode` 를 노출하는지는 **미확인**.
> **② 이 레포의 Q2_0 = Bonsai가 경고한 그 Q2_0 타입과 같은 GGML 타입이다.** `ggml.h`: `GGML_TYPE_Q2_0 = 42`. 도입 PR #24448(2026-07-07) 작성자가 **Prism-ML 자신**이다 — 원문: *"Main motivation is to support **Ternary Bonsai** models"*, 형식 *"group of 64 … {-1,0,+1,+2} × d"*. CUDA(#25707, 07-30)·Metal·Vulkan 백엔드도 병합.
> 🎯 **따라서 [[Ternary-Bonsai-2-27B]] 의 "stock이 Q2_0을 경고 없이 로드하고 쓰레기 출력" 은 타입 문제가 아니라 Bonsai 가중치의 하다마드 회전 문제**다(그 페이지 원문: *"because it has no Hadamard activation runtime"*). 이 레포 카드엔 회전 언급이 없으므로 stock에서 정상 디코드될 것으로 **추정**한다 — **볼트 실행 검증 없음.**
> 📌 주의: `ffn_down_exps` 는 **모든 빌드에서 Q2_0 고정**(640행이 256으로 안 나뉨). IQ3_XXS를 받아도 **Q2_0 커널 지원 빌드가 필요**하다.

> [!note] 📌 볼트 실측 (2026-09-22, HF API) — 원본 역전 없음, 자매는 폭증
> | | 이 레포 | 원본 `Qwen/Qwen3.8-Flash-Next` | 자매 `…27B-GSQ-RCO-GGUF` |
> |---|---|---|---|
> | 다운로드(30일) | **53,094**(수집기 42,965) | **774,778**(수집기 761,112) | **1,292,471**(볼트 09-06: 348,389) |
> | 좋아요 | 225(수집기 201) | 5,564 | 1,548 |
> 원본/파생 DL = **14.6배**(수집기 17.7배) — [[원본-파생-역전]] **아님** ✅. `base_model_relation: quantized` 명시 ✅ → [[파생저장소-식별]] 탐지키 정상 작동 사례.
> 파일 **18개 전수**: GGUF 샤드 6(3빌드×2, 샤드2 3개는 모두 28,800,138,432 B로 동일) · mmproj BF16 0.91GB · **`tensor-allocation/*.rco-allocation.txt` 3개**(텐서별 타입 배정 공개 ✅ [[검사가능성-공사]]) · 플롯 5 · banner · README · .gitattributes.
> 🎯 볼트 [[Qwen3.8-Flash-Next]] 미해결 항목 일부 해소: **MoE 확정(층당 512 전문가 × 48층, 토큰당 10 활성)** · n-gram 임베딩 실재(51.2B) · GGUF 메타 `context_length` **262,144**.
> 📌 번들 chat template 말미 주석 `{#- Unsloth fixes - developer role, merged system messages, tool calling #}` — **대조군에서 빠진 Unsloth의 템플릿을 쓰고 있다.**

## 도메인별 추출 (local-llm)

- **실용성 판단**: 조건부 YES. 🔴 **상주 37.6~47.0GB + KV** → 48GB급 단일 GPU 또는 통합메모리 64GB+ 급. 샤드2(28.8GB)는 SSD에 mmap. 카드 원문: *"Keeping the n-gram table in RAM … removes the paging cost entirely"* — **디스크 페이징 비용은 수치로 제시되지 않았다.**
- **메모리 아키텍처**: 🎯 **per-layer n-gram 임베딩을 디스크 지연 로드** — 파라미터의 29%(51.2B/176.9B)가 행 단위 조회라 VRAM 밖에 둘 수 있다. 로컬 배포에서 "모델 크기 ≠ 상주 크기"인 드문 구조.
- **Hermes 적용**: 현 하드웨어 기준 부담 큼. 27B 자매(IQ3_S 11.8GB)가 여전히 1순위.
- **트레이드오프**: Q2_0 = 프리필 3.4배·지연 1.9배 빠름, task avg **−3.50**(vs IQ3_XXS). RAG·긴 프롬프트에서 격차 최대(카드: RAG 9.6배), 짧은 추론 프롬프트에선 0.8~0.9배로 역전.
- **오픈소스 구현체**: GGUF(업스트림 llama.cpp) · GSQ/RCO 코드 공개(IST-DASLab/GSQ, RCO).

> [!action] 당장 할 것
> 볼트 [[Qwen3.8-27B-GSQ-RCO-GGUF]] 의 high 판정을 **Flash-Next에 전이하지 않는다** — 이 레포는 대조군 없음·라이선스 모순으로 medium. 사용 시 **llama.cpp 2026-08-30 이후 빌드 + 라이선스는 qwen-community-1.0** 으로 전제.

> [!question] 미해결 질문
> 1. 측정 하드웨어·llama.cpp 커밋 — 카드에 없음.
> 2. 샤드2를 SSD mmap으로 둘 때 디코드 속도 저하 폭 — 카드에 수치 없음.
> 3. Unsloth `Qwen3.8-Flash-Next-GGUF` 동급 크기 대비 성능 — 27B에선 했던 비교가 여기선 왜 빠졌나.

## 관련 페이지
- [[ISTA-DASLab]]  *(09-22 연결)*
- [[Qwen3.8-27B-GSQ-RCO-GGUF]]
- [[Qwen3.8-Flash-Next]]
- [[Qwen3.8-Flash-Next-GGUF]]
- [[Qwen3.8-Flash-Next-NVFP4]]
- [[Ternary-Bonsai-2-27B]]
- [[Prism-ML]]
- [[Alibaba]]
- [[단위-불일치]]
- [[파생저장소-식별]]
- [[원본-파생-역전]]
- [[검사가능성-공사]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF
- 볼트 실측(2026-09-22, HF API): DL 53,094 · 좋아요 225 · created 2026-09-07 · lastMod 2026-09-18 · gated false · license(메타) apache-2.0 · base_model `Qwen/Qwen3.8-Flash-Next` · relation `quantized` · GGUF arch `qwen4exp` · ctx 262,144 · 파일 18
- 원본 실측: `Qwen/Qwen3.8-Flash-Next` DL 774,778 · 좋아요 5,564 · license `qwen-community-1.0`
- 수치 출처: README **228행 전문** + llama.cpp master `common/arg.cpp`·`ggml/include/ggml.h`·`src/llama-arch.cpp` + PR #24448 본문 + 27B 자매 README(대조군·라이선스 문장)
- raw 대비: ✅ 크기·bpw·벤치·속도·한정어 전부 일치 · 🔴 **라이선스 모순(Apache 메타 ↔ 원본 상속 문장) 누락** · 🔴 **bpw가 트랜스포머 가중치 한정임을 탈락(파일 평균 3.0~3.4)** · 🎯 **`-lm`/`--lazy-mode` 업스트림 존재·Q2_0 업스트림 타입(Prism-ML 기여) 확인** · 🔴 **27B 대비 Unsloth 대조군 탈락** · ✅ 하드웨어 전문에도 미기재
- 신뢰도: ⭐⭐ (수치 내부정합 완전·할당 파일 공개 / 대조군 없음·라이선스 모순·하드웨어 미상)
