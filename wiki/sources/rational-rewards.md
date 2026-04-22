---
title: RationalRewards — Reasoning Rewards Scale Visual Generation
type: source
domain: ai-news
tags: [ai-news, visual-generation, reasoning-rewards, rl, scaling, video-saas]
created: 2026-04-16
updated: 2026-04-16
sources: []
reliability: medium
---

# RationalRewards

> [!insight] 핵심 인사이트
> 추론 보상(Reasoning Rewards)으로 훈련 시간과 추론 시간 모두에서 시각 생성 품질을 스케일링하는 방법론. 업보트 63. "더 잘 생각하면 더 좋은 이미지/영상이 나온다" — 생성 품질의 새 스케일링 축 제시.

## 핵심 인사이트

**핵심 기여:**
- Test-time compute scaling을 시각 생성 품질 향상에 적용
- 단순 파라미터 증가 없이 추론 과정 자체를 개선해 품질 향상
- Training + Test 시간 모두에서 스케일링 가능

> [!note] 배경 정보
> [[Seedance 2.0]]과 같은 날 발표된 시각 생성 논문. 방향이 다름 — Seedance는 아키텍처/데이터 개선, RationalRewards는 보상 설계+추론 프로세스 개선.

> [!question] 미해결 질문
> Reasoning Rewards가 Diffusion 모델에도 적용 가능한가? DiT 기반 영상 생성에 test-time compute 증가가 실질적 품질 향상으로 이어지는가?

## 관련 페이지

- [[AI-영상-생성-2026]]
- [[Seedance]]
- [[SkillClaw]]

## 원본

- 출처: https://huggingface.co/papers/2604.11626
- 신뢰도: ⭐⭐ (업보트 63)
