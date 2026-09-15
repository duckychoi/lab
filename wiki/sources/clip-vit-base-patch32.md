---
title: openai/clip-vit-base-patch32 — 제로샷 이미지 분류 상시 의존 백본
type: source
domain: ai-news
tags: [ai-news, huggingface, model, clip, zero-shot, vision-language, infrastructure, license-undeclared]
created: 2026-09-15
updated: 2026-09-15
sources: []
reliability: high
---

# HF모델: openai/clip-vit-base-patch32 — 4년째 깔려 있는 바닥

**URL**: https://huggingface.co/openai/clip-vit-base-patch32
**지표(2026-09-15 API 실측 · raw 기록과 완전 일치)**: 다운로드 **21,504,830**(30일) · ♥ **1,531** · trendingScore **179**(목록 API) · **DL:♥ = 14,046:1**
생성 **2022-03-02** · 최종수정 **2024-02-29** · `pipeline_tag: zero-shot-image-classification` · `gated: False`

> [!insight] 핵심 인사이트
> 임의의 이미지 분류 과제에 **제로샷으로 일반화**하는 능력을 연구하려고 만들어진 비전-언어 모델. ImageNet과 그 분포이동 변형(ImageNet-A/R/Sketch/ObjectNet/Vid)에서 강건성을 평가한다.
>
> 🎯 **월 2,150만 다운로드 = 이 배치 3건 중 1위.** 이건 "인기 모델"이 아니라 **파이프라인의 기본 부품**이다. 수많은 이미지 검색·필터링·임베딩 파이프라인이 이 하나에 의존한다. [[huggingface-transformers]] 와 같은 성격 — **가장 많이 쓰이는 것이 가장 늦게 기록된다.**

> [!warning] 🔴 모델카드가 스스로 배포를 말린다
> 카드 명시: **"not developed for general model deployment"** — 일반 배포용으로 개발되지 않았으며 **연구 커뮤니티를 위한 연구 산출물**이다. 배포 전 해당 맥락에서의 능력 검토가 전제된다.
> 📌 **월 2,150만 다운로드와 "배포용 아님"이 공존한다.** 생태계는 저자의 경고를 4년째 무시하고 있다 — 이건 CLIP의 결함이 아니라 **경고문이 다운로드를 막지 못한다**는 사실의 증거다.

> [!warning] 🔴 라이선스 **미선언** — API 실측 확인
> HF 태그에 **`license:` 항목이 존재하지 않는다.** 실측 태그 전체: `transformers`/`pytorch`/`tf`/`jax`/`clip`/`vision`/`arxiv:2103.00020`/`arxiv:1908.04913`/`endpoints_compatible`/`region:us`.
> 같은 배치 [[distilbert-base-uncased]](`license:apache-2.0`) · [[Llama-3.1-8B-Instruct]](`license:llama3.1`) 와 대조된다.
> **2,150만 DL 규모에서 라이선스가 선언되지 않은 상태 — 상용 사용 판단 시 별도 확인 필요.**
> ✅ **다만 이 항목의 기록 방식은 모범이다**: 수집기는 *"라이선스 없음"* 이 아니라 **"미선언이므로 별도 확인 필요"** 로 적었다. 메타데이터 부재를 *사실의 부재*로 읽지 않은 것 → [[메타데이터-부재-추론]] 의 **올바른 처리 사례.**

> [!warning] 🔴 성립 조건 — 트렌딩 진입 사유가 "신규"가 아니다
> **2024-02-29 이후 갱신이 없다.** trendingScore 179는 파이프라인 상시 의존에서 나오는 **기저 다운로드량의 결과**다. 신규 릴리스로 오르는 트렌딩과 **같은 표에 섞여 있다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ 4년 · 2,150만 DL/월 · 논문 2편(arXiv 2103.00020 · 1908.04913) → high
- **즉시 활용**: **이미 쓰고 있을 가능성이 높다**(간접 의존). 직접 쓴다면 **라이선스 미선언**을 먼저 확인.
- **대체 관계**: 최신 SigLIP 계열이 벤치에서 앞서지만 **생태계 호환성은 CLIP이 압도.** 교체 비용이 성능 이득보다 클 수 있다.
- **허와 실**: 과장 없음. 오히려 **저자가 스스로 한정한 것보다 넓게 쓰이고 있다.**

## 관련 페이지
- [[메타데이터-부재-추론]] — 라이선스 미선언의 올바른 처리 사례
- [[distilbert-base-uncased]] · [[Llama-3.1-8B-Instruct]] — 같은 배치 3건
- [[huggingface-transformers]] · [[상대속도-가림]] · [[all-MiniLM-L6-v2]] · [[bert-base-uncased]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/openai/clip-vit-base-patch32
- 검증: HF API 실호출(2026-09-15). **DL·♥·생성일·수정일·gated·라이선스 태그 부재 전건 일치(드리프트 0)**
- 📌 `trendingScore` 는 **목록 API(`/api/models?sort=trendingScore`)에서만 값이 나오고 개별 API(`/api/models/{id}`)는 `null`** 이다 — 볼트가 09-14에 `null` 을 받은 원인. **이번에 개별 API 실측으로 `null` 재확인 = 수집기 설명 검증 완료.**
- 신뢰도: ⭐⭐⭐
