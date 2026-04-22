---
title: jingyaogong/minimind
type: source
domain: ai-news
tags: [ai-news, local-llm, education, gpt, training, minimal, pytorch]
created: 2026-04-20
updated: 2026-04-20
sources: []
reliability: high
---

# jingyaogong/minimind

> [!insight] 핵심 인사이트
> 64M 파라미터 GPT를 2시간 만에 처음부터 학습하는 미니멀 구현 — LLM 내부 구조 이해와 실습에 최적. ⭐47,657로 교육용 LLM 구현체 중 사실상 표준 레포. "LLM 블랙박스 제거"라는 관점에서 [[dive-into-llms]]와 쌍벽.

## 도메인별 추출

**실용성 판단**: 단일 GPU(RTX 3090 급)에서 2시간 학습 가능. 교육·연구 목적 즉시 활용
**메모리 아키텍처**: 표준 Transformer GPT-2 스타일 아키텍처, 단순화된 코드베이스
**Hermes 적용**: ChinameBot 파인튜닝 실험용 기반 코드로 적합
**트레이드오프**: 64M 파라미터로 실제 서비스 품질은 제한적. 학습 목적에 최적화.
**오픈소스 구현체**: https://github.com/jingyaogong/minimind — 바로 사용 가능

## 주요 기능

- 64M 파라미터 GPT 처음부터 학습
- 단일 GPU 2시간 내 완료
- 한국어·중국어·영어 지원
- 토크나이저부터 학습 루프 전체 명시적 구현

> [!action] 당장 할 것
> minimind 클론 후 커스텀 데이터로 파인튜닝 실험 — LLM 파인튜닝 파이프라인 내재화

## 관련 페이지

- [[dive-into-llms]]
- [[local-llm]]
- [[how-to-fine-tune-reasoning-model]]

## 원본

- 출처: https://github.com/jingyaogong/minimind
- 스타: ⭐47,657 (2026-04-20, +214)
- 신뢰도: ⭐⭐⭐⭐⭐
