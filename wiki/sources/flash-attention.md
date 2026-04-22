---
title: Dao-AILab/flash-attention — 메모리 효율 정확 어텐션 구현
type: source
domain: ai-news
tags: [ai-news, github-trending, attention, LLM, transformer, gpu, cuda, performance, inference]
created: 2026-04-12
updated: 2026-04-12
sources: []
reliability: high
---

# Dao-AILab/flash-attention

> [!insight] 핵심 인사이트
> 트랜스포머 어텐션의 메모리-시간 복잡도를 획기적으로 줄인 CUDA 최적화 구현. LLM 학습·추론의 사실상 표준 라이브러리. ⭐23,304 — 수년간 검증된 인프라 레이어.

## 핵심 인사이트

> [!note] 배경 정보
> Tri Dao(MIT → Together AI)의 연구 결과물. 어텐션 계산을 타일 기반으로 재구성해 GPU SRAM 활용을 극대화. 기존 O(n²) 메모리를 O(n)으로 줄이면서 정확도 유지. PyTorch 2.x에 일부 통합됨. 대부분의 최신 LLM 학습 파이프라인에 표준 적용.

> [!note] 현황
> ⭐23,304은 AI 인프라 레포 기준 상위권. 수년간 안정적으로 사용됨 — 트렌딩 재진입은 Gemma-4·GLM-5.1 등 대형 모델 출시로 인한 학습 인프라 관심 상승 반영.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐23,304, 업계 표준, Together AI 공식 지원
- **즉시 활용**: YES — pip install flash-attn, PyTorch LLM 파이프라인에 즉시 적용
- **6개월 영향력**: 변화 없음 — 이미 LLM 인프라 표준. 지속 유지 필요
- **대체 관계**: PyTorch 내장 SDPA 대체 또는 병행 사용
- **허와 실**: CUDA 전용, NVIDIA GPU 필수. AMD/Apple Silicon 대안 별도 필요
- **액션**: 현재 LLM 파이프라인 적용 여부 확인. 미적용 시 즉시 추가

## 관련 페이지

- [[GLM-5.1]] — 대형 MoE 모델, flash-attention 활용 가능성
- [[Gemma-4-31B]] — 학습/추론에 flash-attention 사용
- [[local-llm]] — 로컬 LLM 추론 최적화

## 원본

- 출처: https://github.com/Dao-AILab/flash-attention
- 스타: 23,304 (2026-04-12 기준)
- 신뢰도: ⭐⭐⭐⭐⭐
