---
title: "Qwen-Image-2.1 — 원본이 스스로 사용자를 파생으로 보냈다 (그리고 Apache-2.0 계보가 비상업으로 바뀌었다)"
type: source
domain: ai-news
tags: [ai-news, video-saas, huggingface, qwen, alibaba, image-generation, image-editing, rgba, dit, 원본-파생-역전, 비상업-라이선스]
created: 2026-09-22
updated: 2026-09-24
sources: []
reliability: high
---

# Qwen-Image-2.1

> [!insight] 🎯 핵심 인사이트: 이번 [[원본-파생-역전]] 은 원본이 설계했다
> 볼트 실측(09-22): 원본 `Qwen/Qwen-Image-2.1` DL **6,523**, [[Comfy-Org]] 재포장본 `Comfy-Org/Qwen-Image-2.1` DL **535,365**. **82.1배**다. 파생 58개의 DL 합계는 **599,200** 이다.
> 📌 기존 두 사례([[Swift-Qwen3.8-27B-GGUF]] 12.5배, [[FastVideo]] 95.6배)와 결정적으로 다른 점이 있다. **원본 README가 직접 파생으로 안내한다.** GitHub README News 31행: *"[ComfyUI] natively supports Qwen-Image-2.1 from **Day 0**. Compatible weights at **Comfy-Org/Qwen-Image-2.1**"*. diffusers·ComfyUI·vLLM-Omni·SGLang·LightX2V **5곳 Day-0 지원**이 같은 날(09-20) 공지됐다.
> 🎯 **역전이 "사용자가 포장본을 고른 결과"가 아니라 "발표 단계에서 배포 경로를 미리 나눈 결과"다.** 볼트의 다운로드 기준 수집 채널은 이런 출시에서 **원본을 원리적으로 놓친다.** 수집기가 이 원본을 잡은 것은 규약에 따른 **의식적 예외**였다.
> ✅ 개념 페이지의 *"좋아요는 반대로 간다"* 도 세 번째로 재현됐다. 좋아요는 **원본 1,590 대 Comfy 486**이다.

> [!warning] 🔴 라이선스 계보가 끊겼다(수집기 미기재)
> ✅ 수집기 지적은 정확하다. LICENSE 16행 *"'Non-Commercial' shall mean for **research or evaluation purposes only**"*, 20행 *"You shall not use the Materials for any commercial purpose without obtaining a **separate commercial license**"*. 발효일은 **2026-09-20**이다.
> 🔴 **수집기가 놓친 것이 있다. 직전 Qwen-Image 계열은 전부 Apache-2.0이었다**(HF cardData 실측): `Qwen-Image`(2025-08) · `Qwen-Image-Edit-2511` · `Qwen-Image-Layered`(2025-12) · `Qwen-Image-2512` · `Qwen-Image-Bench` 모두 `apache-2.0`. **2.1에서 처음으로 `qwen-research`(비상업)로 바뀌었다.** 프롬프트 재작성 모델 `Qwen-Image-2.1-PE-T2I/I2I` 도 같은 라이선스다.
> 🎯 **"다음 버전이 나오면 갈아탄다"는 가정이 깨진다.** 상업 파이프라인에서 쓰려면 **Apache 마지막 세대(2512·Edit-2511·Layered)에 머물러야 한다.**
> ✅ Comfy-Org 재포장본도 `qwen-research` 를 그대로 유지한다. [[Comfy-Org-YuE2]] 때처럼 **재포장이 라이선스를 바꾸지는 않았다.**
> 📌 조항 두 개가 더 있다. 31행: 산출물로 모델을 학습해 배포하면 *"Built with Qwen"* 을 표기해야 한다. 37행: 특허·IP 소송을 제기하면 라이선스가 종료된다.

