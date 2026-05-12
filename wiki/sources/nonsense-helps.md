---
title: Nonsense Helps — 프롬프트 노이즈로 추론 탐색 공간 확장
type: source
domain: ai-news
tags: [ai-news, prompt-engineering, reasoning, exploration, noise, llm-reasoning, perturbation]
created: 2026-05-08
updated: 2026-05-08
sources: []
reliability: medium
---

# Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration

> [!insight] 핵심 인사이트
> 프롬프트에 **의도적 노이즈(nonsense)**를 추가하면 LLM의 추론 탐색 공간이 넓어져 성능이 향상됨. 직관에 반하지만 — "완벽한 프롬프트"보다 약간 불완전한 프롬프트가 더 다양한 추론 경로를 탐색하게 만든다.

## 핵심 인사이트

> [!insight] 프롬프트 엔지니어링의 반직관적 발견
> "깔끔하고 정확한 프롬프트 = 최선"이라는 통념에 도전. 노이즈가 추론 샘플링 다양성을 높여 어려운 수학/논리 문제에서 성능 향상 확인. Self-consistency·majority voting과 결합 시 효과 극대화 가능.

> [!action] 당장 할 것
> 복잡한 추론 작업(수학, 코드 생성, 계획)에서 프롬프트 끝에 무관한 문장 추가 실험. wiki 쿼리 응답 품질 향상 여부 테스트.

> [!note] 관련 연구 맥락
> [[Nonsense Helps]]는 [[에이전트-메모리-레이어]]의 프롬프트 구성 전략에도 적용 가능 — 에이전트에게 제공하는 컨텍스트에 약간의 노이즈가 창의적 해결책을 유도할 수 있음.

## 도메인별 추출 (ai-news)

- **신뢰도**: arXiv 2605.05566 → 중간
- **즉시 활용**: YES — 현재 프롬프트에 즉시 적용 가능 (비용 0)
- **6개월 영향력**: 프롬프트 엔지니어링 표준 기법으로 채택 가능성 (특히 chain-of-thought + noise)
- **대체 관계**: 단순 zero-shot 프롬프트보다 복잡 추론에서 우위 주장

## 관련 페이지

- [[Claude-Code-워크플로우]]
- [[andrej-karpathy-skills]]
- [[에이전트-메모리-레이어]]
- [[AI-에이전트-프레임워크]]

## 원본

- 출처: https://huggingface.co/papers/2605.05566
- arXiv: 2605.05566
- 신뢰도: ⭐⭐⭐ (arXiv, 즉시 적용 가능한 실용적 발견)
