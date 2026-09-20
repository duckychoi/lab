---
title: "Swift-Qwen3.8-27B-GGUF — 볼트가 09-19에 도착을 예고한 파생, 그리고 표가 3개였다"
type: source
domain: local-llm
tags: [local-llm, ai-news, hf-model, gguf, quantization, 27b, efficient-thinking, 표-부분인용, 파생저장소-식별]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# Swift-Qwen3.8-27B-GGUF (ukisai)

> [!insight] 🎯 **볼트가 이 항목의 도착을 09-19에 적어 뒀다**
> [[파생저장소-식별]] 124행 원문: *"미보유 8건의 성격이 이 개념을 다시 확인한다: **`ukisai/Swift-Qwen3.8-27b` 와 `ukisai/Swift-Qwen3.8-27B-GGUF` 가 둘 다 미보유**다 — 같은 모델의 base/GGUF 쌍이 각각 NEW로 대기 중이다."*
> ✅ **하루 뒤 GGUF 쪽이 실제로 배달됐다.** 볼트가 트렌딩 목록에서 본 쌍 중 **한쪽만** 왔다.
> 🎯 **왜 한쪽만 왔는지가 이번의 발견이다** → 아래 [[원본-파생-역전]].

> [!warning] 🔴 **수집기 정정 — "이 GGUF 빌드 자체의 측정치가 아니다"는 표 1개만 본 결론이다**
> 수집기 raw: *"벤치는 BF16·vLLM 0.27.1 기준이며 **이 F16 GGUF 빌드 자체의 측정치가 아니다**(카드가 명시)."*
> 🔴 **카드에는 표가 3개다**:
> 1. **BF16 표(9행)** — Qwen3.8-27B BF16 base vs base+Swift adapter, vLLM 0.27.1. ← 수집기가 본 유일한 표
> 2. **양자화 평가 표** — *"Each row compares **the same quantized base** with and without the Swift adapter."* (AWQ INT4 등)
> 3. 🎯 **GGUF quantizations 표 — 24개 tier × {파일크기, KLD wikitext@512, KLD wikitext@32k, KLD held-out@32k, Top-p@32k}**
>
> **3번은 정확히 이 GGUF 빌드의 측정치다.** 양자화 아티팩트에 맞는 지표(BF16 원본 대비 **KL 발산**과 **최상위 토큰 일치율**)로 재어 뒀다.
> 📌 **[[표-부분인용]] 의 "표 개수" 축 두 번째 사례** — 첫 사례 [[Qwen3.8-27B-TWIN-TURBO-709-GGUF]] 는 4표 중 1표만 읽어 **68점 오류**였다. 이번엔 3표 중 1표였고 결론이 *"자체 측정 없음"* → *"24행 있음"* 으로 뒤집힌다.

> [!note] 📌 GGUF 측정 표 발췌 (볼트 실열람) — **KLD는 tier가 내려갈수록 단조 악화한다**
> | tier | 크기 | KLD wikitext@512 | Top-p@32k |
> |---|---|---|---|
> | Q8_0 | 29.1 GB | 0.0009 | 97.92% |
> | Q6_K | 22.9 GB | 0.0020 | 96.85% |
> | Q4_K_M | 18.0 GB | 0.0120 | 94.30% |
> | Q3_K_M | 13.6 GB | 0.0552 | 89.91% |
> | Q2_K | 11.0 GB | 0.1617 | 84.05% |
> | **IQ2_XXS** | **9.1 GB** | **0.2852** | **78.09%** |
>
> 🎯 **이 표가 같은 배치 [[Ternary-Bonsai-2-27B]] 와 정면으로 맞물린다.** Bonsai README는 경쟁자를 익명으로 지목했다 — *"a widely-used '2-bit' build of Qwen3.8-27B is really **2.8 bits/weight at 9.4 GB**"*. **Swift의 IQ2_XXS는 9.1GB(≈2.66 bit/w), IQ2_XS는 9.3GB다** — 크기·베이스가 일치하는 계열이다.
> 📌 **두 레포가 같은 배치에서 같은 비교를 반대편에서 기술한다**: Bonsai는 *"IQ2_XXS 72.59 vs 우리 84.78"*(태스크 정확도), Swift는 *"IQ2_XXS Top-p 78.09% · KLD 0.2852"*(원본 충실도). **볼트가 두 축의 수치를 동시에 갖게 된 첫 사례**다.
> ⚠️ 단 **같은 파일이라는 증거는 없다** — 크기·베이스가 같을 뿐이다. 단정하지 않는다.
> ⚠️ *new tier* 로 표시된 tier들은 **2026-09-13 추가**분이라 **32k 열이 비어 있다**(`—`). 카드가 *"their 32k columns will be filled as those runs complete"* 라고 명시 → ✅ **미완 칸을 비워 두고 이유를 적었다.** [[검사가능성-공사]] 의 좋은 사례.

