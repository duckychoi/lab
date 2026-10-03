---
title: University of Cambridge
type: entity
domain: local-llm
tags: [entity, 대학, 연구기관, distillation, rl, uk]
created: 2026-10-03
updated: 2026-10-03
sources: [On-Policy-or-Off-Policy-Distillation.md]
reliability: high
---

# University of Cambridge

> [!insight] 볼트 유입 경로
> **2026-10-03 배치 [[On-Policy-or-Off-Policy-Distillation]]** 의 소속으로 볼트에 처음 등록. HF 논문 API `organization` = **`CambUni`**(fullname: *University of Cambridge*).

## 볼트 관측 사항

- **[[On-Policy-or-Off-Policy-Distillation]]** (2609.35259 · 2026-09-28 · **upvote 130 = 10-02 게시분 2위**) — **저자 3명**.
  - 🏆 **방법론적 기여가 분명하다**: 기존 비교 연구가 *"여러 요인을 동시에 변화시켜 롤아웃 정책의 기여를 분리하기 어렵다"* 는 문제를 지적하고, **롤아웃 정책 · KL 방향 · 학습률을 독립적으로 변화**시킨 통제 실험을 설계했다.
  - 🏆 **통념을 반박한다**: *"온폴리시가 본질적으로 낫다"* 를 기각하고 **KL 방향이 성능·커버리지를, 학습률이 망각·희소성을 지배**한다고 보인다.
  - ✅ **견고성 조건을 자발 공개**(gradient clipping 제거 · 샘플링 KL 추정량 · 더 긴 추론 체인) → [[자기제한-명시]].
  - 🔴 **수치 0개 · 구현체 0건**(HF API `githubRepo`/`projectPage` 둘 다 `None`) → [[선언된-구현체-공백]] **선언 부재형**.
  - 🔴 **저자 3명 = 오늘 배치 최소 규모**다(다른 4건은 5·8·10·12명). 📌 산업 연구소 대형 저자군과 대비되는 소규모 학술 팀이 **upvote 2위**를 받았다.

> [!insight] 🎯 볼트가 이 기관에 기대할 축
> 오늘 1건으로 일반화할 수 없으나, 이 논문은 **"큰 모델을 작은 모델로 증류할 때의 설계 규칙"** 을 다룬다 — 볼트의 [[local-llm]] 도메인 핵심 관심과 정확히 겹친다. 📌 향후 같은 기관 소스가 오면 **증류/후처리 축으로 분류한다.**

## 관련 페이지
- [[On-Policy-or-Off-Policy-Distillation]]
- [[Sharpening-Tax]] — 같은 배치 · 커버리지를 같은 통화로 사용
- [[자기제한-명시]] · [[선언된-구현체-공백]]
- [[local-llm]]

## 원본
- HF 논문 API `organization.name = CambUni` / `fullname = University of Cambridge`
- 신뢰도: ⭐⭐⭐⭐ (API 1차 확인 / 🔴 PDF 미열람 — 공동 소속 유무 미확인)
