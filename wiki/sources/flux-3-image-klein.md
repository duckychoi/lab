---
title: black-forest-labs/flux-3-image-klein — FLUX 3 Klein distilled 원본 (5.55B 실측)
type: source
domain: video-saas
tags: [video-saas, image-generation, flux, distilled, t2i, image-edit, gated, bfl]
created: 2026-10-17
updated: 2026-10-17
sources: []
reliability: medium
---

# black-forest-labs/flux-3-image-klein

**HF**: https://huggingface.co/black-forest-labs/flux-3-image-klein
**다운로드**: **46,123** (2026-10-17T09:12Z 실측 · 🔴 수집기 **22,790** 대비 **2.02배** — 수 시간 만의 실제 증가로 보이나 **구간 미확정**)
**likes** 417 · **trendingScore 391** · pipeline `image-to-image` · gated `auto` · lastModified 2026-10-16T04:58Z
**파라미터**: 🏆 **5,548,681,984 = 5.55B** (`safetensors.total` 실측 — raw.md 의 "5.6B" 주장 **검증 통과**)
**신뢰도**: ⭐⭐

> [!insight] 핵심 인사이트 — **BFL API 가 실제로 돌리는 그 체크포인트**
> 이 레포는 ComfyUI 재패키징([[flux-3-image-klein-comfy]])의 **원본 distilled 체크포인트**이고, 카드에 따르면 **BFL API 가 서비스에 쓰는 것과 동일**하다. BF16·FP8·NVFP4 트랜스포머 + 텍스트 인코더 + 오토인코더를 포함한다.
> 파인튜닝·LoRA 용도는 **별도 Base 레포**로 분리돼 있다 ⇒ **distilled = 추론 전용 배포**라는 선이 그어져 있다.

> [!warning] 🔴 분포가 뒤집혀 있다 — 재패키징이 원본을 4.86배 앞선다
> | 레포 | 다운로드(10-17 실측) | 수집기 측정 | 배수 변화 |
> |---|--:|--:|--:|
> | [[flux-3-image-klein-comfy]] (ComfyUI 재패키징) | **224,108** | 73,767 | — |
> | **flux-3-image-klein** (원본) | **46,123** | 22,790 | — |
> | **비(comfy/원본)** | **4.86배** | 3.24배 | 🔴 **+1.62 상승** |
>
> ⇒ 🎯 **원본보다 포맷 변환본이 더 많이 당겨간다.** 수집기는 3.24배로 측정했고 볼트 실측은 **4.86배**다 ⇒ **격차가 벌어지는 방향**이다(같은 날 수 시간 간격).
> ⇒ ⚖️ **해석**: 모델의 가치가 가중치가 아니라 **실행 가능한 형태**에 있다. 이는 [[선언된-구현체-공백]] 의 반대편 현상이다 — 구현체가 있는 쪽이 아니라 **바로 돌아가는 쪽**이 수요를 가진다.
> 🔴 **단 구간 미확정이다** — 수집기 관측 시각이 raw.md 에 없어 증분을 시간으로 나눌 수 없다. **10-15 볼트 요청(관측 시각 병기)이 수집기 측에서 또 미이행됐다.**

> [!note] 🆕 메타규약 적용 — `downloadsAllTime` 은 부재가 아니라 기본 미포함이었다
> 기본 `GET /api/models/{id}` 응답에서 `downloadsAllTime` 이 **0** 으로 보였다.
> 🔴 **"집계 결측"으로 적기 전에 같은 자원의 다른 표현을 1회 봤다**: `?expand[]=downloadsAllTime` → **46,123** 반환(dl30 과 동일 = 신규 모델이라 전구간 ≈ 30일 구간).
> ⇒ ✅ **[[메타데이터-부재-추론]] 오판 1건을 사전 차단했다.** 📌 같은 호출에서 [[Unlimited-OCR]] 은 dlAll **9,338,622** vs dl30 1,476,672 = **6.32배** ⇒ 필드는 정상 작동하며 **기본 응답에서 빠질 뿐**이다.
> 🆕 **규약 ⑭ 신설 제안: HF 모델 수치는 `expand[]` 로 1회 더 요청한다. 기본 응답의 0 은 값이 아니라 미포함이다.**

## 도메인별 추출 (video-saas 템플릿)

- **기능 벤치마킹**: t2i + 이미지 편집(참조 최대 10장 → 1장 반환)을 5.55B 로 수행. 내 SaaS 에 올리려면 **BF16 기준 VRAM 약 11GB+**(5.55B × 2B/param) 이고 FP8·NVFP4 로 내릴 선택지가 동봉돼 있다 ⇒ **단일 소비자 GPU 배포가 사정권**이다.
- **프롬프트 패턴**: ⚠️ 카드가 못박았다 — ***"Do not use the model without a prompt upsampler"***. 짧은 프롬프트는 일반적(generic) 출력을 낸다. 🎯 **즉 프롬프트 업샘플러가 선택이 아니라 필수 구성요소다** ⇒ 내 파이프라인에 올릴 때 **LLM 기반 프롬프트 확장 단계를 반드시 앞에 둬야 한다**.
- **디자인 레퍼런스**: distilled **16스텝(guidance 없음)** / base **50스텝(guidance 3.5)** 두 구성 ⇒ 품질·지연 트레이드오프를 스텝수로 노출한다.
- **경쟁 우위 빈틈**: 🔴 **벤치마크 수치 0건**(카드) ⇒ 품질 우위를 수치로 주장하지 않는다. 경쟁 비교가 불가능하므로 **자체 A/B 가 도입 전제**다.
- **워크플로우**: 게이트 레포(`gated: auto` — 조건 동의 필요). 🔴 `raw/main/README.md` **HTTP 401** ⇒ 볼트 규약 ⑬대로 **HTML 1회 열어 사양 확보**(수집기 집행분).

> [!question] 미해결
> ① 게이트 동의 조건 전문 미확인 — [[LTX-2.5]] 사례처럼 **"안전 게이트"가 아니라 리드 수집 게이트**일 수 있다(10-04 확정 사례 존재).
> ② 라이선스 `other` — FLUX 계열 비상업 조항 여부 미확인. **상업 사용 판단 불가.**
> ③ 수집기 관측 시각 부재로 다운로드 증분 구간 미확정.

## 관련 페이지
- [[flux-3-image-klein-comfy]] ← 같은 모델의 ComfyUI 배포물 (4.86배 수요)
- [[선언된-구현체-공백]] ← 반대편 현상
- [[메타데이터-부재-추론]] ← `expand[]` 로 오판 차단
- [[LTX-2.5]] ← 게이트 레포 선례
- [[캐시된-지표-신선도]]

## 원본
- 출처: https://huggingface.co/black-forest-labs/flux-3-image-klein
- 열어 본 것: HF API 기본 + `?expand[]=downloadsAllTime,downloads,trendingScore,likes,gated,safetensors`
- 관측: 2026-10-17T09:12Z (18:12 KST)
- 신뢰도: ⭐⭐ (벤치마크 0건 · 게이트 조건·라이선스 미확인)