> [!warning] 🔴 헤드라인 검증 — **"58.3%"는 18개 셀 중 최댓값이고, "<1% loss"는 9행 중 4행에서 거짓이다**
> BF16 표 9행 전문(수집기는 **5행**만 옮겼다 — C-Eval · IFBench · HMMT · **ERQA** 누락):
>
> | 벤치 | Base | Swift | Δ점수 | 평균토큰↓ | 중앙값토큰↓ |
> |---|---|---|---|---|---|
> | GPQA-Diamond | 88.38 | 88.28 | **−0.10** | 41.0% | **58.3%** |
> | MMLU-Pro | 85.47 | 84.95 | −0.52 | 46.2% | 28.3% |
> | **C-Eval** | 90.00 | **90.62** | **+0.62** | 46.1% | 19.3% |
> | **IFBench** | 73.53 | 71.80 | **−1.73** | 42.2% | 50.5% |
> | AIME 2026 | 98.67 | 94.00 | **−4.67** | 26.7% | 50.2% |
> | **HMMT (Nov 2025)** | 99.33 | 96.00 | **−3.33** | 31.1% | 45.9% |
> | **ERQA**(멀티모달) | 67.45 | 66.30 | **−1.15** | 50.6% | 54.6% |
> | Terminal-Bench 2.1 | 66.74 | 65.84 | −0.90 | 26.5% | 38.7% |
> | LiveCodeBench v6 | 76.76 | **81.55** | **+4.79** | 24.3% | 45.8% |
>
> 🔴 **헤드라인 *"near-identical performance (<1% loss)"* 는 9행 중 5행에서만 참이다** — IFBench −1.73 · AIME −4.67 · HMMT −3.33 · ERQA −1.15 **4행이 1%를 넘는다.** 카드 자신의 표가 카드 자신의 헤드라인을 반증한다.
> 🔴 **헤드라인 *"58.3% fewer thinking tokens"* 는 9행 × {평균, 중앙값} = **18개 셀 중 최댓값**이다.** 평균감소 9개의 산술평균은 **약 37.2%** 다. 수집기는 *"GPQA-Diamond 중앙값 감소폭 한 건"* 이라고 정확히 짚었고 ✅, 볼트는 **"18셀 중 최대"** 로 한 칸 더 좁힌다.
> ✅ **개선 행이 둘이다**(C-Eval +0.62 · LiveCodeBench +4.79). 수집기는 LiveCodeBench만 짚었고 *"near-identical 설명과 방향이 다르다"* 고 옳게 지적했다 — **C-Eval도 같은 방향**이다.
> 🔴 **수집기가 통째로 빠뜨린 헤드라인 주장 하나**: *"as a result getting a **x1.95 speed-up** on several tasks"*. *"several tasks"* 가 어느 것인지, 어느 하드웨어인지 **카드에 표가 없다.**

