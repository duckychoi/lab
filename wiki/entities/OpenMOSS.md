---
title: OpenMOSS
type: entity
domain: video-saas
tags: [video-saas, text-to-image, research-lab, hf, moss]
created: 2026-10-25
updated: 2026-10-26
sources: [Comfy-Org-MOSS-Image.md]
reliability: low
---

# OpenMOSS

HF `OpenMOSS-Team`. 텍스트-투-이미지 모델 **MOSS-Image**(Base · SFT) 원본 발행. ⬜ **소속(대학·기업)은 볼트가 직접 확인하지 않았다.**

> [!insight] 🎯 볼트 보유 1건 — **원본은 1.7만, 재패키징은 194만**
> 원본 `MOSS-Image-Base` 6,943 + `-SFT` 9,717 = **16,660**(diffusers) ↔ [[Comfy-Org]] 재패키징 **1,944,278**(diffusion-single-file · 파일당 계수) ⇒ 원값 116.7배 · 1인당 환산 29~39배(추정). 🎯 **좋아요는 원본이 많다**(1,247 vs 443). → [[Comfy-Org-MOSS-Image]] · [[계수기-배수]] · [[원본-파생-역전]]

## 관련 페이지
- [[Comfy-Org-MOSS-Image]] · [[Comfy-Org]] · [[ComfyUI]]
- [[video-saas]]

## 🔄 2026-10-26 — 파생 생태계 확장: [[Kromoss]]
- lodestones/[[Kromoss]](MOSS-Image-Base 풀 파인튜닝 · Apache-2.0) dl **23,972** = SFT(10,757) 대비 **2.23배** · Base+SFT 합(18,398) 대비 1.31배 — 🎯 **양쪽 다 diffusers 라 계수 단위가 거의 같다**(⑰ 보정 불필요). 좋아요는 원본 우위(SFT 735 · Base 557 vs 263).
- 원본 증가(10-25 → 10-26): SFT 9,717 → **10,757** · Base 6,943 → **7,641** · [[Comfy-Org-MOSS-Image]] 1,944,278 → 2,161,961.
- ⚖️ 수집기 요청 판정: `MOSS-Image-SFT` 단독 소스 페이지는 만들지 않는다 — 이 엔티티와 [[Comfy-Org-MOSS-Image]] 가 원본으로 이미 추적 중 ⇒ [[파생저장소-식별]] (c) 병합.
