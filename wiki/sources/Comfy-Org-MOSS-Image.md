---
title: "Comfy-Org/MOSS-Image — 생성 9일에 194만 다운로드. 원본 2레포 합의 116.7배이고, 그 대부분은 계수기 차이다"
type: source
domain: video-saas
tags: [video-saas, hf-model, comfyui, text-to-image, repackage, diffusion-single-file, 계수기-배수, 원본-파생-역전, qwen3.5, flux2-vae]
created: 2026-10-25
updated: 2026-10-25
sources: [Comfy-Org-Qwen-Image-2.1.md, flux-3-image-klein-comfy.md]
reliability: medium
---

# Comfy-Org/MOSS-Image

**HF**: https://huggingface.co/Comfy-Org/MOSS-Image · 재패키징 [[Comfy-Org]] · 원본 [[OpenMOSS]] (`OpenMOSS-Team/MOSS-Image-Base` · `-SFT`) + LoRA `darask0/MOSS-Image-color-depth-control`
**실측(2026-10-25 KST · HF API)**: downloads **1,944,278**(수집기 일치) · likes **443** · createdAt **2026-10-16** · `library_name` **`diffusion-single-file`** · apache-2.0 · 파일 12개(`.safetensors` **10**)
**도메인 재분류**: 수집기 `ai-news` → **`video-saas`**(이미지 생성 · ComfyUI 워크플로우)
**신뢰도**: ⭐⭐ (다운로드 지표 해석 불가 수준으로 부풀어 있음 · 벤치 0건)

> [!insight] 🏆 핵심 인사이트 — **규약 ⑰(10-24 신설) 첫 집행: 배수 116.7 는 수요 배수가 아니다**
> - 원본 실측: `MOSS-Image-Base` **6,943** · `MOSS-Image-SFT` **9,717** (둘 다 `library_name: diffusers`) ⇒ 합 **16,660**
> - Comfy 재패키징 **1,944,278** ⇒ **116.7배**
> - 🔴 그러나 `diffusion-single-file` 은 **`.safetensors` 파일 요청마다 1회 계수**([[계수기-배수]] 규칙 출처) · diffusers 는 이중계수 방지 필터.
> - **1인당 파일 수 환산**: 최소 워크플로우 = diffusion 1 + text_encoder 1 + VAE 1 = **3파일**(LoRA 사용 시 4) ⇒ 사람 단위 추정 **약 48.6만~64.8만** ⇒ 원본 대비 **29~39배**(추정).
> ⇒ 🎯 **보정해도 역전은 남는다** — [[원본-파생-역전]] 은 성립하지만 크기는 1/3~1/4 로 줄어든다. 수집기의 *"다운로드 집계 부풀림 가능성 확인 필요"* 는 정확했고, 볼트가 계수 규칙으로 정량화했다.
> 🎯 **좋아요는 반대로 간다**(원본-파생-역전 09-20 관측 재현): 원본 Base 543 + SFT 704 = **1,247** > Comfy **443**.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 자연어·태그·**JSON 레이아웃(bbox)** 로 텍스트·객체 배치 제어 — Comfy 워크플로우 템플릿 4종 중 2종이 *"Layout-Guided Text to Image"* ⇒ 썸네일·카드뉴스 자동 레이아웃에 직결
- **크리에이터 인사이트**: 배치 제어 수요(텍스트를 원하는 위치에) — 기존 T2I 의 약점
- **프롬프트 패턴**: JSON 레이아웃 입력(원본 카드 기준 · 미열람)
- **워크플로우**: ComfyUI `models/` 아래 4폴더 배치 → 공식 템플릿 JSON 로드
- **디자인 레퍼런스**: 해당 없음
- **경쟁 우위 빈틈**: 텍스트 인코더 = **Qwen3.5-9B**(int8 · w4a8 GPTQ 제공) · VAE = **FLUX.2 VAE** ⇒ 9B 인코더가 로컬 VRAM 병목(볼트 추정)

> [!warning] 벤치마크 0건
> Comfy 카드·원본 Base 카드 모두 정량 수치 없음(수집기 보고 · 볼트는 Comfy 카드 전문 확인). → [[벤치마크-이미지-봉인]] 이 아니라 **② 부재(카드 전문 기준)**.

> [!action] 당장 할 것
> reat-slides / 썸네일 파이프라인에서 **bbox 레이아웃 T2I** 1회 시험 — int8 diffusion + w4a8 인코더 조합으로 VRAM 측정.

## 관련 페이지
- [[계수기-배수]] · [[원본-파생-역전]] · [[파생저장소-식별]] · [[Comfy-Org]] · [[OpenMOSS]] · [[ComfyUI]]
- [[Comfy-Org-Qwen-Image-2.1]] · [[flux-3-image-klein-comfy]] — 같은 계수기 사례
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/Comfy-Org/MOSS-Image
- 신뢰도: ⭐⭐ (HF 다운로드 1,944,278 — 파일당 계수)
