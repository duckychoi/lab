---
title: black-forest-labs/flux-3-image-klein-comfy — ComfyUI 재패키징이 원본을 4.86배 앞선다
type: source
domain: video-saas
tags: [video-saas, image-generation, flux, comfyui, repackaging, t2i, image-edit, gated, 배포형태수요, 계수기-배수]
created: 2026-10-17
updated: 2026-11-04
sources: []
reliability: medium
---

# black-forest-labs/flux-3-image-klein-comfy

**HF**: https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy
**다운로드**: **224,108** (2026-10-17T09:12Z 실측 · 🔴 수집기 **73,767** 대비 **3.04배** · 구간 미확정)
**likes** 520 · **trendingScore 447**(금일 수집 3모델 중 최고) · pipeline `image-to-image` · gated `auto` · lastModified **2026-10-17T07:10Z**(활발한 갱신 중)
**신뢰도**: ⭐⭐

> [!insight] 🏆 핵심 인사이트 — **가중치가 아니라 "바로 돌아가는 형태"가 수요를 가진다**
> 이 레포는 [[flux-3-image-klein]] 원본 distilled 체크포인트를 **ComfyUI 용으로 재패키징**한 것이다. 모델은 같다. 포맷만 다르다.
> 🔴 **그런데 다운로드가 원본의 4.86배다**(224,108 vs 46,123).
> ⇒ 🎯 **같은 가중치에 대해 "ComfyUI 에 넣으면 그냥 돈다"는 속성이 4.86배의 수요 차이를 만든다.** 재패키징은 기술 기여가 아니라 **마찰 제거**인데, 측정되는 수요는 마찰 제거 쪽이 압도한다.
> ⇒ 📌 **내 SaaS 함의**: 모델 품질 경쟁과 별개로 **"사용자의 기존 파이프라인에 그대로 꽂히는가"가 독립 변수**다. 이 배수가 그 변수의 크기를 처음으로 수치화해 준다.

## 🔴 배수가 벌어지고 있다 — 수집기 3.24배 → 볼트 4.86배

| 레포 | 수집기 측정 | **볼트 실측 (10-17T09:12Z)** | 증가 |
|---|--:|--:|--:|
| **comfy (재패키징)** | 73,767 | **224,108** | **+150,341 (3.04배)** |
| 원본 ([[flux-3-image-klein]]) | 22,790 | **46,123** | +23,333 (2.02배) |
| **비(comfy/원본)** | 3.24배 | **4.86배** | 🔴 **+1.62** |

⇒ ⚖️ **두 레포가 같은 날 같은 모델인데 증가율이 3.04배 vs 2.02배로 다르다** ⇒ 재패키징 쪽이 **더 빨리** 당겨간다. 분포 격차가 수렴이 아니라 **확대**다.
> [!warning] 🔴 단 구간이 미확정이다
> 수집기가 **관측 시각을 raw.md 에 적지 않았다**(10-15 볼트 요청 미이행 · 재발). 따라서 위 증분을 시간으로 나눌 수 없고 **"수 시간"이 몇 시간인지 모른다** ⇒ **일평균·시간당 증분을 쓸 수 없다.** 방향(확대)만 확정이다.

## 사양 (게이트 우회 경로로 확보 — 규약 ⑬)

- 이미지 트랜스포머 **5.6B** 급(원본 실측 5,548,681,984 = **5.55B**) · 텍스트 인코더 **Qwen3-VL-4B-Instruct 별도**
- **참조 이미지 최대 10장 → 1장 반환**
- **distilled 16스텝(guidance 없음)** / **base 50스텝(guidance 3.5)** 두 구성 동봉
- 양자화 **BF16 / int8 / NVFP4**
- ⚠️ ***"Do not use the model without a prompt upsampler"*** — 짧은 프롬프트는 일반적 출력
- 🔴 `gated: auto` ⇒ `raw/main/README.md` **HTTP 401** → **HTML 본문 1회 열어 사양 확보**(볼트 규약 ⑬ 집행 · 수집기 수행)
- 🔴 `safetensors.total` **미반환** — 다중 양자화 배포라 단일 파라미터 수가 집계되지 않는다(원본 레포에서 확보)

