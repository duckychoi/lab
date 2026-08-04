---
title: agentscope — 관측·디버깅 가능한 멀티 에이전트 애플리케이션 프레임워크
type: source
domain: ai-news
tags: [ai-news, agent-framework, multi-agent, observability, production, local-llm]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: high
---

# agentscope-ai/agentscope

> [!insight] 핵심 인사이트
> "**보고·이해하고·신뢰할 수 있는** 에이전트를 만든다"를 표방하는 프로덕션급 멀티 에이전트 프레임워크. ⭐27,749. 2.0에서 **이벤트 버스·권한 시스템·멀티테넌시/멀티세션·샌드박스(local/Docker/E2B/OpenSandbox)·확장 미들웨어**를 갖춰, 프롬프트로 억누르지 않고 **모델의 추론·도구 사용을 그대로 살리는** 설계. 웹 UI로 에이전트 동작·태스크 계획·권한을 실시간 관측.

**GitHub**: https://github.com/agentscope-ai/agentscope  
**스타**: ⭐27,749 (당일 +77)  
**신뢰도**: ⭐⭐⭐⭐ (27.7K 스타·Apache 2.0)

## 도메인별 추출

- **신뢰도**: ⭐⭐⭐⭐ — 27.7K 스타·3.2K forks·Apache 2.0. 프로덕션 지향(멀티테넌시·세션 격리) 성숙도
- **즉시 활용**: YES — 관측·권한·샌드박스가 필요한 다중 에이전트 서비스. 웹 UI 디버깅으로 "에이전트가 왜 그렇게 했나"를 추적 가능 = 스케줄/무인 태스크 신뢰성에 직결
- **6개월 영향력**: "agentic LLM 전제" 설계 = 강한 모델일수록 강해지는 프레임워크. [[deer-flow]]·[[AI-에이전트-프레임워크]]와 함께 "관측 가능성"이 에이전트 프레임워크 선택 기준으로 부상
- **대체 관계**: 순수 오케스트레이션([[herdr]]·[[orca]] 병렬 플릿)보다 **애플리케이션 프레임워크** 층 — LangGraph/AutoGen 계열 경쟁. RAG·장기메모리·human-in-the-loop 내장
- **허와 실**: "production-ready" 마케팅 대비 실제 운영 안정성은 검증 필요. 다만 이벤트/권한/샌드박스 조합은 실전 요구를 정확히 겨냥
- **액션**: 웹 UI 관측 기능만이라도 떼어 현재 스케줄 에이전트 디버깅에 적용 검토

> [!action] 당장 할 것
> agentscope 웹 UI의 이벤트·권한 관측 기능을 로컬에서 띄워, 멀티 에이전트 태스크의 의사결정 추적 UX를 벤치마킹한다.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[deer-flow]]
- [[에이전트-메모리-레이어]]
- [[herdr]]
- [[orca]]

## 원본
- 출처: https://github.com/agentscope-ai/agentscope
- 신뢰도: ⭐⭐⭐⭐ (27.7K 스타·Apache 2.0)
