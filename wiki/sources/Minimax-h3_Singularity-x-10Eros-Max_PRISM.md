---
title: "OliviaRossi/Minimax-h3_Singularity-x-10Eros-Max_PRISM — H3 파인튜닝 2종 자체 알고리즘 병합 (정량 0 · 🔴 H3 라이선스 → 한국 제외 · 원본 표기 충돌)"
type: source
domain: video-saas
tags: [video-saas, hf-model, video-generation, minimax-h3, model-merge, 라이선스, 파생저장소]
created: 2026-11-19
updated: 2026-11-19
sources: [https://huggingface.co/OliviaRossi/Minimax-h3_Singularity-x-10Eros-Max_PRISM]
reliability: low
---

**HF**: 다운로드 **523,654**(30일 = 누적 · 생성 10-24) · ♥359 · trendingScore 65 · license `other` · base_model `WarmBloodAban/Minimax-h3_Singularity` + `TenStrip/10Eros-Max` · 레포 LICENSE **404**(볼트 확인)

## 핵심 인사이트
> [!insight] 병합의 병합 — 라이선스가 "원본을 따른다"로 위임되고 원본 둘은 서로 다른 표기를 한다
> [[MiniMax-H3]] Ref2VA 파인튜닝 2종(볼트 09-08 보유 [[Minimax-h3_Singularity]] + 10Eros-Max 8-step turbo)을 자체 **PRISM** 알고리즘(차분 SVD 분해 · SLERP · 부호 충돌 조정 · 노름 재정렬, mergekit 미사용 — 수집기 판독)으로 병합. fp16 · int8 · w6a8 변형, 작성자 권장 PRISM_DMAD_PDMD(피부 질감 특화).

> [!warning] 🔴 [[라이선스-지역-제외]] 파생 7번째
> - 카드 "원본 모델을 따름(other)" → 원본 둘 다 base 가 MiniMax-H3 → H3 LICENSE 10행 Excluded Territories 에 **대한민국 포함**(EU · 영국 · 미국도). 볼트 개념 페이지의 H3 원문 대조와 일치.
> - 그런데 [[Minimax-h3_Singularity]] 원본은 카드에 **apache-2.0** 으로 표기(볼트 09-08 기록과 일치) — 상위 H3 라이선스와 **충돌**. 하위 표기가 상위 조건을 해제할 수 없으므로 볼트 판단은 **H3 조건 우선 → 한국 사용 보류**(법률 판단 아님).
> - 정량 평가 0건(샘플 영상만). 09-08 볼트가 Singularity 에서 이미 "지표 전무"로 기록 — 병합 후에도 동일.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 낮음 — 미측정 병합 레시피.
- **크리에이터 인사이트**: 52만 다운로드 = 크리에이터는 "8-step + 피부 질감"이라는 **결과 묘사**로 고른다. 측정 대신 샘플 영상이 선택 기준.
- **경쟁 우위 빈틈**: 없음 · 🔴 한국 서비스에 사용 불가 판정.
- **즉시 활용**: NO.

## 관련 페이지
- [[MiniMax-H3]] · [[Minimax-h3_Singularity]] · [[MiniMax]] · [[라이선스-지역-제외]] · [[파생저장소-식별]] · [[LTX2.3-10Eros]] (10Eros 계열 명명 · 다른 베이스) · [[MiniMax-H3-Character-Swap-LoRA]]

## 원본
- 출처: https://huggingface.co/OliviaRossi/Minimax-h3_Singularity-x-10Eros-Max_PRISM
- 확인 범위: HF API(expand · license · base_model) · LICENSE 404 · H3 LICENSE 10행은 볼트 11-12 원문 대조 · 🔴 PRISM 알고리즘 · 변형 목록은 수집기 판독
- 신뢰도: ⭐ (정량 0 · 라이선스 충돌)
