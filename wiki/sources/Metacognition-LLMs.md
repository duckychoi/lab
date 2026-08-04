---
title: Metacognition in LLMs — 메타인지(자기 지식·불확실성) 연구 서베이
type: source
domain: ai-news
tags: [ai-news, hf-paper, survey, metacognition, calibration, uncertainty, self-knowledge, agent-safety]
created: 2026-07-15
updated: 2026-07-15
sources: []
reliability: medium
---

# Metacognition in LLMs: Foundations, Progress, and Opportunities

> [!insight] 핵심 인사이트
> HF 추천 14 (2026-07-14 미수집분 보충, 2026-07-15 처리). **LLM의 "메타인지" — 자기가 무엇을 아는지/모르는지, 답이 얼마나 확실한지를 인식하는 능력 — 을 정리한 서베이.** 자기평가(self-assessment)·캘리브레이션(confidence가 실제 정확도와 맞는가)·한계 인식(모르면 모른다고 하기) 세 축으로 연구 지형을 종합한다. 이 위키를 관리하는 무인 에이전트 관점에서 정확히 이 능력이 핵심 — CLAUDE.md의 제1 원칙("모르면 모른다고 말한다, 추측과 사실을 구분한다")이 곧 메타인지의 실천이다. [[destructive_command_guard]]가 *행동*의 seatbelt라면, 메타인지는 *발화·주장*의 seatbelt(환각·과신 방지). 자동 인제스트가 미검증 초록을 "reliability medium"으로 표시하는 것도 캘리브레이션의 한 형태.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF 추천 14, 서베이 성격. 미래형 ID(2607.11881)로 초록 수준 자동수집 기반·원문 미검증(reliability medium).
- **즉시 활용**: MAYBE — 위키 인제스트·쿼리 응답에서 "확신도 명시·불확실 표기" 관행의 이론적 근거로 채용. 자동 파이프라인의 신뢰도 라벨링(⭐·medium/low)을 캘리브레이션 프레임으로 재정비.
- **6개월 영향력**: 에이전트 신뢰성 논의가 "정확도"에서 "자기 확신의 정직성(캘리브레이션)"으로 확장. 무인 에이전트 안전의 소프트 레이어.
- **대체 관계**: 외부 가드(하드 차단)와 상보 — 모델 내부의 자기검열(불확실할 때 유보). 하드 seatbelt를 못 잡는 "그럴듯한 오답"을 방어.
- **허와 실**: 서베이는 방향 제시일 뿐 즉효 기법은 아님. "메타인지 있다"는 주장과 실제 캘리브레이션 수치는 별개.
- **액션**: 위키 인제스트 규칙에 "확신 없으면 명시적 유보·reliability 하향" 체크를 메타인지 관점으로 재확인(이미 부분 적용 중).

## 관련 페이지
- [[destructive_command_guard]]
- [[LLM-Wiki]]
- [[Metacognition-LLMs]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.11881
- HF 추천: 14 (2026-07-14, 미수집분 보충)
- 신뢰도: ⭐⭐ (미래형 ID·초록 수준 자동수집, 원문 미검증)