> [!note] 📌 볼트 실측 (2026-09-20, HF API) — **파생이 원본을 12.5배 앞선다**
> | | `Swift-Qwen3.8-27B-GGUF` | `Swift-Qwen3.8-27b`(원본) |
> |---|---|---|
> | 다운로드(30일) | **136,668** | **10,962** |
> | 좋아요 | **321** | **497** |
> | 생성 | 2026-09-11 | 2026-09-08 |
> | 라이브러리 | gguf | transformers |
>
> 🎯 **다운로드는 파생이 12.5배 많고, 좋아요는 원본이 1.55배 많다.** 수집기 채널은 **다운로드로 선발**하므로 **구조적으로 파생을 고르고 원본을 버린다.** → 신설 [[원본-파생-역전]].
> ✅ **`base_model_relation: quantized` 를 명시적으로 선언했다** — [[FastVideo]] 병합분 가 이 필드를 비워 `finetune` 으로 오라벨된 것과 대비된다. 🎯 **[[파생저장소-식별]] 의 탐지 키를 `base_model` 에서 `base_model_relation` 으로 한 칸 올려야 한다.**
> 🔴 **사슬은 3홉이다**: `Qwen/Qwen3.8-27B` → `ukisai/Swift-Qwen3.8-27b`(**LoRA 어댑터** — 원본 레포 태그에 `lora`, 카드 본문도 *"the Swift **adapter**"*) → 이 GGUF. `base_model` 은 **1홉만** 기록한다(개념 기존 기술과 일치).
> 수집기 기록 다운로드 120,740 → 볼트 실측 **136,668**(+13.2%) · 좋아요 321 **일치**.

> [!note] 📌 카드에만 있는 배포 수치 — 수집기 미전달분
> - 🎯 **KV 캐시 = 토큰당 64 KiB → 262,144 전체 컨텍스트에서 16 GB.** *"so lower `-c` if it does not fit"* — **볼트가 늘 없다고 적던 "실배포 숫자"가 여기 있다.**
> - 🎯 **MTP(Multi-Token Prediction) 레이어가 모든 tier에 Q8_0로 포함** — 내장 드래프트 모델로 **llama.cpp 투기적 디코딩** 가능. 수집기 미언급.
> - ✅ **멀티모달 지원**: `mmproj-Swift-Qwen3.8-27B-F16.gguf` 동봉, 모든 tier와 호환, `-hf` 사용 시 자동 다운로드.
> - 🔴 **실사용 함정 문서화**: LM Studio·koboldcpp·Jan AI 기본 4,096 컨텍스트가 *"overflows on long reasoning and **looks like an endless loop**"*. → ✅ 실패 모드를 미리 적은 [[자기제한-명시]] 사례.
> ⚠️ **라이선스 불일치**: 카드 370행은 *"Swift weights are distributed through **gated access** under the Swift Open License v1.0"* 인데 **HF API 는 두 레포 모두 `gated: false`** 를 반환한다. 어느 쪽이 최신인지 **확인하지 못했다.** 상용 이용은 별도 Enterprise License(문의).

> [!warning] 🔴 볼트 자기 오류 — **API 파일 목록이 잘려 하마터면 틀릴 뻔했다**
> 볼트의 첫 조회는 `siblings` 를 **40개에서 끊어** 출력했고, 그 범위에 mmproj 가 없어 *"비전 프로젝터 미동봉 → 이미지 입력 불가"* 라는 결론이 나올 뻔했다.
> ✅ 전수 재조회(**54개**) 결과 `mmproj-Swift-Qwen3.8-27B-F16.gguf` **실재**. 카드 309~312행도 명시.
> 📌 **[[표-부분인용]] 이 API 응답에서도 성립한다** — *"잘린 목록은 부분인용이고, 부분인용은 원문 대조를 통과한다."* 본 파일명은 전부 실재했다. **세지 않아서 틀리는 것**이 같다.

## 도메인별 추출 (local-llm)

