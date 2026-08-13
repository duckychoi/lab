---
title: Long-Horizon Consistency — LLM 에이전트 장기 일관성 벤치 (2608.08160)
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent, benchmark, long-horizon, consistency, interactive-narrative]
created: 2026-08-13
updated: 2026-08-13
sources: []
reliability: medium
---

# Can LLM Agents Stick to the Script? — Long-Horizon Consistency Benchmark

**HF 논문**: https://huggingface.co/papers/2608.08160
**지표**: HF 데일리 **4위** · 업보트 24 (2026-08-13 자동수집)

> [!insight] 핵심 인사이트
> **인터랙티브 내러티브(대화형 시나리오)에서 LLM 에이전트가 긴 상호작용 동안 설정·페르소나·규칙을 얼마나 유지하는지(long-horizon consistency)를 측정하는 벤치마크**(제목·raw 기반). 08월 위키가 자율성·자기진화([[Co-Evolution-Agentic]])와 안전([[OpenART]])으로 확장되는 가운데, 이 논문은 그 반대편 — **"에이전트가 오래 가면 대본에서 이탈한다"**는 실전 약점을 정면으로 계량화한다. 롱컨텍스트([[Kimi-K3]] 1M·[[OasisKV]] KV 확장)가 "얼마나 많이 담나"라면, 이 벤치는 "담은 걸 끝까지 지키나"를 본다. 내 ChinameBot류 캐릭터 봇·[[shot-wrighter]]/[[reat-script]] 장편 대본 에이전트가 후반부에 페르소나·설정을 흘리는 문제와 정확히 같은 실패 모드라 실무 진단 렌즈로 유용. 데일리 4위·업보트 24(상단 3편보다는 관심 낮음).

> [!warning] 신뢰도 medium — 미래형 arxiv ID, 원문 미재현
> 논문 ID 2608.08160은 **미래형(2026-08) arxiv ID로 원문 초록·수치·방법 재현 불가**. 제목·raw 한줄요약·HF 데일리 순위/업보트만 근거이며, **구체 벤치 점수·평가 대상 모델·태스크 수·저자/소속은 미기재**([[CLAUDE.md]] 사실확인 원칙). 기존 [[Long-Horizon-Terminal-Bench]](터미널 태스크 장기 일관성)와는 **다른 논문**(이쪽은 인터랙티브 내러티브 대상)임에 유의.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐ (medium) — HF 데일리 4위·업보트 24. 원문 미재현.
- **즉시 활용**: 개념 참조 — 장편 대화/대본 에이전트의 후반부 설정 이탈을 진단하는 사고틀. 캐릭터 봇·대본 스킬 QA에 직접 적용.
- **6개월 영향력**: 중 — 에이전트 평가 축이 "단발 정확도"에서 "긴 상호작용 일관성"으로 이동하는 신호.
- **허와 실**: "stick to the script" 프레이밍은 직관적이나, 일관성 측정 지표의 타당성은 원문 확인 필요.
- **액션**: 원문 공개 시 일관성 측정 방식 확인, 내 캐릭터 봇 장기 대화 회귀 테스트에 대입.

## 관련 페이지
- [[Long-Horizon-Terminal-Bench]] — 장기 일관성 벤치(다른 도메인, 대비)
- [[Kimi-K3]] · [[OasisKV]] — 롱컨텍스트 "많이 담기" 축(대비: 지키기)
- [[shot-wrighter]] · [[reat-script]] — 장편 대본 에이전트 실무 접점
- [[ai-news]] — 도메인 누적 인사이트

## 원본
- 출처: https://huggingface.co/papers/2608.08160
- 신뢰도: ⭐⭐ (HF 데일리 4위·업보트 24, 미래형 ID·원문 미재현)