## 도메인별 추출 (video-saas 템플릿)

- **기능 벤치마킹**: ComfyUI 노드로 바로 t2i + 10장 참조 편집. 🎯 **내 SaaS 가 ComfyUI 백엔드를 쓰면 통합 비용이 거의 0** 이다 — 그게 이 레포의 존재 이유다.
- **크리에이터 인사이트**: 🏆 **4.86배가 바로 그 갭의 측정값이다** — 크리에이터가 원하는 것은 *최신 가중치*가 아니라 *지금 내 그래프에 꽂히는 노드*다.
- **프롬프트 패턴**: 프롬프트 업샘플러 **필수**(카드 명시). 16스텝 distilled 는 guidance 를 안 받으므로 **품질 제어 손잡이가 프롬프트 쪽으로 전부 이동**한다 ⇒ 업샘플러 품질이 최종 품질을 지배한다.
- **디자인 레퍼런스**: 16스텝 ↔ 50스텝 2구성 = **프리뷰/최종 2단 렌더 파이프라인**을 그대로 설계할 수 있다.
- **경쟁 우위 빈틈**: 🔴 **벤치마크 수치 0건** ⇒ 품질 비교 불가. 🏆 **빈틈은 모델이 아니라 유통에 있다** — 원본이 재패키징에 4.86배 밀리는 구조라면, **포맷 어댑터를 먼저 내는 쪽이 수요를 가진다**.
- **액션**: ComfyUI 환경에 int8 또는 NVFP4 변형 1개 내려서 **16스텝 distilled 의 프롬프트 업샘플러 유무 A/B** — 카드 경고가 실제로 얼마나 큰 차이인지 자체 측정. 우선순위 중간.

> [!question] 미해결
> ① 게이트 동의 조건 전문 미확인(리드 수집형 여부 — [[LTX-2.5]] 선례).
> ② 라이선스 `other` 상업 사용 가능 여부 **미확인**.
> ③ 🔴 **4.86배의 분모 해석 주의** — 재패키징 레포는 양자화 변형이 여러 개라 **파일 단위 다운로드가 중복 계수될 수 있다**. HF 다운로드 집계 단위(레포 단위 vs 파일 단위) **미확인** ⇒ 배수가 과대일 가능성을 배제하지 못한다.

## 관련 페이지
- [[flux-3-image-klein]] ← 원본 distilled 체크포인트
- [[선언된-구현체-공백]] ← 반대편 현상(구현체 없는 선언)
- [[계수기-배수]]
- [[LTX-2.5]] ← 게이트 레포 선례
- [[캐시된-지표-신선도]]

## 원본
- 출처: https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy
- 열어 본 것: HF API 기본 + `?expand[]=...`(volt) · 사양은 수집기 HTML 1회 열람분 인용
- 관측: 2026-10-17T09:12Z (18:12 KST)
- 신뢰도: ⭐⭐ (벤치마크 0건 · 집계 단위 미확인 · 라이선스 미확인)

## 🔄 2026-10-24 재수집 업데이트

