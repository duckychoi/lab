---
title: Qwen3.6-35B-Uncensored (HauhauCS) — 커뮤니티 검열 제거 파인튜닝 (2.23M DL)
type: source
domain: ai-news
tags: [ai-news, local-llm, Qwen3.6, uncensored, finetune, MoE, community, text-generation, creative]
created: 2026-05-30
updated: 2026-06-04
sources: []
reliability: medium
---

# Qwen3.6-35B-Uncensored — 검열 제거 커뮤니티 파인튜닝

## 핵심 인사이트

> [!insight] 핵심 인사이트
> HauhauCS의 Qwen3.6 35B A3B(MoE, 활성 3B) 기반 검열 제거 파인튜닝. HF 다운로드 **2,230,000** — 이 수치는 이례적. 커뮤니티의 "무검열 LLM" 수요가 공식 모델 채택 속도를 월등히 앞서는 현상 증명. 창작·리서치용 제약 없는 텍스트 생성이 주 용도.

> [!warning] 주의 / 신뢰도 낮음
> 개인 파인튜닝 모델이므로 품질 안정성 미보장. 불법/유해 콘텐츠 생성에 악용 가능성. 공식 Qwen3.6-35B-A3B([[Qwen3.6-35B-A3B]])와 성능 비교 시 task에 따라 차이 있을 수 있음.

## 도메인별 추출 (local-llm 템플릿)

- **실용성 판단**: YES (로컬 GPU/CPU 환경) — MoE 구조로 실제 활성 파라미터는 3B. 일반 소비자 GPU에서도 실행 가능
- **하드웨어**: A3B 활성 → 고성능 CPU 또는 8~16GB VRAM GPU에서 실행 가능 (GGUF 양자화 버전 추천)
- **메모리 아키텍처**: MoE — 토큰별로 3B 전문가만 활성화, 전체 35B 로딩 필요하지만 추론 시 효율적
- **오픈소스 구현체**: https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive

> [!action] 당장 할 것
> GGUF 양자화 버전([[Qwen3.6-35B-A3B-GGUF]]) 검색 후 ollama/llama.cpp로 로컬 테스트. 창작 시나리오 품질 vs 공식 모델 비교 실험.

## 맥락 분석

**2.23M 다운로드의 의미:**
- 공식 Qwen3.6-35B-A3B(583K)의 약 4배
- 커뮤니티가 "제약 없는 모델"에 더 높은 수요
- "모델 민주화 + 검열 해제" 수요는 지속적이며 커뮤니티 주도로 해결됨
- HF 플랫폼이 이런 모델을 허용하는 정책 → 분산 배포 생태계 건전성 반영

## 관련 페이지

- [[Qwen3.6-35B-A3B]] — 공식 베이스 모델
- [[Qwen3.6-35B-A3B-GGUF]] — 공식 GGUF 양자화 버전
- [[에이전트-메모리-레이어]] — 검열 없는 모델 활용 시 프라이버시 에이전트 구성
- [[local-llm]] — 로컬 LLM 도메인 인사이트

## 원본

- 출처: https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
- 다운로드: 2,230,000 (2026-05-30 기준)
- 신뢰도: ⭐⭐⭐ (커뮤니티 파인튜닝, 검증 미흡)
