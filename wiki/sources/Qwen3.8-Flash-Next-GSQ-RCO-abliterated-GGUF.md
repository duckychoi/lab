---
title: "SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF — 재양자화 없이 텐서 144개만 이식한 거부 제거판"
type: source
domain: local-llm
tags: [local-llm, gguf, abliterated, quantization, tensor-transplant, gsq-rco, qwen3.8]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF]
reliability: medium
---

**모델**: [SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF](https://huggingface.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF) · dl30 **4,081,896** · 누적 5,544,959 · likes 994 · apache-2.0 · created 2026-10-02 · modified 2026-10-24 · base `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF` (HF API 볼트 실측 11-14 09:05Z). 수집기 `ai-news` → 볼트 재분류 `local-llm`.

> [!note] 30일 창은 줄어든다
> 수집기 11-13: 4,120,281 → 볼트 11-14: 4,081,896(−38,385). 누적이 아니라 30일 이동 창이라 감소할 수 있다 → [[지표-창길이]]. 샤드 다중 파일(가중치 + 28.80GB n-gram 임베딩 샤드) 구성이라 요청 수가 사용자 수보다 크게 잡힐 가능성(수집기 지적 · 미검증).

## 핵심 인사이트
> [!insight] 양자화는 건드리지 않고 편집만 옮겨 심는다
> [[ISTA-DASLab]] 의 [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] 를 **재양자화하지 않고**, 48개 층의 잔차 쓰기 투영 텐서 **144개**(전체 1,223개 중)를 `orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF` 의 abliterated 텐서로 교체 — 135개는 바이트 단위 이식, 9개는 GSQ 스케일로 재인코딩(수집기 판독). 티어별 크기 IQ3_S 55.06GB / IQ3_XXS 47.34GB / IQ2_XS 39.67GB / Q2_0 38.02GB + 공용 n-gram 샤드 28.80GB, 원본 대비 **+0.25~0.44GB**(카드 표 볼트 확인).
> 근거: BF16 abliterated 판에서 ΔW 의 σ₂/σ₁ = 0.0032–0.0053(거의 rank-1 편집), 라우팅 전문가 512개의 방향이 공유 전문가 방향과 |cos| = 1.00000.
> ⇒ **"양자화 학습이 만든 값은 그대로 두고 rank-1 편집만 얹는다"** — 양자화 품질과 편집을 분리한 배포 형식. 재양자화 오차를 새로 만들지 않는다는 점이 기존 abliterated GGUF 와의 차이다.

> [!warning] 행동 검증은 프롬프트 1개
> 카드의 검증 4종 중 ③(텐서 단위 blake2b 대조)은 "hard evidence", ④(행동 점검)는 스스로 *"only a spot check … only that one prompt is a clean discriminator … Do not read it as a full evaluation"* 이라고 적는다(볼트 직접 판독) → [[자기제한-명시]]. 거부율 · KL · 품질 벤치 수치는 없다. 카드 안전 고지: 가드레일 없음 · 자체 모더레이션 필수.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 최소 티어도 38GB + 28.8GB 샤드 — 대형 메모리 장비 전용. 볼트 장비에서는 비현실적.
- **메모리 아키텍처**: 해당 없음. n-gram 임베딩 테이블을 mmap 으로 디스크에 두고 토큰당 1행을 읽는 구성(카드).
- **Hermes 적용**: NO(크기).
- **트레이드오프**: 편집 비용 +0.25~0.44GB · 품질 변화 미측정.
- **오픈소스 구현체**: 이식 절차 자체가 다른 GSQ-RCO 양자화본에 재사용 가능한 레시피.

## 관련 페이지
- [[ISTA-DASLab]] · [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] · [[heretic]] · [[자기제한-명시]] · [[지표-창길이]] · [[원본-파생-역전]] · [[DavidAU-Qwen3.5-9B-Defiant-Fable]](같은 날 무검열 계열)

## 원본
- 출처: https://huggingface.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF
- 확인 범위: HF API 메타 · 카드 raw(49,737B) 내려받아 검증 절 · 크기 표 · σ 비 판독 · 🔴 135/9 분해는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐ (dl30 408만 · 행동 측정 1건)
