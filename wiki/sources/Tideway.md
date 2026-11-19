---
title: "Tideway — 소비자 PC에서 VRAM·RAM을 한 풀로 묶는 단계 인식 MoE 추론 (지연 1.97× · TTFT 2.40× · decode 1.61×)"
type: source
domain: local-llm
tags: [local-llm, moe, offloading, consumer-gpu, inference, paper]
created: 2026-11-19
updated: 2026-11-19
sources: [https://huggingface.co/papers/2611.14848]
reliability: medium
---

**논문**: arXiv 2611.14848 · HF Daily 11-19 **1위** · 업보트 60 · Duke University · 코드 [Afterglow231/Tideway](https://github.com/Afterglow231/Tideway)

## 핵심 인사이트
> [!insight] 계층을 "독립 캐시"로 두면 스래싱한다 — VRAM + 호스트 RAM 을 하나의 풀로
> MoE 가중치가 VRAM · RAM · SSD 로 넘칠 때 기존 시스템은 각 층을 독립 캐시로 다뤄 스래싱한다는 관찰. Tideway 는 단일 풀 안에서 **prefill / decode 의 서로 다른 접근 패턴에 맞춰 메모리 배치를 바꾸고**, 전문가 페이징 하에서 CUDA Graph 실행을 최적화한다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 소비자 GPU + 대형 MoE(로컬 배포) 정조준. 코드 공개.
- **메모리 아키텍처**: 가중치 오프로딩 계층 관리(KV 아님).
- **트레이드오프 (초록 · 볼트 대조)**: 가장 빠른 기준선 대비 **평균** 종단 지연 1.97× · TTFT 2.40× · decode 처리량 1.61×. 🔴 하드웨어 · 모델 구성 · 기준선 이름은 초록에 없음(본문 미열람).
- **Hermes 적용**: 현 ChinameBot 이 소형 dense 모델이면 무관. 대형 MoE 로컬 시험 시 llama.cpp 오프로딩과 비교 후보.
- **오픈소스 구현체**: 있음.

> [!question] 미해결
> "fastest baseline" 이 llama.cpp · KTransformers · MoE-Infinity 중 무엇인지, SSD 까지 넘치는 설정의 수치인지 — 본문 확인 필요.

## 관련 페이지
- [[openvino]] · [[dflash]] · [[MMFlash]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2611.14848
- 확인 범위: HF papers API(초록 전문 · 업보트 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐ (코드 공개 · 초록 수치)
