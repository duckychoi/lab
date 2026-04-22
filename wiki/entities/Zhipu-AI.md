---
title: Zhipu AI (Z.AI)
type: entity
domain: ai-news
tags: [entity, zhipu-ai, zai, GLM, chinese-llm, MoE, bilingual, monday-ai]
created: 2026-04-10
updated: 2026-04-10
sources: [GLM-5.1.md]
reliability: high
---

# Zhipu AI (Z.AI)

중국 베이징 기반 AI 연구 기업. GLM(General Language Model) 시리즈 개발사. 글로벌 브랜드명은 **Z.AI**.

## 주요 모델

- **GLM-5-Turbo**: 이 위키 어시스턴트 Monday의 기반 모델
- **GLM-5.1**: 753B MoE 아키텍처, 한국어+영어 이중 언어, MIT 라이선스 (2026-04-08 출시)
- GLM 시리즈: arXiv 2602.15763 기반, `glm_moe_dsa` 아키텍처 (Dynamic Sparse Attention)

> [!insight] 핵심 인사이트
> 오픈소스(MIT) + 한국어 강점 + MoE 효율 세 가지를 모두 갖춘 드문 케이스. 중국 오픈소스 LLM의 글로벌 경쟁력 입증.

> [!note] Monday 연관성
> **Monday(이 AI 어시스턴트)는 GLM-5-Turbo 기반**으로 구동된다. GLM-5.1은 동일 계열 최신 MoE 버전.

## 인퍼런스 서비스

- HuggingFace: https://huggingface.co/zai-org
- Together AI, Fireworks AI 파트너십

## 관련 페이지

- [[GLM-5.1]] — 최신 MoE 모델
- [[local-llm]]
