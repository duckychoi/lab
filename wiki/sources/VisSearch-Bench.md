---
title: "VisSearch-Bench — 이미지 디테일·공간관계를 검색 결과와 엮어야 풀리는 204개 장기 과제. 16개 모델 최고도 26.47%"
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, multimodal-agent, visual-search, deep-research, ant-group]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/papers/2611.04894]
reliability: medium
---

**논문**: arXiv 2611.04894 · HF 업보트 **22**(볼트 11-08 · 수집기 17) · Ant Group · 코드 [antins-labs/VisSearch-Bench-v1](https://github.com/antins-labs/VisSearch-Bench-v1) ★61 · 라이선스 미지정

## 핵심 인사이트
> [!insight] 멀티모달 "딥 리서치"의 진짜 병목은 시각 컨텍스트 관리
> 기존 멀티모달 검색 벤치는 이미지로 엔티티만 식별하고 나머지는 텍스트 검색에 맡긴다. VisSearch-Bench 는 *외형·국소 디테일·공간관계*를 외부 정보와 엮어야 풀리게 만든 **204개 사람 작성 과제(7도메인·25하위도메인)**. 유형: Set-wise / Sequential / Hybrid Wide-Deep / Competitive Visual Disambiguation / Visual-Structure-Guided. 완전 정답(Accuracy)과 부분 정확성(Process Score)을 따로 잰다.

> [!note] 핵심 수치 1개
> **16개 멀티모달 모델 중 최고 시스템도 검색 도구 사용 시 26.47%만 완전 해결**(초록 원문 일치). 모델별 점수표·Process Score 는 미확인 — 어떤 모델이 최고인지 볼트는 모른다.

## 도메인별 추출 (ai-news)
- **즉시 활용**: NO. 다만 이미지가 섞인 리서치 자동화를 기대한다면 **현 수준이 1/4 완결**이라는 기준점.
- **6개월 영향력**: 멀티모달 에이전트 평가 축이 "인식"에서 "시각 근거 추적"으로 이동.

## 관련 페이지
- 멀티모달 에이전트
- 같은 배치: [[SLA-Spatial-Language-Action]](공간관계 축)

## 원본
- 출처: https://huggingface.co/papers/2611.04894
- 확인 범위: HF papers API 초록(볼트 11-08) · GitHub API · 본문 표 미열람
- 신뢰도: ⭐⭐
