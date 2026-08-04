---
title: vLLM — LLM 고처리량·메모리 효율 추론 및 서빙 엔진
type: source
domain: ai-news
tags: [ai-news, github-trending, llm, inference, serving, production, pageattention, throughput, local-llm]
created: 2026-06-17
updated: 2026-06-17
sources: []
reliability: high
---

# vLLM

## 핵심 인사이트

> [!insight] 프로덕션 LLM 서빙의 사실상 표준 — PagedAttention으로 메모리 효율을 혁신
> PagedAttention 알고리즘으로 GPU 메모리를 최대 효율로 사용하는 LLM 추론 엔진. 오픈소스 LLM 프로덕션 배포의 사실상 표준(de facto standard). GitHub ⭐83,131이 이를 증명.

## 도메인별 추출

**핵심 기능:**
- GitHub ⭐83,131, 당일 +124 — 성숙기 안정 성장
- PagedAttention: KV 캐시를 OS 페이지처럼 관리 → 메모리 낭비 없음
- 처리량: 기존 HuggingFace Transformers 대비 최대 24배
- OpenAI API 호환 서버 제공 → 기존 코드 무수정 교체 가능
- 지원 모델: [[Qwen3.6-27B]], [[DeepSeek-V4-Pro]], [[Kimi-K2.7-Code]] 등 대부분 오픈 LLM

**실용성:**
- 실배포 가능? YES — 단일 GPU부터 멀티노드 분산까지
- 즉시 설치: `pip install vllm`
- [[LMCache]]와 조합 시 KV 캐시 오프로딩으로 더 큰 모델 서빙 가능

> [!action] 로컬 LLM 서빙 인프라 구축 시 vLLM → 제1 선택지. OpenAI 드롭인 대체로 기존 코드 재사용

## 관련 페이지
- [[LMCache]]
- [[DeepSeek-V4-Pro]]
- [[Kimi-K2.7-Code]]
- [[local-llm]]
- [[open-webui]]
- [[litellm]]

## 원본
- 출처: https://github.com/vllm-project/vllm
- GitHub ⭐83,131 (2026-06-17 기준, +124/일)
- 신뢰도: ⭐⭐⭐⭐⭐
