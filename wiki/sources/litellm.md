---
title: BerriAI/litellm — 100+ LLM API 단일 인터페이스 SDK·게이트웨이
type: source
domain: ai-news
tags: [ai-news, github-trending, llm-infra, api-gateway, cost-tracking, load-balancing, sdk]
created: 2026-05-13
updated: 2026-05-13
sources: []
reliability: high
---

# BerriAI/litellm

> [!insight] 핵심 인사이트
> OpenAI·Anthropic·Cohere·HuggingFace 등 100개+ LLM API를 **단일 OpenAI 호환 인터페이스**로 통합하는 SDK + 프록시 게이트웨이. 비용 추적, 로드밸런싱, fallback, 캐싱을 내장. 멀티-LLM 프로덕션 시스템 구축의 핵심 인프라.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — GitHub ⭐46,782 (+147, 2026-05-13), BerriAI 공식 유지, 엔터프라이즈 사용 사례 풍부
- **즉시 활용**: YES — `pip install litellm` 즉시 사용. OpenAI SDK 코드 변경 최소화로 전환 가능
- **6개월 영향력**: 멀티-LLM 전략(Claude + DeepSeek + GPT fallback)의 표준 게이트웨이로 정착. 모델 가격 급변 시대에 vendor lock-in 방지 핵심 도구
- **대체 관계**: 직접 API 호출 대체. [[openai-agents-python]]과 연계 시 멀티프로바이더 에이전트 구축 가능
- **허와 실**: SDK는 훌륭하지만 프록시 서버 모드는 별도 인프라 필요. 완전 관리형은 BerriAI 유료
- **액션**: 멀티-LLM 앱 개발 시 첫 번째로 도입할 라이브러리

> [!action] 당장 할 것
> Claude Code + DeepSeek fallback 구성 시 litellm 프록시 활용 검토

> [!note] 배경 정보
> LLM API 가격 경쟁이 치열해진 2026년, 특정 프로바이더에 종속되지 않는 아키텍처의 중요성 증가. litellm은 이 전환 비용을 최소화하는 핵심 추상화 레이어

## 관련 페이지

- [[AI-에이전트-프레임워크]]
- [[hermes-agent]]
- [[openai-agents-python]]
- [[Zhipu AI]]
- [[DeepSeek-V4-Pro]]

## 원본

- 출처: https://github.com/BerriAI/litellm
- GitHub 스타: ⭐46,782 (+147, 2026-05-13)
- 신뢰도: ⭐⭐⭐⭐⭐ (대형 커뮤니티, 엔터프라이즈 채택)