> [!warning] 🏆🔴 **10-17 핵심 인사이트("마찰 제거가 4.86배 수요를 만든다")를 철회한다 — 배수의 대부분은 계수기 단위 차이다**
> 10-17 의 미해결 ③(*"집계 단위 레포 vs 파일 미확인"*)을 **공식 문서 + 계수 규칙 소스 + 파일 트리**로 해소했다.
> - 이 레포의 `library_name` = **`diffusion-single-file`** (API 실측). `huggingface.js/packages/tasks/src/model-libraries.ts` 의 해당 항목: **`countDownloads: path_extension:"safetensors"`** ⇒ **`.safetensors` 파일 하나하나에 대한 GET/HEAD 가 각각 1 다운로드**다.
> - 레포 트리 실측: `.safetensors` **12개**(diffusion_models 6 · text_encoders 5 · vae 1).
> - 🎯 **카드가 직접 권하는 다운로드 명령이 파일 4개를 받는다** — `diffusion_models/…int8-convrot` + `text_encoders/qwen3vl_4b_int8_convrot` + `vae/flux2-vae` + `text_encoders/qwen3.5_9b_flux3_prompt_upsampler_int8_convrot`. ⇒ **ComfyUI 사용자 1명 = 다운로드 4회**(업샘플러 생략 시 3회).
> - 반면 원본 [[flux-3-image-klein]] 은 `diffusers` 이며, `hub-docs/models-download-stats.md` 의 diffusers 필터는 `model_index.json`·`modular_model_index.json` + **최상위** `*.safetensors` 만 센다(하위 폴더 가중치 제외 = 이중계수 방지 설계). ⇒ diffusers 로 로드하는 사용자 1명 ≈ **1회**(수동으로 최상위 `model.safetensors`+`ae.safetensors` 를 받으면 2회).
> ⇒ ⚖️ **두 레포의 다운로드는 다른 단위로 센 수다.** 원(raw) 배수 5.06배는 *"사람 수 비"* 가 아니라 *"요청 수 비"* 다 → 신설 [[계수기-배수]] (짝: [[구조적-영값]]).

### 실측 (2026-10-24T09:06Z · 18:06 KST · `expand[]` 사용 — 규약 ⑭)

| 레포 | 10-17T09:12Z (볼트) | **10-24T09:06Z (볼트)** | 배수 | 일평균(≈7.0일) | 수집기(금일) |
|---|--:|--:|--:|--:|--:|
| **comfy** (`diffusion-single-file`) | 224,108 | **534,837** | ×2.39 | ≈44,400/일 | 534,837 ✅ 일치 |
| 원본 klein (`diffusers`) | 46,123 | **105,768** | ×2.29 | ≈8,520/일 | 105,768 ✅ 일치 |
| 🆕 klein-base (`diffusers`) | — | **106,650** | — | — | (미수집) |
| 🆕 klein-pup 업샘플러 (`transformers`) | — | **43,391** | — | — | (미수집) |

- likes comfy 520 → **1,436**(×2.76) · 원본 417 → 660(×1.58) · trendingScore comfy 447 → **603** / 원본 391 → 181
- `downloads == downloadsAllTime`(양쪽) — 생성 10-13/10-14 로 **30일 창 이내** → [[지표-창길이]]
- comfy `lastModified` **10-17T07:10Z** 에서 멈춤(10-17 이후 무변경)
- 원(raw) 배수: 3.24 (수집기 10-17) → 4.86 (볼트 10-17) → **5.06 (10-24)** · 구간 증분 비 310,729 / 59,645 = **5.21**

### 🎯 배수 재계산 — 단위를 맞추면 순서가 뒤집힐 수 있다

1. **분모를 바로잡는다**: 카드 원문 *"The original model repositories are FLUX 3 Image Klein, FLUX 3 Image Klein Base and FLUX 3 Image Klein Prompt Upsampler"* · `cardData.base_model` 에도 **3개 레포**가 나열된다. ⇒ comfy 는 원본 1개가 아니라 **3개 레포의 묶음**이다. 원본 패밀리 합 = 105,768 + 106,650 + 43,391 = **255,809** ⇒ 원 배수 **2.09배**(5.06배 아님).
2. **분자를 사람 단위로 환산(추정)**: 권장 명령 기준 4파일/인 → 534,837 ÷ 4 ≈ **133,700**, 3파일/인 → ≈ **178,300**.
3. 결과(전부 추정 · 원본 측 1회/인 가정):
   - vs 원본 klein 단독: **약 1.26~1.69배**
   - vs 원본 패밀리 합: **약 0.52~0.70배** ⇒ 🔴 **패밀리 기준으로는 comfy 가 오히려 작을 수 있다.**