> [!warning] ⚠️ "7B"의 한정어: 저자는 붙였고, 플랫폼이 뗐다
> README 28행 원문: *"With just **7B parameters in its visual generation component** (32 Single-Stream DiT layers)"*. ✅ **저자는 한정어를 보존했다.** 수집기도 "생성부 7B"로 옮겼다.
> 🔴 **HF 모델 페이지의 safetensors 메타는 `7,115,124,736`(7.12B)만 표시한다.** 이 숫자는 transformer 파일 **14.23GB ÷ 2바이트**와 정확히 같다. **텍스트 인코더가 계산에서 빠졌다.** → [[한정어-탈락]] 의 **"플랫폼 자동 탈락"** 변형이다. 사람이 아니라 메타데이터 집계기가 한정어를 떼었다.
> ✅ **파일 실측**(`?blobs=true`): transformer **14.23GB** · text_encoder **17.53GB** · vae **1.35GB** · 합계 **33.13GB**. 수집기 수치와 **전부 일치**한다.
> 📌 텍스트 인코더는 GitHub README 382행 기준 **Qwen3-VL 8B**(`Qwen3VLForConditionalGeneration`, 36층, hidden 4096)이다. 17.53GB÷2 ≈ 8.8B이므로 **실행 시 총 파라미터는 약 16B 이상**이다. VRAM 계산은 7B가 아니라 이 숫자로 해야 한다.

> [!warning] 🔴 정량 벤치마크 0개(수집기 ✅, 범위를 넓혀도 같다)
> ✅ HF 카드 157행: 벤치 수치 **0**.
> 🆕 **GitHub README 507행도 0이다.** 352행은 *"detailed benchmarks"* 를 **vLLM-Omni 레시피로 떠넘긴다**. 그 문서도 추론 속도 벤치일 가능성이 높다(⚠️ 미열람). Qwen은 자체 벤치 레포 `Qwen/Qwen-Image-Bench`(2026-05, DL 31,464)를 갖고 있지만 **카드에서 인용하지 않는다.**
> 🎯 벤더가 벤치를 **가지고 있는데 쓰지 않은** 경우다. [[검사가능성-후퇴]] 후보다(⚠️ 블로그 미열람. 블로그에 표가 있으면 철회한다).

> [!note] 🆕 "네이티브 투명"의 범위: 계보상 첫 RGBA는 아니다
> `Qwen-Image-Layered`(2025-12, Apache-2.0)가 이미 *"decomposing an image into multiple **RGBA layers**"* 를 했다. 2.1의 새로운 점은 **RGBA를 T2I·편집과 한 모델에 합친 것**과 **64채널 RGBA VAE**(GitHub 383행)다. 투명 생성은 프롬프트 규약으로 켠다: *"This is an RGBA image with transparency. … The image has alpha channel and the background is transparent."*
> 📌 **[[Qwen-Image-Agent]](06-26)와의 연결**: 볼트는 그때 *"약한 프롬프트 → LLM 자동 보강"* 패턴을 기록했다. 2.1에서 Qwen은 그것을 **별도 모델로 제품화했다.** `Qwen-Image-2.1-PE-T2I`(Qwen3.5-VL 9B 파인튜닝, *"brief request in any language → detailed English prompt + recommended aspect ratio"*)와 `PE-I2I`(DL 4,604)다.
> 📌 [[Qwen-Image-Flash]](06-04)는 **2.0 기반 증류**였다. 2.1과의 직접 계보는 이름 외에는 확인하지 못했다.

## 도메인 판정

