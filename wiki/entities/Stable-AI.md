---
title: Stable AI — LimiX 표형 파운데이션 모델 (Stability AI 아님)
type: entity
domain: ai-news
tags: [ai-news, entity, tabular, china, 신설]
created: 2026-09-19
updated: 2026-09-19
sources: [LimiX-2.md]
reliability: medium
---

# Stable AI

> [!warning] 🔴 **Stability AI 가 아니다** — 이름 혼동 주의
> LICENSE 원문 법인명 **稳准智能(雄安)科技有限公司** (Stable AI Technology Co., Ltd.). HF org 도 `stable-ai`(멤버 3 · 모델 5)로 `stabilityai` 와 **별개**다. 🎯 HF `organization.fullname` 만 보고 엔티티를 연결하면 틀린다 → [[메타데이터-부재-추론]]

> [!insight] 핵심 — 표형 데이터 파운데이션 모델 전문, 칭화대와 공동 연구
> [[LimiX-2]](업보트 261 · 저자 60 · 소속 표기 "Stable AI & Tsinghua University"): p(y|x) 예측을 **p(x,y) 빈칸 채우기**로 바꿔 분류·회귀·결측 보간을 한 모델로.
> 🔴 **라이선스가 닫히는 중**: LimiX-1 Apache 2.0 → LimiX-2 가중치 **비상업**(*"not an open source license"*, 파인튠·LoRA도 파생물).

## 산출물
- LimiX-16M · LimiX-2M(자사 라이선스) · [[LimiX-2]](비상업)

## 관련 페이지
- [[LimiX-2]]
- [[TabPFN]]
- [[tabfm-1.0.0]]

## 원본
- https://github.com/limix-ldm-ai/LimiX (LICENSE 법인명) · https://huggingface.co/stable-ai
- 신뢰도: ⭐⭐ (법인명 원문 확인 · 규모·자금 미확인)
