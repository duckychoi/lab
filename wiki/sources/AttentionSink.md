---
title: Attention Sink in Transformers — 종합 서베이
type: source
domain: ai-news
tags: [ai-news, transformer, attention, interpretability, survey, llm-research]
created: 2026-04-14
updated: 2026-04-14
sources: []
reliability: high
---

# Attention Sink in Transformers: A Survey

> [!insight] 핵심 인사이트
> 트랜스포머에서 [BOS] 토큰 등 특정 위치에 어텐션이 과도하게 집중되는 "어텐션 싱크" 현상을 20명 저자가 종합 조사. 해석·완화·활용 방법론을 체계화한 첫 대형 서베이.

## 핵심 인사이트

> [!note] 배경 정보
> 어텐션 싱크는 StreamingLLM(2023)에서 처음 주목받았다. 싱크 토큰을 유지하면 긴 컨텍스트 생성에서 KV 캐시를 줄일 수 있다는 실용적 발견. 이 서베이는 그 이후 2년간 연구를 정리.

> [!question] 미해결 질문
> 어텐션 싱크가 모델 성능에 실제로 해로운가, 아니면 메모리 효율화에 활용 가능한 현상인가? 연구마다 입장 다름.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — arXiv 2604.10098, 20인 저자 대형 서베이
- **즉시 활용**: MAYBE — 직접 적용보다 [[local-llm]] 최적화 설계 참고용
- **6개월 영향력**: KV 캐시 압축·긴 컨텍스트 추론 최적화에 참고 필수
- **대체 관계**: LLM 추론 최적화([[flash-attention]] 등)와 상호 보완
- **허와 실**: 현상 분류 및 방법론 정리 중심 — 실용 코드 없음
- **액션**: 논문 저장 (local-llm 최적화 필요 시 참조)

## 관련 페이지

- [[flash-attention]]
- [[Mamba4]]
- [[DMax]]

## 원본

- 출처: https://huggingface.co/papers/2604.10098
- 신뢰도: ⭐⭐⭐⭐ (HF 업보트 39, 20인 저자 서베이)
