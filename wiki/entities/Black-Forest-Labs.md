---
title: Black Forest Labs (BFL) — FLUX 이미지 생성 모델 개발사
type: entity
domain: video-saas
tags: [entity, company, image-generation, flux, bfl, 게이트배포]
created: 2026-10-17
updated: 2026-10-17
sources: [flux-3-image-klein.md, flux-3-image-klein-comfy.md]
reliability: medium
---

# Black Forest Labs (BFL)

**HF 조직**: https://huggingface.co/black-forest-labs
**분류**: 이미지 생성 모델 개발사 (FLUX 계열)
**신뢰도**: ⭐⭐

> [!insight] 핵심 — **API 서비스와 가중치 공개를 동시에 하고, 그 경계를 레포 분리로 그었다**
> 금일 확인된 배포 구조:
>
> | 레포 | 성격 | 다운로드(10-17 실측) |
> |---|---|--:|
> | [[flux-3-image-klein]] | **distilled 원본** — *"BFL API 가 실제로 돌리는 바로 그 체크포인트"* | **46,123** |
> | [[flux-3-image-klein-comfy]] | **ComfyUI 재패키징** | **224,108** |
> | (별도 Base 레포) | 파인튜닝·LoRA 용 | 미확인 |
>
> ⇒ 🎯 **distilled = 추론 전용 / Base = 학습용** 으로 선을 그었다. **"서비스와 같은 체크포인트"를 공개한다는 주장이 이 회사 배포 전략의 핵심 소구점**이다.

## 🔴 금일 관측 — 자사 원본이 재패키징에 4.86배 밀린다

**224,108 / 46,123 = 4.86배.** 수집기 측정 시점에는 3.24배였고 **격차가 벌어지는 방향**이다.
⇒ ⚖️ **BFL 이 만든 원본보다 제3포맷 변환본이 더 많이 당겨간다** — 단 **두 레포 모두 `black-forest-labs` 조직 소유**이므로 **자사가 자사 포맷 변환본을 함께 배포하고 그쪽이 이긴 것**이다.
⇒ 🏆 **함의: 모델사의 유통 전략에서 "포맷 어댑터"가 가중치만큼 중요하다.** → [[배포형태-수요]]

## 제품 (금일 확인분)

**FLUX 3 Klein** — t2i + 이미지 편집
- 이미지 트랜스포머 **5.55B** 실측(`safetensors.total` = 5,548,681,984 · 카드 *"5.6B"* 주장 **검증 통과**)
- 텍스트 인코더 **Qwen3-VL-4B-Instruct 별도** ⇒ 🔴 **자사 인코더가 아니라 Qwen 계열을 쓴다**(의존 관계)
- **참조 이미지 최대 10장 → 1장 반환**
- distilled **16스텝(guidance 없음)** / base **50스텝(guidance 3.5)**
- 양자화 **BF16 / FP8 / int8 / NVFP4**
- ⚠️ 카드 명시: ***"Do not use the model without a prompt upsampler"***

## 🔴 배포 관행 — 게이트 레포

- 두 레포 모두 `gated: auto` ⇒ **조건 동의 필요** · `raw/main/README.md` **HTTP 401**
- 라이선스 `other` 🔴 **상업 사용 가능 여부 미확인**
- 🔴 **벤치마크 수치 0건** — 품질 우위를 수치로 주장하지 않는다 ⇒ 경쟁 비교 불가, **자체 A/B 가 도입 전제**

> [!warning] ⚖️ 게이트의 성격 미확인 — [[LTX-2.5]] 선례 적용 필요
> 2026-10-04 에 볼트는 [[LTX-2.5]] 의 게이트가 `extra_gated_description` 상 *"consent to receive **targeted and personalized advertisements**"* ⇒ **안전 게이트가 아니라 리드 수집 게이트**임을 확정했다.
> 🔴 **BFL 게이트의 동의 조건 전문은 미확인이다** — 같은 유형일 수 있다. **다음 배치 확인 대상.**

> [!question] 미해결
> ① 게이트 동의 조건 전문 미열람 ② 라이선스 `other` 상업 조항 미확인 ③ Base 레포 미확인 ④ FLUX 1/2 세대와의 관계·볼트 보유 이력 미대조 ⑤ 회사 소재·규모·투자 등 기업 정보 **전무**(HF 조직 페이지만 봤다)

## 관련 페이지
- [[flux-3-image-klein]] · [[flux-3-image-klein-comfy]]
- [[Lightricks]] ← 같은 생성모델 배포사 · [[LTX-2.5]] 게이트 선례
- [[Qwen]] ← 텍스트 인코더 의존
- [[배포형태-수요]] · [[스타-근거-비동행]]
