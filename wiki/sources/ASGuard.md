---
title: ASGuard — 활성화 스케일링 Jailbreak 방어 기법
type: source
domain: ai-news
tags: [ai-news, hf-paper, safety, jailbreak, activation-scaling, llm-security]
created: 2026-04-17
updated: 2026-04-17
sources: []
reliability: medium
---

# ASGuard: Jailbreak 방어를 위한 Activation-Scaling

> [!insight] 핵심 인사이트
> **활성화 스케일링(Activation Scaling)**으로 타겟형 jailbreak 공격을 방어. HF upvote 13 (2026-04-17). 성능 저하 없이 안전성 강화 — 기존 safety 기법들이 유용성을 희생했던 문제를 개선.

## 핵심 인사이트

> [!note] 배경 정보
> 모델 활성화 값을 스케일링해 특정 유해 행동 패턴을 차단. 파인튜닝이나 RLHF 없이 추론 단계에서 적용 가능한 방식으로 보임. [[GLM-5.1]], [[MiniMax-M2.7]] 같은 오픈소스 모델 배포 시 안전성 레이어로 활용 가능성.

> [!question] 미해결 질문
> 어떤 유형의 jailbreak에 효과적? 화이트박스/블랙박스 공격 모두 방어? 코드 공개?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐ — upvote 13, 학술 논문
- **즉시 활용**: NO — 구현 코드 확인 필요
- **6개월 영향력**: LLM 안전성 파이프라인의 경량 레이어로 채택 가능성
- **대체 관계**: Constitutional AI, 시스템 프롬프트 기반 방어의 보완재
- **허와 실**: "성능 저하 없이" 클레임 — 대화 품질 측면 상세 검증 필요
- **액션**: 관심 보류, 코드 공개 후 재검토

## 관련 페이지
- [[GLM-5.1]]
- [[Zhipu AI]]

## 원본
- 출처: https://huggingface.co/papers/2509.25843
- 신뢰도: ⭐⭐ (upvote 13)