> [!warning] 추정의 한계
> 사용자별 실제 파일 수(BF16 1개만 받는 사람, 여러 정밀도를 받는 사람, 재다운로드)는 **관측 불가**다. 원본 측도 diffusers 로드(1회)와 수동 최상위 파일 다운로드(2회)가 섞여 있다. ⇒ **사람 단위 배수는 이 범위 밖일 수도 있다.** 확정 가능한 것은 *"5.06배는 동일 단위 비교가 아니다"* 하나뿐이다. 사람 단위 수치는 HF Publisher Analytics(조직 전용 원시 로그)로만 나온다 — 볼트는 접근 불가.

> [!insight] 🏆 바뀐 인사이트 — **"배포 형태가 수요를 만든다"가 아니라 "배포 형태가 계수기를 바꾼다"**
> 10-17 의 *"마찰 제거 쪽이 4.86배 압도"* 는 **단위가 다른 두 계수기의 비**였다. 남는 신호는 약하다: 단위를 대충 맞춰도 comfy 가 klein 단독보다 **1.3~1.7배** 정도일 *수* 있다는 것 — 그러나 패밀리 기준이면 역전된다. ⇒ 📌 **내 SaaS 함의 수정**: *"ComfyUI 노드로 내면 5배 수요"* 는 **근거 없음**. 배포 형태 전략의 근거로 HF 다운로드 비를 쓰지 않는다.
> ⇒ 🔴 **볼트 파급**: 같은 `diffusion-single-file` 규칙이 [[Comfy-Org-Qwen-Image-2.1]] 에도 적용된다(API 실측: `library_name` = diffusion-single-file · `.safetensors` **15개**). [[원본-파생-역전]] 의 Comfy 분기 배수(69~82배)도 **같은 단위 문제를 안고 있다** — 해당 페이지에 경고를 달았다.

### 10-17 미해결 항목 상태
- ① 게이트 동의 조건 전문 — ⬜ **여전히 미확인**(`raw/main/README.md` **HTTP 401** 재확인 · 규약 ⑬대로 HTML 1회 열람, 본문 공개 부분에서 게이트 조건 전문은 안 보임)
- ② 라이선스 — 🟡 **부분 해소**: `cardData.license_name` = **`flux-kommunity-license`** · 카드 본문 *"permits non-commercial use and provides a commercial-output exception for Qualifying Users, subject to its terms"*. ⇒ **비상업 기본 + "Qualifying Users" 상업 출력 예외**. Qualifying User 의 정의(매출 한도 등)는 LICENSE.md 가 게이트 뒤라 **미확인**.
- ③ 집계 단위 — ✅ **해소**(위)

### HTML 1회 열람으로 새로 확보한 사양 (규약 ⑬)
- 🆕 **프롬프트 업샘플러 = Qwen3.5-9B 파생**(`qwen3.5_9b_flux3_prompt_upsampler_*` · BF16 18.8GB / int8 9.8GB / w4a8 6.7GB) — 워크플로가 **기본으로 업샘플러를 켠다**. 10-17 *"업샘플러 품질이 최종 품질을 지배"* 가 배포물 설계로 확인됨.
- 🆕 **바운딩 박스 프롬프트**: 0~1000 그리드로 요소 배치·재색·이동·제거(하드 마스크 아님)
- 🆕 int8 파일은 **8GB GPU(RTX 3070) · FP8 미지원 GPU(RTX 30 이하)** 에서 동작 · NVFP4 는 **Blackwell 필요**
- 🆕 *"BF16 트랜스포머와 오토인코더는 원본의 `model.safetensors`·`ae.safetensors` 와 같은 파일"* ⇒ **가중치 동일성 공식 확인**
- 🆕 워크플로 JSON 12개(t2i / i2i / multi-image i2i × base·distilled × bf16·int8)

> [!action] 액션 후보
> - (중간) 8GB GPU 에서 int8 distilled + int8 업샘플러 워크플로로 **업샘플러 ON/OFF A/B** — 10-17 항목 유지, 하드웨어 조건(8GB) 확정으로 실행 장벽 낮아짐
> - (낮음) 다운로드 비교 시 `library_name` 과 `countDownloads` 규칙을 먼저 확인하는 절차를 [[계수기-배수]] 에 규약화(볼트 내부)

> [!question] 남은 미해결
> ① FLUX Kommunity License 의 "Qualifying User" 정의 ② 게이트 동의 조건 ③ 사람 단위 다운로드(접근 불가 데이터) ④ 벤치마크 수치 **여전히 0건**

### 관련 페이지 (추가)
- [[계수기-배수]] · [[구조적-영값]] · [[원본-파생-역전]] · [[파생저장소-식별]] · [[컨테이너-중복]] · [[지표-창길이]]
- [[Comfy-Org-Qwen-Image-2.1]] · [[Comfy-Org]] · [[ComfyUI]] · [[Black-Forest-Labs]] · [[Qwen]]

### 원본 (10-24)
- HF API `?expand[]=downloads,downloadsAllTime,likes,createdAt,lastModified,cardData,gated,safetensors` (klein-comfy / klein / klein-base / klein-pup)
- `api/models/…/tree/main?recursive=true` (comfy · klein)
- https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/src/model-libraries.ts (`diffusion-single-file` 항목)
- https://github.com/huggingface/hub-docs/blob/main/docs/hub/models-download-stats.md (diffusers 필터)
- 모델 페이지 HTML 1회(README raw 401)
- 관측: 2026-10-24T09:06Z (18:06 KST)

## 🔄 2026-10-27 갱신 (인제스트 2026-10-27) — **3일 만에 원본 대비 배수 5.06 → 5.88. 구간 증분 비는 12.4배**

**HF API 실측(2026-10-27T09:05Z · expand)**: comfy `downloads` **700,652**(수집기 **정확히 일치**) = all-time(30일 창 이내 지속) · likes **1,723**(수집기 일치) · `lastModified` 10-17T07:10Z(10일 무변경) · 원본 [[flux-3-image-klein]] **119,172** · likes 728

| 레포 | 10-24T09:06Z | **10-27T09:05Z** | 3일 증분 | 일평균 |
|---|--:|--:|--:|--:|
| **comfy** | 534,837 | **700,652** | +165,815 | ≈55,300 |
| 원본 klein | 105,768 | **119,172** | +13,404 | ≈4,470 |

- 원(raw) 배수: 4.86(10-17) → 5.06(10-24) → **5.88(10-27)** · 구간 증분 비 5.21 → **12.4** ⇒ **역전 폭이 가속**. 원본 일평균은 10-17~24 의 8,520 → **4,470 으로 반감**, comfy 는 44,400 → 55,300 으로 증가.
- ⚖️ 10-24 볼트 지적 유지: comfy(`diffusion-single-file`)와 원본(`diffusers`)은 **계수 규칙이 달라** 배수를 사용자 수 비로 읽으면 안 된다 → [[계수기-배수]] · [[원본-파생-역전]]. 단 **같은 규칙 안의 시계열 변화**(원본 반감 · comfy 증가)는 규칙 차이로 설명되지 않는다 ⇒ **수요가 ComfyUI 패키지로 실제 이동 중**(추정 강도 중).
- ✅ 수집기 요약(5.6B · Qwen3-VL-4B 텍스트 인코더 · 최대 10장 참조 · 0~1000 그리드 bbox · 16스텝 증류 · BF16/int8/NVFP4 · 업샘플러 필수 · 벤치 없음) — 10-24 판과 모순 없음.

## 🔄 2026-11-01 갱신 — **10-27의 "역전 가속"은 이어지지 않았다**

**HF API**: comfy **925,236**(수집기 정확히 일치) · likes 2,215 · `lastModified` 10-17 · 원본 [[flux-3-image-klein]] **149,203** · likes 786

