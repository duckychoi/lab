---
title: SEED — Self-Evolving On-Policy Distillation for Agentic RL
type: source
domain: ai-news
tags: [ai-news, hf-paper, on-policy-distillation, agentic-rl, self-evolving, reinforcement-learning]
created: 2026-07-17
updated: 2026-07-17
sources: [2607.14777]
reliability: medium
---

# SEED — Self-Evolving On-Policy Distillation for Agentic RL (HF 2607.14777)

> [!insight] 핵심 인사이트
> **HF 데일리 상위(upvote 51)**. 에이전트형 강화학습(agentic RL)을 위한 **자기진화 온폴리시 증류(self-evolving on-policy distillation)** 기법. [[온폴리시-증류]] 계보(DanceOPD·OPID·DOPD·Draft-OPD·Weak-to-Strong-Generalization-OPD)의 최신 항으로, "학생이 자기 궤적을 생성 → 교사 신호로 교정"하는 온폴리시 틀에 **교사/학생이 함께 진화(self-evolving)하는 루프**를 더한다. 즉 고정된 교사에 정렬하는 대신, 에이전트가 자기 경험으로 커리큘럼·교사 신호를 스스로 갱신해가며 분포 불일치를 줄이는 방향. agentic RL(다단계 도구 사용·장기 태스크)에 증류를 붙였다는 점에서 [[verifiers]]·[[Long-Horizon-Terminal-Bench]]가 진단한 "장기 에이전트 학습 난제"의 학습법 쪽 대응.

> [!warning] 신뢰도 medium — 원문 미검증
> 미래형 arXiv ID(2607.14777) 기반 자동수집으로 **초록·제목 수준만 확인**. 자기진화 루프의 구체 알고리즘·벤치마크 수치는 원문 확인 필요.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF 데일리 upvote 51로 커뮤니티 주목도는 확정. 벤치마크·구현 세부는 미검증.
- **즉시 활용**: NO — 포스트트레이닝 연구로 당장 워크플로우에 붙일 것 아님. [[온폴리시-증류]] 개념 지도의 최신 좌표로 축적.
- **6개월 영향력**: 온폴리시 증류가 단발 SFT 대체를 넘어 **에이전트 학습의 기본 레시피**로 굳는 흐름 강화. "교사도 진화한다"는 self-evolving은 초정렬([[Weak-to-Strong-Generalization-OPD]])과 맞닿음.
- **대체 관계**: 오프폴리시 SFT·고정교사 증류를 대체하는 방향. [[SkillOpt]]·[[verifiers]] 같은 스킬/검증 레이어와 상보.
- **허와 실**: "self-evolving"은 마케팅 과열 위험 용어 — 실제로 교사 신호가 무엇이고 붕괴(collapse) 없이 진화하는지 원문 검증 필요.
- **액션**: [[온폴리시-증류]] 페이지에 self-evolving 항목 연결, 원문 공개 시 알고리즘 확인.

## 관련 페이지
- [[온폴리시-증류]]
- [[Weak-to-Strong-Generalization-OPD]]
- [[DOPD]]
- [[verifiers]]
- [[Long-Horizon-Terminal-Bench]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.14777
- HF 데일리 upvote 51 (2026-07-17)
- 신뢰도: ⭐⭐ (미래형 ID·초록 수준 자동수집, 원문 미검증)
