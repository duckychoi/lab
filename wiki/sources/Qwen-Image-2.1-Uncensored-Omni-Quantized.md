---
title: "chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized — 무검열 Omni LoRA(90k 스텝) 병합 양자화본 (비상업 연구 라이선스)"
type: source
domain: local-llm
tags: [local-llm, qwen-image, uncensored, gguf, quantization, license]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized]
reliability: medium
---

**모델**: [chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized](https://huggingface.co/chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized) · 다운로드 120,618 · 좋아요 334 · license `other`(qwen-research) · base Qwen/Qwen-Image-2.1 · 생성 2026-11-03 · HF 내부 ID `6aea0825…`.

> [!note] 이름 유사 — 볼트의 [[Qwen-Image-2.1-Uncensored-Quantized]] 와 다른 레포
> 그쪽은 abenzerps(현 `Qwen-Image-2.1-Turbo-Quantized`, ID `6ab000f1…`). 내부 ID 가 달라 개명 · 이전이 아니다(볼트 API 대조) → [[정규명-우선-중복검사]].

## 핵심 인사이트
> [!insight] 정직한 벤치 문서 — 그리고 수집기가 뺀 중간 열
> `BENCHMARK.md`(BF16 LoRA 병합 기준, ±1 SE · 볼트 확인):
> | 지표 | Base | Step 32,000 | Step 90,000 |
> |---|---|---|---|
> | 성인 프롬프트 충실도(960) | 85.1 | 87.4 | **89.7** |
> | 해부학(960) | **70.3** | 67.7 | 69.4 |
> | 일반 SFW(PartiPrompts 300) | **79.8** | 75.8 | 79.6 |
> 🆕 볼트 추가: 중간 체크포인트(32k)는 **일반 SFW −4.0 · 해부학 −2.6** 으로 떨어졌다가 90k 에서 회복 — 배포본이 "손상 없음"인 것은 학습을 더 돌린 결과다. 카드는 *"The base model is already capable here … a few points, not a change from unusable to usable"*(33행)라고 스스로 한정 → [[자기제한-명시]].

## 도메인별 추출 (local-llm)
- **실용성 판단**: GGUF BF16 14.23GB ~ Q4_0 4.20GB · ComfyUI FP8/INT8 ConvRot/NVFP4 · Diffusers NF4 3.67GB. 권장 35스텝 · true CFG 5.0 · `er_sde` · 네거티브 공백 1칸(비우면 CFG 꺼짐).
- **트레이드오프**: 🔴 *"The quantized files were not benchmarked separately"*(10행) — 측정은 BF16 병합, 배포는 양자화. 판정자는 **무검열 Qwen3.8-27B GGUF 단일 VLM** Yes/No 확률(사람 평가 아님 · 수집기).
- **라이선스**: Qwen RESEARCH LICENSE 19–20행 — worldwide 이나 **상업 목적 사용 금지**(별도 라이선스 필요). 지역 제외 없음.
- **Hermes 적용**: 해당 없음.

## 관련 페이지
- [[Qwen-Image-2.1]] · [[Qwen-Image-2.1-Uncensored-Quantized]](다른 레포) · [[Qwen-Image-2.1-Uncensored-GGUF]] · [[Qwen]] · [[자기제한-명시]] · [[정규명-우선-중복검사]] · [[표-부분인용]]

## 원본
- 출처: https://huggingface.co/chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized
- 확인 범위: HF models API 메타 · 내부 ID 대조 · LICENSE 19–20행 · BENCHMARK.md 10–33행(볼트) · 🔴 파일 목록 · 권장 설정 · 판정자 구성은 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐ (벤치 공개 · 양자화본 미측정 · 비상업)