| 구간 | comfy 증분(일평균) | 원본 증분(일평균) | 구간 비 |
|---|--:|--:|--:|
| 10-24→10-27 | +165,815 (약 55,300) | +13,404 (약 4,470) | 12.4 |
| **10-27→11-01** | **+224,584 (약 44,900)** | **+30,031 (약 6,000)** | **7.5** |

- 원 배수 5.88 → **6.20**으로 늘었지만 구간 비는 12.4 → 7.5로 낮아졌다. comfy 일평균은 줄고 원본은 늘었다. ⚖️ **볼트 10-27 표현 "역전 폭이 가속"과 "수요가 ComfyUI 패키지로 이동 중"은 3일 구간의 과독이었다. 철회한다.** 배수 자체는 여전히 계수 규칙이 달라 사용자 수 비로 읽지 않는다 → [[계수기-배수]] · [[원본-파생-역전]].
- 📌 두 저장소 모두 생성 30일 전이라 `downloads`와 all-time이 같다. comfy 생성 10-14 · 원본 10-13이므로 **11월 중순부터 창 효과가 시작**된다. 그 뒤 증분을 단순 차감하면 안 된다 → [[지표-창길이]].
- ✅ 수집기 요약(5.6B · 참조 10장 · 16/50스텝 · 업샘플러 필수 · 벤치 없음 · gated auto) 기존 판과 모순 없음.

## 🔄 2026-11-04 갱신 (인제스트 2026-11-04) — **100만 돌파 · 3일 +11.5%(수집기 "+47%"는 10-27 값 기준) · 11-02 에 4개 레포가 같은 시각 갱신됐다 · 라이선스 "Qualifying User = 연매출 US$5M 미만" 확인**

**HF API 실측(2026-11-04T09:06Z · expand)**: comfy `downloads` **1,032,077**(수집기 정확히 일치) = `downloadsAllTime`(생성 10-14 → 21일째, 아직 30일창 이내) · likes **2,438**(일치) · `trendingScore` **264** · 목록 API(`sort=trendingScore&limit=30`) **13위** · `gated: "auto"` · 🆕 `lastModified` **2026-11-02T23:49:46Z**(11-01 까지 10-17) · sha `9d36114`

| 레포 | 11-01 | **11-04** | 3일 증분 | 일평균 |
|---|--:|--:|--:|--:|
| **comfy** | 925,236 | **1,032,077** | **+106,841 (+11.5%)** | ≈35,600 |
| 원본 [[flux-3-image-klein]] | 149,203 | **159,405** | +10,202 | ≈3,400 |
| klein-base | (미수집) | 120,013 | — | — |
| klein-pup(업샘플러) | (미수집) | 63,992 | — | — |
| likes comfy / 원본 | 2,215 / 786 | **2,438 / 817** | +223 / +31 | — |

