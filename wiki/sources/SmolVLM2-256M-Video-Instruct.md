---
title: "SmolVLM2-256M-Video-Instruct — 2억5천만 파라미터 영상 이해 VLM"
type: source
domain: local-llm
tags: [local-llm, edge-ai, hf-model, vlm, video-understanding, smolvlm, on-device, baseline-resurfacing]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/HuggingFaceTB/SmolVLM2-256M-Video-Instruct]
reliability: high
---

**모델**: HuggingFaceTB/SmolVLM2-256M-Video-Instruct · 다운로드 30일 **45,464**(수집기 11-24) → **46,018**(볼트 API 11-25) · 누적 2,287,246 → **2,289,290** · 좋아요 432 → **445** · trendingScore 72.5(트렌딩 36위) · HF 내부 ID `67aaf6d9…`(일치 확인) · Apache-2.0 · base_model `HuggingFaceTB/SmolVLM-256M-Instruct` · safetensors **256,484,928**(일치 확인) — 2025-02 모델의 재부상([[기준선-재부상]])

## 핵심 인사이트
> [!insight] 256M에서 영상 이해가 가능하다는 것 자체가 지표 — 정확도는 2.2B 대비 18.4점 낮지만
> [[HuggingFace]] 의 Idefics3 기반 초소형 VLM. 영상 · 다중 이미지 · 텍스트를 섞어 넣고 캡션 · 질의응답 · 비교 · 화면 텍스트 전사를 텍스트로 출력. 영어 전용. **카드 표(SmolVLM2 패밀리)**: 256M — Video-MME 33.7 · MLVU 40.6 · MVBench 32.7 / 500M 42.2 · 47.3 · 39.73 / 2.2B 52.1 · 55.2 · 46.27 — 256M은 2.2B 대비 Video-MME **18.4점 낮다**. 2025-02 출시 모델이 다시 트렌딩에 오른 경우(신규 아님) — "엣지에서 영상을 조금이라도"라는 수요가 지속됨을 보여준다.

> [!note] 한계(카드 기준)
> 타 모델과의 비교 · 메모리 사용량 · 한계 섹션은 카드에 없다 — 패밀리 내 수치만 공개.

## 도메인별 추출 (local-llm)
- **실용성**: 브라우저 · 모바일 · 엣지에서 영상 하이라이트 추출 같은 가벼운 작업용. 256M 파라미터는 CPU/WASM 영역 — 정확도가 필요한 영상 분석엔 크기를 올려야 한다.
- **허와 실**: "영상 이해 VLM"이라는 표기는 맞지만 Video-MME 33.7은 대형 VLM 대비 절반 수준 — "가능"과 "쓸만"의 갭이 18.4점.
- **액션**: 없음(관찰 — 엣지 영상 처리 요구 발생 시 후보).

## 관련 페이지
- [[HuggingFace]] · [[기준선-재부상]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/HuggingFaceTB/SmolVLM2-256M-Video-Instruct
- 확인 범위: HF API 재확인(볼트 11-25 — dl30/누적/좋아요/내부 ID/safetensors/생성일 전부 일치) · 모델 카드 패밀리 표(수집기 11-24) · 실행 0
- 신뢰도: ⭐⭐⭐ (수치 API 검증 · 패밀리 내 비교만 존재라 타 모델 대비 위치는 미확인)
