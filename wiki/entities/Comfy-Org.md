---
title: Comfy-Org
type: entity
domain: ai-news
tags: [entity, huggingface, comfyui, repackage, distribution, runtime]
created: 2026-09-17
updated: 2026-09-17
sources: [Comfy-Org-YuE2.md]
reliability: medium
---

# Comfy-Org

ComfyUI 생태계의 공식 조직. **모델을 만들지 않고 런타임에 맞게 재포장(repackage)한다.**

> [!insight] 구조적 위치 — 런타임 적응층
> [[Comfy-Org-YuE2]](DL 59,231)의 카드 본문은 한 문장이다: *"**Repackaged model files for ComfyUI.**"*
> 🎯 **새 가중치가 아니라 배치 경로다** — 원본([[m-a-p]] 의 [[YuE2-3B]]·SheetSage2)을 ComfyUI의 `models/checkpoints/`·`models/audio_encoders/` 구조에 맞춰 다시 담는다.
> 📌 [[Vercel]] 이 스킬 배급층을 가져간 것과 **같은 종류의 자리**다 — 생성하지 않고 **설치 가능하게 만드는 층**.
> ✅ **파생 관계를 숨기지 않는다** — 원본 저장소 링크를 카드 본문에 직접 적었다.

> [!warning] 🔴 볼트가 찾은 문제 3건 (09-17)
> 1. **채택 근거였던 `int8_convrot` 파일이 미문서화** — 파일은 실재하나 **배치 위치·의미·손실이 카드에 없다.** 배치 안내는 bf16 2개만
> 2. **`tags` 에 [[YuE2-3B]] 가 빠졌다** — `cardData.base_model` 에는 있는데 태그 배열에는 SheetSage2만. 🔴 게다가 라벨이 `finetune` 인데 **실제는 재포장** → [[파생표기-함정]] 5번째 사례
> 3. **라이선스가 갈린다** — 이 레포는 **CC-BY-NC-4.0(비상업)**. 🎯 **재포장이 배포 조건을 바꿀 수 있다**는 실무적으로 중요한 사례
> ⚠️ 생성(2026-09-11) 후 **미수정** — int8 안내 누락이 방치된 상태.

> [!note] 볼트 판정
> [[Comfy-Org-YuE2]] 는 **(b) 파생 축 독립 채택 → (c) 원본 병합**으로 정정됐다. 판정 절차는 [[파생저장소-식별]].
> 🎯 조직 자체의 신뢰도는 **medium** — ComfyUI 공식이고 관계를 명시하나, **카드 품질이 얇고(29행) 성능 수치가 없다.**

## 관련 페이지
- [[Comfy-Org-YuE2]] — 제작물 · [[YuE2-3B]] · [[m-a-p]] — 원본
- [[파생저장소-식별]] — 🎯 판정 근거 · [[파생표기-함정]] — 5번째 사례
- [[Vercel]] — 같은 종류의 배급층 · [[메타데이터-부재-추론]] · [[HuggingFace]] · [[ai-news]]
