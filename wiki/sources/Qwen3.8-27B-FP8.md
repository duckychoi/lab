---
title: Qwen3.8-27B-FP8 — Qwen3.8-27B FP8 양자화판 (Alibaba 공식)
type: source
domain: ai-news
tags: [ai-news, hf-model, fp8, quantization, local-inference, qwen, alibaba, local-llm]
created: 2026-08-19
updated: 2026-08-19
sources: []
reliability: medium
---

# Qwen/Qwen3.8-27B-FP8 — 공식 FP8 양자화판

**HF 모델**: https://huggingface.co/Qwen/Qwen3.8-27B-FP8
**지표**: DL **741,011** · 좋아요 **575** (2026-08-19 자동수집) · **형식**: FP8 (양자화·image-text-to-text) · **배포**: [[Alibaba]] Qwen 공식
**원본**: [[Qwen3.8-27B]] (베이스 원본·image-text-to-text)

> [!insight] 핵심 인사이트
> [[Alibaba]] Qwen 팀이 **직접 배포한 공식 FP8 양자화판** — 베이스 [[Qwen3.8-27B]]를 FP8로 눌러 **GPU 서버/워크스테이션의 메모리 절감·추론 가속**을 노린다. 주목점은 같은 베이스가 **두 갈래 양자화 경로**로 갈라진다는 것: 커뮤니티 [[unsloth]]의 **GGUF 재배포([[Qwen3.8-27B-GGUF]]·DL 3.56M·CPU/llama.cpp·워크스테이션)** ↔ Qwen **공식 FP8(GPU 텐서코어·서버)**. 즉 "실행 환경(CPU/엣지 vs GPU 서버)에 따라 양자화 포맷이 분화"되는 구도가 한 모델에서 정량으로 드러남 — GGUF가 DL 약 4.8배로 저변은 로컬 CPU 경로가 더 두껍고, FP8은 공식·서버 배포 신뢰도가 강점. [[LLMRouter]]가 라우팅할 후보 스펙트럼에서 FP8은 "GPU 서버 저비용" 게이트에 자연스러운 자리.

> [!warning] 신뢰도 — 접근성 지표·벤치 미기재 (medium)
> DL 741,011·좋아요 575는 raw 자동수집 수치이며 **실WebFetch 미수행**(타임라인 2026-08 유지). 다운로드·좋아요는 **접근성·관심 지표이지 품질 근거가 아니다**. 베이스 아키텍처·컨텍스트·벤치, FP8 양자화의 품질 손실·요구 하드웨어(FP8 지원 GPU: Hopper/Ada급 등)는 **raw 미기재 → 원문 재현 전 미검증**([[CLAUDE.md]] 사실확인 원칙). "27B"는 모델명 기준·활성 파라미터/밀집 여부는 원문 대조 전 미확정.

## 도메인별 추출 (ai-news · 교차 local-llm)

- **신뢰도**: DL 741k·좋아요 575 (raw)·공식 배포이나 벤치/손실 미기재 → medium
- **즉시 활용**: 조건부 YES — FP8 지원 GPU가 있으면 서버 추론 메모리를 크게 줄일 수 있는 공식 경로. 실제 품질은 스팟체크 필요.
- **6개월 영향력**: 오픈 웨이트 벤더가 GGUF(커뮤니티)와 별개로 **공식 저정밀 웨이트(FP8)**를 함께 내는 게 표준화되는 흐름. 실행 환경별 포맷 분화가 굳어짐.
- **대체 관계**: 로컬 CPU/워크스테이션은 [[Qwen3.8-27B-GGUF]], GPU 서버는 이 FP8판 — 상호 대체가 아니라 **환경별 상보**.
- **허와 실**: DL 741k은 접근성일 뿐 품질 아님. FP8 손실·하드웨어 요건이 실체.
- **액션**: FP8 GPU 보유 시 동일 프롬프트로 GGUF(Q4/Q5) 대비 품질·지연 비교(낮음).

## 관련 페이지
- [[Qwen3.8-27B]] — 공통 베이스 원본
- [[Qwen3.8-27B-GGUF]] — 같은 베이스 GGUF 재배포(CPU/워크스테이션 경로·환경별 상보)
- [[Alibaba]] — 공식 배포 주체
- [[unsloth]] — GGUF 재배포 주체(경로 대비)
- [[omlx]] — 같은 배치 로컬 실행 계층
- [[LLMRouter]] — 환경별 양자화 후보를 편입할 라우팅 계층
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/Qwen/Qwen3.8-27B-FP8
- 지표: DL 741,011 · 좋아요 575 (2026-08-19 자동수집)
- 신뢰도: ⭐⭐⭐ (공식 배포·DL 741k raw 자동수집·FP8 손실/하드웨어 요건 미검증 medium)
- 수집: 2026-08-19 아침 자동수집 (HF 모델)
