---
title: "FLUX.1-schnell — 12B 정류 플로우 텍스트→이미지, 1–4스텝 · Apache-2.0"
type: source
domain: ai-news
tags: [ai-news, hf-model, text-to-image, flow-matching, distillation, apache-license, flux, baseline-resurfacing]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/black-forest-labs/FLUX.1-schnell]
reliability: high
---

**모델**: black-forest-labs/FLUX.1-schnell · 다운로드 30일 **287,421**(볼트 API 11-25 — 수집기 값과 정확 일치) · 누적 23,773,655(일치) · 좋아요 6,941(일치) · trendingScore 42(트렌딩 71위) · HF 내부 ID `66aa974d…` · Apache-2.0 · gated(자동 승인) · safetensors **11,891,178,560**(일치) · 생성 2024-07-31 · 수정 2026-11-19 — [[기준선-재부상]]

## 핵심 인사이트
> [!insight] 상업 이용 가능한 고속 T2I의 "기준선 좌표" — 1–4스텝 · Apache-2.0 · 12B
> 잠재 적대적 확산 증류(LADD)로 1–4스텝 생성하는 12B 플로우 트랜스포머. diffusers `FluxPipeline`(guidance 0, 4스텝, max_seq 256) · ComfyUI · 공식 레퍼런스 구현, Replicate · fal 등 API. 볼트에서는 [[Qwen-Image-Flash]] 의 비교 대상으로만 언급되다가 이번에 독립 등록 — **"상업 이용 가능 고속 T2I 기준선"의 좌표를 잡는 페이지**. 2024년 모델이며 카드 수정일 2026-11-19가 트렌딩 재진입 시점과 겹치나 변경 내용은 확인하지 못했다.

> [!note] 카드 한계
> **벤치 수치 없음** — "클로즈드 모델과 대등" 서술뿐. 한계 섹션: 사실 정보 제공 불가, 프롬프트 스타일에 크게 좌우. 최신 모델 대비 품질 비교 근거는 카드에 없다.

## 도메인별 추출 (ai-news)
- **즉시 활용**: 상업 이용(Apache-2.0) + 4스텝 조합이 필요한 T2I 파이프라인의 기본값. BF16 기준 VRAM 요구가 커서 개인 GPU에선 CPU 오프로드 · 양자화 필요.
- **대체 관계**: [[Qwen-Image-Flash]] 등 신형 대비 품질은 미확인(카드에 비교 없음) — 라이선스 · 속도가 우선인 경우의 기준선.
- **액션**: 없음(관찰 — T2I 필요 시 기준선으로 사용).

## 관련 페이지
- [[Black-Forest-Labs]] · [[Qwen-Image-Flash]] · [[기준선-재부상]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/black-forest-labs/FLUX.1-schnell
- 확인 범위: HF API 재확인(볼트 11-25 — dl30 · 누적 · 좋아요 · safetensors · 생성일 전부 정확 일치) · 모델 카드(수집기 11-25 — gated라 카드 본문 HTML 판독) · 실행 0
- 신뢰도: ⭐⭐⭐ (수치 API 정확 일치 · 단 품질 벤치는 카드에 없음)