- **실용성 판단**: ✅ **YES.** 24 tier 중 고를 수 있고 **KLD·Top-p 로 손실을 정량 비교**할 수 있다. Q4_K_M 18.0GB / KLD 0.0120 / Top-p 94.30% 가 균형점으로 보인다. 🔴 단 **262K를 다 쓰면 KV만 16GB** — 컨텍스트가 곧 VRAM이다.
- **메모리 아키텍처**: 해당 없음(양자화 배포). 🎯 단 **MTP 내장 = 투기적 디코딩**은 속도 축 장치다.
- **Hermes 적용**: 후보. 🔴 **1.95배 가속 주장은 근거표 없음** — 채택 판단은 자체 측정 후.
- **트레이드오프**: 🎯 **이 카드의 미덕은 트레이드오프를 두 축으로 준 것**이다 — 정확도(9행 표)와 원본 충실도(24행 KLD 표). 볼트가 본 GGUF 배포자 중 **가장 잘 잰 축에 든다**([[DavidAU]] *"분모·하네스 미공개"* 와 대비).
- **오픈소스 구현체**: 본 레포 + 원본 `ukisai/Swift-Qwen3.8-27b`.

> [!action] 당장 할 것
> 🔴 **수집기에 원본(`ukisai/Swift-Qwen3.8-27b`)을 별도 요청한다** — 다운로드 10,962로는 **영원히 선발되지 않는다**(좋아요는 497로 파생보다 높은데도). [[원본-파생-역전]] 의 첫 실행 항목.

> [!question] 미해결 질문
> 1. ***"x1.95 speed-up on several tasks"* 의 근거** — 카드에 표 없음.
> 2. **gated 표기 불일치**(카드 gated ↔ API false) — 미해소.
> 3. Swift IQ2_XXS(9.1GB)가 **Bonsai가 지목한 "9.4GB 2-bit 빌드"와 같은 계열인지** — 크기 근접, 동일성 미확인.

## 관련 페이지
- [[원본-파생-역전]]
- [[파생저장소-식별]]
- [[표-부분인용]]
- [[Ternary-Bonsai-2-27B]]
- [[Qwen3.8-27B-TWIN-TURBO-709-GGUF]]
- [[DavidAU-Qwen3.8-27B-TURBO]]
- [[DavidAU]]
- [[자기제한-명시]]
- [[검사가능성-공사]]
- [[UkisAI]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/ukisai/Swift-Qwen3.8-27B-GGUF
- 볼트 실측(2026-09-20, HF API): 다운로드(30일) **136,668**(수집기 120,740, +13.2%) · 좋아요 **321**(일치) · **파일 54개**(mmproj 포함) · `base_model` `ukisai/Swift-Qwen3.8-27b` · **`base_model_relation: quantized`** · `pipeline_tag: image-text-to-text` · license `other`(swift-open-license-1.0) · created 2026-09-11T14:58:56Z · lastMod 2026-09-16T15:17:31Z · gated **false**
- 원본 레포 실측: `ukisai/Swift-Qwen3.8-27b` 다운로드 **10,962** · 좋아요 **497** · `lora` 태그 · base `Qwen/Qwen3.8-27B`(finetune)
- 수치 출처: README **388행 중 표 3개 전부 실열람**(BF16 9행 · 양자화 평가 · **GGUF 24 tier KLD**) + 배포 섹션(KV 64KiB/token · MTP · mmproj · 4,096 함정) + License 섹션
- raw 대비: 볼트 추가 = 🔴 **"GGUF 자체 측정치 없음" 정정 — 24행 KLD 표 실재** · 🔴 **9행 중 4행이 "<1% loss" 반증** · 🔴 **58.3% = 18셀 중 최댓값(평균 37.2%)** · 🔴 **누락 행 4개 복원(C-Eval·IFBench·HMMT·ERQA)** · 🔴 **"x1.95 가속" 주장 자체가 미전달** · 🎯 **다운로드 12.5배 역전 실측 → [[원본-파생-역전]] 신설** · ✅ **`base_model_relation` 탐지키 발견** · **KV 16GB·MTP 발굴**
- 신뢰도: ⭐⭐ (측정 품질은 GGUF 배포자 중 상급·미완 칸 명시 / **헤드라인 2건이 자기 표와 불일치 · 1.95배 근거 없음 · 라이선스 표기 불일치**)