**domain: ai-news 유지, `video-saas` 태그 병기.** 기능만 보면 video-saas에 가깝다. 9:16 네이티브(1536×2752), **투명 PNG 에셋**(자막·스티커·오버레이), 참조 10장 정체성 보존, **"three-view character reference → storyboard"**(GitHub Showcase)가 모두 볼트 운영자의 영상 파이프라인과 맞닿는다. 🔴 **그러나 비상업 라이선스라 SaaS 제품에 넣을 수 없다.** 이 모델의 역할은 **채택 후보가 아니라 기능 레퍼런스와 연구·평가용**이다. 따라서 주 도메인은 기존 Qwen-Image 형제 페이지와 같은 ai-news로 둔다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ Qwen 공식 · 좋아요 1,590 · 파생 58개/599k DL · Day-0 생태계 5곳 · GitHub ★1,142. 🔴 **성능 수치 0**, 논문 없음.
- **즉시 활용**: **연구·평가용으로는 YES, 제품에는 NO.** BF16 33GB라 `enable_model_cpu_offload()` 없이는 소비자 GPU에 올라가지 않는다. 파생 GGUF(`abenzerps/Qwen-Image-2.1-GGUF` DL 33,232)나 ComfyUI 경로가 현실적이다. diffusers는 **git 최신**, transformers **≥5.17** 이 필요하다.
- **6개월 영향력**: 🎯 **"생성 후 배경 제거(rembg류)" 단계가 사라진다.** 투명 에셋을 처음부터 알파 채널로 뽑는다. 다만 상업 라인에서는 **Apache 대체재가 나올 때까지** 영향이 제한된다.
- **대체 관계**: 볼트 운영자 파이프라인의 **배경 제거 + 편집 모델 2단**을 1단으로 줄인다. Qwen 자체 라인에서는 Layered(분해)·Edit-2511(편집)을 합친 상위 모델이다. 🔴 라이선스 때문에 **Apache 세대를 대체하지는 못한다.**
- **허와 실**: 확실한 것은 **아키텍처(32층 single-stream DiT, block-causal attention, prefix KV cache 재사용)와 배포 생태계**다. 🔴 *"strong image quality at low computational cost"* 는 **숫자가 하나도 없는 주장**이다. "Compact"도 텍스트 인코더를 빼고 한 말이다.
- **액션**: 아래.

> [!action] 당장 할 것
> 볼트 운영자 영상의 **자막 배경·스티커 에셋 5종**을 RGBA 프롬프트 규약으로 생성해 **알파 경계 품질을 rembg 후처리와 나란히 비교**한다(평가 목적이므로 라이선스 범위 안). 결과가 확연히 좋으면 **Apache 세대 `Qwen-Image-Layered` 로 같은 결과를 낼 수 있는지**를 이어서 확인한다.

