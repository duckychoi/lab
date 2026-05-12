---
title: jundot/omlx — Apple Silicon 전용 LLM 추론 서버
type: source
domain: ai-news
tags: [ai-news, github-trending, local-llm, apple-silicon, continuous-batching, ssd-cache, macos, edge-ai]
created: 2026-05-11
updated: 2026-05-11
sources: []
reliability: high
---

# jundot/omlx

> [!insight] 핵심 인사이트
> ⭐**13,485** (+185 오늘) — Apple Silicon 전용 LLM 추론 서버로 **continuous batching + SSD 캐싱** 조합. macOS 메뉴바에서 직접 관리. Metal GPU 활용 극대화로 Mac 사용자가 로컬에서 대형 모델을 실용적으로 돌릴 수 있는 기반. [[Qwen3.6-35B-A3B-GGUF]] 같은 GGUF 모델과 조합하면 Mac에서 35B MoE 모델 실행이 현실적.

## 도메인별 추출 (local-llm)

- **실용성 판단**: Apple Silicon(M1/M2/M3/M4) Mac 전용 — continuous batching으로 다중 요청 효율 처리, SSD 캐싱으로 VRAM 초과 모델 실행 가능
- **메모리 아키텍처**: SSD 캐싱 — 모델 가중치를 SSD에 두고 필요 시 Metal로 스트리밍, 통합 메모리 구조(UMA) 최대 활용
- **트레이드오프**: SSD 속도(~3GB/s) vs DRAM 속도(~100GB/s) 차이로 SSD 캐시 활용 시 속도 감소 있으나, 메모리 초과 모델 실행 가능성이 핵심 가치
- **오픈소스 구현체**: https://github.com/jundot/omlx — 직접 설치 가능
- **즉시 활용**: YES (Mac 사용자 한정)
- **6개월 영향력**: Apple Silicon Mac에서 GPT-4급 모델 로컬 실행 기준점이 될 가능성. [[Qwen3.6-27B]], [[Mistral-Medium-3.5-128B]] 같은 모델 로컬 실행 실용화

## 핵심 내용

- Continuous batching: 여러 사용자/요청을 병렬 처리, 토큰 생성 중 새 요청 삽입 가능
- SSD 캐싱: 통합 메모리 부족 시 NVMe SSD를 2차 캐시로 활용
- macOS 메뉴바 통합: 시스템 트레이에서 서버 상태 모니터링·제어

> [!action] 당장 할 것
> Mac 사용자라면 설치 후 [[Qwen3.6-27B]] 또는 [[Qwen3.6-35B-A3B-GGUF]] 로컬 실행 테스트

## 관련 페이지
- [[Qwen3.6-35B-A3B-GGUF]]
- [[Qwen3.6-27B-GGUF]]
- [[gemma-4-e4b-obliterated]]
- [[minimind]]
- [[에이전트-메모리-레이어]]

## 원본
- 출처: https://github.com/jundot/omlx
- 신뢰도: ⭐⭐ (⭐13,485 GitHub stars)
