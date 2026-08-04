---
title: asgeirtj/system_prompts_leaks
type: source
domain: ai-news
tags: [ai-news, prompt-engineering, system-prompt, github-trending, reference]
created: 2026-07-05
updated: 2026-07-05
sources: [system_prompts_leaks.md]
reliability: medium
---

# asgeirtj/system_prompts_leaks

Anthropic·OpenAI·Google·xAI 등 주요 LLM 서비스의 시스템 프롬프트 추출본 모음. 프롬프트 엔지니어링 리버스 참고용 레퍼런스.

## 핵심 인사이트

> [!insight] "프론티어 서비스의 프롬프트 설계를 역공학"
> 상용 챗 서비스가 실제로 어떻게 톤·안전장치·도구사용을 지시하는지 원문 수준으로 관찰 가능. [[system-prompts-and-models-of-ai-tools]]와 짝을 이루는 참고 자산으로, 내 봇/에이전트 프롬프트 설계 시 "검증된 프레이징"을 빌려올 수 있다.

> [!warning] 신뢰도 / 저작권 주의
> "추출본(leak)"은 버전·정확성이 보장되지 않으며 시점에 따라 낡는다. 그대로 복붙 시 서비스 약관·저작권 이슈 소지. 설계 패턴 참고용으로만 활용.

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub ⭐49,225 (+471/일). 콘텐츠 자체는 비공식 추출이라 medium.
- **즉시 활용**: 부분 YES — 프롬프트 구조(역할 정의, 거절 처리, 도구 지시) 패턴을 내 에이전트에 참고.
- **6개월 영향력**: 프롬프트 설계 관행의 상향 평준화. "무엇을 지시해야 하는가"의 공용 레퍼런스화.
- **대체 관계**: 대체 아님 — [[system-prompts-and-models-of-ai-tools]] 보완.
- **허와 실**: 마케팅 없음. 다만 정확성·최신성 미보장.
- **액션**: 거절/안전/도구지시 섹션만 발췌해 패턴 노트화.

## 관련 페이지
- [[system-prompts-and-models-of-ai-tools]]
- [[Claude-Code-워크플로우]]
- [[agent-skills]]

## 원본
- 출처: https://github.com/asgeirtj/system_prompts_leaks
- 신뢰도: ⭐⭐ (GitHub ⭐49,225 / 콘텐츠는 비공식 추출)