## 관련 페이지
- [[원본-파생-역전]]: 🎯 세 번째 사례, **원본이 설계한 역전**
- [[Comfy-Org]] · [[Comfy-Org-YuE2]] · [[ComfyUI]] · [[파생저장소-식별]]
- [[Qwen-Image-Agent]]: 프롬프트 보강 → **PE 모델로 제품화**
- [[Qwen-Image-Flash]]: 2.0 증류(계보 미확인)
- [[한정어-탈락]]: 플랫폼 메타 자동 탈락 · [[검사가능성-후퇴]] 후보
- [[Alibaba]] · [[HuggingFace]] · [[AI-영상-생성-2026]]
- [[ai-news]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/Qwen/Qwen-Image-2.1 · https://github.com/QwenLM/Qwen-Image-2.1
- 볼트 실측(2026-09-22, HF API): DL **6,523**(raw 183) · 좋아요 **1,590**(raw 1,072) · created 2026-09-14T03:47:26Z ✅ · lastModified 2026-09-21T04:50:49Z ✅ · license `other`/`qwen-research` ✅ · base_model 없음 ✅ · pipeline `text-to-image` · diffusers `QwenImage21Pipeline` · safetensors 메타 7,115,124,736
- 파일(`?blobs=true`): transformer 14.23GB · text_encoder 17.53GB · vae 1.35GB · 합계 33.13GB ✅
- 파생(`base_model:` 필터): **58개 / DL 합계 599,200** · Comfy-Org **535,365**/좋아요 486(raw 120/357) · `abenzerps/Qwen-Image-2.1-GGUF` **33,232**/778. 🔴 raw의 `abenzerps/Qwen-Image-2.1-Uncensored-GGUF (DL 0)` 는 현재 **HTTP 307 리다이렉트**다. 이름이 바뀐 동일 레포로 보인다
- GitHub `QwenLM/Qwen-Image-2.1`: ★**1,142**(raw 767) · license NOASSERTION · created 2026-09-14
- 수치 출처: HF README 28·103·115~123·157행, LICENSE 16·19·20·31·37행, GitHub README 29~34·352·380~386·441~451행, text_encoder/transformer `config.json`, `model_index.json` **원문 실열람**. 형제 모델 license는 HF API cardData
- raw 대비: 볼트 추가 = 🎯 **원본 README가 Comfy-Org로 안내한 "설계된 역전"(82.1배)** · 🔴 **Apache-2.0 계보 → 비상업 전환(raw 미기재)** · 🆕 **HF 메타 7.12B = transformer만(플랫폼 한정어 탈락), 텍스트 인코더 Qwen3-VL 8B** · 🆕 **GitHub README도 벤치 0, 자체 Qwen-Image-Bench 미인용** · 🆕 **RGBA는 Layered가 선행** · 🆕 **PE 모델 = [[Qwen-Image-Agent]] 패턴의 제품화** · 🔴 raw DL 183/Comfy 120은 하루 만에 낡음
- 신뢰도: ⭐⭐⭐ (벤더 공식 · 파일·라이선스 전건 실측 / 정량 벤치 0 · 블로그 미열람)

---

## 🔄 2026-09-24 갱신 — **역전 4번째 관측 + trendingScore 라는 새 축**

**볼트 실측** — 원본·재포장·제3자 파생 3종 동시 조회(전부 `expand[]=downloadsAllTime` 포함):

| 저장소 | createdAt | DL(창=누적) | 좋아요 | **trendingScore** |
|---|---|---|---|---|
| `Qwen/Qwen-Image-2.1` (원본) | 2026-09-14 | **28,407** | **2,097** | **1,970** |
| `Comfy-Org/Qwen-Image-2.1` (재포장) | 2026-09-15 | **2,220,609** | 648 | 622 |
| `abenzerps/Qwen-Image-2.1-Uncensored-GGUF` | 2026-09-20 | **350,678** | 1,516 | 1,337 |

- **재포장 / 원본 = 78.17배** (09-22 기록 82.1배 → 소폭 축소, 원본이 상대적 회복)
- **제3자 GGUF / 원본 = 12.34배**
- ✅ **세 저장소 전부 생성 10일 이내 → 창 = 누적 확인.** 배수는 창 아티팩트가 아니다 → [[지표-창길이]]

### 🆕 trendingScore 가 좋아요 편에 선다 — 정체 축에 독립 지표가 하나 더 생겼다

| 지표 | 승자 | 비율 |
|---|---|---|
| 다운로드 | **재포장** | 78.17배 |
| 좋아요 | **원본** | 3.24배 |
| **trendingScore** | **원본** | **3.17배** |

🎯 **좋아요(누적 행위)와 trendingScore(현재 관심)가 거의 같은 비율로 원본을 편든다(3.24 vs 3.17).** [[원본-파생-역전]] 의 2축("파일 vs 정체")에 **정체 쪽 두 번째 독립 지표**가 붙는다.
📌 **주목과 채택이 78배 갈린다** — 원본이 trendingScore 3배 앞서면서 다운로드는 78분의 1이다.
🔴 주의: [[파생저장소-식별]] 이 *"trendingScore 절대값은 볼트 커버리지의 함수"* 라 경고했다. **여기서 쓴 것은 절대값이 아니라 동일 시점 쌍 내 비(比)** 이므로 그 경고에 걸리지 않는다. **배치 간 비교는 여전히 금지.**

### 🎯 `abenzerps` 가 살아났다 — 09-22 제외 판정의 후속
09-22에 이 파생은 **DL 0 · HF 307 리다이렉트**로 수집 제외됐고, 볼트가 *"개명된 레포는 DL 33,232"* 로 정정했다. **09-24 실측 350,678** — **2일 만에 10.6배.** ✅ **"DL 0 으로 제외하지 말고 리다이렉트를 따라가라"는 [[파생저장소-식별]] 규약이 정당했음이 수치로 확인됐다.**

⚠️ 확인 범위: **API 메타데이터만.** 🔴 모델 카드 미열람. 🔴 원본 README가 Comfy-Org 로 안내하는지(09-22 *"배포 설계"* 판정 근거)는 이번에 **재확인하지 않았다.**
