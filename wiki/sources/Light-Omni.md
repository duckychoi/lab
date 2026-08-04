---
title: Light-Omni — 장기 메모리 기반 에이전트형 비디오 이해
type: source
domain: ai-news
tags: [ai-news, video-understanding, agent, long-term-memory, multimodal, reflex]
created: 2026-07-08
updated: 2026-07-08
sources: []
reliability: low
---

# Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory

**HuggingFace Papers**: https://huggingface.co/papers/2607.05511
**업보트**: 18 (2026-07-08)

> [!warning] 원문 미검증
> arXiv ID 2607.05511은 미래 시점 형식으로 원문 직접 검증 불가. 내용은 자동수집 요약 기반 추정, reliability: low.

> [!insight] 핵심 인사이트
> **장기 메모리를 가진 에이전트형 비디오 이해** 모델 — 핵심 주장은 "**reflex over reasoning**", 즉 매 프레임 무거운 추론 대신 **반사적(reflex) 처리 + 장기 메모리 참조**로 효율을 확보. [[claude-video]](자막 우선 → 필요 구간만)·[[video-use]](transcript-only)의 "영상을 통째로 추론하지 않는다" 철학과 같은 방향 — 영상 이해에서 *언제 무겁게 추론하고 언제 가볍게 넘길지*의 정책이 핵심 설계가 됨. 내 [[down-analysis]] 파이프라인의 "장면별 선택적 정밀 분석" 전략과 직결.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐ (HF ↑18 / 원문 미검증 — arXiv 2607.05511 미래형 ID)
- **즉시 활용**: NO(직접) / 개념은 즉시 참고 — "reflex over reasoning + 장기 메모리"는 down-analysis에서 토큰을 아끼는 설계 원칙으로 흡수 가능.
- **6개월 영향력**: 긴 영상 이해가 "전체 추론"에서 "메모리+선택적 반사"로 이동하면 장편 영상 분석 비용이 급감. 에이전트가 영상을 실시간으로 "지켜보는" 유스케이스 개화.
- **대체 관계**: 프레임 전량 VLM 추론을 메모리+반사 하이브리드로 대체.
- **허와 실**: "reflex"가 무엇을 놓치는지(중요 구간 누락)가 관건. 벤치 조건 확인 필요.
- **액션**: 개념(선택적 정밀 분석 정책)을 down-analysis에 반영 검토. 코드 공개 시 벤치 확인.

## 관련 페이지
- [[claude-video]] — 자막 우선·선택적 프레임 (같은 철학)
- [[video-use]] — transcript-only 영상 읽기
- [[down-analysis]] — 내 영상 분석 스킬 (직접 이식 후보)
- [[Vision-as-Unified-Multimodal-Generation]] — 통합 멀티모달 (동일 배치)
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.05511
- HF 업보트: 18 (2026-07-08)
- 신뢰도: ⭐⭐ (원문 미검증 / 자동수집 요약 기반)
