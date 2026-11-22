---
title: "AngelSlim/Hy4-flash-GGUF — Tencent Hy4 flash(220B · 활성 약 12B) GGUF 5종 (최소 128GB 급 · llama.cpp 미병합 PR 빌드 필요 · LICENSE 지역 조항 0건)"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, moe, latent-moe, tencent, license, large-memory]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/AngelSlim/Hy4-flash-GGUF]
reliability: medium
---

**HF**: dl30 94,791 · 좋아요 147(볼트 API 11-22 · 수집기 일치) · 생성 2026-11-16 · 내부 ID `6afb131b…` · 카드 license **필드 없음** · base_model `tencent/Hy4-flash`(dl 5,588 · 좋아요 567 · license `other` = tencent-hy-license · 내부 ID `6afbcdae…`)

## 핵심 인사이트
> [!insight] 활성 12B 라는 숫자는 메모리 요구를 말해 주지 않는다
> 원본 Hy4 flash: **총 220B(Engram n-gram 임베딩 63.5B 포함) · 토큰당 활성 텍스트 11.3B + 비전 0.43B**, 컨텍스트 1M, 텍스트 + 이미지 입력. 희소 어텐션(IndexPool)과 SWA 를 1:3 교차, [[latent-MoE]](512 experts 중 16개 + 공유 1개). 그런데 GGUF 는 Q4_K_M 156.79GiB ~ IQ2-AH 125.73GiB — **최소 128GB 급 메모리**. 활성 파라미터는 연산량의 지표이고 적재량은 총량이 정한다 → [[파라미터-다중표기]].

## 도메인별 추출 (local-llm)
- **실용성 판단**: 🔴 128GB 급 장비 + **llama.cpp 미병합 PR #32517 브랜치 직접 빌드** 필요(볼트가 GGUF 카드에서 `32517` 2회 검출).
- **트레이드오프**: 카드 자체 속도 — M5 Max 128GB Q3_K decode 47–50 tok/s · prefill 521–743 tok/s(4K–32K), RTX Spark 128GB SPARK-4Bit-Fast decode 32–33 tok/s. 품질 벤치는 원본 카드 부록이 이미지라 수치 미확인([[벤치마크-이미지-봉인]]).
- **Hermes 적용**: NO(메모리).
- **오픈소스 구현체**: PR 병합 전까지는 포크 빌드.

> [!note] 라이선스 — 볼트가 원본 LICENSE 를 직접 열었다
> Tencent Hy License 1.0(245행, 볼트 행수 일치). **`territor|korea|european|united kingdom` 적중 0건** — 이전 Hunyuan 계열과 달리 지역 제외 조항이 없다([[라이선스-지역-제외]] 의 반대 사례로 기록). 상업 조항: 207행 **연매출 US$50 million 초과**, 215행 **월간 활성 사용자 1억 초과** 서비스의 MaaS 는 별도 서면 라이선스(내부 전용 사용 예외 — 수집기 판독). GGUF 레포 카드에는 license 필드가 비어 있어, **파생 레포만 보면 이 조건을 알 수 없다** → base 체인 최상위 원본 LICENSE 적용 규칙(11-19).

> [!warning] 원본-파생 역전
> GGUF dl 94,791 vs 원본 5,588 — **약 17배**(볼트 산술). 좋아요는 원본 567 vs 147.

## 관련 페이지
- [[Tencent]] · [[Hy3]] · [[latent-MoE]] · [[파라미터-다중표기]] · [[라이선스-지역-제외]] · [[원본-파생-역전]] · [[벤치마크-이미지-봉인]] · [[Edge0-145B-NVFP4]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/AngelSlim/Hy4-flash-GGUF · https://huggingface.co/tencent/Hy4-flash
- 확인 범위: HF models API 2건 · GGUF 카드 README 원문(4,873B) · 원본 LICENSE 원문(245행 · grep) · 🔴 원본 카드 본문 · 이미지 벤치 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐
