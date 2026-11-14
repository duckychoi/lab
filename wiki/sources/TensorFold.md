---
title: "ashhart/TensorFold — Zig 단일 바이너리 LLM 추론 서버 (Metal · CUDA, 설명의 "Vulkan"은 README 0건)"
type: source
domain: local-llm
tags: [local-llm, github-trending, inference-engine, zig, metal, cuda, apple-silicon]
created: 2026-11-14
updated: 2026-11-14
sources: [https://github.com/ashhart/TensorFold]
reliability: medium
---

**레포**: [ashhart/TensorFold](https://github.com/ashhart/TensorFold) · ★**2,085** · fork 406 · Apache-2.0 · Zig · repo id 1274723381 · created 2026-06-19 · pushed 2026-11-14T09:00Z · open_issues 566(이슈+PR) (GitHub API 볼트 실측). 수집기는 `ai-news` 로 보냈으나 볼트 재분류 → `local-llm`.

## 핵심 인사이트
> [!insight] Python 도 MLX 도 없이, 체크포인트 로딩부터 OpenAI 호환 서빙까지 바이너리 하나
> 체크포인트 로딩 · 토크나이즈 · Metal/CUDA 커널 실행을 Zig 바이너리 하나로 처리해 `/v1/chat/completions` 를 서빙한다. MLX 4/6-bit · NVFP4 · EXL3 체크포인트, MTP 드래프트, 다중 GB10/M5 Ultra 텐서 병렬([[GLM-5.3-Flash]] TP=2/3) 지원 표가 README 에 있다(수집기 판독). CUDA 는 드라이버 R580+(CUDA 13) 필수.

> [!warning] 설명과 본문이 다르다
> 레포 설명: *"LLM Inference Engine for Metal, CUDA and **Vulkan**."* — README 본문(54,170B · 608행)에서 `vulkan` 대소문자 무시 검색 **0건**(볼트 실측, 수집기와 일치). 지원 여부는 확인되지 않았다 → [[선언된-구현체-공백]].
> 처리량(tok/s)은 README 본문이 아니라 "Community benchmarks"·docs 로 위임. 모델별 "checked on" 하드웨어는 1~2대(README 가 스스로 명시 — 수집기 판독).

## 도메인별 추출 (local-llm)
- **실용성 판단**: Apple Silicon · DGX Spark(GB10) 실험용. 1인 주도 · 5개월 차 · open_issues 566 — 운영 대체재로 보기에는 이르다.
- **메모리 아키텍처**: 해당 없음(추론 런타임).
- **Hermes 적용**: NO(현재) — OpenAI 호환이라 붙일 수는 있으나 검증된 하드웨어 범위가 좁다.
- **트레이드오프**: 의존성 0 · 단일 바이너리 vs 검증 범위·생태계. 속도 수치는 본문에 없다.
- **오픈소스 구현체**: 본 레포. 비교 대상은 [[vllm]] · [[omlx]].

## 관련 페이지
- [[선언된-구현체-공백]] · [[vllm]] · [[omlx]] · [[GLM-5.3-Flash]] · [[local-llm]]

## 원본
- 출처: https://github.com/ashhart/TensorFold
- 확인 범위: GitHub API 메타 · README 전문 내려받아 `vulkan` 검색 · 🔴 지원 표 · 하드웨어 한정 문구는 수집기 판독 · 빌드·실행 미확인
- 신뢰도: ⭐⭐ (★2,085 · 신생 · 처리량 수치 미확인)