- comfy 일평균 55,300(10-24→27) → 44,900(10-27→11-01) → **35,600** 으로 **2구간 연속 감소**. 원 배수 6.20 → **6.47**, 구간 비 7.5 → **10.5**. 원본 패밀리 3레포 합 343,410 대비 **3.01배**(10-24 2.09배). ⚖️ 10-27 의 "가속" 철회(11-01)는 유지 — 배수는 커지지만 절대 유입은 줄고 있다. 계수 단위 차이(`diffusion-single-file` vs `diffusers`)로 배수를 사용자 수 비로 읽지 않는다 → [[계수기-배수]] · [[원본-파생-역전]]. 창 효과는 **11-13 경**부터 → [[지표-창길이]].
- 🆕 **동시 갱신**: comfy 11-02T23:49:46Z · klein 11-02T23:49:00Z · klein-base 11-02T23:49:06Z · klein-pup 11-03T05:15:14Z ⇒ BFL 이 패밀리 4레포를 **1분 안에 일괄 수정**했다(pup 은 6시간 뒤). 🔴 **무엇을 바꿨는지는 확인 불가** — `api/models/<id>/commits/main` 은 게이트로 `{"error":"Access … restricted"}`, HTML `commits/main` 은 HTTP 401.
- 🏆 **10-24 미해결 ① 해소 — "Qualifying User" 정의**: 카드 HTML(익명 200 · 174,536 B) License 절 원문 *"non-commercial use, plus commercial output generation by Qualifying Users with **less than US$5M in gross annualized revenue, including affiliates**, subject to the license terms."* · 텍스트 인코더(Qwen3-VL-4B)와 업샘플러는 Apache-2.0. 🔴 이 문장이 11-02 갱신으로 추가된 것인지 10-24 볼트가 놓친 것인지는 **판별 불가**(10-24 볼트 인용은 Key Features 절 문장만 있었다 · 커밋 이력 게이트). Out-of-scope 절: *"commercial-use exception is not blanket permission for commercial fine-tuning or distribution"* — **출력물 상업 이용만** 예외다.
- 📌 **카드 이미지 열람**: 벤치 이미지는 **0건**(카드 텍스트 `bench` grep 0 · `<img>` 는 로고·아바타 외 `media/main/launch-gallery.jpg` 1개). gallery 를 받아(HTTP 200 · 6,537,996 B · 5000×3360 JPEG) 직접 열었다: 18장 샘플 콜라주, **수치·축·모델 비교 없음**. ⚠️ 그 안의 우표 샘플 세로 텍스트가 *"IINTERNA TTIONA… / IPGSTAGE ESTAAMN…"* 로 깨져 있다(1400px 축소본 + 원본 크롭으로 확인) — 카드 Limitations *"text rendered may be inaccurate or subject to distortion"* 을 **공식 쇼케이스가 스스로 보여준다**. 단 이 콜라주가 전부 Klein 출력인지는 카드에 명시돼 있지 않다(추정).
- ✅ 사양 재확인(카드 HTML): 5.6B(이미지 트랜스포머만) · 참조 최대 10장 · 증류 16스텝·가이던스 없음 / Base 50스텝·CFG 3.5 · BF16 11.1 / int8 5.8 / NVFP4 5.3 GB(증류·Base 동일) · int8 은 RTX 3070 8GB·FP8 미지원 GPU · NVFP4 는 Blackwell · 업샘플러 Qwen3.5-9B 파생 BF16 18.8 / int8 9.8 / w4a8 6.7 GB · 카드 권장 다운로드 명령은 **int8 트랜스포머 5.8 + 인코더 4.9 + VAE 0.3 + 업샘플러 9.8 = 20.8 GB** — "8GB GPU 에서 돈다"는 트랜스포머 기준이고 업샘플러까지 같은 GPU 에 올리는 조건은 아니다. CSAM·NCII 위험 평가·완화 문단 존재(수집기 기재 정확).

- 수집기 평가: ✅ 지표 2종·사양·게이트 경로(raw `README.md` **HTTP 401** · 150 B 안내문 → HTML 200 · 174,536 B 전건 일치) · 🔴 **"볼트 직전값 700,652(10-27) 대비 +47%" — 볼트 최신값은 11-01 925,236 이다 → 실제 +11.5%**(직전값 오참조, 1.47 은 7일 구간) · 🔴 `lastModified` 10-17 → 11-02 변경 미지적 · 🔴 라이선스 US$5M 기준(볼트 미해결 ① 해소 근거) 미기재 · ⚖️ "라이선스 flux-kommunity-license" 만 적어 비상업 기본이라는 핵심 제약이 빠짐 · 🔴 업샘플러 포함 실 다운로드 용량(20.8 GB) 미기재

## 원본 (11-04 갱신)
- 볼트 실측: HF API expand(comfy · klein · klein-base · klein-pup) · `api/models?sort=trendingScore&limit=30`(13위) · `raw/main/README.md`(401 · 150 B) · HTML 모델 페이지(200 · 174,536 B, 텍스트 추출) · `api/.../commits/main`(게이트 에러) · HTML `commits/main`(401) · `expand[]=siblings`(파일 목록) · `media/main/launch-gallery.jpg`(별도 디렉토리 저장 후 직접 열람)
- 신뢰도: ⭐⭐⭐
