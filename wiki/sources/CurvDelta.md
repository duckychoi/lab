---
title: "CurvDelta — 보존 손실이 거의 안 변하는 저곡률 공간에서만 업데이트하는 LLM 적응 · 언러닝 (K-FAC · CurvLoRA · 소속 · 코드 없음)"
type: source
domain: ai-news
tags: [ai-news, paper, fine-tuning, unlearning, lora, k-fac, catastrophic-forgetting]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.24654]
reliability: low
---

**논문**: arXiv 2611.24654 · 업보트 26(볼트 · 수집기 일치) · HF 조직 없음 · 저자 6 · 코드 없음(`githubRepo` null)

## 핵심 인사이트
> [!insight] 보존을 손실 항이 아니라 "업데이트가 움직일 수 있는 방향"에 넣는다
> LLM 적응 시 목표 능력은 얻지만 일반 능력이 무너지는 문제. 사전 모델 주변에서 보존 손실의 국소 기하를 분석해 업데이트해도 보존 손실이 거의 변하지 않는 저곡률 공간을 만들고, K-FAC 근사와 인수분해 투영으로 LLM 규모에서 실용화. 저랭크 변형 CurvLoRA 제안.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐ — 소속 표기 없음 · 코드 없음 · 초록 수치 0.
- **즉시 활용**: NO(코드 없음).
- **6개월 영향력**: 로컬 모델 파인튜닝에서 "특화하면 일반 능력이 준다"([[특화-역류]])에 대한 구조적 처방. 언러닝(TOFU · MUSE)까지 같은 틀로 다룬다.
- **대체 관계**: [[PROLA]] (주성분/직교 LoRA)와 같은 "어느 부분공간을 건드릴지" 계열.
- **허와 실**: 수학 추론 · 코드 생성에서 목표 성능은 **"경쟁적"** = 최고가 아니다. 이점은 보존 쪽. 언러닝 유지 성능은 재학습 기준에 "근접".
- **액션**: 없음.

## 관련 페이지
- [[PROLA]] · [[특화-역류]] · [[한정어-탈락]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.24654
- 확인 범위: HF papers API(초록 전문 — K-FAC · CurvLoRA · TOFU · MUSE 확인 · 조직 없음 · githubRepo null) · 🔴 본문 미열람
- 신뢰도: ⭐⭐
