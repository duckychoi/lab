---
title: "lodestones/Kromoss — MOSS-Image-Base 1024px 전체 미세조정 + 8스텝 DMD/DMD2 LoRA. 'SFT 대체품'이라면서 SFT 와는 비교하지 않았다"
type: source
domain: video-saas
tags: [video-saas, hf-model, text-to-image, moss-image, fine-tune, dmd, dmd2, turbo-lora, comfyui, int8, convrot, clip-score, 원본-파생-역전, apache-2.0]
created: 2026-10-26
updated: 2026-10-26
sources: [https://huggingface.co/lodestones/Kromoss]
reliability: medium
---

# lodestones/Kromoss

**HF**: https://huggingface.co/lodestones/Kromoss · 제작 lodestones(Chroma1 계열 제작자) · 베이스 [[OpenMOSS]] `MOSS-Image-Base` (`base_model_relation: finetune` **명시** ✅)
**실측(2026-10-26T09:08Z · HF API)**: downloads(30일) **23,972** = all-time **23,972**(수집기 일치 · 드리프트 0) · likes **263** · createdAt **2026-10-19** · lastModified 10-24 · `library_name` **`diffusers`** · `pipeline_tag: text-to-image` · apache-2.0 · 파일 37개
**도메인**: `video-saas` — 썸네일·크리에이티브용 T2I, [[Comfy-Org-MOSS-Image]] 워크플로우 drop-in
**신뢰도**: ⭐⭐ (자기측정 CLIP 1지표 · n=100 · 데이터 출처 비공개)

> [!insight] 🏆 핵심 인사이트 — **커뮤니티 파인튜닝이 원본 SFT 를 다운로드로 앞질렀고, 계수기는 이번엔 같은 계열이다**
> - Kromoss **23,972** vs 원본 `MOSS-Image-SFT` **10,757** · `MOSS-Image-Base` **7,641** (셋 다 `diffusers`) ⇒ SFT 대비 **2.23배** · Base+SFT 합 대비 **1.31배**
> - ⚖️ 규약 ⑰ 점검: diffusers 계수 = `model_index.json` + **최상위** `*.safetensors` 만(중첩 제외 · hub-docs 10-26 재확인). Kromoss 는 최상위에 LoRA **2개**(`8-steps-dmd*.safetensors`)가 있어 *diffusers 로드 + LoRA 1개* 사용자는 **2회** 계수, ComfyUI 사용자가 `diffusion_models/` 만 받으면 **0회** ⇒ **사용자당 0~2회**. 파일당 계수(diffusion-single-file) 수준의 부풀림은 없다 → **2.23배는 대체로 동일 단위 비교**(LoRA 이중계수 상한 고려 시 ≥1.1배).
> - 🎯 **좋아요는 원본**: SFT **735** · Base **557** > Kromoss **263** — [[원본-파생-역전]] 의 "다운로드는 파생, 평판은 원본" 재현.
> - 📌 같은 제작자의 `lodestones/MOSS-Image-SFT-8-steps-dmd` 가 **145,445** dl(diffusers · 최상위 safetensors 5개라 다중계수 가능)로 Kromoss 의 6배 — **이 제작자의 MOSS 생태계 유통량은 증류 LoRA 쪽이 더 크다.**

> [!warning] 🔴 CLIP 27.19 → 27.90 → 28.13 은 "의미 있는 향상"으로 인용할 수 없다
> 1. **비교 대상이 틀렸다**: 카드는 Kromoss 를 *"drop-in replacement"* for **MOSS-Image-SFT** 라고 소개하지만 표에는 **Base 만** 있고 **SFT 행이 없다.** 사전학습 Base 를 이기는 것은 미세조정의 최소 조건이다 ⇒ **"SFT 보다 나은가"는 카드로 판단 불가.** → [[비매칭-비교]]
> 2. **소표본·무분산**: PartiPrompts **100개** · 시드·분산·CI 미보고. 최대 차이 **+0.94**(27.19→28.13, 상대 +3.5%) · 50스텝 기준 **+0.71**(+2.6%) · LoRA 간 차이 **0.06~0.14**. 볼트는 PartiPrompts 100개 CLIP 의 표본 표준오차를 모른다 ⇒ **유의 여부 미확인**. [[유의성-자기제한]] 형태의 자기 철회도 없다.
> 3. **지표 자체 한계**: CLIP ViT-L/14 점수는 프롬프트-이미지 정합만 보고 미적 품질·인체·텍스트 렌더링을 보지 않는다(일반 통념 · 볼트 미검증). 8스텝 LoRA 가 50스텝보다 **높게** 나오는 것(27.90→28.13)은 CLIP 이 대비·채도에 반응하는 성향일 수 있다(추정) — 카드도 DMD2 를 *"Slightly more contrast"* 라 적었다.
> 4. **"704k training images" 의 해석**: 카드 *"update 11000 … 704k training images"* + *"64 images per update"* ⇒ **11,000 × 64 = 704,000** 으로 정확히 일치 ⇒ **고유 이미지 수가 아니라 학습에 본 샘플 수**일 가능성(볼트 계산). 데이터 출처·라이선스 **비공개** ⇒ Apache-2.0 가중치여도 학습 데이터 권리는 불명.
> 5. **원격 코드**: Quick start 가 `custom_pipeline="pipeline_moss_image", trust_remote_code=True` 를 요구 — 레포 내 `.py` 실행. 볼트는 실행하지 않았다(규약).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: [[Comfy-Org-MOSS-Image]] 의 `moss_image_sft_bf16.safetensors` 자리에 `kromoss_bf16` 을 꽂는 **파일 교체만으로 업그레이드** + int8(ConvRot W8A8, **5.4GB**) 제공 ⇒ 구현 난이도 최저. 🎯 `convert_to_comfy.py`·`quantize_convrot.py` 가 Comfy-Org 의 SFT 파일을 **바이트 단위로 재현**한다고 주장 ⇒ **자기 파인튜닝 → ComfyUI 단일파일 변환 경로가 공개**됐다(미검증).
- **크리에이터 인사이트**: **8스텝 · CFG 1** 은 50스텝 · CFG 3(네거티브 분기 포함) 대비 스텝 기준 약 **1/12 연산**(50×2 vs 8×1 추정) ⇒ 썸네일 대량 시안 생성 비용 직결.
- **프롬프트 패턴**: 50스텝/CFG3/shift5/레이어 22 skip(네거티브) · LoRA 시 euler/simple 8스텝 CFG1 · LoRA 는 **unmerged** 적용(bf16 병합 금지 — *"delta is close to bf16's rounding step"*). 4스텝도 동작 주장.
- **워크플로우**: Comfy-Org MOSS 공식 워크플로우 + `LoraLoaderModelOnly` strength 1 · `kromoss_simple_workflow.json` 동봉(미열람).
- **디자인 레퍼런스**: 해당 없음.
- **경쟁 우위 빈틈**: **Apache-2.0** — 같은 배치 [[Comfy-Org-Fibo-2.0]](CC BY-NC) 대비 **상업 SaaS 탑재 가능**한 쪽. 단 텍스트 인코더 Qwen3.5-9B 그대로라 VRAM 병목은 MOSS 와 동일.

> [!action] 당장 할 것 (중간)
> MOSS-Image-SFT int8 vs Kromoss int8 + DMD2 LoRA 8스텝을 **같은 시드·같은 썸네일 프롬프트 20개**로 나란히 생성해 눈으로 비교 — 카드가 하지 않은 SFT 대조를 직접 채운다.

## 관련 페이지
- [[OpenMOSS]] · [[Comfy-Org-MOSS-Image]] — drop-in 대상 · [[Comfy-Org]] · [[ComfyUI]]
- [[원본-파생-역전]] · [[계수기-배수]] · [[파생저장소-식별]] · [[비매칭-비교]] · [[유의성-자기제한]]
- [[Comfy-Org-Fibo-2.0]] — 같은 배치 T2I(라이선스 대조)
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/lodestones/Kromoss
- 볼트 실측(2026-10-26T09:08Z UTC): dl 30d **23,972** / all-time **23,972** / likes **263** ‖ MOSS-Image-SFT 10,757/10,757/735 · MOSS-Image-Base 7,641/7,641/557
- 신뢰도: ⭐⭐ (HF 다운로드 23,972 · diffusers 계수 · 성능은 자기측정 CLIP n=100)
