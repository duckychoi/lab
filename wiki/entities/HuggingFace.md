---
title: HuggingFace — 모델 정의와 배포의 공통 기반
type: entity
domain: ai-news
tags: [entity, huggingface, infrastructure, platform, open-source, apache-2.0]
created: 2026-09-15
updated: 2026-09-15
sources: [huggingface-transformers.md, clip-vit-base-patch32.md, distilbert-base-uncased.md, Llama-3.1-8B-Instruct.md]
reliability: high
---

# HuggingFace

> [!insight] 이 볼트에서 가장 늦게 기록된 가장 많이 쓰인 조직
> 소스 1,043개를 쌓는 동안 **HuggingFace 자체의 엔티티 페이지가 없었다.** 수백 개 모델 페이지가 `huggingface.co/...` URL과 `library_name: transformers` 태그를 적으면서, **그 플랫폼과 조직은 한 번도 주어가 되지 않았다.**
> 📌 [[암묵을-명시로]] 의 교과서적 사례 — **인프라는 전제로 쓰이기 때문에 서술되지 않는다.**

## 두 개의 축

**1. [[huggingface-transformers]] — 호환성 계약** (★166,137 · Apache-2.0 · 2018-10-29~)
모델 정의를 한 곳에 고정해 학습 프레임워크(Axolotl·Unsloth·DeepSpeed·FSDP)와 추론 엔진(vLLM·SGLang·TGI), 인접 라이브러리(llama.cpp·mlx)가 **동일한 정의를 재사용**하게 만든다. 제품이 아니라 계약이다.

**2. Hub — 배포·계량 인프라**
이 볼트의 모델·논문 소스 대부분이 여기서 온다. 그리고 **볼트의 측정 규칙 상당수가 이 플랫폼의 API 특성에서 유래했다**:

- 🔴 **`trendingScore` 는 엔드포인트마다 다르다** — 목록 API(`/api/models?sort=trendingScore`)에서만 값이 나오고, **개별 API(`/api/models/{id}`)는 `null`** 이다. 볼트가 09-14에 `null` 을 받아 *"필드 폐기"* 로 오인했던 원인. **2026-09-15 양쪽 실측으로 확정**([[clip-vit-base-patch32]] 목록 179 / 개별 null).
- 🔴 **`downloads` 는 30일 누적**이다 — 전체 누적이 아니다. [[단위-불일치]] 상습 지점.
- 🔴 **`gated: manual` 저장소는 카드 본문이 401로 막힌다** — 메타데이터는 공개, 본문은 비공개. [[Llama-3.1-8B-Instruct]] 참조.
- 🔴 **`license:` 태그는 선택 사항이다** — 미선언 ≠ 라이선스 없음([[clip-vit-base-patch32]], 월 2,150만 DL). [[메타데이터-부재-추론]] 참조.

> [!action] 볼트 검증 절차 (확정)
> HF 지표 검증 시 **목록 API와 개별 API를 구분해 조회**한다. 트렌딩 값이 필요하면 목록 API를 쓴다. 다운로드는 **"30일"을 항상 병기**한다.

## 이 볼트의 HF 기원 소스 (일부)
- 상시 인프라: [[clip-vit-base-patch32]] · [[distilbert-base-uncased]] · [[bert-base-uncased]] · [[all-MiniLM-L6-v2]] · [[gpt2]]
- 게이트 모델: [[Llama-3.1-8B-Instruct]]
- 논문 채널: [[Atria-Dawn]] · [[Dream-RSI]] · [[ZGCM-1]] · [[Vidu-S2]] · [[DataFlex-RL]]

## 관련 페이지
- [[huggingface-transformers]] · [[pytorch]] — 하부 인프라 계열
- [[암묵을-명시로]] · [[메타데이터-부재-추론]] · [[단위-불일치]] · [[상대속도-가림]]
- [[Meta]] · [[OpenAI]] · [[Zhipu AI]] · [[Alibaba]]

## 원본
- 검증: GitHub API + HF API 실호출(2026-09-15)
- 신뢰도: ⭐⭐⭐
