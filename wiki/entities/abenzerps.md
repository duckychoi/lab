---
title: "abenzerps — 양자화 재배포자"
type: entity
domain: ai-news
tags: [entity, huggingface, quantization, gguf, comfyui, 원본-파생-역전]
created: 2026-10-02
updated: 2026-10-10
sources: [Qwen-Image-2.1-Uncensored-GGUF.md, Qwen-Image-2.1.md]
reliability: medium
---

# abenzerps

**HF**: https://huggingface.co/abenzerps

> [!insight] 🎯 핵심 — **베이스 제공자보다 많이 다운로드되는 재배포자**
> [[Qwen-Image-2.1-Uncensored-GGUF]] 의 제공자. 📌 **DL 1,303,476 으로 베이스 제공자 [[Qwen]] 의 원본(76,938)을 16.9배 앞선다** → [[원본-파생-역전]] 의 주요 사례.
> 🏆 **볼트가 주목하는 이유는 양자화 품질이 아니라 "동봉" 전략이다** — 가중치만 올리지 않고 **텍스트 인코더(qwen3vl_8b)와 VAE 까지 같은 레포에** 넣어 **ComfyUI 단독 구동**을 가능케 했다. **베이스 레포만으로는 바로 돌지 않는다.** ⇒ **DL 의 상당 부분이 "모델"이 아니라 "작동하는 세트"에 대한 수요로 보인다**(🔴 가설, 미검정).

> [!note] 확인된 것 (볼트 실측)
> - `base_model_relation` = **`quantized`** 로 베이스 관계를 **구조화 선언** → [[파생저장소-식별]] 최강 형태
> - 🎯 **재현 경로를 문자로 고정**: 소스 리비전 `b3179ad3…` · 변환 도구 `stable-diffusion.cpp` 커밋 `1330ceba…` · **SHA256SUMS 제공**. ⚖️ **볼트 수집 이력에서 이 정도로 명시된 파생 제공자는 드물다 — 신뢰도 가산.**
> - 12종 포맷 제공(GGUF·FP8·INT8 ConvRot·NVFP4·MLX 4/6/8bit) · **BF16 14.23GB ~ Q4_0 4.15GB**
> - 카드가 **"내장 안전 검사기·콘텐츠 필터 없음"** 을 명시(무검열 변종). **사실로만 기록한다.**

> [!warning] 🔴 미확인
> - 🔴 **09-22 에 이 레포가 307 리다이렉트로 DL 0 으로 읽혔다** — 당시 개명 이력이 있었고 **개명 전/후 관계 미정리**(actionable 410행)
> - *"Uncensored"* 가 **어떤 조작의 결과인지 카드가 설명하지 않는다**(가중치 변경인지 파이프라인 필터 제거인지 불명)
> - `license_link` **None** — `license_name: qwen-research` 만 선언하고 파일 미동봉 → [[메타데이터-부재-추론]]
> - 다른 보유 레포 · 신원 · 활동 이력 **미조회**

## 관련 페이지
- [[Qwen-Image-2.1-Uncensored-GGUF]] — 주 레포 · [[Qwen]] — 베이스 제공자 · [[Qwen-Image-2.1]]
- [[원본-파생-역전]] · [[파생저장소-식별]] · [[대체필드-대조]] · [[정규명-우선-중복검사]]

---

## 🔄 2026-10-10 갱신 — trending 5위, 12일 동결

> [!insight] 산출물 갱신 — [[Qwen-Image-2.1-Uncensored-GGUF]]
> 다운로드 **2,013,268**(30일 = **전체누적 동일**) · likes 3,801 · **trending 5위** · lastModified 2026-09-28 · created 2026-09-20
> `gguf.total` **7,115,124,736**(71.2억) · 총 파일 **14.23GB** · 아키텍처 `qwen_image21` · `license: other`
> 📌 금일 다운로드 1위는 [[Qwen3.8-27B]](6,783,589)였으나 **raw.md 10-06 배치에 URL 이 이미 있어 중복 제외**하고 본 모델을 1순위로 올렸다.

> [!insight] ✅ `gguf.total` 우회법 재적용
> `safetensors.total` 이 **`None`** 이므로 `gguf.total` 로 파라미터를 읽었다 — 볼트 **누적 우회법 ⑤** 재적용. → [[대체필드-대조]]

> [!warning] 🔴 30일 == 전체누적 (2,013,268) — 성장률을 계산할 수 없다
> ⚖️ **두 해석이 가능하고 단정하지 않는다**: ① 생성 20일째라 전 기간이 30일 창 안 ② `downloadsAllTime` 이 30일 값을 반영
> 📌 **created 2026-09-20 이므로 ①이 더 그럴듯하지만 확인하지 않았다.**
> ⇒ 🆕 **규약: `downloads`(30일) == `downloadsAllTime` 인 모델은 "창 길이가 무의미한 구간"이다.** 🔗 **금일 n=3**([[laya]] 41,468 · [[Ternary-Bonsai-2-27B]] 4,120,718) → [[지표-창길이]]

> [!insight] 📌 [[캐시된-지표-신선도]] 역방향 — 모델은 멈췄고 수요만 움직인다
> **12일간 갱신 없음인데 trending 5위**다. [[Agent-Reach]](21일 동결 · 증분 가속)의 **모델 버전**이고, 이번 2배치에서 **"동결 + 수요 증가"가 3건** 관측됐다.

> [!warning] 🔴 미확인
> **양자화 품질 손실 측정 0개** · `license: other` 와 **원본 Qwen 라이선스의 관계 미확인** · 제공자 실체 미조회.

## 관련 페이지 (갱신 추가)
- [[Qwen-Image-2.1-Uncensored-GGUF]] · [[지표-창길이]] · [[대체필드-대조]]
- [[캐시된-지표-신선도]] · [[laya]] · [[Agent-Reach]] · [[Qwen]]
