---
title: ClawMark — 멀티턴·멀티데이·멀티모달 AI 동료 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, agent-evaluation, multimodal, multi-turn, coworker-agent]
created: 2026-04-28
updated: 2026-04-28
sources: []
reliability: medium
---

# ClawMark (HF arXiv 2604.23781, upvotes: 80)

> [!insight] 핵심 인사이트
> 현실의 지식 노동자가 AI 동료(coworker agent)와 협업하는 방식을 벤치마킹. 단순 단일 질의·응답이 아니라 "여러 날에 걸쳐, 여러 번 대화하며, 멀티모달 정보를 주고받는" 시나리오로 평가. 기존 벤치마크(단일 턴, 짧은 세션)가 실무 에이전트 성능을 과대평가하고 있다는 문제 제기.

**HuggingFace**: https://huggingface.co/papers/2604.23781  
**upvotes**: 80 (2026-04-28 기준)  
**신뢰도**: ⭐⭐⭐ — arXiv, upvotes 80으로 주목도 높음

## 핵심 인사이트

> [!note] 배경 정보
> "Multi-Turn Multi-Day Multimodal Coworker Agents" 세 가지 속성이 핵심. 현실 업무에서는 에이전트가 하루 이상에 걸쳐 작업을 이어가고, 이미지·문서 등 멀티모달 입력을 처리하며, 여러 번의 대화 턴을 통해 결과를 다듬는다. 이를 시뮬레이션하는 벤치마크.

> [!action] 당장 할 것
> [[ClawBench]](GUI 에이전트 평가)와 함께 에이전트 평가 프레임워크 선택지로 보관. 자체 에이전트 시스템 평가 시 ClawMark 태스크 유형 참고.

> [!question] 미해결 질문
> 현재 어떤 에이전트 모델이 ClawMark에서 최고 성능? [[ClawBench]]·[[gameworld]]·[[occubench]]와의 태스크 중복도는?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — arXiv 논문, 80 upvotes (ai-news 임계 충족)
- **즉시 활용**: 부분적 YES — 벤치마크 프레임워크로 자체 에이전트 평가 설계에 참고 가능
- **6개월 영향력**: 장기·멀티모달 에이전트 연구 표준 벤치마크로 자리잡을 가능성. 현재 단발성 벤치마크 과포화 상태에서 "현실성"을 강점으로 차별화
- **대체 관계**: [[ClawBench]](GUI), [[gameworld]](게임), [[DR3-Eval]](딥리서치) — 각각 다른 에이전트 유형 평가. ClawMark는 일반 지식 노동 협업에 특화
- **허와 실**: "멀티데이" 시뮬레이션이 실제 멀티데이를 얼마나 충실하게 재현하는지 검증 필요
- **액션**: 논문 전문 읽기 → 평가 태스크 종류 확인 → 자체 에이전트 평가 설계에 통합

## 관련 페이지

- [[ClawBench]]
- [[ClawGUI]]
- [[gameworld]]
- [[occubench]]
- [[AI-에이전트-프레임워크]]
- [[에이전트-메모리-레이어]]

## 원본

- 출처: https://huggingface.co/papers/2604.23781
- 신뢰도: ⭐⭐⭐
