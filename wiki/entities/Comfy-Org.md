---
title: Comfy-Org
type: entity
domain: ai-news
tags: [entity, huggingface, comfyui, repackage, distribution, runtime]
created: 2026-09-17
updated: 2026-09-24
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

---

## 🔄 2026-09-24 갱신 — **본체 레포가 이 조직으로 이관됐다 (문서는 절반만)**

볼트 실측: `comfyanonymous/ComfyUI` → **HTTP 301** → **`Comfy-Org/ComfyUI`**(레포 ID **589831718**, ★**134,790**, GPL-3.0).
🎯 **볼트가 이 조직의 재포장본을 세 번 추적하는 동안 본체가 이 조직으로 넘어왔다.** [[ComfyUI]] 페이지는 2026-08-11부터 있었으나 **구 이름(`comfyanonymous`)으로 적혀 있었고**, 그 때문에 09-24 수집기 중복 검사를 통과해 *"본체 누락"* 으로 재배달됐다 → 신설 개념 [[정규명-우선-중복검사]]

### 🔴 이관이 문서에서 절반만 끝났다 (README 437행 실측)
`## Release Process`(90행)의 3레포 중 **본체만 구 이름**이다:
1. **ComfyUI Core → `comfyanonymous/ComfyUI`** 🔴
2. Comfy Desktop → `Comfy-Org/Comfy-Desktop` ✅
3. ComfyUI Frontend → `Comfy-Org/ComfyUI_frontend` ✅
배지·릴리스·예제 링크(27~32·62행)도 전부 구 이름. 📌 **위성은 넘어왔고 본체 표기만 남았다.**

### 🎯 이 조직의 위상이 수치로 확인됐다
| 저장소 | DL(창=누적) | 좋아요 | trendingScore |
|---|---|---|---|
| `Qwen/Qwen-Image-2.1` (원본) | 28,407 | **2,097** | **1,970** |
| **`Comfy-Org/Qwen-Image-2.1`** | **2,220,609** | 648 | 622 |

**재포장이 원본의 78.17배.** 🎯 **이 조직은 모델을 만들지 않지만 모델 소비의 관문이다** — 그리고 이제 그 관문의 **런타임 본체까지 보유한다**(Core + Desktop + Frontend + 재포장 배포).
🔴 단 **주목은 원본에 남는다**(좋아요 3.24배 · trendingScore 3.17배) → [[원본-파생-역전]]

⬜ 미확인: 법인 실체·comfyanonymous 개인과의 관계·이관 시점·거버넌스 구조 **전부 미확인**.

## 🔗 추가 관련 페이지 *(2026-09-24)*
- [[ComfyUI]] — 이관된 본체(도메인 `video-saas` 재판정)
- [[정규명-우선-중복검사]] · [[파생저장소-식별]] · [[원본-파생-역전]]
