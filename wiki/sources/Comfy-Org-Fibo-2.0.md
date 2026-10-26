---
title: "Comfy-Org/Fibo-2.0 — 원본은 게이트(양식 제출) 뒤에, 재패키징은 게이트 없이. 원값 60.2배 · 파일당 계수 보정 15~20배"
type: source
domain: video-saas
tags: [video-saas, hf-model, comfyui, text-to-image, image-editing, repackage, diffusion-single-file, 계수기-배수, 원본-파생-역전, structured-caption, qwen3-vl, flux2-vae, cc-by-nc, gated]
created: 2026-10-26
updated: 2026-10-26
sources: [https://huggingface.co/Comfy-Org/Fibo-2.0]
reliability: medium
---

# Comfy-Org/Fibo-2.0

**HF**: https://huggingface.co/Comfy-Org/Fibo-2.0 · 재패키징 [[Comfy-Org]] · 원본 BRIA AI `briaai/Fibo-2.0-dev`(T2I) + `briaai/Fibo-2.0-edit-turbo`(편집)
**실측(2026-10-26T09:08Z · HF API)**: downloads(30일) **124,557** = all-time **124,557**(수집기 일치 · 드리프트 0) · likes **186** · createdAt **2026-10-20T18:53Z** · lastModified 10-21 · `library_name` **`diffusion-single-file`** · `gated: False` · cc-by-nc-4.0 · 파일 10개(`.safetensors` **8**)
**도메인**: `video-saas` — 썸네일·크리에이티브 이미지 생성/편집 · ComfyUI 워크플로우([[Comfy-Org-MOSS-Image]] 선례)
**신뢰도**: ⭐⭐ (다운로드는 파일당 계수 · 벤치 0건 · 비상업 라이선스)

> [!insight] 🏆 핵심 인사이트 ① — **규약 ⑰ 두 번째 집행: 60.2배 중 약 3/4 은 계수기, 나머지 일부는 게이트**
> - 원본 실측(같은 시각): `Fibo-2.0-dev` **1,115** · `Fibo-2.0-edit-turbo` **955** (둘 다 `library_name: diffusers`) ⇒ 합 **2,070** ⇒ 원값 **60.2배**
> - 🔴 `diffusion-single-file` = **`.safetensors` 파일 요청마다 1회**([[계수기-배수]] 규칙 출처 `model-libraries.ts` 10-26 재확인). 레포 내 `.safetensors` **8개**: diffusion 4(dev/edit × bf16/int8) · LoRA 1 · text encoder 2(bf16/int8) · VAE 1
> - **1인당 파일 수**: 최소 T2I = diffusion 1 + text_encoder 1 + VAE 1 = **3** · turbo LoRA 또는 edit 모델 추가 시 **4** ⇒ 사람 단위 추정 **약 3.1만~4.2만** ⇒ 원본 대비 **15~20배**(추정). dev+edit+LoRA 를 모두 받는 사용자(5파일)가 많으면 ~12배까지 내려간다.
> ⇒ 🎯 **보정해도 [[원본-파생-역전]] 은 남는다** — MOSS-Image(29~39배)보다 작은 역전.
> 🎯 **좋아요는 다시 원본 쪽**: 원본 157 + 121 = **278** > Comfy **186** (09-20 관측 패턴 · MOSS 에 이어 재현).

> [!insight] 🏆 핵심 인사이트 ② — **역전의 비(非)계수기 성분 = 게이트 우회** (볼트 신규 관측)
> 원본 2레포는 **`gated: auto`** 이고 접근 양식이 **회사명·회사 URL·Discord·용도(Commercial/Academic/Personal)** 를 수집한다(`cardData.extra_gated_fields` 실측). 볼트의 익명 `raw/main/README.md` 요청은 *"Access to model briaai/Fibo-2.0-dev is restricted"* 로 거부됐다.
> **Comfy 재패키징은 `gated: False`** — 같은 가중치(카드: *"Weight values are unchanged (bf16)"*)를 양식 없이 받는다.
> ⇒ 📌 CC BY-NC 4.0 은 비상업 재배포를 허용하므로 위법이라고 단정할 근거는 없다(볼트 판단 · 법률 검토 아님). 그러나 **BRIA 가 게이트로 얻으려던 리드 정보(누가·무엇에 쓰는가)는 재패키징 경로에서 사라진다.** [[Comfy-Org-YuE2]] 의 *"재포장이 배포 조건을 바꿀 수 있다"* 의 **접근 조건판**이다.
> 🔴 게이트가 원본 다운로드를 얼마나 억제했는지는 분리 불가 — 15~20배 중 게이트 몫은 **정량화하지 못한다.**

> [!warning] 주의 / 검증 한계
> - 🔴 **비상업 전용**: 카드 *"Commercial use requires a separate agreement with BRIA AI"*. 원본 `license: other` · `license_name: bria-fibo` · 링크는 CC BY-NC 4.0 ⇒ **내 SaaS 에 상업 탑재 불가**(유료 라이선스 별도).
> - **벤치마크 0건(Comfy 카드 전문 기준)**. 원본 카드는 게이트로 **볼트 미열람** — 원본에 수치가 있는지는 모른다.
> - 수집기 클레임 중 *"text encoder Qwen3-VL-4B · FLUX.2 VAE"* 는 **파일명으로만 확인**(`qwen3vl_4b_*`, `flux2-vae`). *"structured caption"* 은 인용 논문 제목(arXiv 2511.06876 *"Generating an Image From 1,000 Words: Enhancing Text-To-Image With Structured Captions"*)으로 확인 — 논문 본문 미열람.
> - **[[파생표기-함정]] 재현**: `cardData.base_model` 은 2개(dev · edit-turbo)인데 **`tags` 에는 `Fibo-2.0-dev` 하나만**, 관계는 `base_model:finetune:`(실제는 재포장 · `base_model_relation` 미설정 기본값) — YuE2 와 같은 패턴.
> - ✅ YuE2 때와 달리 **int8 파일이 문서화됐다**: *"int8 (Hadamard rotation, per-channel scales), adaLN modulation layers kept in bf16. Outputs differ slightly from the original."* — 단 **손실 정량치 없음**.
> - LoRA `fibo_2.0_turbo_lora_avg_rank_270_bf16` 는 폴더 안내 트리에 **빠져 있다**(파일은 실재 · `loras/`).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: T2I(dev) + **이미지 편집(edit-turbo)** 을 한 레포·한 인코더·한 VAE 로 묶음 ⇒ 썸네일 생성 → 부분 수정 파이프라인을 단일 ComfyUI 그래프로 구성 가능. 난이도 낮음(파일 배치만), 스택 = ComfyUI.
- **크리에이터 인사이트**: "긴 프롬프트를 구조화해 정확히 반영"(structured caption 논문) — 수십 개 요소를 지정하는 썸네일·광고 시안 수요와 맞닿음(추정).
- **프롬프트 패턴**: 원본 계열은 JSON 구조 프롬프트를 쓴다(`briaai/FIBO-*-prompt-to-JSON` 레포 다수 실재 · 내용 미열람) ⇒ LLM 으로 자연어→JSON 변환 후 입력하는 2단 구조로 보임(추정).
- **워크플로우**: `models/diffusion_models/` · `text_encoders/` · `vae/` (+ `loras/`) 배치 → Comfy 워크플로우.
- **디자인 레퍼런스**: 해당 없음.
- **경쟁 우위 빈틈**: 인코더 **Qwen3-VL-4B** 는 [[Comfy-Org-MOSS-Image]] 의 Qwen3.5-9B 보다 작다 ⇒ 로컬 VRAM 부담이 낮을 가능성(추정). VAE 는 [[Black-Forest-Labs]] FLUX.2 VAE 공유 — 10월 Comfy 배포 T2I 들이 **FLUX.2 VAE 로 수렴** 중(MOSS·Fibo 2건 관측). 🔴 그러나 **NC 라이선스가 SaaS 채택의 1차 차단 요인**.

> [!action] 당장 할 것 (낮음)
> 비상업 내부 실험(썸네일 시안)으로만 int8 dev + int8 인코더 VRAM 측정. 상업 파이프라인 후보에서는 제외.

## 관련 페이지
- [[Comfy-Org]] · [[ComfyUI]] · [[계수기-배수]] · [[원본-파생-역전]] · [[파생저장소-식별]] · [[파생표기-함정]]
- [[Comfy-Org-MOSS-Image]] — 규약 ⑰ 첫 집행(116.7 → 29~39배) · [[Comfy-Org-YuE2]] — 재포장이 라이선스를 바꾼 사례 · [[Comfy-Org-Qwen-Image-2.1]] · [[flux-3-image-klein-comfy]]
- [[Black-Forest-Labs]] · [[flux-3-image-klein]] — FLUX VAE 계열
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/Comfy-Org/Fibo-2.0 · 원본(게이트) https://huggingface.co/briaai/Fibo-2.0-dev · https://huggingface.co/briaai/Fibo-2.0-edit-turbo
- 볼트 실측(2026-10-26T09:08Z UTC): dl 30d **124,557** / all-time **124,557** / likes **186** ‖ 원본 dev 1,115/1,115/157 · edit-turbo 955/955/121
- 신뢰도: ⭐⭐ (HF 다운로드 124,557 — 파일당 계수 · 사람 단위 추정 3.1만~4.2만)
