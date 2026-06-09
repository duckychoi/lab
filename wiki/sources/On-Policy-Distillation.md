---
title: On-Policy-Distillation
type: source
domain: ai-news
tags: [knowledge-distillation, on-policy, geometry, optimization, llm-training]
created: 2026-06-09
updated: 2026-06-09
sources: []
reliability: medium
---

# On-Policy-Distillation (온폴리시 지식 증류의 기하학)

## 핵심 인사이트

> [!insight] 증류의 기하학적 분석 — 왜 온폴리시 증류가 오프폴리시보다 잘 되는지 이론화
> 온폴리시 지식 증류의 기하학적 특성을 분석. 교사-학생 분포 간 보간 경로와 최적화 지형을 이론적으로 규명. "어떻게" 증류하는지보다 "왜 작동하는지"에 집중한 이론 연구.

## 도메인별 추출

**핵심 내용:**
- HF upvotes 49
- 온폴리시 증류: 학생 모델이 자신의 출력을 기반으로 교사에게 학습
- 기하학적 분석 → 최적화 경로가 오프폴리시 대비 더 안정적임을 수학적으로 설명
- [[Qwen3.5-Claude-Distilled]] 같은 실제 증류 사례의 이론적 근거 제공

**적용 맥락:**
- [[how-to-fine-tune-reasoning-model]]의 교사-학생 SFT 전략과 이론적으로 연결
- 소형 모델 성능 향상을 위한 증류 레시피 설계에 활용 가능

## 관련 페이지
- [[Qwen3.5-Claude-Distilled]]
- [[how-to-fine-tune-reasoning-model]]
- [[Switch-KD]]

## 원본
- 출처: https://huggingface.co/papers/2606.07082
- HF upvotes 49 (2026-06-09 기준)
- 신뢰도: ⭐⭐⭐
