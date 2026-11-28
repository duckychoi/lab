---
title: Aleph-Alpha
type: entity
domain: local-llm
tags: [entity, org, german, moe, reasoning, sovereignty, gguf]
created: 2026-11-28
updated: 2026-11-28
sources: [Kolibri-1.1.md]
reliability: medium
---

## 개요
HF 조직 `Aleph-Alpha` — **볼트 조직 실측(11-28 · HF API)**: 공개 모델 **32개**. 독일어/영어 이중 MoE 추론 라인 **Kolibri**(1.0 → 1.1)와 구형 Pharia-1-LLM-7B-control 계열이 확인된다. 수집기 보고 기준 **유럽 GPAI 코드 서명국 제품**(볼트 미검증).

## 모델 (볼트 실측 2026-11-28)
- [[Kolibri-1.1]] — DL **1,725** · ♥ **222** · Apache-2.0 · created 2026-11-20 (신규)
- Kolibri-1.1-GGUF — DL **44,807** · ♥ 37 — **베이스 레포보다 26배**([[원본-파생-역전]] 역방향: GGUF가 본류보다 큰 파생)
- Kolibri-1 — DL **11,009** · ♥ **1,028** (전세대)
- Pharia-1-LLM-7B-control(+aligned/hf) — DL 0~457 (구 라인 · 연구 계열 t-free/umup/sp-baseline 다수)

## 관찰
- **좋아요 밀도가 비정상적으로 높다**: Kolibri-1.1 ♥222/DL 1,725 — 다운로드당 좋아요 비율이 대형 조직 관행을 크게 벗어난다. 신모델 초기 관찰 특성(선도 유저층) 가능성 → [[지표-창길이]] 재관측 필요.
- **전세대 Kolibri-1(♥1,028)이 신세대보다 좋아요가 많다** — 세대 교체 진행 판단은 이르다(09-07 [[timesfm-3.0-pytorch]] 사례와 동형: 좋아요는 누적되고 다운로드는 이동한다).
- 범위 한계: 조직 소속·법인 규모·GPAI 서명 여부는 미확인 — 볼트 실측은 HF 조직 목록뿐.

## 관련 페이지
- [[Kolibri-1.1]] · [[원본-파생-역전]] · [[지표-창길이]] · [[복합지표-분해]] · [[local-llm]]
