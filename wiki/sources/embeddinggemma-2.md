---
title: "google/embeddinggemma-2 — 740M 4모달(텍스트·이미지·영상·오디오) 통합 임베딩 · 256d 까지는 거의 무손실, 128d 는 텍스트 전용"
type: source
domain: local-llm
tags: [local-llm, embedding, multimodal, on-device, matryoshka, gemma, google, agent-memory]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/google/embeddinggemma-2]
reliability: high
---

**모델**: [google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) · dl30 **517,987** · 누적 661,386 · likes 3,418 · apache-2.0 · 게이트 없음 · safetensors 744,371,512 파라미터 · created 2026-09-14 · modified 2026-10-28 · arXiv 2610.37364 (HF API 볼트 실측 — 수집기와 전건 일치). 수집기 `ai-news` → 볼트 재분류 `local-llm`.

> [!note] 볼트는 파생본을 먼저 갖고 있었다
> [[embeddinggemma-2-GGUF]](10-11 수록 · actionable "한국어 임베딩 1회 측정" 대기 중)의 **원본**이 이 페이지다. 원본 카드가 들어오면서 GGUF 측정의 기준선(아래 표)이 생겼다.

## 핵심 인사이트
> [!insight] 개선은 텍스트가 아니라 코드와 멀티모달에서 왔다
> Gemma 4 기반, 텍스트(코드 포함) · 이미지 · 영상 · 오디오를 하나의 768차원 공간에. 텍스트 백본 **270M**(트랜스포머 130M + 임베더 140M)에 비전 170M · 오디오 300M 인코더를 **필요할 때만 로드**. 8K 컨텍스트 · MRL 절단 512/256/128(최대 6배 저장 절감). 카드 raw 82–101행(볼트 직접 판독):
> | 지표 (768d) | EmbeddingGemma 2 | 전작 |
> |---|---|---|
> | MTEB 다국어 v2 | **61.36** | 61.15 (+0.21) |
> | MTEB 코드 v1 | **78.68** | 68.76 (+9.92) |
>
> 절단 표: 768d 행 `61.36 / 68.46 / 78.68 / 65.67 / 59.01 / 69.54 / 49.87` → 128d 행 `57.89 / 65.68 / 71.41 / 59.97 / 45.65 / 56.71 / 47.28`. 다섯째 열(수집기 표기로는 MMEB)은 59.01 → **45.65**(−13.36)로 급락, 첫째 열(MTEB 다국어)은 −3.47. 카드 문구: *"minimal quality impact down to 256d. 128d is best suited to text-only workloads"* · *"128 dimensions degrades multimodal quality substantially"*.

> [!warning] 읽는 법
> 1. 텍스트 다국어는 전작과 사실상 같다(+0.21) — "2"의 가치는 **코드(+9.92)와 모달리티 추가**다. 텍스트 전용 한국어 검색이 목적이면 전작/GGUF 로 충분할 수 있다.
> 2. 비교 대상이 자사 전작뿐 — 타사 임베딩 대비 수치 없음.
> 3. 한국어 단독 수치는 카드에 없다(MTEB 다국어 평균만) — 10-11 actionable 의 측정 필요성은 그대로.

## 도메인별 추출 (local-llm · 에이전트 메모리)
- **실용성 판단**: YES — 텍스트 전용 로드 270M 은 CPU 구동 범위. apache-2.0 · 게이트 없음 · 지역 제한 없음.
- **메모리 아키텍처**: RAG 의 검색기. 4모달 단일 공간이라 "영상 클립 · 음성 메모 · 텍스트 노트"를 한 인덱스에 넣을 수 있다 — 볼트(영상 SaaS + 위키) 용도에 직접 맞는다.
- **Hermes 적용**: 후보 — 256d 절단으로 인덱스 크기를 1/3 로 줄이고 품질은 거의 유지(MTEB 다국어 60.41, 수집기 판독). 멀티모달을 쓸 거면 128d 금지.
- **트레이드오프**: 768d → 256d 저장 1/3 · 소폭 하락 / 128d 저장 1/6 · 멀티모달 급락.
- **오픈소스 구현체**: transformers · sentence-transformers(카드 태그) · GGUF 는 [[embeddinggemma-2-GGUF]].

> [!action] 당장 할 것
> 10-11 actionable(한국어 문장 5쌍 코사인 측정)을 **원본 768d vs 256d** 두 조건으로 돌린다 — 측정 한 번에 절단 손실까지 확인.

## 관련 페이지
- [[embeddinggemma-2-GGUF]] · [[Google]] · [[에이전트-메모리-레이어]] · [[원본-파생-역전]] · [[배포출처-봉인]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/google/embeddinggemma-2
- 확인 범위: HF API 메타 · 카드 raw(22,234B) 36–101 · 163–187행 직접 판독 · 🔴 MIEB/MMEB/MSEB/MAEB 열 이름 대응 · 256d 행은 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐⭐ (Google DeepMind · likes 3,418 · 논문 · 절단 표 공개)
