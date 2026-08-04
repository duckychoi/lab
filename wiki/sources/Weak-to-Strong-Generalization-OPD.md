---
title: Weak-to-Strong Generalization via Direct On-Policy Distillation
type: source
domain: ai-news
tags: [ai-news, hf-paper, on-policy-distillation, weak-to-strong, alignment, training]
created: 2026-07-14
updated: 2026-07-14
sources: []
reliability: medium
---

# HF논문: Weak-to-Strong Generalization via Direct On-Policy Distillation

**HuggingFace**: https://huggingface.co/papers/2607.05394
**upvotes**: 42 · **도메인**: ai-news (+ local-llm 교차)

> [!insight] 핵심 인사이트
> **약한 교사 모델의 신호로 더 강한 학생 모델을 온폴리시 증류로 끌어올리는 weak-to-strong 일반화 기법.** 초정렬(superalignment) 난제 — "인간(약한 감독자)이 자기보다 똑똑한 모델을 어떻게 감독하나?" — 를 **직접 온폴리시 증류**로 접근한다. 학생이 스스로 생성한 샘플(on-policy)에 약한 교사의 신호를 입혀 분포 불일치를 줄이는 [[온폴리시-증류]] 클러스터의 최신 항목으로, [[DanceOPD]]·[[Trust-Region-Policy-Distillation]]과 계보를 잇는다. 핵심 반전은 **"교사가 학생보다 약해도 강한 학생을 만들 수 있다"** — 라벨 품질보다 최적화 궤적(on-policy)이 중요하다는 방향.

> [!warning] 검증 상태
> arXiv ID `2607.05394`은 미래형(2026-07)으로 원문 전문 검증 보류. 자동수집 초록 수준 요약 기반. reliability: medium.

## 도메인별 추출 (local-llm)

- **신뢰도**: ⭐⭐⭐ (HF upvotes 42, 초록 수준·미래형 ID)
- **실용성 판단**: 소형 로컬 모델을 저비용 교사로 상위 모델 튜닝 → 데이터·컴퓨트 절감 가능성. 실측 수치 미확인.
- **트레이드오프**: weak-to-strong의 상한(교사가 너무 약하면 붕괴)과 안정성은 [[Trust-Region-Policy-Distillation]] 계열의 신뢰영역 제약과 함께 봐야 함.
- **오픈소스 구현체**: 미확인(원문 공개 시 코드 여부 확인).

## 관련 페이지
- [[온폴리시-증류]] — 상위 개념(자기생성 샘플 + 교사신호)
- [[Trust-Region-Policy-Distillation]] — 같은 계열, 안정화 축
- [[DanceOPD]] — 온폴리시 증류 초기 항목
- [[local-llm]] — 로컬/효율 학습 도메인

## 원본
- 출처: https://huggingface.co/papers/2607.05394
- 신뢰도: ⭐⭐⭐ (HF upvotes 42, 초록검증·미래형 ID)
