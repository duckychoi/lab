---
title: Alibaba — Qwen 시리즈·오픈 에이전트 개발 빅테크
type: entity
domain: ai-news
tags: [ai-news, entity, alibaba, qwen, china, big-tech]
created: 2026-06-26
updated: 2026-07-10
sources: [zvec.md, Qwen3.6-27B.md]
reliability: high
---

# Alibaba (알리바바)

> [!insight] 핵심 인사이트
> 중국 빅테크로, [[Qwen]] 계열 오픈 LLM·멀티모달 모델과 다수 오픈소스 에이전트를 공개해 온 조직. 2026-06-26 기준 GitHub에 **[[page-agent]]**(인페이지 웹 GUI 조작 에이전트, ⭐20,091)를, HF 데일리에 **[[Qwen-Image-Agent]]**(이미지 생성 컨텍스트 보강 에이전트)를 동시에 올리며 *에이전트형 제품군*을 빠르게 확장 중. [[Zhipu AI]]([[GLM-5.2]])와 함께 중국발 오픈 가중치·오픈소스 에이전트 생태계의 양대 축.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 대형 빅테크, Qwen 브랜드의 일관된 오픈 공개 이력.
- **즉시 활용**: 모델(Qwen 오픈 가중치)·도구([[page-agent]]) 모두 직접 사용 후보. 웹 자동화·이미지 생성 워크플로우에 끼울 여지.
- **6개월 영향력**: "모델 + 에이전트 + 자동화 도구"를 묶어 공개하는 전략이 [[Zhipu AI]]·[[NousResearch]]와 함께 오픈 에이전트 인프라 경쟁을 가속.

> [!note] 2026-07-09 추가 — 인프라로 확장
> 모델·에이전트에 이어 **데이터 인프라**로 저변을 넓힘. **[[zvec]]**(인프로세스 벡터 DB, ⭐14,573·Apache 2.0·C++)를 공개해 "별도 서버 없이 앱에 임베드하는 RAG/벡터 검색"을 겨냥 — 오픈 모델([[Qwen]])·에이전트([[page-agent]])에 이어 **검색·메모리 하부 레이어**까지 오픈으로 채우는 풀스택 포지션.

> [!note] 2026-07-10 추가 — 플래그십 멀티모달 실측
> 대표 오픈 모델 **[[Qwen3.6-27B]]**의 스펙을 모델카드로 확정: **Gated DeltaNet+Gated Attention 하이브리드**·262K(→1M YaRN)·**멀티모달(텍스트+이미지+비디오)**, SWE-bench Verified 77.2·AIME2026 94.1·VideoMME 87.7, Apache 2.0·월간 DL 4.84M. [[ThinkingCap-Qwen3.6-27B-GGUF]]·[[Qwen3.6-27B-NVFP4]] 등 파생 생태계까지 형성 — Qwen이 "오픈 멀티모달 기준선" 지위를 실측 수치로 재확인.

> [!note] 2026-07-11 추가 — 35B-A3B 파생 3종 동시 관측
> [[Qwen3.6-35B-A3B]] 계열이 **효율·특화·커뮤니티 세 갈래 파생**으로 확장: **[[Qwen3.6-35B-A3B-MTP-GGUF]]**(unsloth, DL 77만·MTP 자기투기 1.5-2배 가속·262K→1M·멀티모달)·**[[Qwopus3.6-35B-A3B-Coder-MTP-GGUF]]**(Jackrong, DL 31.8만·코딩 특화·thinking-off·SWE-bench 자가 62.4%)·**[[Qwen3.6-40B-Deckard-Heretic]]**(DavidAU, DL 42.7만·커뮤니티 병합·⚠️카드 미검증). Qwen 오픈 가중치가 **MTP 가속·코딩·창작**으로 재배포되며 로컬 생태계의 사실상 기반임을 재확인.

## 관련 페이지

- [[page-agent]]
- [[Qwen-Image-Agent]]
- [[zvec]] — 인프로세스 벡터 DB (2026-07-09)
- [[Qwen3.6-27B]] — 플래그십 오픈 멀티모달 (2026-07-10 실측)
- [[Qwen3.6-35B-A3B]] — Qwen 오픈 모델 계열
- [[Qwen3.6-35B-A3B-MTP-GGUF]] — MTP 가속 배포 (2026-07-11)
- [[Qwopus3.6-35B-A3B-Coder-MTP-GGUF]] — 코딩 특화 (2026-07-11)
- [[Zhipu AI]]
- [[AI-에이전트-프레임워크]]

## 원본
- 대표 산출물: [[page-agent]] (GitHub ⭐20,091), [[Qwen-Image-Agent]] (HF papers)
- 신뢰도: ⭐⭐⭐⭐ (빅테크, Qwen 오픈 모델 계보)
